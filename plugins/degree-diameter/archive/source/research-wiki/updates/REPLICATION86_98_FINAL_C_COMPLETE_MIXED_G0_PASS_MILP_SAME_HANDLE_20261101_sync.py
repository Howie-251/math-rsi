from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';V=S+'reviews/';C=V+'REPLICATION86_98_FINAL_C_';E='expert_review_current/REPLICATION86_98_TWO_RESULTS_20261101';D=S+'retained_edge_transfer/mixed_copy_cycle_sigma_31/'
B='REPLICATION86_98_FINAL_C_COMPLETE_MIXED_G0_PASS_MILP_SAME_HANDLE_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,148,39,42)
ids=['ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101','ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101'];rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
c=json.loads((R/(C+'GEMINI_RAW.json')).read_text())['structuredContent'];assert c['status']=='SUCCESS' and c['threadId']=='ce6eb098-dcb5-4864-b0bd-c5a87b05647c'
assert c['threadId']not in ['e4b6c102-1c55-4739-82e4-d281acc2e835','5da20cd4-ab3f-4327-9df5-8d0e80d7eee3']
ts=next(json.loads(x)['targets']for x in re.findall(r'```json\s*([\s\S]*?)```',c['content'])if 'targets'in json.loads(x));assert {(x['Delta'],x['D'],x['n'],x['m'])for x in ts}=={(86,3,363420,15573870),(98,3,414132,19680570)}
assert all(all(x[k]=='PASS'for k in ['math','formal','binding'])and x['priority']=='UNKNOWN'for x in ts)
draft=json.loads((R/(E+'_DRAFT_RECEIPT.json')).read_text());assert draft['status']=='UNFROZEN_TWO_TARGET_EXPERT_DRAFT_C_ROOT_DISPOSED' and draft['C_complete_render_requested'] and not draft['delivery_ZIP_created']
base=json.loads((R/D/'RESULT.json').read_text());bt=json.loads((R/D/'TERMINAL.json').read_text());cube=json.loads((R/D/'NEW_B_CUBE_CHECK.json').read_text());handle=json.loads((R/D/'MILP_HANDLE.json').read_text());model=json.loads((R/D/'MODEL.json').read_text())
assert base['status']=='FIXED_G0_PRODUCER_PASS_READY_FOR_ROOT_EXACT_JOINT_MODEL' and (base['n'],base['m'],base['pool_size'],base['freed_U_vertices'])==(10070,154390,1750,130)
assert cube['status']=='PASS' and cube['ordered_entries_checked']==342225 and cube['mismatch_count']==0
assert model['rows']==62181 and model['variables']==10500 and model['nonzeros']==7349320 and model['all_old_targets_included']
finalC=dict(status='ACTUAL_SUCCESS_TWO_EXACT_ORIGINAL_MATH_FORMAL_BINDING_PASS_DISTINCT_FRESH',cell=672,thread=c['threadId'],actual_shared_calls=1,
    A_thread='e4b6c102-1c55-4739-82e4-d281acc2e835',B_thread='5da20cd4-ab3f-4327-9df5-8d0e80d7eee3',distinct_from_actual_A_B=True,targets=ts,priority='UNKNOWN',old_case_PASS_inherited=False,
    small_helper_or_mixed_G0_scope_included=False,new_validation_runs=0,raw=C+'GEMINI_RAW.json',disposition=C+'DISPOSITION.md')
q8=rows[0];m=q8['other_metrics'];m['replication86_98_actual_batch']['distinctfreshC']=finalC;m['all_row_original_A_B_distinctfreshC_complete']=True
m['completed_Lean_and_A_B_C_scope']='all7actualq8roworiginalsmath_kernel_A_B_distinctfreshCcomplete;smallhelperandmixedexperimentexcluded'
for g in m['validated_graph_instances']:
    if g['n']in [363420,414132]:g.update(external_fresh_C='ACTUAL_SUCCESS_NEW_SCOPE_MATH_FORMAL_BINDING_PASS',external_final_C_thread=c['threadId'],external_final_C_distinct_from_actual_A_B=True,external_B_C_complete=True,new_case_reviews_complete=True,priority='UNKNOWN')
