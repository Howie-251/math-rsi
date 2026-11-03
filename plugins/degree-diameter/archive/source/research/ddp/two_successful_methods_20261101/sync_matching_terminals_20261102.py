"""Sync actual terminal artifacts; preserve research history and the single Wiki."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
STATE = BASE/'STAGE_STATE.json'
ROUND = BASE/'STALE_FOLLOWUP_ROUND_20261101.json'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def read(p):
    return json.loads(p.read_text())

def save(p,o):
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')

receipts = [
 'wiki_sync/K19_EXACT_POINT_AND_ASSIGNMENT_SHIFT_TERMINAL_20261102_RECEIPT.json',
 'wiki_sync/SOURCE672_RIGHTMATCHING_FULL_DOMAIN_TERMINAL_20261102_RECEIPT.json',
 'wiki_sync/LOZ1100_ALL_RIGHTMATCHINGS_TERMINAL_20261102_RECEIPT.json',
 'wiki_sync/NATURAL364_JOINT_PORT_INTERFACE_READ_20261102_RECEIPT.json']
rr=[read(BASE/x) for x in receipts]
assert [(x['records_before'],x['records_after']) for x in rr] == [(452,453),(453,454),(454,455),(455,455)]
ledger=rr[-1]['records_after']
s=read(STATE);r=read(ROUND)
paths={
 'source672_right_matching1344':'stale_record_transfer_d8D4/two672_right_matching1344',
 'source1100_right_matching2200':'stale_record_transfer_d9D4/two1100_right_matching2200'}
for key,d in paths.items():
    case={'directory':d+'/', 'status':read(BASE/d/'ROOT_DISPOSITION.json')['status'],
          'actual_result':read(BASE/d/'RESULT.json'),
          'root_disposition':read(BASE/d/'ROOT_DISPOSITION.json'),
          'new_graph_parameter_Lean':[0,0,0]}
    if key.startswith('source672'):
        case['saved_row_phase_diagnostic']=read(BASE/d/'PHASE_COMPATIBILITY_DIAGNOSTIC.json')
    else:
        case['phase_capacity']=read(BASE/d/'PHASE_CAPACITY.json')
        case['actual_phase_maxima']=read(BASE/d/'PHASE_ACTUAL_MAXIMA.json')
    s[key]=case;r[key]=case
jp='stale_record_transfer_d4D5/port_matching_core2_star365/JOINT_PORT_INTERFACE_READ.json'
j=read(BASE/jp)
next_decision={
 'status':'JOINT_PORT_INTERFACE_READ_COMPLETE_NO_NEW_NUMERICAL_BATCH_AUTHORIZED',
 'target':[4,5,365], 'directory':'stale_record_transfer_d4D5/port_matching_core2_star365/',
 'question_zh':'回到(4,5)的364→365保存对象，先判断能否把28个余度端口的配对与新星点覆盖联合设计；不续随机样本或旧solver。',
 'actual_read_gate':j,
 'read_gate_path':jp,
 'old_status':'10000sample_nohit_isUNKNOWN_notwholefamilyNO',
 'new_numerics_authorized':False,
 'no_automatic_old_seed_solver_source_helper_ladder':True}
for obj in (s,r):
    obj['updated_UTC']=now
    obj['next_computation_decision']=next_decision
    obj['wiki_ledger_rows']=ledger
    obj['second_mathematical_question']={'status':'NONE_RUNNING','reason':'AllK19/source672/source1100numericterminal;onlyonejointportreadinterface;max2mainquestions'}
for rel in receipts:
    if rel not in r['wiki_receipts']:r['wiki_receipts'].append(rel)
for key in ['source684_K19_matching_interface','source672_right_matching1344','source1100_right_matching2200']:
    record={'key':key,'status':s[key]['status'],'directory':s[key]['directory']}
    if not any(x.get('key')==key for x in r['completed_computation_decisions']):
        r['completed_computation_decisions'].append(record)
r['status']='ALL15_OLD_CELLS_TESTED_ZERO_RECORDS_K19_UNKNOWN_TWO_RIGHTMATCHING_FAMILIES_NO_NEXT_D4D5_JOINT_PORT'
r['new_graphs']=0;r['new_Lean_instances']=0
s['phase']='MATCHING_FAMILIES_TERMINAL_NEXT_OLD_D4D5_JOINT_PORT_INTERFACE'
s['current_goal_turn_classification']='PROGRESS: actualK19predictionrefutation and exactpointSATUNKNOWN; source672/source1100completefiniteNO withphasebottlenecks; no newgraph'
s['main_lines']=['A:15staleparametercells alltested, zero records; next4D5 saved364jointport coverage interface, numericalbatch notyet authorized','B:no secondmajorquestion; K19UNKNOWN and672/1100rightmatchingfullNO allSTOP']
s.setdefault('prior_line_summaries_before_matching_20261102', {'A':s['A'],'B':s['B']})
s['A']='Next4D5jointportmatching/star: readsaved364failure, useoneexactcoverprediction; no oldrandom/solver continuation authorized.'
s['B']='D3small-degree literal4q/30q^3 belowpublicbounds; matching alternatives testedprecisely and stopped; no secondmajorquestionrunning.'
s['jobs_scope']='No live numeric solver/BFS/formal/review; allthreecurrentcases terminal; one4D5 readinterface complete. Oldjobs neverrestarted.'
s['wiki_sync']={'status':'ACTUAL_INCREMENTAL_TERMINAL_SYNC_COMPLETE_455','receipts':receipts}
s['latest_wiki_sync']={'ledger_rows':ledger,'receipts':receipts,'records_added_in_this_current_matching_continuation':3,'new_graph_parameter_Lean':[0,0,0],'all_completed_numerics_synced':True,'human_top_preserved':True,'full_rebuild_reimport':False}
s['long_stale_main_priority_revision_20261101']['last_current_order_recheck']='public_baseline_audit/STALE_MAIN_TABLE_RECHECK_20261102.json'
s['long_stale_main_priority_revision_20261101']['latest_actual_status']=r['status']
r['source364_core2_star365']['joint_port_interface_read']=j
s['stale_followup_round_20261101']=r
save(ROUND,r);save(STATE,s)

block=f'''<!-- AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->
### {now} 当前执行：15格清单与有限迁移已实际检验；K19未知，两rightmatching族NO；回到4D5联合端口接口

同一Goal ACTIVE，不新Goal/重导Wiki/重读handoff/重启旧队列。当前153合法版本／43参数／47具体Lean，本次0新图/参数/Lean；15老格均有本轮新检验但0老格新纪录。14格至少10年＋2018备选，原范围占8格；11月2日在线主表15阶数均未变，经典Moore余量11.1%–88.7%不是可实现承诺。唯一Wiki实际455研究记录（452→453K19→454S672→455Loz1100），不是方法/成果数；三数值receipt及一读门原位receipt见STATE，人工top保留，无fullrebuild。

(8,4)/1368 K19实际端点模型已完成三个SAT窗口60/20/5秒，均UNKNOWN；一次assignment容量min19只是必要条件。28→28紧行可在5DFS节点独立铺满19，推翻局部不可实现预测，不保证共享36shifts全局兼容。2603entailed二元约束后仍UNKNOWN；samecase96.356641619/100CPU已STOP，不能继续原timer/换sigma或冒NO。旧H342全233928域NO仍只限旧更小域。正例fresh脚本仅草稿0运行。

(8,4)/1344：actualpublishedSampels672 RIGHT source已恢复，identity闭R4=672只是源复现不计新图。全672个M(h)=h*t匹配精确U_t均不满；保存行诊断原‘各phase可单满但pair冲突’预测被反驳，六phase各自max106/112且0局部满。固定源全部leftH-equivariant族NO，不任意matching/general8D4。case1.645124787/10CPU含读门/准备/诊断/root，旧684/K19重跑0，0candidateBFS/Lean/ARIS，STOP无otherS/action/window。

清单外(9,4)/2200：actualLoz1100 RIGHT C20作用2/Z55，沿用原S8与R3缓存426，保两copy8800旧边＋1100rightmatching。相位endpoint-pairs容量最小66≥55，P1容量不足预测被反驳；全1100t真实U_t均失败，P2存在预测被反驳。relativephase10 max43/55（首t115），候选66至少23重复映像、至少12缺点；66不是独立NB路线数。只排fixedsource等变匹配，不任意matching/改旧边/一般9D4。case1.695619759/10，0图/BFS/Lean/ARIS；不增15老格计数，停止copy/rightmatching梯。

下一唯一问题回到(4,5) actual364→365保存样本，JOINT_PORT_INTERFACE_READ已实际完成，机器入口为STATE.next_computation_decision；问联合28余度portmatching与star能否改变覆盖，不把原10000样本UNKNOWN变整族NO。当前无新数值批授权，不恢复随机seed/旧solver或自动扩cut/helper/source。下一批须先针对读门的一个具体预测与最小数据定预算；普通研究无需逐次问用户。最多两数学主问保留。

1250三cut移端口11178及三matchingcuts/K1,3完整1743779域、two6804任意crossmatching点球重叠NO均继承，不重跑；其一般参数未排。旧N8/n61暂停。153/43/47与已有16416完整独验/Lean/A+B+distinctC/专家包不变，全球优先权认证0、humanfeedback及最终完整图要求保留。STATE/ROUND嵌入一致，HTML/源码/CSV以最终builder同步；文档更新不计数学成果。不hash/安装/付费重试，Goal未完成。
<!-- /AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->'''
for rel in ['AGENTS.md','context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md','context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md','research/ddp/two_successful_methods_20261101/REPORT.md']:
    p=ROOT/rel;t=p.read_text();pat=r'<!-- AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->.*?<!-- /AVAILABLE_PIN_EXTENSION_20261101_CURRENT -->'
    assert len(re.findall(pat,t,re.S))==1,rel
    p.write_text(re.sub(pat,lambda _:block,t,count=1,flags=re.S))

p=ROOT/'research/progress.html';text=p.read_text()
text=re.sub(r'<p>更新 [^<]+</p>', f'<p>更新 {now}。同一Goal ACTIVE；旧D2/n61任务继续暂停。</p>',text,count=1)
pat=r'<section id="stale-route-current">.*?</section>'
old=re.search(pat,text,re.S).group()
latest=f'''<section id="stale-route-current">
<h2>15项老题与Moore空间：已实际试验，新增达标图仍为0</h2>
<p><a href="stale_record_candidates.html">15项清单、年份、Moore差与逐项方法</a> · <a href="stale_record_candidates.html.txt">可交专家的完整HTML源码</a> · <a href="stale_record_candidates.csv">CSV</a>。11月2日实读主表，15项点数与清单一致；14格至少约10年，另1格2018年备选。经典Moore余量11.1%–88.7%，不是可实现点数承诺。</p>
<table><thead><tr><th>问题与预测</th><th>实际检验</th><th>下一步判断</th></tr></thead><tbody>
<tr><td>(8,4)/1368：放宽到K19的36轨道匹配；紧行是否自身不可实现</td><td>60/20/5秒SAT均UNKNOWN；紧行可铺满19，局部不可实现预测被反驳。累计96.357/100CPU</td><td>停止原窗口；全局共享shift仍未知，不能写NO</td></tr>
<tr><td>(8,4)/1344：两份672的全部rightmatching；各层能否单独满覆盖</td><td>672参数全失败；六phase各max106/112，0局部满。case1.645/10CPU</td><td>固定源此族NO，单层覆盖不足；不推广到任意matching</td></tr>
<tr><td>清单外(9,4)/2200：两份1100的全部rightmatching</td><td>1100参数全失败；phase10候选对66、真实最多43/55。case1.696/10CPU</td><td>候选路线映像重复；停止该族，不继续优化坏对</td></tr>
</tbody></table>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/K19_exact_matching_interface/NOTE.md">K19模型、预测与未知边界</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/NOTE.md">672完整域与相位诊断</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/NOTE.md">1100完整域与重复覆盖瓶颈</a>。</p>
<p><strong>理解如何改变下一步：</strong>不再继续双副本等变匹配梯。回到老格(4,5)的364→365保存对象，先判断能否联合设计端口配对与新星点覆盖。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365/JOINT_PORT_INTERFACE_READ.md">针对性读取门</a>已完成；下一数值批尚未授权，不续原10000随机样本或旧solver。原样本只支持UNKNOWN，不支持整族失败。</p>
<p>D3原4q／30q³模板在8–11度最多q=2、名义240点，低于对应主表；直接换field不能改进。此前1250星形与6804任意跨匹配排除继续保留，均不等于一般参数无解。</p>
<p><strong>当前本次0新增图／参数／Lean；仍153合法版本／43参数／47具体Lean。</strong>三名互补代理参与机制纸面、保存结果诊断及Wiki增量，所有数值已终态。唯一Wiki{ledger}条研究记录，非成果数；人工意见顶块保留。已有16416完整成果与专家包继承，全球优先权认证仍0；Goal ACTIVE未完成。</p>
</section>'''
history=old.replace('id="stale-route-current"','id="before-k19-0014-history"',1)
replacement=latest+'\n<details id="before-k19-0014-snapshot"><summary>00:14快照：1250、6804及当时K19尚未启动（历史）</summary>\n'+history+'\n</details>'
text=re.sub(pat,lambda _:replacement,text,count=1,flags=re.S)
p.write_text(text);p.with_suffix('.html.txt').write_text(text)
print(json.dumps({'updated_UTC':now,'wiki_records':ledger,'counts':[s['accepted_total_named_legal_instances'],s['accepted_total_parameter_pairs'],s['complete_concrete_formula_Lean_instances']],'round_cells':len(r['shortlist_cells_tested_this_round']),'new_graphs':0,'next_numerics_authorized':False},ensure_ascii=False))
