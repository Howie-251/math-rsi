from pathlib import Path
from datetime import datetime, timezone
import copy, json, subprocess, sys

R = Path(__file__).resolve().parents[2]
W = R / 'research-wiki'
S = 'research/ddp/two_successful_methods_20261101/'
P = S + 'public_baseline_audit/'
V = S + 'reviews/'
T = S + 'd2_record106_edge_repair/'
X = T + 'sector_matching_extension/'
E = T + 'paper_S11_domination/NOTE.md'
H = 'research/public_comparison_current.html'
B = 'D3_SEVEN_LARGEST_FOUND_HTML_D2_C7_D4_AB_C925_20261101'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def read(path):
    return json.loads((R / path).read_text())

keys = ['record_count', 'validated_named_graph_examples', 'validated_named_parameter_pairs', 'complete_Lean_graph_instances']
L = read('research-wiki/DDP_METHOD_LEDGER.json')
assert tuple(L[k] for k in keys) == (421, 152, 43, 46)
ids = [
    'ddp-f4-bhakar-c60-global-pgl2-complete-negative-edge-dependent-preparing-20261101',
    'ddp-f5-source-plane-block-clone-d21-d22-terminal-graphs-20261101',
    'ddp-opposite-gq35-vertical-spread-24flag-pins-6160-d24-d3-20261101',
    'ddp-opposite-gq44-desarguesian-spread-7242-d25-d3-20261101',
    'ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101',
    'ddp-d2-public106-internal-pin-old-edge-repair-scoped-gates-20261101',
    'ddp-d15-d4-current15552-source-gap-20261027',
]
rows = [copy.deepcopy(next(x for x in L['rows'] if x['id'] == i)['source_record']) for i in ids]
summary_path = P + 'D3_CAP20_26_USER_SEARCH_SUMMARY_20261101.json'
summary = read(summary_path)
lo = read(P + 'D3_CAP20_23_USER_PRIMARY_SEARCH_20261101.json')
hi = read(P + 'D3_CAP24_26_USER_PRIMARY_SEARCH_20261101.json')
assert summary['status'] == 'SEVEN_LOCAL_INSTANCES_LARGEST_FOUND_IN_REVIEWED_PUBLIC_SOURCES'
assert not summary['global_best_or_priority_certified'] and not summary['method_novelty_established']
assert lo['author_paper_branch_query_count'] == hi['new_search_query_count'] == 8
assert [(t['Delta'], t['our_n'], t['best_verified_public_method_guarantee']) for t in summary['targets']] == [
    (20, 3840, 2791), (21, 3984, 2928), (22, 4192, 3294), (23, 4336, 3549),
    (24, 6160, 6144), (25, 7242, 7225), (26, 7532, 7514)]
assert all(not t['external_at_least_our_n_located'] for t in summary['targets'])
search_evidence = [summary_path] + [P + n for n in [
    'D3_CAP20_23_USER_PRIMARY_SEARCH_20261101.json', 'D3_CAP20_23_USER_PRIMARY_SEARCH_20261101.md',
    'D3_CAP24_26_USER_PRIMARY_SEARCH_20261101.json', 'D3_CAP24_26_USER_PRIMARY_SEARCH_20261101.md',
    'D3_CAP20_26_GLOBAL_TABLE_ACCESS_20261101.json', 'D3_CAP20_26_GLOBAL_TABLE_REQUESTS_ACCESS_20261101.json']]
navigation = [H, H + '.txt', 'research/public_comparison_current.csv']

