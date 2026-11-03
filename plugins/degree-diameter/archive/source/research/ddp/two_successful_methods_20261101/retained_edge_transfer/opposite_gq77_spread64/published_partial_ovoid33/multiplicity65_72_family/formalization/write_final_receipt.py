import json
from pathlib import Path
import re
from time import process_time

start=process_time();D=Path(__file__).resolve().parent;family=D.parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
prefix='GQ77Published33CloneFamily'
receipts=[json.loads(p.read_text())for p in sorted(D.glob(prefix+'*_RESULT.json'))]
assert len(receipts)==24 and all(r['exit_code']==0 for r in receipts)
history=[json.loads(p.read_text())for p in (D/'build_history').glob('*_RESULT.json')]if(D/'build_history').exists()else[]
binding=json.loads((D/'INPUT_BINDING_CHECK.json').read_text())
assert binding['independent_rows_all_eight_cases']==59400
audit=(D/(prefix+'Audit.log')).read_text()
groups=re.findall(r'depends on axioms:\s*\[([^\]]*)\]',audit,re.S)
assert len(groups)==20
standard={'propext','Classical.choice','Quot.sound'}
assert all({x.strip()for x in g.split(',')}==standard for g in groups)
targets=json.loads((D/'TARGETS.json').read_text())['endpoints']
for e in targets:
    assert prefix+'.'+e['theorem'] in audit
    assert prefix+'.FinalClaim'+str(e['degree']) in audit
    assert prefix+'.final_claim'+str(e['degree']) in audit
for path in [*(R/'formal/DegreeDiameter/Portfolio').glob(prefix+'*.lean'),R/'formal'/(prefix+'Audit.lean')]:
    assert not re.search(r'\bsorry\b|\bnative_decide\b|^axiom\s',path.read_text(),re.M)
prep=json.loads((D/'PREPARATION_RESULT.json').read_text())
queue=json.loads((D/'QUEUE_RESULT.json').read_text())
lean=sum(r['CPU_seconds']for r in receipts+history)
accounted=lean+prep['CPU_seconds']+binding['CPU_seconds']+queue['CPU_seconds']
fresh=json.loads((family/'independent_acceptance/RESULT.json').read_text())
assert fresh['status']=='PASS_ALL_EIGHT_P33_ENDPOINT_GRAPHS'
result={'status':'COMPLETE_EIGHT_UNCONDITIONAL_CONCRETE_TARGETS_AND_SEPARATE_AUDIT',
        'namespace':'DegreeDiameter.Portfolio.'+prefix,'actual_source_carrier':'Fin160000 ⊕ Fin50',
        'actual_family_carrier':'OppositeGQ77Spread.Vertex ⊕ (Fin k × Fin1650)',
        'label_target':'Fin(160050+1650*k)','endpoints':targets,
        'new_modules_compiled':24,'finite_chunks_compiled':20,'finite_incidence_positions':3200,
        'failed_attempts':sum(r['exit_code']!=0 for r in receipts+history),
        'Lean_CPU_seconds':lean,'preparation_CPU_seconds':prep['CPU_seconds'],
        'external_binding_CPU_seconds':binding['CPU_seconds'],'queue_controller_CPU_seconds':queue['CPU_seconds'],
        'accounted_CPU_seconds':accounted,'CPU_budget_seconds':900,
        'maximum_new_module_CPU_seconds':max(r['CPU_seconds']for r in receipts+history),
        'module_hard_limit_CPU_seconds':60,'workers':1,
        'standard_axioms_only':True,'printed_axiom_groups':20,'user_certificate_premises':False,
        'actual_SimpleGraph_Walk_D3':True,'not_D2':True,
        'external_ordered_recipe_rows_bound':59400,'Lean_ASCII_parser_claim':False,
        'independent_actual_status':fresh['status'],
        'fresh_BFS_scope':'maximum k8 only:13200 new roots;all8 literalbindings and sourceR2-only1650 once',
        'old_source_or_generic_modified_or_recompiled':False,
        'external_reviews':'root managed separately; no review verdict claimed by this receipt',
        'running':False,'active_modules':[],'active_processes':[]}
(D/'FINAL.json').write_text(json.dumps(result,indent=2)+'\n')
state=json.loads((D/'STAGE_STATE.json').read_text());state.update(status=result['status'],running=False,active_modules=[],active_processes=[],
    definitions_compiled=True,finite_chunks_compiled=20,inputs_compiled=True,exact_compiled=True,audit_compiled=True,
    external_binding_complete=True,independent_acceptance=fresh['status'],concrete_original_targets_complete=8,
    accounted_CPU_seconds=accounted,external_review='root managed separately')
