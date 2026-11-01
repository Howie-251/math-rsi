"""Exact full-support selector certificates on the saved17-point signed witness; not a general occurrence3 proof."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product
from collections import Counter
import json,time
HERE=Path(__file__).parent

def witness():
    H={f'h{i}' for i in range(1,4)};M=[f'm{i}' for i in range(1,10)];W={f'l{i}' for i in range(1,6)}
    A=[{'h1','h2','m1','m2'},{'h1','m3','m4','l1'},{'h2','h3','m5','m6'},{'m7','m8','m9','l2'},{'h1','h3','m1','m3'},{'h2','h3','m2','m4'},{'m5','m7','m9','l3'},{'m6','m8','l4','l5'}]
    B=[H,H,H,H|{'m1'}]+[{M[(i+j)%9] for j in range(4)} for i in range(9)]+[{'m2','m3','m4','m5'},{'m6','m7','m8','m9'}]+[W-{f'l{i}'} for i in [1,2,3,4,5,3]]
    D=[{'l3','l4','l5'},{'l1','l2','l3'}]
    return A,B,D

def mul(xs):
    z=Q(1)
    for x in xs:z*=x
    return z

def exact_hit_probability(F,A,pi):
    return sum(((-1)**len(S)*mul(1-sum((pi[i].get(x,Q()) for x in S),Q()) for i in range(len(A))) for n in range(len(F)+1) for S in combinations(F,n)),Q())

def main():
    st=time.time();A,B,D=witness();occ=Counter(x for s in A for x in s)
    assert len(A)==8 and len(B)==21 and len(set().union(*A))==17
    assert set(Counter(x for s in A+B+D for x in s).values())=={7}
    cases=[]
    for rule in ('uniform','half_high','inverse_power'):
        w={x:Q(1) if rule=='uniform' else Q(1,2) if occ[x]==3 else Q(2) if rule=='inverse_power' and occ[x]==1 else Q(1) for x in occ}
        pi=[{x:w[x]/sum((w[y] for y in s),Q()) for x in s} for s in A]
        assert all(sum(z.values(),Q())==1 and min(z.values())>0 for z in pi)
        q={x:1-mul(1-z.get(x,Q()) for z in pi) for x in occ}
        product_bound=sum((mul(q[x] for x in s) for s in B),Q())
        pair_bounds=[]
        for F in B:
            candidates=[]
            for x,y in combinations(F,2):
                ux=mul(1-z.get(x,Q()) for z in pi);uy=mul(1-z.get(y,Q()) for z in pi)
                uxy=mul(1-z.get(x,Q())-z.get(y,Q()) for z in pi)
                candidates.append((1-ux-uy+uxy)*mul(q[z] for z in F-{x,y}))
            pair_bounds.append(min(candidates))
        probs=[exact_hit_probability(s,A,pi) for s in B]
        assert all(a<=b for a,b in zip(probs,pair_bounds))
        cases.append(dict(rule=rule,full_support=True,weights={x:str(w[x]) for x in sorted(w)},marginals={x:str(q[x]) for x in sorted(q)},product_bound=str(product_bound),pair_union_bound=str(sum(pair_bounds,Q())),exact_union_bound=str(sum(probs,Q())),negative_probabilities=list(map(str,probs))))
    # Independent enumeration of the65536 indexed uniform draws, not original hypergraphs.
    counts=[0]*len(B)
    for draws in product(*(tuple(sorted(s)) for s in A)):
        R=set(draws)
        for j,F in enumerate(B):counts[j]+=F<=R
    uniform=cases[0]
    assert [Q(n,4**8) for n in counts]==list(map(Q,uniform['negative_probabilities']))
    assert uniform['exact_union_bound']=='675/1024'
    assert uniform['pair_union_bound']=='236357/262144'
    assert cases[1]['product_bound']=='1881574225/1975228416'
    assert cases[2]['product_bound']=='544448383/664301250'
    # Actual paircover violation, recorded separately from signed feasibility.
    x,y='h2','h3';lam=sum(x in s and y in s for s in A+B+D);r=sum(x in s for s in B[:3]+D)
    assert lam==6 and r==3 and lam>6-r
    out=dict(status='PASS',scope=__doc__,cases=cases,independent_uniform_draws=4**8,independent_event_counts=counts,actual_paircover_violation=dict(pair=[x,y],codegree=lam,number_P2_edges=r,required_upper_bound=6-r),elapsed_seconds=time.time()-st)
    (HERE/'WEIGHTED_SELECTOR_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print([(r['rule'],r['product_bound'],r['exact_union_bound']) for r in cases]);print('PASS',out['elapsed_seconds'])
if __name__=='__main__':main()
