#!/usr/bin/env python3
"""Linux-only shared-pivot rows joined to the complete 63 cycle supports."""
import collections,hashlib,itertools as it,json,pathlib,platform,sys,time
assert platform.system()=='Linux'
root=pathlib.Path(__file__).resolve().parent;source=root.parent/'first';out=root/'first';out.mkdir(exist_ok=False);began=time.monotonic()
def dump(name,x):(out/name).write_text(json.dumps(x,indent=2)+'\n')
U=json.loads((source/'universe.json').read_text());W=list(map(tuple,U['subsets']));index={w:i for i,w in enumerate(W)};assert len(W)==70
cycles=json.loads((source/'cycles.json').read_text());rows=[]
for i,cy in enumerate(cycles):rows.append(dict(kind='certified_cycle',key=i,support=sorted(cy),rhs=len(cy)-7))
I=set(range(2,8));all_coords=set(range(1,9))
for Omega in it.combinations(range(2,8),4):
    descending=tuple(reversed(Omega));faces=[set(Omega)-{v} for v in descending]
    private={index[tuple(sorted(C|{end}))] for C in faces for end in (1,8)}
    internal={index[w] for w in it.combinations(range(2,8),4) if faces[0]<=set(w) or faces[3]<=set(w)}
    support=private|internal;assert len(private)==8 and len(internal)==5 and len(support)==13
    for transpose in (False,True):
        transported={index[tuple(sorted(9-v for v in all_coords-set(W[s])))] for s in support} if transpose else support
        rows.append(dict(kind='shared_pivot',Omega=Omega,transpose=transpose,support=sorted(transported),rhs=1))
rows.append(dict(kind='imported_total_holes_at_least_7',support=list(range(70)),rhs=7))
dump('rows.json',rows);old=json.loads((source/'cover_10.json').read_text())['holes'];cut=[i for i,r in enumerate(rows) if len(set(old)&set(r['support']))<r['rhs']]
dump('old-mask-regression.json',dict(holes=old,violated_rows=cut,violations=[rows[i] for i in cut]))
import numpy as np,scipy
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csr_matrix
rr=[];cc=[]
for i,r in enumerate(rows):
    for j in r['support']:rr.append(i);cc.append(j)
A=csr_matrix((np.ones(len(rr)),(rr,cc)),shape=(len(rows),70));rhs=np.array([r['rhs'] for r in rows],float)
mi=milp(np.ones(70),integrality=np.ones(70),bounds=Bounds(0,1),constraints=LinearConstraint(A,rhs,np.inf),options={'time_limit':20})
result=dict(host=platform.node(),source_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),scipy=scipy.__version__,rows=len(rows),kind_counts=dict(collections.Counter(r['kind'] for r in rows)),milp_status=int(mi.status),message=mi.message,raw_optimization_is_not_an_infeasibility_proof=True,old_mask_violations=len(cut))
if mi.x is not None:
    holes=[i for i,v in enumerate(mi.x) if v>.5];assert all(len(set(holes)&set(r['support']))>=r['rhs'] for r in rows)
    dump('cover.json',dict(holes=holes,subsets=[W[i] for i in holes]));result['holes']=len(holes);result['exact_matrix_minimum_from_explicit_7_row_and_7_witness']=len(holes)==7
result['seconds']=time.monotonic()-began;dump('result.json',result);print(json.dumps(result),flush=True)
