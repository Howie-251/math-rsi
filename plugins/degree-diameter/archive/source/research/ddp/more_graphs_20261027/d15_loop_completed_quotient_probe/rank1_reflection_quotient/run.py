"""Exact two-choice reflection compatibility; no source or quotient graph."""
from pathlib import Path
from collections import Counter
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(10,10))
START=time.process_time()
P=Path(__file__).resolve().parent
assert json.loads((P/'PREDICTION.json').read_text())['frozen_before_reflection_pair_tests_and_2SAT']
assert not (P/'RESULT.json').exists()
table=json.loads((P.parent/'affine_relation_recovery/source15552_AFFINE_RELATIONS.json').read_text())
profile=json.loads((P.parent/'matroid36_induced_subset/LABEL_POOL.json').read_text())
assert table['complete'] and table['n']==15552 and len(table['arcs'])==960
assert len(profile['controllers'])==192

def matmul(A,B):
    return [[sum(A[i][h]*B[h][j] for h in range(4))%3 for j in range(4)] for i in range(4)]

def matvec(A,v):
    return [sum(a*b for a,b in zip(row,v))%3 for row in A]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))%3

def normalized(v):
    scale=next(x for x in v if x)
    return [scale*x%3 for x in v]

def rref_kernel(matrix):
    rows=[[x%3 for x in row] for row in matrix]
    pivots=[]
    at=0
    for j in range(4):
        pivot=next((i for i in range(at,len(rows)) if rows[i][j]),None)
        if pivot is None:
            continue
        rows[at],rows[pivot]=rows[pivot],rows[at]
        inverse=rows[at][j]
        rows[at]=[inverse*x%3 for x in rows[at]]
        for i in range(len(rows)):
            if i!=at and rows[i][j]:
                scale=rows[i][j]
                rows[i]=[(x-scale*y)%3 for x,y in zip(rows[i],rows[at])]
        pivots.append(j)
        at+=1
    basis=[]
    for free in (i for i in range(4) if i not in pivots):
        v=[0]*4
        v[free]=1
        for i,pivot in enumerate(pivots):
            v[pivot]=-rows[i][free]%3
        basis.append(v)
    return pivots,basis

I=[[int(i==j) for j in range(4)] for i in range(4)]
choices=[]
for record in profile['controllers']:
    a=record['controller']
    kernels=record['kernel_representatives']
    assert a==len(choices) and len(record['axis_port_indices'])==2
    row=[]
    for choice,coloop in enumerate(record['axis_port_indices']):
        u=kernels[coloop]
        other=[kernels[i] for i in range(5) if i!=coloop]
        pivots,basis=rref_kernel(other)
        assert len(pivots)==3 and len(basis)==1
        ell=basis[0]
        value=dot(ell,u)
        assert value in (1,2)
        ell=[value*x%3 for x in ell]
        assert dot(ell,u)==1 and all(dot(ell,v)==0 for v in other)
        R=[[(I[i][j]-2*u[i]*ell[j])%3 for j in range(4)] for i in range(4)]
        assert matmul(R,R)==I
        difference=[[(R[i][j]-I[i][j])%3 for j in range(4)] for i in range(4)]
        assert len(rref_kernel(difference)[0])==1
        assert matvec(R,u)==[(-x)%3 for x in u]
        assert all(matvec(R,v)==v for v in other)
        row.append({'choice':choice,'coloop_port_index':coloop,'u':u,'ell':ell,
                    'R':R,'fixed_dimension':3,'minus_dimension':1})
    assert row[0]['R']!=row[1]['R']
    choices.append({'controller':a,'choices':row})

def condition(arc,Ra,Rb):
    B,v,j=arc['B'],arc['v'],arc['pivot']
    assert not any(arc['c']) and v[j]==1 and all(x==0 for x in B[j])
    Rbv=matvec(Rb,v)
    line_ok=any(Rbv) and normalized(Rbv)==normalized(v)
    Q=[[(I[i][ell]-v[i]*int(ell==j))%3 for ell in range(4)] for i in range(4)]
    left=matmul(matmul(Q,Rb),B)
    right=matmul(B,Ra)
    return line_ok and left==right,{'output_line_preserved':bool(line_ok),
                                  'Rb_v':Rbv,'Qv_Rb_B':left,'B_Ra':right}

