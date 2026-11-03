"""One frozen-source nonorbit clone node; no math rerun or page rebuild."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import json
import re
import runpy
import time

START = time.process_time()
R = next(p for p in Path(__file__).resolve().parents if (p / 'research-wiki').is_dir())
W = R / 'research-wiki'
S = 'research/ddp/two_successful_methods_20261101/'
P = S + 'retained_edge_transfer/published_d15_15552_D4_source_gate/nonorbit_clone_interface/'
A = S + 'retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/available_pin_extension16417/'
OUT = R / S / 'wiki_sync'
LABEL = 'NONORBIT_D4_LOCAL_GLOBAL_TERMINAL_20261101'
RID = 'ddp-d16d4-source15552-nonorbit-fulln-local-exchange-no-global-unknown-20261101'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def read(path):
    return json.loads((R / path).read_text())


root = read(P + 'ROOT_DISPOSITION.json')
local = read(P + 'append_oneout_twoin_gate/RESULT.json')
post = read(P + 'append_oneout_twoin_gate/BLOCKER4_GROUP_POSTPROCESS.json')
final = read(P + 'global_incidence_warm864_gate/FINAL.json')
term = read(P + 'global_incidence_warm864_gate/TERMINAL.json')
assert root['status'] == 'ROOT_ACCEPTED_LOCAL_EXCLUSIONS_AND_GLOBAL_UNKNOWN_STOP'
assert local['full_domain_complete'] and local['append_candidates_checked'] == 14688
assert local['removal_domains_completed'] == 864 and local['possible_individually_feasible_pair_domain'] == 0
assert local['blocking']['unselected_center_blocking_owner_histogram']['4'] == 342
assert post['minimum_blocking_owners'] == 4 and post['groups'] == 342 and post['maximum_group_size'] == 1
assert post['source_parses'] == post['packing_pair_or_candidate_evaluations'] == 0
assert final['model_rows'] == final['model_columns'] == 15552 and final['model_incidence_nonzeros'] == 232632
assert final['known864_full_start_handchecked'] and final['setSolution_return'] == 'HighsStatus.kOk'
assert final['model_status'] == 'HighsModelStatus.kTimeLimit' and final['returned_best_count'] == 864
assert final['returned_binary_and_all_capacities_handchecked'] and not final['candidate_generated']
assert final['raw_dual_bound'] == -2384 and final['mip_nodes'] == 0 and final['log_LP_iterations'] == 21593
assert final['run_calls'] == 1 and final['retries'] == 0 and not final['max864_certified']
assert abs(final['cumulative_CPU_seconds'] - 68.299114264) < 1e-9
assert term['all_processes_terminal'] and not term['running']
L = read('research-wiki/DDP_METHOD_LEDGER.json')
before = L['record_count']
assert before == 447, f'Unexpected live ledger{before}; do not overwrite concurrent records'
records = {row['id']: row for row in L['rows']}
assert len(records) == before and RID not in records
assert not (W / 'experiments' / f'{RID}.md').exists()
assert not any(P in json.dumps(row.get('evidence_paths', [])) for row in L['rows'])
keys = ['validated_named_graph_examples', 'validated_named_parameter_pairs', 'complete_Lean_graph_instances',
        'saved_main_table_improvement_graph_examples', 'saved_main_table_improvement_parameter_pairs',
        'pending_outside_saved_table_graph_examples', 'pending_outside_saved_table_parameter_pairs',
        'known_publicly_dominated_graph_examples', 'known_publicly_dominated_also_saved_table_improvement_examples']
counts = {key: L[key] for key in keys}
assert tuple(counts[key] for key in keys[:5]) == (153, 43, 47, 105, 4)
generated = ['research/stale_record_candidates.csv', 'research/stale_record_candidates.html',
    'research/stale_record_candidates.html.txt', S + 'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json',
    S + 'build_stale_record_page.py']
generated_mtimes = {path: (R / path).stat().st_mtime_ns for path in generated}
evidence = [P + name for name in [
    'FULL_VERTEX_CLONE_PACKING_READ_GATE.json', 'ROOT_DISPOSITION.json',
    'append_oneout_twoin_gate/PRED.md', 'append_oneout_twoin_gate/run_once.py',
    'append_oneout_twoin_gate/RESULT.json', 'append_oneout_twoin_gate/TERMINAL.json',
    'append_oneout_twoin_gate/NOTE.md', 'append_oneout_twoin_gate/BLOCKER4_GROUP_PRED.md',
    'append_oneout_twoin_gate/blocker4_group_once.py', 'append_oneout_twoin_gate/BLOCKER4_GROUP_POSTPROCESS.json',
    'SOLVER_INCUMBENT_API_READ_GATE.json', 'SOLVER_INCUMBENT_API_READ_GATE.md', 'API_READ_ATTEMPT002.json',
    'global_incidence_warm864_gate/PRED.md', 'global_incidence_warm864_gate/run_global_once.py',
    'global_incidence_warm864_gate/global_child.py', 'global_incidence_warm864_gate/FINAL.json',
    'global_incidence_warm864_gate/RESULT.json', 'global_incidence_warm864_gate/TERMINAL.json',
    'global_incidence_warm864_gate/HANDLE.json', 'global_incidence_warm864_gate/NOTE.md',
    'global_incidence_warm864_gate/GLOBAL_STDOUT.log', 'global_incidence_warm864_gate/GLOBAL_STDERR.log']]
assert all((R / path).is_file() for path in evidence)
raw = dict(
    id=RID, title='16D4冻结15552源全中心克隆：局部≤4out严格NO；全局warm864超时仍UNKNOWN',
    family='Frozen-original full-neighborhood clone incidence packing with residual degree capacities',
    idea_family='idea:ddp-open-parameter-construction-20261026', date='2026-11-01', wiki_verdict='partial',
    record_type='frozen_fullN_clone_local_exchange_exclusions_and_global_incidence_UNKNOWN',
    target_Delta=16, target_D=4, savedL=16384,
    baseline_date='Inherited current-main/URSA16384 and accepted16416 incumbent; no new primary lookup or source validation',
    n=dict(actual=None, hypothetical=16417), actual_graph_Delta=None, actual_D=None,
    actual_D_scope='No new graph or diameter check. Source15552D4 and accepted16416D4/kernel inherited; local necessary incidence exclusions and one global MIP window did not produce any center set larger than known864.',
    ordinary_bad_unordered_pairs=None, ordinary_bad_target_D=4, new_lower_bound=False,
    scope='Fixedaccepted15552/116316originalsimplegraphH,sourceolddegrees14/15. EverynewrolefreezesONLYoriginalN_H(center),neverfinal16416neighborhood;alloldHedgesretainedandnonewnew. All15552centersareallowed,notjustwholeW27/controllerorbits. Exactoldcapacities16-degree_H are2atolddegree14and1atolddegree15;overlapallowedwherecapacitypermits. Localclosuresonlyabouttheaccepted864set,notany864set/globaloptimum. OneglobalbinaryincidenceMIPreturnsold864attimecap,notmaximumproof.',
    outcome_class='ROOT_ACCEPTED_LOCAL_EXCLUSIONS_AND_GLOBAL_UNKNOWN_STOP',
    distance_text='已有864/16416不是新解。local完整14688未选中心的append及864个remove1/add2域结束，个别可行新中心pair域0；所有未选blocker-owner至少4(4..15)。旧15552行profile一次postprocess，342个size4blocker sets全部singleton，结合min4严格排同incumbent净≤4out/k+1in。全局15552binary/15552rows/232632incidence，以cap2/1保overlap，known864暖启动手检并setSolutionkOk，唯一60秒窗口rawkTimeLimit返回同864。nodes0、LP21593、dual−2384仅raw未完成，不能证max864。累计68.299114264/90CPU含local/post与API导入失败成本；0改进center/图/源D4BFS/field/Lean/ARIS。',
    lesson_and_restart_condition='STOPthelocalclosedrangesandthecompletedglobalwindow. Localmin4andsingletonS4blocksarevalidstructuralobstructionsaboutthisincumbent;theydoNOTproveglobalmax864. Thereturned864istheknownincumbent,notanotherconstructionresult;rawdualandrootLPprogressarenotproof. Anyfurtherwholepackingrequiresanewexplicitboundedquestion,notautomaticrestart/seed orresumingthetimer. Nextactual16416availablepinSingleExtensionusesrealcurrentneighborhoods/slackandisanotherconnectionrule,notclone865.',
    restart_condition='Anewroot-authorizedfinitequestionoutsideclosed≤4outlocalrangeorwithasubstantiveglobalgenerating/compatibilitychange;nomorelocalexchangesteps,seedorglobalwindowautomatically.',
    unclosed_gap='Globalall-sourcecenterpackingimprovementremainsUNKNOWN,max864notcertified. Otherincumbents,largerexchangesandotherconnectionrulesarenotexcluded. Actual16416available4050pins/closedR3SingleExtensionisaseparatecase;itsstatusislinkedontheprogresspageandisnotanewgraphorpartofthisledgerresult. No new graph/parameter/Lean/independentmethodclaim.',
    positive_guarantees=[
        'FrozenN_H(center)isexactsimpleoldneighborhoodaftervirtualselfdeletion;anoldcenteranditsnewcloneneednotremainfullfalse twinsinthefinalgraph.',
        'Olddegree14capacity2isretained;globalmodeldoesnotrequireload<=1,independentcenters,wholeplanesoroldincumbentcontainment.',
        'Binarycentervariableslose nolegalmultiplicityhere:everyoriginalN_H(v)containsanolddegree15neighborwithcapacity1,sotwocopiesofthesamecenterareimpossible.ThisfinitepremiseisintheacceptedPRED,notrecomputed.',
        'GenericFullNeighborhoodClonesD4/prefixproofhandlesadjacentcenters;existingkernelisreusedwithoutnewmoduleorfield/BFSvalidation.',
        'Localmin4and342singleton4blockerscloseonlythegivenincumbentnet≤4outexchanges;rawglobaltimeoutdoesnotcertifymaximum864.'
    ],
    other_metrics=dict(
        new_graphs=0, new_parameter_pairs=0, new_Lean_instances=0, new_independent_method_claims=0,
        source_n=15552, source_m=116316, source_degree_histogram={'14': 648, '15': 14904},
        accepted_incumbent_centers=864, accepted_incumbent_graph_n=16416,
        accepted_incumbent_graph_m=129240, new_fullN_only_original_source=True,
        final_false_twin_assumption_not_used=True, old_degree14_capacity=2, old_degree15_capacity=1,
        all_original_centers=15552, binary_complete_by_each_N_having_old15neighbor=True,
        old14_overlap_preserved=True, wholeplanes_required=False, independent_centers_required=False,
        local_append_candidates=14688, local_remove_domains=864, local_complete=True,
        local_distinct_pair_domain=0, local_minimum_unselected_blocker_owners=4,
        local_maximum_unselected_blocker_owners=15, blocker4_profile_rows_read_once=15552,
        blocker4_centers=342, blocker4_groups=342, blocker4_max_group_size=1,
        local_net_k_out_kplus1_in_k_at_most4='COMPLETE_NO_ABOUT_THIS864_INCUMBENT',
        local_plus_postprocess_CPU_seconds=2.956499532,
        global_model_rows=15552, global_model_columns=15552, global_model_incidence_nonzeros=232632,
        global_objective='minimize -sum x', global_known864_start_handchecked=True,
        global_setSolution='HighsStatus.kOk', global_actual_log_start_feasible=True,
        global_run_calls=1, global_retries=0, global_model_status='HighsModelStatus.kTimeLimit',
        global_returned_best_count=864, global_returned_all_caps_binary_handchecked=True,
        global_returned_actual_max_load=1, global_raw_primal=-864, global_raw_dual=-2384,
        global_raw_nodes=0, global_raw_LP_iterations=21593,
        global_max864_certified=False, global_family_status='UNKNOWN_NO_VERIFIED_IMPROVEMENT',
        prior_API_CPU_seconds=4.322222089, API_import_failure_preserved_in_total=True,
        global_preparation_CPU_seconds=.5, actual_global_child_wait4_CPU_seconds=60.51635,
        actual_global_driver_CPU_seconds=.004042643,
        cumulative_CPU_seconds=68.299114264, cumulative_CPU_cap_seconds=90,
        oldsource_D4_BFS_field_Lean_ARIS_revalidation=0, actual_candidate_graphs=0,
        all_processes_terminal=True, new_fullclone_acceptance_draft_executed=False,
        next_distinct_mechanism='actual16416availablepinsclosedR3SingleExtension,notthe865thfrozenfullNclone',
        same_Goal='ACTIVE', old_N8_n61='PAUSED'), evidence_paths=evidence)

END = '<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
prefix = {}
for fn in ['index.md', 'query_pack.md', 'gap_map.md']:
    text = (W / fn).read_text()
    assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and LABEL not in text
    prefix[fn] = text[:text.index(END) + len(END)]
rawpath = OUT / f'{LABEL}_ROW.json'
rawpath.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + '\n')
api = runpy.run_path(str(R / 'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
helper = api['helper']
helper.rebuild_index = lambda *args, **kwargs: None
helper.rebuild_query_pack = lambda *args, **kwargs: None
edges_mtime = (W / 'graph/edges.jsonl').stat().st_mtime_ns
n = api['normalize'](raw)
n['goal']['baseline_date'] = raw['baseline_date']
with (OUT / f'{LABEL}_NODE_CALLS.log').open('w') as log, contextlib.redirect_stdout(log):
    api['write_node'](n)
assert re.search(r'^verdict: partial$', (R / n['wiki_path']).read_text(), re.M)
records[RID] = n
L.update(rows=list(records.values()), record_count=before+1, updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))] = 1
(W / 'DDP_METHOD_LEDGER.json').write_text(json.dumps(L, ensure_ascii=False, indent=2) + '\n')
safe = api['safe']
table = '| [' + safe(n['title']) + '](experiments/' + RID + '.md) | ' + safe(api['goal_text'](n)) + ' | ' + safe(api['gap_text'](n)) + ' | ' + safe(n['exact_scope']) + '；' + safe(n['lesson']) + '；[ROOT处置](../' + P + 'ROOT_DISPOSITION.json) |'
ledger_md = W / 'DDP_METHOD_LEDGER.md'
text = ledger_md.read_text()
needle = f'本页有{before}条记录；不以此宣称{before}种独立方法。'
assert needle in text
text = text.replace(needle, f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。', 1)
text += '\n\n<!-- ' + LABEL + ' -->\n## ' + NOW + ' nonorbit D4：局部严格NO与global UNKNOWN分账\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n' + table + '\n\n一个实验节点，不新增图、参数、Lean或独立方法。保原15552的N、允许旧14度cap2 overlap；不能误当复制final16416的false twins。local min4+342个singleton4blocker关闭同incumbent≤4out净增1，global60秒只返回known864，rawdual/nodes/LP不证max864。累计68.299114264/90含API失败和post，全部终态停止。153／43／Lean47与14格老题实测不变。\n'
ledger_md.write_text(text)

available_handle = read(A + 'HANDLE.json') if (R / A / 'HANDLE.json').is_file() else {}
available_terminal = read(A + 'TERMINAL.json') if (R / A / 'TERMINAL.json').is_file() else None
if available_terminal is not None:
    available_status = available_terminal['status']
    available_text = ('该唯一窗口已实际终态：' + available_status + '。已建立4050个当前合法pin的闭R3支持，等价压至3798列；已知完整cover仍29个，未得到<=16。一次30秒窗口到时，' +
        '29不是已证最优、也不能判<=16不可能。0个16417候选；当前case累计' + str(available_terminal.get('wholecase_CPU_seconds')) + '／60CPU，具体处置由ROOT负责。')
else:
    available_status = available_handle.get('status', 'AUTHORIZED_NO_ACTUAL_HANDLE_REPORTED')
    available_text = ('累计60CPU仅授权一次4050availablepins的闭R3cover<=16问题；读取时实际HANDLE状态为' + available_status +
        '，运行与候选状态以同目录HANDLE为准，不预称候选或PASS。')
nav = '<!-- ' + LABEL + ' -->\n### ' + NOW + ' 全源克隆局部NO、全局UNKNOWN均终态；下一规则用当前图真实余度\n\n冻结原15552的完整旧N，不要求whole27或最终false twins。local14688未选点append／864 remove1域完整，min4 blocker；342个四blocker组全singleton，关闭同incumbent净≤4out/k+1in。全局15552×15552／232632 incidence，old14cap2保留；known864 warm手检/setSolutionkOk，唯一60s窗口kTimeLimit仍返旧864，nodes0／LP21593／rawdual−2384不证max864。68.299114264／90CPU含API导入失败与post，0新图／BFS／field／Lean／ARIS，停止不续。\n\n当前不同问题为accepted16416的全部4050 availablepins取<=16的closedR3 cover：' + available_text + '\n\n唯一Wiki447→448为新增一个实验记录，非独立新方法或图数。153／43／Lean47、savedmain105/4、14个老题实测／0老题新达标图保持。650节点的20秒无incumbent UNKNOWN保留，不重复。人工顶部与旧历史逐字保留、无fullrebuild/reimport；sameGoalACTIVE、旧N8/n61暂停。\n\n[' + n['title'] + '](experiments/' + RID + '.md)\n\n'
preserved = {}
index_before = None
for fn, top in prefix.items():
    path = W / fn
    text = path.read_text()
    assert text.startswith(top)
    at = len(top)
    text = text[:at] + '\n\n' + nav + text[at:]
    if fn == 'index.md':
        match = re.search(r'^## Experiments \((\d+)\)$', text, re.M)
        assert match and ('`exp:' + RID + '`') not in text
        index_before = int(match[1])
        text = text[:match.start()] + f'## Experiments ({index_before+1})' + text[match.end():]
        pos = text.index('\n', match.start()) + 1
        text = text[:pos] + '- `exp:' + RID + '` — ' + n['title'] + ' [partial]\n' + text[pos:]
    assert text[:at] == top
    path.write_text(text)
    preserved[fn] = True
helper.append_log(str(W), LABEL + ': one15552frozenfullNnonorbitpackingnode447to448,notmethod/graph. Localappend1out2incompleteNO+min4/342singleton4blockersclose≤4outnet+1about864;globalone60swindowwarm864kOk/timecapstill864/rawdual-2384/nodes0LP21593UNKNOWN,no max864.68.299114264/90CPUincludesAPIimportfailureandpost,0sourceD4BFS/field/Lean/ARIS/newgraph. Source14cap2andbinarypremisepreserved;notfinalfalse twins. Actualavailable16416SingleExtensionseparatelylinked,no suite/PASS.14oldcells/153/43/47same;human15top exact,nobuild/reimport/ROOTownedwrites.')

page_path = R / 'research/progress.html'
page = page_path.read_text()
assert page == (R / 'research/progress.html.txt').read_text()
match = re.search(r'<section id="stale-route-current">.*?</section>', page, re.S)
assert match
history = match.group().replace('id="stale-route-current"', 'id="650-before-nonorbit-d4-terminal"', 1)
history = '<details id="650-before-nonorbit-d4-terminal-history"><summary>前一轮快照：650终态与当时D4局部结果入口（保留历史）</summary>\n' + history + '\n</details>'
current = '''<section id="stale-route-current">
<h2>当前结果：D4全源克隆局部排除，全局窗口UNKNOWN</h2>
<div class="note"><strong>本轮0张新增图；仍153个合法版本／43组参数／47个具体Lean实例。15项老题中14格有本轮新检验，老题仍0张新增达标图。</strong><p>本轮回到已成功D4源的非轨道点级选择；返回known864不是新图，也不增加老表实测格。唯一Wiki现448条研究记录，非448种方法或成果。</p></div>
<p>固定原15552点源，克隆邻域始终冻结为原simple N，不复制最终16416的整个邻域。原14度顶点允许load2、15度只允许load1；不强加whole27平面、独立中心或load1。每个原N都有一个15度邻点，故同center多重复制也被cap1挡住，binary不是人为丢掉重数。</p>
<table><thead><tr><th>范围</th><th>实际结果</th><th>能说明什么</th></tr></thead><tbody><tr><td>同864 incumbent局部</td><td>14688 append与864 remove1域完整NO；未选至少4 blockers</td><td>不是全局最优</td></tr><tr><td>旧profile一次后处理</td><td>342个四blocker组全singleton</td><td>与min4合并关闭同incumbent≤4out净增1</td></tr><tr><td>全部15552中心incidence MIP</td><td>15552行／15552列／232632非零项；warm864 kOk；60秒后仍864</td><td>UNKNOWN，不能证max864</td></tr></tbody></table>
<p>global原始nodes0、LP21593、dual−2384只保留为未完成求解指标；没有新中心组或图。累计68.299CPU／90，含API导入失败与post成本；源D4／旧BFS／field／Lean／ARIS均0重验，局部/global都已终态停止，不续同timer或局部交换层级。</p>
<p><a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/nonorbit_clone_interface/ROOT_DISPOSITION.json">ROOT总处置</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/nonorbit_clone_interface/append_oneout_twoin_gate/NOTE.md">局部完整范围</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/nonorbit_clone_interface/append_oneout_twoin_gate/BLOCKER4_GROUP_POSTPROCESS.json">四blocker组证据</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/nonorbit_clone_interface/global_incidence_warm864_gate/FINAL.json">global实际终态与CPU</a>。</p>
<h3>当前不同连接规则：在accepted16416的真实余度上加一个任意pin邻域点</h3>
<p>使用当前全图的4050个degree&lt;16 pins，问能否选≤16个closedR3覆盖全部16416点（包括原864个克隆）。这属于SingleExtension，不是第865个冻结旧N clone。旧旧D4因保全部边继承；真正候选才需要独立检查新根及完整边表。</p>
<p>AVAILABLESTATUS</p>
<p><a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/available_pin_extension16417/HANDLE.json">实际HANDLE</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/available_pin_extension16417/PRED.md">当前cover预测与预算</a>。没有完整16417图时，两份验收接口均保持草稿，未跑任何旧套件或制造验收PASS。</p>
<p>650的1170变量单窗口20秒无incumbent仍UNKNOWN，15配对/BFS均未启动，历史在下方保留。人工15格选题与先预测再检验要求保留；Goal继续ACTIVE、旧N8/n61暂停，globalpriority确认0、16416完整交付和153／43／Lean47不变。</p>
</section>'''.replace('AVAILABLESTATUS', available_text)
page = page[:match.start()] + current + '\n' + history + page[match.end():]
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
page = re.sub(r'<p>更新 [^<]*</p>', '<p>更新 ' + stamp + '。同一Goal ACTIVE；旧D2/n61任务继续暂停。</p>', page, count=1)
page_path.write_text(page)
(R / 'research/progress.html.txt').write_text(page)
after = read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count'] == before+1 == len(after['rows'])
assert {key: after[key] for key in keys} == counts
assert {path: (R / path).stat().st_mtime_ns for path in generated} == generated_mtimes
assert page_path.read_bytes() == (R / 'research/progress.html.txt').read_bytes()
modified = ['research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md', n['wiki_path'],
    'research-wiki/index.md', 'research-wiki/query_pack.md', 'research-wiki/gap_map.md', 'research-wiki/log.md',
    'research/progress.html', 'research/progress.html.txt', str(rawpath.relative_to(R)),
    str((OUT / f'{LABEL}_NODE_CALLS.log').relative_to(R)), str(Path(__file__).relative_to(R)),
    str((OUT / f'{LABEL}_RECEIPT.json').relative_to(R))]
if (W / 'graph/edges.jsonl').stat().st_mtime_ns != edges_mtime:
    modified.append('research-wiki/graph/edges.jsonl')
receipt = dict(status='PASS_ONE_NONORBIT_D4_LOCAL_GLOBAL_TERMINAL_NODE', updated_UTC=NOW,
    records_before=before, records_after=before+1, records_added=1, experiment_id=RID,
    graph_parameter_Lean_method_increments=[0, 0, 0, 0], counts_unchanged=counts,
    local_append_1out2in_complete_NO=True, local_le4out_netplus1_paper_NO=True,
    local_blocker4_groups=342, local_blocker4_maxsize=1,
    global_model_shape=[15552, 15552, 232632], global_known864_warm_kOk=True,
    global_returned864_is_old_not_new=True, global_status='UNKNOWN_NO_VERIFIED_IMPROVEMENT',
    global_max864_certified=False, global_raw_nodes_LP_dual=[0, 21593, -2384],
    actual_math_cumulative_CPU_seconds=68.299114264, actual_math_cap_seconds=90,
    API_failure_and_post_cost_preserved=True, old14_capacity2_overlap_preserved=True,
    binary_multiplicity_reason_preserved=True, frozen_original_N_not_final_false_twins=True,
    human_top_preserved_exact=preserved, prior_progress_snapshot_preserved=True,
    current_SingleExtension_HANDLE_status=available_status,
    current_SingleExtension_separate_from_this_node=True,
    no_new_actual_graph_or_acceptance_PASS=True,
    builder_and_existing15row_outputs_unchanged_NOT_BUILT=True,
    shortlist_newly_tested_cells=14, progress_html_and_source_identical=True,
    fullrebuild_reimport=False, root_STATE_ROUND_recovery_REPORT_modified=False,
    raw_math_files_modified=False, new_numeric_BFS_field_solver_Lean_review_runs=0,
    modified_paths=modified, CPU_seconds=time.process_time()-START, stop=True)
(OUT / f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(receipt, ensure_ascii=False))
