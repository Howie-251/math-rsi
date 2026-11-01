"""Extend surviving actual low-lock traces; reject only by strict projections."""
from pathlib import Path
from itertools import permutations,combinations
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(HERE.parent/'high-math'))
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile,Engine,json_value

def canon(ns,s):
 return min(tuple(sorted((sum(1<<p[i] for i in range(s) if t&(1<<i)),n) for t,n in ns.items() if n)) for p in permutations(range(s)))

def project(ns,keep):
 out={}
 for t,n in ns.items():
  u=sum(1<<i for i,j in enumerate(keep) if t&(1<<j));out[u]=out.get(u,0)+n
 return out

def extensions(ns,s,v,new_degree=6,max_extra=None,old_degrees=None,codegree_caps=None):
 E=25-v
 if max_extra is None:max_extra=E
 ds=old_degrees or [6]*s
 maxlam=[1+(4*ds[i]-(v-1))-sum((sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))-1) for j in range(s) if j!=i) for i in range(s)]
 if codegree_caps is not None:maxlam=[min(a,b) for a,b in zip(maxlam,codegree_caps)]
 ts=[t for t in ns if t and t.bit_count()<=4];prom={};lam=[0]*s
 def rec(k,used):
  if used>new_degree or sum(lam)>s+max_extra:return
  if k==len(ts):
   n0=new_degree-used
   if min(lam)<1 or n0>ns.get(0,0):return
   out=dict(ns)
   for t,n in prom.items():
    out[t]-=n;out[t|(1<<s)]=n
   out[0]=out.get(0,0)-n0;out[1<<s]=n0
   yield {t:n for t,n in out.items() if n};return
  t=ts[k];ids=[i for i in range(s) if t&(1<<i)]
  cap=min(ns[t],new_degree-used,*[maxlam[i]-lam[i] for i in ids])
  for n in range(cap+1):
   prom[t]=n
   for i in ids:lam[i]+=n
   yield from rec(k+1,used+n)
   for i in ids:lam[i]-=n
  prom.pop(t)
 yield from rec(0,0)

def main(v,s):
 start=perf_counter();source=json.loads((HERE/(f'FOUR_LOW_{v}.json' if s==4 else f'EXTEND_LOW_{v}_{s}.json')).read_text())
 bad=[{int(t):n for t,n in w['counts'].items()} for w in source['results'] if Q(w['final_bound'])>=1]
 badkeys={canon(n,s) for n in bad};raw=0;filtered=0;groups={}
 for ns in bad:
  for out in extensions(ns,s,v):
   raw+=1
   if any(canon(project(out,keep),s) not in badkeys for keep in combinations(range(s+1),s)):continue
   filtered+=1;key=canon(out,s+1);groups[key]=len(groups) if key not in groups else groups[key]
 print(v,s,'sources',len(bad),'extensions',raw,'filtered',filtered,'orbits',len(groups),flush=True)
 eng=Engine(v,s+1);rows=[]
 for key,gid in groups.items():
  ns=dict(key);sub=SubsetEngine(v,s+1,ns);r=sub.solve();w=dict(r,graph=f'v{v}-low{s+1}',group=gid,counts=ns)
  if r['bound']>=1:w['joint']=solve_profile(eng,w)
  w['final_bound']=w.get('joint',w).get('bound',9)
  if r['bound']<1:sub.verify(r);w['independent_ABC']=True
  rows.append(w);print(gid,w['final_bound'],flush=True)
  if perf_counter()-start>180:break
 (HERE/f'EXTEND_LOW_{v}_{s+1}.json').write_text(json.dumps(json_value(dict(scope=__doc__,v=v,source_count=len(bad),raw=raw,filtered=filtered,groups=len(groups),complete=len(rows)==len(groups),results=rows,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
if __name__=='__main__':main(int(sys.argv[1]),int(sys.argv[2]))
