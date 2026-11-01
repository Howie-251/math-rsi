"""Actual-source filters; only the mixed21 patch and hypothetical ten-gate are new."""
from pathlib import Path
from collections import Counter
import json
HERE=Path(__file__).resolve().parent
rows=[json.loads(s) for s in (HERE/'TAIL186.jsonl').open()]
def mix(s):return sum(s[:4])==8 and s[1]<=2 and all(s[k]==0 for k in (2,3,4,5,6)) and s[7]<=21
def ten(s):return s[:6]==[10,0,0,0,0,0] and s[6]<=2 and s[7]<=18
m=[];rest=[];both=[];after=[];observations=Counter()
for i,r in enumerate(rows):
 mc=next((c for c in r['choices'] if mix(c['signature'])),None)
 tc=next((c for c in r['choices'] if ten(c['signature'])),None)
 if mc:m.append(dict(r,original_tail_index=i,selected_blue=mc['blue'],selected_signature=mc['signature'],
   selected_positive_source_indices=mc['positive_source_indices'],selected_negative_source_indices=mc['negative_source_indices'],
   gate='EIGHT_MIXED_TWO_SMALL_EIGHTEEN_REPAIR_ZERO_TRIPLE_21_EXTENSION',mathematical_status='PROVED_ROOT_PAPER_ACCEPTED_CROSS_MODEL_SCOPE_PENDING'))
 else:rest.append(dict(r,original_tail_index=i))
 if mc and tc:both.append(i)
 if not mc and not tc:after.append(dict(r,original_tail_index=i,conditional_scope='Still remains even if the unproved10P4/T<=2/B<=18 gate is established.'))
for name,rs in [('MIXED21_SOURCES47.jsonl',m),('AFTER_MIXED21_TAIL139.jsonl',rest),('IF_TEN_PROVED_TAIL42.jsonl',after)]:
 with (HERE/name).open('w') as f:
  for r in rs:f.write(json.dumps(r,separators=(',',':'))+'\n')
assert (len(m),len(rest),len(both),len(after))==(47,139,44,42)
cells=Counter((tuple(r['inventory']),r['nine']) for r in after);best=Counter();freq=Counter()
for r in after:
 ss={tuple(c['signature'][:8]) for c in r['choices'] if not any(c['signature'][k] for k in (2,3,4,5))}
 for s in ss:freq[s]+=1
 best[min(ss,key=lambda s:(sum(s[:4]),s[1],s[6],s[7]))]+=1
out={'source_tail':186,'mixed21_actual_sources':47,'remaining_after_mixed21':139,
 'unproved_ten_interface_sources':141,'overlap':44,'union_if_ten_proved':144,'remaining_if_ten_proved':42,
 'new_mixed_patch_status':'PROVED: EIGHT_MIXED_TWO_SMALL_EIGHTEEN_REPAIR.md appended zero-triple21 extension; root paper accepted, new cross-model scope pending',
 'ten_gate_status':'unproved diagnostic target, not accepted by this report',
 'remaining42_cells':[{'inventory':i,'nine':n,'inputs':c} for (i,n),c in sorted(cells.items())],
 'remaining42_best_signatures':[{'counts':k,'inputs':v} for k,v in best.most_common()],
 'remaining42_top_signatures':[{'counts':k,'inputs':v} for k,v in freq.most_common(20)]}
(HERE/'CUTS_SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
