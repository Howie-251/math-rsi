"""Independently reproducible integer-only Property B certificates.

The full exact probability formulas and structural selection proofs are in
propertyB_k10_k11_research.md. Run:
    python propertyB_k10_k11_verified.py 10
    python propertyB_k10_k11_verified.py 11

Requires Python 3.10+ and numpy. All probability decisions are certified by
exact integer calculations. NO floating point participates in verification.

The cached probabilities are rounded outward to a common denominator S=2**52.
For upper terms use ceil(S*p); for lower bad-pair deductions use floor(S*p).
The numerical slack checks preserve the strict inequality U<1.
NumPy signed int64 is used for acceleration after verifying, exactly, that
no intermediate product or sum in an einsum can overflow. This makes the
NumPy-based calculations equivalent to Python arbitrary-integer arithmetic.
"""
import sys
import numpy as np
from itertools import combinations_with_replacement
from propertyB_k10_k11_certified import FixedCertificate,CEIL,triple_D,S,C

MAXI=(1<<63)-1

class FastExact(FixedCertificate):
    def table(self,v,s):
        key=(v,s,'fast')
        if key in self.cache:return self.cache[key]
        t,A,B,WH,WL=super().table(v,s)
        ah=np.asarray(A,dtype=np.int64)
        bh=np.asarray(B,dtype=np.int64)
        wh=np.asarray(WH,dtype=np.int64)
        wl=np.asarray(WL,dtype=np.int64)
        # One event probability is at most 1; all precomputed integer
        # probabilities are in [0,S]. All terms of the matrix contractions are
        # NONNEGATIVE; their sum is <=m^2*maxweight, regardless of profile.
        assert self.M*self.M*int(wh.max()) < MAXI
        assert self.M*max(int(ah.max()),int(bh.max())) < MAXI
        # The two directional weights of an unordered pair are counted with
        # <=m(m-1)/2 pair capacity, so deletion total <=m(m-1)*maxweight.
        self.cache[key]=(t,ah,bh,wh,wl)
        return self.cache[key]

    def bound(self,v,cnt):
        assert sum(cnt)==self.M and min(cnt)>=0
        s=(len(cnt)-1).bit_length()
        t,A,B,WH,WL=self.table(v,s)
        n=np.asarray(cnt,dtype=np.int64)
        ends=A@n;begins=B@n
        crit=np.einsum('hij,i,j->h',WH,n,n,optimize=True)-np.einsum('hii,i->h',WH,n)
        # These two contractions implement sum_{i,j} n_i(n_j-[i=j]) w_ij.
        # Each intermediate is safe thanks to the table() overflow check.
        for j,h in enumerate(t):
            deg=sum(cnt[x] for x in range(len(cnt)) if x&(1<<j))
            q=CEIL((self.k-1)*deg-(v-1),self.k-2)
            assert q>=0
            cells=[]
            for x in range(len(cnt)):
                if not x&(1<<j):continue
                for y in range(x,len(cnt)):
                    if not y&(1<<j):continue
                    cap=C(cnt[x],2) if x==y else cnt[x]*cnt[y]
                    if cap:
                        lower=int(WL[h-1,x,y])+int(WL[h-1,y,x])
                        cells.append((lower,cap))
            cells.sort()
            D=0
            for w,cap in cells:
                nbad=min(q,cap)
                D+=nbad*w
                q-=nbad
                if not q:break
            assert q==0
            crit[h-1]-=D
        assert np.all(crit>=0)
        # Sum with Python arbitrary precision even if a generic a priori
        # bound for v*max(A,B,C) exceeds int64.
        return sum(int(z) for z in np.minimum(np.minimum(ends,begins),crit))

def verify(k):
    if k==10:
        M=1111
        phases=[(67,207,'none'),(208,229,'one'),(230,266,'two'),(267,316,'three')]
    elif k==11:
        M=2274
        phases=[(79,332,'none'),(333,368,'one'),(369,429,'two'),(430,500,'three')]
    else:raise ValueError('This paper certifies k=10 and k=11 only')
    cal=FastExact(k,M)
    first,last=phases[0][0],phases[-1][1]
    assert (last+1)*CEIL(last,k-1)>k*M
    for v in range(2*k-1,first):
        assert M*(C(v//2,k)+C(v-v//2,k))<C(v,k)
    profiles=0
    rows=[]
    for lo,hi,mode in phases:
        worst=(-1,None,None)
        count=0
        for v in range(lo,hi+1):
            assert v*CEIL(v-1,k-1)<=k*M
            d0=CEIL(v-1,k-1)
            if mode=='none':param=[()]
            elif mode=='one':param=[(d,) for d in range(d0,k*M//v+1)]
            elif mode=='two':
                param=[]
                for d in range(d0,k*M//v+1):
                    s=2*(v-1)-(k-1)*d
                    assert s>0
                    B=next(b for b in range(d,M+1) if v*d+s*(b+1-d)>k*M)
                    param.extend((d,e) for e in range(d,B+1))
            else:
                D=triple_D(k,M,v)
                assert (D+1)*v>k*M
                assert 2*(k-1)*((D+1)*v-k*M)>((k-1)*(D+1)-v+2)**2
                param=((ds,typ) for ds in combinations_with_replacement(range(d0,D+1),3)
                      for typ in (False,True))
            for p in param:
                if mode=='none':z=cal.unlocked(v)
                elif mode=='one':z=cal.one(v,*p)
                elif mode=='two':z=cal.two(v,*p)
                else:z=cal.three(v,*p)
                assert z<S, (k,M,v,mode,p,z,S)
                if z>worst[0]:worst=(z,v,p)
                count+=1
        profiles+=count
        rows.append((mode,lo,hi,count,worst))
        print(f'{k=}, {mode:5s}, v={lo}..{hi}, profiles={count}, worst={worst[0]}/{S} at v={worst[1]}, configuration={worst[2]}, integer_gap={S-worst[0]}',flush=True)
    print(f'FULL CERTIFICATE PASSED: m({k}) >= {M+1}, {profiles} parameter configurations, all exact integer arithmetic.',flush=True)
    return rows

if __name__=='__main__':
    verify(int(sys.argv[1]))
