"""Saved-controller diagnosis: complete one-switch neighborhood, bounded joint moves."""
from pathlib import Path
from collections import Counter,deque
from itertools import combinations
import json,time
import numpy as np

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'second_mechanism/control_unrestricted_n31.edges'


def cycles(adj,length):
    result=[]
    for root in range(len(adj)):
        def visit(path):
            if len(path)==length:
                if root in adj[path[-1]] and path[1]<path[-1]:result.append(path)
                return
            for v in sorted(adj[path[-1]]):
                if v>root and v not in path:visit(path+[v])
        visit([root])
    return result


def switches(edges,A):
    for k,l in combinations(range(len(edges)),2):
        a,b=edges[k];c,d=edges[l]
        if len({a,b,c,d})<4:continue
        for x,y in [(c,d),(d,c)]:
            if not A[a,x] and not A[b,y]:
                yield k,l,[(a,b),(c,d)],[(a,x),(b,y)]


def change(A,remove,add):
    B=A.copy()
    for u,v in remove:B[u,v]=B[v,u]=0
    for u,v in add:B[u,v]=B[v,u]=1
    return B


def main():
    cpu_start=time.process_time();wall_start=time.monotonic()
    rows=[tuple(map(int,line.split())) for line in SOURCE.read_text().splitlines() if line]
    n,m=rows[0];edges=sorted(tuple(sorted(e)) for e in rows[1:]);assert (n,m)==(31,62) and len(edges)==m
    A=np.zeros((n,n),dtype=np.int64)
    for u,v in edges:assert not A[u,v] and u!=v;A[u,v]=A[v,u]=1
    assert np.all(A.sum(axis=1)==4)
    A2=A@A;A3=A2@A;original_zeros=[tuple(map(int,p)) for p in np.argwhere(A3==0)]
    assert len(original_zeros)==4 and np.all(np.diag(A3)>0)
    adj=[set(map(int,np.flatnonzero(A[u]))) for u in range(n)]
    cs={k:cycles(adj,k) for k in (3,4,5)}
    triangle_incidence={v:[i for i,t in enumerate(cs[3]) if v in t] for v in range(n)}
    triangle_components=[];unused=set(range(len(cs[3])))
    while unused:
        component={min(unused)};unused-=component;front=list(component)
        while front:
            i=front.pop()
            add={j for j in unused if set(cs[3][i])&set(cs[3][j])}
            component|=add;unused-=add;front.extend(add)
        triangle_components.append(dict(triangle_ids=sorted(component),
                triangles=[cs[3][i] for i in sorted(component)],
                vertices=sorted({v for i in component for v in cs[3][i]})))
    holes=[]
    for s,t in original_zeros:
        if s>=t:continue
        distance=[-1]*n;distance[s]=0;queue=deque([s])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if distance[v]<0:distance[v]=distance[u]+1;queue.append(v)
        paths=[(s,)];walk_counts=[];shortest_paths=[]
        for length in range(5):
            got=[list(p) for p in paths if p[-1]==t];walk_counts.append(len(got))
            if length==4:shortest_paths=got
            paths=[p+(v,) for p in paths for v in sorted(adj[p[-1]])]
        boundary_s=sorted(np.flatnonzero(A2[s]).tolist());boundary_t=sorted(np.flatnonzero(A2[t]).tolist())
        holes.append(dict(pair=[s,t],distance=distance[t],neighbors_s=sorted(adj[s]),neighbors_t=sorted(adj[t]),
                    exact_two_walk_support_s=boundary_s,exact_two_walk_support_t=boundary_t,
                    common_neighbors=sorted(adj[s]&adj[t]),
                    radius_layers_s={d:[v for v in range(n) if distance[v]==d] for d in range(max(distance)+1)},
                    counts_walks_length_0_to_4=walk_counts,length_four_paths=shortest_paths))
    vertex_cycles={k:{v:sum(v in c for c in cs[k]) for v in range(n)} for k in cs}
    edge_cycles={k:{f'{u}-{v}':sum(any({u,v}=={c[i],c[(i+1)%k]} for i in range(k)) for c in cs[k])
                    for u,v in edges} for k in cs}

    # Complete single-switch neighborhood; no stochastic search or budget restart.
    one=[];hist=Counter();best_one=n*n
    for k,l,remove,add in switches(edges,A):
        B=change(A,remove,add);B3=(B@B)@B;zeros=np.argwhere(B3==0)
        item=dict(remove=remove,add=add,zero_count=len(zeros),
                  zero_diagonal=int(np.count_nonzero(np.diag(B3)==0)),
                  original_zero_count=int(sum(B3[s,t]==0 for s,t in original_zeros)),
                  zero_pairs=sorted([list(map(int,p)) for p in zeros]))
        hist[len(zeros)]+=1;best_one=min(best_one,len(zeros));one.append(item)
    (HERE/'single_switches.json').write_text(json.dumps(one,indent=2)+'\n')
    targeted=[x for x in one if x['original_zero_count']==0 and x['zero_diagonal']==0 and x['zero_count']<=30]
    targeted.sort(key=lambda x:(x['zero_count'],x['remove'],x['add']))
    selected=targeted[:64]
    # Finite joint proposals: each selected first move covers BOTH original holes;
    # the second move ranges over its complete legal 2-switch neighborhood.
    checked=0;complete_first=0;best_joint=n*n;best_joint_record=None;solutions=[];timed_out=False
    best_nontrivial=n*n;best_nontrivial_record=None;nontrivial_best_count=0;undo_count=0
    for first in selected:
        if time.process_time()-cpu_start>28:timed_out=True;break
        B=change(A,first['remove'],first['add'])
        edges_B=[(u,v) for u in range(n) for v in range(u+1,n) if B[u,v]]
        local_complete=True
        for k,l,remove,add in switches(edges_B,B):
            if checked%1000==0 and time.process_time()-cpu_start>28:timed_out=True;local_complete=False;break
            C=change(B,remove,add);C3=(C@C)@C;zero=int(np.count_nonzero(C3==0));checked+=1
            undo=np.array_equal(C,A)
            if undo:undo_count+=1
            elif zero<best_nontrivial:
                best_nontrivial=zero;nontrivial_best_count=1
                best_nontrivial_record=dict(first=first,second=dict(remove=remove,add=add),
                                    zero_count=zero,zero_pairs=np.argwhere(C3==0).tolist(),
                                    net_removed=[list(e) for e in edges if not C[e[0],e[1]]],
                                    net_added=[[u,v] for u in range(n) for v in range(u+1,n) if C[u,v] and not A[u,v]])
            elif zero==best_nontrivial:nontrivial_best_count+=1
            if zero<best_joint:
                best_joint=zero;best_joint_record=dict(first=first,second=dict(remove=remove,add=add),
                                    zero_count=zero,zero_pairs=np.argwhere(C3==0).tolist())
            if zero==0:
                solution_edges=[(u,v) for u in range(n) for v in range(u+1,n) if C[u,v]]
                solution=best_joint_record.copy();solutions.append(solution)
                (HERE/'control31_joint_repair.edges').write_text(f'{n} {len(solution_edges)}\n'+
                        ''.join(f'{u} {v}\n' for u,v in solution_edges))
                (HERE/'control31_joint_repair.json').write_text(json.dumps(solution,indent=2)+'\n')
                local_complete=False;break
        if local_complete:complete_first+=1
        if timed_out or solutions:break
    result=dict(source=str(SOURCE),n=n,m=m,scope='saved graph only; complete single switches and finite targeted joint proposals',
                original_zero_pairs=[list(p) for p in original_zeros],cycles=cs,
                triangle_components=triangle_components,vertex_cycle_counts=vertex_cycles,
                edge_cycle_counts=edge_cycles,holes=holes,
                single_switch_count=len(one),single_switch_zero_count_hist=dict(hist),best_single_zero_count=best_one,
                targeted_first_pool=len(targeted),targeted_first_selected=len(selected),
                targeted_gate='covers both old unordered holes; no zero diagonal; <=30 ordered zero entries; first 64 in deterministic score/edge order',
                joint_evaluations=checked,joint_completed_first=complete_first,best_joint_zero_count=best_joint,
                best_joint=best_joint_record,best_nontrivial_joint_zero_count=best_nontrivial,
                best_nontrivial_joint=best_nontrivial_record,nontrivial_best_count=nontrivial_best_count,
                exact_undo_count=undo_count,solutions=len(solutions),timed_out=timed_out,
                cpu_seconds=time.process_time()-cpu_start,wall_seconds=time.monotonic()-wall_start)
    (HERE/'diagnosis.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['single_switch_count','single_switch_zero_count_hist','best_single_zero_count',
        'targeted_first_pool','targeted_first_selected','joint_evaluations','joint_completed_first','best_joint_zero_count',
        'best_nontrivial_joint_zero_count','nontrivial_best_count','exact_undo_count',
        'solutions','timed_out','cpu_seconds','wall_seconds']},indent=2))
    print('triangle components',triangle_components)
    print('cycle totals',{k:len(v) for k,v in cs.items()})


if __name__=='__main__':main()
