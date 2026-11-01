"""Join the same97 actual residual four-neighbour views into a shared five-neighbour star.
All five choose4 projections share one center partition and all inclusive moments.
Center blocks have size<=4; the new five-neighbour moment is0 or1 by simplicity.
"""
from pathlib import Path
from itertools import combinations,product
from collections import defaultdict
import sys,json,time
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from pilot import recover,SubsetEngine
from multilock import json_value

def canon(P):return tuple(sorted(tuple(sorted(B)) for B in P))
def restricted(P,S):
 m={old:i for i,old in enumerate(S)}
 return canon([[m[i] for i in B if i in m] for B in P if any(i in m for i in B)])
def moments(r):
 ns={int(t):n for t,n in r['counts'].items()}
 return {u:sum(n for t,n in ns.items() if t&(u<<1)==u<<1) for u in range(1,16)}
def move_moments(I,S):return {sum(1<<S[i] for i in range(4) if u>>i&1):n for u,n in I.items()}
def extensions(P):
 yield canon(P+((4,),))
 for i,B in enumerate(P):
  if len(B)<4:yield canon(P[:i]+(B+(4,),)+P[i+1:])

def main():
 start=time.time();all4=json.loads((HERE/'UNIT_FOUR_DP.json').read_text())['cases'];joint=json.loads((HERE/'JOINT_FOUR9.json').read_text())['results']
 from fractions import Fraction as Q
 strictjoint={z['source_id'] for z in joint if Q(z.get('bound','2'))<1}
 rem=[r for i,r in enumerate(all4) if not r['strict'] and i not in strictjoint and r['neighbor_degrees']==[9]*4]
 grouped=defaultdict(list)
 for r in rem:grouped[(tuple(r['neighbor_degrees']),canon(r['partition']))].append((r,moments(r)))
 out=[];seen=set();joins=0
 for ds in ((9,9,9,9,9),):
  base=[r for r in rem if tuple(r['neighbor_degrees'])==ds[:4]]
  for r in base:
   I0=moments(r);I0[16]=9
   for P in extensions(canon(r['partition'])):
    relations=[]
    for omit in range(4):
     S=tuple(i for i in range(5) if i!=omit)
     cands=[]
     for rr,J in grouped[(tuple(ds[i] for i in S),restricted(P,S))]:
      G=move_moments(J,S)
      if all(u not in I0 or I0[u]==n for u,n in G.items()):cands.append(G)
     relations.append(cands)
    if any(not z for z in relations):continue
    relations.sort(key=len)
    def dfs(j,I):
     nonlocal joins
     if j==len(relations):
      joins+=1
      for five in (0,1):
       II=dict(I);II[31]=five
       pairs=list(combinations(range(5),2));ps=[II[sum(1<<i for i in S)] for S in pairs]
       high={u:n for u,n in II.items() if u.bit_count()>=3}
       ns=recover(7,ds,ps,P,high)
       if ns is None:continue
       key=(ds,tuple(sorted((t,n) for t,n in ns.items() if n)))
       if key in seen:continue
       seen.add(key);out.append(dict(neighbor_degrees=ds,partition=P,moments=II,counts=ns,base_source_id=r['source_id']))
      return
     for G in relations[j]:
      if all(u not in I or I[u]==n for u,n in G.items()):dfs(j+1,I|G)
    dfs(0,I0)
 result=dict(scope=__doc__,four_residual_count=len(rem),full_moment_joins=joins,cases=out,elapsed_seconds=time.time()-start)
 (HERE/'FIVE_NINES_DOMAIN.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
 scored=[]
 for r in out:
  en=SubsetEngine(20,6,r['counts']);z=en.verify(en.solve());z.update(r);z['strict']=z['bound']<1;scored.append(z)
 (HERE/'FIVE_NINES_DP.json').write_text(json.dumps(json_value(dict(cases=scored,complete=True,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 print('strict',sum(z['strict'] for z in scored),'/',len(scored))
 print('domain',len(out),'joins',joins,'bydegrees',{str(ds):sum(tuple(z['neighbor_degrees'])==ds for z in out) for ds in ((8,8,9,9,9),(8,9,9,9,9),(9,9,9,9,9))},'seconds',time.time()-start)
if __name__=='__main__':main()
