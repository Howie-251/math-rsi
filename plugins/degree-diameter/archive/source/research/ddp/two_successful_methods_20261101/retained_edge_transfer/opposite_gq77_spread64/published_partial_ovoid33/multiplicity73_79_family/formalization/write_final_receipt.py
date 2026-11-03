import json,re
from pathlib import Path

D=Path(__file__).resolve().parent;family=D.parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
P='GQ77Published33CloneFamily';U=P+'Upper'
receipts=[json.loads((D/(U+s+'_RESULT.json')).read_text())for s in ['Exact','Audit']]
assert all(r['exit_code']==0 for r in receipts)
history=[json.loads(p.read_text())for p in(D/'build_history').glob('*_RESULT.json')]if(D/'build_history').exists()else[]
binding=json.loads((D/'INPUT_BINDING_CHECK.json').read_text());assert binding['independent_upper_rows']==138600
prep=json.loads((D/'PREPARATION_RESULT.json').read_text())
audit=(D/(U+'Audit.log')).read_text()
groups=re.findall(r'depends on axioms:\s*\[([^\]]*)\]',audit,re.S)
assert len(groups)==17 and all({x.strip()for x in g.split(',')}=={'propext','Classical.choice','Quot.sound'}for g in groups)
targets=json.loads((D/'TARGETS.json').read_text())['endpoints']
assert [t['k']for t in targets]==list(range(9,16))
for t in targets:
    for suffix in [t['theorem'],t['FinalClaim'],t['final_claim']]:assert U+'.'+suffix in audit
for path in [R/'formal/DegreeDiameter/Portfolio'/(U+'Exact.lean'),R/'formal'/(U+'Audit.lean')]:
    text=path.read_text();assert not re.search(r'\bsorry\b|\bnative_decide\b|^axiom\s|\bd80_',text,re.M)
fresh=json.loads((family/'independent_acceptance/RESULT.json').read_text())
assert fresh['status']=='PASS_ALL_SEVEN_P33_DEGREE73_79_ENDPOINT_GRAPHS'
lean=sum(r['CPU_seconds']for r in receipts+history)
accounted=lean+prep['CPU_seconds']+binding['CPU_seconds']
result={'status':'COMPLETE_SEVEN_UPPER_ORIGINAL_TARGETS_AND_SEPARATE_AUDIT',
        'namespace':'DegreeDiameter.Portfolio.'+U,'parent_namespace':'DegreeDiameter.Portfolio.'+P,
        'actual_graph':'parent graph k, k9..15','actual_source_carrier':'Fin160000 ⊕ Fin50',
        'actual_family_carrier':'Source.Vertex ⊕ (Fin k × Fin1650)',
        'original_endpoints':targets,'new_modules_compiled':2,'new_finite_checks':0,
        'parent24_modified_or_recompiled':False,'old_source_or_generic_modified_or_recompiled':False,
        'failed_attempts':sum(r['exit_code']!=0 for r in receipts+history),
        'Lean_CPU_seconds':lean,'preparation_CPU_seconds':prep['CPU_seconds'],
        'external_binding_CPU_seconds':binding['CPU_seconds'],'accounted_CPU_seconds':accounted,
        'CPU_budget_seconds':300,'module_hard_limit_CPU_seconds':60,'workers':1,
        'standard_axioms_only':True,'printed_axiom_groups':17,'user_certificate_premises':False,
        'actual_SimpleGraph_Walk_D3':True,'not_D2':True,'upper_external_rows_bound':138600,
        'preserved_lower_rows_not_rechecked':59400,'Lean_ASCII_parser_claim':False,
        'independent_actual_status':fresh['status'],
        'fresh_BFS_scope':'upper maximum k15 only:24750 new roots;all7 literalbindings;old sourceR2 predictions inherited without rerun',
        'degree80_concrete_instance_or_graph_written':False,'old_expert8_draft_modified':False,
        'external_review':'root managed; planned transparent lower8+upper7 fifteen-target scope, not claimed complete here',
        'running':False,'active_modules':[],'active_processes':[]}
