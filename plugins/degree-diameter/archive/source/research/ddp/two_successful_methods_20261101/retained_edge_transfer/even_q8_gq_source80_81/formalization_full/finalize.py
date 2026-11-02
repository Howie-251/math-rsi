"""Record completed actual compile receipts; does not run Lean or graph checks."""
import json,os,re,time
from pathlib import Path
T=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
def save(path,value):
    temp=path.with_suffix(path.suffix+'.tmp');temp.write_text(json.dumps(value,indent=2)+'\n');os.replace(temp,path)
s=json.loads((D/'CHECKPOINT.json').read_text());plan=json.loads((D/'MODULE_PLAN.json').read_text())
mods=plan['common']+plan['leaves']+plan['assembly']
assert not s['running'] and not s['active_modules']
assert s['source_targets_complete'] and set(mods)==set(s['completed'])
assert s['status']in {'ALL_MODULES_PASS_AWAIT_EXTERNAL_BINDING','COMPLETE_KERNEL_AUDIT_AND_EXTERNAL_BINDING_PASS'}
binding=json.loads((D/'EXTERNAL_TABLE_BINDING.json').read_text())
assert binding['status'].startswith('PASS_')
for mod in mods:
    good=[a for a in s['attempts']if a['module']==mod and a['PASS']]
    assert len(good)==1,(mod,len(good))
    assert good[0]['exit_code']==0 and Path(good[0]['output']).exists()
    assert good[0]['CPU_seconds']<60
fail=[a for a in s['attempts']if not a['PASS']]
assert all(a.get('classification')in {'CONTROLLED_COST_REASSESSMENT','ASSEMBLY_TACTIC_IMPORT_MISSING','ASSEMBLY_TACTIC_IMPORT_RUNTIME_STALL','ASSEMBLY_NATIVE_STACK_OVERFLOW','EXACT_GRAPH_ALIAS_INSTANCE'}for a in fail)
audit=next(a for a in s['attempts']if a['module']=='EvenQ8SourceFullAudit'and a['PASS'])
audittext=Path(audit['log']).read_text()
assert 'error:'not in audittext and 'sorryAx'not in audittext
std={'propext','Classical.choice','Quot.sound'}
groups=re.findall(r'depends on axioms: \[([^\]]*)\]',audittext)
assert len(groups)>=2
for group in groups:assert set(x.strip()for x in group.split(',')if x.strip())<=std
for target in ['D80_327744.final_claim','D81_342290.final_claim']:
    assert target in audittext
    assert re.search(re.escape(target)+r"' depends on axioms: \[[^\]]*\]",audittext)
