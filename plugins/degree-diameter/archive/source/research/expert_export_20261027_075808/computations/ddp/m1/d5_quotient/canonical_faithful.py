"""Three predetermined faithful actions, after the C27-action-kernel obstruction search.
This generates quotient representatives only, not successful graphs.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from math import gcd
import json,time
import canonical_skeletons as base

CASES=[(109,3),(41,8),(37,9)]

def order(r,p):
    x=r;k=1
    while x!=1:x=x*r%p;k+=1
    return k

def main():
    here=Path(__file__).resolve().parent/'faithful';here.mkdir(exist_ok=True)
    summaries=[]
    for p,m in CASES:
        assert all(p%d for d in range(2,int(p**.5)+1))
        r=next(r for r in range(2,p) if order(r,p)==m)
        base.N=m;base.UNITS=[k for k in range(1,m) if gcd(k,m)==1 and pow(r,k,p)==r]
        start=time.monotonic()
        todo={(a,b,s,t) for a in range(m//2+1) for b in range(m//2+1)
              for s,t in combinations_with_replacement(range(m),2)
              if gcd(m,gcd(a,gcd(b,gcd(s,t))))==1}
        raw=len(todo); reps=[];sizes=[]
        while todo:
            z=min(todo);orb=set(base.orbit(z))
            assert z in orb and orb<=todo
            assert all(set(base.orbit(w))==orb for w in orb)
            todo.difference_update(orb);reps.append(z);sizes.append(len(orb))
        name=f'p{p}_m{m}_r{r}'
        (here/(name+'.skeletons.txt')).write_text(''.join(' '.join(map(str,z))+'\n' for z in reps))
        result=dict(p=p,m=m,r=r,action_order=order(r,p),vertices=2*p*m,degree=5,diameter_target=5,
                    baseline=650,raw_skeletons=raw,canonical_skeletons=len(reps),
                    projective_points_per_skeleton=p*p+p+1,
                    candidate_ceiling=len(reps)*(p*p+p+1),compatible_units=base.UNITS,
                    orbit_sizes={str(s):sizes.count(s) for s in sorted(set(sizes))},
                    orbit_closure_checked=True,seconds=time.monotonic()-start)
        (here/(name+'.summary.json')).write_text(json.dumps(result,indent=2)+'\n')
        summaries.append(result)
    (here/'batch.json').write_text(json.dumps(summaries,indent=2)+'\n')
    print(json.dumps(summaries))

if __name__=='__main__': main()
