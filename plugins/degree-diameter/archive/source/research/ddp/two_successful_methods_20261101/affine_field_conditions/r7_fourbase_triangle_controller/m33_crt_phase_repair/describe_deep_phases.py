"""Read existing phase records only; no support reevaluation or new phases."""
import json
from pathlib import Path
from time import process_time

start=process_time();root=Path(__file__).resolve().parent
assert not (root/'DEEP_PHASES.json').exists()
capacity=json.loads((root/'CAPACITY_RESULT.json').read_text())
raw=(root/'PHASE_ATTEMPTS.bin').read_bytes();free=[0,1,2,4,5,6,7,8,9]
deep=[]
for offset in range(0,len(raw),13):
    if raw[offset+10]!=1 or raw[offset+11]!=3:continue
    profile=raw[offset];phase=list(raw[offset+1:offset+10])
    q=capacity['profiles'][profile-1]['fixed_parameters_mod11'];v=list(q);index=0
    for j,p in zip(free,phase):
        v[j]=q[j]+11*((2*(p-q[j]))%3);index=3*index+p
    deep.append({'profile':profile,'phase_index_0based':index,'phases':phase,
                 'parameters':v,'first_failed_class':3,'support_size':raw[offset+12]})
relations=[]
for profile in [1,2]:
    pair=[d for d in deep if d['profile']==profile]
    assert len(pair)==2
    assert [(23*x)%33 for x in pair[0]['parameters']]==pair[1]['parameters']
    relations.append({'profile':profile,'number_preserving_first_eight_classes':2,
                      'existing_candidates_related_by_unit23':True,
                      'unit_mod11':23%11,'unit_mod3':23%3,
                      'phase_or_support_assignments_newly_evaluated':0})
result={'status':'COMPLETE_READ_ONLY_DEEP_PHASE_DESCRIPTION','deep_candidates':deep,
        'relations':relations,'support_reevaluations':0,'new_phase_assignments':0,
        'CPU_seconds':process_time()-start,'running':False,'active_processes':[]}
(root/'DEEP_PHASES.json').write_text(json.dumps(result,indent=2)+'\n')
final=json.loads((root/'RESULT.json').read_text());final['read_only_description_CPU_seconds']=result['CPU_seconds'];final['accounted_CPU_seconds']+=result['CPU_seconds']
for name in ['RESULT.json','TERMINAL.json']:(root/name).write_text(json.dumps(final,indent=2)+'\n')
print(json.dumps(result))
