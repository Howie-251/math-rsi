"""One whole-spare K1,9 construction, no helper-count or seed continuation."""
import json
import os
from pathlib import Path
import resource
import time
from collections import Counter,deque
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
P=Path(__file__).resolve().parent;start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(20,21))
def save(name,x):(P/name).write_text(json.dumps(x,indent=2)+'\n')
save('RUN_HANDLE.json',dict(status='ACTUAL_PROCESS_RUNNING',pid=os.getpid(),command='python run.py',CPU_limit=20))
cache=json.loads((P.parent/'monotone_R2_cover/radius2_sets.json').read_text())
free=cache['eligible'];R2=[set(x) for x in cache['closed_R2']]
R1=[set(x) for x in json.loads((P.parent/'joint_buddy_cover/CAPACITY_DIAGNOSTIC.json').read_text())['R1_sets']]
rows={}
for line in (P.parent/'source972.author.adjlist.txt').read_text().splitlines():
    if line.strip() and not line.startswith('#'):
        a=list(map(int,line.split()));rows[a[0]]=set(a[1:])
adj=[rows[u] for u in range(972)];full=[u for u in range(972) if len(adj[u])==13]
assert len(full)==864 and free==[u for u in range(972) if len(adj[u])==12]
assert set().union(*R1)==set(range(972))
import numpy as np
from scipy.optimize import Bounds,LinearConstraint,linprog,milp
from scipy.sparse import coo_matrix,vstack
def sparse(spec):
    rr=[];cc=[];data=[]
    for i,row in enumerate(spec):
        for col,value in row:rr.append(i);cc.append(col);data.append(value)
    return coo_matrix((data,(rr,cc)),shape=(len(spec),1080)).tocsc()
cover=[]
for t in full:
    common=[(j,1) for j in range(108) if t in R1[j]]
    own=[j for j in range(108) if t in R2[j]]
    for leaf in range(9):cover.append(common+[(108*(leaf+1)+j,1) for j in own])
Acover=sparse(cover)
Aassign=sparse([[(group*108+j,1) for group in range(10)] for j in range(108)])
Abudget=sparse([[(group*108+j,1) for j in range(108)] for group in range(10)])
caps=np.array([4]+[12]*9,dtype=float)
Aub=vstack([-Acover,Abudget]).tocsc();bub=np.r_[-np.ones(7776),caps]
lp=linprog(np.ones(1080),A_ub=Aub,b_ub=bub,A_eq=Aassign,b_eq=np.ones(108),bounds=(0,1),method='highs',options={'time_limit':max(.01,min(3,19.5-(time.process_time()-start))),'threads':1})
save('LP_DIAGNOSTIC.json',dict(status=int(lp.status),message=lp.message,objective=None if lp.fun is None else float(lp.fun),LP_leaf_ordering_applied=False,objective_is_constant108=True,variables=1080,coverage_rows=7776,assignment_equalities=108,budget_rows=10,nonzeros=Aub.nnz+Aassign.nnz,CPU_seconds=time.process_time()-start))
print('STAR_LP_STATUS',lp.status,'objective',lp.fun,flush=True)
# Sort the nine nonempty leaf sets by their distinct smallest selected pin.
# This breaks only the actual permutation symmetry of leaves; hub is different.
sym=[]
for leaf in range(1,9):
    for p in range(108):
        sym.append([(108*(leaf+1)+p,1)]+[(108*leaf+q,-1) for q in range(p)])
Asym=sparse(sym)
matrix=vstack([Acover,Abudget,Aassign,Asym]).tocsc()
lower=np.r_[np.ones(7776),np.full(10,-np.inf),np.ones(108),np.full(864,-np.inf)]
upper=np.r_[np.full(7776,np.inf),caps,np.ones(108),np.zeros(864)]
remaining=max(.01,19.5-(time.process_time()-start))
solved=milp(c=np.ones(1080),integrality=np.ones(1080),bounds=Bounds(np.zeros(1080),np.ones(1080)),constraints=LinearConstraint(matrix,lower,upper),options={'time_limit':remaining,'threads':1,'mip_rel_gap':0.0})
groups=[] if solved.x is None else [[free[j] for j in range(108) if solved.x[group*108+j]>.5] for group in range(10)]
hit=False;coverage=[]
if groups and len(groups[0])<=4 and all(1<=len(x)<=12 for x in groups[1:]):
    flat=[x for row in groups for x in row]
    if len(flat)==108 and len(set(flat))==108 and set(flat)==set(free):
        idx={p:i for i,p in enumerate(free)}
        common=set().union(*(R1[idx[p]] for p in groups[0])) if groups[0] else set()
        coverage=[len(set(full)&(common|set().union(*(R2[idx[p]] for p in pins)))) for pins in groups[1:]]
        hit=coverage==[864]*9
