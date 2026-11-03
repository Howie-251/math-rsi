"""Exact quotient orbits for two inverse pairs per side and one identity cross edge."""
from pathlib import Path
from itertools import combinations_with_replacement
from math import gcd
import json,time

CASES=[(13,27,3),(109,3,45),(41,8,3),(37,9,7)]

def normalize(z,m):
    z=[min(x%m,(-x)%m) for x in z]
    a=tuple(sorted(z[:2]));b=tuple(sorted(z[2:]));a,b=sorted([a,b])
    return a+b

def main():
    here=Path(__file__).resolve().parent;summary=[]
    for p,m,r in CASES:
        start=time.monotonic();units=[k for k in range(1,m) if gcd(k,m)==1 and pow(r,k,p)==r]
        pairs=list(combinations_with_replacement(range(m//2+1),2))
        remaining={a+b for a,b in combinations_with_replacement(pairs,2)
                   if gcd(m,gcd(*a,*b))==1}
        raw=len(remaining);reps=[];sizes=[]
        def orbit(z):return {normalize(tuple(k*x%m for x in z),m) for k in units}
        while remaining:
            z=min(remaining);orb=orbit(z)
            assert z in orb and orb<=remaining
            assert all(orbit(w)==orb for w in orb)
            remaining.difference_update(orb);reps.append(z);sizes.append(len(orb))
        name=f'p{p}_m{m}_r{r}'
        (here/(name+'.skeletons.txt')).write_text(''.join(' '.join(map(str,z))+'\n' for z in reps))
        out=dict(p=p,m=m,r=r,n=2*p*m,coordinate_order=['a','c','b','d'],
                 internal='A={a,a^-1,c,c^-1}, B={b,b^-1,d,d^-1}',cross='identity only',
                 raw_quotient_skeletons=raw,canonical_skeletons=len(reps),
                 projective_per_skeleton=p*p+p+1,candidate_ceiling=len(reps)*(p*p+p+1),
                 compatible_units=units,orbit_sizes={str(s):sizes.count(s) for s in sorted(set(sizes))},
                 orbit_closure_checked=True,seconds=time.monotonic()-start)
        (here/(name+'.metadata.json')).write_text(json.dumps(out,indent=2)+'\n');summary.append(out)
    (here/'batch.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary))

if __name__=='__main__':main()
