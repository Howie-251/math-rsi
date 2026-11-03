"""One fixed two-root complementary-cover model, no original graph BFS."""
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
rows={}
for line in (P.parent/'source972.author.adjlist.txt').read_text().splitlines():
    if line.strip() and not line.startswith('#'):
        a=list(map(int,line.split()));rows[a[0]]=set(a[1:])
adj=[rows[u] for u in range(972)]
cache=json.loads((P.parent/'monotone_R2_cover/radius2_sets.json').read_text())
free=cache['eligible'];R2=[set(x) for x in cache['closed_R2']]
assert free==[u for u in range(972) if len(adj[u])<13]
R1=[{pin}|adj[pin] for pin in free]
weights=json.loads((P.parent/'monotone_R2_cover/INTEGER_ROW_WEIGHTS.json').read_text())['row_weights']
C2=max(sum(weights[t] for t in ball) for ball in R2)
C1=max(sum(weights[t] for t in ball) for ball in R1)
save('CAPACITY_DIAGNOSTIC.json',dict(W=sum(weights),C2=C2,C1=C1,W_minus_12C2_plus_12C1=sum(weights)-12*(C2+C1),all_eligible_closed_R1_union=len(set().union(*R1)),source_R2_balls_recomputed=0,R1_sets=[sorted(x) for x in R1]))
import numpy as np
from scipy.optimize import Bounds,LinearConstraint,linprog,milp
from scipy.sparse import csc_matrix,hstack,vstack,eye
A2=csc_matrix(np.array([[t in b for b in R2] for t in range(972)],dtype=float))
A1=csc_matrix(np.array([[t in b for b in R1] for t in range(972)],dtype=float))
cover=vstack([hstack([A2,A1]),hstack([A1,A2])]).tocsc()
disjoint=hstack([eye(108),eye(108)]).tocsc()
budgets=csc_matrix(np.array([[1]*108+[0]*108,[0]*108+[1]*108],dtype=float))
matrix=vstack([cover,disjoint,budgets]).tocsc()
lb=np.r_[np.ones(1944),np.full(110,-np.inf)]
ub=np.r_[np.full(1944,np.inf),np.ones(108),12,12]
lp=linprog(np.ones(216),A_ub=vstack([-cover,disjoint,budgets]).tocsc(),b_ub=np.r_[-np.ones(1944),np.ones(108),12,12],bounds=(0,1),method='highs',options={'time_limit':max(.01,19.5-(time.process_time()-start)),'threads':1})
lpdata=dict(status=int(lp.status),message=lp.message,fractional_minimum=None if lp.fun is None else float(lp.fun),row_dual=None if lp.ineqlin.marginals is None else list(map(float,lp.ineqlin.marginals)),lower_bound_dual=None if lp.lower.marginals is None else list(map(float,lp.lower.marginals)),upper_bound_dual=None if lp.upper.marginals is None else list(map(float,lp.upper.marginals)),CPU_seconds=time.process_time()-start)
save('LP_DIAGNOSTIC.json',lpdata)
remaining=max(.01,19.5-(time.process_time()-start))
solved=milp(c=np.zeros(216),integrality=np.ones(216),bounds=Bounds(np.zeros(216),np.ones(216)),constraints=LinearConstraint(matrix,lb,ub),options={'time_limit':remaining,'threads':1,'mip_rel_gap':0.0})
selA=[] if solved.x is None else [i for i in range(108) if solved.x[i]>.5]
selB=[] if solved.x is None else [i for i in range(108) if solved.x[108+i]>.5]
def union(balls,ids):return set().union(*(balls[i] for i in ids)) if ids else set()
covA=union(R2,selA)|union(R1,selB)
covB=union(R2,selB)|union(R1,selA)
hit=len(selA)<=12 and len(selB)<=12 and not set(selA)&set(selB) and len(covA)==len(covB)==972
result=dict(status='COMPLETE974_BUDDY_EXTENSION_REQUIRES_PARENT_ACCEPTANCE' if hit else 'FIXED_BUDDY_INTEGER_MODEL_INFEASIBLE' if solved.status==2 else 'UNKNOWN_NO_COMPLETE_BUDDY_INCUMBENT',source_n=972,source_m=6264,target_Delta=13,target_D=3,savedL=972,hypothetical_n=974,actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,source_allroot_BFS=0,source_single_root_BFS=0,candidate_newroot_BFS=0,binary_variables=216,old_target_cover_constraints=1944,pin_disjointness_constraints=108,attachment_budgets=[12,12],LP_status=int(lp.status),LP_fractional_minimum=lpdata['fractional_minimum'],MIP_status=int(solved.status),MIP_message=solved.message,exact_selected_cover_A=len(covA),exact_selected_cover_B=len(covB),selected_A=[free[i] for i in selA],selected_B=[free[i] for i in selB],solver_time_budget_remaining=remaining)
if hit:
    A=[free[i] for i in selA];B=[free[i] for i in selB]
    graph=[set(row) for row in adj]+[{973}|set(A),{972}|set(B)]
    for v in A:graph[v].add(972)
    for v in B:graph[v].add(973)
    assert all(len(row)<=13 for row in graph)
    assert all(adj[u]<=graph[u] for u in range(972))
    assert all(u not in row and all(u in graph[v] for v in row) for u,row in enumerate(graph))
    checks=[]
    for root in [972,973]:
        dist=[-1]*974;dist[root]=0;q=deque([root])
        while q:
            u=q.popleft()
            for v in graph[u]:
                if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
        assert all(0<=d<=3 for d in dist)
        checks.append(dict(root=root,visited=974,eccentricity=max(dist),distance_histogram=dict(Counter(dist)),distances=dist))
    m=6264+len(A)+len(B)+1
    path=P/'graph_d13_D3_n974.edges'
    with path.open('w') as out:
        out.write(f'974 {m}\n')
        for u,row in enumerate(graph):
            for v in sorted(row):
                if u<v:out.write(f'{u} {v}\n')
    result.update(actual_n=974,actual_m=m,actual_D=3,actual_Delta=max(map(len,graph)),simple=True,connected=True,old_edges_exactly_retained=True,candidate_newroot_BFS=2,newroot_checks=checks,new_degrees=[len(A)+1,len(B)+1],graph_file=str(path))
    save('CONSTRUCTION.json',dict(source='../source972.author.adjlist.txt',source_n=972,source_m=6264,new_labels=[972,973],new_mutual_edge=[972,973],A=A,B=B,old_pin_degrees={str(v):len(adj[v]) for v in A+B},source_edges_all_retained=True,proof='Old-old<=3 inherited. Newa reaches allold byR2(A) unionR1(B); newb byR2(B) unionR1(A); a-b hasdistance1. Exact currentcoverage and bothnewroot fullBFS checked.',graph_file=str(path)))
result['process_CPU_seconds']=time.process_time()-start
save('RESULT.json',result)
save('terminal.json',dict(status=result['status'],running=False,pending=[],CPU_seconds=result['process_CPU_seconds']))
save('RUN_HANDLE.json',dict(status=result['status'],running=False,pid=os.getpid(),CPU_limit=20,CPU_seconds=result['process_CPU_seconds']))
print(json.dumps({k:v for k,v in result.items() if k!='newroot_checks'}))