cpu=s['accounted_CPU_seconds']+time.process_time()-T
assert cpu<=12000
claims=[dict(name='d80_327744',order=327744,max_degree=80,explicit_label='Fin 327744',FinalClaim='DegreeDiameter.Portfolio.EvenQ8SourceFull.D80_327744.FinalClaim',final_claim='DegreeDiameter.Portfolio.EvenQ8SourceFull.D80_327744.final_claim'),dict(name='d81_342290',order=342290,max_degree=81,explicit_label='Fin 342290',FinalClaim='DegreeDiameter.Portfolio.EvenQ8SourceFull.D81_342290.FinalClaim',final_claim='DegreeDiameter.Portfolio.EvenQ8SourceFull.D81_342290.final_claim')]
result=dict(status='BOTH_ORIGINAL_CONCRETE_SOURCE_TARGETS_KERNEL_AUDIT_AND_EXTERNAL_BINDING_PASS',claims=claims,new_modules=len(mods),PASS_module_attempts=len(mods),controlled_cost_reassessment_attempts=sum(a.get('classification')=='CONTROLLED_COST_REASSESSMENT'for a in fail),assembly_elaboration_failures=sum(a.get('classification')=='ASSEMBLY_TACTIC_IMPORT_MISSING'for a in fail),preparation_parse_failures=2,conservative_preparation_parse_CPU_charge=0.2,mathematical_finite_failures=0,new_projection_rows=1095,new_projection_pairs=668680,reused_pilot_projection_pairs=1225,complete_projection_pairs=669905,complete_hline_positions=10385,complete_howner_positions=1097,axioms=sorted(std),Audit_log=audit['log'],CPU_seconds=cpu,CPU_budget_seconds=12000,pilot_separate_CPU_seconds=40.105386447,old_modules_modified_or_recompiled=False,no_user_certificate_premises=True,genuine_Walk_D3_and_not_D2=True,formal_regular_equality_claimed=False,external_table_binding=str(D/'EXTERNAL_TABLE_BINDING.json'),full_literal_graph_receipt=str(D.parent/'independent_acceptance/RESULT.json'),large_graph_files_read_in_formal_batch=0,BFS_in_formal_batch=0,running=False,active_modules=[],public_priority='UNKNOWN',global_record_claimed=False)
result['failed_module_attempts']=len(fail)
result['failed_attempt_classifications']={kind:sum(a.get('classification')==kind for a in fail)for kind in sorted({a.get('classification')for a in fail})}
result['Lean_version']='4.24.0 (existing pinned executable)'
result['final_aggregation_thread_stack_KB']=65536
save(D/'FINAL.json',result)
s.update(status='COMPLETE_KERNEL_AUDIT_AND_EXTERNAL_BINDING_PASS',running=False,active_modules=[],source_targets_complete=True,final_receipt=str(D/'FINAL.json'),accounted_CPU_seconds=cpu)
save(D/'CHECKPOINT.json',s)
handle=json.loads((D/'DRIVER_HANDLE.json').read_text())
handle.update(status=s['status'],running=False,active_modules=[],completed=len(mods),remaining=0,accounted_CPU_seconds=cpu)
save(D/'DRIVER_HANDLE.json',handle)
save(D/'STAGE_STATE.json',dict(status=result['status'],running=False,active_modules=[],completed_new_modules=len(mods),remaining_new_modules=0,source_targets_complete=True,actual_original_targets=[c['name']for c in claims],final_receipt=str(D/'FINAL.json'),CPU_seconds=cpu))
save(D/'CHECKPOINT_B.json',dict(status='ACTUAL_FINITE_TO_GENERIC_TO_TWO_ORIGINAL_TARGETS_CLOSED',Definitions='formal/DegreeDiameter/Portfolio/EvenQ8SourceDefinitions.lean',Inputs=['formal/DegreeDiameter/Portfolio/'+m+'.lean'for m in plan['assembly'][:2]],Exact='formal/DegreeDiameter/Portfolio/EvenQ8SourceFullExact.lean',Audit='formal/EvenQ8SourceFullAudit.lean',claims=claims,all_finite_premises_closed=True,external_binding=str(D/'EXTERNAL_TABLE_BINDING.json')))
save(D/'CHECKPOINT_C.json',dict(status='LOCAL_FINAL_ACTUAL_PASS_EXTERNAL_FRESH_REVIEW_NOT_RUN_BY_THIS_AGENT',claims=claims,Audit_log=audit['log'],FINAL=str(D/'FINAL.json'),new_external_review_calls=0,public_priority='UNKNOWN'))
(D/'PROOF.md').write_text('''# Two concrete q8 source targets closed in Lean

The fixed derived geometry uses Point=Fin512, Line=Fin640, Old=Fin327680,
Helper=Fin64; the balanced geometry uses Fin585, Fin585, Fin342225, Fin65.
Old labels are p*nl+l, helper labels oldn+j, and the explicit sum equivalences
land in Fin327744 and Fin342290. These are the actual fixed source graph types.

All669905 projection point/line pairs now have kernel-checked finite witnesses.
The pilot's1225 last-point pairs are reused and668680 others are proved by the
new row leaves. hline and howner are proved at every10385 and1097 respective
position, including the pilot boundary proofs. Both Inputs assemble all rows.
The previously compiled generic supplies actual SimpleGraph.Walk paths of length
at most3 and a radius-two cardinal obstruction, rather than a Boolean BFS claim.
All its finite premises are discharged in the concrete caller. The original
d80_327744 and d81_342290 FinalClaim/final_claim theorems have no user premises.

Standalone Audit actually imported the final module and printed both original
types, Fin labels, theorem bodies and standard axioms. Formal claims are order,
maximum degree80/81, Walk diameter at most3 and not at most2. The independent
complete literal graph validator establishes full regularity equality; the
current generic Lean theorem only asserts the maximum-degree bound.

The external small-table binding independently decodes the actual Lean literal
LP/PL/spread/owner data and matches the fresh physical incidence order and all
5120+5265 already independently validated ordered helper pins. This is an
external literal-graph correspondence, not a Lean ASCII parser theorem. No large
edge file, old field/geometry, old source proof, or graph BFS was rerun here.

Every attempt and CPU receipt remains in the original12000 CPU ledger. The
explicit controlled cost-reassessment barrier is distinguished from mathematical
finite failures. Successfully compiled rows were preserved, and only uncompiled
witness declarations were repacked without changing their finite equations.

The gains64 and65 are relative to located public source guarantees. Exact
spread-fill priority and global priority remain UNKNOWN. External A/B/C review
and global counts are owned by root; local kernel completion does not assert a
world record.
''')
print(json.dumps(result),flush=True)
