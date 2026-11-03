"""Update only the existing eight-instance family from the actual local final receipt."""
from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[2];W=ROOT/'research-wiki'
STEM='P33_EIGHT_KERNEL_LEAN27_A_B_IN_FLIGHT_20261101'
ID='ddp-gq77-published-p33-immutable-fulln64-clone-eight-degree65-72-family-20261101'
S='research/ddp/two_successful_methods_20261101/'
F=S+'retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/formalization/'
read=lambda p:json.loads((ROOT/p).read_text())
state=read(S+'STAGE_STATE.json');assert state['complete_concrete_formula_Lean_instances']==27
final=read(F+'FINAL.json');binding=read(F+'INPUT_BINDING_CHECK.json')
assert final['status']=='COMPLETE_EIGHT_UNCONDITIONAL_CONCRETE_TARGETS_AND_SEPARATE_AUDIT'
assert final['new_modules_compiled']==24 and final['failed_attempts']==0
assert final['finite_incidence_positions']==3200 and final['actual_source_carrier']=='Fin160000 ⊕ Fin50'
assert binding['status']=='PASS_EXTERNAL_BINDING_COMPILED_LABELS_TO_FRESH_ORDERED_RECIPES'
assert binding['independent_rows_all_eight_cases']==59400
l=read('research-wiki/DDP_METHOD_LEDGER.json')
row=copy.deepcopy(next(r for r in l['rows'] if r['id']==ID)['source_record'])
row['title']='P33同一family八完整图65..72：fresh独验／八无前提具体Lean及独立Audit完成；新A/B在途'
row['outcome_class']='EIGHT_COMPLETE_LITERAL_GRAPHS_FRESH_ACCEPTED_EIGHT_UNCONDITIONAL_CONCRETE_LEAN_AUDIT_COMPLETE_A_B_IN_FLIGHT_C_NOT_REQUESTED'
row['unclosed_gap']='八完整数学图及八个无前提具体Lean原目标／独立Audit均actualPASS，24新模块首编0失败、std3、真实SimpleGraph.WalkD3/nonD2、59400逐case recipe绑定完成。新scope外审仅共享A423 encoding与B428新thread独立bridge各一次在途，distinctfresh最终C尚未派；本地CHECKPOINT_C只是kernel/label completion packet，不是外部C。全球最高／优先权未认证，旧冻结包不含本family。'
row['distance_text']+=' 八个原具体声明d65_161700至d72_173250和各final_claim、独立Audit现实际全PASS，无certificate前提/std3；24新模块、20有限chunks合3200incidence positions（不是把528Gram pair称Lean检查），总95.041500998CPU。实际源carrierFin160000⊕Fin50，标签等价接Fin160050；59400外部逐j绑定靠已编译label/center定理＋独立小recipe readback，不是Audit#eval59400或LeanASCIIparser。旧source/generic未改未重编。'
row['lesson_and_restart_condition']='公开33复现和filled-source N64规则已实际产生并验收八端点，现各具体原目标／独立Audit和标签绑定均闭合；数学合法总133/26、具体Lean由19增27。一family八实例仍非八方法。当前只收新scope A/B并待其返回后distinctfresh最终C，不自动73+、不重跑图/BFS/Lean，不把本地Cpacket冒外部C。'
m=row['other_metrics'];m.update(new_Lean_instances=8,concrete_Lean_complete=True,formal_final_binding_acceptance_pending=False,
    formal_stage_status=final['status'],formal_current_modules=24,formal_finite_chunks_compiled=20,
    formal_finite_incidence_positions=3200,formal_Gram528_pairs_claimed_as_kernel_checks=False,
    formal_source_carrier=final['actual_source_carrier'],formal_family_carrier=final['actual_family_carrier'],
    formal_CPU_seconds=final['accounted_CPU_seconds'],formal_Lean_CPU_seconds=final['Lean_CPU_seconds'],
    formal_failed_attempts=0,formal_user_certificate_premises=False,formal_standard_axioms=['propext','Classical.choice','Quot.sound'],
    formal_actual_SimpleGraph_Walk_D3=True,formal_not_D2=True,formal_actual_original_targets_complete=8,
    formal_external_ordered_recipe_rows_bound=59400,formal_Lean_ASCII_parser_claim=False,formal_Audit_eval59400_claim=False,
    formal_old_source_or_generic_modified_or_recompiled=False,formal_all_local_processes_terminal=True,
    formal_final_receipt=F+'FINAL.json',local_checkpoint_C_is_external_review=False,
    external_review_A='IN_FLIGHT_ENCODING_CHECKPOINT_ONLY',external_review_A_cell='423',
    external_review_B='IN_FLIGHT_NEW_THREAD_INDEPENDENT_ORIGINAL_BRIDGE_REVIEW',external_review_B_cell='428',
    external_review_distinctfreshC='NOT_YET_REQUESTED',external_all_A_B_freshC_complete=False)
