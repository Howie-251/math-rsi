"""Combine root's new vertex-flag P (declared upstream lemma) with the15 exact remaining pilot-cap12 keys, without a new domain scan."""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time();old=json.loads((P/'CAP12_KEY_REFINEMENT.json').read_text());ps=json.loads((ROOT/'context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/RESULT.json').read_text());lookup={(j['spectrum_id'],tuple(k['n']),k['tau']):k for j in ps['jobs'] for k in j['keys']};rows=[]
for j in old['jobs']:
 for k in j['remaining']:
  z=lookup[j['spectrum_id'],tuple(k['n']),k['tau']];caps=k['new_caps'];shared=z['newP'];v=-1 if shared<0 else 6864*k['n'][1]+sum(dw*min(shared,sum(caps[i:])) for i,dw in enumerate((36,84,210,462,924)))
  rows.append({'spectrum_id':j['spectrum_id'],'n':k['n'],'tau':k['tau'],'cap12_actual_caller_complete_in_pilot':k['cap12_caller_complete_in_pilot'],'caps':caps,'old_twice_L':k['new_twice_L'],'newP':shared,'oldP':z['oldP'],'new_twice_L':v,'strict':v<5445440})
out={'status':'COMPLETE_SAVED15_KEY_REFINEMENT_CONDITIONAL_ON_ROOT_NEW_P_LEMMA','scope':__doc__,'source_keys':len(rows),'strict_keys':sum(k['strict'] for k in rows),'remaining_keys':sum(not k['strict'] for k in rows),'newly_whole_spectrum_ids':[j['spectrum_id'] for j in old['jobs'] if j['remaining'] and all(k['strict'] for k in rows if k['spectrum_id']==j['spectrum_id'])],'keys':rows,'cpu_seconds':time.process_time()-st};(P/'NEWP_REFINEMENT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
