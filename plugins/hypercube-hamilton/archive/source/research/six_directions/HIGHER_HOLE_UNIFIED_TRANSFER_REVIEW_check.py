"""Independent finite sanity checks; not a census or replacement for the proof."""
import hashlib, itertools, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def edge(a,b): return tuple(sorted((a,b)))

rows = [(5,1,2,2,(3,3),0),(5,2,3,3,(2,2),0),
        (5,2,2,2,(2,4),1),(5,3,3,3,(1,3),1),
        (5,1,3,2,(4,2),1),(5,2,4,3,(3,1),1),
        (5,4,3,3,(0,4),2),(5,2,5,3,(4,0),2),
        (6,2,3,3,(3,3),0),(6,3,3,3,(2,4),1),
        (6,2,4,3,(4,2),1)]
table=[]
for k,a,b,q,want,omit in rows:
    if a+1>=b:
        s=a+1-b
        got=(k-a-1,k-b+s)
        assert 1<=b<=3 and s<=a and q==b and omit==s
        parity='odd'
    else:
        t=b-a-1
        got=(k-a-1+t,k-b)
        assert 0<=a<=2 and a>=1 and q==a+1 and omit==t
        parity='even'
    assert got==want
    table.append(dict(k=k,a=a,b=b,A_balanced=q,B_holes=got,omitted=omit,omitted_parity=parity))

# Exact cardinality identities on every feasible short-cut parity population.
population_count=0
empty_D_count=0
for k in range(1,33):
  for a in range(k):
    for b in range(k+1):
      for delta in (0,1):
        for mA in range(17):
          pE,pO=16-a-delta-mA,16-b-mA
          hBE,hBO=k-a-delta,k-b
          mBE,mBO=16-hBE-pO,16-hBO-pE
          if min(pE,pO,hBE,hBO,mBE,mBO)<0 or mBE!=mBO or pE+pO==0:
            continue
          c=pE+pO
          assert c%2==(a+delta+b)%2
          assert pE-pO==b-a-delta
          if 1<=b<=3 and a+1-b>=0:
            s=a+1-b
            assert s<=a
            if delta:
              dverts=c+s
              AE,AO=a+1-s,b
            elif s:
              dverts=c+s-1
              AE,AO=a-s+1,b
            else:
              assert pE>=1
              dverts=c-1
              AE,AO=a+1,b
            assert dverts%2==0 and (AE,AO)==(b,b)
            assert (hBE-(1-delta),hBO+s)==(k-a-1,k-b+s)
            assert not delta or dverts>0
            population_count+=1
            empty_D_count+=dverts==0
          if 0<=a<=2 and b-a-1>=1:
            t=b-a-1
            assert b-t==a+1
            if delta:
              dverts=c+t
            else:
              assert pE>=t+1
              dverts=c-1+t
            assert dverts%2==0
            assert (a+1,b-t)==(a+1,a+1)
            assert (hBE-(1-delta)+t,hBO)==(k-a-1+t,k-b)
            assert dverts>0
            population_count+=1

def adjacency(edges):
    adj={}
    for a,b in edges:
        assert a!=b
        adj.setdefault(a,[]).append(b)
        adj.setdefault(b,[]).append(a)
    return adj

def components(edges):
    adj=adjacency(edges)
    seen=set(); out=[]
    for start in adj:
        if start in seen: continue
        todo=[start]; group=set()
        while todo:
            v=todo.pop()
            if v in group: continue
            group.add(v); todo.extend(adj[v])
        seen|=group; out.append(group)
    return adj,out

