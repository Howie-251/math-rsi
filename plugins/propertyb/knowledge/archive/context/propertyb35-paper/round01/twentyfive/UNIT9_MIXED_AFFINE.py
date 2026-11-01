"""M35 nine-unit locks, all q=0..9 low-degree choices via exact affine compression.
For fixed large-block family, q and consecutive layout: free-center contribution
is constant, while each lock-center corrected true min depends only on its own
6/7 degree. All low subsets are overapproximated, never discarded structurally.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(S),str(R/'computations'),str(R/'computations/propertyb33/round01')]
from unit_catalogue import fullblocks
from bare_layout import BareLayout
from multilock import Profile,json_value
from pure_quota import certificate


def lock_functions(engine,bs,single,eligible):
    # Empty traces do not enter any lock-center row. Set their count to zero.
    hi={**{t:1 for t in bs},**{1<<i:z for i,z in enumerate(single) if z}}
    lo={**{t:1 for t in bs},**{1<<i:z-int(i in eligible) for i,z in enumerate(single) if z-int(i in eligible)}}
    vals=[]
    for ns in (hi,lo):
      _,abc=engine.bound(ns,True);profile=Profile(25,5,engine.pos,ns);g=[]
      for i,pos in enumerate(engine.pos):
        loss=certificate(profile,i)['loss'];a,b,c=abc[pos-1]
        g.append(min(a,b,c-loss))
      vals.append(g)
    high,low=vals
    return high,[low[i]-high[i] if i in eligible else Q() for i in range(9)]


def free_value(engine,empty,beta):
    # No free center lies inside a consecutive lock block. For such a center,
    # all nonempty traces lie on the same side and only their size buckets enter.
    total=0
    for k,(left,right,pivot,aw,bw,cw) in enumerate(engine.rows,1):
      if pivot:continue
      if k<min(engine.pos):
        A=empty*aw.get(5,0)
        B=empty*bw.get(5,0)+sum(n*bw.get(r,0) for r,n in beta.items())
        C=empty*(empty-1)*cw.get((5,5),0)+empty*sum(n*cw.get((5,r),0) for r,n in beta.items())
      else:
        A=empty*aw.get(5,0)+sum(n*aw.get(r,0) for r,n in beta.items())
        B=empty*bw.get(5,0)
        C=empty*(empty-1)*cw.get((5,5),0)+empty*sum(n*cw.get((r,5),0) for r,n in beta.items())
      total+=min(A,B,C)
    return Q(total,engine.D)


def counts(bs,single,empty,low):
    return {**{t:1 for t in bs},**{1<<i:z-int(i in low) for i,z in enumerate(single) if z-int(i in low)},0:empty}


def direct(engine,ns):
    _,abc=engine.bound(ns,True);profile=Profile(25,5,engine.pos,ns)
    losses={engine.pos[i]:certificate(profile,i)['loss'] for i in range(9)}
    return sum((min(a,b,c-losses.get(k,Q())) for k,(a,b,c) in enumerate(abc,1)),Q())


def run(limit=None):
 st=time.perf_counter();src=json.loads((S/'UNIT_CATALOGUE_9.json').read_text())['orbits']
 if limit is not None:src=src[:limit]
 engines=[BareLayout(25,range(a,a+9)) for a in range(1,18)]
 families=[];summary={q:dict(feasible_families=0,feasible_colors=0,uniform_strict_families=0,uniform_strict_colors=0,multilayout_strict_colors=0,residual_colors=0) for q in range(10)}
 checks=0
 for base,big in enumerate(src):
    bs=fullblocks(big,9);inc=[sum(bool(t>>i&1) for t in bs) for i in range(9)]
    single=[7-z for z in inc]
    if min(single)<0:
      families.append(dict(base=base,feasible=False,reason='negative high singleton'));continue
    eligible=[i for i,z in enumerate(single) if z>=1]
    ebase=35-len(bs)-sum(single)
    qs=[q for q in range(10) if q<=len(eligible) and ebase+q>=0]
    if not qs:
      families.append(dict(base=base,feasible=False,reason='no feasible q'));continue
    layouts=[]
    for eng in engines:
      high,slopes=lock_functions(eng,bs,single,eligible)
      layouts.append(dict(positions=eng.pos,high=high,slopes=slopes))
    cases=[]
    for q in qs:
      e=ebase+q;bet=Counter(5-t.bit_count() for t in bs);bet[4]+=sum(single)-q
      models=[]
      for eng,lay in zip(engines,layouts):
        F=free_value(eng,e,bet);constant=F+sum(lay['high'],Q())
        top=sorted(eligible,key=lambda i:lay['slopes'][i],reverse=True)[:q]
        worst=constant+sum((lay['slopes'][i] for i in top),Q())
        models.append(dict(positions=lay['positions'],free=F,constant=constant,slopes=lay['slopes'],top_low=top,uniform_maximum=worst))
      best=min(models,key=lambda z:z['uniform_maximum']);ncolors=comb(len(eligible),q)
      z=dict(q=q,empty=e,colors=ncolors,uniform_best=best,layout_constants=[m['constant'] for m in models])
      sm=summary[q];sm['feasible_families']+=1;sm['feasible_colors']+=ncolors
      if best['uniform_maximum']<1:
        sm['uniform_strict_families']+=1;sm['uniform_strict_colors']+=ncolors
      else:
        residual=[];strict=0;maxbest=Q();worst_low=None;worst_positions=None
        for low in combinations(eligible,q):
          candidates=[(m['constant']+sum((m['slopes'][i] for i in low),Q()),j) for j,m in enumerate(models)]
          v,j=min(candidates)
          if v>maxbest:maxbest=v;worst_low=low;worst_positions=models[j]['positions']
          if v<1:strict+=1
          else:residual.append(sum(1<<i for i in low))
        sm['multilayout_strict_colors']+=strict;sm['residual_colors']+=len(residual)
        z.update(multilayout_strict_colors=strict,residual_colors=residual,maximum_minimum=maxbest,worst_low=worst_low,worst_positions=worst_positions)
      # Deterministic independent-of-maximization identity checks: one arbitrary
      # color per q (plus worst low assignment) in two separated translations.
      low0=tuple(eligible[:q])
      for j in (0,16):
        m=models[j];actual=direct(engines[j],counts(bs,single,e,low0))
        predicted=m['constant']+sum((m['slopes'][i] for i in low0),Q())
        assert actual==predicted,(base,q,j,actual,predicted);checks+=1
      j=next(j for j,m in enumerate(models) if m is best)
      assert direct(engines[j],counts(bs,single,e,best['top_low']))==best['uniform_maximum'];checks+=1
      cases.append(z)
    families.append(dict(base=base,feasible=True,large=big,full=bs,incidences=inc,single_high=single,eligible=eligible,empty_base=ebase,layouts=layouts,cases=cases))
    if base and base%50==0:print('family',base,'elapsed',time.perf_counter()-st,flush=True)
 out=dict(scope=__doc__,complete=limit is None,catalogue_families=len(src),summary=summary,affine_identity_checks=checks,elapsed_seconds=time.perf_counter()-st,families=families)
 target='UNIT9_MIXED_PILOT.json' if limit is not None else 'UNIT9_MIXED_AFFINE.json'
 (P/target).write_text(json.dumps(json_value(out),separators=(',',':'))+'\n')
 print(json.dumps(json_value({k:v for k,v in out.items() if k!='families'}),indent=2))
 return out
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else None)
