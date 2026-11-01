"""Exact20->23 difference on the unchanged981 graph domain and76 old duals."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time();BASE=HERE.parent/'six_label_pilot'
j=json.loads((BASE/'CENSUS_PROFILE.json').read_text());new=[];raw=[]
for r in j['rows']:
 failed=[]
 for p in r['maximal_b_parameter_rows']:
  a=p['C3_margin'];b=p['C4_margin']-3
  if a<=0 and b<=0:failed.append(dict(p,b=p['b']+3,C4_blocker=p['C4_blocker']+3,C4_margin=b))
 if failed:
  item={'graph':r['vector'],'orbit_size':r['orbit_size'],'sets':r['sets'],'C3':r['C3'],'C4':r['C4'],
        'two_isolates':r['two_isolates_analytic_repair'],'failed_maximal_b_parameters':failed}
  raw.append(item)
  if not r['nongated_maximal_b_rows']:new.append(item)
certs=json.loads((BASE/'joint_cover_lp/ALL77.json').read_text());duals=[]
for r in certs['rows']:
 if 'dual_certificate' in r:
  c=r['dual_certificate'];bound=F(c['coverage_upper_bound'])+3*F(c['budget_weights'][2]);duals.append({'graph':r['graph'],'bound23':str(bound),'strict':bound<1})
# Record payoff only against the frozen current79 that survived the proposed21 gate.
P6=HERE.parent/'budget21_difference/P6_REMAINING.jsonl'
actual=[json.loads(x) for x in P6.open()]
coverage={k:[] for k in (22,23)}
for i,r in enumerate(actual):
 for budget in (22,23):
  w=next((c for c in r['choices'] if c['signature'][:6]==[9,0,0,0,0,0] and c['signature'][6]<=3 and sum(c['signature'][6:8])<=budget),None)
  if w:coverage[budget].append({'source_index':i,'inventory':r['inventory'],'nine':r['nine'],'higher':r['higher'],'J':r['J'],
    'own_blue':w['blue'],'signature':w['signature']})
out={'status':'COMPLETE_EXACT_DIFFERENCE','old981':981,'raw_sum_nongated_at23':len(raw),
 'newly_nongated_old902':len(new),'newly_nongated_records':new,
 'old76_all_cost23_strict':all(r['strict'] for r in duals),'old76_max_cost23':str(max(F(r['bound23']) for r in duals)),
 'old76_cost23':duals,'all_raw_sum_nongated':raw,
 'current_P6_79_sources':len(actual),'P6_coverage_if22':len(coverage[22]),'P6_coverage_if23':len(coverage[23]),
 'P6_diagnostic_coverage':coverage,'cpu_seconds':time.process_time()-start,
 'scope':'No new graph classification, no LP. Payoff gates are not yet proved.'}
(HERE/'DIFFERENCE.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ('newly_nongated_records','old76_cost23','all_raw_sum_nongated','P6_diagnostic_coverage')})
