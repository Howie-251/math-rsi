from pathlib import Path
from datetime import datetime,timezone
import json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';B='B_SOURCE17_TRANSPORT_AND_UNIQUE_PLANE_POOL_STOP_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
row=json.loads((W/f'updates/{B}_ROWS.json').read_text())[0];ID=row['id'];L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,143,36,37)
block=f'''<!-- {B} -->
# 当前：B source17运输对照已终态，唯一最佳plane仍数值无811；停止该分支

同Goal ACTIVE，ledger420仅复用B现节点1row；143合法／36参数、stage39／33、Lean37不变，0新图。q8仅B3 cell516在途，C3未发；三图专家稿/根状态本轮不动。

[B实际新反馈](experiments/{ID}.md)：7个shared pair完整线族不交iff两侧scalar images分离，等式两边必须同倍数缩放。source17 ambientrank3/全部91plane限制rank2；46个全6dart横截plane最少4方向(原W5)，8个最优，首normal(1,0,4)、basis(0,1,0)/(8,0,1)。无单线性slab坐标只关整个plane，不排小集合/非线性支持。

只换这一个source17 plane、其他18层不变的真实1539pool，唯一数值MIP INFEASIBLE/3.933452689CPU，旧810只违反新card阈值。无incumbent/rootLP/独立UNSAT证书，非全W/全pointsets无解。局部方向5→4仍不足协调所有actualpin。已停止本分支：不扫第二plane、不续旧timer、不扩729池；下一B需联合cross-dart支持构造或有依据改变整体结构。以下保留历史。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
comment=f'''\n\n## {NOW} B source17实际运输与唯一plane对照：预测检验后停止分支

只最小复用[B现节点](experiments/{ID}.md)，ledger420、143／36／Lean37和stage39／33均不变，0新图/新Lean/新方法行。root已接受实际小文件；本次不跑solver/数学、不改q8专家稿或根文件。

先前不知道一个共同source17平面能否把各target的独立slabs协调起来。实际7pair拉回给完整线族不交iff f17(S17)∩fw(Sw)=空；规范化要对等式双侧同倍数，不能独立projective缩放再当相等。ambientrank3使任意二维plane上的7限制满rank2，单一线性坐标不能覆盖整个plane的共同限制。91表中46个保持6dart全部transversal；原W需5方向，8个plane能降到4，首normal(1,0,4)/basis(0,1,0),(8,0,1)，该局部接口是真实改善，非packing保证。

root仅授权一个有依据的受控替换：source17改为(8t,s,t)，其他14变量层和4固定层仍旧W，全部1539候选/1215点变量，实际pin模型要求≥811。一次MIP数值INFEASIBLE，terminal3.933452689CPU，不是UNKNOWN；旧810负对照全部pin/logic过，只差新增cardinality1。原返回无x/bound/gap/nodecount，未取得rootLP或独立整数UNSAT证书，不能外推全部plane/所有W/全pointsets。正预测“只降方向数便够811”未支持，留下的认识是多个源层的投影images仍须联合满足。

该分支已明确停止，不扫第二最佳plane/旧timer/729大池。下一B必须联合cross-dart支持构造，或凭新结构依据改变整体连接；不能把本次局部改善当继续小调的理由。q8三个原目标已kernel/Audit完成，当前只有B3 cell516外审在途，C3尚未发；本pilot不属于其graph计数或外审scope。
'''
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+comment)
helper=R/'aris_repo/tools/research_wiki.py';calls=[]
def call(*args):
 cmd=[sys.executable,str(helper),*map(str,args)];p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);calls.append({'command':cmd,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0,(cmd,p.stderr)
call('log',W,'2026-11-01 oneexistingBnodeonlysource17transport7pairscalarimagesiffwithjointscaling/ambientrank3/all91rank2/46transversalmin4dirs8bestoriginal5,onebestnormal104basis010_801actual1539pool811numericalINFEAS3.933452689CPU;baseline810onlycardthresholdfails,norootLP/UNSATcertificate/globalWclaim. Branchstopped:no2ndplane/nooldtimer/no729pool,nextjointcrossdartsupportorstructuralchange. ledger420/math143_36/Lean37unchanged,B3cell516inflight/C3notrequested,0newmath/graph/Lean/docsrender/rootfiles/expertpacketedit.')
call('rebuild_index',W);call('rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
paths=set()
for x in row['evidence_paths']:
 p=R/x;assert p.exists(),p;paths.add(str(p))
node=W/'experiments'/f'{ID}.md';texts=[(node,node.read_text()),(W/'gap_map.md',block),(W/'DD82_PROGRESS_AND_COMMENTS_20261018.md',comment),(W/'query_pack.md',(W/'query_pack.md').read_text())];links=0
for origin,txt in texts:
 for target in re.findall(r'\]\(([^)]+)\)',txt):
  target=target.strip().strip('<>')
  if target.startswith(('http:','https:','mailto:','#')):continue
  target=target.split('#')[0]
  if target:assert (origin.parent/target).resolve().exists(),(origin,target);links+=1
receipt={'status':'PASS_EXISTING_B_NODE_SOURCE17_TRANSPORT_AND_UNIQUE_PLANE_BRANCH_STOP','updated_UTC':NOW,'ledger_records':420,'records_added':0,'records_updated':1,'named_legal_graphs':143,'legal_parameter_pairs':36,'stage_graphs':39,'stage_pairs':33,'complete_formula_Lean':37,'new_graphs':0,'new_Lean':0,'new_frameworks':0,'transport_pairs':7,'joint_two_sided_scaling_explicit':True,'ambient_rank':3,'all91_plane_rank':2,'transversal_planes':46,'minimum_directions':4,'old_W_directions':5,'best_planes':8,'first_normal':[1,0,4],'first_basis':[[0,1,0],[8,0,1]],'unique_changed_plane_pool_status':'NUMERICAL_MIP_INFEASIBLE_NOT_FORMAL_UNSAT','unique_pool_terminal_CPU':3.933452689,'baseline810_control':'ONLY_NEW_CARDINALITY_THRESHOLD_FAILS','rootLP_or_independent_UNSAT_certificate_claimed':False,'branch_stopped':True,'next_plane_timer_or729pool_dispatched':False,'B3':'CELL516_INFLIGHT','freshC3':'NOT_REQUESTED','resolved_evidence_paths':len(paths),'checked_local_links':links,'actual_helper_calls':f'research-wiki/updates/{B}_HELPER_CALLS.json','query_current':True,'solver_math_BFS_Lean_reruns':0,'document_renders':0,'root_files_modified':False,'expert_three_documents_modified':False,'other_old_experiment_nodes_modified':False}
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
