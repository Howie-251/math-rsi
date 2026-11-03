"""Sync actual terminals and a single next parameter; preserve all accepted history."""
from pathlib import Path
from datetime import datetime,timezone
import json,re
B=Path(__file__).resolve().parent;R=B.parents[2]
def load(p):return json.loads(p.read_text())
def save(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');s=load(B/'STAGE_STATE.json');r=load(B/'STALE_FOLLOWUP_ROUND_20261101.json')
assert [s['accepted_total_named_legal_instances'],s['accepted_total_parameter_pairs'],s['complete_concrete_formula_Lean_instances']]==[153,43,47]
receipts=['wiki_sync/EDGE_VOLTAGE_LOCAL_FULL_AND_GLOBAL32_20261102_RECEIPT.json','wiki_sync/SOURCE3645_SINGLECUT_MAXSTAR_AND_NONBASEBASE_BOUND_20261102_RECEIPT.json','wiki_sync/NATURAL364_HELPERS14_COMPLETE_TERMINAL_20261102_RECEIPT.json','wiki_sync/NATURAL364_PETERSEN19_METRIC_ASSIGNMENTS_TERMINAL_20261102_RECEIPT.json']
assert [(load(B/p)['records_before'],load(B/p)['records_after']) for p in receipts]==[(459,459),(459,460),(460,460),(460,461)]
ledger=load(R/'research-wiki/DDP_METHOD_LEDGER.json');assert ledger['record_count']==len(ledger['rows'])==461
cases={
 'binary240_edge_voltage_progress':('stale_record_transfer_d8D5/binary_C30_base240_C23_cover/','EDGE_VOLTAGE_ROOT_DISPOSITION.json'),
 'source3645_singlecut_maxstar3646':('retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/','ROOT_DISPOSITION.json'),
 'natural364_cooperative_helpers14':('retained_edge_transfer/natural364_cooperative_helpers14_read/','ROOT_DISPOSITION.json'),
 'natural364_petersen_helpers19':('retained_edge_transfer/natural364_petersen_subdivision19/','ROOT_DISPOSITION.json')}
for k,(d,f) in cases.items():
 z={'directory':d,'root':load(B/d/f),'new_accepted_graph_parameter_Lean':[0,0,0]};s[k]=z;r[k]=z
N='stale_record_transfer_d3D9/two_cut_adjacent_helpers602_read/'
assert (B/N/'WEIGHTED_SOURCE_DISTANCE_INTERFACE.md').is_file()
nextq={'status':'READY_FIXED600_TWO_CUT_ADJACENT_HELPERS_NEW_BATCH_NOT_STARTED','target':[3,9,602],'directory':N,'question_zh':'转(3,9)实际600源，完整两不交cut＋相邻双helper，四端点保全部3种2+2分割；先用原G的R7/R8精确判双新根，再实际查旧旧距离。','read_gate':N+'READ_GATE.json','paper':N+'WEIGHTED_SOURCE_DISTANCE_INTERFACE.md','source':'research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.edges','source_n_m_degree_D_inherited':[600,900,3,9],'static_legal_edgepairs':402750,'static_configurations':1208250,'actual_configurations_enumerated':0,'partitions_per_unordered_cutpair':3,'cross_only2_not_complete':True,'new_radius_queries_needed':'one600rootdepth8batchexportclosedR7andR8;ifnewPREDbudgetauthorized','source_D9_revalidation_BFS':0,'new_numerics_started':False,'requires_user_approval':False,'before_next_numeric':'writePREDandfiniteCPU/returnobjects;do notresumeold3or4cutsamples','exact_newroot_condition':'R7_G(AunionB) union (R8_G(A) intersection R8_G(B)) = all600','oldold_D9':'separateactual602graphcheckrequired;newrootpassnotrecord','old_n8_D2_n61':'stillpaused'}
s['source600_two_cut_adjacent_helpers_read']=r['source600_two_cut_adjacent_helpers_read']={'directory':N,'actual_read_gate':load(B/N/'READ_GATE.json'),'paper':N+'WEIGHTED_SOURCE_DISTANCE_INTERFACE.md','new_numeric_operations':0}
for o in(s,r):
 o['updated_UTC']=now;o['wiki_ledger_rows']=461;o['next_computation_decision']=nextq;o['second_mathematical_question']={'status':'NONE_RUNNING','B_independentC23':'STOPgenericconditional32sampling_UNKNOWN','A_previous_families':'allnumericterminal,nohelpercountorcutladder'}
r.update(status='ALL15_TESTED_ZERO_RECORDS_EDGEVOLTAGE_LOCAL_SUCCESS_32UNKNOWN_3645SINGLECUT_NO_HELPERS14_NO_H19_RAW_UNSAT_NEXT3D9',new_graphs=0,new_Lean_instances=0,goal_complete=False)
for p in receipts:
 if p not in r['wiki_receipts']:r['wiki_receipts'].append(p)
s.update(phase='EDGE_VOLTAGE_AND_COOPERATIVE_HELPERS_TERMINAL_NEXT_D3D9_TWO_CUT',previous_goal_turn_classification='PROGRESS:previous15list/smallD4/C23globalcoeffcompleteNOchangednextgenerationrule',current_goal_turn_classification='PROGRESS:rank65explicitpacketvoltage/allpairflowcapacity/32globalnohit;3645all20044singlecutNO;natural364k14entireNO;Petersen19all6rawUNSAT+subsetUNKNOWN;0newgraph',jobs_scope='All numerical solver/BFS/topology/phase handles terminal. Complementary source/history,mechanism/scope,andWiki agents completed;onlynew600batchready,notstarted.',main_lines=['A: nextactual600/3D9 two-cut adjacenthelpers602, all3pinpartitions; exactweighted-sourceR7/R8 interface ready, no numericstarted','B: fixedbinary240 independentC23 conditional32 sampling STOP UNKNOWN;oldfourglobalcoeffstrictNO preserved'])
s['A'],s['B']=s['main_lines'];s['wiki_sync']={'status':'ACTUAL_INCREMENTAL_TERMINALS_COMPLETE_461','receipts':receipts};s['latest_wiki_sync']={'ledger_rows':461,'receipts':receipts,'records_added_since459':2,'human_top_preserved':True,'full_rebuild_reimport':False,'all_completed_math_synced':True,'new_accepted_graph_parameter_Lean':[0,0,0]}
# Add a small restoration entry without another research/method/graph record.
marker='<!-- NEXT_3D9_WEIGHTED_SOURCE_ROUTE_FRONTIER_20261102 -->';humanend='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
frontier=f'''\n{marker}\n## {now} 当前恢复入口：0新图；下一3D9源600双cut相邻helper\n\n完整数学终态见 [STATE](../research/ddp/two_successful_methods_20261101/STAGE_STATE.json)；Wiki研究记录461，不是图/方法数。合法版本153／参数43／具体Lean47保持。B逐边电压单packet可构造，但32全局样本无hit仍UNKNOWN；A3645单cut完整NO、自然364保边helpers1–14完整NO、Petersen19六orbit仅rawUNSAT/诊断两helperUNKNOWN，均按各自scope停止。\n\n下一 [600源读门](../research/ddp/two_successful_methods_20261101/{N}READ_GATE.md) 与 [权1/2精确路线](../research/ddp/two_successful_methods_20261101/{N}WEIGHTED_SOURCE_DISTANCE_INTERFACE.md)：保3种2+2分割，静态1208250配置，实际枚举0；须先PRED/预算再新R7/R8批，不续旧3/4cut样本或旧solver。所有旧数值终态；旧N8/D2/n61继续暂停，同一Goal ACTIVE。\n<!-- /NEXT_3D9_WEIGHTED_SOURCE_ROUTE_FRONTIER_20261102 -->\n'''
for name in ['index.md','query_pack.md','gap_map.md']:
 p=R/'research-wiki'/name;t=p.read_text();assert marker not in t and humanend in t;pos=t.index(humanend)+len(humanend);p.write_text(t[:pos]+frontier+t[pos:])
frec='wiki_sync/NEXT_3D9_WEIGHTED_SOURCE_ROUTE_FRONTIER_20261102_RECEIPT.json';save(B/frec,{'status':'PASS_RESTORE_FRONTIER_ONLY_NO_NEW_LEDGER_RECORD','updated_UTC':now,'records_before':461,'records_after':461,'new_numerics':0,'graph_parameter_Lean_increments':[0,0,0],'human_top_preserved':True,'full_rebuild_reimport':False,'modified':['research-wiki/index.md','research-wiki/query_pack.md','research-wiki/gap_map.md']});r['wiki_receipts'].append(frec);s['latest_wiki_sync']['frontier_receipt']=frec;s['stale_followup_round_20261101']=r
save(B/'STALE_FOLLOWUP_ROUND_20261101.json',r);save(B/'STAGE_STATE.json',s)
block=f'''<!-- AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->
### {now} 当前执行：本turn0新图；全局电压与合作helper已实测，下一转3D9源600

同一Goal ACTIVE，不新建/重导Wiki/重启旧队列。上一Goalturn PROGRESS；本turn亦有实际PROGRESS，未把文件更新算数学成果。仍153合法named版本／43参数／47具体Lean，阶段49图/40参数等历史口径保持，本turn0新图/参数/Lean；15老格全已新检验、0老格新纪录。唯一Wiki461研究记录，B与helper总node原位、3645和Petersen19各一新node，非图/方法数；人工顶块/旧原始source_record全部保留。

B fixedbinary240→ordinaryC23/5520：旧四globalcoeff12720全NO保留。新消费保存66paths：signededgeflow全66不同、差rank65，解22独立方程得单packet全23（21非零边）。一次全pair枚2699760flow/28920unorderedpackets全不同/min66，diag81..97，capacity必要门全过；稀疏witness仅critical一个packet满。再保22eq、给938freeedge分散随机值后补pivot，固定32完整参数，critical32/32保、首diag24/32修好，仍0全D5。best27有19987packet满/全部至少18/diag200/未覆phase10784，非目标普通坏对数；final5.704705500/20CPU，STOP不33rd/seed/hillclimb。一般逐边C23和22eq族均UNKNOWN；没有5520edgefile/新BFS/Lean/ARIS。

A actual3645/11D4：purepreservededges任意增广旧NO继承。新singlecut+all7free+cutends最大star，完整20044edge全新根fail，最佳仍漏305，0oldold阶段。复用1993R3/补1652新radius3支持，sourceD4未重验；metadata roots/new_roots首准备失败在native前、保守.1CPU保历史。按cachedrows BB/BI/II最大补holes438/356/338，两cuts都非BB则≤712<743（共享端点亦成立），至少31漏；这是paper bound非枚2cut。final2.943111119/15，STOPsinglecut不自动加cut/repair。

A natural364/714合作：旧1..13helper NO不重跑3276/81900 masks。14tree由2slack/满3叶枝与旧zero-good纸面NO；14unicyclic有28spokes且helper全度4，G1全部helper→owner≤4，G2 parent度≥3的leaf→owner≤3。按cycle/depth/childrenmultiset/dihedralcanon完整1930拓扑，1910败G1、20败G2、0幸存，fixedhost/noaddedoldold保边1..14全NO。raw计数标签已纠正first-min ordered，未重算；case.880238423/10。不是任意finiteH或一般378图NO，不自动k15。

新合作规则Petersen10九edge各细分一次：H19/m24，所有helper有spokes1或2、总28，目标383/766全4。全部5005pattern有235 Hdiam4/4770 diam5，Petersen120automorphism归6orbits。完整532assignment变量＋顺序counter共1848vars/10528clauses，6916为全部19×364精确coverage；oldold与H-H分别继承/D4保证。6orbits每个唯一5秒window均快速rawUNSAT，无prooflogged/checked，不冒形式化整族NO。第6从未测，因前5实际只1.115CPU明确重评补齐，非续旧timer。orbit0诊断0..8/0..3 rawUNSAT，0..1单次2秒UNKNOWN，按预测STOP，不能说已判单helper或两群兼容。final9.371241682/40，0source/目标383BFS/新球/Lean/ARIS，0图。

下一唯一A转(3,9) actualExoo600/900/all3/D9继承：两disjointsourcecuts＋相邻两helper，四端点全部3种unordered2+2分割；cross-only两种不完整。静态402750cutpairs/1208250配置，actual枚举0，旧3/4cut各10000样本不等此域。已读源/header和历史门；newroot exact min(1+d_G(A,t),2+d_G(B,t))由last-cut restart成立，双root可用R7(P)∨(R8(A)∧R8(B))精确筛。新通用R7/R8缓存尚无，下一须PRED预算后一次600root深8导出，不重sourceD9验证；oldold仍须实际602图检查。WEIGHTED_SOURCE_DISTANCE_INTERFACE已paper支持，不是已跑结果。

所有本轮数值与solver handles terminal，无live BFS/solver/Lean/远审；三互补代理围绕同一问题完成history/interface/scope/Wiki，不扩独立模板清单。下一600批未START，不需用户批准普通研究。旧N(8,2)/n61继续暂停；16416完整独验/Lean/A+B+distinctC/专家包、全球优先权认证0及人工反馈要求保持，所有旧严格NO与UNKNOWN范围继承不重跑。STATE/ROUND/嵌入一致，progress与候选HTML/源码/CSV同步；Goal未完成，不hash/安装/付费重试。
<!-- /AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->'''
pat=r'<!-- AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->.*?<!-- /AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->'
for rel in ['AGENTS.md','context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md','context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md','research/ddp/two_successful_methods_20261101/REPORT.md']:
 p=R/rel;t=p.read_text();assert len(re.findall(pat,t,re.S))==1;p.write_text(re.sub(pat,lambda _:block,t,count=1,flags=re.S))
p=R/'research/progress.html';t=p.read_text();t=re.sub(r'<p>更新 [^<]+</p>',f'<p>更新 {now}。同一Goal ACTIVE；旧N(8,2)/n61任务继续暂停。</p>',t,count=1)
section=f'''<section id="stale-route-current"><h2>最新：仍0新增图；全局电压与合作助手已完成实际检验</h2>
<div class="note"><strong>当前仍153合法版本／43参数／47具体Lean。本轮0新增达标图。</strong><p><a href="stale_record_candidates.html">15项清单与逐项方法</a> · <a href="stale_record_candidates.html.txt">清单HTML源码</a> · <a href="progress.html.txt">本页HTML源码</a>。下面的局部构造与排除不计新纪录。</p></div>
<table><thead><tr><th>研究问题</th><th>本轮实际结果</th><th>据此决定</th></tr></thead><tbody>
<tr><td>(8,5)独立逐边C23电压</td><td>66flow差rank65，显式单packet全23；全28920packet流容量够，32个全局参数仍无D5</td><td>局部障碍可修、全局赋值未解。STOP generic采样，逐边族UNKNOWN</td></tr>
<tr><td>(11,4)3645→3646单cut最大新星</td><td>完整20044edge全新根失败，最好漏305；两cut均非BB也有712&lt;743界</td><td>固定singlecut族NO，未进入旧旧检验，不追加cut梯</td></tr>
<tr><td>(4,5)14helper合作</td><td>tree纸面排、1930单环拓扑全排；旧1..13证据继承</td><td>固定自然364保边/noaddedoldold的1..14范围NO，更多helper未排</td></tr>
<tr><td>(4,5)Petersen19合作，目标383</td><td>5005metric中235过门/6轨道；6个完整assignment模型rawUNSAT。前4helper子模型raw冲突、前2为UNKNOWN</td><td>没有383图；未proofchecked不冒正式整族NO，停止骨架，不假装已解释单helper/共享冲突</td></tr>
</tbody></table>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D5/binary_C30_base240_C23_cover/EDGE_VOLTAGE_NOTE.md">电压构造与检验</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/NOTE.md">3645完整域</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/natural364_cooperative_helpers14_read/NOTE.md">14helper证明</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/natural364_petersen_subdivision19/NOTE.md">Petersen19模型与明确卡点</a>。</p>
<h3>下一换参数：(3,9)实际600→602</h3><p>两旧cut的四端点分2+2，连接两个相邻新helper。所有3种分割保留，静态1208250配置；旧3/4cut样本不是这个机制。已证明原G的R7/R8给精确双新根门，旧旧距离另查。本轮只完成读门与路线证明，数值尚未启动。</p>
<p><a href="ddp/two_successful_methods_20261101/{N}READ_GATE.md">600源与旧范围</a> · <a href="ddp/two_successful_methods_20261101/{N}WEIGHTED_SOURCE_DISTANCE_INTERFACE.md">精确加权路线</a>。全部数值已终态；Wiki461是研究记录，不是图数。Goal ACTIVE未完成，人工反馈与完整新图验收要求不变。</p></section>'''
spat=r'<section id="stale-route-current">.*?</section>';assert len(re.findall(spat,t,re.S))==1;old=re.search(spat,t,re.S).group().replace('id="stale-route-current"','id="before-edgevoltage-cooperative-history"',1);t=re.sub(spat,lambda _:section+'\n<details><summary>上一轮快照：补点对照与四系数族检验（历史）</summary>'+old+'</details>',t,count=1,flags=re.S);p.write_text(t);p.with_suffix('.html.txt').write_text(t)
print(json.dumps({'updated_UTC':now,'Goal':'ACTIVE','Wiki':461,'accepted_counts':[153,43,47],'new_target_graphs':0,'all_numeric_terminal':True,'next_parameter':[3,9],'next_started':False},ensure_ascii=False))
