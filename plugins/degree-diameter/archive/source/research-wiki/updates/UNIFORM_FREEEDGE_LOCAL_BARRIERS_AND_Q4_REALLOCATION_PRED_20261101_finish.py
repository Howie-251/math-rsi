from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';B='UNIFORM_FREEEDGE_LOCAL_BARRIERS_AND_Q4_REALLOCATION_PRED_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');rows=json.loads((W/f'updates/{B}_ROWS.json').read_text());L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,143,36,37)
block=f'''<!-- {B} -->
# 当前：新uniform/free-edge局部障碍已存；q4重分配7532只是待检验预测

同Goal ACTIVE，ledger420复用2现节点/0新行；143／36／Lean37、stage39／33不变。q8三原目标C与冻结ZIP已完成，以下新局部lemma不在其Cscope，冻结包不动。

[原barrier节点](experiments/{rows[0]['id']}.md)新增两范围：uniform完整k-copy、固定旧邻接，任意helperbatch须M≤floor((Δ+2)²/4)，balancedk1..45/Paynek1..44排除；6291456 subset-owner toy支持/1.112874562CPU。允许free-old互连但保source/mandatoryclone边时，旧route被合法peerclone gadget推翻，新分类给M≤floor((δ+2k+1)²/4)，balancedk1..23/Paynek1..22排除；.033554806CPU/仅2个13点tinyBFS。都不适用P33/F9的不同free-complement；旧onecopy历史不重写、不重跑。

[q4旧7531节点中的新规则预测](experiments/{rows[1]['id']}.md)：保7242源H全部90525边，省17条diagonalclone→fill边，加hub7531连全部17fillers；预计7532/97750/max26/D3，degree17:1/24:17/25:289/26:7225，尚未验收/不计图Lean。该规则改变mandatory边，超出旧barrier前提；producer/freshindep各≤20CPU，仅这一实例，须比较三类新根预测。以下保留历史。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
comment=f'''\n\n## {NOW} 新局部饱和障碍推进到uniform多copy与free-edge；生成转为q4删边重分配预测

原Wiki仅复用[barrier节点](experiments/{rows[0]['id']}.md)及[7531节点](experiments/{rows[1]['id']}.md)，ledger420、143／36／Lean37、stage39／33保持。新lemma不计图/Lean/framework/Ctarget，不回写已冻结q8包；本次0数学或solver重跑。

uniform多copy的纸面论证真正越过旧k1唯一owner限制：owner可为任意subset，emptyclass有实际toy例，所以不再用“每class必须有人”辅助断言。准确旧中心route覆盖与degree双计数给M≤floor((Δ+2)²/4)，Δ=δ+k，对任意k必要；balancedk≤45、Paynek≤44因此关闭。6291456个新subset-owner配置/1953140route-valid/0反例，terminal1.112874562CPU，不重跑旧singleton toy。旧单helper和onecopy已证历史保留，最新较宽范围另记，粗界到下一cap取等不等于存在。

free-edge模型保每条source及mandatoryclone边，允许free-old/clone之间任意加边。实际13点k2peerclone新三步路线推翻旧fixed-adj精确route式，不能直接套用；合法首pin消耗自身一个slot，最多再借k−1个peer，共至多k+1个旧targets，新求和给M≤floor((δ+2k+1)²/4)。balancedk≤23、Paynek≤22关闭，.033554806CPU只做2次tinyhelperBFS，0q8大图/Lean/外审。允许更宽连接令可排k区间缩小，未把必要界当全局degree-diameter上界。

两者依赖D=H减unionN⊆C且在C孤立、C_off matching等abstract接口。P33旧free余54450、F9U10旧free余13122不满足complement全在C，故不适用；只继承metadata未重测。nonuniform、饱和前联合生成、删除/修改mandatory边或换source/code等仍开放，不自动派高k图。

新预测由这个障碍实质改变生成：旧7531的immutable fullN(H)模型改成保7242源H所有90525边，省原17个diagclone→filler边，再加单hub连17fillers，m不变预计n7532/97750/Δ26/D3。它不是在保留7531全部边的图上单加点，故不被前述固定mandatory边障碍直接否定。事前degreehist17:1/24:17/25:289/26:7225；三类新根预测分别17×(1,24,418,7089)、272×(1,25,441,7065)、hub(1,17,425,7089)。producer/freshindep各20CPU待实际结果；不继承旧7531的图/Lean/外审完成，不提前加计，也不派更大参数梯子。
'''
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+comment)
helper=R/'aris_repo/tools/research_wiki.py';calls=[]
def call(*args):
 cmd=[sys.executable,str(helper),*map(str,args)];p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);calls.append({'command':cmd,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0,(cmd,p.stderr)
call('log',W,'2026-11-01 minimalexistingbarrier+7531nodes:uniformallkfixedadjM<=floor((Delta+2)^2/4)closesbalancedk1_45Payne1_44/new6291456subsettoy1.112874562CPU;freeedgewithmandatoryedgesM<=floor((delta+2k+1)^2/4)closesbalanced1_23Payne1_22/.033554806CPU/tinytoyonly.NotP33_F9/not3graphCscope/frozenQ8untouched. Newq4diagonalfillreallocationpredictiononly7532/97750/cap26/keepH90525/remove17clonefill/add17hubfill;producer_indep20CPUeach/notaccepted/noextraLean. ledger420143_36Lean37unchanged/0newrows/mathreruns/rootfiles.')
call('rebuild_index',W);call('rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
S=R/'research/ddp/two_successful_methods_20261101';G=S/'retained_edge_transfer/even_q8_gq_geometry_pilot';ps=[G/(prefix+'_'+suffix)for prefix in ['INDEPENDENT_UNIFORM_MULTICOPY','INDEPENDENT_FREE_EDGE_AUGMENTATION']for suffix in ['NOTE.md','RESULT.json','TERMINAL.json']]+[S/'retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/diagonal_fill_reallocation/PREDICTION_AND_SCOPE.md'];assert all(p.is_file()for p in ps)
receipt={'status':'PASS_EXISTING_BARRIER_UNIFORM_FREEEDGE_AND_Q4_PREDICTION_ONLY_WIKI_SYNC','updated_UTC':NOW,'ledger_records':420,'records_added':0,'records_updated':2,'named_legal_graphs':143,'legal_parameter_pairs':36,'stage_graphs':39,'stage_pairs':33,'complete_formula_Lean':37,'new_graphs':0,'new_Lean':0,'new_frameworks':0,'new_local_lemmas_in_q8_three_C_scope':False,'uniform_bound':'M<=floor((Delta+2)^2/4)','uniform_k_excluded':{'balanced':[1,45],'Payne':[1,44]},'uniform_toy_configurations':6291456,'uniform_CPU':1.112874562,'freeedge_bound':'M<=floor((delta+2k+1)^2/4)','freeedge_k_excluded':{'balanced':[1,23],'Payne':[1,22]},'freeedge_CPU':0.033554806,'freeedge_tiny_BFS_historical':2,'q8_BFS_repeated_now':0,'applies_to_P33_F9':False,'candidate7532_status':'PREDICTION_NOT_ACCEPTED','candidate7532_expected_parameters':[26,3,7532,97750],'candidate7532_accepted_instances_added':0,'candidate_producer_and_independent_CPU_budget_each':20,'old_onecopy_history_preserved':True,'new_small_evidence_paths_checked':7,'actual_helper_calls':f'research-wiki/updates/{B}_HELPER_CALLS.json','query_current':True,'math_solver_Lean_runs_this_sync':0,'root_files_modified':False,'frozen_Q8_package_modified':False}
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