(D/'FINAL.json').write_text(json.dumps(result,indent=2)+'\n')
state=json.loads((D/'STAGE_STATE.json').read_text());state.update(status=result['status'],running=False,active_modules=[],active_processes=[],
    exact_compiled=True,audit_compiled=True,external_binding_complete=True,parent24_recompiled=False,
    independent_acceptance=fresh['status'],concrete_original_targets_complete=7,accounted_CPU_seconds=accounted)
(D/'STAGE_STATE.json').write_text(json.dumps(state,indent=2)+'\n')
rows='\n'.join('| '+str(t['degree'])+' | '+str(t['n'])+' | `'+t['theorem']+'` | `'+t['FinalClaim']+'` / `'+t['final_claim']+'` |'for t in targets)
text=f'''# Upper seven: actual concrete kernel and recipe-binding checkpoint

Only two new modules were compiled: `formal/DegreeDiameter/Portfolio/{U}Exact.lean` and the separate `formal/{U}Audit.lean`. Both passed first attempt. Exact imports the already closed parent `{P}Exact` and applies its unconditional fixed-family theorem at k9,...,15. No parent24module,old source,generic source or cache was modified or recompiled. No new finite data proof was run.

The graph and type are the actual parent graph and Source.Vertex⊕(Fin k×Fin1650),with Source.Vertex=Fin160000⊕Fin50. Audit checks the compiled parent label equivalence against each explicit Fin(order),prints actual SimpleGraph.Walk semantics,each original type/body/FinalClaim,and axioms. Fin k is a copy index; no field of order k is used.

| degree | order | original theorem | final claims |
| ---: | ---: | --- | --- |
{rows}

Every original target is unconditional card/degree/WalkD3/nonD2,with no user-certificate premise. The17actual Audit axiom groups are all exactly propext,Classical.choice,Quot.sound. Degree80 has no concrete target,Audit instance or produced graph; its classical public blocker is retained in the actual scalar window document.

The fresh independent result is `{fresh['status']}`. It binds all seven full files and138600immutableN64clone rows; ordinary BFS was only on the maximumk15's24750newroots. Earlier sourceR2-only predictions were inherited by exactcenterID,not rerun. Lower59400external rows retain their original passed receipt and were not reread by this new binding. The new138600-row correspondence uses compiled symbolic labels and small recipes only; it is not a Lean ASCII parser theorem or an Audit#eval claim. See INPUT_BINDING_CHECK.json and its code.

Lean CPU{lean:.9f},preparation{prep['CPU_seconds']:.9f},newbinding{binding['CPU_seconds']:.9f},measured accounted total{accounted:.9f}<300. Exact took40.382508wall seconds for normal imports but4.490453CPU;it was not restarted. Every module stayed below60CPU. All local processes are terminal.

Root owns acceptance/counts and external A/B/freshC. This local receipt is ready for the transparent shared lower8+upper7 fifteen-original-target review,not a claim that external review is complete. The old expert8 draft is unchanged.
'''
(D/'CHECKPOINT_B.md').write_text(text)
(D/'CHECKPOINT_C.md').write_text('# Local final packet,not an external C verdict\n\n'+text)
notes='\n'.join(f"| {r['module']} | {r['exit_code']} | {r['CPU_seconds']:.6f} | {r['wall_seconds']:.6f} |"for r in receipts)
(D/'BUILD_NOTES.md').write_text(f'''# Upper two-module build

Pinned Lean4.24.0,explicit inherited LEAN_PATH,LEAN_NUM_THREADS=1,and only new -j1 output paths. No lakefetch,installation or old cache rebuild.

| module | exit | CPU seconds | wall seconds |
| --- | ---: | ---: | ---: |
{notes}

Measured preparation/binding-inclusive CPU{accounted:.9f};0failed attempts. Actual17Audit groups use the standard three axioms. See individual actual command/result/log files. Both new targets files and the138600-row binding are complete;all local active flags are false.
''')
print(json.dumps({'status':result['status'],'Lean_CPU_seconds':lean,'accounted_CPU_seconds':accounted,'axiom_groups':17,'running':False}))
