"""Publish the already-accepted Hall and binary-interface terminal state locally."""
from pathlib import Path
from datetime import datetime,timezone
import json,re
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[2]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads(p.read_text())
def save(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
s=read(BASE/'STAGE_STATE.json');r=read(BASE/'STALE_FOLLOWUP_ROUND_20261101.json')
receipts=['wiki_sync/NATURAL364_ALL_TWO_CORECUTS_HALL_TERMINAL_20261102_RECEIPT.json','wiki_sync/BINARY_MULTIROUTE_PACKETS_AND_CONTROLLER_FAMILIES_20261102_RECEIPT.json']
rec=[read(BASE/x)for x in receipts]
assert [(x['records_before'],x['records_after'])for x in rec]==[(455,455),(455,456)]
A='stale_record_transfer_d4D5/port_matching_core2_star365/'
B='stale_record_transfer_d8D3/controller32_F2_multiroute_readgate/'
N='stale_record_transfer_d10D3/fp_endpoint_transfer651/'
hall=read(BASE/A/'all_two_corecut_Hall_gate/ROOT_DISPOSITION.json')
binary=read(BASE/B/'ROOT_DISPOSITION.json')
nextread=read(BASE/N/'NEXT_STRUCTURAL_READ_GATE.json')
old650=read(BASE/N/'ROOT_DISPOSITION.json')
s['source364_all_two_corecut_Hall']['root_disposition']=hall
r['source364_core2_star365']['later_complete_two_corecut_Hall']=s['source364_all_two_corecut_Hall']
r['source364_core2_star365']['current_scope_status']='COMPLETE_WHOLE_TWO_CORECUT_PORTMATCHING_STAR_RULE_NO'
z={'directory':B,'status':binary['status'],'root_disposition':binary,'actual_packet_result':read(BASE/B/'adjacent_packet_controlled_test/RESULT.json'),'actual_repair_result':read(BASE/B/'conjugate_route_repair/RESULT.json'),'C32_point_result':read(BASE/B/'typed_C30_to32_twochart_insertion/RESULT.json'),'C32_capacity_stage1':read(BASE/B/'typed_C30_to32_twochart_insertion/BASE_CAPACITY_RESULT.json'),'C32_capacity_stage2':read(BASE/B/'typed_C30_to32_twochart_insertion/CAPACITY_SURVIVOR_RESULT.json'),'C33_point_result':read(BASE/B/'uniform_triangle_C33_C11/RESULT.json'),'C33_projection_postprocess_path':B+'uniform_triangle_C33_C11/PROJECTION_POSTPROCESS.json','scope_review_path':B+'B_FAMILY_TERMINALS_SCOPE_ATTACK.md','new_graph_parameter_Lean':[0,0,0]}
s['binary_multiroute_and_controller_families']=z;r['binary_multiroute_and_controller_families']=z
s['source650_next_structural_read']=nextread;r['source650_next_structural_read']=nextread
nextdecision={'status':'READY_ONE_SAVED_COEFFICIENT_TWIN_CLASS_CAPACITY_DIAGNOSTIC_AUTHORIZED_NOT_STARTED','target':[10,3,651],'directory':N+'twin_class_packet_capacity_gate/','question_zh':'转(10,3) actual650源，只用保存覆盖系数，按65个双胞类的0/1/2 donor配额做八packet容量上界；检验哪些two-starP choices尚未被路线容量排除。','input_read_gate':N+'NEXT_STRUCTURAL_READ_GATE.json','inputs':[N+'FP_MODEL.json',N+'FP_MODEL_MATRIX.npz','research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/STRUCTURE_ROOT.json'],'source_or_A2_A3_rechecks':0,'solver_calls_allowed':0,'old_20second_window':'TERMINAL_UNKNOWN_NO_INCUMBENT_NOT_RESUMED','samecase_CPU_prior':old650['wholecase_CPU_seconds'],'new_read_CPU':.25,'new_preparation_allowance_CPU':.2,'new_native_CPU_budget':10,'samecase_CPU_cap':45,'new_numerics_authorized':True,'started':False,'return_object':'per-starPpair bound/quota/witness; ifa boundfailsnotactualcover; survivor isUNKNOWN notcandidategraph','if_loose_or_nohit':'STOP_REASSESS; noautomaticMIP/extraFPcuts/seed','prediction_to_test':'at leastone starPpair passes groupedcapacity necessary upper; notactualcover','sole_numeric_owner_next':'root'}
s['next_computation_decision']=nextdecision;r['next_computation_decision']=nextdecision
for o in(s,r):
 o['updated_UTC']=now;o['wiki_ledger_rows']=456;o['second_mathematical_question']={'status':'NONE_RUNNING','reason':'Hall architecture and binary controllerfamilies allnumericterminal; onlyone650cached-data diagnostic ready'}
s['phase']='HALL_AND_BINARY_FAMILIES_TERMINAL_NEXT_D10D3_TWIN_CLASS_CACHED_CAPACITY'
s['current_goal_turn_classification']='PROGRESS: actualfixedPpredictionrefuted24vs1/full196371HallNO; binaryactualrank2unionandcontrolledloss;C32/C33familycapacityNO;0newgraph'
s['main_lines']=['A: next10D3source650savedcoefficient/twinclasspacketcapacity, solefinite10CPUdiagnosticready notstarted;no oldsolver/sourceBFS','B: actualbinaryadjacentcoveragevalidated;twofixedcontrollerfamiliesclosedbyroutecapacity/projection;STOPnogroup/field/controller-size ladder']
s['A']=s['main_lines'][0];s['B']=s['main_lines'][1]
s['jobs_scope']='No numeric/solver/BFS/Lean/reviewrunning; allactualhandles terminal; new650diagnosticauthorizednotstarted; nooldtimerrecovery'
s['wiki_sync']={'status':'ACTUAL_INCREMENTAL_HALL_UPSERT_AND_BINARY_NODE_COMPLETE_456','receipts':receipts}
s['latest_wiki_sync']={'ledger_rows':456,'receipts':receipts,'records_added_this_goalturn':1,'A_updated_in_place':True,'human_top_preserved':True,'full_rebuild_reimport':False,'all_completed_math_synced':True,'new_graph_parameter_Lean':[0,0,0]}
r['status']='ALL15_TESTED_ZERO_RECORDS_NEW_D4D5_WHOLE_HALL_NO_BINARY_LOCAL_COVERAGE_POSITIVE_CONTROLLER_FAMILIES_NO_NEXT_D10D3'
r['new_graphs']=0;r['new_Lean_instances']=0
for x in receipts:
 if x not in r['wiki_receipts']:r['wiki_receipts'].append(x)
s['stale_followup_round_20261101']=r
save(BASE/'STALE_FOLLOWUP_ROUND_20261101.json',r);save(BASE/'STAGE_STATE.json',s)
block=f'''<!-- AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->
### {now} 当前执行：4D5整个两corecut机制NO；binary实际联合覆盖成立但两controller族NO；下一10D3保存系数容量门

同一Goal ACTIVE，上一Goalturn为PROGRESS（K19实际预测/UNKNOWN与两个rightmatching全域NO改变下一动作），本turn亦PROGRESS，不新Goal/重导Wiki/重读handoff/重启旧队列。当前153合法版本／43参数／47具体Lean，本turn0新图/参数/Lean；15老格本轮全有新检验但0老格新纪录。14格至少10年＋2018备选、8格在原范围；11月2日主表15阶数一致，Moore差11.1%–88.7%不保证存在。唯一Wiki实际456研究记录，不是图/方法数；A旧node原位455保持，B一新node455→456。人工顶块保留，无fullrebuild。

A (4,5)自然364/714：固定首P43/58/151/314联合matching预测被4个新深4支持反驳，24个β2-holeowner却仅nearport126可作mate。由此改问完整Hall域：原630core边的全部196371个unordered不交cutpairs全检，复用4支持补332深4支持，每P hardowner21..27、near0..2，min差20、0幸存。必要注入条件排整个fixedsource“两原corecuts＋28port任意perfectmatching＋四端点新星”规则，0matching/365graph/oldrootBFS；原10000样本UNKNOWN/raw费用保历史，不排其它删改或一般365图。三个nestedHall计数的精确newroot接口已paper接受。finalsamecase3.913081991/20CPU，全STOP不加第三cut/seed。

B (8,3)真实multiroute：旧197568只排36约化三词各自rank3，不关多route并。实际C30 pair0→18，两套completeinverse F2chart、全部8source坐标：ARC三rank2packet并满8，合法COLLINEAR并6/全部9短路并7，真实互补被支持，非自由拼plane或仅x0。定向改B使唯一021的0→5从4→8且adj保8，却修4conjugate同时损4cyclic词；goodword24→28预测反驳，实际都24。不拿局部修好冒整体优势。

理解改变B生成器：typedC30插两点全378450参数/284310simple，ARC/R两chart全失败于新root30；ordinary全walk加权容量保存行诊断283388 min0＋907 min4＋15 min8（‘root30全不足’预测被15例反驳）；这15再只查root31全min0。故该插边族所有8fiber/每typedstep≤2choice提升均NO，不能说907个base本身D>3。改为11三角单元C33/C11，固定ARC保003/030/300闭route，100规范代表覆盖1000raw非零参数；同层fibre全部实测pass，仍每参数至少一type-root三步到不了全部33，projection0存活/max minreach32。因此这三型C11controller族本身D>3，任何投影提升都不能D3。两族STOP不m12/其它chart/field梯。Cayley32两globalinversepair接口另有商kernel8/≤3最多5及cyclic25<32纸面NO，不排一般C32。Bfinalsamecase5.653785158/30CPU；原read1.6较计划1.5多.1如实保留。0完整图/图BFS/Lean/ARIS/solver；实际源/生成码/全部scope在controller32_F2_multiroute_readgate/NOTE及ROOT。

下一唯一A转(10,3) actual650/3250：旧1170binary模型唯一20秒无incumbent仍UNKNOWN、累计22.084731374/45，0prototype/15repair/BFS。新READ_GATE实际完成：65组Ptwins/每组8F；FP选择可精确投影为650binary/652rows，非新生成规则。已有PP边的underdegree9分支已实现但未运行、不能改变F-cover。已授权下一单cached-coefficient诊断（尚未START）：只用FP_MODEL/NPZ的520coverage rows＋twinlabels，按class0/1/2donor和总8做packet最大union容量DP，two-starP给class最低quota；跨类重叠有利忽略，所以upper不足可排starPair，上界通过仅UNKNOWN不是651图。native cap10，原45samecase加read.25/prep.2不清零；不源/A2重算、不续MIP、不自动加FPcuts/seed。入口STATE.next_computation_decision，不需用户逐次批准普通研究。

先前K19 full/frozenSAT60/20/5秒仍UNKNOWN，96.356641619/100已STOP，旧H342域NO不扩它；Sampels672全部rightmatchingNO、Loz1100全部rightmatchingNO、1250两完整规则NO、two6804任意crossmatchingNO均继承不重跑。所有旧/本turn数值及review handles终态；最多两主问，目前只有650准备就绪，无live solver/BFS/kernel/外审。旧N(8,2)/n61继续暂停；已有16416完整独验/Lean/A+B+distinctC/专家包保留，全球优先权认证0及人工反馈/完整新图最终验收要求不变。STATE/ROUND嵌入一致；progress与candidate HTML/源码/CSV由最终builder同步。文档/认识不计新纪录，Goal未完成；不hash/安装/付费重试。
<!-- /AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->'''
pat=r'<!-- AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->.*?<!-- /AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->'
for rel in ['AGENTS.md','context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md','context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md','research/ddp/two_successful_methods_20261101/REPORT.md']:
 p=ROOT/rel;t=p.read_text();assert len(re.findall(pat,t,re.S))==1
 p.write_text(re.sub(pat,lambda _:block,t,count=1,flags=re.S))
p=ROOT/'research/progress.html';text=p.read_text()
text=re.sub(r'<p>更新 [^<]+</p>',f'<p>更新 {now}。同一Goal ACTIVE；旧N(8,2)/n61任务继续暂停。</p>',text,count=1)
spat=r'<section id="stale-route-current">.*?</section>'
old=re.search(spat,text,re.S).group()
latest=f'''<section id="stale-route-current">
<h2>当前：联合端口规则完整排除；二元域路线互补已实测，尚无新图</h2>
<div class="note"><strong>本轮0张新增完整图；仍153合法版本／43参数／47具体Lean实例。</strong><p>15项老题均有本轮检验，仍0老题新增达标图。<a href="stale_record_candidates.html">15项完整清单与最新范围</a> · <a href="stale_record_candidates.html.txt">清单HTML源码</a> · <a href="progress.html.txt">本进展页HTML源码</a>。下面的局部覆盖与完整族排除分别记账。</p></div>
<h3>(4,5)：随机样本UNKNOWN之后，实际关闭整个两corecut规则</h3>
<p>原10000随机配置的失败保为历史。新问题是：固定四个新点接点后，能否协调全部28个端口的配对？精确路线条件把它化为三个nested Hall数量条件。固定首P发现24个缺点类必须使用唯一近端口，预测被反驳。随后全部196371种不交corecut对均有至少21个β2缺口类，却最多2个入口，0幸存。因此自然364源“两corecuts＋任意portmatching＋四端点新星”的整个规则NO，无须生成365图或检查旧根。</p>
<p>21来自完整有限数据，不包装为一般几何定理；其它源、其它删改和一般365图仍开放。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365/all_two_corecut_Hall_gate/FINAL_PROOF.md">预测、完整证明与停止范围</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365/JOINT_PORT_HALL_PAPER.md">三个Hall条件</a>。</p>
<h3>(8,3)：真实路线能互补；局部修好也会损伤另一类路线</h3>
<table><thead><tr><th>具体检验</th><th>预测与实际</th><th>如何改变下一步</th></tr></thead><tbody>
<tr><td>已有C30边0→18，三条rank2 packet，全部8个源坐标</td><td>ARC并满8；合法COLLINEAR只并6，全部9短路也只并7。两套完整可逆</td><td>保留四arc噪声方向，邻层可由真实联合覆盖保证，不强迫每词单独rank3</td></tr>
<tr><td>唯一0→5三步词021，定向改B</td><td>4→8、邻层保8；同时修4conjugate词、损4cyclic词。24→28预测被推翻，实际同24</td><td>不把局部修好或goodword计数当整体优势，需联合选拓扑与映射</td></tr>
<tr><td>C30插两点：378450参数／284310simple</td><td>两chart全No；容量诊断排284295，15幸存又全败于第二新根</td><td>该插点族任意8fiber/≤2choice规则都NO，继续调矩阵无用</td></tr>
<tr><td>11三角单元C33/C11：100规范代表</td><td>同层fibres全pass，但100个basecontroller均有type-root三步到不了全33点</td><td>这个三型C11拓扑族本身D&gt;3，停止，不再换chart或m12续试</td></tr>
</tbody></table>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/controller32_F2_multiroute_readgate/NOTE.md">全部输入、预测、实测与未排范围</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/controller32_F2_multiroute_readgate/B_FAMILY_TERMINALS_SCOPE_ATTACK.md">互补代理范围检查</a>。32点Cayley的两globalinversepair接口另有商空间阻碍；非Cayley控制器及一般8D3没有被关闭。当前0张256或264候选图。</p>
<h3>下一项：(10,3)的650源，只做保存系数的结构诊断</h3>
<p>已有八FP cuts模型唯一20秒窗口无incumbent，仍UNKNOWN。新读取确认65个双胞类可消去重复donor分配，但保留已有PP边的分支不能绕开F-cover。下一已授权单一10CPU容量门、尚未启动：用保存的覆盖系数按每类0/1/2donor配额选择八packet，判断two-starP choices的必要上界；不重源图/A2，不续旧MIP，也不先试repair配对。通过上界仍不是651图。</p>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/NEXT_STRUCTURAL_READ_GATE.md">具体预测、公式、最小数据与旧scope</a>。全部在途数值已终态；已有16416交付、旧K19未知与其它严格排除均继承，不重跑。Wiki456条是研究记录，不是图数，人工意见保留；Goal ACTIVE未完成，全球优先权认证仍0。</p>
</section>'''
history=old.replace('id="stale-route-current"','id="before-joint-port-binary-history"',1)
text=re.sub(spat,lambda _:latest+'\n<details id="before-joint-port-binary-snapshot"><summary>上一轮快照：匹配族终态与当时4D5联合端口尚未检验（历史）</summary>\n'+history+'\n</details>',text,count=1,flags=re.S)
p.write_text(text);p.with_suffix('.html.txt').write_text(text)
print(json.dumps({'updated_UTC':now,'wiki_records':456,'counts':[s['accepted_total_named_legal_instances'],s['accepted_total_parameter_pairs'],s['complete_concrete_formula_Lean_instances']],'new_graphs':0,'next650_started':False,'next650_native_budget':10},ensure_ascii=False))
