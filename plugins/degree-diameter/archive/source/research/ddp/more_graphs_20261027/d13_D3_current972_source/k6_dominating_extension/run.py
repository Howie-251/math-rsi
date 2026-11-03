"""One fixed minimum-F-domination K6 construction, shared20CPU budget."""
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
model=json.loads((P.parent/'K6_free_dom_structure/min_dom_model.json').read_text())
cache=json.loads((P.parent/'monotone_R2_cover/radius2_sets.json').read_text())
R1cache=json.loads((P.parent/'joint_buddy_cover/CAPACITY_DIAGNOSTIC.json').read_text())
free=cache['eligible'];assert free==model['free_vertices'];pinidx={p:i for i,p in enumerate(free)}
R2=[set(x) for x in cache['closed_R2']];R1=[set(x) for x in R1cache['R1_sets']]
rows={}
for line in (P.parent/'source972.author.adjlist.txt').read_text().splitlines():
    if line.strip() and not line.startswith('#'):
        a=list(map(int,line.split()));rows[a[0]]=set(a[1:])
adj=[rows[u] for u in range(972)];full=[u for u in range(972) if len(adj[u])==13]
assert len(free)==108 and len(full)==864
assert [u for u in range(972) if len(adj[u])<13]==free
forced=model['forced_selected'];pairs=model['choice_pairs'];forbidden=model['forbidden_in_any_min_F_domset']
assert len(forced)==12 and len(pairs)==36 and len(forbidden)==24
assert len(set(forced+[p for pair in pairs for p in pair]+forbidden))==108
centers=model['fixed_color_centers'];assert centers==sorted(centers) and len(centers)==6
import numpy as np
from scipy.optimize import Bounds,LinearConstraint,linprog,milp
from scipy.sparse import coo_matrix,vstack
near1={t:[j for j in range(108) if t in R1[j]] for t in full}
near2only={t:[j for j in range(108) if t in R2[j] and t not in R1[j]] for t in full}
def matrix(spec):
    rr=[];cc=[]
    for i,cols in enumerate(spec):
        for c in cols:rr.append(i);cc.append(c)
    return coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(len(spec),648)).tocsc()
cover=[]
for t in full:
    common=[color*108+j for j in near1[t] for color in range(6)]
    for color in range(6):cover.append(common+[color*108+j for j in near2only[t]])
Acover=matrix(cover);Adis=matrix([[color*108+j for color in range(6)] for j in range(108)])
eqspec=[];eqrhs=[]
for pair in pairs:eqspec.append([color*108+pinidx[p] for p in pair for color in range(6)]);eqrhs.append(1)
for p in forced:eqspec.append([color*108+pinidx[p] for color in range(6)]);eqrhs.append(1)
for color in range(6):eqspec.append([color*108+j for j in range(108)]);eqrhs.append(8)
Aeq=matrix(eqspec);eqrhs=np.array(eqrhs,dtype=float)
lower=np.zeros(648);upper=np.ones(648)
for p in forbidden:
    for color in range(6):upper[color*108+pinidx[p]]=0
for color,p in enumerate(centers):
    lower[color*108+pinidx[p]]=1
    for other in range(6):
        if color!=other:upper[other*108+pinidx[p]]=0
Aub=vstack([-Acover,Adis]).tocsc();bub=np.r_[-np.ones(5184),np.ones(108)]
lp=linprog(np.ones(648),A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=eqrhs,bounds=list(zip(lower,upper)),method='highs',options={'time_limit':max(.01,19.5-(time.process_time()-start)),'threads':1})
save('LP_DIAGNOSTIC.json',dict(status=int(lp.status),message=lp.message,objective=None if lp.fun is None else float(lp.fun),constant_objective='Everyfeasible minDom/color solution has exactly48 selectedpins, so objective48 isconstant andnot a coverage score.',variables=648,cover_rows=5184,disjoint_rows=108,equality_rows=len(eqspec),total_nonzeros=Aub.nnz+Aeq.nnz,CPU_seconds=time.process_time()-start))
constraints=LinearConstraint(vstack([Acover,Adis,Aeq]).tocsc(),np.r_[np.ones(5184),np.full(108,-np.inf),eqrhs],np.r_[np.full(5184,np.inf),np.ones(108),eqrhs])
remaining=max(.01,19.5-(time.process_time()-start))
solved=milp(c=np.ones(648),integrality=np.ones(648),bounds=Bounds(lower,upper),constraints=constraints,options={'time_limit':remaining,'threads':1,'mip_rel_gap':0.0})
colors=[] if solved.x is None else [[free[j] for j in range(108) if solved.x[color*108+j]>.5] for color in range(6)]
hit=False
coverage=[]
if colors and all(len(x)==8 for x in colors):
    S=set().union(*(set(x) for x in colors))
    if len(S)==48:
        coverage=[]
        for color in range(6):
            own={pinidx[x] for x in colors[color]};other={pinidx[x] for x in S-set(colors[color])}
            covered=set().union(*(R2[j] for j in own),*(R1[j] for j in other))
            coverage.append(len(covered))
        hit=coverage==[972]*6 and all(centers[color] in colors[color] for color in range(6))