for row in rows[:5]:
    m = row['other_metrics']
    targets = []
    for graph in m['validated_graph_instances']:
        target = next((t for t in summary['targets'] if (graph['Delta'], graph['D'], graph['n']) == (t['Delta'], t['D'], t['our_n'])), None)
        if target is None:
            continue
        targets.append(copy.deepcopy(target))
        graph.update(public_comparison_status='LARGEST_INSTANCE_IN_PUBLIC_SOURCES_REVIEWED_20261101_RECORD_CANDIDATE_GLOBAL_PRIORITY_UNKNOWN',
            best_located_public_lower_bound=target['best_verified_public_method_guarantee'],
            bounded_public_margin=target['margin'], public_search_date='2026-11-01',
            largest_found_in_this_reviewed_public_scope=True, record_candidate_not_certified_global=True,
            public_priority='UNKNOWN', method_originality='NOT_ESTABLISHED', latest_global_record_confirmed=False,
            public_search_summary=summary_path)
    assert targets
    m['user_requested_D3_20_26_bounded_primary_search'] = dict(
        status=summary['status'], date='2026-11-01', targets=targets,
        allowed_statement=summary['statement_allowed'], prior_research_exists=True,
        Comellas_absence_not_no_prior_work=True, two_complementary_branches_each_batches=2,
        two_complementary_branches_each_queries=8, root_global_table_access_terminal=True,
        global_certified=False, global_priority='UNKNOWN', method_novelty='NOT_ESTABLISHED',
        unresolved_gaps=summary['gaps'], user3250_lead=summary['user3250'],
        cap20_2791_source='Rajiv19_2783_plus_Delorme_section7_not_PolarStar',
        comparison_HTML=H, comparison_HTML_source=H + '.txt', summary=summary_path,
        no_new_graph_or_Lean=True, D3_new_degree_copy_field_dispatch='STOP')
    values='、'.join(f"{t['Delta']}/D3:{t['our_n']} 对已核方法保证{t['best_verified_public_method_guarantee']} (+{t['margin']})" for t in targets)
    row['distance_text'] += ' 最新用户专项primary检索已终态：' + values + '；本轮未定位达到本地的外部公开图，可标“截至2026-11-01本轮已查公开资料中最大实例／纪录候选”。这些参数已有研究，Comellas止16不是无人做。实时高degree表未取得、JGT增强原文未读、用户3250线索保留；globalpriority和innovation未确立。20的2791来自Rajiv19/2783+Delorme而非PolarStar。比较HTML与原样源码已持久链接，非新增图/参数/Lean/方法，D3新梯子仍STOP。'
    row['evidence_paths'] = list(dict.fromkeys(row.get('evidence_paths', []) + search_evidence + navigation))

d2 = rows[5]
dm = d2['other_metrics']
match = read(X + 'RESULT.json')
terminal = read(X + 'TERMINAL.json')
assert match['selected_generator_order'] == 7 and match['orbit_length_histogram'] == {'1': 8, '7': 14}
assert match['full_edges_per_accepted_permutation'] == 582 and terminal['all_processes_terminal']
assert abs(terminal['case_CPU_seconds'] - 10.585169327) < 1e-9
dm['structure_symmetry_sector_once']['later_status'] = 'SUPERSEDED_ONLY_C7_UNKNOWN_BY_ACTUAL_ORDER7_WITNESS_PRIOR_SIGNATURE_COUNTEREXAMPLE_PRESERVED'
dm['sector_matching_extension_actual'] = dict(status=match['status'], generator_order=7,
    fixed_vertices=match['actual_fixed_vertices'], orbit_histogram=match['orbit_length_histogram'],
    full_source_edges_per_permutation_checked=582, accepted_permutations=3,
    tested_sector_prefix=1026, full_sector_enumeration=False, first_order7_stop=True,
    no_full_automorphism_group_claim=True, batch_CPU=terminal['batch_CPU_seconds'],
    case_cumulative_CPU=terminal['case_CPU_seconds'], case_budget=20,
    all_processes_terminal=True, no_BFS_or_solver=True, note=X + 'NOTE.md')
dm['C7_preserving_internal_S10_S11_paper_exclusion'] = dict(status='INDEPENDENT_PAPER_SUPPORTED_SCOPED_EXCLUSION',
    source=[11, 2, 106], target_order=107, pin_sizes=[10, 11],
    fixed_scope='preserve_this_actual_C7_fix_new_z_change_only_old_edges_inside_invariant_S',
    S10_newroot_upper=104, S11_closed_domination_upper=105, required_source_order=106,
    earlier_numerical_MILP_UNKNOWN_not_rewritten=True, general107_excluded=False,
    noninvariant_pins_or_symmetry_breaking_or_cross_S_edits_not_excluded=True,
    stronger_pinset_only_prediction='UNTESTED_AT_THIS_SYNC_NOT_A_CONCLUSION', note=E)
dm['current_research_execution'] = dict(status='D2_NEW_COMPUTATION_PAUSED_FOR_USER_PUBLIC_SEARCH_NO_SOLVER_CONTINUATION',
    oldN8_n61_still_paused=True, no_timer_seed_or_model_continuation=True, new_graph_parameter_Lean_method_increments=[0, 0, 0, 0])
