"""No SciPy, no producer matrix imports. Independently enumerate row8 graphs
by solving for the last three edges; decode each certificate as a polynomial
in one literal original-edge type and check exact Fraction inequalities.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,permutations,combinations
from math import comb
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
E=list(combinations(range(5),2));index={e:i for i,e in enumerate(E)}
maps=[[index[tuple(sorted((p[i],p[j])))] for i,j in E] for p in permutations(range(5))]
def canon(w):return min(tuple(w[k] for k in mp) for mp in maps)
labelled=[]
for first in product(range(4),repeat=4):
    if sum(first)!=8:continue
    a,b,c,d=first
    for e,f in product(range(4),repeat=2):
        g=8-a-e-f
        if not 0<=g<=3:continue
        for h in range(4):
            i=8-b-e-h;j=8-c-f-h
            if not(0<=i<=3 and 0<=j<=3 and d+g+i+j==8):continue
            labelled.append((a,b,c,d,e,f,g,h,i,j))
assert len(labelled)==len(set(labelled))==148
orbits={canon(w) for w in labelled};assert len(orbits)==6
R=json.loads((P/'NONUNIFORM_RESULT.json').read_text())
uniform=(2,)*10
assert {canon(tuple(r['w'])) for r in R['records']}==orbits-{uniform}

def features(ell,G,Y,w):
    # Built afresh from counting definitions, never saved matrix columns.
    v={f'edge_low_count_{l}':(int(ell==l),[15,10,10][l]) for l in range(3)}
    for g in range(3):
        v[f'G{g}_degree_total']=(G[g],35)
        v[f'G{g}_internal_pair_incidence']=(comb(G[g],2),20)
        v[f'low_G{g}_pair_incidence']=(ell*G[g],25)
    for g,h in combinations(range(3),2):v[f'G{g}_G{h}_cross_pair_incidence']=(G[g]*G[h],25)
    for y in range(5):
        v[f'Y{y}_degree']=(int(y in Y),8)
        v[f'low_Y{y}_pair_incidence']=(ell*int(y in Y),5)
        for g in range(3):v[f'G{g}_Y{y}_cross_pair_incidence']=(G[g]*int(y in Y),5)
    for k,(y,z) in enumerate(E):v[f'Y{y}_Y{z}_pair_incidence']=(int(y in Y and z in Y),1+w[k])
    assert len(v)==50
    return v
receipts=[]
for r in R['records']:
    w=r['w'];eq=r['exact_equality_dual'];ub=r['exact_inequality_dual']
    assert all(Q(z['coefficient'])>=0 for z in ub)
    checked=0;minimum=None;rhs=None
    for ell in range(3):
        for size in range(6-ell):
            for Ytuple in combinations(range(5),size):
                Y=set(Ytuple);m=5-ell-size
                for aa in range(m+1):
                    for bb in range(m-aa+1):
                        G=(aa,bb,m-aa-bb);v=features(ell,G,Y,w)
                        assert all(v[z['name']][1]==z['rhs'] for z in eq)
                        assert all(w[index[tuple(z['Y_pair'])]]==3 and z['rhs']==1 for z in ub)
                        coeff=sum((Q(z['coefficient'])*v[z['name']][0] for z in eq),Q())
                        coeff+=sum((Q(z['coefficient'])*ell*int(set(z['Y_pair'])<=Y) for z in ub),Q())
                        bound=sum((Q(z['coefficient'])*v[z['name']][1] for z in eq),Q())+sum((Q(z['coefficient']) for z in ub),Q())
                        if rhs is None:rhs=bound
                        else:assert bound==rhs
                        if not r.get('excluded_by_exact_Farkas'):
                            cost=ell*(sum(comb(g,2) for g in G)+sum(ww for (y,z),ww in zip(E,w) if y in Y and z in Y))
                            coeff-=cost
                        assert coeff>=0
                        minimum=coeff if minimum is None else min(minimum,coeff);checked+=1
    assert checked==512
    if r.get('excluded_by_exact_Farkas'):
        assert rhs<0 and rhs==Q(r['exact_farkas_rhs']);kind='Farkas'
    else:
        assert rhs<130 and rhs==Q(r['exact_optimum']);kind='objective_upper'
    receipts.append({'w':w,'certificate':kind,'exact_rhs':str(rhs),'all512_types':True,'minimum_slack':str(minimum)})
out={'status':'PASS','scope':__doc__,'labelled_row8_wcap3_graphs':148,'S5_orbits':6,'uniform_orbits':1,
     'nonuniform_certificates':5,'producer_orbit_set_equal':True,'receipts':receipts,'CPU_seconds':time.process_time()-start}
(P/'VERIFY_NONUNIFORM_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
