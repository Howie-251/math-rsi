from pathlib import Path
from math import comb
from fractions import Fraction
from itertools import combinations_with_replacement
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
source=json.loads((P.parent/'three_nonunit_direct_repair_20261020/RESULT.json').read_text())
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def extra(t,r):
 if t=='P':return 0
 if t==0:return C(12,r-5)+C(12,r)
 return C(12+t,r)
def bad(types,a,r):return a*C(13,r-4)+(31-a)*C(13,r)-max(a-1,0)*C(9,r-8)+sum(extra(t,r) for t in types)
tables={}
for types in combinations_with_replacement(['P',0,2,3,4],3):
 fail=[a for a in range(32) if all(bad(types,a,r)>=C(17,r) for r in range(18))]
 tables[types]=fail
rows=[];generic=0;actual=0
for src in source['orbits']:
 tr=src['traces'];sizes=[m.bit_count() for m in tr];s=sum(sizes)
 types=[tuple(sorted(('P' if m>>v&1 else m.bit_count() for m in tr),key=lambda x:['P',0,2,3,4].index(x))) for v in range(5)]
 fail=[tables[t] for t in types];h=[sum(m>>v&1 for m in tr) for v in range(5)]
 tails=[];ng=[0]
 def visit(i,left,aa):
  if i==5:
   if left:return
   ng[0]+=1
   ds=[1+a+b for a,b in zip(aa,h)]
   if min(ds)<6:return
   assoc=[4*aa[v]+sum(5-m.bit_count() for m in tr if m>>v&1) for v in range(5)]
   if min(assoc)<17:return
   dirty=15-s;clean=17-dirty;outside=139-s
   rmax=(outside-6*dirty)//clean
   tails.append({'attachments':aa,'F_degrees':ds,'outside_assoc_by_F':assoc,'dirty_union_upper':dirty,'clean_lower':clean,'clean_degree_upper':rmax,'outside_degree_sum':outside,'outside_excess_above6':37-s})
   return
  if not fail[i]:return
  low=sum(min(x) for x in fail[i+1:]) if all(fail[i+1:]) else 100
  high=sum(max(x) for x in fail[i+1:]) if all(fail[i+1:]) else -100
  for a in fail[i]:
   if low<=left-a<=high:visit(i+1,left-a,aa+[a])
 visit(0,31,[])
 generic+=ng[0];actual+=len(tails)
 rows.append({'traces':tr,'sizes':sizes,'S5_label_count':src['labels'],'generic_failed_attachments':ng[0],'actual_necessary_profiles':tails})
res={'scope':'22/35/simple5/paircover/min6,qGamma(F)=3; anchor-bound residuals with exact n22 constants, then actual F-degree and outside paircoverage filters. These are necessary profiles, not H realizability classes. No new locks/certificate search.','geometry_source':'../three_nonunit_direct_repair_20261020/RESULT.json: all3276 trace triples/91 S5 orbits; orbit geometry independent of n','trace_orbits':len(rows),'labeled_trace_triples':sum(r['S5_label_count'] for r in rows),'anchor_closed_orbits':sum(not r['generic_failed_attachments'] for r in rows),'generic_failed_attachments':generic,'actual_tail_orbits':sum(bool(r['actual_necessary_profiles']) for r in rows),'actual_necessary_profiles':actual,'clean_rmax_histogram':dict(Counter(z['clean_degree_upper'] for r in rows for z in r['actual_necessary_profiles'])),'trace_sum_histogram':dict(Counter(sum(r['sizes']) for r in rows for z in r['actual_necessary_profiles'])),'rows':rows,'cpu_seconds':time.process_time()-start}
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
print({k:v for k,v in res.items() if k!='rows'})
for r in rows:
 if r['actual_necessary_profiles']:print(r['traces'],r['sizes'],len(r['actual_necessary_profiles']),'example',r['actual_necessary_profiles'][0])
