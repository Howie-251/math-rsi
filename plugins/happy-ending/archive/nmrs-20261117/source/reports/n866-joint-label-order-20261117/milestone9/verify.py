#!/usr/bin/env python3
"""Standalone semantic reconstruction and actual proof replay of the nine-hole milestone."""
import argparse,collections,hashlib,itertools as it,json,pathlib,platform,subprocess,time
assert platform.system()=='Linux'
pa=argparse.ArgumentParser();pa.add_argument('--directory',required=True);pa.add_argument('--checker',default='/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim');args=pa.parse_args();root=pathlib.Path(args.directory);began=time.monotonic();meta=json.loads((root/'metadata.json').read_text());W=list(map(tuple,meta['universe']['subsets']));H=list(map(tuple,meta['universe']['column_heights']));assert W==list(it.combinations(range(1,9),4)) and H==[tuple(w[3-j]-(4-j) for j in range(4)) for w in W]
cells=[frozenset((x,y) for x in range(1,5) for y in range(1,h[x-1]+1)) for h in H];lookup={c:i for i,c in enumerate(cells)};wi={w:i for i,w in enumerate(W)};transpose={i:lookup[frozenset((y,x) for x,y in c)] for i,c in enumerate(cells)}
assert all(transpose[i]==wi[tuple(sorted(9-v for v in set(range(1,9))-set(W[i])))] for i in range(70))
def loadcnf(p):
    lines=p.read_text().splitlines();return [list(map(int,l.split()))[:-1] for l in lines if l and l[0] not in 'cp']
