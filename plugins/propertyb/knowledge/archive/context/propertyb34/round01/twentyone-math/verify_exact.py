"""Exact recheck; independent labelled-injection ABC, quotas and complete slot capacity."""
from pathlib import Path
import sys,json,time
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile,rows,total_bound,pair_weight,json_value
from independent_structure_bounds import independent_rows
from pure_quota import certificate as pure

def audit(r):
 v=r['v'];ds=tuple(r['ds']);pos=tuple(r['pos']);ns={int(t):n for t,n in r['counts'].items() if n};s=len(pos)
 assert sum(ns.values())==34 and len(set(pos))==s and all(1<=k<=v for k in pos)
 assert tuple(sum(n for t,n in ns.items() if t&(1<<i)) for i in range(s))==ds
 p=Profile(v,5,pos,ns);loss=[]
 for i,c in enumerate(r['cs']):
  if 'dual' not in c:
   z=pure(p,i);assert z['loss']==Q(c['loss']);loss.append(z['loss']);continue
  dsaved=c['dual'];main=Q();penalty=Q()
  for z in dsaved:
   R=z['avoid'];a=Q(z['alpha']);assert 0<=R<1<<s and not R&(1<<i) and a>=0
   n=sum(n for t,n in ns.items() if t&(1<<i) and not t&R)
   q=max(0,(4*n-(v-1-R.bit_count())+2)//3)
   assert n==z['edge_count'] and q==z['q'];main+=a*q
  for t,u in combinations_with_replacement(sorted(t for t in ns if t&(1<<i)),2):
   cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
   w=pair_weight(v,5,pos,t,u,pos[i])+pair_weight(v,5,pos,u,t,pos[i])
   threshold=sum((Q(z['alpha']) for z in dsaved if not (t|u)&z['avoid']),Q())
   penalty+=cap*max(Q(),threshold-w)
  value=max(Q(),main-penalty);assert value==Q(c['loss']);loss.append(value)
 rs=rows(p,deductions={pos[i]:loss[i] for i in range(s)});bound=total_bound(rs)
 assert bound==Q(r['bound'])<1
 stubs=[frozenset(i+1 for i in range(s) if t&(1<<i)) for t,n in ns.items() for _ in range(n)]
 rr=independent_rows(v,pos,stubs)
 assert len(rr)==len(rs)==v
 for a,b in zip(rs,rr):
  assert all(a[k]==b[k] for k in ('A','B','C'))
 return {'bound':str(bound),'independent_ABC':True,'complete_quota_inventory':True,'actual_degree_binding':True}

if __name__=='__main__':
 source=Path(sys.argv[1]);data=json.loads(source.read_text());start=time.time()
 cases=data['cases'] if isinstance(data,dict) else data
 results=[audit(r) for r in cases]
 out={'source':str(source),'count':len(results),'elapsed_seconds':time.time()-start,'checks':results}
 target=source.with_name(source.stem+'_VERIFIED.json');target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'count':len(results),'max_bound':str(max(Q(r['bound']) for r in results)),'seconds':time.time()-start}))
