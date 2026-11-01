"""Floating diagnostics only, not proof certification.
Stable finite-population products, no lgamma subtraction for large v.
"""
from __future__ import annotations
import json, math, time
from pathlib import Path
import numpy as np


def prod_ratio(numer, denom, r):
    # All caller arrays represent legitimate nonnegative binomial counts.
    z=np.ones_like(numer,dtype=float)
    for j in range(r): z*=np.maximum(numer-j,0)/(denom-j)
    return z


def zero(k,M,v,pair_factor=1.):
    h=np.arange(1,v+1,dtype=float);a=h-1;b=v-h;r=k-1
    aa=M*k/v*prod_ratio(a,v-1,r)
    bb=M*k/v*prod_ratio(b,v-1,r)
    cc=np.full(v,M*(M-1)*pair_factor/v)
    # (a)_r (b)_r / (v-1)_{2r}
    for j in range(r):cc*=np.maximum(a-j,0)/(v-1-j)
    for j in range(r):cc*=np.maximum(b-j,0)/(v-1-r-j)
    Q=max(0,math.ceil((M*k*(k-1)/2-v*(v-1)/2)/((k-1)*(k-2)/2)))
    if not pair_factor!=1.:cc*=1-2*Q/(M*(M-1))
    return float(np.minimum(np.minimum(aa,bb),cc).sum())


def one_components(k,M,v,d):
    t=v//2;N=v-1;r=k-1
    h=np.arange(1,v+1,dtype=float);free=h!=t
    a=h-1-(t<h);b=v-h-(t>h)
    # left side only, reflected coordinates on right; endpoint smaller side.
    small=np.minimum(a,b);large=np.maximum(a,b)
    ae=(M-d)*k/N*prod_ratio(small,N-1,r)
    w00=np.full(v,1/N)
    for j in range(r):w00*=np.maximum(small-j,0)/(N-1-j)
    for j in range(r):w00*=np.maximum(large-j,0)/(N-1-r-j)
    # Ratio is evaluated only where endpoint is nonzero.
    ratio=np.divide(N-2*r,large-r+1,out=np.zeros_like(large),where=large>=r)
    ce=(M-d)*(M-d-1)*w00+(M-d)*d*w00*ratio
    wf=float(np.minimum(ae,ce)[free].sum())
    a0=t-1;b0=v-t
    ae0=d*math.prod((a0-j)/(N-j) for j in range(r))
    be0=d*math.prod((b0-j)/(N-j) for j in range(r))
    wc=math.prod((a0-j)/(N-j) for j in range(r))*math.prod((b0-j)/(N-r-j) for j in range(r))
    q=-(-((k-1)*d-(v-1))//(k-2))
    ce0=(d*(d-1)-2*q)*wc
    return wf,min(ae0,be0,ce0)


def one_envelope(k,M,v):
    lo=-(-(v-1)//(k-1));hi=k*M//v
    fr,cenlo=one_components(k,M,v,lo)
    _,cenhi=one_components(k,M,v,hi)
    return dict(E1=fr+cenhi,U1_d0=fr+cenlo,d0=lo,dmax=hi,center_lo=cenlo,center_hi=cenhi)


def continuum(k,M,pair_factor=1.,steps=40000):
    # midpoint quadrature; primary diagnostic only.
    x=(np.arange(steps)+.5)/steps;r=k-1
    a=M*k*np.power(x,r);b=M*k*np.power(1-x,r)
    c=M*(M-1)*pair_factor*np.power(x*(1-x),r)
    return float(np.minimum(np.minimum(a,b),c).mean())


def continuous_budget(k):
    lo=1.;hi=2.**k*math.sqrt(k)
    for _ in range(60):
        mid=(lo+hi)/2
        if continuum(k,mid)<1:lo=mid
        else:hi=mid
    return (lo+hi)/2


def v_max(k,M):
    # exact integer bound, no scan.
    lo=2*k-1;hi=math.isqrt(k*(k-1)*M)+k
    while lo<hi:
        md=(lo+hi+1)//2
        if md*((md-2)//(k-1)+1)<=k*M:lo=md
        else:hi=md-1
    return lo


def first_balanced(k,M):
    lo=2*k-1;hi=math.isqrt(k*(k-1)*M)+k
    def balanced(v):
        return M*(math.comb(v//2,k)+math.comb(v-v//2,k))>=math.comb(v,k)
    while lo<hi:
        md=(lo+hi)//2
        if balanced(md):hi=md
        else:lo=md+1
    return lo


def main():
    out={'status':'FLOAT_DIAGNOSTIC_NOT_CERTIFIED','cases':[]}
    for k in (12,16,32,64):
        mc=continuous_budget(k);M=int(mc);vm=v_max(k,M);vb=first_balanced(k,M)
        points={vb,vm if vm<=500000 else 500000}
        # all point counts diagnostic, never claimed full-v coverage.
        for c in (.5,1,2,4,8,16,32):
            v=int(c*k*k)
            if vb<=v<=min(vm,500000):points.add(v)
        case=dict(k=k,M=M,M_continuum=mc,a=M/2**k,v_balanced_first=vb,v_max=vm,
                  U_continuum=continuum(k,M),rows=[])
        for v in sorted(points):
            if v<vb or v>vm:continue
            z=zero(k,M,v);one=one_envelope(k,M,v)
            row=dict(v=v,U0=z,**one)
            case['rows'].append(row)
        out['cases'].append(case)
        print(json.dumps(case),flush=True)
    Path(__file__).with_name('profile.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
