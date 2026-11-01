"""Complete five-neighbour relation joins for the eight actual degree vectors.
Every four-view has the same x-edge partition and inclusive moments.
"""
from pilot import *
from fractions import Fraction as Q
from collections import defaultdict
start=time.time();cpu=time.process_time()
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
patterns=((8,8,8,8,8),(8,8,8,8,9),(8,8,8,8,10),(8,8,8,9,9),(8,8,8,9,10),(8,8,9,9,9),(8,8,9,9,10),(8,9,9,9,9))
def main():
 rem=[]
 for base,cert in [('REFINED_FOUR_DP.json','JOINT_REFINED_FOUR.json'),('FOUR_WITH_TEN_DP.json','JOINT_FOUR_WITH_TEN.json')]:
  all4=json.loads((HERE/base).read_text())['cases'];joint=json.loads((HERE/cert).read_text())['results']
  assert json.loads((HERE/cert).read_text())['complete']
  strict={z['source_id'] for z in joint if Q(z.get('bound','2'))<1}
  rem += [dict(r,source_file=base,source_idx=i) for i,r in enumerate(all4) if not r['strict'] and i not in strict]
 grouped=defaultdict(list)
 for r in rem:grouped[(tuple(r['neighbor_degrees']),canon(r['partition']))].append((r,moments(r)))
 out=[];seen=set();joins=0
 for ds in patterns:
  before=len(out)
  for r in [r for r in rem if tuple(r['neighbor_degrees'])==ds[:4]]:
   I0=moments(r);I0[16]=ds[4]
   for P in extensions(canon(r['partition'])):
    relations=[]
    for omit in range(4):
     S=tuple(i for i in range(5) if i!=omit);cands=[]
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
       ps=[II[sum(1<<i for i in S)] for S in combinations(range(5),2)]
       ns=recover(7,ds,ps,P,{u:n for u,n in II.items() if u.bit_count()>=3})
       if ns is None:continue
       key=(ds,tuple(sorted((t,n) for t,n in ns.items() if n)))
       if key in seen:continue
       seen.add(key);out.append(dict(neighbor_degrees=ds,partition=P,moments=II,counts=ns))
      return
     for G in relations[j]:
      if all(u not in I or I[u]==n for u,n in G.items()):dfs(j+1,I|G)
    dfs(0,I0)
  print(ds,'domain',len(out)-before,flush=True)
 result=dict(complete=True,four_residual_count=len(rem),full_moment_joins=joins,cases=out,cpu_seconds=time.process_time()-cpu,wall_seconds=time.time()-start)
 (HERE/'EIGHT_FIVE_DOMAIN.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
 print('complete',len(out),'seconds',time.time()-start)
if __name__=='__main__':main()
