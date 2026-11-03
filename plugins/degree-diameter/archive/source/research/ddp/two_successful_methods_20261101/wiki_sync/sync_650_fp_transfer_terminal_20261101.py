"""One650 FP-transfer UNKNOWN node; no numerical work or15-row build."""
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
P = S + 'stale_record_transfer_d10D3/fp_endpoint_transfer651/'
OUT = R / S / 'wiki_sync'
LABEL = 'SOURCE650_FP_TRANSFER_TERMINAL_20261101'
RID = 'ddp-stale-d10d3-650-eight-fp-endpoint-transfer651-mip-unknown-20261101'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def read(path):
    return json.loads((R / path).read_text())


root = read(P + 'ROOT_DISPOSITION.json')
result = read(P + 'FP_RESULT.json')
term = read(P + 'FP_TERMINAL.json')
solver = read(P + 'FP_SOLVER_RETURN.json')
model = read(P + 'FP_MODEL.json')
assert root['status'] == 'ROOT_ACCEPTED_ACTUAL_TIMEOUT_UNKNOWN_NO_FAMILY_EXCLUSION'
assert result['status'] == 'UNKNOWN_F_COVER_MODEL_NO_INCUMBENT'
assert result['solver_calls'] == 1
assert result['candidate_pairings_checked'] == result['newroot_BFS_count'] == result['oldroot_BFS_count'] == 0
assert term['terminal'] and term['active_processes'] == 0
assert solver['status'] == 1 and solver['incumbent'] is None and not solver['success']
assert not solver['infeasibility_certificate_checked']
assert 'Time limit reached' in solver['message']
assert (model['binary_variables'], model['rows'], model['nonzeros']) == (1170, 1302, 90480)
assert abs(result['wholecase_CPU_seconds'] - 22.084731374) < 1e-9
L = read('research-wiki/DDP_METHOD_LEDGER.json')
before = L['record_count']
assert before == 446, f'Ledger changed to{before}; inspect before any write'
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
    'research/stale_record_candidates.html.txt', S + 'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json']
generated_mtimes = {path: (R / path).stat().st_mtime_ns for path in generated}
evidence_names = ['SOURCE650_FP_TRANSFER_READ_GATE.md', 'SOURCE650_FP_TRANSFER_READ_GATE.json',
    'FP_PRED.md', 'FP_once.py', 'FP_MODEL.json', 'FP_MODEL_MATRIX.npz', 'FP_SOLVER_RETURN.json',
    'FP_RESULT.json', 'FP_TERMINAL.json', 'FP_HANDLE.json', 'FP_NOTE.md', 'ROOT_DISPOSITION.json']
