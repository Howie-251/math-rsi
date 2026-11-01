from pathlib import Path
from collections import Counter
import json
HERE=Path(__file__).resolve().parent
j=json.loads((HERE/'SUMMARY.json').read_text());rows=[json.loads(x) for x in (HERE/'TAIL186.jsonl').open()]
w=j['candidate_witnesses']['10P4_Tle2_Ble18'];outrows=[]
for a in w:
 r=rows[a['tail_index']];S=a['blue'];assert len(S)==2
 bmask=sum(1<<v for v in S)
 lam=sum((mask&bmask)==bmask for mask in r['trace_masks'])
 assert r['J'][list(__import__('itertools').combinations(range(6),2)).index(tuple(S))]==0
 assert all(set(S)&set(t) for t in r['higher'])
 outrows.append(dict(a,lambda_between_blue_centres=lam))
out={'first_own_witnesses':len(w),'all_witnesses_are_blue_pairs':True,'all_pair_J_multiplicities_zero':True,'all_higher_traces_proper':True,
 'private_group_size_histogram':[{'sizes':k,'sources':v} for k,v in Counter(tuple(sorted(a['private_star_counts'])) for a in w).items()],
 'blue_centre_degree_histogram':[{'degrees':k,'sources':v} for k,v in Counter(tuple(sorted(a['blue_point_P_degree'])) for a in w).items()],
 'lambda_histogram':dict(Counter(a['lambda_between_blue_centres'] for a in outrows)),
 'maximum_private_union_bound_histogram':dict(Counter(max(a['private_star_union_lower_bounds']) for a in w)),
 'witnesses':outrows}
(HERE/'STRUCTURE.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='witnesses'})
