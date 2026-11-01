"""Exact final common-E contradiction; imported q4 proofs are receipts, not rerun here."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
a=json.loads((P/'NO_CRITICAL_RESULT.json').read_text());b=json.loads((P/'NO_CRITICAL_CHECK.json').read_text());rows=json.loads((P/'NO_CRITICAL_SURVIVORS33.json').read_text())
assert a['complete'] and b['status']=='PASS' and a['A2_final']==b['A2_survivors']==0
assert len(rows)==a['A3_final']==b['A3_survivors']==33 and all(r['a']==3 for r in rows)
E=Counter(595-r['n'][1] for r in rows);assert E=={70:24,71:7,72:2}
Q=P.parent/'four_nonunit_degree_six_center_20261020'
q=json.loads((Q/'RESULT.json').read_text());v=json.loads((Q/'INDEPENDENT_RESULT.json').read_text());c=json.loads((Q/'FIVE_LOCK_FULL5.json').read_text())
assert q['labeled_traces']==v['labeled_inputs']==23751 and q['S4_orbits']==1563 and v['status']=='PASS'
assert v['tail_matches_primary'] and v['all70_threshold_failure_sets_match'] and v['joint_tail_orbits']==5
assert len(c['cases'])==c['strict_count']==5
mx=max(Fraction(r['best']['bound']) for r in c['cases']);assert mx==Fraction(233003,240240) and all(r['zero_quota'] and r['best']['strict'] for r in c['cases'])
assert 6*5+29*4==146 and (146+1)//2==73
out=dict(status='PASS',scope=__doc__,A2_remaining=0,A3_aggregate_before_low_center=33,E_histogram=dict(E),actual_E_lower=73,A3_remaining_after_low_center=0,q4_imported_domain=23751,q4_imported_orbits=1563,q4_imported_joint_tails=5,q4_imported_max=str(mx),no_T33_T34_critical_or_threshold_import=True,cpu_seconds=time.process_time()-st)
(P/'ASSEMBLY_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
