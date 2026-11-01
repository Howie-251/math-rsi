"""Exact same-domain21-budget differences, no new classification or LP."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
BASE=HERE.parent/'six_label_pilot'
j=json.loads((BASE/'CENSUS_PROFILE.json').read_text())
old_strict=[r for r in j['rows'] if not r['nongated_maximal_b_rows']]
new=[];all_raw_new=[];min_strict=None
for r in j['rows']:
 failed=[]
 for q in r['maximal_b_parameter_rows']:
  c3=q['C3_margin'];c4=q['C4_margin']-1
  if c3<=0 and c4<=0:failed.append({'u':q['u'],'t':q['t'],'v':q['v'],'b':q['b']+1,
    'C3_blocker':q['C3_blocker'],'C4_blocker':q['C4_blocker']+1,'C3_margin':c3,'C4_margin':c4})
  if r in old_strict:
   margin=max(c3,c4)
   min_strict=margin if min_strict is None else min(min_strict,margin)
 if failed:
  rec={'graph':r['vector'],'orbit_size':r['orbit_size'],'failed_maximal_b_parameters':failed}
  all_raw_new.append(rec)
  if not r['nongated_maximal_b_rows']:new.append(rec)
certs=json.loads((BASE/'joint_cover_lp/ALL77.json').read_text())
duals=[]
for r in certs['rows']:
 if 'dual_certificate' not in r:continue
 c=r['dual_certificate'];old=F(c['coverage_upper_bound']);delta=F(c['budget_weights'][2]);bound=old+delta
 duals.append({'graph':r['graph'],'bound20':str(old),'beta_total':str(delta),'bound21':str(bound),'strict':bound<1})
assert len(old_strict)==902 and len(duals)==76
# Actual current139 own-source menus, and direct colour rebuild for each accepted source.
P6=HERE.parents[2]/'p6_residual_census_20261020'/'tail186_analysis'
rows=[json.loads(s) for s in (P6/'AFTER_MIXED21_TAIL139.jsonl').open()]
covered=[];remaining=[]
for r in rows:
 choices=[]
 for choice in r['choices']:
  S=set(choice['blue']);bm=sum(1<<v for v in S);pos=Counter();neg=Counter()
  for m in r['trace_masks']:
   if m&bm and m&~bm:continue
   (pos if not m&~bm else neg)[5-m.bit_count()]+=1
  sig=(pos[4],pos[3],pos[2],pos[1],neg[1],neg[2],neg[3],neg[4])
  assert sig==tuple(choice['signature'][:8])
  if sig[:6]==(9,0,0,0,0,0) and sig[6]<=3 and sig[6]+sig[7]<=21:choices.append((choice,sig))
 if choices:
  c,s=choices[0];covered.append(dict(r,selected_blue=c['blue'],selected_signature=c['signature'],
   proposed_gate='NINE_P4_Tle3_TOTAL_NEG21_SAME_DOMAIN_EXTENSION',mathematical_status='EXACT_DIFFERENCE_PROOF_READY_ROOT_ASSEMBLY_PENDING'))
 else:remaining.append(r)
for name,data in [('P6_OWN_SOURCES.jsonl',covered),('P6_REMAINING.jsonl',remaining)]:
 with (HERE/name).open('w') as f:
  for r in data:f.write(json.dumps(r,separators=(',',':'))+'\n')
out={'status':'EXACT_DIFFERENCE_COMPLETE','old_domain_orbits':981,'old_raw_sum_strict_orbits':902,
 'new_raw_sum_nongated_orbits':len(all_raw_new),'newly_nongated_from_old902':len(new),'newly_nongated_records':new,
 'minimum_joint_strict_margin_on_old902_at21':min_strict,
 'dual76_all_strict_at21':all(d['strict'] for d in duals),'dual76_max_bound21':str(max(F(d['bound21']) for d in duals)),
 'dual_records':duals,'two_isolates_scalar':{'Kge5':{'bound':69,'candidate_min':80},'K4_ule2':{'bound':60,'candidate_min':64},'K4_unonmax':{'bound':61,'candidate_min':64},'K4_final_shared_pair':'unchanged <=9<16'},
 'one_integer_case':'unchanged; does not use total negative count',
 'low_occurrence_bound21':str(3*F(7,16)**3+18*F(7,16)**4),
 'P6_current139_sources':len(rows),'P6_new21_source_count':len(covered),'P6_remaining_count':len(remaining),
 'P6_remaining_by_cell':[{'inventory':k[0],'nine':k[1],'sources':v} for k,v in Counter((tuple(r['inventory']),r['nine']) for r in remaining).items()],
 'P6_new21_signatures':[{'signature':k,'sources':v} for k,v in Counter(tuple(r['selected_signature'][:8]) for r in covered).items()],
 'cpu_seconds':time.process_time()-start,
 'scope':'Only exact budget difference on existing complete981 graph domain and76 certificates, plus current139 own-source replay. No LP or new graph/H domain.'}
(HERE/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ('dual_records','newly_nongated_records')})