targets={e['degree']:e for e in final['endpoints']}
for g in m['validated_graph_instances']:
    e=targets[g['Delta']];assert e['n']==g['n']
    g.update(complete_Lean_graph_instance=True,formal_status='COMPLETE_UNCONDITIONAL_ORIGINAL_CONCRETE_TARGET_AND_SEPARATE_AUDIT_STD3',
        concrete_original_theorem=final['namespace']+'.'+e['theorem'],final_claim=final['namespace']+f'.final_claim{e["degree"]}',
        formal_scope='Actual fixed deterministic graph/card/maxdegree/true SimpleGraph.WalkD3/nonD2, no user certificate premises; separate original type/body/axiom Audit std3. Exact mixed degree/ASCII binding external; all59400 ordered rows bound to compiled labels.',
        external_A='encoding423inflight',external_B='newthread_bridge428inflight',external_distinctfreshC='notrequested')
extra=[F+n for n in ['FINAL.json','INPUT_BINDING_CHECK.json','CHECKPOINT_B.md','CHECKPOINT_C.md','GQ77Published33CloneFamilyAudit.log']]
extra+=['formal/DegreeDiameter/Portfolio/'+n+'.lean' for n in ['GQ77Published33CloneFamilyDefinitions','GQ77Published33CloneFamilyInputs','GQ77Published33CloneFamilyExact']]
extra+=['formal/GQ77Published33CloneFamilyAudit.lean']
row['evidence_paths']=list(dict.fromkeys(row['evidence_paths']+extra))
assert all((ROOT/p).exists() for p in row['evidence_paths'])
raw=W/'updates'/f'{STEM}_ROWS.json';raw.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
cmd=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(raw)]
r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);assert r.returncode==0,(r.stdout,r.stderr)
sync=json.loads(r.stdout)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
intro=f'''<!-- {STEM} -->
# 当前：P33八具体Lean原目标与独立Audit完成，133例／26参数／Lean27

同Goal ACTIVE：133合法图／26参数、阶段29图／23参数，ledger416不新增行，具体Lean27=19+8。knownpublicdominated43（旧65/70仍合法）、savedoverlap40、outsidepending27/22、全球认证0。

[P33同family八图](experiments/{ID}.md)65..72各+50，八无前提具体原目标及独立Audit实际全PASS。24新模块首编0fail，20chunks核3200incidence positions，非528Gram pair；实际sourcecarrierFin160000⊕Fin50，std3／真实WalkD3/nonD2。总95.041501CPU，59400逐case绑定完成；非Audit#eval59400／LeanASCIIparser，旧source/generic无重编。

完整图独验范围保持：59400完整N64行、1650sourceR2only一次，仅k8实际13200新根BFS，七小图各自binding＋old-only prefix证明。新共享A423 encoding与B428 fresh独立bridge各一次在途，最终distinctfreshC未派；本地CHECKPOINT_C不是外部C，旧six-target最终C保持完成。旧冻结包不改，root另写公开比较勘误；不自动73+，先收本批外审。以下保留历史。

'''
gap=W/'gap_map.md';t=gap.read_text()
if not t.startswith(f'<!-- {STEM} -->'):gap.write_text(intro+t)
h=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if f'<!-- {STEM} -->' not in h.read_text():
    with h.open('a') as f:f.write(f'''\n\n<!-- {STEM} -->
## 2026-11-01 P33八原目标及独立Audit完成：Lean27，外审A/B在途

root已实际核8originalExact源码、Inputs、Audit逐type/body/std3、59400输入绑定及真实[FINAL.json](../{F}FINAL.json)，正式计具体Lean19+8=27；合法133/26、stage29/23、ledger416不变。只复用[同一family节点](experiments/{ID}.md)，不新增方法或图。24新模块首次编译0fail，含准备/绑定95.041500998CPU。20finitechunks证明3200incidence positions给hO，528Gram pair仅外部坐标检验，不混作kernel枚举。source实际carrier是Fin160000⊕Fin50，经既有label等价，不假设直接等于Fin160050；旧source/generic无改写/重编。

各d65_161700至d72_173250及各final_claim/独立Audit actualPASS，无用户证书前提、std3、真实SimpleGraph.WalkD3/非D2；59400外部recipe行依已编译label/center定理及逐行小表readback绑定，不是Audit#eval59400或LeanASCIIparser。原独验59400绑定/最大端点13200BFS/其余七端点各自prefix证明均保留不重跑。

新scope仅共享Gemini A423 encoding及B428新thread独立bridge各发一次在途，distinctfresh最终C待两者实际返回后由root派；本地CHECKPOINT_C是localfinalpacket，不能冒外部finalC。旧six-target C仍完整。knownpublicdominated43/savedoverlap40/outsidepending27/22/global0不变；旧冻结包不改，不派新数学查询或extraaudits，不自动73+。
''')
helper=ROOT/'aris_repo/tools/research_wiki.py';calls=[]
for args in [('log',str(W),'2026-11-01 existingP33onefamilyeightoriginalconcreteLeanandseparateAuditactualPASS+59400binding;24newmoduleszeroFailures95.041500998CPU,3200incpositionsnot528Gramkernel,sourceFin160000plusFin50. ledger416unchanged/133legal26pairsstage29_23Lean27;newA423andB428inflightfreshCnotrequested/localCpacketnotexternal. 0newgraphorresearchrerun,publicdominated43overlap40pending27_22global0,frozenpackunchanged.'),('rebuild_index',str(W)),('rebuild_query_pack',str(W))]:
    c=[sys.executable,str(helper),*args];x=subprocess.run(c,cwd=ROOT,text=True,capture_output=True)
    calls.append(dict(command=c,returncode=x.returncode,stdout=x.stdout,stderr=x.stderr));assert x.returncode==0,calls[-1]
