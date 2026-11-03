"""Read saved attempts once; check only two previously unreported candidates."""
import importlib.util
import json
from pathlib import Path
from time import process_time,perf_counter

start,wall=process_time(),perf_counter()
root=Path(__file__).resolve().parent
assert not (root/'DIAGNOSTIC_RESULT.json').exists(),'One diagnostic already completed.'
batch=json.loads((root/'RESULT.json').read_text())
assert batch['status']=='UNKNOWN_SAMPLE_CAP_REACHED'
order=batch['check_order']; reps=batch['branch_representatives']
branch_of=[-1]*33
for i,a in enumerate(reps):branch_of[a]=i
fail_depth=[16]*256
for i,c in enumerate(order):fail_depth[c]=i
depths=[[0]*17 for _ in reps]
firstfails=[[0]*16 for _ in reps]
selected=[]
raw=(root/'ATTEMPTS.bin').read_bytes()
assert len(raw)==24000000
for offset in range(0,len(raw),12):
    branch=branch_of[raw[offset]];failed=raw[offset+10]
    depths[branch][fail_depth[failed]]+=1
    if failed!=255:firstfails[branch][failed]+=1
    if failed==3:
        selected.append({'attempt_1based':offset//12+1,'parameters':list(raw[offset:offset+10]),
                         'first_failed_class':failed,'first_failed_support_size':raw[offset+11]})
assert len(selected)==3
existing=json.loads((root/'EXAMPLE_COVERAGE.json').read_text())
spec=importlib.util.spec_from_file_location('m33_candidate_checker',root.parent/'check_m33_candidate.py')
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
targeted=0
for candidate in selected:
    if candidate['parameters']==existing['parameters']:
        signature=existing;source='reused_existing_EXAMPLE_COVERAGE.json'
    else:
        actual=checker.check(candidate['parameters']);targeted+=1
        sizes=actual['support_sizes'];missing={(r['source'],r['target']):r['missing'] for r in actual['missing_supports']}
        signature={'parameters':candidate['parameters'],
                   'classes':[{'source':s,'target':t,'support_size':sizes[s][t],
                               'missing':missing.get((s,t),[])}for s in range(4)for t in range(4)]}
        source='one_targeted_check_m33_candidate.check_call'
    candidate['signature_source']=source
    candidate['complete_signature']=signature
assert targeted==2
branches=[]
for i,a in enumerate(reps):
    total=sum(depths[i])
    branches.append({'a0':a,'candidates':total,'passed_3_to_3':total-depths[i][0],
                     'passed_0_to_2':total-depths[i][0]-depths[i][1],
                     'first_failure_by_completed_check_count_0_through16':depths[i],
                     'passed_each_class_in_order':[sum(depths[i][d+1:])for d in range(16)],
                     'first_failure_by_source_times4_plus_target':firstfails[i]})
bad_sets=[{(c['source'],c['target'])for c in candidate['complete_signature']['classes']if c['missing']}for candidate in selected]
common=set.intersection(*bad_sets)
result={'status':'COMPLETE_READ_ONLY_EXISTING_SAMPLE_DIAGNOSTIC','source_batch_status':batch['status'],
        'check_order':order,'records_read_once':len(raw)//12,'new_global_samples':0,
        'bulk_support_replays':0,'targeted_single_candidate_checks':targeted,
        'reused_complete_signatures':1,'branches':branches,'three_candidates':selected,
        'common_incomplete_basepairs':[list(x)for x in sorted(common)],
        'CPU_seconds':process_time()-start,'wall_seconds':perf_counter()-wall,
        'CPU_budget_seconds':2,'running':False,'active_processes':[]}
(root/'DIAGNOSTIC_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'CPU_seconds':result['CPU_seconds'],
                  'branches':branches,'three_candidates':selected,
                  'common_incomplete_basepairs':result['common_incomplete_basepairs']}))