d2['distance_text'] += ' 后续matching传播已实际找到order7源自同构，8fixed+14个7cycles，582条源边逐一核过；case累计10.585169327/20CPU终态，首次order7即停，非完整自同构群。独立paper_S11_domination支持当前保持此C7、只改G[S]的S10/S11规则排除：S10新根至多104<107，S11源closed domination至多105<106；不把旧数值UNKNOWN改成solver已解、不一般排107。更强仅pinSET invariant而可打破内部C7的新预测未验，不能套此结论。D2新计算随用户专项检索先停，不续solver。'
d2['lesson_and_restart_condition'] += ' 实际order7替代此前C7UNKNOWN，但旧small-signature唯一性反例保留。纸面界改变下一步：停止此C7-preserving内部S10/S11规则；非对称pin/跨S改边/其它模型未被关闭，不能自动扩大排除或启动solver。'
d2_evidence=[X + n for n in ['PRED.md', 'NOTE.md', 'RESULT.json', 'TERMINAL.json', 'ORDER7_GENERATOR_AND_ORBITS.json']] + [E]
d2['evidence_paths'] = list(dict.fromkeys(d2['evidence_paths'] + d2_evidence))

d4 = rows[6]
fm = d4['other_metrics']
ad = V + 'D16_D4_16389_A_DISPOSITION.md'
bd = V + 'D16_D4_16389_B_DISPOSITION.md'
ar = V + 'D16_D4_16389_A_DELIVERED_GEMINI_RAW.json'
cr = V + 'D16_D4_16389_FINAL_C_REQUEST.json'
assert 'Root接受A' in (R / ad).read_text() and 'Root接受B' in (R / bd).read_text()
request = read(cr)
assert request['target'] == [16, 4, 16389, 128835]
Ath = 'e4b6c102-1c55-4739-82e4-d281acc2e835'
Bth = '5da20cd4-ab3f-4327-9df5-8d0e80d7eee3'
assert set(request['must_differ_from_threads']) == {Ath, Bth}
fm['degree16_exact_new_scope_reviews'].update(
    A=dict(status='ACTUAL_DELIVERED_SUCCESS_ROOT_FULLTEXT_DISPOSED_THREE_FACETS_PASS', thread=Ath,
        model='gemini-3.8-flash-high/high', root_read_chars=16731, math='PASS', formal='PASS', binding='PASS',
        priority='UNKNOWN', old_transport_UNKNOWN_preserved=True, completed_exact_scope_A_calls=1, raw=ar, disposition=ad),
    B=dict(status='ORIGINAL_COMPLETED_RESPONSE_RECOVERED_ROOT_FULLTEXT_DISPOSED_THREE_FACETS_PASS', thread=Bth,
        root_read_chars=11389, math='PASS', formal='PASS', binding='PASS', priority='UNKNOWN',
        original_call_no_resend=True, MCP_SUCCESS_not_fabricated=True,
        raw_text=V + 'D16_D4_16389_B_RECOVERED_RESPONSE.txt', disposition=bd),
    freshC=dict(status='ACTUAL_SINGLE_DISTINCT_FRESH_CALL_DISPATCHED_INFLIGHT_NOT_RETURNED',
        actual_exec_cell=925, request=cr, request_file_prepared_label_superseded_by_actual_root_dispatch=True,
        actual_dispatch_evidence='parent_root_actual_message_20261101_C925', thread='PENDING_ACTUAL_TOOL_RETURN',
        must_differ_from=[Ath, Bth], scope=[16, 4, 16389, 128835], final_verdict='PENDING', paid_retry=False),
    old_scope_PASS_inherited=False)
fg = fm['validated_graph_instances'][0]
assert fg['n'] == 16389 and fg['complete_Lean_graph_instance']
fg.update(external_A='ACTUAL_EXACT_SCOPE_THREE_FACETS_PASS_ROOT_DISPOSED',
    external_B='ACTUAL_ORIGINAL_RECOVERED_THREE_FACETS_PASS_ROOT_DISPOSED',
    external_fresh_C='ACTUAL_C925_INFLIGHT_NO_VERDICT', external_A_thread=Ath, external_B_thread=Bth,
    old17_or90_94_review_inherited=False)
fm['derived_user_graph_catalog_navigation'].update(current_comparison_HTML=H, current_comparison_HTML_source=H + '.txt', concrete_Lean_instances=46)
fm['current_user_D3_20_26_comparison'] = dict(status=summary['status'], statement=summary['statement_allowed'], summary=summary_path, HTML=H, global_priority='UNKNOWN', method_novelty='NOT_ESTABLISHED', global_certified_records=0)
d4['title'] = '16/D4/16389完整kernel实际Lean46；新scope A/B全文处置PASS，唯一distinctfresh C925在途'
d4['outcome_class'] = 'D16_D4_COMPLETE_KERNEL_A_B_ACTUAL_PASS_DISTINCTFRESH_C925_INFLIGHT'
d4['distance_text'] += ' 最新外审实际推进：root全文读A16731字、实际SUCCESS/e4线程三facetPASS；B原11389字恢复全文也已接受三facetPASS，不伪造MCP SUCCESS、不重发B。原丢失A transportUNKNOWN历史保留，只计一次完成A。唯一distinctfresh C实际cell925在途，thread待实际返回，未有C判定、不借旧D3/17PASS。A纠正文案Fin192非未经证明Z192、只有global vertex全相等才收缩holding、单条长4walk不单独证明lower；原kernel/BFS分别给上下界。七组D3本轮largest-found候选及HTML另有明确检索范围，global0不变。'
d4['lesson_and_restart_condition'] += ' 新D4 A/B已实际完成，只等同一唯一C925真实终态；不重发、不借旧scope，不把pending标PASS。16389原图计数不变。'
d4_evidence=[ad, bd, ar, cr, V + 'D16_D4_16389_B_RECOVERED_RESPONSE.txt']
d4['evidence_paths'] = list(dict.fromkeys(d4['evidence_paths'] + d4_evidence + navigation + [summary_path]))

