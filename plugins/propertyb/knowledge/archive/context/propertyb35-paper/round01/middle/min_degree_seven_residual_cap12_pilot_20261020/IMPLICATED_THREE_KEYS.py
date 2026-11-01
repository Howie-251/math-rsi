"""Exact13-failure implication and shared-column/tau inputs for only the3 surviving keys after root newP."""
from pathlib import Path
from collections import Counter
from itertools import product,permutations
from math import comb
import json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time();r=json.loads((P/'RESULT.json').read_text());newp=json.loads((P/'NEWP_REFINEMENT.json').read_text());source=json.loads((ROOT/'context/propertyb35-paper/round01/root/tau_shared_capacities_20261020/FINAL_LAMBDA4_VERIFY.json').read_text());jobs={j['spectrum_id']:j for j in source['jobs']};out=[]
for key in newp['keys']:
 if key['strict']:continue
 j=jobs[key['spectrum_id']];ki=next(i for i,z in enumerate(j['survivors']) if z['n']==key['n'] and z['tau']==key['tau']);tails=[]
 for f in r['all_nonstrict']:
  if f['legacy'] or not any(c['spectrum_id']==j['spectrum_id'] and c['survivor_index']==ki for c in f['active_contexts']):continue
  mu=f['counts'];inc={m:sum(n for T,n in enumerate(mu) if T&m==m) for m in (3,5,6,9,10,12)};q=sum(comb(l-1,2) for l in inc.values());R=key['tau']-q;S=[4*d-sum(l for T,l in inc.items() if T>>i&1) for i,d in enumerate(f['degrees'])];cols={str(T):n*(5-T.bit_count()) for T,n in enumerate(mu) if n};outside=Counter(j['degrees'])-Counter(f['degrees']);hist=[]
  for t in product(range(R+1),repeat=4):
   if sum(t)>R:continue
   n1=[34+t[i]-S[i] for i in range(4)];n2=[17-n1[i]-t[i] for i in range(4)]
   if min(n1+n2)<0:continue
   hist.append({'lambda3_counts':t,'lambda1_counts':n1,'lambda2_counts':n2})
  assert R<=2 and hist
  tails.append({'quad':f['quad'],'degrees':f['degrees'],'counts':mu,'expanded35_masks':f['expanded35_masks'],'best_fixed':f['best'],'K6_pair_codegrees':inc,'K6_cost':q,'remaining_shared_tau':R,'selected_to_outside_row_totals':S,'shared_type_column_targets':cols,'actual_outside_degree_counts':dict(outside),'actual_seven_pool':outside[7],'at_least_seven_points_all_K_rows_le2':max(0,outside[7]-R),'complete_necessary_17point_row_histograms':hist})
 out.append({'spectrum_id':j['spectrum_id'],'key':key,'source_survivor_index':ki,'implicated_failure_count':len(tails),'implicated_tails':tails})
ans={'status':'COMPLETE_TYPED_INPUTS_ONLY_NO_NEW_STAR_TABLE_OR_LP','scope':__doc__,'remaining_keys':len(out),'jobs':out,'cpu_seconds':time.process_time()-st};(P/'IMPLICATED_THREE_KEYS.json').write_text(json.dumps(ans,indent=2)+'\n');print([(j['spectrum_id'],j['key']['tau'],j['implicated_failure_count']) for j in out],ans['cpu_seconds'])
