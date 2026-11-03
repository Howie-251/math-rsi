import json,re,time
from pathlib import Path
started=time.process_time()
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
P=R/'formal/DegreeDiameter/Portfolio'
state=json.loads((D/'CHECKPOINT.json').read_text())
assert not state['running'] and len(state['completed'])==4
assert len(state['attempts'])==5 and sum(a['PASS'] for a in state['attempts'])==4
assert all(a['CPU_seconds']<=a['CPU_limit_seconds']+1 for a in state['attempts'])
binding=json.loads((D/'EXTERNAL_BINDING_RESULT.json').read_text())
assert binding['status'].startswith('PASS_')
audit=(D/'F3Graph15552Clone16416Audit_attempt001.log').read_text()
axioms=re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]",audit,re.S)
assert len(axioms)==11
allowed={'propext','Classical.choice','Quot.sound'}
for name,body in axioms:assert set(re.split(r',\s*',body.strip()))<=allowed
for mod in state['completed']:
    p=R/'formal'/(mod+'.lean') if mod.endswith('Audit') else P/(mod+'.lean')
    assert not re.search(r'\bsorry\b|\bnative_decide\b|^\s*axiom\s',p.read_text(),re.M)
prep=dict(status='FINAL_RECEIPTS_WRITTEN',CPU_seconds=time.process_time()-started,
    final_receipt_write_reserve_CPU_seconds=0.05)
prep['CPU_seconds']+=prep['final_receipt_write_reserve_CPU_seconds']
(D/'FINALIZATION_PREPARATION_RESULT.json').write_text(json.dumps(prep,indent=2)+'\n')
total=state['CPU_seconds']+binding['CPU_seconds']+prep['CPU_seconds']+0.02
state.update(status='COMPLETE_CONCRETE_D16_16416_KERNEL_AUDIT_AND_EXTERNAL_BINDING',running=False,
    active_modules=[],remaining_requested_modules=[],CPU_seconds=total,
    external_binding_CPU_seconds=binding['CPU_seconds'],finalization_CPU_seconds=prep['CPU_seconds'])
(D/'CHECKPOINT.json').write_text(json.dumps(state,indent=2)+'\n')
handle=json.loads((D/'DRIVER_HANDLE.json').read_text())
handle.update(status=state['status'],running=False,active_modules=[],CPU_seconds=total)
(D/'DRIVER_HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
env=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text())
(D/'FORMAL_ENV_USED.json').write_text(json.dumps(dict(lean_binary=str(R/'.tools/lean-4.24.0-linux/bin/lean'),
    Lean_version='4.24.0',LEAN_PATH=env['LEAN_PATH'],LEAN_NUM_THREADS='1',compile_flags=['-j1','-s65536'],
    old_modules_import_only=True,old_cache_modified=False),indent=2)+'\n')
result=dict(status=state['status'],target='DegreeDiameter.Portfolio.F3Graph15552.Clone16416.d16_16416',
    final_claim='DegreeDiameter.Portfolio.F3Graph15552.Clone16416.final_claim',
    original_concrete_goal='DegreeDiameter.Portfolio.F3Graph15552.Clone16416.original_concrete_goal',
    explicit_FinalClaim_no_user_premises=True,source_type='Fin 15552',carrier='Fin 15552 ⊕ Fin 864',
    label_equivalence='Clone16416.label : Vertex ≃ Fin 16416',card=16416,maxdegree_bound=16,
    actual_SimpleGraph_Walk_bound=4,not_DiameterAtMost=3,
    fresh_graph_n=16416,fresh_graph_m=129240,fresh_independent_ordinary_final_BFS_roots=16416,
    fresh_independent_receipt='../independent_acceptance/RESULT.json',
    new_positive_controller_owner_equations=160,new_fullN_role_bindings=864,new_pin_bindings=12924,
    no_user_JSON_certificates_assumed=True,axioms=sorted(allowed),Audit_types_body_axioms_actual_PASS=True,
    source_public_reproduction_new_results=0,new_concrete_target_count=1,
    new_PASS_modules=state['completed'],attempt_count=len(state['attempts']),failed_attempt_count=1,
    failed_attempt_preserved='F3Graph15552Clone16416Definitions_attempt001.json',
    failure_scope='A new optional expanded-label theorem needed Vec simplification before rewrite; corrected only this unpassed new module.',
    CPU_seconds=total,CPU_budget_seconds=200,per_module_hard_CPU_limit_seconds=60,
    compiler_worker_count=1,all_processes_terminal=True,active_processes=0,
    graph_BFS_runs_in_this_Lean_batch=0,old_field_rank_geometry_rechecks=0,old_PASS_Lean_recompiles=0,
    source_reuse='Already closed literal F3Graph15552.graph; only its symbolic/source and table binding are inherited.',
    old16389_graph_PASS_not_used_as_new_graph_evidence=True,
    external_binding='EXTERNAL_BINDING_RESULT.json',ASCII_parser_theorem=False,Audit_evaluates864_external_rows=False,
    remote_reviews='Root coordinates new-scope A/B/distinct-fresh-C; no new target external verdict is asserted here.',
    global_priority='UNKNOWN',root_counts_changed=False)
