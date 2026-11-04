"""Independent first-orbit geometry and two-bridge topology verification."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib,json
P=Path(__file__).resolve().parent
def sha(n):return 'sha256:'+hashlib.sha256((P/n).read_bytes()).hexdigest()
def edge(a,b):return tuple(sorted((a,b)))
def forest(edges,ends,interior):
    adj={}
    for a,b in edges:
        assert a!=b
        adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
    assert all(len(n)<=2 for n in adj.values())
    assert {x for x,n in adj.items() if len(n)==1}==ends
    assert all(len(adj[x])==2 for x in interior)
    unseen=set(adj)
    while unseen:
        stack=[next(iter(unseen))];part=set()
        while stack:
            x=stack.pop()
            if x in part:continue
            part.add(x);stack.extend(adj[x]-part)
        unseen-=part
        assert len(part&ends)==2

# All classifications of the four candidate mirrors, all permitted mutual
# internal required edges, every feasible even crossing count.
selection_checks=0
for c in range(0,11,2):
    for bits in range(16):
        ports={i for i in range(4) if bits&(1<<i)}
        if len(ports)>c:continue
        internal=set(range(4))-ports
        pairs=list(combinations(sorted(internal),2))
        for b in range(1<<len(pairs)):
            F={pairs[j] for j in range(len(pairs)) if b&(1<<j)}
            vertices=[x for e in F for x in e]
            if len(set(vertices))!=len(vertices):continue
            choices=[]
            for t,s in combinations(range(4),2):
                p=len({t,s}&ports)
                allowed=(ports and internal and p==1) or (not ports and (t,s) not in F) or (len(ports)==4)
                if allowed:
                    assert (c+2)//2>p
                    if p==0:assert (t,s) not in F
                    choices.append((t,s))
            assert choices
            selection_checks+=1

# Every cyclic order of all deleted gap endpoints on an abstract15-cycle.
cycle={edge(i,(i+1)%15) for i in range(15)}
checks=Counter();matching_sizes=Counter()
for bits in range(1,1<<15):
    if bits&(bits<<1) or (bits&1 and bits&(1<<14)):continue
    D={edge(i,(i+1)%15) for i in range(15) if bits&(1<<i)}
    d=len(D);c=2*d-2
    if c>10:continue
    endpoints={x for e in D for x in e};matching_sizes[d]+=1
    mate={a:b for a,b in D}|{b:a for a,b in D}
    for t,s in combinations(sorted(endpoints),2):
        # p0: internal mirrors deliberately not paired in original F_B.
        w,z,k,l=500,501,502,503
        other=endpoints-{t,s};bports={100+x for x in other}
        graph=(cycle-D)|{edge(x,100+x) for x in other}|{edge(t,w),edge(s,z),edge(w,k),edge(z,l)}
        forest(graph,bports|{k,l},set(range(15))|{w,z})
        checks['both_internal_unpaired']+=1
        if mate[t]==s:continue
        # p1: t mirror is a port with actual required A partner mate[t].
        x=mate[t];other=endpoints-{t,s,x}
        graph=(cycle-D)|{edge(y,100+y) for y in other}|{edge(t,w),edge(x,w),edge(s,z),edge(z,l)}
        forest(graph,{100+y for y in other}|{l},set(range(15))|{w,z})
        checks['one_port_one_internal']+=1
        if d<3:
            checks['two_ports_restore_all_gaps_excluded']+=1
            continue
        y=mate[s];other=endpoints-{t,s,x,y}
        graph=(cycle-D)|{edge(q,100+q) for q in other}|{edge(t,w),edge(x,w),edge(s,z),edge(y,z)}
        forest(graph,{100+q for q in other},set(range(15))|{w,z})
        checks['both_ports_at_least_one_gap_remains']+=1

# Direct geometry condition on all160 existing residual members. Adjacent
# swaps, not the producer's120 permutation minimization, expand the first orbit.
def swap(x,i):return x^(3<<i) if ((x>>i)^(x>>(i+1)))&1 else x
seed=((3,5,6,15),(8,25,26));images={seed};todo=[seed]
while todo:
    a,b=todo.pop()
    for i in range(4):
        g=(tuple(sorted(swap(x,i) for x in a)),tuple(sorted(swap(x,i) for x in b)))
        if g not in images:images.add(g);todo.append(g)
assert len(images)==60
given=json.loads((P/'A8_geometry_census.json').read_text())
residual={(tuple(r['Z']),tuple(r['W'])) for g in given['residual_orbits'] for r in g['members']}
condition=set();geometry_witnesses=[]
for a,b in residual:
    good=[i for i in range(5) if all(x&(1<<i)==0 for x in (0,)+a) and sum(x&(1<<i)==0 for x in b)==1]
    if good:
        condition.add((a,b));geometry_witnesses.append({'Z':list(a),'W':list(b),'cut':good[0]})
assert condition==images and len(residual-images)==100
assert [g['size'] for g in given['residual_orbits'][1:]]==[20,30,30,20]

deps=['Q4_GENERAL_AUGMENTATION.md','Q4_TWO_AVOIDED_TRANSFER.md','Q4_TWO_AVOIDED_REVIEW.md','Q4_TWO_AVOIDED_REVIEW.json',
 'A6_CLOSURE_DRAFT.md','A6_CLOSURE_REVIEW.md','A6_CLOSURE_REVIEW.json',
 'A8_PARTIAL_PROOF_PACKAGE.md','A8_geometry_census.py','A8_geometry_census.json','A8_PARTIAL_REVIEW.md','A8_PARTIAL_REVIEW.json']
hashchecks=0
for name in ['Q4_TWO_AVOIDED_REVIEW.json','A6_CLOSURE_REVIEW.json','A8_PARTIAL_REVIEW.json']:
    report=json.loads((P/name).read_text(encoding='utf8'));assert report['verdict']=='PASS'
    for field in ['audited_input_hashes','imported_dependency_hashes']:
        for n in deps:
            h=report.get(field,{}).get(n)
            if h:
                assert sha(n).removeprefix('sha256:')==h.removeprefix('sha256:')
                hashchecks+=1
out={'status':'PASS','audited_input_hashes':{'A8_DELTA4_FIRST_ORBIT.md':sha('A8_DELTA4_FIRST_ORBIT.md')},
 'imported_dependency_hashes':{n:sha(n) for n in deps},
 'checker_source_hash':sha('A8_DELTA4_FIRST_ORBIT_REVIEW_check.py'),
 'candidate_mirror_classification_checks':selection_checks,
 'cycle_deleted_matching_sizes':dict(sorted(matching_sizes.items())),
 'abstract_transfer_topology_checks':dict(checks),
 'complete_residual_first_orbit':60,'partial_package_residual':160,'combined_remaining':100,
 'combined_remaining_orbit_sizes':[20,30,30,20],
 'all_condition_geometries_equal_first_orbit':True,
 'geometry_cut_witnesses':sorted(geometry_witnesses,key=lambda r:(r['Z'],r['W'])),
 'recorded_import_hash_comparisons':hashchecks,
 'producer_modules_imported_or_executed':False,'full_A8_proved':False,'full_P6_proved':False}
(P/'A8_DELTA4_FIRST_ORBIT_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ('imported_dependency_hashes','geometry_cut_witnesses')},indent=2))
