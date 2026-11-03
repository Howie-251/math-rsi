import json,re,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
P=R/'formal/DegreeDiameter/Portfolio';case=D.parent;gate=case.parent
s=json.loads((D/'CHECKPOINT.json').read_text());assert not s['running']
required=['F3Graph15552FullRows','F3Graph15552FullDegree','F3Graph15552FullLower','F3Graph15552FullExact','F3Graph15552FullAudit','F3Graph15552FullCloneInputs','F3Graph15552FullCloneExact','F3Graph15552FullCloneAudit']
for m in required:
    assert m in s['completed'],m
    assert next(a for a in reversed(s['attempts']) if a['module']==m)['PASS'],m
logs={m:Path(next(a for a in reversed(s['attempts']) if a['module']==m)['log']) for m in required if m.endswith('Audit')}
allowed={'propext','Classical.choice','Quot.sound'}
for m,p in logs.items():
    txt=p.read_text()
    blocks=re.findall(r"depends on axioms:\s*\[([^\]]*)\]",txt,re.S)
    assert blocks,m
    for b in blocks:assert {x.strip() for x in b.split(',')}<=allowed,(m,b)
    assert 'sorryAx' not in txt and 'error:' not in txt,m
    target='d16_16389' if 'Clone' in m else 'd15_15552'
    assert target in txt and 'final_claim' in txt
oldbind=json.loads((case/'formalization/EXTERNAL_BINDING_PREPARATION_RESULT.json').read_text())
assert oldbind['status']=='PASS_NEW_TYPED_SOURCE_LITERAL_AND837_ORDERED_RECIPE_SMALL_BINDING'
fresh=json.loads((case/'independent_acceptance/RESULT.json').read_text())
assert fresh['status']=='PASS_COMPLETE_LITERAL_AND_ALL16389_FINAL_ROOTS_EXACT_D4'
assert fresh['ordered_fullN_roles_bound']==837 and fresh['all_source_edges_retained_exact']==116316
assert fresh['new_edges']==12519 and fresh['maximum_old_pin_load']==1 and fresh['all_virtualself_entries_excluded_at_oldcenter']
# Inherit the completed small typed-source/label binding and independent literal
# neighborhood receipt.  Neither operation parses a large edge file again.
binding=dict(status='PASS_INHERITED_TYPED_SOURCE_LABELS_AND_FRESH837_LITERAL_NEIGHBORHOODS',
    inherited_typed_source_and837_recipe=str((case/'formalization/EXTERNAL_BINDING_PREPARATION_RESULT.json').relative_to(R)),
    inherited_independent_literal_receipt=str((case/'independent_acceptance/RESULT.json').relative_to(R)),
    inherited_actual837_role_table=str((case/'independent_acceptance/ALL837_ACTUAL_ROLE_BINDINGS.tsv').relative_to(R)),
    source_type='Fin 15552',clone_type='Fin 15552 ⊕ Fin 837',explicit_label_target='Fin 16389',
    source_label='81*a+x0+3*x1+9*x2+27*x3',new_label='15552+j',
    center_label='81*I[j//27]+j%3+9*(j//3%3)+27*(j//9%3)',
    source_controller_entries=960,source_matrix_entries=80,source_direction_entries=20,source_constant_entries=20,
    ordered_clones=837,full_N_pins=12519,physical_old_edges_retained=116316,
    old_virtualself_removed_before_freezing_N=True,
    kernel_load='Clone16389.pinOwner_forward/common_pin_index_unique/load_le_one',
    kernel_label_theorems=['Clone16389.label_old','Clone16389.label_new'],
    finite_route_coefficients='all actual coefficient equations checked by kernel; correctness does not assume JSON certificates',
    large_graph_reads=0,BFS=0,old_field_rank_rechecks=0,old_Lean_recompiles=0,
    ASCII_parser_theorem=False,Audit_evaluates837_external_rows=False,
    source_and_label_binding_reexecuted=False)