clauses=[]
clause_index={}
arc_pairs=[]
raw_forbidden=0
self_tautologies=0
for arc_id,arc in enumerate(table['arcs']):
    a,b=arc['from'],arc['to']
    allowed=[]
    forbidden=[]
    for ca in (0,1):
        for cb in (0,1):
            ok,evidence=condition(arc,choices[a]['choices'][ca]['R'],choices[b]['choices'][cb]['R'])
            if ok:
                allowed.append([ca,cb])
                continue
            raw_forbidden+=1
            # A positive literal means choice1; a negative literal choice0.
            la=(a+1) if ca==0 else -(a+1)
            lb=(b+1) if cb==0 else -(b+1)
            origin={'arc_id':arc_id,'from':a,'to':b,'forbidden_choices':[ca,cb]}
            item={**origin,**evidence}
            if la==-lb:
                self_tautologies+=1
                item['constraint_kind']='TAUTOLOGY_SELFARC_DISTINCT_CHOICES'
                item['clause_id']=None
            else:
                clause=tuple(sorted({la,lb}))
                if clause not in clause_index:
                    clause_index[clause]=len(clauses)
                    clauses.append({'clause_id':len(clauses),'literals':list(clause),'origins':[]})
                cid=clause_index[clause]
                clauses[cid]['origins'].append(origin)
                item['clause_id']=cid
                item['constraint_kind']='UNIT' if len(clause)==1 else 'BINARY'
            forbidden.append(item)
    arc_pairs.append({'arc_id':arc_id,'from':a,'to':b,'allowed_choice_pairs':allowed,
                      'forbidden_choice_pairs':forbidden})
(P/'LOCAL_REFLECTION_CHOICES.json').write_text(json.dumps({'controllers':choices},ensure_ascii=False,indent=2)+'\n')
(P/'ARC_CHOICE_PAIRS.json').write_text(json.dumps({'arcs':arc_pairs},ensure_ascii=False,indent=2)+'\n')

def node(lit):
    return 2*(abs(lit)-1)+int(lit>0)

