"""Independent ordered-type-pair replay of each q1 uniform-worst witness.
Affine extrema cover every admissible one-low label; this checks all 240 maxima.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import sys,json,time
P=Path(__file__).resolve().parent;R=P.parents[3]
sys.dont_write_bytecode=True
sys.path[:0]=[str(R/'computations')]
from multilock import Profile,rows,total_bound,pair_weight
st=time.perf_counter()
def loss(p,i):
 bit=1<<i;ts=sorted(t for t in p.counts if t&bit);d=sum(p.counts[t] for t in ts);assert d in (6,7)
 q=max(0,(4*d-24+2)//3);pure=max(0,(4*p.counts.get(bit,0)-16+2)//3)
 inv=[]
 for j,t in enumerate(ts):
  for u in ts[j:]:
   cap=comb(p.counts[t],2) if t==u else p.counts[t]*p.counts[u]
   if cap:inv.append([pair_weight(25,5,p.positions,t,u,p.positions[i])+pair_weight(25,5,p.positions,u,t,p.positions[i]),cap,t==u==bit])
 ded=Q();left=pure
 for z in sorted(inv):
  if z[2]:k=min(left,z[1]);left-=k;z[1]-=k;ded+=k*z[0]
 assert left==0
 left=max(q-pure,0)
 for z in sorted(inv):k=min(left,z[1]);left-=k;ded+=k*z[0]
 assert left==0
 return ded
src=json.loads((P/'UNIT9_MIXED_AFFINE.json').read_text());checked=colors=0;maximum=Q();worst=None
for f in src['families']:
 if not f['feasible']:continue
 for c in f['cases']:
  if c['q']!=1:continue
  z=c['uniform_best'];low=z['top_low']
  ns={**{int(t):1 for t in f['full']},**{1<<i:a-int(i in low) for i,a in enumerate(f['single_high']) if a-int(i in low)},0:c['empty']}
  ns={t:a for t,a in ns.items() if a};assert sum(ns.values())==35
  assert sorted(sum(a for t,a in ns.items() if t>>i&1) for i in range(9))==[6]+[7]*8
  p=Profile(25,5,z['positions'],ns);dd={p.positions[i]:loss(p,i) for i in range(9)}
  rr=rows(p,deductions=dd);v=total_bound(rr)
  assert v==Q(z['uniform_maximum']) and v<1
  if v>maximum:maximum=v;worst=dict(base=f['base'],low=low,positions=z['positions'],value=str(v))
  checked+=1;colors+=c['colors']
out=dict(scope=__doc__,feasible_families=checked,covered_colors=colors,maximum=str(maximum),worst=worst,all_equal=True,elapsed_seconds=time.perf_counter()-st)
(P/'UNIT9_MIXED_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
