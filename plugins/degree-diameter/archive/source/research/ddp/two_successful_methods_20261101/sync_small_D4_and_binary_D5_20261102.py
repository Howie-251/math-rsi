"""Publish accepted numerical terminals, preserving the existing goal and history."""
from pathlib import Path
from datetime import datetime,timezone
import json,re
B=Path(__file__).resolve().parent;R=B.parents[2]
def load(p):return json.loads(p.read_text())
def save(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
s=load(B/'STAGE_STATE.json');r=load(B/'STALE_FOLLOWUP_ROUND_20261101.json')
assert [s['accepted_total_named_legal_instances'],s['accepted_total_parameter_pairs'],s['complete_concrete_formula_Lean_instances']]==[153,43,47]
receipts=['wiki_sync/SOURCE650_CAPACITY_AND_PROJECTED_TERMINAL_20261102_RECEIPT.json','wiki_sync/D4_BINARY_PAIR_AND_CROSS_CHART_TERMINALS_20261102_RECEIPT.json','wiki_sync/SMALL_D4_TWO_CUT_STAR_COHORT_TERMINAL_20261102_RECEIPT.json','wiki_sync/D5_BASE240_C23_FOUR_COEFFICIENT_TERMINAL_20261102_RECEIPT.json']
actual=[load(B/p) for p in receipts]
assert [(x['records_before'],x['records_after']) for x in actual]==[(456,456),(456,457),(457,458),(458,459)]
ledger=load(R/'research-wiki/DDP_METHOD_LEDGER.json');assert ledger['record_count']==len(ledger['rows'])==459
cases={
 'source252_two_cut_star253':'stale_record_transfer_d5D4/source252_two_cut_star253/',
 'source104ab_two_cut_star105':'stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/',
 'binary240_C23_four_coefficient_cover5520':'stale_record_transfer_d8D5/binary_C30_base240_C23_cover/'
}
for k,d in cases.items():
 item={'directory':d,'root':load(B/d/'ROOT_DISPOSITION.json'),'actual':load(B/d/('CRITICAL_PACKET_RESULT.json' if k.startswith('binary240') else 'RESULT.json')),'new_accepted_graph_parameter_Lean':[0,0,0]}
 if k.startswith('binary240'):item['base_calibration']=load(B/d/'BASE_RESULT.json');item['scope_review']=d+'CRITICAL_PACKET_SCOPE_REVIEW.md'
 s[k]=item;r[k]=item
s['source650_FP_transfer']['later_capacity_and_projected_root']=load(B/'stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_ROOT.json')
r['source650_FP_transfer']=s['source650_FP_transfer']
for k in ['source650_twin_class_capacity','source650_projected_F_cover','binary_D4_controlled_charts']:
 r[k]=s[k]
nextq={'status':'PAPER_INTERFACE_READY_NEXT_SAVED_PATH_QUESTION_NOT_NUMERIC_STARTED','target':[8,5,5520],'directory':cases['binary240_C23_four_coefficient_cover5520'],'question_zh':'固定240底图；先利用已保存66条路线，检验逐实际边电压能打散哪些global-form重复，以及仍有多少不可避免碰撞，再决定一个有预算的小批；不重跑12720四系数族或自动换field/fold/base。','evidence':'同form的paths1/14可由edge{8,104}的反向一致电压扰动分离；这不证明整pair或cover可行。','new_numerics_started':False,'old_timers_resumed':False,'requires_user_approval':False,'target_graph_generated':False,'before_next_numeric':'write concrete prediction,return object,budget and reevaluation node'}
for o in(s,r):
 o['updated_UTC']=now;o['wiki_ledger_rows']=459;o['next_computation_decision']=nextq;o['second_mathematical_question']={'status':'NONE_RUNNING','all_previous_numeric_handles':'TERMINAL; no oldsolver/field/BFS/Lean/reviewrestart'}
for p in receipts:
 if p not in r['wiki_receipts']:r['wiki_receipts'].append(p)
r.update(status='ALL15_TESTED_ZERO_STALE_RECORDS_650_UNKNOWN_SMALLD4_RULES_NO_BINARY_C23_GLOBAL_RULE_NO',new_graphs=0,new_Lean_instances=0,goal_complete=False)
s.update(phase='SMALL_D4_AND_BINARY_D5_TERMINAL_NEXT_EDGE_VOLTAGE_PATH_INTERFACE',current_goal_turn_classification='PROGRESS:650capacitypass/projectedUNKNOWN;237423smallD4configsNO;binaryC23NBcapacitypass but12720globalcoeffNO;0newtargetgraph',jobs_scope='All numerical handles terminal; no solver/BFS/Lean/ARIS running. Three complementary agents supported source/cohort/voltage-scope work; document tasks terminal after publication.',main_lines=['A: one fixedbinary240 base, nextsaved66paths edge-voltage interface; globalfourcoeffC23 completeNO STOP','B: smallD4 two-cutstar source252/104a/104b completeNO STOP;650projectedFcoverUNKNOWN STOPno3rdsolve'])
s['A'],s['B']=s['main_lines']
s['wiki_sync']={'status':'ACTUAL_INCREMENTAL_TERMINALS_COMPLETE_459','receipts':receipts}
s['latest_wiki_sync']={'ledger_rows':459,'receipts':receipts,'records_added_since456':3,'human_top_preserved':True,'full_rebuild_reimport':False,'all_completed_math_synced':True,'new_accepted_graph_parameter_Lean':[0,0,0]}
s['stale_followup_round_20261101']=r
save(B/'STALE_FOLLOWUP_ROUND_20261101.json',r);save(B/'STAGE_STATE.json',s)
block=f'''<!-- AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->
### {now} 当前执行：15老题清单已试；补点两类障碍对照、C23全局电压NO，0新纪录

同一Goal ACTIVE，不新建Goal/重导Wiki/重启研究。153合法named版本／43参数／47具体Lean继承；本次0新目标图/参数/Lean，15老格本轮均已有新检验但0新纪录。清单14格至少10年＋2018备选、8格原范围；经典Moore差11.1%–88.7%不表示可实现。11月2日02:10 UTC实读当前主表15阶数均未变。唯一Wiki实际459研究记录，不是图/方法数；650原node原位、D4binary/smallD4/D5binary各一node，人工顶块保留、不fullrebuild。

(10,3)650 FP转移：旧1170binary唯一20秒UNKNOWN原样保留。新8385个starP对容量upper全过、min surplus46；首实际argmax八packet仍漏29，不是可行见证。K8,2整数精确投影650binary/652rows/50440nnz，唯一18秒HiGHS仍UNKNOWN/noincumbent。final42.416193092/45 CPU STOP，不第三solve/seed；donor/PPpairing/651graph/BFS均未进入，不能说这些后阶段失败或整族NO。

D4二元C192：identity五distinctdirection与真实bar不兼容；legalidentity零offset只能span≤3，断连。两实际inversechart的same-fibre全192×16满覆盖；改M0修0→1从8→16，却新0→3只并12/14，全部192controller根仍有cross失败。只关闭两个固定chart，不排全部binary；final1.233294418/10，STOP不第三matrix/field。旧cap15/15553的648freepin任意R3-cover MILP/SAT UNKNOWN只继承、不重算。

smallD4受控对照：Rajiv252/5reg的全部195615个两不交cut＋四端点新星配置，新根最多覆盖222/252、0过门；Bhakar104 unlettered(alias a)/b各20904完整配置，新根过门16/24却全部oldold失败。首a旧0→19、b旧0→22源距4变5，保存actual反例。合237423是参数数，不是非同构图；104c旧同规则20904NO继承不重跑。只有固定sources/此规则NO，一般253/105或其他删改开放。252批CPU 2.151099672/10，104ab .574206988/10，均STOP不第三cut/seed。

D3技巧迁移(8,5)：真实C30/F2³ ARC图生成240点/960边、全8reg，唯一240根得D4，是校准底图不计目标成果。普通C23 cover若成5520>saved/live主表5334。全部basepair NB≤5最少66、无低于23；最紧8→70按长度3/4/5为1/10/55。随后先保存PRED：至少23forms且存在全23phase参数；实际66paths→26四系数forms支持前者，全12720first-nonzero1规范参数最多22/23、0幸存推翻后者。故这个固定base/四globalcoeff C23族完整NO，STOP；不排逐边voltage、其它ordinarycovers或一般8D5。samecase1.496812969/5 CPU；没有5520图/solver/Lean/ARIS。PAPER_INTERFACE和CRITICAL_PACKET_SCOPE_REVIEW支持精确scope。

下一唯一问题是读取已保存66paths的逐实际边电压接口：同form paths1/14可由edge{{8,104}}电压扰动分离，不能据此声称整pair/cover可行。先查哪些碰撞不可避免，再对明确问题另写有限预测/预算；尚未启动新数值，不需用户批准普通研究，不自动换base/fold/field或恢复旧timer。所有实际数值已terminal，无solver/BFS/Lean/远审在途；三互补代理做源/对照/电压范围反馈，没有另扩独立模板清单。

此前4D5全196371 Hall NO、C32/C33 controller族NO、K19三个SAT窗口UNKNOWN、672/1100rightmatching NO、1250两规则NO、two6804任意crossmatchingNO均继承不重跑。旧N(8,2)/n61继续暂停；已有16416完整独验/Lean/A+B+distinctC/专家包保留。全球优先权认证0、人工反馈和完整新图最终验收要求不变。STATE/ROUND嵌入一致；progress与candidate HTML/源码/CSV同步。本阶段不以文档、校准底图或认识冒新纪录，Goal未完成；不hash/安装/付费重试。
<!-- /AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->'''
pat=r'<!-- AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->.*?<!-- /AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->'
for rel in ['AGENTS.md','context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md','context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md','research/ddp/two_successful_methods_20261101/REPORT.md']:
 p=R/rel;t=p.read_text();assert len(re.findall(pat,t,re.S))==1;p.write_text(re.sub(pat,lambda _:block,t,count=1,flags=re.S))
p=R/'research/progress.html';text=p.read_text();text=re.sub(r'<p>更新 [^<]+</p>',f'<p>更新 {now}。同一Goal ACTIVE；旧N(8,2)/n61任务继续暂停。</p>',text,count=1)
latest=f'''<section id="stale-route-current">
<h2>当前：15项老题清单与新一轮补点／D3迁移检验</h2>
<div class="note"><strong>本次0张新增达标图；全项目仍153合法版本／43参数／47具体Lean。</strong><p><a href="stale_record_candidates.html">15项清单、年份、Moore空间与每项已试方法</a> · <a href="stale_record_candidates.html.txt">清单HTML源码</a> · <a href="stale_record_candidates.csv">CSV</a> · <a href="progress.html.txt">本页HTML源码</a>。这15格一般问题均开放；已有16416完整成果另列原交付，不混计本轮老题结果。</p></div>
<table><thead><tr><th>具体问题</th><th>预测与检验</th><th>下一动作</th></tr></thead><tbody>
<tr><td>(10,3)650→651：八FP删边的覆盖是否可行</td><td>8385starP对容量上界全过，不能排除；650变量精确投影唯一18秒仍UNKNOWN，无incumbent</td><td>累计42.416/45CPU停止；不第三solve/seed，不把UNKNOWN写NO</td></tr>
<tr><td>(5,4)252→253：两不交cut＋四端点新星</td><td>完整195615配置，新根最多222/252，0过门</td><td>关闭此固定源规则，不加第三cut续试</td></tr>
<tr><td>(4,4)两个104源→105：同规则对照</td><td>各20904配置，新根过门16／24，但全部破坏旧点距离，0完整图</td><td>区别新根缺路线与旧路线损伤；该规则停止，104c旧NO不重跑</td></tr>
<tr><td>(10,4)C192二元路线互补</td><td>改M0保同层覆盖并修0→1的8→16，却新0→3仅12或14/16，两chart均不成</td><td>局部修好不冒全局优势，停止两固定chart</td></tr>
<tr><td>(8,5)D3二元技巧＋C23普通覆盖，目标5520</td><td>240点校准底图8正则/D4；最紧pair66条NB短路/26forms，全12720全局电压最多22/23层</td><td>路线容量预测支持、电压可同时实现预测反驳；关闭四系数族，逐边电压仍开放</td></tr>
</tbody></table>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_NOTE.md">650的UNKNOWN</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d5D4/source252_two_cut_star253/NOTE.md">252补点</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/NOTE.md">104对照与反例</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D5/binary_C30_base240_C23_cover/NOTE.md">D3→D5的预测和实际</a>。</p>
<p>下一步只研究保存的66条路线在逐边电压下的重复：已有具体同form路径可由单边扰动分离，但还不能保证全部23层或完整5520图。所有数值已终态，未自动开展另一轮参数筛选；旧严格排除不重跑。Wiki459条是研究记录，不是图数，人工意见保留；Goal ACTIVE未完成。</p>
</section>'''
spat=r'<section id="stale-route-current">.*?</section>';assert len(re.findall(spat,text,re.S))==1
old=re.search(spat,text,re.S).group().replace('id="stale-route-current"','id="before-smallD4-binaryD5-history"',1)
text=re.sub(spat,lambda _:latest+'\n<details id="before-smallD4-binaryD5-snapshot"><summary>上一轮快照：联合Hall与binary controller检验（历史）</summary>\n'+old+'\n</details>',text,count=1,flags=re.S)
p.write_text(text);p.with_suffix('.html.txt').write_text(text)
recheck=B/'public_baseline_audit/STALE_MAIN_TABLE_RECHECK_20261102.json';d=load(recheck);d['latest_web_open_UTC']='2026-11-02 02:10:08 UTC';d['latest_web_open_URL']='https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html';d['latest_web_15_orders_unchanged']=True;save(recheck,d)
print(json.dumps({'updated_UTC':now,'wiki_records':459,'accepted_counts':[153,43,47],'new_target_graphs':0,'all_numeric_terminal':True},ensure_ascii=False))