skeletons=0; selected_target_port=0; tagged_conflicts=0; double_conflicts=0
for n in range(4,11):
  all_A={edge(i,i+1) for i in range(n-1)}
  # D cannot touch the free A root; it can touch the odd target.
  for mask in range(1<<(n-2)):
    deleted=[i+1 for i in range(n-2) if mask>>i&1]
    if any(j==i+1 for i,j in zip(deleted,deleted[1:])): continue
    D={edge(i,i+1) for i in deleted}
    ports=sorted({v for e in D for v in e})
    for delta in (0,1):
      if delta and not D: continue
      attachment=ports+([] if delta else [0])
      leaves={v:100+v for v in attachment}
      u=0 if delta else 200
      tag=edge(u,n-1)
      forest=(all_A-D)|{edge(v,w) for v,w in leaves.items()}|{tag}
      adj,groups=components(forest)
      endpoints=set(leaves.values())|({u} if not delta else set())
      T={}; tagT=None
      for group in groups:
        assert sum(len(adj[v]) for v in group)//2==len(group)-1
        ends=[v for v in group if len(adj[v])==1]
        assert len(ends)==2 and set(ends)<=endpoints
        cur,stop=ends; previous=None; path=[cur]
        while cur!=stop:
            nxt=next(x for x in adj[cur] if x!=previous)
            previous,cur=cur,nxt; path.append(cur)
        e=edge(*ends); T[e]=path
        if set(tag)<=group:
            assert tagT is None; tagT=e
      assert tagT is not None and {v for e in T for v in e}==endpoints
      # Enumerate all conflict placements. These include more patterns than
      # actual same-parity Y can realize, so no parity feasibility is assumed.
      candidates=sorted(leaves.values())
      for ymask in range(1<<len(candidates)):
        Y={v for j,v in enumerate(candidates) if ymask>>j&1}
        mates={y:300+y for y in Y}
        MB={edge(y,h) for y,h in mates.items()}|{(500,501)}
        combined=set(T)|MB
        cadj,cgroups=components(combined)
        L={}; expanded_paths={}
        for group in cgroups:
            assert sum(len(cadj[v]) for v in group)//2==len(group)-1
            ends=[v for v in group if len(cadj[v])==1]
            assert len(ends)==2
            assert {v for v in group if len(cadj[v])==2}<=Y
            start,stop=ends; cur=start; prev=None; path=[cur]
            while cur!=stop:
                nxt=next(x for x in cadj[cur] if x!=prev)
                prev,cur=cur,nxt; path.append(cur)
            e=edge(start,stop); L[e]=path
            full=[path[0]]
            for x,z in zip(path,path[1:]):
                sub=T.get(edge(x,z),[x,z])
                if sub[0]!=x: sub=list(reversed(sub))
                full+=sub[1:]
            expanded_paths[e]=full
        assert all(v not in Y for e in L for v in e)
        assert len({v for e in L for v in e})==2*len(L)
        assert {v for e in combined for v in e}-{v for e in L for v in e}==Y
        assert sum(tag in {edge(x,z) for x,z in zip(p,p[1:])} for p in expanded_paths.values())==1
        # Make a cycle containing L using matched pairs as blocks and two
        # extra singleton B holes. Expand all paths and remove the true tag.
        blocks=[list(e) for e in L]+[[600],[601]]
        order=[v for block in blocks for v in block]
        cyc={edge(x,z) for x,z in zip(order,order[1:]+order[:1])}
        assert set(L)<=cyc
        for e,p in expanded_paths.items():
            cyc.remove(e)
            cyc|={edge(x,z) for x,z in zip(p,p[1:])}
        assert tag in cyc
        out=cyc-{tag}
        oadj,ogroups=components(out)
        assert len(ogroups)==1
        assert {v for v in oadj if len(oadj[v])==1}=={u,n-1}
        assert all(len(oadj[v]) in (1,2) for v in oadj)
        assert set(range(n))<=set(oadj) and Y<=set(oadj)
        assert MB<=out and (all_A-D)<=out
        skeletons+=1
        selected_target_port+=n-1 in ports
        tagged_conflicts+=any(v in Y for v in tagT)
        double_conflicts+=any(set(e)<=Y for e in T)

result={"status":"PASS","table_rows":table,"feasible_population_branch_checks":population_count,
        "empty_D_population_checks":empty_D_count,"abstract_path_skeleton_checks":skeletons,
        "covered_target_port_checks":selected_target_port,"tag_incident_conflict_checks":tagged_conflicts,
        "two_Y_endpoints_on_one_transfer_edge_checks":double_conflicts,
        "scope":"Finite boundary checks only; universal forest proof is reviewed separately. No higher-hole geometry census or old certificate recertification."}
conditional=[]
for k,a,b in [(5,3,2),(5,1,4),(6,4,3),(6,2,5)]:
    even=a+1>=b
    consumed=a+1-b if even else b-a-1
    got=(k-a-1,k-b+consumed) if even else (k-a-1+consumed,k-b)
    assert consumed==2 and got in ((1,5),(5,1))
    conditional.append(dict(k=k,a=a,b=b,B_holes=got,omitted=consumed,requires_marked_geometry=True))
result['conditional_T15_rows']=conditional
def sha(path): return 'sha256:'+hashlib.sha256(path.read_bytes()).hexdigest()
review_names=['EIGHT_HOLE_FULL_REVIEW.json','A6_CLOSURE_REVIEW.json',
              'EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW.json',
              'T44_Q5_CLOSURE_REVIEW.json','CANONICAL_COMPLETION_REVIEW.json',
              'GENERAL_NEAR_PERFECT_REVIEW.json']
sources=['HIGHER_HOLE_UNIFIED_TRANSFER.md','EIGHT_HOLE_FULL_CLOSURE.md',
         'EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md','A6_AND_EIGHT_FREE_CLOSED.md',
         'A6_CLOSURE_DRAFT.md','CANONICAL_A4_CLOSURE.md','GENERAL_NEAR_PERFECT.md',
         'T44_Q5_CLOSURE_DRAFT.md']
result['imported_reports']={}
hash_checks=0
for name in review_names:
    report=json.loads((ROOT/name).read_text(encoding='utf-8-sig'))
    assert report['verdict']=='PASS', (name,report['verdict'])
    result['imported_reports'][name]={'verdict':report['verdict'],'source_hash_checks':[]}
    for key in ('audited_input_hashes','imported_dependency_hashes'):
        for source in sources:
            recorded=report.get(key,{}).get(source)
            if recorded is not None:
                assert recorded.removeprefix('sha256:')==sha(ROOT/source).removeprefix('sha256:'), (name,source)
                result['imported_reports'][name]['source_hash_checks'].append(source)
                hash_checks+=1
result['import_source_hash_comparisons']=hash_checks
result['audited_input_hashes']={'HIGHER_HOLE_UNIFIED_TRANSFER.md':sha(ROOT/'HIGHER_HOLE_UNIFIED_TRANSFER.md')}
result['imported_dependency_hashes']={name:sha(ROOT/name) for name in sources[1:]+review_names}
(ROOT/'HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='table_rows'},indent=2))
