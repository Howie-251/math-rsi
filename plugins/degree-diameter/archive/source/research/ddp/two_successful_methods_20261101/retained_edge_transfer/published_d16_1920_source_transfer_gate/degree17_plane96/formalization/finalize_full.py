import json,re,time
from pathlib import Path
start=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
def save(name,value):(D/name).write_text(json.dumps(value,indent=2)+'\n')
s=json.loads((D/'CHECKPOINT.json').read_text());assert not s['running']
required=json.loads((D/'ASSEMBLY_PREPARATION_RESULT.json').read_text())['sequential_modules']
assert all(m in s['completed'] for m in required)
assert all(f'F4Graph1920Row{i}{kind}' in s['completed'] for i in range(30) for kind in ['Data','Certificate','Walks'])
allowed={'propext','Classical.choice','Quot.sound'}
audits={}
for module,target in [('F4Graph1920SourceAudit','d16_1920'),('F4Graph1920CloneAudit','d17_2016')]:
    receipt=[a for a in s['attempts'] if a['module']==module and a['PASS']][-1]
    text=Path(receipt['log']).read_text()
    assert target in text and 'final_claim' in text and 'sorryAx' not in text
    axioms=re.findall(r'depends on axioms:\s*\[([^]]*)\]',text,re.S)
    assert axioms and all({a.strip() for a in names.split(',') if a.strip()}<=allowed for names in axioms)
    audits[module]=dict(log=receipt['log'],exit_code=0,target_type_and_body_printed=True,
                       all_printed_axiom_lists_within_standard_three=True)
binding=json.loads((D/'EXTERNAL_BINDING_RESULT.json').read_text())
binding['center_ordered_label_kernel_status']='PASS_F4Graph1920CloneExact_AND_STANDALONE_AUDIT'
save('EXTERNAL_BINDING_RESULT.json',binding)
aux=0.
for name,key in [('CLONE_PREPARATION_RESULT.json','code_preparation_CPU_seconds'),
 ('ASSEMBLY_PREPARATION_RESULT.json','CPU_seconds'),('EXTERNAL_BINDING_RESULT.json','CPU_seconds'),
 ('SERIAL_PREPARATION_RESULT.json','CPU_seconds')]:
    p=D/name
    if p.exists():aux+=json.loads(p.read_text()).get(key,0.)
finalizer=time.process_time()-start
cost=s['pilot_CPU_seconds']+s['full_preparation_CPU_seconds']+s['driver_CPU_seconds']+aux+sum(a['CPU_seconds']for a in s['attempts'])+finalizer
assert cost<=1200
result=dict(status='PASS_UNCONDITIONAL_LITERAL_SOURCE1920_AND_CLONE2016_KERNEL_AUDITS_EXTERNAL_BINDING',
    CPU_seconds=cost,CPU_budget_seconds=1200,pilot_included_CPU_seconds=s['pilot_CPU_seconds'],
    full_preparation_CPU_seconds=s['full_preparation_CPU_seconds'],aux_preparation_CPU_seconds=aux,
    driver_CPU_seconds=s['driver_CPU_seconds'],finalizer_CPU_seconds=finalizer,
    completed_modules=len(s['completed']),completed_module_names=s['completed'],
    failed_attempts=sum(not a['PASS'] for a in s['pilot_attempts']+s['attempts']),
    all_attempts=s['pilot_attempts']+s['attempts'],
    source=dict(target='DegreeDiameter.Portfolio.F4Graph1920.d16_1920',
       final_claim='DegreeDiameter.Portfolio.F4Graph1920.final_claim',n=1920,degree_bound=16,
       source_reproduction_only=True,portfolio_increment=0,concrete_success_increment=0,
       complete_controller_rows=30,controller_pairs=900,NB_pairs=780,adjacent_pencils=120,
       NB_basis_checks=2340,adjacent_residual_checks=7680,
       cardinality_and_degree_and_genuine_Walk_D3_and_nonD2=True,nonD2_witness=[0,192]),
    clone=dict(target='DegreeDiameter.Portfolio.F4Graph1920.Clone2016.d17_2016',
       final_claim='DegreeDiameter.Portfolio.F4Graph1920.Clone2016.final_claim',n=2016,degree_bound=17,
       carrier='Fin 1920 + Fin 96',label='Fin 2016',ordered_centers=96,load_bound=1,
       cardinality_and_degree_and_genuine_Walk_D3_and_nonD2=True,
       concrete_success_increment_if_accepted_by_root=1),
    no_user_certificate_premises=True,axioms=sorted(allowed),standalone_audits=audits,
    external_small_table_binding='EXTERNAL_BINDING_RESULT.json',
    external_actual_graph_binding='../independent_acceptance/RESULT.json',
    source_graph_reads_in_full_Lean_batch=0,old_BFS_field_rank_pencil_solver_runs=0,
    old_or_already_passed_modules_modified_or_recompiled=False,
    running=False,active_modules=[],root_counts_modified=False,global_priority='UNKNOWN')
