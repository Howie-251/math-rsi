"""Decimal exploration of RS-FKG-integral and Turan-cap candidates.
No numerical output is a proof; candidate formula supplied by root.
All roots are real-budget diagnostic roots; cap uses V floored at int(M).
"""
from decimal import Decimal as D, getcontext
from math import comb, isqrt
from pathlib import Path
import json, time
getcontext().prec=105
TWO=D(2);FOUR=D(4);ONE=D(1)

def dec(x):return D(str(x))
def integral(k,p):
    # Exact polynomial integral, evaluated in Decimal.
    r=k-1;psq=p*p;power=p;s=D(0)
    for j in range(k):
        term=D(comb(r,j))*power/D(2*j+1)
        s=s+term if j%2==0 else s-term
        power*=psq
    return s

def vertex_cap(k,M):
    m=int(M);return (1+isqrt(1+4*k*(k-1)*m))//2

def gamma(k,M,mode):
    old=M*(M-1)
    if mode=='old':return old
    v=vertex_cap(k,M)
    if mode=='turan':return min(old,M*M*(1-ONE/D(v)))
    raise ValueError(mode)

def value(k,M,p,mode='old',fkg=True):
    kap=M/TWO**(k-1);g=gamma(k,M,mode)
    z=(1-p)**k
    outer=1-((1-z).ln()*kap).exp() if fkg else kap*z
    return outer+g/FOUR**(k-1)*integral(k,p)

def derivative_sign_log(k,M,p,mode):
    kap=M/TWO**(k-1);g=gamma(k,M,mode);q=1-(1-p)**k
    return g.ln()-D(k-1)*FOUR.ln()+D(k-1)*(1+p).ln()-kap.ln()-D(k).ln()-(kap-1)*q.ln()

def optimal_p(k,M,mode):
    # We want the second derivative zero-crossing: negative to positive F'.
    # Expected local minimum near log(k/kap)/k. Coarse search is only bracketing.
    lastp=D('0.000001');last=derivative_sign_log(k,M,lastp,mode)
    bracket=None
    for j in range(1,201):
        p=D(j)/D(250) # up to .8; all present optima well inside.
        z=derivative_sign_log(k,M,p,mode)
        if last<0 and z>=0:bracket=(lastp,p);break
        lastp,last=p,z
    if bracket is None:return D(0)  # endpoint gives F=1; not colorable by strict criterion
    lo,hi=bracket
    for _ in range(175):
        md=(lo+hi)/2
        if derivative_sign_log(k,M,md,mode)<0:lo=md
        else:hi=md
    return (lo+hi)/2

def budget_root(k,mode):
    lo=TWO**(k-1);hi=TWO**k*D(k).sqrt()
    # Narrow float-ish stage, then enough iterations for absolute <1e-12.
    for _ in range(k+70):
        M=(lo+hi)/2;p=optimal_p(k,M,mode)
        if value(k,M,p,mode)<1:lo=M
        else:hi=M
    M=(lo+hi)/2;p=optimal_p(k,M,mode)
    return M,p,value(k,M,p,mode)

def min_root(k):
    lo=TWO**(k-1);hi=TWO**k*D(k).sqrt()
    for _ in range(k+70):
        M=(lo+hi)/2;kap=M/TWO**(k-1);g=gamma(k,M,'old')
        p=((kap.ln()+D(k).ln()-g.ln()+D(k-1)*FOUR.ln())/D(k-1)).exp()-1
        if value(k,M,p,'old',False)<1:lo=M
        else:hi=M
    return (lo+hi)/2

def main():
    started=time.time();out={'status':'DECIMAL_EXPLORATION_NOT_CERTIFIED','precision':105,'cases':[]}
    for k in (16,32,64,128):
        old,p0,f0=budget_root(k,'old');new,p1,f1=budget_root(k,'turan');v=vertex_cap(k,new)
        classic=min_root(k)
        # Verify nearby integer budgets numerically on each side of integer threshold.
        last_old=int(old);last_new=int(new)
        checks=[]
        for mode,m in [('old',last_old),('old',last_old+1),('turan',last_new),('turan',last_new+1)]:
            p=optimal_p(k,D(m),mode);checks.append({'mode':mode,'M':m,'p':str(p),'F_minus_1':str(value(k,D(m),p,mode)-1)})
        row=dict(k=k,old_root=str(old),turan_root=str(new),real_budget_gain=str(new-old),
             old_last_colorable_integer=last_old,new_last_colorable_integer=last_new,
             candidate_integer_gain=last_new-last_old,V=v,p_old=str(p0),p_new=str(p1),
             old_root_minus_classic_min_root=str(old-classic),classic_min_root=str(classic),
             sqrtM_over_k=str(new.sqrt()/D(k)),checks=checks)
        out['cases'].append(row);print(json.dumps(row),flush=True)
        Path(__file__).with_name('fkg_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
    out['wall_seconds']=time.time()-started
    Path(__file__).with_name('fkg_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
