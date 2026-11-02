from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';F=S+'retained_edge_transfer/diagonal_fill_reallocation_formalization/'
B='Q4_REALLOCATION_CONCRETE_LEAN38_Q8_DEFS_COST_REPAIR_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,37)
ids=['ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101','ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101'];rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
f=json.loads((R/F/'Q4_FINAL.json').read_text());binding=json.loads((R/F/'Q4_EXTERNAL_INPUT_BINDING.json').read_text());a1=json.loads((R/F/'Q8DiagonalFillDefinitions_attempt001.json').read_text());a2=json.loads((R/F/'Q8DiagonalFillDefinitions_attempt002.json').read_text())
assert f['status'] in ['ORIGINAL_Q4_D26_7532_KERNEL_AUDIT_AND_EXTERNAL_LABEL_BINDING_PASS','ORIGINAL_TARGET_KERNEL_AUDIT_AND_EXTERNAL_LABEL_BINDING_PASS'] and f['target']=='DegreeDiameter.Portfolio.Q4DiagonalFill.d26_7532' and f['order']==7532 and f['no_user_certificate_premises'] and set(f['axioms'])=={'propext','Classical.choice','Quot.sound'}
assert binding['status']=='PASS_ACTUAL_TYPED_CENTER_ORDER_NEW_LABELS_HUB_AND_COVER_PAYLOAD_BINDING';assert a1['exit_code']==-9 and a2['exit_code']==0
shared=f.get('shared_batch_CPU_snapshot',f.get('shared_batch_CPU_seconds'))
formal=dict(status=f['status'],target=f['target'],FinalClaim=f['FinalClaim'],final_claim=f['final_claim'],explicit_label='Fin7532',
    genuine_Walk_D3=True,not_D2=True,no_user_certificate_premises=True,axioms=f['axioms'],case_modules=4,shared_generic_modules=5,
    case_module_CPU_seconds=f['case_module_CPU_seconds'],shared_batch_CPU_snapshot=shared,shared_batch_CPU_is_not_case_exclusive=True,
    external_binding=dict(status=binding['status'],CPU=binding['CPU_seconds'],clone_rows=289,diagonal_rows=17,cover_slots=85,label='7242+17*i+j',hub=7531,large_graph_reads=0),
    literal_ascii_parser_or_exact_regular_histogram_in_Lean_claimed=False,old_modules_recompiled=False,old_field_projection_BFS_reruns=0,
    FINAL=F+'Q4_FINAL.json',Audit=F+'Q4DiagonalFillAudit_attempt001.log',binding=F+'Q4_EXTERNAL_INPUT_BINDING.json')
repair=dict(status='Q8_NEW_DEFINITIONS_COST_LIMIT_TARGETED_INTERFACE_REPAIR_ACTUAL_PASS_NOT_ORIGINAL_TARGET_COMPLETION',
    failed_attempt_exit=-9,failed_attempt_CPU=a1['CPU_seconds'],successful_attempt_exit=0,successful_attempt_CPU=a2['CPU_seconds'],
    classification='NEW_MODULE_SINGLE_CPU_LIMIT_INTERFACE_REPAIR_NOT_MATHEMATICAL_COUNTEREXAMPLE',same_original600CPU_budget_retained=True,
    old_modules_recompiled=False,old_field_projection_BFS_reruns=0,new_Q8_concrete_Lean_count=0,
    attempts=[F+'Q8DiagonalFillDefinitions_attempt001.json',F+'Q8DiagonalFillDefinitions_attempt002.json'])