result=dict(status='COMPLETE978_K6_EXTENSION_REQUIRES_PARENT_ACCEPTANCE' if hit else 'FIXED_K6_MODEL_NUMERICALLY_INFEASIBLE' if solved.status==2 else 'UNKNOWN_NO_COMPLETE_K6_INCUMBENT',source_n=972,source_m=6264,target_Delta=13,target_D=3,savedL=972,hypothetical_n=978,actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,variables=648,fulltarget_cover_rows=5184,disjoint_rows=108,equality_rows=len(eqspec),fixed_extra_distinct_P3center_colors=centers,LP_status=int(lp.status),LP_objective=None if lp.fun is None else float(lp.fun),MIP_calls=1,MIP_status=int(solved.status),MIP_message=solved.message,MIP_time_limit_seconds=remaining,source_allroot_BFS=0,candidate_newroot_BFS=0,cached_R2_balls_recomputed=0,exact_selected_cover_per_helper=coverage)
if hit:
    S=sorted(set().union(*(set(x) for x in colors)))
    assert len(S)==48 and all(sum(p in color for color in colors)==1 for p in S)
    assert all(sum(p in S for p in pair)==1 for pair in pairs) and set(forced)<=set(S)
    F=set(free);assert F<=set().union(*(R1[pinidx[p]] for p in S))
    graph=[set(x) for x in adj]+[set() for _ in range(6)]
    for i in range(6):
        for j in range(i+1,6):graph[972+i].add(972+j);graph[972+j].add(972+i)
        for pin in colors[i]:assert len(adj[pin])==12;graph[pin].add(972+i);graph[972+i].add(pin)
    assert all(len(x)<=13 for x in graph)
    assert all({v for v in graph[u] if v<972}==adj[u] for u in range(972))
    assert all(u not in row and all(u in graph[v] for v in row) for u,row in enumerate(graph))
    newroots=[]
    for root in range(972,978):
        dist=[-1]*978;dist[root]=0;q=deque([root])
        while q:
            u=q.popleft()
            for v in graph[u]:
                if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
        assert all(0<=d<=3 for d in dist)
        newroots.append(dict(root=root,visited=978,eccentricity=max(dist),distance_histogram=dict(Counter(dist)),distances=dist))
    m=sum(map(len,graph))//2;assert m==6327
    path=P/'graph_d13_D3_n978.edges'
    with path.open('w') as out:
        out.write('978 6327\n')
        for u,row in enumerate(graph):
            for v in sorted(row):
                if u<v:out.write(f'{u} {v}\n')
    save('CONSTRUCTION.json',dict(source='../source972.author.adjlist.txt',source_n=972,source_m=6264,new_labels=list(range(972,978)),S=S,colors=colors,clique_edges=[[i,j] for i in range(972,978) for j in range(i+1,978)],old_pin_degrees=[12]*48,fixed_color_centers=centers,extra_restriction_not_WLOG=True,old_induced_source_exactly_retained=True,degree_histogram=dict(Counter(map(len,graph))),proof='Eachhelperoldtarget coverR2(owncolor) unionR1(othercolors) verifiedall972. All6newrootsactualfullBFS<=3. Old-oldD3 inheritedfromretainedpublishedsource; helperpairsdistance1.',source_min_dom_model='../K6_free_dom_structure/min_dom_model.json',graph_file=str(path)))
    result.update(actual_n=978,actual_m=6327,actual_D=3,actual_Delta=13,simple=True,connected=True,source_edges_all_retained=True,S=S,colors=colors,candidate_newroot_BFS=6,newroot_checks=newroots,degree_histogram=dict(Counter(map(len,graph))),graph_file=str(path))
result['process_CPU_seconds']=time.process_time()-start
save('RESULT.json',result)
save('terminal.json',dict(status=result['status'],running=False,pending=[],process_CPU_seconds=result['process_CPU_seconds']))
save('RUN_HANDLE.json',dict(status=result['status'],running=False,pid=os.getpid(),process_CPU_seconds=result['process_CPU_seconds']))
print(json.dumps({k:v for k,v in result.items() if k!='newroot_checks'}))
