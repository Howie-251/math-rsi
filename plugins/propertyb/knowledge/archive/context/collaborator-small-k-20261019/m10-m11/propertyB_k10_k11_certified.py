"""Exact integer-arithmetic (outward-rounded fixed point) Property B certificates.

NO FLOATING POINT OPERATIONS PARTICIPATE IN ANY CERTIFICATION.
Every probability p is replaced by ceil(2**52*p)/2**52 in upper bounds,
and by floor(2**52*p)/2**52 when used as a lower deletion weight.
Consequently a computed upper bound U_num / 2**52 is rigorous.

numpy.int64 is used only after ensuring all signed intermediate values stay
within range for the certified k=10/11 input ranges (assertion on outputs;
scalar proof bound can be checked by CERTIFY_INT64). To avoid any reliance on
machine integer overflow, certification uses Python arbitrary integers in
critical pair accumulation, with numpy solely for cached indexing; hence
integer correctness does not depend on int64 overflows.
"""
from math import comb
from itertools import combinations_with_replacement
from functools import lru_cache
from fractions import Fraction
import argparse
import sys

S=1<<52

def C(n,r): return comb(n,r) if n>=0 and 0<=r<=n else 0
def CEIL(a,b):return -(-a//b)
def hi(n,d):
    assert d>0 and n>=0
    return (n*S+d-1)//d
def lo(n,d):
    assert d>0 and n>=0
    return (n*S)//d

class FixedCertificate:
    def __init__(self,k,M):self.k,self.M=k,M;self.cache={};self.profiles=0;self.stageworst={}
    def table(self,v,s):
        key=(v,s)
        if key in self.cache:return self.cache[key]
        k=self.k;N=v-s;sz=1<<s
        t=tuple((v//2-1,v//2,v//2+1) if s==3 else (v//2,v//2+1) if s==2 else (v//2,) if s==1 else ())
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
    def bound(self,v,cnt):
        m=self.M;k=self.k
        assert sum(cnt)==m and min(cnt)>=0
        s=(len(cnt)-1).bit_length()
        t,A,B,WH,WL=self.table(v,s)
        active=[i for i,z in enumerate(cnt) if z]
        D={}
        for j,h in enumerate(t):
            degree=sum(cnt[x] for x in active if x&(1<<j))
            q=CEIL((k-1)*degree-(v-1),k-2)
            assert q>=0
            cells=[]
            for ix,x in enumerate(active):
                if not x&(1<<j):continue
                for y in active[ix:]:
                    if not y&(1<<j):continue
                    cap=C(cnt[x],2) if x==y else cnt[x]*cnt[y]
                    if cap:
                        # Sum of rounded-down directional weights: safe lower bound
                        wt=WL[h-1][x][y]+WL[h-1][y][x]
                        cells.append((wt,cap))
            cells.sort()
            deduction=0
            for wt,cap in cells:
                use=min(q,cap)
                deduction+=use*wt
                q-=use
                if q==0:break
            assert q==0
            D[h]=deduction
        total=0
        for h in range(1,v+1):
            a=sum(cnt[x]*A[h-1][x] for x in active)
            b=sum(cnt[x]*B[h-1][x] for x in active)
            c=sum(cnt[x]*(cnt[y]-(x==y))*WH[h-1][x][y]
                for x in active for y in active) - D.get(h,0)
            assert c>=0,(v,cnt,h,c)
            total+=min(a,b,c)
        return total
    def unlocked(self,v):
        k,m=self.k,self.M
        overlap=max(0,CEIL(m*C(k,2)-C(v,2),C(k-1,2)))
        count=m*(m-1)-2*overlap
        total=0
        for h in range(1,v+1):
            a=m*hi(k*C(h-1,k-1),v*C(v-1,k-1))
            b=m*hi(k*C(v-h,k-1),v*C(v-1,k-1))
            c=count*hi(C(h-1,k-1)*C(v-h,k-1),v*C(v-1,k-1)*C(v-k,k-1))
            total+=min(a,b,c)
        return total
    def one(self,v,d):return self.bound(v,[self.M-d,d])
    def two(self,v,d,e):return self.bound(v,[self.M-d-e+1,d-1,e-1,1])
    def three(self,v,deg,triple):
        a,b,c=deg
        if triple:return self.bound(v,[self.M-a-b-c+2,a-1,b-1,0,c-1,0,0,1])
        return self.bound(v,[self.M-a-b-c+3,a-2,b-2,1,c-2,1,1,0])

def triple_D(k,m,v):
    d0=CEIL(v-1,k-1)
    return next(D for D in range(d0,d0+50) if
          ((D+1)*v-k*m)>0 and
          2*(k-1)*((D+1)*v-k*m)>((k-1)*(D+1)-v+2)**2)

def certify(k,m,parts,report_every=10):
    calc=FixedCertificate(k,m)
    first=parts[0][0];last=parts[-1][1]
    assert all(parts[i][1]+1==parts[i+1][0] for i in range(len(parts)-1))
    assert (last+1)*CEIL(last,k-1)>k*m
    for v in range(2*k-1,first):
        assert m*(C(v//2,k)+C(v-v//2,k))<C(v,k)
    ct=0
    for l,r,stage in parts:
        worst=(-1,None,None)
        for v in range(l,r+1):
            assert v*CEIL(v-1,k-1)<=k*m
            d0=CEIL(v-1,k-1)
            if stage=='unlocked':args=[()]
            elif stage=='one':args=[(d,) for d in range(d0,k*m//v+1)]
            elif stage=='two':
                args=[]
                for d in range(d0,k*m//v+1):
                    n=2*(v-1)-(k-1)*d
                    assert n>0
                    B=next(b for b in range(d,m+1) if v*d+n*(b+1-d)>k*m)
                    args += [(d,e) for e in range(d,B+1)]
            else:
                D=triple_D(k,m,v)
                args=[(ds,flag) for ds in combinations_with_replacement(range(d0,D+1),3) for flag in (False,True)]
            for args_one in args:
                if stage=='unlocked':z=calc.unlocked(v)
                elif stage=='one':z=calc.one(v,*args_one)
                elif stage=='two':z=calc.two(v,*args_one)
                else:z=calc.three(v,*args_one)
                if z>=S:
                    raise AssertionError(f'BAD k={k} m={m} {stage} v={v} profile={args_one} computed={z}/{S}')
                if z>worst[0]:worst=(z,v,args_one)
            ct+=len(args)
            if report_every and v%report_every==0:
                print(f'  {stage} v={v}, checked={ct}',flush=True)
        z,v,config=worst
        calc.stageworst[stage]=(z,v,config)
        print(f'PASS k={k} m={m} stage={stage} v={l}..{r}, worst={z}/{S} at v={v}, profile={config}, gap={(S-z)/S:.8g}; all checked={ct}',flush=True)
    print(f'FULL PASS: m({k}) >= {m+1}, verified {ct} exact integer profiles.',flush=True)
    return calc.stageworst,ct

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('k',type=int,choices=[10,11]);opt=ap.parse_args()
    if opt.k==10:certify(10,1111,[(67,207,'unlocked'),(208,229,'one'),(230,266,'two'),(267,316,'three')])
    else:certify(11,2274,[(79,332,'unlocked'),(333,368,'one'),(369,429,'two'),(430,500,'three')])
