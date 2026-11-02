import json
import pathlib
import resource
import subprocess
import sys
import time

HERE=pathlib.Path(__file__).resolve().parent
FORMS=pathlib.Path(sys.argv[1]).resolve()
START=time.process_time()
C0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+r.ru_utime+r.ru_stime-C0.ru_utime-C0.ru_stime
assert not (HERE/'RESULT.json').exists()
pred=json.loads((HERE/'PREDICTION.json').read_text())
frames=pred['new_phase_frame_representatives']
assert frames==[[2,10],[2,14],[2,34],[10,22]]
old=json.loads((HERE.parent/'generic_ab109_search/RESULT.json').read_text())
assert old['cases_processed']==71286 and not old['hit'] and not old['CPU_limited']
inputs=[]
for pa,pb in frames:
    folder=FORMS/f'frame_{pa}_{pb}'
    binaries=list(folder.glob('*.forms.bin'))
    assert len(binaries)==1
    inputs.append((pa,pb,binaries[0]))
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],check=True)
compiled=cpu()
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':'RUNNING_FIXED_FOUR_PHASE_FRAMES','forms_root':str(FORMS),'CPU_budget':30,'compile_CPU_seconds':compiled},indent=2)+'\n')
rows=[];stop='ALL_FOUR_NEW_FRAMES_COMPLETE';hit=None
for pa,pb,binary in inputs:
    if 29.5-cpu()<0.1:
        stop='CPU_BUDGET_BEFORE_NEXT_FRAME_UNKNOWN'
        break
    out=HERE/'frames'/f'frame_{pa}_{pb}';out.mkdir(parents=True,exist_ok=True)
    with (out/'search.log').open('w') as log:
        subprocess.run([str(HERE/'search'),str(binary),str(out),str(29.5-cpu()),str(pa),str(pb)],
                       stdout=log,stderr=log,check=True,timeout=40)
    one=json.loads((out/'NATIVE_RESULT.json').read_text())
    assert one['phase_pair']==[pa,pb]
    one.update(forms_input=str(binary),output_directory=str(out))
    (out/'RESULT.json').write_text(json.dumps(one,indent=2)+'\n')
    rows.append(one)
    print('FRAME '+json.dumps({k:one[k] for k in ['phase_pair','cases_processed','numeric_cases','capacity_pruned_cases','hit','CPU_limited','native_CPU_seconds']}),flush=True)
    if one['hit']:
        hit=json.loads((out/'FIRST_HIT.json').read_text())
        hit.update(graph_file=str(out/'graph_d4_D9_n11772.edges'),parameter_file=str(out/'FIRST_HIT.json'))
        stop='FIRST_COMPLETE_HIT'
        (HERE/'FIRST_HIT.json').write_text(json.dumps(hit,indent=2)+'\n')
        break
    if one['CPU_limited']:
        stop='CPU_BUDGET_WITH_PARTIAL_FRAME_UNKNOWN'
        break
processed=sum(r['cases_processed'] for r in rows)
result={'status':stop,'new_phase_frames_planned':4,'new_phase_frames_entered':len(rows),
        'new_normalized_settings_scope':285144,'new_normalized_settings_processed':processed,
        'new_numeric_settings':sum(r['numeric_cases'] for r in rows),
        'new_capacity_pruned_settings':sum(r['capacity_pruned_cases'] for r in rows),
        'unattempted_new_settings':285144-processed,
        'inherited_phase_frame':[2,22],'inherited_actual_old_frame':[10,14],
        'inherited_old_normalized_settings':71286,'inherited_frame_recomputed':False,
        'raw_unordered_phase_pairs':15,'phase_pair_orbits':5,
        'rows':rows,'slot_evaluations':sum(r['slot_evaluations'] for r in rows),
        'hit':hit is not None,'actual_graphs_generated':sum(r['actual_graphs_generated'] for r in rows),
        'actual_graph_orbit_BFS':sum(r['actual_graph_orbit_BFS'] for r in rows),
        'actual_n':11772 if hit else None,'actual_D':hit['actual_global_D'] if hit else None,
        'ordinary_bad_unordered_pairs':0 if hit else None,'hypothetical_n':11772,
        'compile_CPU_seconds':compiled,'native_CPU_seconds':sum(r['native_CPU_seconds'] for r in rows),
        'total_batch_CPU_seconds':cpu(),'source_BFS':0,
        'prediction':'SUPPORTED' if hit else 'REFUTED' if processed==285144 else 'UNRESOLVED',
        'pending':['Root independent acceptance/Gemini'] if hit else []}
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'RUN_HANDLE.json').write_text(json.dumps({'status':stop,'new_settings_processed':processed,'pending':result['pending'],'total_batch_CPU_seconds':result['total_batch_CPU_seconds']},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
