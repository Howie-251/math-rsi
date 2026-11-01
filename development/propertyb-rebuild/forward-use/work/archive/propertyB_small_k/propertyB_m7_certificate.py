"""Exact certificate for m(7)>=130 via locked random greedy coloring.

Mathematical hypotheses:
 - A minimal-vertex non-Property-B 7-graph with at most 129 edges
   covers all vertex pairs.
 - Uniform balanced coloring eliminates <=36 vertices; degree counting
   eliminates >=74 vertices.
 - The lock selection lemmas are proved in the companion Markdown.

This program checks the exact conditional union bounds for all 115
required parameter profiles using fractions, plus structural arithmetic.
Python 3.10+ standard library only. Run: python propertyB_m7_certificate.py
"""
from fractions import Fraction as F
from math import comb
from functools import lru_cache
K,M=7,129
C=lambda n,r: comb(n,r) if n>=0 and 0<=r<=n else 0
ceil=lambda a,b: -(-a//b)
@lru_cache(None)
def base(v,pos,h):
 locked=set(pos); a=sum(t not in locked for t in range(1,h)); b=sum(t not in locked for t in range(h+1,v+1)); lo=sum(1<<j for j,t in enumerate(pos) if t<h); hi=sum(1<<j for j,t in enumerate(pos) if t>h); j=pos.index(h) if h in locked else -1
 return a,b,lo,hi,j
@lru_cache(None)
def endpoint(v,pos,h,T,last):
 N=v-len(pos); a,b,lo,hi,j=base(v,pos,h);r=K-T.bit_count()
 if j==-1:
  if N==0 or r==0 or T & ~(lo if last else hi):return F(0)
  return F(r*C(a if last else b,r-1),N*C(N-1,r-1))
 if not T&(1<<j) or (T&~(1<<j)) & ~(lo if last else hi):return F(0)
 return F(C(a if last else b,r),C(N,r))
@lru_cache(None)
def weight(v,pos,h,T,U):
 N=v-len(pos);a,b,lo,hi,j=base(v,pos,h);r=K-T.bit_count();u=K-U.bit_count()
 if j==-1:
  if T&~lo or U&~hi or r<1 or u<1 or r+u-1>N:return F(0)
  return F(C(a,r-1)*C(b,u-1),N*C(N-1,r-1)*C(N-r,u-1))
 if T&U!=(1<<j) or (T&~(1<<j)) &~lo or (U&~(1<<j))&~hi or r+u>N: return F(0)
 return F(C(a,r)*C(b,u),C(N,r)*C(N-r,u))
def deletion(v,pos,ell,j):
 h=pos[j];d=sum(n for T,n in ell.items() if T&(1<<j));q=ceil((K-1)*d-(v-1),K-2)
 cells=[]; typ=[T for T in ell if T&(1<<j)]
 for i,T in enumerate(typ):
  for U in typ[i:]:
   cap=C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap: cells.append((weight(v,pos,h,T,U)+weight(v,pos,h,U,T),cap))
 if q<0:q=0
 if sum(cap for _,cap in cells)<q: raise ValueError('not enough capacity')
 cells.sort(key=lambda a:a[0]);val=F(0)
 for w,cap in cells:
  j=min(cap,q);val+=j*w;q-=j
  if q==0:break
 assert q==0
 return val
def profile_bound(v,pos,ell,use_deletion=True):
 pos=tuple(pos)
 assert len(set(pos))==len(pos) and sum(ell.values())==M and min(ell.values())>=0,(pos,ell)
 D={pos[j]:deletion(v,pos,ell,j) for j in range(len(pos))} if use_deletion else {}
 tot=F(0)
 for h in range(1,v+1):
  A=sum(n*endpoint(v,pos,h,T,True) for T,n in ell.items());B=sum(n*endpoint(v,pos,h,T,False) for T,n in ell.items());
  Q=sum(n*(m-(T==U))*weight(v,pos,h,T,U) for T,n in ell.items() for U,m in ell.items());
  cc=Q-D.get(h,F(0));assert cc>=0
  tot+=min(A,B,cc)
 return tot
def unlocked(v):
 q=ceil(M*C(K,2)-C(v,2),C(K-1,2));gamma=M*(M-1)-2*q
 out=F(0)
 for h in range(1,v+1):
  A=F(M*K,v)*F(C(h-1,K-1),C(v-1,K-1));B=F(M*K,v)*F(C(v-h,K-1),C(v-1,K-1));w=F(C(h-1,K-1)*C(v-h,K-1),v*C(v-1,K-1)*C(v-K,K-1));out+=min(A,B,gamma*w)
 return out

def one(v,d,mid=None):
 return profile_bound(v,(mid or v//2,),{0:M-d,1:d})
def two(v,d1,d2,pos=None):
 return profile_bound(v,pos or (v//2,v//2+1),{0:M-d1-d2+1,1:d1-1,2:d2-1,3:1})
def three(v,ds,tri,pos=None):
 d1,d2,d3=ds
 if tri:ell={0:M-sum(ds)+2,1:d1-1,2:d2-1,4:d3-1,7:1}
 else:ell={0:M-sum(ds)+3,1:d1-2,2:d2-2,4:d3-2,3:1,5:1,6:1}
 return profile_bound(v,pos or (v//2-1,v//2,v//2+1),ell)


def verify():
    assert K==7 and M==129
    assert 73*ceil(72,6)<=903 and 74*ceil(73,6)>903
    # Balanced random coloring excludes v=13,..,36;
    # v<=12 admits an immediate two-coloring.
    for v in range(13,37):
        assert F(M*(C(v//2,K)+C(v-v//2,K)),C(v,K))<1,(v,'balanced')
    assert F(M*(C(37//2,K)+C(37-37//2,K)),C(37,K)) >= 1
    groups={name:[] for name in ('zero','one','two','three')}
    # Stage 1: completely unlocked, global redundant pair subtraction
    for v in range(37,57):
        val=unlocked(v)
        assert val<1,('zero',v,val)
        groups['zero'].append((val,v,'none'))
    # Stage 2: one minimum-degree vertex locked at floor(v/2)
    for v in range(57,62):
        for d in range(ceil(v-1,K-1), K*M//v+1):
            val=one(v,d)
            assert val<1,('one',v,d,val)
            groups['one'].append((val,v,d))
    # Stage 3: min degree x, choose codegree-1 neighbor y of degree <=B.
    # If s=2(v-1)-6d is the minimum number of codegree-1 neighbors,
    # and all s had degree >=B+1, the total degree sum would exceed 903.
    for v in range(62,71):
        for d in range(ceil(v-1,K-1),K*M//v+1):
            s=2*(v-1)-6*d
            assert s>0
            B=next(b for b in range(d, K*M+1)
                   if v*d+s*(b+1-d)>K*M)
            assert v*d+s*(B+1-d)>K*M
            for dy in range(d,B+1):
                val=two(v,d,dy)
                assert val<1,('two',v,d,dy,B,val)
                groups['two'].append((val,v,(d,dy,B)))
    # Stage 4: many 12-degree vertices, and among them 3 pairwise-codegree-1.
    for v in range(71,74):
        assert ceil(v-1,6)==12
        r=13*v-K*M  # >= number of vertices of degree exactly 12
        excess=6*12-(v-1)
        assert r>=3*(excess+1)
        for tri in (0,1):
            val=three(v,(12,12,12),tri)
            assert val<1,('three',v,tri,val)
            groups['three'].append((val,v,tri))
    total=sum(len(vals) for vals in groups.values())
    assert total==115
    for key,vals in groups.items():
        x=max(vals)
        print(f'{key:5s}: {len(vals):3d} exact profiles; max={x[0]} at v={x[1]}, type={x[2]}')
    print(f'PASS: all {total} rational bounds strictly <1; m(7) >=130 conditional on proved combinatorial lemmas')

if __name__=='__main__':
    verify()