result=dict(status='COMPLETE982_STAR_EXTENSION_REQUIRES_PARENT_ACCEPTANCE' if hit else 'FIXED_STAR_MODEL_NUMERICALLY_INFEASIBLE' if solved.status==2 else 'UNKNOWN_NO_COMPLETE_STAR_INCUMBENT',source_n=972,source_m=6264,target_Delta=13,target_D=3,savedL=972,hypothetical_n=982,hypothetical_m=6381,actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,variables=1080,oldfull_target_cover_rows=7776,assignment_equalities=108,hub_budget=4,leaf_budgets=[12]*9,valid_leaf_symmetry_rows=864,LP_status=int(lp.status),LP_objective=None if lp.fun is None else float(lp.fun),LP_leaf_ordering_applied=False,MIP_calls=1,MIP_status=int(solved.status),MIP_message=solved.message,MIP_time_limit_seconds=remaining,source_allroot_BFS=0,candidate_newroot_BFS=0,cached_R2_balls_recomputed=0,exact_fulltarget_coverage_per_leaf=coverage)
if hit:
    C=groups[0];A=groups[1:];assert [min(x) for x in A]==sorted(min(x) for x in A)
    graph=[set(x) for x in adj]+[set() for _ in range(10)]
    for leaf in range(973,982):graph[972].add(leaf);graph[leaf].add(972)
    for helper,pins in enumerate(groups,972):
        for p in pins:assert len(adj[p])==12;graph[p].add(helper);graph[helper].add(p)
    assert all(len(x)<=13 for x in graph)
    assert all({v for v in graph[u] if v<972}==adj[u] for u in range(972))
    assert all(u not in row and all(u in graph[v] for v in row) for u,row in enumerate(graph))
    checks=[]
    for root in range(972,982):
        dist=[-1]*982;dist[root]=0;q=deque([root])
        while q:
            u=q.popleft()
            for v in graph[u]:
                if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
        assert all(0<=d<=3 for d in dist)
        checks.append(dict(root=root,visited=982,eccentricity=max(dist),distance_histogram=dict(Counter(dist)),distances=dist))
    assert sum(map(len,graph))//2==6381
    path=P/'graph_d13_D3_n982.edges'
    with path.open('w') as out:
        out.write('982 6381\n')
        for u,row in enumerate(graph):
            for v in sorted(row):
                if u<v:out.write(f'{u} {v}\n')
    save('CONSTRUCTION.json',dict(source='../source972.author.adjlist.txt',source_n=972,source_m=6264,new_labels=list(range(972,982)),hub=972,leaves=list(range(973,982)),C=C,A=A,oldfree_all_assigned_once=free,old_pin_degrees=[12]*108,helper_edges=[[972,j] for j in range(973,982)],true_WLOG_leaf_minima_order=True,old_induced_source_exactly_retained=True,degree_histogram=dict(Counter(map(len,graph))),proof='AllFassigned andhelperdiameter2 covereveryfree target within3; oldFdominatesH sohubcoversalloldfullwithin3. Eachleaf864fulltargets exactR2(Ai) unionR1(C) checked. All10newroots actualBFS<=3; oldoldD3inherited.',graph_file=str(path)))
    result.update(actual_n=982,actual_m=6381,actual_D=3,actual_Delta=13,simple=True,connected=True,old_source_edges_all_retained=True,C=C,A=A,candidate_newroot_BFS=10,newroot_checks=checks,degree_histogram=dict(Counter(map(len,graph))),graph_file=str(path))
result['process_CPU_seconds']=time.process_time()-start
save('RESULT.json',result)
save('terminal.json',dict(status=result['status'],running=False,pending=[],process_CPU_seconds=result['process_CPU_seconds']))
save('RUN_HANDLE.json',dict(status=result['status'],running=False,pid=os.getpid(),process_CPU_seconds=result['process_CPU_seconds']))
print(json.dumps({k:v for k,v in result.items() if k!='newroot_checks'}))
