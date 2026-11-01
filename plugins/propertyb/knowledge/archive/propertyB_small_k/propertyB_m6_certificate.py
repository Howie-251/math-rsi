"""Exact-arithmetic certificate for Property B of six-uniform hypergraphs with <=64 edges.

Proof ingredients (to be proved mathematically): minimal-vertex counterexample
covers all pairs; conditional random greedy coloring and critical pairs; link
intersection lower bound; low-degree codegree-one point selection.

This script verifies *only* the finite rational inequalities needed after those lemmas.
Requires Python 3.10+; no third-party dependencies.
"""
from fractions import Fraction as F
from math import comb, ceil
from functools import lru_cache
from itertools import combinations_with_replacement

K, M = 6, 64

def C(n, r):
    return comb(n, r) if n >= 0 and 0 <= r <= n else 0

def ceilings(a, b):
    return -(-a // b)

@lru_cache(maxsize=None)
def base(v, pos, h):
    """Free positions, lock-index masks to left / right, lock index (or -1)."""
    locked = set(pos)
    a = sum(t not in locked for t in range(1, h))
    b = sum(t not in locked for t in range(h+1, v+1))
    lo = sum(1 << j for j, t in enumerate(pos) if t < h)
    hi = sum(1 << j for j, t in enumerate(pos) if t > h)
    j = pos.index(h) if h in locked else -1
    return a, b, lo, hi, j

@lru_cache(maxsize=None)
def endpoint(v, pos, h, T, last):
    s = len(pos); N = v-s
    a,b,lo,hi,j = base(v,pos,h)
    r = K - T.bit_count()
    if j == -1:
        if N==0 or r==0 or T & ~(lo if last else hi): return F(0)
        return F(r * C(a if last else b, r-1),N*C(N-1,r-1))
    if not (T & (1<<j)): return F(0)
    if (T & ~(1<<j)) & ~(lo if last else hi): return F(0)
    return F(C(a if last else b,r),C(N,r))

@lru_cache(maxsize=None)
def weight(v, pos, h, T, U):
    s = len(pos); N=v-s
    a,b,lo,hi,j = base(v,pos,h)
    r=K-T.bit_count(); u=K-U.bit_count()
    if j==-1:
        if T & ~lo or U & ~hi or r<1 or u<1 or r+u-1>N: return F(0)
        return F(C(a,r-1)*C(b,u-1),N*C(N-1,r-1)*C(N-r,u-1))
    if T&U != (1<<j) or (T&~(1<<j))&~lo or (U&~(1<<j))&~hi or r+u>N:
        return F(0)
    return F(C(a,r)*C(b,u),C(N,r)*C(N-r,u))

def bad_pair_deletion(v, pos, ell, j):
    """Adversarial minimum weight among >=q(u) distinct overlapping link pairs.

    Every pair containing locked vertex j is in exactly one unordered type cell.
    For each cell, capacities count ALL unordered pairs, so the q smallest
    weights across cells are <= the total weight of any q distinct bad pairs.
    """
    h=pos[j]
    d=sum(n for T,n in ell.items() if T & (1<<j))
    surplus=5*d-(v-1)
    assert surplus>=0
    q=ceilings(surplus,4)
    cells=[]
    typ=[T for T in ell if T & (1<<j)]
    for i,T in enumerate(typ):
        for U in typ[i:]:
            cap=C(ell[T],2) if T==U else ell[T]*ell[U]
            if not cap: continue
            w=weight(v,pos,h,T,U)+weight(v,pos,h,U,T)
            cells.append((w,cap))
    assert sum(c for _,c in cells)>=q
    cells.sort(key=lambda p:p[0])
    rem=q; val=F(0)
    for w,cap in cells:
        take=min(rem,cap)
        val+=take*w
        rem-=take
    assert rem==0
    return val

def profile_bound(v, positions, ell, use_deletion=True):
    pos=tuple(positions)
    assert len(set(pos))==len(pos)
    assert sum(ell.values())==M
    assert all(x>=0 for x in ell.values())
    assert sum(ell[T]*(K-T.bit_count()) for T in ell) <= K*M
    deletion={pos[j]:bad_pair_deletion(v,pos,ell,j)
              for j in range(len(pos))} if use_deletion else {}
    total=F(0)
    for h in range(1,v+1):
        A=sum(n*endpoint(v,pos,h,T,True) for T,n in ell.items())
        B=sum(n*endpoint(v,pos,h,T,False) for T,n in ell.items())
        Q=sum(n*(m-(T==U))*weight(v,pos,h,T,U)
              for T,n in ell.items() for U,m in ell.items())
        Cr=Q-deletion.get(h,F(0))
        assert Cr>=0
        total+=min(A,B,Cr)
    return total

def unlocked(v):
    # Global pair-excess bound:
    # q >= ceil((64*15 - binom(v,2))/binom(5,2))
    q=ceilings(64*C(6,2)-C(v,2),C(5,2))
    gamma=64*63-2*q
    total=F(0)
    for h in range(1,v+1):
        A=F(64*6,v)*F(C(h-1,5),C(v-1,5))
        B=F(64*6,v)*F(C(v-h,5),C(v-1,5))
        w=F(C(h-1,5)*C(v-h,5),v*C(v-1,5)*C(v-6,5))
        total+=min(A,B,gamma*w)
    return total

def one(v,d):
    return profile_bound(v,(v//2,),{0:M-d,1:d})

def two(v,d1,d2):
    # lambda_xy=1: empty, x-only, y-only, xy
    return profile_bound(v,(v//2,v//2+1),
                         {0:M-d1-d2+1,1:d1-1,2:d2-1,3:1})

def three(v,ds,tri):
    """Pairwise codegree one => either 3 pair blocks, or one triple block."""
    d1,d2,d3=ds
    if tri:
        ell={0:M-d1-d2-d3+2,1:d1-1,2:d2-1,4:d3-1,7:1}
    else:
        ell={0:M-d1-d2-d3+3,1:d1-2,2:d2-2,4:d3-2,
             3:1,5:1,6:1}
    return profile_bound(v,(v//2-1,v//2,v//2+1),ell)

def test_group(label, cases):
    vals=[(f(),name) for name,f in cases]
    bad=[(str(u),name) for u,name in vals if u>=1]
    assert not bad, f'{label}: NOT proved: {bad}'
    worst=max(vals)
    print(f'{label:16} {len(vals):3} cases; MAX U = {worst[0]} = {float(worst[0]):.12f} at {worst[1]}')
    return worst

def check_structural_arithmetic():
    # Balanced sampling excludes v <= 26; v <= 10 are trivially colorable.
    for v in range(11,27):
        p = F(C(v//2,6)+C(v-v//2,6),C(v,6))
        assert 64*p < 1, (v,p)
    assert 42*ceilings(41,5) <= 384
    assert 43*ceilings(42,5) > 384
    # The neighbor-selection arguments in cases v=35,36,37.
    for v,ds,target in ((35,(10,),13),(36,(10,),13),(37,(8,9,10),12)):
        for d in ds:
            excess = 5*d-(v-1)
            # At least v-1-excess other points have codegree exactly one.
            # If every such point had degree >= target+1, sum degrees
            # would exceed 384 (other points have degree >= d).
            forced = d+(v-1-excess)*(target+1)+excess*d
            assert forced > 384, (v,d,forced)
    # Caro--Wei (or greedy random order): alpha(G) >= r^2/(r+2e(G)).
    # Here low-degree <= 11 vertices are L, and their excess pairs control e(G).
    for v in (38,39,40,41):
        d0=ceilings(v-1,5)
        rmin=ceilings(12*v-384,12-d0)
        assert rmin>=3
        for r in range(rmin,v+1):
            upper_2e=(61-v)*r+1920-60*v
            assert upper_2e>=0
            assert r*r > 2*(r+upper_2e), (v,r)
    # At v=42 at least 36 vertices are degree 9, and the auxiliary
    # graph of codegree>=2 among them has max degree <= 4.
    assert 42*9+6 == 384 and ceilings(36,5)>=3


def main():
    check_structural_arithmetic()
    test_group('v=27..33',[(str(v),lambda v=v:unlocked(v)) for v in range(27,34)])
    test_group('v=34 single',[(f'd={d}',lambda d=d:one(34,d)) for d in range(7,12)])
    for v in (35,36):
        test_group(f'v={v} single',[(f'd={d}',lambda d=d,v=v:one(v,d)) for d in range(7,10)])
        test_group(f'v={v} pair',[(f'(10,{d})',lambda d=d,v=v:two(v,10,d)) for d in range(10,14)])
    test_group('v=37 pair',[(f'({d},{e})',lambda d=d,e=e:two(37,d,e))
                              for d in range(8,11) for e in range(d,13)])
    for v in (38,39,40,41):
        d0=ceilings(v-1,5)
        test_group(f'v={v} triple',[(f'{ds},tri={t}',lambda ds=ds,t=t,v=v:three(v,ds,t))
                                   for ds in combinations_with_replacement(range(d0,12),3)
                                   for t in (0,1)])
    test_group('v=42 triple',[(f'9,9,9; tri={t}',lambda t=t:three(42,(9,9,9),t))
                                 for t in (0,1)])
    print('All exact rational inequalities certified (<1).')

if __name__=='__main__':
    main()