for name in ['RESULT.json','FINAL.json']:(D/name).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
(D/'TERMINAL.json').write_text(json.dumps(dict(status=state['status'],running=False,all_processes_terminal=True,
    CPU_seconds=total,CPU_budget_seconds=200,original_claim_complete=True,external_binding_complete=True,
    all_attempts_retained=True,no_automatic_continuation=True),indent=2)+'\n')
(D/'CHECKPOINT_A.md').write_text('''# Actual new-target encoding checkpoint\n\nF3Graph15552Clone16416Definitions compiled successfully in attempt2. Actual carrier Fin15552 ⊕ Fin864, label Fin16416, layerI32 exact SELECTED_BLOCKS order, center j uses oldlabel81*I32[j/27]+j%3+9*(j/3%3)+27*(j/9%3), newlabel15552+j. Old-center virtualself deletion remains the inherited actual source SimpleGraph adjacency. Inputs checks only160 positive new controller-owner equations and imports the old symbolic recover_plane. This checkpoint records actual encoding; complete-target receipt is FINAL.json.\n''')
(D/'CHECKPOINT_B.md').write_text('''# Actual source-to-original-target bridge\n\nNew Inputs proves pinOwner_forward and load_le_one for the new864 centers without any field/rank or negative-pair enumeration. Exact imports the already closed literal source FullExact once and uses FullNeighborhoodClones.degree_le/diameterAtMost/not_diameterAtMost. d16_16416 and original_concrete_goal have no user premises. Walks are genuine SimpleGraph.Walk; old_walk_bound_iff also preserves nonD3. Source reproduction contributes no new result. Standalone Audit has separately imported Exact and printed target types, bodies and axioms. External small-table binding matches all864 labels and12924 pins to the actual independently parsed graph; it is not a Lean ASCII parser theorem.\n''')
(D/'CHECKPOINT_C.md').write_text('''# Local final kernel and binding checkpoint\n\nAll four new modules and standalone Audit actually exit0. d16_16416, final_claim, original_concrete_goal, degree/D4/nonD3/load/labels expose only propext, Classical.choice, Quot.sound (some labels use fewer). The failed first Definitions attempt and its log remain in the cumulative ledger. All old source/rank/coset/field modules were import-only. No BFS or large graph read occurred in this Lean batch. Root has the separate fresh all16416-root graph acceptance. New external review A/B/C results are not asserted by this local checkpoint. See FINAL.json for actual CPU and files.\n''')
(D/'NOTE.md').write_text(f'''# Concrete16416 kernel closure\n\nThe actual I32 whole-plane clone graph is closed in namespace DegreeDiameter.Portfolio.F3Graph15552.Clone16416. The carrier and label target are explicit, the old source is unchanged, and the new centers are bound to the ordered actual864-role table. Source holding moves and deletion of virtual self are inherited from the already proved literal source, while generic full-neighborhood cloning supplies the genuine Walk bound and retraction-based nonD3.\n\nThe new proof checks160 positive controller-owner equalities, then reuses the symbolic plane inverse to prove common-pin uniqueness and load≤1. It does not enumerate15552×864 pairs or reprove old ranks/cosets. Actual original target, FinalClaim/final_claim and standalone Audit are all unconditional and use only the standard three axioms.\n\nThe first new Definitions compile failed in an expanded-label simp/rewrite proof (2.347902CPU); only that unpassed module was fixed. Four new modules now PASS. All failures, preparation and external small-table binding remain charged: {total:.9f}/200CPU seconds. No old PASS recompiles, BFS, large graph reads, field/rank checks, solver, install, hashes or review calls occurred.\n\nIndependent graph acceptance is separate and actual: all16416 final roots,864 full neighborhoods and12924 pins were independently bound. Our external binding checks the ordered recipe and labels against those actual tables and the producer table; no Lean ASCII parser theorem or Audit evaluation of external rows is claimed. Source15552 is a published reproduction (zero added source result). Root owns final counts and the new external A/B/freshC scopes; global priority remains UNKNOWN.\n''')
print(json.dumps({'status':result['status'],'CPU_seconds':total,'new_PASS_modules':4,'attempts':5}))
