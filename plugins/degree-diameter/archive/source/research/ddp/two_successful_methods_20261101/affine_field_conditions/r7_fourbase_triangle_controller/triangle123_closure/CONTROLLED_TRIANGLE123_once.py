import csv,importlib.util,json,resource,time
from pathlib import Path

start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(1,2))
D=Path(__file__).resolve().parent
R=D.parent
diag=json.loads((R/'m33_global_batch/DIAGNOSTIC_RESULT.json').read_text())
old=diag['three_candidates'][2]['complete_signature']
original=[22,29,21,0,5,0,9,2,15,30]
assert old['parameters']==original
new=original.copy();new[5]=(new[7]-new[9])%33
assert new==[22,29,21,0,5,5,9,2,15,30]
spec=importlib.util.spec_from_file_location('existing_fourbase_m33_candidate_checker',R/'check_m33_candidate.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
check_start=time.process_time()
actual=module.check(new)
check_cpu=time.process_time()-check_start
oldmissing={(c['source'],c['target']):set(c['missing']) for c in old['classes']}
newmissing={(s,t):set() for s in range(4) for t in range(4)}
for c in actual['missing_supports']:newmissing[c['source'],c['target']]=set(c['missing'])
comparison=[]
for s in range(4):
    for t in range(4):
        before=oldmissing[s,t];after=newmissing[s,t]
        comparison.append({'source':s,'target':t,'old_support_size':33-len(before),'new_support_size':33-len(after),'old_missing':sorted(before),'new_missing':sorted(after),'gained_targets':sorted(before-after),'lost_targets':sorted(after-before),'old_full':not before,'new_full':not after})
bucket={5,16,27}
prediction_supported=not (newmissing[2,3]&bucket)
with (D/'CONTROLLED_TRIANGLE123_CLASS_COMPARISON.csv').open('w') as out:
    w=csv.writer(out);w.writerow(['source','target','old_support','new_support','old_missing','new_missing','gained','lost'])
    for c in comparison:w.writerow([c['source'],c['target'],c['old_support_size'],c['new_support_size'],json.dumps(c['old_missing']),json.dumps(c['new_missing']),json.dumps(c['gained_targets']),json.dumps(c['lost_targets'])])
result={'status':'ONE_CONTROLLED_TRIANGLE123_CHECK_COMPLETE','original_parameters':original,'new_parameters':new,'changed_parameter':'sigma23:0→5 only','triangle_closure_mod33':(new[7]-new[9]-new[5])%33==0,'existing_checker_calls':1,'original_candidate_rechecked':False,'new_checker_result':actual,'comparison_all_16_classes':comparison,'target_bucket_source2_target3_mod11_residue5':[5,16,27],'target_bucket_fully_repaired':prediction_supported,'simplicity_prediction_supported':actual['simple'],'old_B_triangles_preserved_by_unchanged_B_rule':True,'B3_zero_deck_targets_present_in_all_4_diagonal_supports':all(0 not in newmissing[s,s] for s in range(4)),'route_R_S_A_plus_old_value':(original[2]-original[5]+original[8])%33,'route_R_S_A_plus_new_value':(new[2]-new[5]+new[8])%33,'old_target3_in_new_03_support':3 not in newmissing[0,3],'new_target31_in_new_03_support':31 not in newmissing[0,3],'newly_incomplete_classes':[[c['source'],c['target']] for c in comparison if c['old_full'] and not c['new_full']],'fully_repaired_classes':[[c['source'],c['target']] for c in comparison if not c['old_full'] and c['new_full']],'net_missing_count_before':sum(len(x) for x in oldmissing.values()),'net_missing_count_after':sum(len(x) for x in newmissing.values()),'all_exact_three_classes_complete':actual['all_exact_three_supports_complete'],'candidate_passes_controller_gate':actual['candidate_passes_controller_gate'],'CPU_seconds_existing_checker_call':check_cpu,'total_measured_executable_CPU_seconds':time.process_time()-start,'CPU_budget_seconds':1,'all_local_processes_terminal':True,'producer_closure_symbolic_count_repeated':False,'new_global_or_local_parameter_searches':0,'graphs_BFS_Lean':0,'evidence':['CONTROLLED_TRIANGLE123_PRED.md','CONTROLLED_TRIANGLE123_CLASS_COMPARISON.csv','../m33_global_batch/DIAGNOSTIC_RESULT.json','../check_m33_candidate.py']}
(D/'CONTROLLED_TRIANGLE123_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
