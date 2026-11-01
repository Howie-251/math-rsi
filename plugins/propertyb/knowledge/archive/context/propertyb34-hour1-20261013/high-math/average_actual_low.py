"""Uniform lock-label averaging, actual unique low bad slot selected before permutation.
U averaged over label permutations is free-row average plus sum of center-row averages.
Each center average is bounded by max over its admissible actual slot, separately.
No independence of actual slots, and no joint-slot enumeration, is assumed.
"""
from pathlib import Path
from fractions import Fraction
from itertools import permutations,combinations
from math import factorial,comb
import json,sys,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01'),str(Path(__file__).parent)]
from multilock import edge_weight,pair_weight,position_context,json_value
from mixed_six import trans

def rawrows(v,s,pos):
 D=factorial(v-s);valid=[t for t in range(1<<s) if t.bit_count()<=5];rs=[]
 for k in range(1,v+1):
  aa={t:int(D*edge_weight(v,5,pos,t,k,True)) for t in valid};bb={t:int(D*edge_weight(v,5,pos,t,k,False)) for t in valid};cc={(t,u):int(D*pair_weight(v,5,pos,t,u,k)) for t in valid for u in valid};rs.append((aa,bb,{p:w for p,w in cc.items() if w}))
 edge_weight.cache_clear();pair_weight.cache_clear();position_context.cache_clear()
 return rs

def average(ns,v,s,pos,rs=None,perms=None):
 D=factorial(v-s);rs=rs or rawrows(v,s,pos);slots=[]
 for i in range(s):
  bit=1<<i;ts=sorted(t for t in ns if t&bit);pure=max(0,(4*ns.get(bit,0)-(v-s)+2)//3);ss=[]
  for j,t in enumerate(ts):
   for u in ts[j:]:
    cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
    if cap and t&u==bit and (not pure or t==u==bit):ss.append((t,u))
  if not ss:return dict(infeasible=True,center=i)
  slots.append(ss)
 sums=[[0]*len(ss) for ss in slots];free=0;num=0
 for perm in (perms if perms is not None else permutations(range(s))):
  num+=1;transport=lambda t:sum(1<<perm[i] for i in range(s) if t&(1<<i));mapping={t:transport(t) for t in ns};counts={mapping[t]:n for t,n in ns.items()};inverse=[perm.index(i) for i in range(s)]
  for k,(aa,bb,cc) in enumerate(rs,1):
   A=sum(n*aa[t] for t,n in counts.items());B=sum(n*bb[t] for t,n in counts.items());base=min(A,B)
   if base:C=sum(counts.get(t,0)*(counts.get(u,0)-int(t==u))*w for (t,u),w in cc.items())
   else:C=0
   if k not in pos:free+=min(base,C);continue
   center=inverse[pos.index(k)]
   for j,(t,u) in enumerate(slots[center]):
    mt,mu=mapping[t],mapping[u];loss=cc.get((mt,mu),0)+cc.get((mu,mt),0)
    sums[center][j]+=min(base,C-loss)
 total=free+sum(max(ss) for ss in sums)
 return dict(bound=Fraction(total,num*D),positions=pos,counts=ns,permutations=num,free_average=Fraction(free,num*D),centers=[dict(center=i,slots=slots[i],averages=[Fraction(x,num*D) for x in sums[i]],maximum=Fraction(max(sums[i]),num*D)) for i in range(s)])

if __name__=='__main__':
 start=time.perf_counter();source=json.loads(Path(__file__).with_name('MIXED_SIX_v24_low6_badnone.json').read_text());out={};layouts=[tuple(range(a,a+6)) for a in (10,9,8,7,11)]+[(10,11,12,13,14,24),(9,10,11,12,13,24),(10,11,12,13,23,24),(8,9,10,11,12,14)]
 for pos in layouts:
  rs=rawrows(24,6,pos)
  for x in source['results']:
   gid=x['group']
   if Fraction(x['bound'])<1 or (gid in out and (out[gid].get('infeasible') or out[gid]['bound']<1)):continue
   ns={int(t):n for t,n in x['counts'].items()};z=average(ns,24,6,pos,rs)
   if gid not in out or z.get('infeasible') or z['bound']<out[gid]['bound']:out[gid]=dict(group=gid,blocks=x['blocks'],**z)
   print(gid,pos,z.get('bound','infeasible'),'sec',time.perf_counter()-start,flush=True)
  Path(__file__).with_name('SIX_LOW_ACTUAL_AVERAGE.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,results=list(out.values()))),indent=2)+'\n')
