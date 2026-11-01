"""Decompose nu_T=(5-|T|)mu_T into twenty set partitions of G.
Reduce to pairing disjoint nonsingle block copies; singleton completions are
forced by the exact degree20 identities. Positive answers carry full witnesses.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();budget=30
source=json.loads((P/'GROUP5_CATALOGUE.json').read_text());records=[]
class Timeout(Exception):pass

def solve(mu):
 nu={t:(5-t.bit_count())*c for t,c in mu.items() if t and t!=31}
 nu={t:c for t,c in nu.items() if c}
 assert all(sum(c for t,c in nu.items() if t>>i&1)==20 for i in range(5))
 types=sorted(t for t in nu if t.bit_count()>=2);initial=tuple(nu[t] for t in types);N=sum(initial);target=max(0,N-20)
 if N>40:
  return dict(status='INFEASIBLE',nu=nu,nonsingle_occurrences=N,certificate=dict(kind='rational_partition_capacity',inequality='sum_{|T|>=2} nu_T <= 40',left=N,right=40),recursion_nodes=0)
 neighbors={i:[j for j,t in enumerate(types) if not t&types[i]] for i in range(len(types))};nodes=0
 @lru_cache(None)
 def rec(state,need):
  nonlocal nodes
  nodes+=1
  if nodes%1000==0 and time.perf_counter()-st>budget:raise Timeout
  if need==0:return ()
  if sum(state)<2*need:return None
  # Permanently isolated copies cannot participate in a matching.
  alive=[i for i,c in enumerate(state) if c and any(state[j] for j in neighbors[i])]
  if sum(state[i] for i in alive)<2*need:return None
  i=min(alive,key=lambda i:(sum(state[j]>0 for j in neighbors[i]),state[i],types[i]))
  for j in sorted((j for j in neighbors[i] if state[j]),key=lambda j:(sum(state[k]>0 for k in neighbors[j]),-state[j],types[j])):
   ss=list(state);ss[i]-=1;ss[j]-=1
   tail=rec(tuple(ss),need-1)
   if tail is not None:return ((i,j),)+tail
  # Chosen copy unmatched: together with each possible partner above, exhaustive.
  ss=list(state);ss[i]-=1
  return rec(tuple(ss),need)
 matching=rec(initial,target)
 if matching is None:
  return dict(status='INFEASIBLE_EXHAUSTIVE',nu=nu,nonsingle_occurrences=N,required_pairs=target,recursion_nodes=nodes,failed_states=rec.cache_info().currsize)
 unused=list(initial);parts=[]
 for i,j in matching:
  unused[i]-=1;unused[j]-=1;assert unused[i]>=0 and unused[j]>=0
  t,u=types[i],types[j];assert t&u==0
  parts.append(tuple(sorted([t,u]+[1<<k for k in range(5) if not ((t|u)>>k&1)])))
 for i,c in enumerate(unused):
  t=types[i]
  for _ in range(c):parts.append(tuple(sorted([t]+[1<<k for k in range(5) if not (t>>k&1)])))
 while len(parts)<20:parts.append((1,2,4,8,16))
 assert len(parts)==20
 replay=Counter()
 for part in parts:
  union=0
  for t in part:assert not union&t;union|=t;replay[t]+=1
  assert union==31
 assert dict(sorted(replay.items()))==dict(sorted(nu.items()))
 mult=Counter(parts)
 return dict(status='FEASIBLE',nu=nu,nonsingle_occurrences=N,required_pairs=target,paired_blocks=[[types[i],types[j]] for i,j in matching],partition_multiset=[dict(blocks=list(part),multiplicity=c) for part,c in sorted(mult.items())],recursion_nodes=nodes,all_31_trace_marginals_replayed=True)
for r in source['representatives']:
 mu={int(t):c for t,c in r['counts'].items()};z=solve(mu);records.append(dict(id=r['id'],**z))
 print(r['id'],z['status'],'N',z['nonsingle_occurrences'],'nodes',z['recursion_nodes'],flush=True)
summary=dict(scope=__doc__,complete=len(records)==27,orbits=27,feasible=sum(r['status']=='FEASIBLE' for r in records),infeasible=sum(r['status']=='INFEASIBLE' for r in records),exhaustive_infeasible=sum(r['status']=='INFEASIBLE_EXHAUSTIVE' for r in records),total_recursion_nodes=sum(r['recursion_nodes'] for r in records),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_PARTITIONS.json').write_text(json.dumps(dict(summary=summary,results=records),indent=2)+'\n');print(json.dumps(summary,indent=2))
