"""Check temporary negative all-seven profiles are retained until lowering."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from seven_matching import extend,canonical,profiles

if __name__=='__main__':
 start=time.perf_counter();rows=[];rescued=set();examples=[]
 catalogue=json.loads((HERE/'SEVEN_HOMOGENEOUS_MATCHING.json').read_text())
 known={tuple(sorted((int(t),n) for t,n in z['counts'].items())) for z in catalogue['profiles'] if z['low_count']<=3}
 bound=json.loads((HERE/'SEVEN_HOMOGENEOUS_MATCHING_BOUNDS.json').read_text());assert bound['complete']
 bounded={tuple(sorted((int(t),n) for t,n in z['counts'].items())) for z in bound['results']}
 for m in range(4):
  gs,_,_=profiles([7]*6,[3<<(2*i) for i in range(m)]);stat=Counter();qq=Counter();minempty=34
  for g in gs.values():
   for ns in extend(g['counts']):
    stat['promotions']+=1;minempty=min(minempty,ns.get(0,0));ne=ns.get(0,0)<0;nsing=any(ns.get(1<<i,0)<0 for i in range(7));stat['negative_empty']+=ne;stat['negative_singleton']+=nsing
    if not ne and not nsing:continue
    for q in range(4):
     for low in combinations(range(7),q):
      nc=ns.copy()
      for i in low:nc[1<<i]=nc.get(1<<i,0)-1
      nc[0]=nc.get(0,0)+q
      if min(nc.values())<0:continue
      ds=[6 if i in low else 7 for i in range(7)]
      if any(ds[i]!=ds[j] and sum(c for t,c in nc.items() if t&(1<<i) and t&(1<<j))>1 for i in range(7) for j in range(i)):continue
      k=canonical(nc,7);assert k in known and k in bounded;rescued.add(k);qq[q]+=1
      if len(examples)<4:examples.append(dict(matching=m,all7_counts=ns,low_labels=low,actual_counts={t:c for t,c in nc.items() if c},canonical_and_bound_present=True))
  rows.append(dict(matching=m,**stat,minimum_empty_before_lowering=minempty,rescued_label_assignments_by_q=dict(qq)))
 out=dict(scope=__doc__,rows=rows,total_promotions=sum(x['promotions'] for x in rows),total_negative_empty=sum(x['negative_empty'] for x in rows),total_negative_singleton=sum(x['negative_singleton'] for x in rows),rescued_actual_orbits_q_at_most_three=len(rescued),every_rescued_orbit_and_bound_present=True,examples=examples,elapsed=time.perf_counter()-start)
 (HERE/'SEVEN_TEMPORARY_NEGATIVE_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',out['total_negative_empty'],out['rescued_actual_orbits_q_at_most_three'])
