"""Exact bounded selection arithmetic; no hypergraph enumeration."""
from fractions import Fraction
import json
from pathlib import Path

def cdiv(a,b): return -(-a//b)

def one(v,D):
    d0=cdiv(v-1,4)
    Z=(D+1)*v-175
    T=4*(D+1)-v+2
    rmin=max(0,cdiv(Z,D+1-d0))
    rows=[]
    for r in range(rmin,v+1):
        raw=min((4*D-v+1)*r,(T-1)*r-4*Z,r*(r-1))
        even=2*(raw//2)
        if even<0:
            rows.append(dict(r=r,raw_upper_2e=raw,excluded=True))
            continue
        bound=Fraction(r*r,r+even) if r else Fraction(0)
        alpha=cdiv(bound.numerator,bound.denominator)
        rows.append(dict(r=r,raw_upper_2e=raw,upper_2e=even,excluded=False,caro_wei=str(bound),alpha_guarantee=alpha))
    valid=[x for x in rows if not x['excluded']]
    assert valid, (v,D)
    guarantee=min(x['alpha_guarantee'] for x in valid)
    continuous=[s for s in range(2,11) if Z>0 and 16*Z>(s-1)*T*T]
    finite=[s for s in range(2,11) if guarantee>=s]
    assert set(continuous)<=set(finite), (v,D,continuous,finite)
    return dict(v=v,D=D,d0=d0,Z=Z,T=T,rmin=rmin,rows=rows,finite_guarantee=guarantee,continuous_s=continuous,finite_s=finite)

rows=[one(v,D) for v in range(18,26) for D in range(cdiv(v-1,4),16)]
summary=[]
for v in range(18,26):
    vr=[x for x in rows if x['v']==v]
    for s in range(2,11):
        coarse=next((x['D'] for x in vr if s in x['continuous_s']),None)
        finite=next((x['D'] for x in vr if s in x['finite_s']),None)
        summary.append(dict(v=v,s=s,continuous_min_D=coarse,finite_min_D=finite,improved=(finite is not None and (coarse is None or finite<coarse))))
obj=dict(parameters=dict(k=5,M=35,v_range=[18,25],D_max=15,s_range=[2,10]),summary=summary,profiles=rows)
out=Path(__file__).parent
(out/'K5_SELECTION_PILOT.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
for v in range(18,26):
    rr=[x for x in summary if x['v']==v]
    print(v,'continuous',[x['continuous_min_D'] for x in rr],'finite',[x['finite_min_D'] for x in rr])
for v,D in ((25,7),(18,9),(18,10),(18,11),(18,12),(18,13),(18,14),(18,15)):
    x=next(x for x in rows if x['v']==v and x['D']==D)
    mins=[a for a in x['rows'] if not a['excluded'] and a['alpha_guarantee']==x['finite_guarantee']]
    print('special',v,D,'Z,T,rmin,guarantee',x['Z'],x['T'],x['rmin'],x['finite_guarantee'],'bottlenecks',mins)
