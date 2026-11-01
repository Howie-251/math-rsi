"""Summaries and hypothetical-interface coverage, never new accepted gates."""
import json
from pathlib import Path
from collections import Counter
from itertools import combinations
HERE=Path(__file__).resolve().parent
j=json.loads((HERE/'CENSUS.json').read_text());cells=[]
for inv in j['inventories']:
 for nine in (0,5):
  rs=[r for r in j['rows'] if r['inventory']==inv and r['nine']==nine]
  assert len(rs)==rs[0]['high_orbits_in_cell']
  assert sum(r['high_orbit_size'] for r in rs)==rs[0]['labelled_high_families_in_cell']
  cells.append({'inventory':inv,'nine':nine,'higher_orbits':len(rs),
   'labelled_higher':sum(r['high_orbit_size'] for r in rs),
   'necessary':sum(r['necessary'] for r in rs),
   'passed':sum(sum(r['passed'].values()) for r in rs),
   'nongated':sum(r['nongated'] for r in rs),
   'nongated_higher_orbits':sum(bool(r['nongated']) for r in rs)})
preds={
 '9P4_Tle3_Ntotalle20':lambda s:s[:6]==(9,0,0,0,0,0) and s[6]<=3 and s[6]+s[7]<=20,
 '8mixed_2small_Tle2_Ntotalle21':lambda s:sum(s[:4])==8 and s[1]<=2 and not any(s[k] for k in (2,3,4,5)) and s[6]<=2 and s[6]+s[7]<=21,
 '10P4_Tle4_Ntotalle20':lambda s:s[:6]==(10,0,0,0,0,0) and s[6]<=4 and s[6]+s[7]<=20,
}
cover={k:set() for k in preds};weights={m['id']:m['necessary_count'] for m in j['menus']}
best=Counter();freq=Counter();clean=0
for m in j['menus']:
 ss={tuple(r['counts'][:8]) for r in m['signatures']}
 for s in ss:freq[s]+=weights[m['id']]
 ok=[s for s in ss if not any(s[k] for k in (2,3,4,5))]
 if ok:
  clean+=weights[m['id']]
  best[min(ok,key=lambda s:(sum(s[:4]),s[1],s[6],s[7]))]+=weights[m['id']]
 for k,pred in preds.items():
  if any(map(pred,ss)):cover[k].add(m['id'])
union=set().union(*cover.values());left=[]
for line in (HERE/'CENSUS_NONGATED.jsonl').open():
 r=json.loads(line)
 if r['menu_id'] not in union:left.append(r)
out={'status':'COMPLETE','note':'All candidate interfaces below are UNPROVED and were not accepted by the selector.',
 'cells':cells,'all_nongated_with_clean_3_4_interface':clean,
 'candidate_statements_not_proved':{k:sum(weights[x] for x in v) for k,v in cover.items()},
 'candidate_pairs_not_proved':{' + '.join(ks):sum(weights[x] for x in cover[ks[0]]|cover[ks[1]]) for ks in combinations(preds,2)},
 'candidate_three_union_not_proved':sum(weights[x] for x in union),
 'left_after_all_three_not_proved':len(left),'remaining_keys_after_three_hypotheses':left,
 'best_signature_order':'minimum total positive count, then P3,N3,N4; no claim of mathematical optimality',
 'best_clean_signatures':[{'counts':k,'necessary_count':v} for k,v in best.most_common()],
 'most_frequent_clean_signatures':[{'counts':k,'necessary_count':v} for k,v in freq.most_common(20)]}
(HERE/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('best_clean_signatures','most_frequent_clean_signatures','cells')},indent=2))