m['replication86_98_two_expert_DRAFT'].update(status=draft['status'],C_complete_render_requested=True,C_thread=c['threadId'],HTML_and_source_bytes=22497,Word_bytes=8351,selected_local_paths=81,missing_local_paths=0,
    actual_prepare_CPU=draft['CPU_seconds'],new_ZIP=False,freeze_performed=False,extra_render_or_link_recheck_this_sync=False)
q8['title']='86/363420与98/414132数学/kernel/A/B/独立freshC已全部完成，轻量专家材料已更新但未冻结'
q8['outcome_class']='ALL_ACTUAL_Q8_ROW_ORIGINALS_MATH_KERNEL_A_B_DISTINCTFRESHC_COMPLETE_NEW_TWO_DELIVERY_UNFROZEN'
q8['scope']+=' 两新原目标finalC672实际ce6eb098…异真实A e4/B5da，逐tuple三facetPASS、priorityUNKNOWN；不再等待672。--c-complete轻量材料已实际更新，仍0ZIP，不含mixed/base/MILP认证。'
q8['distance_text']+=' 最终C672实际SUCCESS，MCPthreadce6eb098-dcb5-4864-b0bd-c5a87b05647c不同A/B，一次sharedfreshcall逐86/98精确tuple math/formal/bindingPASS，prior旧scope未冒代。两ROOT_GRAPH_RELEASE也已标新scope审阅完整。轻量HTML/txt各22497B、Word8351B、81paths/.014047383CPU，C_complete_rendertrue，仍未冻结/0ZIP；old146snapshot包不变。'
q8['lesson_and_restart_condition']+=' 两新图本地数学/fresh/kernel/Audit/binding及newA/B/distinctfreshC现实际闭合，公开priority/global仍UNKNOWN；C672已终态不poll或重试。当前新研究独立只恢复mixed-copy既有session65524，不把新小参数模型纳入C判定；无自动90/94或新cap队列。'
bar=rows[1];p=bar['other_metrics']['mixed_five_holes_copycycles_sigma31_experiment'];p.update(status='ACTUAL_G0_PREP_PASS_ONE_EXACT_MILP_STARTED_FEASIBILITY_NOT_REPORTED',
    actual_G0_n=10070,actual_G0_m=154390,actual_pin_pool=1750,actual_freed_old_U=130,actual_degree_histogram=base['degree_histogram'],actual_spare_histogram=base['exact_spare_histogram'],
    all1295_literal_clone_N_binding=True,source_edges_preserved=True,actual_source_prep_CPU_terminal=bt['CPU_seconds'],root_total_source_prep_about_CPU=8.552,
    new_literal_Bcube=dict(status='PASS',identity='Blooped^3=16Blooped+J',entries=342225,mismatches=0,old_R2_Steiner_sigma_field_BFS_reruns=False),
    solver_model=dict(rows=62181,binaries=10500,nonzeros=7349320,old_target_coverage_rows=60420,all_old_targets=True,matrix_import_prep_CPU=model['matrix_preparation_and_import_CPU_seconds'],
        helper_graph='K6',helper_pin_budget=26,objective='feasibilityonly',total_CPU_budget=120,solver_limit_seconds=90,single_thread=True),
    solver_saved_handle=dict(status=handle['status'],session=65524,supervisor_pid=handle['supervisor_pid'],child_pid=handle['child_pid'],handle=D+'MILP_HANDLE.json',
        state_scope='lastactualsavedhandle_nooutcomeinferred;pollthissameexistingsessiononly',no_timer_restart=True),
    independent_interface_paper='SUPPORTED_ALL_OLD_TARGET_ROWS_AND_FIXED_K6_CLOSED_B2_B1_IFF_NO_NEW_EXPERIMENT',independent_interface_note=D+'INDEPENDENT_INTERFACE_NOTE.md',
    mixed_in86_98_C_scope=False,complete_candidate_10076_accepted=False,portfolio_graph_parameter_Lean_increments=[0,0,0])