for r in rows:
    m=r['other_metrics'];m['diagonal_reallocation_two_targets_pending_proof_and_review'].update(concrete_Lean='Q4_ORIGINAL_COMPLETE_Q8_ORIGINAL_NOT_YET_ACCEPTED',completed_original_targets=1,Q4_concrete_complete=True,Q8_concrete_complete=False)
    m['new_q4_concrete_kernel_completion']=copy.deepcopy(formal);m['new_q8_definitions_cost_repair']=copy.deepcopy(repair)
    r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+[F+'Q4_FINAL.json',F+'Q4_EXTERNAL_INPUT_BINDING.json',F+'Q4DiagonalFillAudit_attempt001.log',F+'Q8DiagonalFillDefinitions_attempt001.json',F+'Q8DiagonalFillDefinitions_attempt002.json']))
    r['lesson_and_restart_condition']+=' 新q4/7532具体原目标d26_7532/FinalClaim/final_claim/Fin7532与独立Audit/std3/no用户前提和实际label绑定全部闭合，case4module14.510148CPU，共享batch108.234539769CPU快照不可当case独占或另行相加。Q8新Definitions首试60.365404CPU触单module限后接口成本修复，第二试实际PASS3.587344CPU，原600预算继续保留；只更新真实修复，不把DefsPASS当346516原目标closed。Lean现38，83仍待parent闭合后的另150CPU；外审A历史formalPENDING不自动变PASS，B/freshC未派，冻结包不动。'
