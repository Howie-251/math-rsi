"""One fixed threshold13 cover; old-source diameter is inherited."""
import json
import os
from pathlib import Path
import resource
import time
from collections import Counter,deque

P=Path(__file__).resolve().parent
start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(10,11))
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
def save(name,x):(P/name).write_text(json.dumps(x,indent=2)+'\n')
save('RUN_HANDLE.json',dict(pid=os.getpid(),status='ACTUAL_PROCESS_RUNNING',command='python run.py',CPU_limit=10))
rows={}
for line in (P.parent/'source972.author.adjlist.txt').read_text().splitlines():
    if line.strip() and not line.startswith('#'):
        a=list(map(int,line.split()));rows[a[0]]=set(a[1:])
adj=[rows[i] for i in range(972)]
free=[u for u in range(972) if len(adj[u])<13]
assert len(free)==108
balls=[]
for pin in free:
    b={pin}|adj[pin]
    for v in adj[pin]:b|=adj[v]
    balls.append(b)
allunion=set().union(*balls)
support=[sum(t in b for b in balls) for t in range(972)]
pre=dict(source_n=972,source_m=sum(map(len,adj))//2,eligible=free,ball_sizes=[len(b) for b in balls],all_eligible_R2_union=len(allunion),union_missing=sorted(set(range(972))-allunion),target_support_histogram=dict(Counter(support)),minimum_target_support=min(support),targets_with_minimum_support=[t for t,n in enumerate(support) if n==min(support)],unique_support_patterns=len({tuple(i for i,b in enumerate(balls) if t in b) for t in range(972)}),CPU_seconds=time.process_time()-start)
save('PREFLIGHT.json',pre)
save('radius2_sets.json',dict(source_n=972,eligible=free,closed_R2=[sorted(b) for b in balls]))
result=dict(target_Delta=13,target_D=3,savedL=972,source_n=972,source_m=6264,hypothetical_n=973,actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,source_allroot_BFS=0,candidate_newroot_BFS=0)
if len(allunion)<972:
    result.update(status='ALL_ELIGIBLE_R2_UNION_MISS_NO_MIP',witness=pre['union_missing'][0])
else:
    import numpy as np
    from scipy.optimize import Bounds,LinearConstraint,milp,linprog
    from scipy.sparse import csc_matrix,vstack
    A=csc_matrix(np.array([[t in b for b in balls] for t in range(972)],dtype=float))
    lp=linprog(np.ones(108),A_ub=-A,b_ub=-np.ones(972),bounds=(0,1),method='highs',options={'time_limit':max(.01,9.7-(time.process_time()-start)),'threads':1})
    lpdata=dict(status=int(lp.status),message=lp.message,fractional_minimum=None if lp.fun is None else float(lp.fun),CPU_seconds=time.process_time()-start)
    save('LP_DIAGNOSTIC.json',lpdata)
    constraints=LinearConstraint(vstack([A,csc_matrix(np.ones((1,108)))]).tocsc(),np.r_[np.ones(972),-np.inf],np.r_[np.full(972,np.inf),13])
    remaining=max(.01,9.7-(time.process_time()-start))
    solved=milp(c=np.zeros(108),integrality=np.ones(108),bounds=Bounds(np.zeros(108),np.ones(108)),constraints=constraints,options={'time_limit':remaining,'threads':1,'mip_rel_gap':0.0})
    selected=[] if solved.x is None else [i for i,x in enumerate(solved.x) if x>.5]
    covered=set().union(*(balls[i] for i in selected)) if selected else set()
    hit=bool(selected) and len(selected)<=13 and len(covered)==972
    result.update(status='COMPLETE973_EXTENSION_REQUIRES_PARENT_ACCEPTANCE' if hit else 'THRESHOLD13_INTEGER_COVER_INFEASIBLE' if solved.status==2 else 'UNKNOWN_NO_COMPLETE_COVER_INCUMBENT',solver_status=int(solved.status),solver_message=solved.message,LP_fractional_minimum=lpdata['fractional_minimum'],selected_count=len(selected),exact_selected_R2_coverage=len(covered),solver_time_budget_remaining=remaining)
    if hit:
        pins=[free[i] for i in selected]
        graph=[set(x) for x in adj]+[set(pins)]
        for pin in pins:graph[pin].add(972)
        assert all(len(x)<=13 for x in graph)
        assert all(adj[u]<=graph[u] for u in range(972))
        assert all(u not in x and all(u in graph[v] for v in x) for u,x in enumerate(graph))
        dist=[-1]*973;dist[972]=0;q=deque([972])
        while q:
            u=q.popleft()
            for v in graph[u]:
                if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
        assert all(0<=d<=3 for d in dist)
        path=P/'graph_d13_D3_n973.edges'
        with path.open('w') as out:
            out.write(f'973 {6264+len(pins)}\n')
            for u,row in enumerate(graph):
                for v in sorted(row):
                    if u<v:out.write(f'{u} {v}\n')
        result.update(actual_n=973,actual_m=6264+len(pins),actual_D=3,actual_Delta=max(map(len,graph)),pins=pins,pin_old_degrees=[len(adj[u]) for u in pins],newroot=972,newroot_eccentricity=max(dist),newroot_visited=973,newroot_distance_histogram=dict(Counter(dist)),candidate_newroot_BFS=1,old_edges_exactly_retained=True,simple=True,connected=True,graph_file=str(path),newroot_distances=dist)
        save('CONSTRUCTION.json',dict(source='../source972.author.adjlist.txt',source_n=972,source_m=6264,new_label=972,new_neighbors=pins,new_vertex_degree=len(pins),retain_every_source_edge=True,actual_Delta=max(map(len,graph)),proof='Old-old distances<=3 are inherited from published source and retained edges. Every old target has old distance<=2 to a chosen pin, checked by exact R2 union; actual newroot BFS confirms ecc3.',evidence='RESULT.json'))
result['process_CPU_seconds']=time.process_time()-start
save('RESULT.json',result)
save('terminal.json',dict(status=result['status'],running=False,pending=[],CPU_seconds=result['process_CPU_seconds']))
save('RUN_HANDLE.json',dict(pid=os.getpid(),status=result['status'],running=False,completed=True,command='python run.py',CPU_limit=10,CPU_seconds=result['process_CPU_seconds']))
print(json.dumps({k:v for k,v in result.items() if k!='newroot_distances'}))
