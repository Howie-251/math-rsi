"""Diagnostic exact matching model for failure of four bridge criteria.
SAT witnesses only guide research; solver infeasibility is not a proof here.
"""
import json,itertools as it,numpy as np
from pathlib import Path
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
R=Path(__file__).resolve().parent
H={0,15,23,27,29,1,2,4};V=[x for x in range(32) if x not in H]
edges=list(it.combinations(V,2));index={e:i for i,e in enumerate(edges)};ne=len(edges)
cuts=[{'i':1,'Y':[3,6],'ob':[10,18]},
      {'i':2,'Y':[5,6],'ob':[12,20]},
      {'i':3,'Y':[9,10,12],'ob':[8,24]},
      {'i':4,'Y':[17,18,20],'ob':[16,24]}]
constraints=[]
def add(coeff,lo,hi):constraints.append((coeff,lo,hi))
for v in V:add({j:1 for j,e in enumerate(edges) if v in e},1,1)
def form(pred):return {j:1 for j,e in enumerate(edges) if pred(*e)}
def combine(*terms):
    d={}
    for scale,term in terms:
        for j,a in term.items():d[j]=d.get(j,0)+scale*a
    return {j:a for j,a in d.items() if a}
forms=[]
for k,cut in enumerate(cuts):
    i=cut['i'];Y=set(cut['Y']);p,q=cut['ob'];m=len(Y);extra=ne+k
    crossing=form(lambda x,y:bool((x^y)>>i&1))
    yp=form(lambda x,y:bool((x^y)>>i&1) and (x in Y or y in Y))
    inside=form(lambda x,y:x in Y and y in Y)
    def active(v):return form(lambda x,y:(x==v and (not(y>>i&1) or y in Y)) or (y==v and(not(x>>i&1) or x in Y)))
    ap,aq=active(p),active(q)
    # z is the AND of two binary active-endpoint indicators.
    add(combine((1,{extra:1}),(-1,ap)),-np.inf,0)
    add(combine((1,{extra:1}),(-1,aq)),-np.inf,0)
    add(combine((1,{extra:1}),(-1,ap),(-1,aq)),-1,np.inf)
    # Failure: fixed OB, or |J| >= (c + number of bridges)/2.
    obidx=index[tuple(sorted((p,q)))];big=32
    add(combine((2,yp),(2,inside),(2,{extra:1}),(-1,crossing),(big,{obidx:1})),m,np.inf)
    forms.append((crossing,yp,inside,ap,aq))
A=lil_matrix((len(constraints),ne+len(cuts)),dtype=float)
for row,(d,lo,hi) in enumerate(constraints):
    for col,v in d.items():A[row,col]=v
cost=np.array([(x^y).bit_count() for x,y in edges]+[0]*len(cuts),dtype=float)
res=milp(cost,integrality=np.ones(len(cost)),bounds=Bounds(np.zeros(len(cost)),np.ones(len(cost))),
    constraints=LinearConstraint(A.tocsr(),[x[1] for x in constraints],[x[2] for x in constraints]),
    options={'time_limit':30})
out={'scope':'Feasible witnesses to failure of sufficient bridge criteria only; not A8 counterexamples',
     'solver_status':int(res.status),'solver_message':str(res.message),'full_a8_proved':False}
if res.x is not None:
    chosen=[e for j,e in enumerate(edges) if res.x[j]>.5]
    assert len(chosen)==12 and sorted(x for e in chosen for x in e)==V
    mate={x:y for e in chosen for x,y in (e,e[::-1])};reports=[]
    for cut in cuts:
        i=cut['i'];Y=set(cut['Y']);p,q=cut['ob'];X={x for x in V if x>>i&1 and (mate[x]^x)>>i&1}
        cross=len(X);port_y=len(Y&X);internal=sum(mate[x] in Y for x in Y)//2
        extra=int((p in X or mate[p] in Y) and(q in X or mate[q] in Y))
        fixed=mate[p]==q;d=(cross+len(Y))//2;J=port_y+internal+extra
        assert (cross+len(Y))%2==0 and(fixed or J>=d)
        reports.append({**cut,'crossings':cross,'ports_B':sorted(X),'fixed_OB':fixed,
                        'D_size':d,'J_size':J,'Y_ports':port_y,'Y_internal_pairs':internal,'extra_pair':extra})
    out.update(matching=chosen,criteria=reports,total_matching_length=sum((x^y).bit_count() for x,y in chosen))
(R/'A8_orbit4_joint_bad_milp.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
