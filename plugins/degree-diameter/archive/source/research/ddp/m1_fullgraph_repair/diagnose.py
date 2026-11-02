#!/usr/bin/env python3
"""Bounded, one-CPU diagnosis of the original702 graph; no repair trajectory."""
from collections import Counter, deque
from pathlib import Path
import json
import random
import statistics
import time

OUT=Path(__file__).resolve().parent
PROJECT=OUT.parents[2]
SOURCE=PROJECT/'computations/ddp/m1/d7_profile/D7_Meta_13_27_3.edges'

def main():
 start=time.monotonic()
 lines=SOURCE.read_text().splitlines();n,m=map(int,lines[0].split())
 adj=[set()for _ in range(n)]
 for line in lines[1:]:
  u,v=map(int,line.split());adj[u].add(v);adj[v].add(u)
 def ball2(u):
  seen={u}|adj[u]
  for v in adj[u]:seen.update(adj[v])
  return sum(1<<v for v in seen)
 balls=[ball2(u)for u in range(n)]
 badpairs=[(u,v)for u in range(n)for v in range(u+1,n)if not balls[u]&balls[v]]
 badadj=[set()for _ in range(n)]
 for u,v in badpairs:badadj[u].add(v);badadj[v].add(u)
 def label(v):return [v//351,(v%351)//27,v%27]
 def switch(a,b,c,d):
  assert len({a,b,c,d})==4 and b in adj[a] and d in adj[c] and c not in adj[a] and d not in adj[b]
  U={a,b,c,d};affected=U|set().union(*(adj[u]for u in U))
  adj[a].remove(b);adj[b].remove(a);adj[c].remove(d);adj[d].remove(c)
  adj[a].add(c);adj[c].add(a);adj[b].add(d);adj[d].add(b)
  revised={u:ball2(u)for u in affected};fixed=broken=0
  for u in affected:
   ub=revised[u]
   for v in range(n):
    if u==v or(v in affected and u>v):continue
    oldbad=not balls[u]&balls[v];newbad=not ub&revised.get(v,balls[v])
    fixed+=oldbad and not newbad;broken+=newbad and not oldbad
  adj[a].remove(c);adj[c].remove(a);adj[b].remove(d);adj[d].remove(b)
  adj[a].add(b);adj[b].add(a);adj[c].add(d);adj[d].add(c)
  return {'edges_removed':[[a,b],[c,d]],'edges_added':[[a,c],[b,d]],
          'affected_vertices':len(affected),'fixed_bad_pairs':fixed,
          'new_bad_pairs':broken,'delta':broken-fixed}
 representatives=[(0,446),(0,475),(0,677),(351,488)]
 direct=[]
 for u,v in representatives:
  moves=[switch(u,b,v,d)for b in sorted(adj[u])for d in sorted(adj[v])]
  direct.append({'bad_pair':[u,v],'count':len(moves),'delta_min':min(x['delta']for x in moves),
                 'delta_median':statistics.median(x['delta']for x in moves),
                 'delta_max':max(x['delta']for x in moves),'best_move':min(moves,key=lambda x:x['delta'])})
 rng=random.Random(7021404);guided=[]
 while len(guided)<256:
  u,v=rng.choice(representatives)
  if rng.randrange(2):u,v=v,u
  a=rng.choice(sorted(adj[u]));x=rng.choice(sorted(adj[v]));c=rng.choice(sorted(adj[x]))
  b=rng.choice(sorted(adj[a]-{u}));d=rng.choice(sorted(adj[c]-{x}))
  if len({a,b,c,d})<4 or c in adj[a] or d in adj[b]:continue
  guided.append(switch(a,b,c,d))
 # Quotient by the normalC13 subgroup acting as translation on the x coordinate.
 base_edges={}
 for u in range(n):
  for v in adj[u]:
   if u>v:continue
   su,x,i=label(u);sv,y,j=label(v);bu=su*27+i;bv=sv*27+j
   assert bu!=bv
   voltage=(y-x)%13
   if bu>bv:bu,bv=bv,bu;voltage=-voltage%13
   if (bu,bv)in base_edges:assert base_edges[bu,bv]==voltage
   base_edges[bu,bv]=voltage
 assert len(base_edges)==189
 base_adj=[[]for _ in range(54)];edge_rows=[]
 for eid,((u,v),voltage)in enumerate(sorted(base_edges.items())):
  base_adj[u].append((v,eid,1));base_adj[v].append((u,eid,-1))
  edge_rows.append([u,v,voltage])
 assert all(len(row)==7 for row in base_adj)
 def extend(form,eid,sign):
  d=dict(form);d[eid]=(d.get(eid,0)+sign)%13
  if not d[eid]:del d[eid]
  return tuple(sorted(d.items()))
 formal_counts=[];actual_counts=[];formal_hist=Counter();defective=[]
 for root in range(54):
  reached={(root,())};frontier=reached.copy()
  for depth in range(4):
   new={(v,extend(form,eid,sign))for u,form in frontier for v,eid,sign in base_adj[u]}
   new.difference_update(reached);reached.update(new);frontier=new
  buckets=[set()for _ in range(54)]
  for v,form in reached:buckets[v].add(form)
  fc=[len(f)for f in buckets];ac=[]
  for target,forms in enumerate(buckets):
   values={sum(coef*edge_rows[eid][2]for eid,coef in form)%13 for form in forms}
   ac.append(len(values));formal_hist[len(forms)]+=1
   if len(values)<13:defective.append({'root':root,'target':target,'formal_count':len(forms),
                                      'actual_count':len(values),'missing':sorted(set(range(13))-values)})
  formal_counts.append(fc);actual_counts.append(ac)
 # Independent original-lift reachability check for each base root at translation0.
 for root in range(54):
  side,residue=divmod(root,27);vertex=side*351+residue
  reached={vertex};frontier={vertex}
  for depth in range(4):
   new=set().union(*(adj[u]for u in frontier))-reached;reached.update(new);frontier=new
  observed=[0]*54
  for v in reached:s,x,i=label(v);observed[s*27+i]+=1
  assert observed==actual_counts[root]
 out={
  'source':str(SOURCE.relative_to(PROJECT)),'n':n,'m':m,'bad_unordered_pairs':len(badpairs),
  'bad_pair_types':{str(k):v for k,v in Counter((u//351,v//351)for u,v in badpairs).items()},
  'root_missing':{str(r):[label(v)for v in sorted(badadj[r])]for r in [0,351]},
  'direct_bad_edge_switches':direct,
  'guided_switch_sample':{'seed':7021404,'count':len(guided),'delta_min':min(x['delta']for x in guided),
      'delta_median':statistics.median(x['delta']for x in guided),'delta_max':max(x['delta']for x in guided),
      'best_move':min(guided,key=lambda x:x['delta']),
      'nonworsening_count':sum(x['delta']<=0 for x in guided)},
  'C13_quotient':{'vertices':54,'edges':189,'degree':7,'edge_voltages':edge_rows,
      'minimum_formal_fiber_capacity':min(map(min,formal_counts)),
      'formal_capacity_histogram':dict(sorted(formal_hist.items())),
      'formal_counts':formal_counts,'actual_counts':actual_counts,'defective_fibers':defective,
      'all54_original_lift_root_checks_match':True,
      'note':'Distinct formal forms are necessary capacity only, not simultaneous solvability.'},
  'elapsed_seconds':time.monotonic()-start}
 (OUT/'diagnosis.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'bad_pairs':len(badpairs),'direct':[x['delta_min']for x in direct],
                  'guided':out['guided_switch_sample'],
                  'C13_min_formal':out['C13_quotient']['minimum_formal_fiber_capacity'],
                  'C13_defective_ordered_base_pairs':len(defective),'elapsed_seconds':out['elapsed_seconds']}))

if __name__=='__main__':main()