paths = [P + name for name in evidence_names]
assert all((R / path).is_file() for path in paths)
raw = dict(
    id=RID, title='10D3 actual650八FP端点转移：1170变量单窗口20秒无incumbent，UNKNOWN而非不可行',
    family='F-neighborhood-twin coverage with FP endpoint transfer and PP repairs',
    idea_family='idea:ddp-open-parameter-construction-20261026', date='2026-11-01', wiki_verdict='partial',
    record_type='fixed_host_FP_surgery_core_coverage_feasibility_UNKNOWN_no_candidate',
    target_Delta=10, target_D=3, savedL=650,
    baseline_date='Inherited actual650/3250 Delorme polarity-replication source and current saved-main650; no new public-source search or sourceD3 validation',
    n=dict(actual=None, hypothetical=651), actual_graph_Delta=None, actual_D=None,
    actual_D_scope='No651graph,prototypeorordinarydistanceBFSwasgenerated. OneexactF-onlycoverageMIPwindowreturnedUNKNOWNwithoutincumbent;15PPpairingsandnewroot/oldrootstageswereNOT_ENTERED.',
    ordinary_bad_unordered_pairs=None, ordinary_bad_target_D=3, new_lower_bound=False,
    scope='Fixedactual650/3250all10sourcewithP130,F520,65F-neighborhoodtwinsandPPcycles79/21/30. Select8oldFPcutswithdistinctFandPends;addonezadjacentall8Fand2selecteddonorP;pairremaining6Pby3PPrepairs,allowingalready-oldPPedgeswithunderdegree9becausecap<=10. OneHiGHSfeasibilitywindowonlyselectsthe8cuts/2PstarbyexactsourceB2Fcoverage. Noincumbent,soNOprototypefreeze,pairing,candidateorD3test. Notthesameasold<=5cut/allendpoints/purehubNO;notageneralFP-familyexclusion.',
    outcome_class='ROOT_ACCEPTED_ACTUAL_TIMEOUT_UNKNOWN_NO_FAMILY_EXCLUSION',
    distance_text='正预测是存在8FP/2Pstar使新根三步覆盖520F。继承twin替路将删边后F-only门精确写成sourceB2(S)，PP修补不能补z→F。一次1170binary(1040FP+130Pstar)/1302rows/90480nnz、c=0、threads1/time_limit20，HiGHS实际status1 Time limit reached/primalNone，x为空；不是rawINFEASIBLE。solver20.013963667CPU，进程20.333854394，累计22.084731374/45含read1.50087698+prep.25。无incumbent，预测UNRESOLVED，未冻结原型、0/15pairings、0新旧根BFS、0候选图，不能归因旧P损伤或把未进入stage记失败。',
    lesson_and_restart_condition='STOPthissinglefeasibilitywindowwithoutsecondsolver,seed,prototypeorbudgetextension. KeepUNKNOWNdistinctfromcertifiedNO;thereisnocandidatefromwhichtoinferoldPdamage. Themodelisreviewable,butnoincumbentdoesnotproveF-routecoverageimpossible. ExistingPPedgesremainlegalunderdegree9inthepreparedpairinginterface;itwasnotexecuted. Anyfutureworkrequiresanexplicitnewboundedstructuralquestion;donotautomaticallyrepeatthesametimewindow.',
    restart_condition='Anewexplicitboundedquestionorchangedconnection/encodingauthorizedbyroot;notmerelymoretime,anotherseedorthesameF-coverfeasibilitywindow.',
    unclosed_gap='WholeFP-transferfamilyremainsUNKNOWN;nocertifiedinfeasibility,integerportselection,15pairingresult,newrootcoverageoroldoldD3evidence. No651graph/newparameter/Lean/methodorpriorityclaim. SameGoalACTIVE,oldN8/n61PAUSED.',
    positive_guarantees=[
        'ActualsourceandP/F/twins/A2A3comefromthe650degree10D3cache,notother650degree5D5or6D4objects.',
        'SourceR2usescachedordinaryA2positivityplusidentityandadjacency;noBFS,newmatrixmultiplication,fieldorsourceD3validation.',
        'F/Pcutend<=1,starPrequiresdonorP,sumcuts8,sumstarP2andall520Fcoverageconstraintsareinthepersisted1170binarymodel.',
        'TheF-neighborhoodtwinbridgehandlescutendpointsthatarenotallstarspokes;genericall-endpointdistanceinvarianceisnotmisapplied.',
        'Actualsolverstatus1/noincumbentisnotINFEASIBLEorstrictfamilyNO;alllaterstagesareexplicitlyunexecuted.'
    ],
    other_metrics=dict(
        new_graphs=0, new_parameter_pairs=0, new_Lean_instances=0, new_independent_method_claims=0,
        source_n=650, source_m=3250, source_regular_degree=10, source_P=130, source_F=520,
        source_F_neighborhood_twin_pairs=65, inherited_P_cycle_lengths=[79, 21, 30],
        hypothetical_order=651, hypothetical_m_when3new_PP=3255, target_maxdegree=10,
        already_old_PP_allowed_underdegree9=True, eight_distinct_F_P_cuts=True,
        source_B2_F_coverage_exact_by_twin_paper=True, PPrepairs_cannot_aid_newroot_F_le3=True,
        model_binary_variables=1170, model_FP_variables=1040, model_starP_variables=130,
        model_rows=1302, model_nonzeros=90480, objective='zero_feasibility',
        solver='SciPy milp/HiGHS', solver_threads=1, solver_time_limit_seconds=20,
        solver_calls=1, solver_actual_status=1, solver_message=solver['message'], solver_incumbent=None,
        solver_returned_infeasible=False, certified_infeasibility=False,
        mip_node_count=solver['mip_node_count'], mip_dual_bound=solver['mip_dual_bound'], mip_gap=solver['mip_gap'],
        solver_CPU_seconds=20.013963667, prediction_status='UNRESOLVED_NO_INCUMBENT_NOT_REFUTED',
        frozen_prototypes=0, planned_pairing_domain=15, actual_pairings=0,
        newroot_BFS=0, oldroot_BFS=0, source_validity_BFS=0, candidate_graphs=0,
        literal_input_parses=1, existing_A2_reused=True, new_walkmatrix_field_Lean_review_runs=0,
        prior_read_CPU_seconds=1.50087698, new_preparation_CPU_seconds=.25,
        actual_parent_allthreads_CPU_seconds=20.333854394, actual_children_CPU_seconds=0,
        wholecase_CPU_seconds=22.084731374, wholecase_CPU_cap_seconds=45,
        all_processes_terminal=True, old_purehub_scope='delete1to5oldedges/newhubadjacentALLdistinctendpoints/nootheradditionsCOMPLETE_NO_inherited',
        shortlist_cells_newly_tested=14, shortlist_new_legal_graphs=0,
        same_Goal='ACTIVE', old_N8_n61='PAUSED'), evidence_paths=paths)

