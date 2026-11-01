"""Two degree8 locks on25/M35: all300 unordered position pairs, raw ABC.
If these do not force w<=2, enumerate only integer five-vertex row8 graphs.
No original-H search, no MILP, no new nine-lock DP.
"""
from pathlib import Path
from itertools import combinations,permutations,product
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from bare_layout import BareLayout
from independent_structure_bounds import independent_rows
start=time.process_time()
layouts=[(pos,BareLayout(25,pos)) for pos in combinations(range(1,26),2)]
assert len(layouts)==300
paircases=[]
for c in range(1,9):
    ns={t:n for t,n in {0:19+c,1:8-c,2:8-c,3:c}.items() if n}
    value,pos=min((lay.bound(ns),pos) for pos,lay in layouts)
    rows=independent_rows(25,pos,[frozenset(i+1 for i in range(2) if t>>i&1) for t,n in ns.items() for _ in range(n)])
    raw=sum((min(z['A'],z['B'],z['C']) for z in rows),Fraction())
    assert value==raw
    paircases.append({'lambda':c,'w':c-1,'counts':ns,'positions':pos,'raw_bound':value,'strict':value<1,'independent_rows':rows})
pairCPU=time.process_time()-start
possible=[z['w'] for z in paircases if not z['strict']]
cap=max(possible,default=-1)
out={'scope':'All selected degree8 pair codegrees1..8 and all300 unordered position pairs; equality of degrees makes reverse orders equivalent.',
     'pair_cases':paircases,'max_w_not_excluded_by_raw_pair_gate':cap,'pair_CPU_seconds':pairCPU}
if cap>2:
    # Each row is completed before proceeding. Last-row nonnegativity and
    # degree-zero closure provide a complete integer multigraph enumeration.
    es=list(combinations(range(5),2));N=len(es);seen={};labelled=0
    pmaps=[]
    idx={e:i for i,e in enumerate(es)}
    for p in permutations(range(5)):
        pmaps.append([idx[tuple(sorted((p[i],p[j])))] for i,j in es])
    w=[0]*10
    def dfs(k,rem):
        global labelled
        if k==N:
            if any(rem):return
            labelled+=1
            key=min(tuple(w[m[i]] for i in range(10)) for m in pmaps)
            if key not in seen:
                value=sum(x*min(5,1+x) for x in key)
                seen[key]={'w':key,'sum_cost':value,'labelled_multiplicity':0}
            seen[key]['labelled_multiplicity']+=1
            return
        i,j=es[k]
        # A completed vertex may not leave a positive residual row.
        for x in range(min(cap,rem[i],rem[j])+1):
            nxt=rem.copy();nxt[i]-=x;nxt[j]-=x
            if k+1==N or es[k+1][0]!=i:
                if nxt[i]:continue
            if any(nxt[v]>cap*sum(v in e for e in es[k+1:]) for v in range(5)):continue
            w[k]=x;dfs(k+1,nxt)
    dfs(0,[8]*5)
    reps=list(seen.values())
    out['integer_Y_graphs']={'edge_order':es,'w_cap':cap,'labelled_count':labelled,'S5_orbits':len(reps),
         'maximum_cost':max(z['sum_cost'] for z in reps),'minimum_cost':min(z['sum_cost'] for z in reps),
         'all_representatives':reps,'CPU_seconds':time.process_time()-start-pairCPU}
    assert sum(z['labelled_multiplicity'] for z in reps)==labelled
else:
    out['integer_Y_graphs']={'forced_uniform_w2':cap==2,'reason':'Four nonnegative neighbors each w<=2 and row sum8 force all four w=2.'}
out['total_CPU_seconds']=time.process_time()-start
def serial(x):
    if isinstance(x,Fraction):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x
(P/'K5_EXCEPTION_RESULT.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(serial({k:v for k,v in out.items() if k not in ['pair_cases','integer_Y_graphs']}),indent=2))
print('pairs',[(z['lambda'],str(z['raw_bound']),z['positions']) for z in paircases])
if 'all_representatives' in out['integer_Y_graphs']:
    print({k:v for k,v in out['integer_Y_graphs'].items() if k!='all_representatives'})
else:print(out['integer_Y_graphs'])