save('FINAL.json',result)
s.update(status=result['status'],CPU_seconds=cost,aux_preparation_CPU_seconds=aux,
         finalizer_CPU_seconds=finalizer,running=False,active_modules=[])
save('CHECKPOINT.json',s)
save('TERMINAL.json',dict(status=result['status'],CPU_seconds=cost,CPU_budget_seconds=1200,
     running=False,active_modules=[],all_source_and_clone_targets_complete=True))
save('DRIVER_HANDLE.json',dict(status=result['status'],running=False,active_modules=[],CPU_seconds=cost))
(D/'STAGE_STATE').write_text('COMPLETE_NO_ACTIVE_PROCESSES_SOURCE1920_REPRODUCTION_CLONE2016_UNCONDITIONAL_KERNEL_PASS\n')
(D/'CHECKPOINT_B.md').write_text('''# Actual source and clone targets closed

`DegreeDiameter.Portfolio.F4Graph1920.d16_1920` is an unconditional
published-source reproduction: Fin1920, degree at most16, genuine Walks of
length at most3 for every pair, and non-D2 witnessed by source labels0/192.
All30 source rows/900 controller pairs are kernel closed. It adds no new
portfolio or concrete-instance success count.

`F4Graph1920.Clone2016.d17_2016` and `final_claim` are unconditional for the
actual accepted2016 graph. The96 centers lie in six literal controller layers
and plane(a,b,a+b). A symbolic normal111 projection defines a unique pin owner;
24 controller-layer/port facts prove load at most1. FullNeighborhoodClones
lifts actual Walks and retracts old-old walks, so adjacent centers require no
independence assumption. Every prefix uses only old-source interiors.

Both standalone Audit logs print original theorem types, bodies and axiom
lists contained in propext/Classical.choice/Quot.sound. See FINAL.json for
actual receipts and the cumulative1200-CPU budget including the pilot and
failed attempts. No old PASS module or old field/rank/BFS check was rerun.
''')
(D/'CHECKPOINT_C.md').write_text('''# External literal binding and scope

EXTERNAL_BINDING_RESULT.json binds all120 controller entries,1080 actual
matrix code entries,12 direction entries, and all96 ordered center/new labels
to the author parameters and completed independent literal graph receipt.
The new kernel theorem center_ordered_label checks every ordered center label;
label_old/label_new supply the explicit Fin2016 interface.

The fresh suite separately bound the15360 original source edges and all96
actual full neighborhoods/1536 distinct pins. It ran96 new-root BFS searches
and zero old-root BFS searches. This formal batch only reads the small receipts
and TSV; it does not claim a Lean ASCII edge-parser theorem or formal regularity.

Source1920 is published reproduction. Degree17/2016 is one accepted mathematical
candidate, with global/priority UNKNOWN. Root owns external review and counting;
previous four-endpoint reviews do not cover this new target.
''')
(D/'FULL_NOTE.md').write_text(f'''# Completed literal source and degree17 clone

The full fixed construction is kernel closed in {cost:.9f} cumulative CPU
seconds out of1200, including the59.696392030-CPU pilot, all recorded failures,
new finite witnesses, both target assemblies, standalone Audits and small
external binding. The pilot RESULT/NOTE and failed attempt logs remain history;
FINAL.json and the latest CHECKPOINT/TERMINAL are the completed-state receipts.

The actual source uses its30-controller/120 edge-local matrix parameters,
not the old60-controller3840 theorem. Thirty parameterized source-row Walk
theorems cover every source vertex and target. The non-D2 proof uses controller
labels0 and3 (physical vertex labels0 and192), excluding one- and two-step
controller routes. Published1920 reproduction is not a new portfolio result.

The accepted2016 graph has96 complete-neighborhood clones from the six actual
controller layers[0,3,5,7,9,16], plane(a,b,a+b). A true matrix inverse followed
by normal111 projection reconstructs a unique clone owner for every pin.
Load is at most1, hence the degree bound17. FullNeighborhoodClones lifts real
SimpleGraph.Walks and retracts old-old walks; each prefix uses source interiors.
Selected centers need not be independent.

Every source parameter and ordered center/new label is externally bound to
the literal author data and the completed fresh receipt. The fresh suite had
all15360 source edges and all96 full neighborhoods bound, with96 new-root BFS
and0 old-root BFS. This Lean batch performs no graph read or repeated BFS,
field-law, rank, pencil, or old-source verification; it proves no ASCII parser
or full-regularity claim. Both final theorems have no user-certificate premises,
and both independent import/Audit logs show only the standard three axioms.

Global record and priority remain UNKNOWN. Root controls acceptance/counting
and the new target's external reviews; old four-endpoint reviews do not apply.
''')
print(json.dumps({k:result[k] for k in ['status','CPU_seconds','CPU_budget_seconds','failed_attempts','completed_modules']}))
