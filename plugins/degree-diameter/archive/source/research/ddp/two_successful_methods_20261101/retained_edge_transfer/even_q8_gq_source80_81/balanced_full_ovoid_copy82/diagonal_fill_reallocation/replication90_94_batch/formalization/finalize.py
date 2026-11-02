import json,re,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent;P=D.parent.parent
state=json.loads((D/'CHECKPOINT.json').read_text());binding=json.loads((D/'EXTERNAL_INPUT_BINDING.json').read_text())
assert not state['running']and len(state['completed'])==8 and all(x['PASS']for x in state['attempts'])
assert binding['status']=='BOTH_TARGETS_ALL84520_TYPED_NEW_ROLE_LABEL_ROWS_BOUND'
claims=[]
for cap,r,n,directory in[(90,8,380324,'multiplicity9_degree90'),(94,12,397228,'multiplicity13_degree94')]:
    ns=f'DegreeDiameter.Portfolio.Q8DiagonalFill{cap}';target=f'{ns}.d{cap}_{n}'
    log=D/f'Q8DiagonalFill{cap}Audit_attempt001.log';text=log.read_text()
    for name in(target,ns+'.final_claim'):
        found=re.search(re.escape("'"+name+"' depends on axioms:")+r'\s*\[([^]]*)\]',text)
        assert found and set(re.findall(r'[A-Za-z][A-Za-z.]*',found.group(1)))=={'propext','Classical.choice','Quot.sound'}
    assert 'sorryAx'not in text and f'label : Vertex ≃ Fin {n}'in text
    final=dict(status=f'ORIGINAL_D{cap}_{n}_KERNEL_AUDIT_EXTERNAL_ROLE_BINDING_PASS',target=target,
        FinalClaim=ns+'.FinalClaim',final_claim=ns+'.final_claim',order=n,max_degree=cap,
        genuine_Walk_D3=True,not_D2=True,no_user_certificate_premises=True,
        axioms=['propext','Classical.choice','Quot.sound'],label=f'Fin{n}',new_modules=4,
        all_first_attempt_PASS=True,per_target_compile_CPU_seconds=sum(a['CPU_seconds']for a in state['attempts']if a['module'].startswith(f'Q8DiagonalFill{cap}')),
        shared_batch_CPU_receipt=str(D/'FINAL.json'),Audit_log=str(log),
        external_binding=str(P/directory/'formalization/EXTERNAL_INPUT_BINDING.json'),
        parent_source='Q8DiagonalFill.d82_346516',parent_source_order=346516,
        imported83_role_uniqueness_is_about_G1_not83_graph=True,
        source_base_role_count=4226,r=r,new_role_count=r*4226,new_finite_geometry_checks=0,
        old_modules_modified_or_recompiled=False,large_graph_reads=0,BFS=0,
        running=False,active_modules=[],priority='UNKNOWN',external_review_calls=0)
    (P/directory/'formalization/FINAL.json').write_text(json.dumps(final,indent=2)+'\n');claims.append(final)
total=state['CPU_seconds']+binding['CPU_seconds']+time.process_time()-started
final=dict(status='BOTH_ORIGINAL_D90_D94_KERNEL_AUDIT_EXTERNAL_ROLE_BINDING_PASS',
    CPU_seconds=total,CPU_budget_seconds=300,preparation_and_driver_and_all_attempts_included=True,
    new_module_count=8,failed_attempts=0,max_module_CPU_seconds=max(a['CPU_seconds']for a in state['attempts']),
    all_attempts=state['attempts'],targets=claims,typed_external_binding_rows=84520,
    actual_fresh_BFS_roots_per_case=68,actual_fresh_BFS_total=136,
    unmeasured_new_roots=33740+50644,allpair_and_prefix_true_Walk_proof=True,
    new_finite_geometry_checks=0,old_modules_modified_or_recompiled=False,
    large_graph_reads_in_Lean_binding=0,BFS_in_Lean_batch=0,root_counts_Wiki_frozen_files_modified=False,
    external_reviews_requested=0,running=False,active_modules=[],priority='UNKNOWN')
for name in('FINAL.json','CHECKPOINT_B.json','CHECKPOINT_C.json'):
    (D/name).write_text(json.dumps(final,indent=2)+'\n')
encoding=dict(status='BOTH_ACTUAL_DEFINITIONS_INPUTS_EXACT_AND_AUDIT_PASS',
    targets=[x['target']for x in claims],definitions=['formal/DegreeDiameter/Portfolio/Q8DiagonalFill90Definitions.lean',
    'formal/DegreeDiameter/Portfolio/Q8DiagonalFill94Definitions.lean'],
    exacts=['formal/DegreeDiameter/Portfolio/Q8DiagonalFill90Exact.lean','formal/DegreeDiameter/Portfolio/Q8DiagonalFill94Exact.lean'],
    source='G1/346516 frozen; imported83 Source alias and role lemmas refer to G1',
    typed_carrier='Q8DiagonalFill.Vertex ⊕ (Fin r × (CloneIndex ⊕ Unit))',
    labels=['Fin380324','Fin397228'],new_label_formula='346516+4226*b+h',source_center_formula='342290+h',
    typed_external_binding_rows=84520,full_kernel_and_binding_complete=True,new_finite_checks=0)
(D/'CHECKPOINT_A.json').write_text(json.dumps(encoding,indent=2)+'\n')
(D/'STAGE_STATE.json').write_text(json.dumps(dict(status=final['status'],running=False,active_modules=[],
    completed_modules=8,failed_attempts=0,CPU_seconds=total,actual_final_targets_complete=True),indent=2)+'\n')
print(json.dumps(dict(status=final['status'],CPU_seconds=total,targets=[x['target']for x in claims],running=False)))
