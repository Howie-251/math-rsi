"""Explicit-position version of the original scalar certificate table.
Only the lock-position selector is changed; conditional probability formulas,
rounding, bad-pair deletion, and bound evaluation are the original code.
"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path('context/collaborator-small-k-20261019/m10-m11').resolve()))
from propertyB_k10_k11_certified import FixedCertificate,C,CEIL,hi,lo,S

class LayoutCertificate(FixedCertificate):
    def __init__(self,k,M,positions):
        super().__init__(k,M)
        self.positions=tuple(positions)
    def table(self,v,s):
        key=(v,s)
        if key in self.cache:return self.cache[key]
        k=self.k;N=v-s;sz=1<<s
        t=self.positions
        assert len(t)==s and tuple(sorted(set(t)))==t and all(1<=z<=v for z in t)
        A=[[0]*sz for h in range(v)]
        B=[[0]*sz for h in range(v)]
        WH=[[[0]*sz for _ in range(sz)] for h in range(v)]
        WL=[[[0]*sz for _ in range(sz)] for h in range(v)]
        for h in range(1,v+1):
            a=sum(z not in t for z in range(1,h))
            b=sum(z not in t for z in range(h+1,v+1))
            left=sum(1<<i for i,z in enumerate(t) if z<h)
            right=sum(1<<i for i,z in enumerate(t) if z>h)
            j=t.index(h) if h in t else -1
            for typ in range(sz):
                r=k-typ.bit_count()
                if j<0:
                    if r>0 and not typ&~left: A[h-1][typ]=hi(r*C(a,r-1),N*C(N-1,r-1))
                    if r>0 and not typ&~right: B[h-1][typ]=hi(r*C(b,r-1),N*C(N-1,r-1))
                elif typ & (1<<j):
                    if not (typ&~(1<<j))&~left:A[h-1][typ]=hi(C(a,r),C(N,r))
                    if not (typ&~(1<<j))&~right:B[h-1][typ]=hi(C(b,r),C(N,r))
            for x in range(sz):
                r=k-x.bit_count()
                for y in range(sz):
                    z=k-y.bit_count()
                    if j<0:
                        if x&~left or y&~right or min(r,z)<1 or r+z-1>N:continue
                        numerator=C(a,r-1)*C(b,z-1)
                        denom=N*C(N-1,r-1)*C(N-r,z-1)
                    else:
                        if x&y!=(1<<j) or (x&~(1<<j))&~left or (y&~(1<<j))&~right or r+z>N:continue
                        numerator=C(a,r)*C(b,z)
                        denom=C(N,r)*C(N-r,z)
                    WH[h-1][x][y]=hi(numerator,denom)
                    WL[h-1][x][y]=lo(numerator,denom)
        self.cache.clear() # only one v and lock size needed at a time
        self.cache[key]=(t,A,B,WH,WL)
        return self.cache[key]