cp=W/'updates'/f'{STEM}_HELPER_CALLS.json';cp.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
ledger=read('research-wiki/DDP_METHOD_LEDGER.json')
expect={'record_count':416,'validated_named_graph_examples':133,'validated_named_parameter_pairs':26,'complete_Lean_graph_instances':27,'known_publicly_dominated_graph_examples':43,'known_publicly_dominated_also_saved_table_improvement_examples':40,'pending_outside_saved_table_graph_examples':27,'pending_outside_saved_table_parameter_pairs':22}
for k,v in expect.items():assert ledger[k]==v,(k,ledger[k],v)
checked=0;p=W/'experiments'/f'{ID}.md'
for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
    target=unquote(target.strip('<>').split('#',1)[0])
    if not target or re.match(r'\w+://',target):continue
    assert (p.parent/target).exists(),target;checked+=1
q=(W/'query_pack.md').read_text();assert 'Lean27' in q and 'ledger416' in q and 'B428' in q
receipt=dict(updated_UTC=now,status='PASS_EXISTING_P33_FAMILY_EIGHT_CONCRETE_KERNEL_AUDIT_LEAN27_SYNC',ledger_records=416,records_added=0,records_updated=1,named_legal_graphs=133,legal_parameter_pairs=26,stage_graphs=29,stage_pairs=23,complete_formula_Lean=27,concrete_Lean_instances_newly_counted=8,new_graphs=0,new_frameworks=0,known_publicly_dominated=43,saved_table_dominated_overlap=40,pending_outside_saved_table_graphs=27,pending_outside_saved_table_pairs=22,certified_global_records=0,actual_final_receipt=F+'FINAL.json',new_modules=24,failed_attempts=0,finite_incidence_positions=3200,external_binding_rows=59400,formal_accounted_CPU_seconds=95.04150099799998,external_A='423encodinginflight',external_B='428newthreadbridgeinflight',external_freshC='notrequested',local_C_is_external_review=False,canonical_upsert_command=cmd,canonical_upsert_stdout=sync,actual_helper_calls=str(cp.relative_to(ROOT)),resolved_evidence_paths=len(row['evidence_paths']),checked_local_markdown_links=checked,query_current=True,experiments_rerun=0,root_owned_files_modified=False,frozen_expert_packets_modified=False)
rp=W/'updates'/f'{STEM}_RECEIPT.json';rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
