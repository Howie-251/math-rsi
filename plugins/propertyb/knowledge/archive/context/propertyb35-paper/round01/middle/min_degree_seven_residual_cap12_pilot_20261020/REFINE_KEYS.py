"""Apply only the complete tau-conditioned cap12 callers discovered for49/63 saved real-spectrum moment keys. No new moment-domain scan."""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();d=json.loads((P/'RESULT.json').read_text());jobs={};rows=[]
for c in d['context_scope']:
 z=c['key'];sid=c['spectrum_id'];caps=z['caps'].copy();n1=z['n'][1];n3=z['n'][3]
 if c['all_missing_quad_gates_discovered']:caps[3]=min(caps[3],12*n3)
 q,rem=divmod(2*n1,30);cells=[rem//5+int(i<rem%5) for i in range(5)];Pbox=360*q+sum(cells[i]*cells[j] for i in range(5) for j in range(i))
 tail=[sum(caps[i:]) for i in range(5)];v=6864*n1+sum(dw*min(Pbox,t) for dw,t in zip((36,84,210,462,924),tail))
 assert v<=z['twice_L']
 r={'spectrum_id':sid,'survivor_index':c['survivor_index'],'n':z['n'],'tau':z['tau'],'cap12_caller_complete_in_pilot':c['all_missing_quad_gates_discovered'],'old_twice_L':z['twice_L'],'new_twice_L':v,'new_caps':caps,'strict':v<5445440,'missing_quad_states':c['missing_quad_states']};rows.append(r)
 job=jobs.setdefault(sid,{'spectrum_id':sid,'source_keys':0,'cap12_complete_keys':0,'newly_strict_keys':0,'remaining':[]});job['source_keys']+=1;job['cap12_complete_keys']+=int(c['all_missing_quad_gates_discovered']);job['newly_strict_keys']+=int(r['strict'])
 if not r['strict']:job['remaining'].append(r)
for j in jobs.values():j['whole_source_spectrum_strict_given_new_caller_verification']=not j['remaining']
out={'status':'COMPLETE_SAVED63_KEY_REFINEMENT_PENDING_LOCAL_CERTIFICATE_AUDIT','scope':__doc__,'source_keys':len(rows),'cap12_complete_keys':sum(z['cap12_caller_complete_in_pilot'] for z in rows),'newly_strict_keys':sum(z['strict'] for z in rows),'whole_new_spectrum_ids':[sid for sid,j in jobs.items() if not j['remaining']],'remaining_keys':sum(len(j['remaining']) for j in jobs.values()),'jobs':list(jobs.values()),'all_keys':rows,'cpu_seconds':time.process_time()-st}
(P/'CAP12_KEY_REFINEMENT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('jobs','all_keys')})
for j in jobs.values():print(j['spectrum_id'],'source',j['source_keys'],'caller12',j['cap12_complete_keys'],'strict',j['newly_strict_keys'],'remain',len(j['remaining']))
