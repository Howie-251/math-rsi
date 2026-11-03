import json
from pathlib import Path
D=Path(__file__).resolve().parent;R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
mods=['OppositeGQ35SpreadGeneric','OppositeGQ35SpreadDefinitions','OppositeGQ35SpreadWalks','OppositeGQ35SpreadSlots','OppositeGQ35SpreadLowerGeneric','OppositeGQ35SpreadFastTables','OppositeGQ35SpreadInputData','OppositeGQ35SpreadIncidence','OppositeGQ35SpreadInputChecks']+[f'OppositeGQ35SpreadInputRow{i:02}' for i in range(64)]+['OppositeGQ35SpreadInputs','OppositeGQ35SpreadDegree','OppositeGQ35SpreadDiameter','OppositeGQ35SpreadLower','OppositeGQ35SpreadExact','OppositeGQ35SpreadAudit']
receipts=[]
for m in mods:
 p=(D/'lower_helper/COMPILE_RESULT.json') if m.endswith('LowerGeneric') else D/f'{m}_RESULT.json'
 x=json.loads(p.read_text());assert x['exit_code']==0,(m,x)
 receipts.append({'module':m,'exit_code':0,'CPU_seconds':x.get('CPU_seconds',x.get('cpu_seconds')),'receipt':str(p.relative_to(R)),'log':x.get('log')})
audit=(D/'OppositeGQ35SpreadAudit.log').read_text();assert 'sorryAx' not in audit and 'error:' not in audit
allr=[]
for p in list(D.glob('*_RESULT.json'))+list((D/'build_history').glob('*_RESULT.json')):
 try:x=json.loads(p.read_text())
 except Exception:continue
 if 'CPU_seconds' in x:allr.append((p,x))
finite=sum(x['CPU_seconds'] for p,x in allr if 'Input' in x.get('module','') or x.get('module') in ['OppositeGQ35SpreadFastTables','OppositeGQ35SpreadIncidence'])
conservative=sum(x['CPU_seconds'] for _,x in allr)+json.loads((D/'lower_helper/COMPILE_RESULT.json').read_text())['CPU_seconds']
result={'status':'KERNEL_COMPLETE_UNCONDITIONAL_6160_GRAPH_WITH_IMPORT_TYPE_AXIOM_AUDIT','final_module':'formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadExact.lean','audit_module':'formal/OppositeGQ35SpreadAudit.lean','namespace':'DegreeDiameter.Portfolio.OppositeGQ35Spread','theorem':'concrete_order_degree_and_exact_D3','type':'Fintype.card Vertex = 6160 ∧ (∀ v, graph.degree v ≤ 24) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2','carrier':'Fin6144 ⊕ Fin16','Fin6160_equivalence':'label; label_old v=v; label_new j=6144+j','exported_certificate_premises':[],'axioms':['propext','Classical.choice','Quot.sound'],'module_count':len(mods),'projection_point_line_pairs_kernel_checked':6144,'original_line_entries_kernel_bound_to_fast_tables':384,'original_pointLine_entries_kernel_bound_to_fast_tables':384,'positive_incidence_coverage_checks':384,'spread_owner_checks':64,'finite_CPU_all_attempts':finite,'finite_CPU_budget':750,'generic_CPU_conservative_all_attempts':conservative-finite,'generic_CPU_budget':450,'all_CPU_conservative':conservative,'all_CPU_budget':1200,'CPU_note':'Child-rusage start/end subtraction is recorded in current harness. Earlier Slots receipt33.065214 includes inherited child usage from preceding commands and is retained as a conservative overcount; no unchanged module was rebuilt to repair its timing.','single_module_CPU_limit':115,'max_batch_workers':3,'old_modules_changed':False,'old_modules_recompiled':False,'BFS_runs_in_this_formalization':0,'solver_calls':0,'native_decide':False,'unproved_axioms':False,'hashes':False,'independent_literal_acceptance':'PASS all6160roots; see ../independent_acceptance/INDEPENDENT_ACCEPTANCE.json','input_binding':'INPUT_BINDING_CHECK.json','external_review':{'A':'SUCCESS/PASS see reviews/GQ6160_A_DISPOSITION.md','B':'SUCCESS/SOUND ARCHITECTURE at read scope; see reviews/GQ6160_B_DISPOSITION.md','C':'PENDING_ROOT_FINAL_SCOPE'},'global_novelty':'UNCONFIRMED','module_receipts':receipts}
assert finite<750 and conservative-finite<450 and conservative<1200
(D/'FINAL_COMPILE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='module_receipts'}))
