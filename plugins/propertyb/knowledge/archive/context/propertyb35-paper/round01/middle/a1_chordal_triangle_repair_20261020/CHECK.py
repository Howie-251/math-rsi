#!/usr/bin/env python3
"""Only scalar/local checks; no original-H or lock-domain enumeration."""
from itertools import combinations, product
from math import comb
from pathlib import Path
import json, time
start=time.process_time()

def joint_mono_count(sets):
    # These locally supplied sets have connected nonempty intersections.
    u=len(set().union(*sets))
    return 2*comb(20-u,10-u) if u<=10 else 0

geometries=[]
for t in (1,2,3):
    nxt=0
    def fresh(n):
        global nxt
        ans=set(range(nxt,nxt+n)); nxt+=n; return ans
    core=fresh(t)
    pair={e:fresh(3-t) for e in combinations(range(3),2)}
    singles=[fresh(t-1) for _ in range(3)]
    sets=[core|singles[i]|set().union(*(v for e,v in pair.items() if i in e)) for i in range(3)]
    assert [len(s) for s in sets]==[5]*3
    assert all(len(sets[i]&sets[j])==3 for i,j in combinations(range(3),2))
    assert len(set.intersection(*sets))==t
    beta=joint_mono_count(sets)
    assert beta=={1:572,2:132,3:22}[t]
    assert all(joint_mono_count([sets[i],sets[j]])==572 for i,j in combinations(range(3),2))
    geometries.append(dict(t=t,sets=[sorted(s) for s in sets],union=len(set.union(*sets)),triple_count=beta,gain=572-beta))

# Explicit certified constructions: isolated/bridge/edge-parent attachments.
orders=[ [(),(0,),(0,1),(0,1),(0,2),(4,)], [(),(),(0,),(0,2),(1,)], [(),(0,),(0,1)] ]
pointwise=0
for earlier in orders:
    edges={tuple(sorted((i,j))) for i,N in enumerate(earlier) for j in N}
    assert all(all(tuple(sorted(e)) in edges for e in combinations(N,2)) for N in earlier)
    cliques=[C for k in range(1,len(earlier)+1) for C in combinations(range(len(earlier)),k) if all(e in edges for e in combinations(C,2))]
    for bits in product((0,1),repeat=len(earlier)):
        Y=sum(bits[i]*all(not bits[j] for j in N) for i,N in enumerate(earlier))
        Euler=sum((-1)**(len(C)+1)*all(bits[i] for i in C) for C in cliques)
        assert Y==Euler and Y>=int(any(bits))
        pointwise+=1
assert 4-4==0<1   # Four-cycle, all four events active.
examples=[(3,3,0,1,9306),(3,3,2,0,9636),(3,4,1,0,9636),(2,7,2,0,9526),(2,8,1,0,9526),(0,11,6,0,9306)]
for q4,q3,g2,g3,expected in examples:
    D=1826+1870*q4+440*q3+440*g2+550*g3
    assert q4+q3<=11 and D==expected and D>9278
book=[]
for m1 in range(3):
    for m2 in range(7):
        for m3 in range(3):
            if m2+3*m3>6: continue
            r=1+m1+m2+m3
            D0=1166+550*m1+990*m2+1100*m3
            D1=1826+440*r+440*m2+550*m3
            book.append((D0,D1,m1,m2,m3))
assert max(v[0] for v in book)==8206
assert max(v[1] for v in book)==8426
assert 1826+1870+8*440+6*440==9856
out=dict(status='PASS',scope='local geometry and scalar conditional theorem only',geometry=geometries,
pointwise_masks_checked=pointwise,examples=[dict(q4=a,q3=b,g2=c,g3=d,deduction=e) for a,b,c,d,e in examples],
book_baseline_max=max(v[0] for v in book),book_rank11_max=max(v[1] for v in book),saturated_book_deduction=9856,cpu_seconds=time.process_time()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