(D/'EXTERNAL_BINDING_RESULT.json').write_text(json.dumps(binding,indent=2)+'\n')
# The fixed source identity is imported from the original passed Definitions;
# these exact target files introduce no extra finite-data premises.
source=(P/'F3Graph15552FullExact.lean').read_text();clone=(P/'F3Graph15552FullCloneExact.lean').read_text()
assert 'theorem d15_15552 :' in source and 'theorem final_claim : FinalClaim := d15_15552' in source
assert 'theorem d16_16389 :' in clone and 'theorem final_claim : FinalClaim := d16_16389' in clone
note='''# Complete kernel receipts for published15552 source and new16389 target

Actual final status: both original target theorems and the two separate import Audits passed. All final axioms are among `propext`, `Classical.choice`, `Quot.sound`; there is no user-certificate premise. Source15552 is a published-object reproduction and does not add a portfolio result. Only clone16389 is the new concrete Lean instance, subject to root acceptance.

The source is exactly Fin15552, with old label 81*a+local4vector and the inherited five affine types/960 controller arcs. A completed affine holding step contracts to nil only when the entire global vertex is equal; other steps use a real SimpleGraph edge. Coefficient certificates feed the symbolic coset solution and actual Walk construction. 173 shared rank-four certificates were imported from the passed pilot. All91 used coset groups (2260 column-vector and7371 cover-vector identities in total) are now closed. Eight representative controller rows have1536 endpoint bindings; two generator commutation/positive coverage proofs transport their Walks to all192 layers. No parent graph BFS or old field/rank/module computation was repeated.

The source degree<=15 proof turns every undirected neighbor into one of15 forward labels, using a symbolic true reverse. The nonD3 witness is old0 to81: a125-entry controller triple-type obstruction covers all shorter words by initial type0 holding. It is independent of the accepted external BFS.

The clone is Fin15552 ⊕ Fin837 with an explicit equivalence to Fin16389. Its centre order is the fixed31 layers,27 points of x1=0 per layer. A155-entry positive owner table plus the symbolic inverse-type recovery map proves pinOwner(forward(center j))=j and hence load<=1; it assumes no independence of centres. FullNeighborhoodClones supplies degree<=16, genuine Walk diameter<=4, and preservation of the source nonD3 witness. The original d16_16389 and final_claim have no assumptions.

The existing pilot small-table/837-label binding and actual independent literal full-N receipt are inherited. EXTERNAL_BINDING_RESULT.json records their paths and exact scope. It is not a Lean ASCII-parser theorem and the Audit does not evaluate837 external rows. The previously accepted final graph BFS is not repeated. Failed attempts remain in the cumulative ledger, including two clone elaboration repairs; their failed elaborator placeholders do not occur in successful target dependencies.

GLOBAL_COSET4 and NEW_ROUTE4 historical scope remains unchanged: the single full-rank route hypothesis was refuted; unions of certified route cosets complete the proof. No new graph, parameter, source search, installation, hash, or remote review was initiated here. Public-table +5 and global/priority UNKNOWN are unchanged. Root owns review and count updates.
'''
(D/'NOTE.md').write_text(note)
(D/'CHECKPOINT_B.md').write_text('''# Actual complete source/clone bridge packet

Both source and clone original targets and independent Audits are kernel PASS. Read the following final code in order (repo-relative):

- formal/DegreeDiameter/Portfolio/F3Graph15552Definitions.lean (passed original pilot; imported only)
- formal/DegreeDiameter/Portfolio/F3Graph15552Linear.lean and F3Graph15552Routes.lean (passed pilot: symbolic coset solve and holding-to-Walk)
- formal/DegreeDiameter/Portfolio/F3Graph15552FullPackages.lean, FullRowData.lean, FullEndpointRow0..7.lean (shared certificates to1536 endpoints)
- formal/DegreeDiameter/Portfolio/F3Graph15552FullSymmetry.lean and FullRows.lean (all192 layers)
- formal/DegreeDiameter/Portfolio/F3Graph15552FullDegree.lean, FullLower.lean, FullExact.lean
- formal/DegreeDiameter/Portfolio/F3Graph15552FullCloneInputs.lean and FullCloneExact.lean
- formal/F3Graph15552FullAudit.lean and formal/F3Graph15552FullCloneAudit.lean

The actual log/attempt paths are in FINAL.json and CHECKPOINT.json. EXTERNAL_BINDING_RESULT.json describes inherited physical-label/N receipts. No external reviewer verdict is asserted by this local packet.
''')
(D/'CHECKPOINT_C.md').write_text('''# Actual final original targets ready for root review

1. DegreeDiameter.Portfolio.F3Graph15552.d15_15552 / final_claim: Fin15552, degree<=15, genuineWalk D4 and nonD3; published reproduction.
2. DegreeDiameter.Portfolio.F3Graph15552.Clone16389.d16_16389 / final_claim: Fin15552 ⊕ Fin837 ≃ Fin16389, degree<=16, genuineWalk D4 and nonD3; no user premises.

Both separate import/type/body/axioms Audits actually exited0 and report only the three standard axioms. Read FINAL.json, NOTE.md, EXTERNAL_BINDING_RESULT.json and the two actual Audit logs. The local packet does not claim a remote A/B/C verdict, a parser theorem, global record or certified priority.
''')
prep={'CPU_seconds':time.process_time()-started,'scope':'final successful audit log receipt and inherited small external binding; no new Lean/BFS/large graph read'}
(D/'FINALIZATION_PREPARATION_RESULT.json').write_text(json.dumps(prep,indent=2)+'\n')
# Cost includes the original pilot once, all new attempts (failed and successful),
# driver CPU and every recorded new preparation.  Do not reset the ledger.
newprep=sum(json.loads(p.read_text()).get('CPU_seconds',json.loads(p.read_text()).get('code_preparation_CPU_seconds',0.))for p in D.glob('*PREPARATION_RESULT.json'))
cpu=s['base_pilot_CPU_seconds']+newprep+s['driver_CPU_seconds']+sum(a['CPU_seconds'] for a in s['attempts'])
status='PASS_COMPLETE_SOURCE15552_AND_CLONE16389_ORIGINAL_TARGETS_AUDITS_AND_INHERITED_BINDING'
final=dict(status=status,running=False,CPU_seconds=cpu,CPU_budget_seconds=1200,per_module_CPU_limit_seconds=60,
    base_pilot_CPU_seconds=s['base_pilot_CPU_seconds'],new_preparation_CPU_seconds=newprep,
    new_compilation_CPU_seconds=sum(a['CPU_seconds']for a in s['attempts']),new_driver_CPU_seconds=s['driver_CPU_seconds'],
    new_successful_modules=len(s['completed']),pilot_successful_modules=len(s['pilot_completed']),
    all_attempts=len(s['attempts']),failed_new_attempts=sum(not a['PASS']for a in s['attempts']),
    pilot_failed_attempts=3,completed_modules=s['completed'],
    source_original_target='DegreeDiameter.Portfolio.F3Graph15552.d15_15552',
    clone_original_target='DegreeDiameter.Portfolio.F3Graph15552.Clone16389.d16_16389',
    source_final_claim='DegreeDiameter.Portfolio.F3Graph15552.final_claim',
    clone_final_claim='DegreeDiameter.Portfolio.F3Graph15552.Clone16389.final_claim',
    source_full_claim_complete=True,clone_full_claim_complete=True,user_certificate_premises=0,
    audit_logs={m:str(p.relative_to(R))for m,p in logs.items()},axioms=sorted(allowed),
    external_binding=str((D/'EXTERNAL_BINDING_RESULT.json').relative_to(R)),
    shared_fullrank_words_imported=173,all_complete_coset_groups=91,
    representative_controller_rows=8,representative_endpoint_pairs=1536,source_layers=192,
    controller_symmetry_generators=2,actual_genuine_walks=True,
    old_modules_recompiled=0,large_graph_reads=0,BFS=0,new_field_or_rank_enumerations=0,
    source_reproduction_count_increment=0,potential_clone_Lean_increment_only_after_root_acceptance=1,
    remote_review_verdict_claimed=False,global_priority_certified=False)
for name in ['FINAL.json','RESULT.json']:(D/name).write_text(json.dumps(final,indent=2)+'\n')
s.update(status=status,CPU_seconds=cpu,preparation_CPU_seconds=newprep,running=False,active_modules=[],source_full_claim_complete=True,clone_full_claim_complete=True)
(D/'CHECKPOINT.json').write_text(json.dumps(s,indent=2)+'\n')
(D/'DRIVER_HANDLE.json').write_text(json.dumps(dict(driver_pid=None,last_driver_pid=json.loads((D/'DRIVER_HANDLE.json').read_text())['driver_pid'],status=status,running=False,CPU_seconds=cpu,active_modules=[]),indent=2)+'\n')
(D/'TERMINAL.json').write_text(json.dumps(dict(status=status,running=False,CPU_seconds=cpu,CPU_budget_seconds=1200,source_full_claim_complete=True,clone_full_claim_complete=True,active_modules=[]),indent=2)+'\n')
print(json.dumps({k:final[k]for k in ['status','CPU_seconds','new_successful_modules','pilot_successful_modules','all_attempts','failed_new_attempts','source_full_claim_complete','clone_full_claim_complete']}))
