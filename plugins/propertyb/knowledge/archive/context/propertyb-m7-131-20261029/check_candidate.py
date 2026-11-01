"""Exact 424-profile candidate for M=130; original kernel plus seven-uniform avoided quotas.
This is a replay of a complete structurally selected parameter domain, not a hypergraph search.
"""
import importlib.util,itertools,json,time
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('p',P/'pilot.py');p=importlib.util.module_from_spec(sp);sp.loader.exec_module(p);c=p.c

def main():
 start=time.process_time();rows=[];structural=[]
 assert 73*c.ceil(72,6)<=910<74*c.ceil(73,6)
 for v in range(13,37):assert F(130*(c.C(v//2,7)+c.C(v-v//2,7)),c.C(v,7))<1
 assert F(130*(c.C(18,7)+c.C(19,7)),c.C(37,7))>=1
 def add(v,kind,ds,ell,pos,avoid,extra=None):
  assert sum(ell.values())==130 and min(ell.values())>=0
  for j,d in enumerate(ds):assert sum(n for T,n in ell.items() if T&(1<<j))==d
  u=p.bound(v,pos,ell,avoid) if pos else c.unlocked(v)
  assert u<1,(v,kind,ds,u)
  rows.append(dict(v=v,kind=kind,degrees=ds,ell=ell,positions=pos,avoid=avoid,U=str(u),**(extra or {})))
 for v in range(37,54):add(v,'zero',[],{0:130},[],False)
 for v in range(54,67):
  for d in range(c.ceil(v-1,6),910//v+1):
   s=2*(v-1)-6*d;assert s>0
   B=next(b for b in range(d,911) if v*d+s*(b+1-d)>910)
   for dy in range(d,B+1):
    ell={0:131-d-dy,1:d-1,2:dy-1,3:1}
    u,pos=min((p.bound(v,pos,ell,True),pos) for pos in ((v//2,v//2+1),(v//2,v//2-1)))
    add(v,'two',[d,dy],ell,pos,True,dict(B=B,unit_neighbors_lower=s))
 for v,D in ((67,14),(68,13),(69,13),(70,13)):
  d0=c.ceil(v-1,6);Z=(D+1)*v-910;T=6*(D+1)-v+2
  assert Z>0 and 24*Z>2*T*T and D+1>d0
  structural.append(dict(v=v,D=D,d0=d0,Z=Z,T=T,lhs=24*Z,rhs=2*T*T))
  for ds in itertools.combinations_with_replacement(range(d0,D+1),3):
   for tri in (0,1):
    ell={0:132-sum(ds),1:ds[0]-1,2:ds[1]-1,4:ds[2]-1,7:1} if tri else {0:133-sum(ds),1:ds[0]-2,2:ds[1]-2,4:ds[2]-2,3:1,5:1,6:1}
    add(v,'three',ds,ell,(v//2-1,v//2,v//2+1),True,dict(tri=tri))
 for v in range(71,74):
  r=13*v-910;e=73-v;assert r>=3*(e+1)
  for tri in (0,1):
   ell={0:96,1:11,2:11,4:11,7:1} if tri else {0:97,1:10,2:10,4:10,3:1,5:1,6:1}
   add(v,'three_tail',[12]*3,ell,(v//2-1,v//2,v//2+1),False,dict(tri=tri,r_lower=r,aux_degree_upper=e))
 assert len(rows)==424
 groups=[]
 for v in range(37,74):
  rs=[r for r in rows if r['v']==v];mx=max(rs,key=lambda r:F(r['U']));groups.append(dict(v=v,profiles=len(rs),maximum=mx['U'],max_degrees=mx['degrees'],max_positions=mx['positions']))
 out=dict(status='complete-computer-assisted-proof-candidate; not independent audit or Lean',M=130,conclusion='m(7)>=131',profiles=len(rows),cpu_seconds=time.process_time()-start,structural=structural,groups=groups,rows=rows,maximum=max((r['U'] for r in rows),key=F))
 (P/'CANDIDATE.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ('rows','groups')},indent=2))
if __name__=='__main__':main()