evidence = list(dict.fromkeys(search_evidence + navigation + d2_evidence + d4_evidence))
assert all((R / x).is_file() for x in evidence)
assert (R / H).stat().st_size == (R / (H + '.txt')).stat().st_size == 33556
raw = W / f'updates/{B}_ROWS.json'
raw.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
calls=[]
def call(*cmd):
    p=subprocess.run([str(x) for x in cmd], cwd=R, text=True, capture_output=True)
    calls.append(dict(command=[str(x) for x in cmd], returncode=p.returncode, stdout=p.stdout, stderr=p.stderr))
    assert p.returncode == 0, (cmd, p.stdout, p.stderr)
    return p.stdout

print(call(sys.executable, R / 'research/ddp/more_graphs_20261027/sync_additional_probes.py', raw).strip())
L = read('research-wiki/DDP_METHOD_LEDGER.json')
assert tuple(L[k] for k in keys) == (421, 152, 43, 46)
assert (L['valid_new_graph_examples'], L['mathematically_improved_parameter_pairs'], L['known_publicly_dominated_graph_examples']) == (104, 4, 43)
nav = '[当前43组公开比较HTML](../' + H + ') · [HTML原样源码](../' + H + '.txt) · [七组D3本轮专项检索](../' + summary_path + ')。截至2026-11-01所查公开资料中最大实例／纪录候选7组；有既往研究，globalpriority及innovation未确立，3250线索保留。152图／43参数／Lean46不变。D2真实C7与当前保持C7的内部S10/S11排除已存，更强pinset-only预测未验；D2新计算先停。D4新scope A/B全文实际三facetPASS，唯一distinctfresh C925在途未返，不借旧scope。'
gap = W / 'gap_map.md'
text = gap.read_text()
assert B not in text
text = text.replace('152行／43参数／Lean45；', '152行／43参数／Lean46；', 1)
pos = text.find('<!--', 4) if text.startswith('<!-- GRAPH_CATALOG_NAVIGATION_ONLY_20261101 -->') else 0
assert pos >= 0
gap.write_text(text[:pos] + '<!-- ' + B + ' -->\n' + nav + '\n\n' + text[pos:])
comments = W / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
comments.write_text(comments.read_text() + f'''\n\n## {now} 用户专项：D3七组本轮largest-found候选与HTML入口；D2真实C7／D4 A-B终态\n\n{nav}\n\n七组Δ20..26本地3840／3984／4192／4336／6160／7242／7532，对已核公开方法保证2791／2928／3294／3549／6144／7225／7514分别+1049／1056／898／787／16／17／18。两个互补分支各两batch八queries、root高degree表入口均已终态；未定位达到本地的外部构造，允许明确标为截至2026-11-01本轮已查公开资料中最大实例／纪录候选，不要求证明未公开对象不存在。已有高degree研究，Comellas止16不是无人做；实时Wiki未取得、原JGT增强全文未读、人工3250线索保留。20的2791是Rajiv19/2783+Delorme而非PolarStar。不能据此确立globalpriority或方法创新，全球认证0，D3新构造梯子继续STOP。\n\nD2 matching传播实际得到order7、8fixed+14个7cycles、582边全核，case10.585169327/20CPU终态，旧signature反例保留。独立paper_S11_domination严格排当前保持该C7且只改G[S]的S10/S11；不把旧MILP UNKNOWN改成solver已解、不一般排107，也不提前接受更强pinset-only新预测。用户专项检索期间不续D2 solver。\n\nD4/16389完整原目标已计Lean46不重复。A16731字与B原11389字均root实际全文三facetPASS，实际A e4b6线程／B5da20线程；A原未观测投递历史UNKNOWN保留，新完成A只计一次；B原恢复不伪造toolSUCCESS或重发。root实际唯一distinctfresh C925在途、thread待回，C仍未PASS，不借旧D3/17审阅。当前152／43／46、stage48／40、main104／4、known43/outside45／38/global0全部不变。只七个既有节点、日志和导航增量；0数学／网络／图／BFS／Lean／solver／互审调用，不动根文件或冻包。\n''')
helper = R / 'aris_repo/tools/research_wiki.py'
call(sys.executable, helper, 'log', W, 'UserRequestedD3caps20to26_twoComplementaryPrimaryBranchesEach2batches8queriesPlusRootGlobalTableAccessAllTerminal_noExternalAtLeast3840_3984_4192_4336_6160_7242_7532Located_knownMethodGuarantees2791_2928_3294_3549_6144_7225_7514_allowedLargestInstancesInPublicSourcesReviewed20261101_RecordCandidates7_notGlobalCertificate_notInnovationProof_priorResearchExists_ComellasStop16NotNoResearch_cap20Rajiv19_2783plusDelormeNotPolarStar_user3250Retained_realTimeWikiAndJGTFulltextGaps. PersistentCurrentComparisonHTMLandOriginalSource33556BLinked. D2actualC7order7_8fixed14cycles_All582EdgesChecked_case10.585169327of20_terminal_independentPaperOnlyC7preservingInternalS10S11Excluded_general107NotExcluded_strongerPinsetOnlyPredictionUntested_D2newComputePausedNoSolverContinuation. D4exactA16731andB11389RootFulltextThreeFacetsPASS_actualThreadsE4and5da_originalATransportUnknownPreserved_onlyOneCompletedA_originalBRecoveredNoResendNoFabricatedMCPSuccess_uniqueDistinctFreshC925ActuallyInflightThreadPendingNoVerdict_noOldScopeInheritance. Existing7rowsLedger421_counts152_43Lean46stage48_40main104_4known43outside45_38global0unchanged_noNewMethod_noMathGraphBFSLeanSolverWebPaidReviewRootownedFrozenWrites.')
call(sys.executable, helper, 'rebuild_index', W)
call(sys.executable, helper, 'rebuild_query_pack', W)
(W / f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls, ensure_ascii=False, indent=2) + '\n')
assert len(calls) == 4 and all(x['returncode'] == 0 for x in calls)
query = (W / 'query_pack.md').read_text()
assert H in query and 'research/graph_catalog.html' in query and 'C925' in query
for i, row in zip(ids, rows):
    assert row['title'] in (W / 'experiments' / (i + '.md')).read_text()