def prove(cnf,proof):
    p=subprocess.run([args.checker,str(cnf),str(proof)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=15);assert p.returncode==0 and 's VERIFIED' in p.stdout
cycles=json.loads((root/'cycles.json').read_text());baseline=[];six_checks=0
for cy in cycles:
    assert len(cy)==8 and len(set(cy))==8
    for tri in it.combinations(cy,3):
        for pi in it.permutations(range(3)):
            a,b,c=[tri[j] for j in pi];ab=cells[b]-cells[a];bc=cells[c]-cells[b];ac=cells[c]-cells[a]
            if not ab or not bc or not ac:continue
            coordinate=sum(pi[i]>pi[j] for i in range(3) for j in range(i+1,3))%2
            assert max(p[coordinate] for p in bc)<=min(p[coordinate] for p in ab);six_checks+=1
    baseline.append(tuple(sorted(cy)))
pivot_branches=0
for O in it.combinations(range(2,8),4):
    faces=[set(O)-{v} for v in reversed(O)];starts=[wi[tuple(sorted(f|{1}))] for f in faces];ends=[wi[tuple(sorted(f|{8}))] for f in faces];red=[]
    for k in (0,3):
        A,B=H[starts[k]],H[ends[k]];path=[lookup[frozenset((x,y) for x in range(1,5) for y in range(1,max(A[x-1],min(B[x-1],h))+1))] for h in range(5)];assert len(set(path))==5
        differences=[cells[b]-cells[a] for a,b in zip(path,path[1:])];assert all(differences) and all(max(x for x,y in q)<=min(x for x,y in p) for p,q in zip(differences,differences[1:]));red.append(path)
    support=set(starts+ends+red[0][1:-1]+red[1][1:-1]);assert len(support)==13;pivot=(starts[3],ends[0]);domain=cells[pivot[1]]-cells[pivot[0]];assert {x for x,y in domain}=={1,4}
    for label in domain:
        blue=starts+[ends[0]] if label[0]==4 else [starts[3]]+ends;R=red[0] if label[0]==4 else red[1];assert (blue[0],blue[-1])==(R[0],R[-1]) and len(set(blue)|set(R))==8
        differences=[{label} if (a,b)==pivot else cells[b]-cells[a] for a,b in zip(blue,blue[1:])];assert all(differences) and all(max(y for x,y in q)<=min(y for x,y in p) for p,q in zip(differences,differences[1:]));pivot_branches+=2
    baseline.extend([tuple(sorted(support)),tuple(sorted(transpose[v] for v in support))])
assert len(set(baseline))==93 and set(baseline)=={tuple(r['support']) for r in meta['rows']}
names={i+1:('hole',i) for i in range(70)};L={};C={};R4={};R5={}
for r in meta['labels']:
    a,b=r['pair'];assert cells[a]<cells[b] and {tuple(c['cell']) for c in r['choices']}==cells[b]-cells[a]
    for c in r['choices']:names[c['variable']]=('label',a,b,tuple(c['cell']));L[a,b,tuple(c['cell'])]=c['variable']
for r in meta['colors']:
    a,b,c=r['triple'];assert cells[a]<cells[b]<cells[c];names[r['variable']]=('color',a,b,c);C[a,b,c]=r['variable']
for group,D in [('reach4',R4),('reach5',R5)]:
    for r in meta[group]:names[r['variable']]=(group,*r['key']);D[tuple(r['key'])]=r['variable']
def meaning_clause(clause,allowed):
    descriptions=[(l,names[abs(l)]) for l in clause];kinds=collections.Counter(d[0] for l,d in descriptions)
    for l,d in descriptions:
        physical=[d[1]] if d[0]=='hole' else list(d[1:-1]) if d[0] in ('label','reach4','reach5') else list(d[1:])
        assert set(physical)<=allowed
    if kinds=={'hole':1}:assert len(clause)==1 and clause[0]<0;return 'occupied'
    if set(kinds)=={'label'}:
        params=[d for l,d in descriptions];pair=params[0][1:3];assert all(d[1:3]==pair for d in params)
        if all(l>0 for l,d in descriptions):assert set(clause)=={v for (a,b,c),v in L.items() if (a,b)==pair};return 'label_some'
        assert len(clause)==2 and all(l<0 for l,d in descriptions) and len(set(clause))==2;return 'label_unique'
    h=[d[1] for l,d in descriptions if d[0]=='hole'];assert all(l>0 for l,d in descriptions if d[0]=='hole')
    if kinds=={'hole':3,'label':2,'color':1}:
        label=[(l,d) for l,d in descriptions if d[0]=='label'];assert all(l<0 for l,d in label);col=next((l,d) for l,d in descriptions if d[0]=='color');a,b,c=col[1][1:];assert set(h)=={a,b,c}
        first=next(d[3] for l,d in label if d[1:3]==(a,b));second=next(d[3] for l,d in label if d[1:3]==(b,c));coordinate=0 if col[0]>0 else 1;assert second[coordinate]<=first[coordinate];return 'growth'
    if kinds=={'hole':4,'color':4}:
        a,b,c,d=sorted(h);assert cells[a]<cells[b]<cells[c]<cells[d];ordered=[C[t] for t in ((a,b,c),(a,b,d),(a,c,d),(b,c,d))];bits=[-v in clause for v in ordered];assert all(v in clause or -v in clause for v in ordered) and sum(x!=y for x,y in zip(bits,bits[1:]))>1;return 'packet'
    if kinds=={'hole':4,'color':2,'reach4':1}:
        atom=next((l,d) for l,d in descriptions if d[0]=='reach4');assert atom[0]>0;a,u,v,color=atom[1][1:];t=next(iter(set(h)-{a,u,v}));assert set(h)=={a,t,u,v} and cells[a]<cells[t]<cells[u]<cells[v];sign=-1 if color else 1;assert sign*C[a,t,u] in clause and sign*C[t,u,v] in clause;return 'path4'
    if kinds=={'hole':1,'color':1,'reach4':1,'reach5':1}:
        four=next((l,d) for l,d in descriptions if d[0]=='reach4');five=next((l,d) for l,d in descriptions if d[0]=='reach5');assert four[0]<0 and five[0]>0;a,t,u,color=four[1][1:];v=h[0];assert five[1][1:]==(a,v,color) and cells[a]<cells[t]<cells[u]<cells[v];assert (-1 if color else 1)*C[t,u,v] in clause;return 'path5'
    assert kinds=={'reach5':2} and all(l<0 for l,d in descriptions);params=[d[1:] for l,d in descriptions];assert params[0][:2]==params[1][:2] and {p[-1] for p in params}=={0,1};return 'no_joint5'
kernel_index=json.loads((root/'kernels/index.json').read_text());row_set=set(baseline);summaries=[]
for k in kernel_index:
    allowed=set(k['support']);clauses=loadcnf(root/'kernels'/k['cnf']);kinds=collections.Counter(meaning_clause(c,allowed) for c in clauses);assert {(-c[0]-1) for c in clauses if len(c)==1 and -70<=c[0]<=-1}==allowed
    prove(root/'kernels'/k['cnf'],root/'kernels'/k['proof']);row_set.add(tuple(sorted(allowed)));row_set.add(tuple(sorted(transpose[v] for v in allowed)));summaries.append(dict(name=k['name'],support=len(allowed),clauses=len(clauses),types=dict(kinds)))
rows=json.loads((root/'rows.json').read_text());assert len(rows)==115 and {tuple(r['support']) for r in rows}==row_set and all(r['rhs']==1 for r in rows)
budget=json.loads((root/'matrix/result.json').read_text());assert budget['budget']==8 and budget['status']=='CHECKED_UNSAT';counter={};nextvar=70
for i in range(1,71):
    for j in range(1,min(i,9)+1):nextvar+=1;counter[i,j]=nextvar
expected=[[v+1 for v in r['support']] for r in rows]
for i in range(1,71):
    expected.append([-i,counter[i,1]])
    for j in range(1,10):
        if (i-1,j) in counter:expected.append([-counter[i-1,j],counter[i,j]])
    for j in range(2,10):
        if (i,j) in counter:expected.append([-i,-counter[i-1,j-1],counter[i,j]])
expected.append([-counter[70,9]]);assert loadcnf(root/'matrix/formula.cnf')==expected;assert hashlib.sha256((root/'matrix/formula.cnf').read_bytes()).hexdigest()==budget['cnf_sha256'];assert hashlib.sha256((root/'matrix/proof.drat').read_bytes()).hexdigest()==budget['proof_sha256'];prove(root/'matrix/formula.cnf',root/'matrix/proof.drat')
cover=json.loads((root/'nine-holes.json').read_text());holes=cover['holes'];assert len(set(holes))==len(holes)==9 and all(set(holes)&set(r['support']) for r in rows)
two=json.loads((root/'two-label/result.json').read_text());core=loadcnf(root/two['core_file']);two_cnf=loadcnf(root/'two-label/formula.cnf');a,b=two['pair'];variables=two['variables'];assert cells[b]-cells[a]==set(map(tuple,two['cells'])) and set(variables)=={L[a,b,tuple(c)] for c in two['cells']};assert two_cnf==core+[variables]
for branch in two['branches']:
    values={branch['assumption']:True}
    for step in branch['trace']:
        u=step['literal'];clause=core[step['clause']];assert u in clause and abs(u) not in values and all(abs(l) in values and values[abs(l)]!=(l>0) for l in clause if l!=u);values[abs(u)]=u>0
    assert all(abs(l) in values and values[abs(l)]!=(l>0) for l in core[branch['conflict']])
prove(root/'two-label/formula.cnf',root/'two-label/proof.drat')
result=dict(host=platform.node(),status='PASS',baseline_rows=93,six_order_checks=six_checks,pivot_cell_branches=pivot_branches,kernels=summaries,checked_matrix_rows=len(rows),checked_budget8_unsat=True,verified9_hole_vector=holes,exact_matrix_minimum=9,two_cell_pair=[W[a],W[b]],two_cells=two['cells'],two_branch_unit_replay=True,two_label_proof_additions=3,seconds=time.monotonic()-began)
(root/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