bar['distance_text']+=' 新mixed G0实际prepPASS：10070/154390/pool1750/130freedU、degree28:20/29:1600/30:130/31:8320与spare3:20/2:1600/1:130全命中；新增literalB³=16B+J的342225项0错，sourceprep约8.552CPU/30，0旧R2/Steiner/σedges/BFS/field重跑。唯一MIP实际session65524/MILP_HANDLE child464924启动，MODEL62181rows/10500binary/7349320nnz，prep1.603CPU、solver90/total120单thread；纸面接口全oldtarget+fixedK6必要充分SUPPORTED，无新实验，feasibility未报不加图/Lean。'
bar['lesson_and_restart_condition']+=' 生成规则的具体预测已由actualG0 counts/spare/freeU命中，而可同时实现全部helper覆盖仍留给这唯一MIP实际终态。必要充分currentG0 closedB2/closedB1接口只对固定K6成立，不以抽样或badpair目标替代全部oldtargets，也不强加单helperprefix。恢复只poll现session65524、以MILP_HANDLE为准，无seed/timer/新pattern重启；即使有feasible pins仍需完整候选和fresh接受，当前0portfolio/Lean，不被86/98 C认证。'
e=[C+'GEMINI_RAW.json',C+'DISPOSITION.md',E+'_DRAFT_RECEIPT.json',E+'.html',E+'.html.txt',E+'.docx']
de=[D+x for x in ['RESULT.json','TERMINAL.json','NEW_B_CUBE_CHECK.json','MODEL.json','MILP_HANDLE.json','SOLVER_CHECKPOINT.json','INDEPENDENT_INTERFACE_NOTE.md','PROOF_AND_INTERFACE.md','PARAMETERS.json','G0.edges','PIN_POOL.tsv']]
assert all((R/x).is_file()for x in e+de);q8['evidence_paths']=list(dict.fromkeys(q8['evidence_paths']+e));bar['evidence_paths']=list(dict.fromkeys(bar['evidence_paths']+de))
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 t=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=t.returncode,stdout=t.stdout,stderr=t.stderr));assert t.returncode==0,(cmd,t.stderr,t.stdout);return t.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,148,39,42)
block=f'''<!-- {B} -->
# 当前：86/98最终C672已实际PASS；mixed G0准备PASS，唯一MILP恢复同session65524

同Goal ACTIVE，ledger420复用[q8](experiments/{ids[0]}.md)+[barrier](experiments/{ids[1]}.md)两现节点/0新行；148／39／Lean42、stage44／36、outside42／35、known43/main103_3/global0不变。finalC672真实ce6eb098-dcb5-4864-b0bd-c5a87b05647c异A e4/B5da，86/98两个精确tuple三facet实际PASS，priorityUNKNOWN；本两图完整数学/kernel/A/B/freshC已齐，不再等672。轻量--c-complete已实际HTML/txt22497B、Word8351B、81paths/.014047383CPU，仍0ZIP/未冻结，旧包不改。

mixed源/base实际PASS：G0=10070/154390、pool1750、freedU130与degree/spare全命中，新Bcube342225项PASS，约8.552CPU/30且没重旧R2/Steiner/σ/BFS/field。f9 paper支持fixedK6所有oldtarget闭B2/B1必要充分接口，0额外实验。唯一MILP已启动，当前保存handle {handle['status']}、child{handle['child_pid']}，62181rows/10500binary/7349320nnz，prep1.603CPU；solver90/total120单thread，恢复只poll同session65524及MILP_HANDLE，不预报可行、不新建run、不加图/Lean。mixed与固定helper旁支不在已完成86/98 Cscope。

'''
p0=W/'gap_map.md';assert B not in p0.read_text();p0.write_text(block+p0.read_text())
p0=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p0.write_text(p0.read_text()+f'''

## {now} 两新端点finalC已实际终态PASS，轻量材料完成更新；mixed唯一联合模型接actualbase

本次只复用[q8](experiments/{ids[0]}.md)、[barrier](experiments/{ids[1]}.md)，ledger420/0新行，148／39／Lean42、stage44／36、outside42／35、known43/main103_3/global0不变。finalC672完整raw/JSON与rootdisposition实际读取，真实threadce6eb098-dcb5-4864-b0bd-c5a87b05647c异A e4/B5da，一次sharedfreshcall逐86/363420与98/414132 math/formal/bindingPASS+priorityUNKNOWN。两ROOT release已明确新scope A/B/C完整，0review验证重跑，不再等待或poll672。实际--c-complete轻量DRAFT_RECEIPT已读，statusUNFROZEN_TWO_TARGET_EXPERT_DRAFT_C_ROOT_DISPOSED，HTML/txt各22497B、Word8351B、81selectedpaths无缺、.014047383CPU；仍0ZIP/未freeze，旧146/37/40包不可变。

mixed-fiveholes/cycle/σ新base预测经produceractualPASS：S8775原边全保，1295clone完整原26N绑定，G0=10070/154390、F1620、cycles1620+σpeers800；130freedU，pool1750、degree28:20/29:1600/30:130/31:8320及spare3:20/2:1600/1:130全命中。新增Blooped³=16B+J在342225orderedentries0错，为同步三步product路线提供literal输入，未重A³/旧B-R2/Steiner/σ2600edges/order2/field/旧BFS。prep约8.552CPU/30，base不是10076候选验收，0portfolio/参数/Lean。

f9只读code/receipt纸面SUPPORTED，所有G0 oldtargets含F与freedU均入fixedK6闭B2/B1联合覆盖；K6可缩短helper交错路径，故条件既必要又充分，pin余度端点约束也精确。未重新载CSR/图做额外check，不将paper支持当literal最终候选或求解可行证。唯一exactMILP root已启动session65524，当前MILP_HANDLE保存status{handle['status']}/supervisor{handle['supervisor_pid']}/child{handle['child_pid']}；MODEL62181rows含60420coverage、10500binary/7349320nnz，matrix/importprep1.602992CPU，solver90/total120单thread。feasibility未报，不加计，不重timer/seed/pattern；恢复只poll这同一session及handle，后续可行仍需完整graph与fresh数学接受。所有mixed/helper分析不在86/98 Cscope，根文件和旧包未改。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'Actualnew86_98finalC672SUCCESSce6eb098distinctA_e4_B5da/twoexacttuplemathformalbindingPASSpriorityUNKNOWN/0reruns;Ccompletednolongerpending. LightweightccompleteDRAFT22497htmltxt8351Word81paths.014047383CPU0ZIPoldpacketunchanged. MixedG0produceractualPASS10070_154390_pool1750_freedU130degree_sparematch/newBcube342225PASS/sourceprepabout8.552CPU0oldR2SteinerSigmaBFSfield. FixedK6alloldtargetinterfacepaperSUPPORTED0newexperiment;oneMILPsession65524handlecurrentrows62181binary10500nnz7349320prep1.603CPU_solver90total120oneThread_feasibilityunknown_recoveronlysamehandle/notinCscope. Ledger420twoexistingrows148_39Lean42unchanged/0newmathruns_rootedits_frozenwrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_ACTUAL86_98_FINAL_C_COMPLETE_MIXED_BASE_PASS_EXISTING_MILP_HANDLE_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=148,legal_parameter_pairs=39,stage_graphs=44,stage_pairs=36,complete_formula_Lean=42,outside42_35=True,known43_main103_3_global0=True,new_graphs=0,new_Lean=0,new_frameworks=0,
    new_two_actual_final_C='SUCCESS',C_actual_thread=c['threadId'],C_distinct_A_B=True,C672_completed_not_pending=True,lightweight_DRAFT_Ccomplete=True,new_ZIP=0,
    mixed_G0_actual=[10070,154390],mixed_pool=1750,mixed_freedU=130,new_Bcube342225_PASS=True,source_prep_terminal_CPU=bt['CPU_seconds'],mixed_interface_paperSUPPORTED=True,
    mixed_MILP=dict(session=65524,status_as_saved_handle=handle['status'],supervisor_pid=handle['supervisor_pid'],child_pid=handle['child_pid'],rows=62181,binaries=10500,nnz=7349320,solver90_total120=True,feasibility='NOT_REPORTED',resume_only_same_handle=True),mixed_not_C_scope=True,
    evidence_paths_checked=len(e)+len(de),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
