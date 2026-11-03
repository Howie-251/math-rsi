"""Finish one already-upserted Wiki increment with real helper receipts."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'research-wiki';BASE='Q8_FORMAL_FULL_PENDING_P33_FROZEN_AND_LOCAL_MECHANISMS_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
rows=json.loads((W/f'updates/{BASE}_ROWS.json').read_text());L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text())
assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,142,35,34)
ID=rows[-1]['id'];QID=rows[0]['id'];PID=rows[1]['id'];AID=rows[2]['id'];UID=rows[3]['id']
qmetric=rows[0]['other_metrics'];fm=qmetric['full_Lean_queue'];snapshot_completed=fm['actual_completed_snapshot']
block=f'''<!-- {BASE} -->
# 当前：局部路线障碍改变生成，q8 fullproof实际续跑；142／35／Lean34

同Goal ACTIVE，ledger420；142合法／35参数、stage38／32、具体Lean34；known43/overlap40/main103_3/outside36_31/global0不变。本次0图／Lean新增。

[q8两源](experiments/{QID}.md)数学已验/A编码实际PASS；1225pairs finitepilot40.105386447CPU。成本受控调整非数学失败，原缓存/558.4055CPU保留；row040 packed32/640pairs PASS7.353664CPU后原12000CPU预算内实际PID1602629/session41458、8workers续跑，完整原目标未完。HANDLE/CHECKPOINT是恢复入口，别按旧PID或pilot计Lean。

[A饱和局部门](experiments/{AID}.md)：onecopy任意helperbatch必要M≤floor((Δ+2)²/4)，两q8均失败；任意≤5 diagonal holes净增一点必要式也失败。0copy图；不排k2/offdiagholes/改边。

[B点级交换](experiments/{ID}.md)：55LP精确关retU9/U8；MIP min6仅solver证据。fixedsupport837被target48真实rank3三族sum≤73/product≤8000否定，不止F3切片。下一步改真实三方线互补，19层固定W/ret4≥811单次pilot准备/在途未返，非整池无解。

[P33十五包](../expert_review_current/P33_FIFTEEN_RESULTS_20261101_FREEZE_RECEIPT.json)已实冻317192282B/816entries/16边表，140/33/Lean34快照排除q8；sourcefill/JGT优先权仍UNKNOWN，未认证全球。以下保留历史。

'''
gap=W/'gap_map.md';old=gap.read_text()
assert BASE not in old
gap.write_text(block+old)
comment=f'''\n\n## {NOW} 本轮一次增量：从容量/余度转向真实短路线与线族互补

同Goal ACTIVE。真实helper已复用4节点、新增1个local机制节点，ledger420；142合法／35参数、stage38／32、具体Lean34、known43/main103_3/outside36_31/global0不变。没有新完整图、新Lean实例或新framework，不把文档同步计数学成果。

[q8两完整源](experiments/{QID}.md)数学独验继承，不重跑旧field/graph。finitepilot实际1225pairs、两module、40.105386447CPU PASS；新sharedA编码SUCCESS，两原目标各PASS，thread45b60268-8b9e-4aa3-b8f3-24208bab0107，非finalkernel。fullproof实际授权1104新module/12000CPU/单module60/最多8leaf。两次CONTROLLED_COST_REASSESSMENT不是数学失败，历史558.405518791CPU和49PASS保留；row040 packed32的640pairs实际7.353664CPU/propext PASS，预计8500CPU只是估算。写入前实际ps见PID1602629命令driver.py --resume --workers8，session41458、同预算续跑；payload snapshot为{snapshot_completed}PASS，实际恢复读HANDLE/CHECKPOINT，q8具体Lean仍0。

[A局部门](experiments/{AID}.md)先预测完整onecopy饱和后任意内部helper图也缺路线；完整≤3route分类支持uniqueowner、active degree≥t−2，得M≤t(Δ+2−t)≤floor((Δ+2)²/4)。balanced4160>1764、Payne4032>1722，onecopy任意finite jointbatch关闭；小toy含unused/inactive且0反例，并有sharp中心路线例，不冒完整图。再预测少量diagonal holes能否净增一点；任意I证明(R−b)(R−b−1)≤(b+1)(b+2)Δ，b1..5均失败。每源一个b5小表只支持路线坐标，普遍排除来自纸面证明。停止上述samecap饱和batch和≤5diagonal修补；k≥2、offdiagonal holes、b6+、改code/旧边/提高cap未排，0copy图。

[B点级交换](experiments/{ID}.md)原来不知道810整层code能否局部松动：预测retU9不增而retU8或有gap；55个精确primal/dual实际81/162，P1支持/P2推翻。只有两个替换对和一个C4，不能继续靠保留8/9整plane微调。单次MIP返回min改变6/数值bound6，仅solver最优非formal排5。固定原13残余support的唯一LP精确837达界，却在target48的17/35/74三方向det6处预测失败：投影分离给三正线族sum≤73/product≤8000，27³违规。512格及20/20/20、1/8/64实际局部witness支持，排任意完整F9line-unions，非仅F3hyperplane。837不是实际候选图，改用真实三way互补生成权重。完整admissible还含64/71未纳入该LP；19层(4full+15)固定W/ret4≥811单次实际pinpilot准备/在途，尚无终态，不登记整池失败。

[十五图冻结回执](../expert_review_current/P33_FIFTEEN_RESULTS_20261101_FREEZE_RECEIPT.json)实际317192282B/816entries/16边表，140/33/Lean34归档，不含新q8；本轮只读receipt不重验ZIP。A/B/distinctfreshC十五原目标齐全仍不解除sourcefill priority UNKNOWN/JGT正文缺口，若同fill/接口已公开则十五+50归0。旧冻结包未动，root-owned状态/报告/HTML/恢复由root负责。
'''
comments=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';comments.write_text(comments.read_text()+comment)
CALLS=[];HELPER=ROOT/'aris_repo/tools/research_wiki.py'
def call(*args):
 cmd=[sys.executable,str(HELPER),*map(str,args)];r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
 CALLS.append({'command':cmd,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 assert r.returncode==0,(cmd,r.stdout,r.stderr)
 return r
for to,typ,text in [(UID,'extends','Actualpointcapacity/linecompatibilityfollowup,notreplacementofacceptedU10fivegraphs.'),('ddp-f9-c78-all-controller-open-neighborhood-packing-exact10-20261101','uses','Wholeplaneopt10inheritedwithoutBBreplay;new55LPscopeandactualrank3obstructionarepointlevelbounded.'),('ddp-schreier78-f9-six-conic-affine-fullgraph-56862-d54-d3-20261101','uses','ImmutableacceptedF9actualcontrollerports/chartsinherited;0sourcegraphBFSorallfieldranksrepeated.')]:
 call('add_edge',W,'--from','exp:'+ID,'--to','exp:'+to,'--type',typ,'--evidence',text)
call('log',W,'2026-11-01 oneincrementledger420/142legal35pairsstage38_32Lean34:reuse4nodesadd1localU10node;55exactLPretU9U8closed,minchange6solveronly,capacity837rejectedbyactualtarget48rank3arbitrarylinebound73/product8000;actual19layerW>=811pilotpendingdifferentweightsallowed. q8singlehelper+onecopyarbitraryjointbatch+diagonalb1to5localscopesclosed,0copygraphs. q8finitepilot1225pairs40.105386447CPU/encodingAactualPASS2targets1call;controlledcostreassessment0mathfail,actualPID1602629session41458resumeworkers8/same12000CPU,noq8concreteLean. P33fifteenactualfrozen317192282B816entries16edgefiles140_33snapshotexcludesq8,priorityUNKNOWN/global0. 0experimentrerun/rootfiles/frozenpacketedit.')
call('rebuild_index',W);call('rebuild_query_pack',W)
(W/f'updates/{BASE}_HELPER_CALLS.json').write_text(json.dumps(CALLS,ensure_ascii=False,indent=2)+'\n')
# Scope the static checks to the changed nodes/current recovery text and their real evidence.
paths=set()
for row in rows:
 for p in row['evidence_paths']:
  path=ROOT/p
  assert path.exists(),path
  paths.add(str(path))
files=[W/'experiments'/f"{row['id']}.md" for row in rows]
texts=[(p,p.read_text()) for p in files]+[(gap,block),(comments,comment),(W/'query_pack.md',(W/'query_pack.md').read_text())]
links=0
for origin,txt in texts:
 for target in re.findall(r'\]\(([^)]+)\)',txt):
  target=target.strip().strip('<>')
  if target.startswith(('http:','https:','mailto:','#')):continue
  target=target.split('#')[0]
  if not target:continue
  path=(origin.parent/target).resolve() if not target.startswith('/') else Path(target)
  assert path.exists(),(origin,target,path)
  links+=1
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text())
assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'],L['known_publicly_dominated_graph_examples'],L['pending_outside_saved_table_graph_examples'],L['pending_outside_saved_table_parameter_pairs'])==(420,142,35,34,43,36,31)
receipt={'updated_UTC':NOW,'status':'PASS_ONE_INCREMENT_FORMAL_LIVE_COST_FEEDBACK_FROZEN_P33_AND_LOCAL_ROUTE_LINE_MECHANISMS','ledger_records':420,'records_added':1,'records_updated':4,'new_accepted_graphs':0,'new_concrete_Lean':0,'new_frameworks':0,'named_legal_graphs':142,'legal_parameter_pairs':35,'stage_graphs':38,'stage_pairs':32,'complete_formula_Lean':34,'known_publicly_dominated':43,'saved_table_dominated_overlap':40,'main_table_graphs':103,'main_table_parameter_pairs':3,'pending_outside_saved_table_graphs':36,'pending_outside_saved_table_pairs':31,'certified_global_records':0,'q8_finite_pilot_actual_pairs':1225,'q8_finite_pilot_actual_CPU':40.105386447,'q8_full_authorized_modules':1104,'q8_full_authorized_CPU':12000,'q8_full_latest_actual_PID':fm['latest_driver_PID'],'q8_full_latest_session':41458,'q8_full_actual_status_snapshot':fm['actual_status'],'q8_full_completed_snapshot':snapshot_completed,'q8_complete_concrete_Lean':0,'q8_cost_control_is_math_failure':False,'q8_external_A_actual':'PASS_BOTH_ENCODINGS_ONE_SHARED_CALL','P33_frozen_bytes':317192282,'P33_frozen_entries':816,'P33_archived_edge_files':16,'P33_snapshot':[140,33,34],'P33_snapshot_excludes_q8':True,'sourcefill_priority':'UNKNOWN_JGT_BODY_GAP','actual_W19_pointpacking_pilot':'PREPARING_OR_RUNNING_NO_TERMINAL_NOT_ACCEPTED_GRAPH','canonical_upsert_command':[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(W/f'updates/{BASE}_ROWS.json')],'actual_helper_calls':f'research-wiki/updates/{BASE}_HELPER_CALLS.json','resolved_evidence_paths':len(paths),'checked_local_links':links,'query_current':True,'experiments_rerun':0,'root_owned_files_modified':False,'frozen_expert_packets_modified':False,'ZIP_checks_repeated':False}
(W/f'updates/{BASE}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
