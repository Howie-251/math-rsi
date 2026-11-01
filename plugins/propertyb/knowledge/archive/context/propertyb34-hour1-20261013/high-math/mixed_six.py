"""Exact local six-lock diagnostic for chosen degree vector and pair budgets."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
from math import factorial,comb
from fractions import Fraction
from functools import lru_cache
import sys,json,time,argparse
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile,rows,total_bound,pair_weight,edge_weight,position_context,json_value,link_q_lower
from pure_quota import certificate
from independent_structure_bounds import independent_rows

def trans(t,p):return sum(1<<p[i] for i in range(6) if t&(1<<i))
def profiles(degs,bad):
 pairs=[sum(1<<i for i in p) for p in combinations(range(6),2)];blocks=[b for b in range(64) if 2<=b.bit_count()<=5];contents={b:tuple(i for i,p in enumerate(pairs) if b&p==p) for b in blocks};initial=tuple(2 if p in bad else 1 for p in pairs)
 @lru_cache(None)
 def rec(rem):
  if not any(rem):return frozenset([()])
  i=next(i for i,n in enumerate(rem) if n);out=set()
  for b in blocks:
   inds=contents[b]
   if i not in inds or any(rem[j]==0 for j in inds):continue
   nxt=list(rem)
   for j in inds:nxt[j]-=1
   for tail in rec(tuple(nxt)):out.add(tuple(sorted((b,)+tail)))
  return frozenset(out)
 raw=rec(initial);groups={};orbit={};valid=0;auto=[p for p in permutations(range(6)) if {trans(b,p) for b in bad}==set(bad) and all(degs[i]==degs[p[i]] for i in range(6))]
 for bs in sorted(raw):
  ns=dict(Counter(bs))
  for i in range(6):ns[1<<i]=degs[i]-sum(bool(b&(1<<i)) for b in bs)
  ns[0]=34-sum(ns.values())
  if min(ns.values())<0:continue
  ns={b:n for b,n in ns.items() if n};key=tuple(sorted(ns.items()));valid+=1
  if key not in orbit:
   gid=len(groups);groups[gid]=dict(counts=ns,blocks=bs,best=None)
   for p in auto:orbit[tuple(sorted((trans(b,p),n) for b,n in ns.items()))]=gid
 return groups,len(raw),valid

def run(v,degs,bad,budget=60):
 start=time.perf_counter();N=v-6;D=factorial(N);groups,nraw,validcount=profiles(degs,bad);print('raw',nraw,'valid',validcount,'groups',len(groups),flush=True)
 allperms=list(permutations(range(6)));valid=[t for t in range(64) if t.bit_count()<=5]
 for a in [9,8,10,7,11,6,12,5,13,4,14]:
  pos=tuple(range(a,a+6));raw=[]
  for k in range(1,v+1):
   aa={t:int(D*edge_weight(v,5,pos,t,k,True)) for t in valid};bb={t:int(D*edge_weight(v,5,pos,t,k,False)) for t in valid};cc={(t,u):int(D*pair_weight(v,5,pos,t,u,k)) for t in valid for u in valid};raw.append((aa,bb,{p:w for p,w in cc.items() if w}))
  for gid,g in groups.items():
   if g['best'] is not None and g['best']<D:continue
   seen=set()
   for perm in allperms:
    ns={trans(t,perm):n for t,n in g['counts'].items()};key=tuple(sorted(ns.items()))
    if key in seen:continue
    seen.add(key);total=0
    for k,(aa,bb,cc) in enumerate(raw,1):
     A=sum(n*aa[t] for t,n in ns.items());B=sum(n*bb[t] for t,n in ns.items());C=sum(ns.get(t,0)*(ns.get(u,0)-int(t==u))*w for (t,u),w in cc.items())
     if k in pos:
      bit=1<<pos.index(k);deg=sum(n for t,n in ns.items() if t&bit);q=link_q_lower(v,5,deg);r=max(0,(4*ns.get(bit,0)-N+2)//3);loss=2*r*cc.get((bit,bit),0);rem=max(0,q-r);ts=sorted(t for t in ns if t&bit);slots=[]
      for j,t in enumerate(ts):
       for u in ts[j:]:
        cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
        if t==u==bit:cap-=r
        if cap:slots.append((cc.get((t,u),0)+cc.get((u,t),0),cap))
      for w,cap in sorted(slots):take=min(rem,cap);rem-=take;loss+=take*w
      assert rem==0;C-=loss
     total+=min(A,B,C)
    if g['best'] is None or total<g['best']:g.update(best=total,bound=Fraction(total,D),positions=tuple(pos[perm[i]] for i in range(6)))
    if total<D:break
  passed=sum(g['best'] is not None and g['best']<D for g in groups.values());print('window',a,'pass',passed,'/',len(groups),'sec',time.perf_counter()-start,flush=True)
  edge_weight.cache_clear();pair_weight.cache_clear();position_context.cache_clear()
  if passed==len(groups) or time.perf_counter()-start>budget:break
 out=[]
 for gid,g in groups.items():
  p=Profile(v,5,g['positions'],g['counts']);cs=[certificate(p,i) for i in range(6)];rs=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(6)});assert total_bound(rs)==g['bound'];g.update(group=gid,certificates=cs,rows=rs);out.append(g)
 return dict(v=v,degrees=degs,bad_masks=bad,raw=nraw,valid=validcount,groups=len(groups),passed=sum(g['bound']<1 for g in out),results=out,elapsed_seconds=time.perf_counter()-start)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--v',type=int,default=25);ap.add_argument('--low',type=int,default=5);ap.add_argument('--bad',type=int,nargs='*',default=[]);ap.add_argument('--budget',type=float,default=60);a=ap.parse_args()
 r=run(a.v,[6]*a.low+[7]*(6-a.low),a.bad,a.budget)
 p=Path(__file__).with_name(f'MIXED_SIX_v{a.v}_low{a.low}_bad'+('_'.join(map(str,a.bad)) or 'none')+'.json');p.write_text(json.dumps(json_value(r),indent=2)+'\n');print(p,'PASS',r['passed'],'/',r['groups'])