def literal(vertex):
    return (vertex//2+1)*(1 if vertex%2 else -1)

solve_start=time.process_time()
graph=[[] for _ in range(384)]
reverse=[[] for _ in range(384)]
for rec in clauses:
    cid=rec['clause_id']
    p=rec['literals'][0]
    q=rec['literals'][-1]
    for left,right in [(-p,q),(-q,p)]:
        u,v=node(left),node(right)
        graph[u].append((v,cid))
        reverse[v].append(u)
visited=set()
order=[]
for root in range(384):
    if root in visited:
        continue
    visited.add(root)
    stack=[(root,0)]
    while stack:
        v,index=stack[-1]
        if index<len(graph[v]):
            stack[-1]=(v,index+1)
            nxt,_=graph[v][index]
            if nxt not in visited:
                visited.add(nxt)
                stack.append((nxt,0))
        else:
            order.append(v)
            stack.pop()
component=[-1]*384
count=0
for root in reversed(order):
    if component[root]>=0:
        continue
    component[root]=count
    stack=[root]
    while stack:
        v=stack.pop()
        for nxt in reverse[v]:
            if component[nxt]<0:
                component[nxt]=count
                stack.append(nxt)
    count+=1
conflict=next((a for a in range(192) if component[2*a]==component[2*a+1]),None)
solvecpu=time.process_time()-solve_start
assert solvecpu<=5

def implication_path(start,finish):
    parents={start:None}
    stack=[start]
    while stack and finish not in parents:
        v=stack.pop()
        for nxt,cid in graph[v]:
            if nxt not in parents:
                parents[nxt]=(v,cid)
                stack.append(nxt)
    assert finish in parents
    path=[]
    v=finish
    while v!=start:
        before,cid=parents[v]
        path.append({'from_literal':literal(before),'to_literal':literal(v),'clause_id':cid})
        v=before
    return list(reversed(path))

sat=conflict is None
assignment=None
contradiction=None
arc_rechecks=0
orbits=None
if not sat:
    contradiction={'controller':conflict,'choice0_to_choice1':implication_path(2*conflict,2*conflict+1),
                   'choice1_to_choice0':implication_path(2*conflict+1,2*conflict)}
else:
    assignment=[int(component[2*a+1]>component[2*a]) for a in range(192)]
    assert all(any((lit>0 and assignment[abs(lit)-1]==1) or (lit<0 and assignment[abs(lit)-1]==0)
                   for lit in rec['literals']) for rec in clauses)
    selected=[choices[a]['choices'][assignment[a]] for a in range(192)]
    for arc in table['arcs']:
        ok,_=condition(arc,selected[arc['from']]['R'],selected[arc['to']]['R'])
        assert ok
        arc_rechecks+=1
    assert arc_rechecks==960
    mapping=[-1]*15552
    involution=[-1]*15552
    representatives=[]
    per_controller=[]
    for a in range(192):
        R=selected[a]['R']
        images=[]
        for x in range(81):
            digits=[x//3**i%3 for i in range(4)]
            y=matvec(R,digits)
            images.append(sum(v*3**i for i,v in enumerate(y)))
        assert len(set(images))==81 and all(images[images[x]]==x for x in range(81))
        fixed=sum(x==y for x,y in enumerate(images))
        assert fixed==27
        before=len(representatives)
        for x,y in enumerate(images):
            involution[81*a+x]=81*a+y
            if mapping[81*a+x]>=0:
                continue
            newlabel=len(representatives)
            representatives.append(81*a+x)
            mapping[81*a+x]=newlabel
            mapping[81*a+y]=newlabel
        assert len(representatives)-before==54
        per_controller.append({'controller':a,'fixed_vertices':fixed,'orbit_count':54,
                               'first_orbit_label':before,'choice':assignment[a]})
    assert len(representatives)==10368 and all(0<=v<10368 for v in mapping)
    orbits={'status':'COMPLETE_VERIFIED_SOURCE_AUTOMORPHISM_ORBIT_MAP',
            'source_n':15552,'source_m':table['m'],'orbit_count':10368,
            'old_vertex_to_orbit':mapping,'orbit_representatives':representatives,
            'old_involution_image':involution,'per_controller':per_controller,
            'graph_generated':False,'source_BFS':0}
    (P/'ORBIT_MAP.json').write_text(json.dumps(orbits,ensure_ascii=False,separators=(',',':'))+'\n')
    (P/'REFLECTION_MAPS.json').write_text(json.dumps({'assignment':assignment,
       'controllers':[{'controller':a,**selected[a]} for a in range(192)],
       'all960_arc_conditions_verified':True},ensure_ascii=False,indent=2)+'\n')

logic={'status':'SAT' if sat else 'UNSAT','solver':'One deterministic Kosaraju2SAT solve',
       'variables':192,'clauses':clauses,'raw_forbidden_choice_pairs':raw_forbidden,
       'selfarc_tautologies_removed':self_tautologies,'SCC_count':count,
       'SCC_component_of_literal_nodes':component,'assignment':assignment,
       'contradiction':contradiction,'solve_CPU_seconds':solvecpu}
(P/'TWOSAT_RESULT.json').write_text(json.dumps(logic,ensure_ascii=False,indent=2)+'\n')
result={'status':'SAT_VERIFIED_ALL960_ARCS_ORBIT_MAP_READY' if sat else 'UNSAT_FIXED_CANONICAL_REFLECTION_CLASS',
        'prediction_status':'SUPPORTED' if sat else 'REFUTED',
        'source_n':15552,'source_m':table['m'],'local_choices_per_controller':2,
        'controllers':192,'arc_pair_tests':3840,'effective_unique_clauses':len(clauses),
        'raw_forbidden_pairs':raw_forbidden,'selfarc_tautologies_removed':self_tautologies,
        'solve_CPU_seconds':solvecpu,'all_arc_rechecks':arc_rechecks,
        'quotient_label_count':10368 if sat else None,'first_conflict_controller':conflict,
        'orbit_map':'ORBIT_MAP.json' if sat else None,
        'CPU_seconds':time.process_time()-START,'external_solver_calls':0,
        'source_BFS':0,'quotient_graph_generated':False,
        'scope':'Only the two canonical controller-fixed rank1 coloop reflections preserving all five local noise lines; no other involution or controller permutation.'}
(P/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