END = '<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
prefix = {}
for filename in ['index.md', 'query_pack.md', 'gap_map.md']:
    text = (W / filename).read_text()
    assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and LABEL not in text
    prefix[filename] = text[:text.index(END) + len(END)]
rawpath = OUT / f'{LABEL}_ROW.json'
rawpath.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + '\n')
api = runpy.run_path(str(R / 'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
helper = api['helper']
helper.rebuild_index = lambda *args, **kwargs: None
helper.rebuild_query_pack = lambda *args, **kwargs: None
edges_mtime = (W / 'graph/edges.jsonl').stat().st_mtime_ns
normalized = api['normalize'](raw)
normalized['goal']['baseline_date'] = raw['baseline_date']
assert normalized['id'] == RID
with (OUT / f'{LABEL}_NODE_CALLS.log').open('w') as log, contextlib.redirect_stdout(log):
    api['write_node'](normalized)
assert re.search(r'^verdict: partial$', (W / 'experiments' / f'{RID}.md').read_text(), re.M)
records[RID] = normalized
L.update(rows=list(records.values()), record_count=before + 1, updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))] = 1
(W / 'DDP_METHOD_LEDGER.json').write_text(json.dumps(L, ensure_ascii=False, indent=2) + '\n')
safe = api['safe']
table = '| [' + safe(normalized['title']) + '](experiments/' + RID + '.md) | ' + safe(api['goal_text'](normalized)) + ' | ' + safe(api['gap_text'](normalized)) + ' | ' + safe(normalized['exact_scope']) + '；' + safe(normalized['lesson']) + '；[ROOT处置](../' + P + 'ROOT_DISPOSITION.json) |'
ledger_md = W / 'DDP_METHOD_LEDGER.md'
text = ledger_md.read_text()
needle = f'本页有{before}条记录；不以此宣称{before}种独立方法。'
assert needle in text
text = text.replace(needle, f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。', 1)
text += '\n\n<!-- ' + LABEL + ' -->\n## ' + NOW + ' 650八FP端点转移：唯一窗口UNKNOWN\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n' + table + '\n\n1170变量／1302行／90480非零项，HiGHS实际20秒到时，无incumbent、非INFEASIBLE，不能全族NO。没有frozenprototype，所以15配对／新旧根BFS／图均未进入；不把未进入阶段写作失败。累计22.084731374／45CPU，停止不第二求解/seed/原型。唯一账本447是研究记录，不是447方法或图；15老格14格有本轮新检验、0新达标图，153／43／Lean47保持。\n'
ledger_md.write_text(text)

nav = '<!-- ' + LABEL + ' -->\n### ' + NOW + ' 650新FP转移窗口实际UNKNOWN，尚无可冻结端口组\n\n唯一HiGHS feasibility实际1170binary／1302rows／90480nnz，20秒到时status1、primalNone、无incumbent；不是INFEASIBLE或certified族NO。520F覆盖由旧sourceA2与twin替路接口给出，源D3/旧BFS/field均未重验。未冻结8cuts/2Pstar，15配对、候选新旧根BFS与651图均0。累计22.084731374／45CPU，预测UNRESOLVED，不能归因旧P路线损伤；停止此窗口，不第二solver/seed/原型。\n\n新增一个同scope实验node，446→447，14/15老格有本轮新检验而不是14张图；老题0新增达标图，153图／43参数／47具体Lean、savedmain105/4/globalpriority确认0保持。人工top与历史逐字保留，无fullrebuild/reimport，GoalACTIVE、旧N8/n61暂停。新D4 nonorbitappend1swap由另一owner负责；其代理已报告actual终态，本650节点不将它冒作本轮新图或替ROOT做D4验收。\n\n[' + normalized['title'] + '](experiments/' + RID + '.md)\n\n'
preserved = {}
index_before = None
for filename, top in prefix.items():
    path = W / filename
    text = path.read_text()
    assert text.startswith(top)
    at = len(top)
    text = text[:at] + '\n\n' + nav + text[at:]
    if filename == 'index.md':
        match = re.search(r'^## Experiments \((\d+)\)$', text, re.M)
        assert match and ('`exp:' + RID + '`') not in text
        index_before = int(match[1])
        text = text[:match.start()] + f'## Experiments ({index_before+1})' + text[match.end():]
        pos = text.index('\n', match.start()) + 1
        text = text[:pos] + '- `exp:' + RID + '` — ' + normalized['title'] + ' [partial]\n' + text[pos:]
    assert text[:at] == top
    path.write_text(text)
    preserved[filename] = True
helper.append_log(str(W), LABEL + ': one650FPtransferUNKNOWNnode446to447,notmethod/graphcount.1170binary/1302rows/90480nnz,c0,threads1,sole20stimeoutstatus1noincumbent,notINFEASIBLEorstrictNO.15pairings/newoldBFS/graph0,wholecase22.084731374/45CPU.14testedoldcells,0newoldrecordgraphs,153/43/47unchanged.Human15top exact;buildereditedNOTBUILT,rootownsonefinalbuild;noSTATE/ROUND/recovery/REPORTwrites.')

page_path = R / 'research/progress.html'
page = page_path.read_text()
assert page == (R / 'research/progress.html.txt').read_text()
match = re.search(r'<section id="stale-route-current">.*?</section>', page, re.S)
assert match
history = match.group().replace('id="stale-route-current"', 'id="585-k1-before650-fp"', 1)
history = '<details id="585-k1-before650-fp-history"><summary>前一轮快照：585原型闭合与当时650尚未报告运行（保留历史）</summary>\n' + history + '\n</details>'
current = '''<section id="stale-route-current">
<h2>当前结果：650新FP端点转移单窗口UNKNOWN，无incumbent</h2>
<div class="note"><strong>本轮0张新增图；仍153个合法版本／43组参数／47个具体Lean实例。15项老题中14格有本轮新检验，老题仍0张新增达标图。</strong><p><a href="stale_record_candidates.html">15项问题与实际范围</a> · <a href="stale_record_candidates.html.txt">HTML源码</a> · <a href="stale_record_candidates.csv">CSV</a>。生成器已更新650行与14格标记，最终页面由ROOT结合最新447账本统一build；本次未重建这些产物。</p></div>
<p><strong>实际改变了旧连接：</strong>固定650／3250的10度源，选八条FP旧边且F、P端点各互异，新根连接八F及二P，余六P再配三对。继承P的F-neighborhood twins，把新根到520F的三步覆盖写成原source-R2；PP修补不能补这类F路线。旧至多五cut／全端点纯hub的NO不自动适用。</p>
<table><thead><tr><th>实际阶段</th><th>结果</th></tr></thead><tbody><tr><td>一次可行性模型</td><td>1170 binary／1302行／90480非零项，objective0、threads1</td></tr><tr><td>HiGHS唯一20秒窗口</td><td>status1 Time limit reached，primalNone，无incumbent；不是INFEASIBLE</td></tr><tr><td>冻结原型／15种PP配对</td><td>0，尚未进入</td></tr><tr><td>新根／旧根BFS、651图</td><td>全部0；不能归因于旧P路线损伤</td></tr></tbody></table>
<p>solver实际20.014CPU、进程20.334CPU，含原read与准备后累计22.085／45CPU。存在F覆盖端口组的预测仍未决，不因无incumbent判整族NO；本窗口已停止，不第二solve、seed或原型。已有PP边会保留为合法underdegree9分支的后续接口，但该分支没有实际执行。</p>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_NOTE.md">本轮解释与边界</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL.json">完整模型接口</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_SOLVER_RETURN.json">实际返回</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/ROOT_DISPOSITION.json">ROOT接受UNKNOWN处置</a>。</p>
<p>此前585固定p0四cut原型的k0／k1数值与k≥2纸面NO完整保留，不重跑。唯一Wiki现447条研究记录，记录数不是独立方法或成果数。人工15格优先选题、先预测再检验、完整图验收要求保留；Goal继续ACTIVE、旧N8/n61暂停，globalpriority确认0与16416完整交付不变。</p>
<p><strong>另一路D4 nonorbit append1swap：</strong>此前仅获20CPU授权，现代理已报告实际有限门终态；本次650同步不代ROOT确认其结论，也不新增图／参数／Lean计数。<a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/nonorbit_clone_interface/append_oneout_twoin_gate/RESULT.json">D4实际结果入口</a>，后续处置由ROOT更新。</p>
</section>'''
page = page[:match.start()] + current + '\n' + history + page[match.end():]
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
page = re.sub(r'<p>更新 [^<]*</p>', '<p>更新 ' + stamp + '。同一Goal ACTIVE；旧D2/n61任务继续暂停。</p>', page, count=1)
page_path.write_text(page)
(R / 'research/progress.html.txt').write_text(page)

after = read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count'] == before + 1 == len(after['rows'])
assert {key: after[key] for key in keys} == counts
assert {path: (R / path).stat().st_mtime_ns for path in generated} == generated_mtimes
assert page_path.read_bytes() == (R / 'research/progress.html.txt').read_bytes()
builder_text = (R / S / 'build_stale_record_page.py').read_text()
assert '(10, 3)' in builder_text and '90480' in builder_text
assert '(9, 3), (10, 3), (8, 4)' in builder_text
modified = ['research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md', normalized['wiki_path'],
    'research-wiki/index.md', 'research-wiki/query_pack.md', 'research-wiki/gap_map.md', 'research-wiki/log.md',
    S + 'build_stale_record_page.py', 'research/progress.html', 'research/progress.html.txt',
    str(rawpath.relative_to(R)), str((OUT / f'{LABEL}_NODE_CALLS.log').relative_to(R)),
    str(Path(__file__).relative_to(R)), str((OUT / f'{LABEL}_RECEIPT.json').relative_to(R))]
if (W / 'graph/edges.jsonl').stat().st_mtime_ns != edges_mtime:
    modified.append('research-wiki/graph/edges.jsonl')
receipt = dict(status='PASS_ONE_650_FP_UNKNOWN_NODE_AND_LIGHT_NAV_SYNC', updated_UTC=NOW,
    records_before=before, records_after=before+1, records_added=1, experiment_id=RID,
    counts_unchanged=counts, graph_parameter_Lean_method_increments=[0, 0, 0, 0],
    solver_actual_status=1, no_incumbent=True, INFEASIBLE_or_strict_family_NO_claim=False,
    model_binary_variables=1170, model_rows=1302, model_nonzeros=90480,
    actual_pairing_newroot_oldroot_BFS_counts=[0, 0, 0], actual_mathematical_case_CPU_seconds=22.084731374,
    shortlist_newly_tested_cells=14, shortlist_new_legal_graphs=0,
    human_top_preserved_exact=preserved, old_progress_snapshot_preserved=True,
    builder_edited_only_NOT_BUILT=True, generated15row_HTML_CSV_JSON_unchanged=True,
    progress_html_and_source_identical=True, fullrebuild_reimport=False,
    new_numeric_BFS_field_solver_Lean_review_runs=0,
    root_STATE_ROUND_recovery_REPORT_modified=False,
    D4_actual_peer_terminal_report_linked_NOT_ROOT_ACCEPTANCE=True,
    root_to_do_one_final15row_build=True, modified_paths=modified,
    CPU_seconds=time.process_time()-START, stop=True)
(OUT / f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(receipt, ensure_ascii=False))
