"""Six actual unit degree9 neighbours, conditional on having no unit degree8 point.
Join all six five-neighbour projections from the225 exact DP-residual views.
Center-partition blocks<=4; all five-point inclusive moments<=1; six-point moment=0.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import sys,json,time
HERE=Path(__file__).parent;sys.path[:0]=[str(HERE.parent),str(HERE.parent/'twentytwo')]
from star_pilot import recover
from multilock import json_value
from star_five_domain import canon,restricted

def moments(r):
 ns={int(t):n for t,n in r['counts'].items()}
 return {u:sum(n for t,n in ns.items() if t&(u<<1)==u<<1) for u in range(1,32)}
def move(I,S):return {sum(1<<S[i] for i in range(5) if u>>i&1):n for u,n in I.items()}
def extensions(P):
 if len(P)<6:yield canon(P+((5,),))
 for i,B in enumerate(P):
  if len(B)<4:yield canon(P[:i]+(B+(5,),)+P[i+1:])
def main():
 start=time.time();old=json.loads((HERE/'STAR_FIVE_DP.json').read_text())['cases'];rem=[r for r in old if not r['strict']]
 assert len(rem)==225 and all(r['neighbor_degrees']==[9]*5 for r in rem)
 grouped=defaultdict(list)
 for r in rem:grouped[canon(r['center_partition'])].append((r,moments(r)))
 out=[];seen=set();joins=0;attempts=0
 for r in rem:
  I0=moments(r);I0[32]=9
  for P in extensions(canon(r['center_partition'])):
   relations=[]
   for omit in range(5):
    S=tuple(i for i in range(6) if i!=omit);cands=[]
    for rr,J in grouped[restricted(P,S)]:
     G=move(J,S)
     if all(u not in I0 or I0[u]==n for u,n in G.items()):cands.append(G)
    relations.append(cands)
   if any(not z for z in relations):continue
   relations.sort(key=len)
   def dfs(j,I):
    nonlocal joins,attempts
    attempts+=1
    if j==len(relations):
     joins+=1;II=dict(I);II[63]=0
     assert all(n<=1 for u,n in II.items() if u.bit_count()==5)
     ps=[II[sum(1<<i for i in S)] for S in combinations(range(6),2)]
     ns=recover(6,[9]*6,ps,P,{u:n for u,n in II.items() if u.bit_count()>=3})
     if ns is None:return
     key=tuple(sorted((t,n) for t,n in ns.items() if n))
     if key in seen:return
     seen.add(key);out.append(dict(neighbor_degrees=[9]*6,center_partition=P,moments=II,counts=ns,base_source_id=r['source_id']))
     return
    for G in relations[j]:
     if all(u not in I or I[u]==n for u,n in G.items()):dfs(j+1,I|G)
   dfs(0,I0)
 result=dict(scope=__doc__,five_residual_count=225,full_moment_joins=joins,search_nodes=attempts,cases=out,elapsed_seconds=time.time()-start)
 (HERE/'STAR_SIX_DOMAIN.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
 print('domain',len(out),'joins',joins,'nodes',attempts,'seconds',time.time()-start)
if __name__=='__main__':main()
