"""Canonical quotient skeletons for the degree-five C13 semidirect C27 lift.
No claim of inequivalence between retained representatives is needed: the
canonical action only removes skeletons connected by explicit graph isomorphisms.
"""
from itertools import combinations_with_replacement
from pathlib import Path
import json
import time

N=27
UNITS=[k for k in range(1,N) if k%3==1]

def invpair(a):
    return min(a%N,(-a)%N)

def orbit(skeleton):
    a,b,s,t=skeleton
    for swap in (False,True):
        aa,bb=(b,a) if swap else (a,b)
        triple=[0,(-s)%N,(-t)%N] if swap else [0,s,t]
        for anchor in set(triple):
            shifted=[(x-anchor)%N for x in triple]
            shifted.remove(0)
            for k in UNITS:
                st=sorted(k*x%N for x in shifted)
                yield (invpair(k*aa),invpair(k*bb),*st)

def main():
    start=time.monotonic()
    remaining={(a,b,s,t) for a in range(14) for b in range(14)
               for s,t in combinations_with_replacement(range(27),2)
               if any(x%3 for x in (a,b,s,t))}
    total=len(remaining)
    reps=[]; sizes=[]
    while remaining:
        z=min(remaining)
        orb=set(orbit(z))
        assert z in orb and orb <= remaining, 'the stated equivalence must be a full orbit'
        # Check closure on each orbit element without assuming the transformation set is a group.
        assert all(set(orbit(w))==orb for w in orb)
        remaining.difference_update(orb)
        reps.append(z);sizes.append(len(orb))
    here=Path(__file__).resolve().parent
    (here/'skeletons.txt').write_text(''.join(' '.join(map(str,z))+'\n' for z in reps))
    result=dict(group='F13 semidirect C27, action3',internal_degree=2,cross_degree=3,
                target_diameter=5,normalized_raw_skeletons=total,canonical_representatives=len(reps),
                orbit_sizes={str(s):sizes.count(s) for s in sorted(set(sizes))},
                normalization='independent inverse pairs, compatible quotient units, cross anchoring, side swap',
                exhaustive_orbit_closure_checked=True,seconds=time.monotonic()-start)
    (here/'skeletons_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
