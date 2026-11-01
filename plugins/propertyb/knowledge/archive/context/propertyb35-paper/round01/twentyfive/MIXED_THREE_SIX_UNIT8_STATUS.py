"""Bind the completed screen and bounded partial DP without running any DP."""
from pathlib import Path
from fractions import Fraction as Q
import json
P=Path(__file__).resolve().parent;s=json.loads((P/'MIXED_THREE_SIX_UNIT8_SCREEN.json').read_text());d=json.loads((P/'MIXED_THREE_SIX_UNIT8_PILOT.json').read_text());done={(z['base'],tuple(z['low'])):z for z in d['results']};strict_labels=0;strict_orbits=0;failed=[];unprocessed=[]
for z in s['orbits']:
 if Q(z['raw_ABC_bound'])<1:strict_labels+=len(z['low_labels']);strict_orbits+=1;continue
 w=done.get((z['base'],tuple(z['low'])))
 if w is None:unprocessed.append(dict(base=z['base'],low=z['low'],low_labels=z['low_labels'],screen_bound=z['raw_ABC_bound']));continue
 if Q(w['raw_ABC_bound'])<1:strict_labels+=len(z['low_labels']);strict_orbits+=1
 else:failed.append(dict(base=z['base'],low=z['low'],low_labels=z['low_labels'],counts=w['counts'],positions=w['positions'],reported_DP_optimum=w['bound'],raw_witness_bound=w['raw_ABC_bound']))
out=dict(scope=__doc__,full_domain_marked_inputs=2968,full_domain_marked_orbits=915,full_screen_seconds=s['summary']['elapsed_seconds'],screen_strict_labels=s['summary']['strict'],DP_expected_residual_orbits=130,DP_processed_orbits=len(d['results']),DP_strict_orbits=d['summary']['raw_strict'],DP_seconds=d['summary']['elapsed_seconds'],strict_labels_with_witnesses=strict_labels,strict_orbits_with_witnesses=strict_orbits,non_strict_processed_orbits=len(failed),non_strict_labels=sum(len(z['low_labels']) for z in failed),unprocessed_orbits=len(unprocessed),unprocessed_labels=sum(len(z['low_labels']) for z in unprocessed),gate_raw_complete=False,full_strict_domain_replay_claimed=False,non_strict=failed,unprocessed=unprocessed)
assert strict_labels+out['non_strict_labels']+out['unprocessed_labels']==2968 and strict_orbits+len(failed)+len(unprocessed)==915
(P/'MIXED_THREE_SIX_UNIT8_STATUS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['non_strict','unprocessed']},indent=2))