q4=rows[0];m=q4['other_metrics'];g=next(g for g in m['validated_graph_instances']if g['n']==7532)
g.update(complete_Lean_graph_instance=True,complete_concrete_Lean_status='ORIGINAL_TARGET_KERNEL_AUDIT_EXTERNAL_LABEL_BINDING_ACTUAL_PASS',concrete_original_target=f['target'],formal_final_receipt=F+'Q4_FINAL.json',formal_standard_axioms=f['axioms'],formal_user_certificate_premises=False,formal_case_module_CPU=f['case_module_CPU_seconds'])
m['all_row_graph_instances_complete_Lean']=True;m['new_Lean_instances']=2
m['diagonal_fill_reallocation_prediction'].update(concrete_Lean_status='ORIGINAL_TARGET_KERNEL_AUDIT_EXTERNAL_LABEL_BINDING_ACTUAL_PASS',new_concrete_Lean=1)
m['diagonal_fill_reallocation_prediction']['new_review_status']['concrete_Lean']='Q4_ORIGINAL_COMPLETE;ACTUAL_A_FORMAL_VERDICT_REMAINS_HISTORICAL_PENDING'
q4['title']='GQ(4,4)7531与新7532两具体Lean闭合；7532数学A通过，B及freshC待'
q4['outcome_class']='OLD7531_COMPLETE_NEW7532_MATH_AND_CONCRETE_KERNEL_AUDIT_PASS_NEW_B_C_PENDING'
q4['distance_text']+=' 新7532具体Lean原目标、Fin7532标签和独立Audit/std3/no证书前提已实际PASS，case4module14.510148CPU；外部289center/17diag/85coverSlots绑定.023981154CPU，0大图读取，不冒LeanASCIIparser或exacthist。总Lean38；A仍为实际当时mathbindingPASS/formalPENDING历史判定，B/freshC未派。'
q4['unclosed_gap']+=' 最新7532具体kernel/Audit/labelbinding已完成；剩该新图后续B和distinctfreshC及公开priority，不撤旧历史。'
extra=['formal/DegreeDiameter/Portfolio/Q4DiagonalFillDefinitions.lean','formal/DegreeDiameter/Portfolio/Q4DiagonalFillInputs.lean','formal/DegreeDiameter/Portfolio/Q4DiagonalFillExact.lean','formal/DegreeDiameter/Portfolio/Q8DiagonalFillDefinitions.lean']
q4['evidence_paths']=list(dict.fromkeys(q4['evidence_paths']+extra));assert all((R/x).is_file()for x in extra)
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,38)
block=f'''<!-- {B} -->
# 当前：q4/7532具体Lean及独立Audit/绑定已闭合，总Lean38；q8Definitions成本修复PASS

同Goal ACTIVE，ledger420复用2现节点，146合法／37参数、stage42／34不变；具体Lean38，0新数学图。[7532节点](experiments/{ids[0]}.md)实际原目标/FinalClaim/final_claim/Fin7532、真WalkD3/nonD2/std3/no用户前提与独立Audit/289row绑定全PASS。case4module14.510148CPU；共享108.234539769CPU是batch快照，非case独占，不重复加总。

[q8现节点](experiments/{ids[1]}.md)只记录新Definitions首试60.365404CPU触单module限，targeted接口修复第二试实际PASS3.587344CPU；原600CPU预算保留，旧source/field/projection不重跑。该修复不等于346516原目标完成，83另150CPU仍依赖parent；不提前计Lean40。A历史mathbindingPASS/formalPENDING不自动改判，B/freshC未派；旧冻结包不动。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} q4具体原目标及Audit闭合，Lean38；q8新Definitions成本修复保留原预算

复用[7531/7532节点](experiments/{ids[0]}.md)及[q8现节点](experiments/{ids[1]}.md)，ledger420/0新行，数学图146／37、stage42／34不变，只有具体Lean37→38。已实际读Q4_FINAL/独立Audit/外部binding：d26_7532及FinalClaim/final_claim真WalkD3/nonD2、degree≤26、card7532、显式Fin7532label全闭合，std3/no用户证书前提。四case新module14.510148CPU，5generic共享模块另属原600batch；108.234539769CPU仅共享时刻快照，不与case重复相加。外部289clone/17diag/85coverSlots/7242+17i+j和hub7531绑定PASS，.023981154CPU，0大图/旧field/projection/BFS重读，不冒LeanASCIIparser/exactdegreehist。

Q8新Definitions首试exit−9/60.365404CPU属于singlemodule成本接口问题；原600预算保留，未当数学反例或Goal暂停。第二试actualexit0/3.587344CPU已记录，两attempt原日志保留，旧成功module不重编。只记这次真实修复；346516原目标/Audit尚未root接受时不计，83也仍需parentclosed后另150CPU/每module60/单worker。A559已实际mathbindingPASS，其当时formalNOT_REVIEWED/PENDING历史不因本地kernel后来完成而自动升级；B/freshC未派，无付费重call。旧三q8冻结包保持原143/36/37scope，根状态与恢复文件未改。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'ActualQ4original7532kernelFinalClaim_finalclaim_Fin7532_genuineWalkD3_nonD2_std3_noUserPremise_independentAudit_external289labelsPASS;case4module14.510148CPU/sharedbatch108.234539769snapshotnotadditive/binding.023981154CPU. Lean38onlyQ4new;146_37stage42_34unchanged. Q8Definitionssingle60.365404CPUlimitretainedoriginal600budget/targetedrepairsecondPASS3.587344CPU/notoriginaltargetcompletion/83separate150afterparent. Aformalhistorypending_notautomaticPASS/BfreshCnotdispatched. Ledger420twoexistingrows/0mathBFSfieldLeanreruns/rootedits/frozenpackchanges.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_Q4_CONCRETE_LEAN38_AND_Q8_DEFINITIONS_ACTUAL_COST_REPAIR_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=146,legal_parameter_pairs=37,stage_graphs=42,stage_pairs=34,complete_formula_Lean=38,new_graphs=0,new_Lean=1,new_frameworks=0,
    Q4_original_FINAL=f['status'],Q4_case_CPU=f['case_module_CPU_seconds'],shared_batch_CPU_snapshot=shared,shared_CPU_not_additive=True,Q4_external_binding_CPU=binding['CPU_seconds'],
    Q8_new_definitions_first_limit_CPU=a1['CPU_seconds'],Q8_new_definitions_repair_PASS_CPU=a2['CPU_seconds'],original600CPU_budget_retained=True,Q8_original_closed_counted=False,degree83_original_closed_counted=False,
    external_A_formal_verdict_not_automatically_changed=True,actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
