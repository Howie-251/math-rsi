"""Independent Fraction recomputation of the narrowest reported boundary."""
from fractions import Fraction as F
from math import comb,ceil
from pathlib import Path
import json,time,resource
from propertyB_k10_k11_certified import FixedCertificate,S
start=time.monotonic();before=resource.getrusage(resource.RUSAGE_SELF)
def C(n,r):return comb(n,r) if n>=0 and 0<=r<=n else 0
def exact(k,M,v,counts):
    s=(len(counts)-1).bit_length();N=v-s
    locks=([v//2-1,v//2,v//2+1] if s==3 else [v//2,v//2+1] if s==2 else [v//2] if s==1 else [])
    result=F(0)
    for h in range(1,v+1):
        a=h-1-sum(t<h for t in locks);b=v-h-sum(t>h for t in locks)
        left=sum(1<<i for i,t in enumerate(locks) if t<h);right=sum(1<<i for i,t in enumerate(locks) if t>h)
        j=locks.index(h) if h in locks else None
        last=[];first=[];w={}
        for x in range(1<<s):
            r=k-x.bit_count()
            if j is None:
                last.append(F(r*C(a,r-1),N*C(N-1,r-1)) if r>=1 and x&~left==0 else F(0))
                first.append(F(r*C(b,r-1),N*C(N-1,r-1)) if r>=1 and x&~right==0 else F(0))
            else:
                last.append(F(C(a,r),C(N,r)) if x&(1<<j) and (x&~(1<<j))&~left==0 else F(0))
                first.append(F(C(b,r),C(N,r)) if x&(1<<j) and (x&~(1<<j))&~right==0 else F(0))
            for y in range(1<<s):
                z=k-y.bit_count();q=F(0)
                if j is None:
                    if x&~left==0 and y&~right==0 and min(r,z)>=1 and r+z-1<=N:
                        q=F(C(a,r-1)*C(b,z-1),N*C(N-1,r-1)*C(N-r,z-1))
                elif x&y==(1<<j) and (x&~(1<<j))&~left==0 and (y&~(1<<j))&~right==0 and r+z<=N:
                    q=F(C(a,r)*C(b,z),C(N,r)*C(N-r,z))
                w[x,y]=q
        A=sum(n*q for n,q in zip(counts,last));B=sum(n*q for n,q in zip(counts,first))
        crit=sum(nx*(ny-(x==y))*w[x,y] for x,nx in enumerate(counts) for y,ny in enumerate(counts))
        if j is not None:
            deg=sum(n for x,n in enumerate(counts) if x&(1<<j));need=ceil(F((k-1)*deg-(v-1),k-2))
            cells=[]
            for x,nx in enumerate(counts):
                for y in range(x,len(counts)):
                    if not(x&(1<<j) and y&(1<<j)):continue
                    cap=C(nx,2) if x==y else nx*counts[y]
                    if cap:cells.append((w[x,y]+w[y,x],cap))
            for weight,cap in sorted(cells):
                used=min(need,cap);crit-=used*weight;need-=used
                if need==0:break
            assert need==0
        assert crit>=0
        result+=min(A,B,crit)
    return result
out=[]
for k,M,v,d in [(10,1111,266,30),(11,2274,429,43)]:
    counts=[M-2*d+1,d-1,d-1,1];value=exact(k,M,v,counts);cert=FixedCertificate(k,M).two(v,d,d)
    assert value<=F(cert,S)<1
    out.append(dict(k=k,M=M,v=v,degrees=[d,d],rational_numerator=str(value.numerator),rational_denominator=str(value.denominator),certificate_numerator=cert,S=S,passes=True))
k5=[]
for v in (18,25):
    eligible=[]
    for D in range(ceil(F(v-1,4)),176):
        Z=(D+1)*v-175;T=4*(D+1)-v+2
        if Z>0 and 8*Z>T*T:eligible.append(D)
    k5.append(dict(v=v,triple_criterion_D_min=min(eligible) if eligible else None))
for triple in (False,True):
    counts=[17,5,5,1,5,1,1,0] if not triple else [16,6,6,0,6,0,0,1]
    value=exact(5,35,25,counts)
    k5.append(dict(v=25,degrees=[7,7,7],triple=triple,exact_bound_numerator=str(value.numerator),exact_bound_denominator=str(value.denominator),below_one=value<1))
after=resource.getrusage(resource.RUSAGE_SELF)
summary=dict(independent_boundaries=out,k5_diagnostics=k5,wall_seconds=time.monotonic()-start,cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime)
Path(__file__).with_name('INDEPENDENT_CHECKS.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
