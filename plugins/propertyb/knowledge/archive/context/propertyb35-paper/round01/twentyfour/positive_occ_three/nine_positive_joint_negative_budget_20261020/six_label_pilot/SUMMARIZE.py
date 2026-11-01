from pathlib import Path
from collections import Counter
import json
HERE=Path(__file__).resolve().parent;j=json.loads((HERE/'CENSUS_PROFILE.json').read_text());E=j['edge_order']
raw=[r for r in j['rows'] if r['nongated_maximal_b_rows']];ng=[r for r in raw if r['unresolved_by_bounds_and_analytic']]
def components(r):
 adj=[set() for _ in range(6)]
 for (a,b),v in zip(E,r['vector']):
  if v:adj[a].add(b);adj[b].add(a)
 left=set(range(6));sizes=[]
 while left:
  todo=[next(iter(left))];s=set()
  while todo:
   a=todo.pop()
   if a in s:continue
   s.add(a);todo.extend(adj[a]-s)
  left-=s;sizes.append(len(s))
 return tuple(sorted(sizes))
records=[]
for r in raw:
 intervals=[]
 for par in r['nongated_maximal_b_rows']:
  u,t,v=par['u'],par['t'],par['v']
  low=max(v,r['C4']-r['C4_pair_prefix_sums'][u]-(t-u+v)*r['C4_max_triple_extension']+v)
  assert low<=20-t and r['C3']<=r['C3_pair_prefix_sums'][u]+t-u+v
  intervals.append({'u':u,'t':t,'v':v,'b_min':low,'b_max':20-t})
 records.append({'vector':r['vector'],'orbit_size':r['orbit_size'],'E':r['E'],'M3':r['M3'],'degrees':r['degrees'],
  'isolated_labels':r['isolated_labels'],'support_components':components(r),'C3':r['C3'],'C4':r['C4'],
  'resolved_by_two_isolates':r['two_isolates_analytic_repair'],'all_nongated_parameter_intervals':intervals})
out={'status':'COMPLETE','labelled_domain':417328,'orbit_domain':981,'raw_bound_nongated_orbits':len(raw),
 'two_isolates_orbits':sum(r['two_isolates_analytic_repair'] for r in j['rows']),
 'two_isolates_raw_nongated_resolved':sum(r['two_isolates_analytic_repair'] for r in raw),
 'remaining_orbits':len(ng),'remaining_labelled':sum(r['orbit_size'] for r in ng),
 'remaining_E_histogram':dict(Counter(r['E'] for r in ng)),
 'remaining_M3_histogram':dict(Counter(r['M3'] for r in ng)),
 'remaining_isolates_histogram':dict(Counter(r['isolated_labels'] for r in ng)),
 'remaining_components':[{'sizes':k,'orbits':v} for k,v in sorted(Counter(components(r) for r in ng).items())],
 'remaining_min_t_histogram':dict(Counter(min(p['t'] for p in r['nongated_maximal_b_rows']) for r in ng)),
 'all_raw_bound_nongated_records':records,
 'scope':'Failure of candidate blocker bounds only, not feasible negative layouts or signed counterexamples.'}
(HERE/'CENSUS_SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='all_raw_bound_nongated_records'})
