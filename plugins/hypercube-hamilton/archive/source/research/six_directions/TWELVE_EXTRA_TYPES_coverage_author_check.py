"""Producer structural/set validation of all hit sets, greedy cover and residual bytes."""
from pathlib import Path
from collections import defaultdict
import json,struct
P=Path(__file__).resolve().parent
out=json.loads((P/'TWELVE_EXTRA_TYPES_coverage.json').read_text());profile=json.loads((P/'TWELVE_EXTRA_TYPES_profile.json').read_text())
g={r['index']:r for r in profile['rows']};chosen=set(out['greedy_registry_indices']);positive=set(out['producer_full_rank_indices'])
inputs={v:(P/f'TWELVE_NEW_FORCED_HALL_union_remaining_v{v}.bin').read_bytes() for v in (1,7,31)}
sets=defaultdict(set);union=set();selected=set()
for name,selection in [('TWELVE_EXTRA_TYPES_positive_hits.bin',False),('TWELVE_EXTRA_TYPES_selected_witnesses.bin',True)]:
 raw=(P/name).read_bytes();assert len(raw)%28==0
 seen=set()
 for v,i,orb,d,S,M,J,U in struct.iter_unpack('<BIHBQIII',raw):
  assert orb in (chosen if selection else positive) and 0<=d<6
  rec=inputs[v][i*11:i*11+11];assert len(rec)==11
  Z=set(rec[:5]);W=set(rec[5:]);A={x for x in range(64) if (x>>d&1)==(v>>d&1)}
  source={x for x in range(64) if S>>x&1};s=len(Z&A)+1-len(W&A)
  assert len(source)==abs(s) and len(source)==len(g[orb]['omitted'])
  if s>0:assert len(W&A)>=1 and source<=Z&A;minor=Z-A;major=W-A
  else:assert source<=W&A and (1<<d) not in source;minor=W-A;major=Z-A
  project=lambda x:(x&((1<<d)-1))|((x>>(d+1))<<d)
  assert M==sum(1<<project(x) for x in minor)
  assert U==sum(1<<project(x) for x in source)
  assert J==sum(1<<project(x) for x in major)|U
  assert not M&J and U&J==U
  rid=(v,i)
  if selection:assert rid not in selected;selected.add(rid)
  else:
   assert (rid,orb) not in seen;seen.add((rid,orb));sets[orb].add(rid);union.add(rid)
assert len(union)==len(selected)==out['all_positive_covered'] and union==selected
assert set().union(*(sets[i] for i in chosen))==union
for i in positive:assert len(sets[i])==g[i]['actual_records']
for r in out['reports']:
 v=r['v'];raw=inputs[v];expected=b''.join(raw[i:i+11] for i in range(0,len(raw),11) if (v,i//11) not in union)
 assert expected==(P/r['remaining_file']).read_bytes() and len(expected)==r['remaining']*11
result={'status':'PASS_PRODUCER_NOT_FRESH_REVIEW','complete_positive_hit_records':out['all_positive_hit_records'],'positive_union':out['all_positive_covered'],'greedy_rows':len(chosen),'all_selected_actual_source_projection_witnesses_replayed':True,'exact_remaining_bytes':True,'all_positive_orbit_counts_equal_profile':True,'full_twelve_hole_proved':False,'full_P6_proved':False}
(P/'TWELVE_EXTRA_TYPES_coverage_author_check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
