"""Six degree7 locks at23 vertices, codegree2 perfect matching, other pairs1.
A complete local pair-budget recursion produces actual multi-trace candidates.
This supports the three-clique seven-degree graph branch; it is not itself a
whole-hypergraph exclusion. All arithmetic uses exact weights.
"""
from pathlib import Path
from itertools import permutations,combinations,product
from functools import lru_cache
from math import factorial,comb
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'computations'));sys.path.insert(0,str(ROOT/'computations/propertyb33/round01'))
from multilock import Profile,rows,total_bound,pair_weight,edge_weight,position_context,json_value
from pure_quota import certificate
from independent_structure_bounds import independent_rows

def trans(t,p):return sum(1<<p[i] for i in range(6) if t&(1<<i))
def profiles(extra):
 pairs=[sum(1<<i for i in p) for p in combinations(range(6),2)];blocks=[b for b in range(64) if 2<=b.bit_count()<=5];contents={b:tuple(i for i,p in enumerate(pairs) if b&p==p) for b in blocks};bad=(3,) if extra else ();initial=tuple(2 if p in bad else 1 for p in pairs)
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
 raw=rec(initial);groups={};orbit={};auto=[p for p in permutations(range(6)) if {trans(b,p) for b in bad}==set(bad)]
 for bs in sorted(raw):
  ns={b:bs.count(b) for b in set(bs)}
  for i in range(6):ns[1<<i]=7-sum(bool(b&(1<<i)) for b in bs)
  ns[0]=34-sum(ns.values())
  if min(ns.values())<0:continue
  ns={b:n for b,n in ns.items() if n};key=tuple(sorted(ns.items()))
  if key not in orbit:
   gid=len(groups);groups[gid]=dict(counts=ns,blocks=bs,best=None)
   for p in auto:orbit[tuple(sorted((trans(b,p),n) for b,n in ns.items()))]=gid
 return groups,len(raw)

def main():
 start=time.perf_counter();v=24;s=6;D=factorial(18);groups={};nraw=0
 for extra in (0,1):
  gs,nr=profiles(extra);nraw+=nr
  for g in gs.values():groups[len(groups)]=dict(extra=extra,**g)
 print('raw',nraw,'groups',len(groups),'generation',time.perf_counter()-start,flush=True)
 permutations_all=list(permutations(range(6)));valid=[t for t in range(64) if t.bit_count()<=5]
 for a in [8,9,10,7,11,6,12,5,13,4,14,3,15,2,16,1,17,18]:
  pos=tuple(range(a,a+6));raw=[]
  for k in range(1,v+1):
   aa={t:int(D*edge_weight(v,5,pos,t,k,True)) for t in valid};bb={t:int(D*edge_weight(v,5,pos,t,k,False)) for t in valid};cc={(t,u):int(D*pair_weight(v,5,pos,t,u,k)) for t in valid for u in valid};raw.append((aa,bb,{p:w for p,w in cc.items() if w}))
  for gid,g in groups.items():
   if g['best'] is not None and g['best']<D:continue
   seen=set()
   for perm in permutations_all:
    ns={trans(t,perm):n for t,n in g['counts'].items()};key=tuple(sorted(ns.items()))
    if key in seen:continue
    seen.add(key);total=0
    for k,(aa,bb,cc) in enumerate(raw,1):
     A=sum(n*aa[t] for t,n in ns.items());B=sum(n*bb[t] for t,n in ns.items());C=sum(ns.get(t,0)*(ns.get(u,0)-int(t==u))*w for (t,u),w in cc.items())
     if k in pos:
      bit=1<<pos.index(k);r=max(0,(4*ns.get(bit,0)-18+2)//3);loss=2*r*cc.get((bit,bit),0);rem=max(0,2-r);ts=sorted(t for t in ns if t&bit);slots=[]
      for j,t in enumerate(ts):
       for u in ts[j:]:
        cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
        if t==u==bit:cap-=r
        if cap:slots.append((cc.get((t,u),0)+cc.get((u,t),0),cap))
      for w,cap in sorted(slots):
       take=min(rem,cap);rem-=take;loss+=take*w
      assert rem==0;C-=loss
     total+=min(A,B,C)
    if g['best'] is None or total<g['best']:g.update(best=total,bound=Fraction(total,D),positions=tuple(pos[perm[i]] for i in range(6)))
    if total<D:break
  passed=sum(g['best'] is not None and g['best']<D for g in groups.values());print('window',a,'passed',passed,'/',len(groups),'seconds',time.perf_counter()-start,flush=True)
  edge_weight.cache_clear();pair_weight.cache_clear();position_context.cache_clear()
  if passed==len(groups):break
  if time.perf_counter()-start>90:break
 out=[]
 for gid,g in groups.items():
  p=Profile(v,5,g['positions'],g['counts']);cs=[certificate(p,i) for i in range(6)];rs=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(6)});assert total_bound(rs)==g['bound'];g.update(group=gid,certificates=cs,rows=rs);out.append(g)
 result=dict(scope=__doc__,raw=nraw,groups=len(groups),passed=sum(g['bound']<1 for g in out),all_have_witness=all(g['bound']<1 for g in out),results=out,elapsed_seconds=time.perf_counter()-start)
 Path(__file__).with_name('SIX_SEVEN_V24.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
 print('summary',result['passed'],'/',result['groups'],result['elapsed_seconds'])
if __name__=='__main__':main()