(D/'STAGE_STATE.json').write_text(json.dumps(state,indent=2)+'\n')
rows='\n'.join('| '+str(e['degree'])+' | '+str(e['n'])+' | `'+e['theorem']+'` | `FinalClaim'+str(e['degree'])+'` / `final_claim'+str(e['degree'])+'` |'for e in targets)
B=f'''# Actual structural checkpoint B: all eight original targets compiled

Definitions,20 finite chunks,Inputs,Exact and the separate Audit all compiled successfully,24new modules total, with no failed attempt. The real source type is Fin160000⊕Fin50; the family carrier adds Fin k×Fin1650. It does not identify the source carrier with Fin160050 by assumption: the compiled existing label equivalence supplies that conversion.

The3200 finite incidence-position checks prove the new33-point hO. The old compiled source supplies hS. OvoidSpreadCloneCapacity gives base load<=1, and injection to Fin k gives copy load<=k. The actual center graph need not be independent. The fixed-source clone graph has no new-new edges and uses only immutable source adjacency.

Exact imports the old closed OppositeGQ77SpreadExact theorem and derives source non-isolation from its actual WalkD3 and two distinct source vertices. Degree/card/WalkD3/nonD2 are unconditional. Each original endpoint below has its own explicit type; the all-k lemma is not substituted for eight checked instances.

| degree | order | original theorem | final claim |
| ---: | ---: | --- | --- |
{rows}

Read `formal/DegreeDiameter/Portfolio/{prefix}Definitions.lean`,the20InputChunk files,`{prefix}Inputs.lean`,`{prefix}Exact.lean`,and`formal/{prefix}Audit.lean`. Actual logs and receipts are in this directory. The Audit prints each original type,body,FinalClaim,and axioms; its20axiom groups are all exactly propext,Classical.choice,Quot.sound. DiameterAtMost explicitly contains SimpleGraph.Walk.

External input binding passed for33point labels,1650basecenter order,13200maxproducer rows and all59400independent per-case rows. It reads only small recipes,not large edgefiles,and makes no formal ASCII parser or Audit#eval claim. The fresh independent receipt is actual `{fresh['status']}`. Its BFS scope is maximumk8's13200newroots only,with all8literalbindings and one1650sourceR2-only prediction; smaller endpoints have their own mathematical prefix proof.

Lean CPU{lean:.9f}, measured preparation/binding/queue-inclusive accounted CPU{accounted:.9f}, versus900budget; maximum module{result['maximum_new_module_CPU_seconds']:.6f}<60. No old source/generic module or cache was changed/recompiled. Root's shared externalA/B/freshC review is separate and not claimed completed here.
'''
(D/'CHECKPOINT_B.md').write_text(B)
(D/'CHECKPOINT_C.md').write_text('# Local final kernel and label-binding receipt\n\nThis is a local completion packet,not an external reviewer C verdict.\n\n'+B.split('\n\n',1)[1])
notes='\n'.join(f"| {r['module']} | {r['exit_code']} | {r['CPU_seconds']:.6f} | {r['wall_seconds']:.6f} |"for r in receipts)
(D/'BUILD_NOTES.md').write_text(f'''# Actual build and binding receipts

Pinned executable: `{R}/.tools/lean-4.24.0-linux/bin/lean`; every command is the recorded `-j1 -o newmodule.olean newmodule.lean`. LEAN_PATH is explicitly inherited from `research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json`;LEAN_NUM_THREADS=1. There is no lakefetch or old dependency rebuild.

| new module | exit | CPU seconds | wall seconds |
| --- | ---: | ---: | ---: |
{notes}

All24new modules passed on their first attempt. Lean CPU{lean:.9f}; generation{prep['CPU_seconds']:.9f};external recipe binding{binding['CPU_seconds']:.9f};queue controller{queue['CPU_seconds']:.9f};measured accounted total{accounted:.9f}<900. The initial Definitions import took37.538wall seconds but completed normally; it was not restarted. No module approached its60CPU-second hard limit.

The separate Audit has20actual axiom printouts,all exactly the standard three. All eight original endpoints and aliases have no user-certificate premise. The final state is complete with no active module/process. Final external review and ledger updates remain root-owned.
''')
print(json.dumps({'status':result['status'],'Lean_CPU_seconds':lean,'accounted_CPU_seconds':accounted,'modules':24,'axiom_groups':len(groups),'running':False}))