receipt = dict(status='PASS_EXISTING_SEVEN_NODES_USER_D3_LARGEST_FOUND_HTML_D2_C7_D4_ACTUAL_AB_C925',
    updated_UTC=now, ledger_records=421, records_added=0, records_updated=7,
    named_legal_graphs=152, legal_parameter_pairs=43, complete_formula_Lean=46,
    stage_graphs=48, stage_pairs=40, saved_main_graphs=104, saved_main_pairs=4,
    known_publicly_dominated=43, outside_graphs=45, outside_pairs=38, global_certified_records=0,
    new_graph_parameter_Lean_method_increments=[0, 0, 0, 0],
    D3_record_candidates_in_reviewed_scope=7, D3_primary_queries_this_sync=0,
    inherited_search_each_branch_batches=2, inherited_search_each_branch_queries=8,
    current_comparison_HTML=H, current_comparison_HTML_source=H + '.txt', HTML_size=33556,
    global_priority='UNKNOWN', innovation='NOT_ESTABLISHED', user3250_clue_retained=True,
    D2_actual_C7_order=7, D2_case_CPU=terminal['case_CPU_seconds'],
    D2_exclusion_scope='this_C7_preserving_internalS10S11_only', stronger_pinset_prediction_untested=True,
    D4_A='ACTUAL_ROOT_DISPOSED_THREE_FACETS_PASS', D4_B='ACTUAL_ROOT_DISPOSED_THREE_FACETS_PASS',
    D4_C='ACTUAL_UNIQUE_C925_INFLIGHT_THREAD_PENDING_NO_VERDICT',
    evidence_paths_checked=len(evidence), actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',
    static_scope_check='PASS_existing7nodes_unchanged421_152_43_46_HTMLcatalogC925QueryNavigation_fourActualHelperCalls',
    math_graph_BFS_Lean_solver_web_paid_runs_this_sync=0, root_owned_files_modified=False,
    expert_or_frozen_packets_modified=False, writes_stopped_after_receipt=True)
(W / f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(receipt, ensure_ascii=False))
