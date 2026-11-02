"""Small canonical Wiki delta; no research computation or full-Wiki import."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
import json
import re
import runpy

R = next(p for p in Path(__file__).resolve().parents if (p / 'research-wiki').is_dir())
W = R / 'research-wiki'
S = 'research/ddp/two_successful_methods_20261101/'
OUT = R / S / 'wiki_sync'
LABEL = 'STALE_RECORD_TRANSFER_TERMINALS_20261101'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def read(path):
    return json.loads((R / path).read_text())


def evidence(directory, names):
    result = [directory + name for name in names]
    assert all((R / p).is_file() for p in result)
    return result


def raw(rid, title, family, degree, diameter, baseline, hypothetical, scope,
        outcome, distance, next_condition, metrics, paths):
    return dict(id=rid, title=title, family=family,
        idea_family='idea:ddp-open-parameter-construction-20261026',
        date='2026-11-01', record_type='necessary_route_or_input_transfer_gate',
        target_Delta=degree, target_D=diameter, savedL=baseline,
        baseline_date='2026-11-01 actual current Comellas main; staleness uses matching-order dates, not page dates',
        n=dict(actual=None, hypothetical=hypothetical), actual_graph_Delta=None,
        actual_D=None, actual_D_scope='No full target graph was generated; source legality inherited only',
        ordinary_bad_unordered_pairs=None, ordinary_bad_target_D=diameter,
        scope=scope, outcome_class=outcome, new_lower_bound=False,
        distance_text=distance, lesson_and_restart_condition=next_condition,
        restart_condition=next_condition,
        unclosed_gap='No accepted target graph; broader rules beyond the exact recorded scope remain open.',
        other_metrics=dict(new_graphs=0, new_parameter_pairs=0,
            new_Lean_instances=0, new_independent_method_claims=0, **metrics),
        evidence_paths=paths)


L0 = read('research-wiki/DDP_METHOD_LEDGER.json')
counts_keys = ['validated_named_graph_examples', 'validated_named_parameter_pairs',
               'complete_Lean_graph_instances', 'saved_main_table_improvement_graph_examples',
               'saved_main_table_improvement_parameter_pairs']
before_counts = {k: L0[k] for k in counts_keys}
assert tuple(before_counts[k] for k in counts_keys[:3]) == (152, 43, 46)
before_count = L0['record_count']

P8 = S + 'stale_record_transfer_d8D4/loz1100_split_gate/'
split = read(P8 + 'RESULT.json')
split_term = read(P8 + 'TERMINAL.json')
assert split['status'] == 'EXACT_NO_SINGLE_SPLIT_DUE_TO_SINGLETON_R4_SUPPORT'
assert split['singleton_target_count'] == 95 and not split_term['running']
rows = [raw('ddp-stale-d8d4-loz1100-single-split-boundary-20261101',
    '长期8D4=1100拆点迁移：95个唯一首步排全部单root相邻拆分，未生1101图',
    'vertex splitting and matching', 8, 4, 1100, 1101,
    'Only the inherited RIGHT-law C20 semidirect_2 Z55 Loz1100 source. Replace one vertex by two adjacent roles, partition all8old neighbors into nonempty disjoint A/B, freeze all other edges. Cayley translation fixes root0. Not multiple splits or other rewiring.',
    split['status'],
    '实际root0距离层(1,8,56,361,674)；674个R4目标中95个firsthop singleton。target2唯一首步533，旧4路0–533–459–223–2；两侧不能同时分到533，故逻辑排全部254有向／127互补分区，未枚分区、未生1101图。近端≤3可容许一次role-edge插步，不是失败点。',
    'STOP this exact single-split source/rule. A further experiment needs changed connection rules, multiple split vertices or another source; do not repeat this root/partition batch.',
    dict(source_order=1100, source_degree=8, source_D=4,
        source_legality='inherited_not_revalidated', actual_N1=split['actual_N1'],
        actual_R4=split['actual_R4'], firsthop_support_size_histogram=split['firsthop_support_size_histogram'],
        singleton_target_count=95, witness=split['singleton_witness'],
        excluded_oriented_partitions=254, excluded_complement_classes=127,
        partitions_actually_enumerated=0, new_root0_route_support_calculations=1,
        source_allroot_BFS=0, charged_CPU=split_term['charged_case_CPU_seconds'],
        actual_process_CPU=split_term['actual_process_CPU_seconds'],
        conservative_preparation_charge=0.1, CPU_budget=10, terminal=True),
    evidence(P8, ['PRED.md', 'NOTE.md', 'RESULT.json', 'TERMINAL.json',
                  'SOURCE_RECIPE_INPUT.json', 'R4_BOUNDARY_SUPPORTS.csv', 'run_once.py']))]

P2 = S + 'stale_record_transfer_d8D4/c30_f2_fivecover_gate/'
binary = read(P2 + 'RESULT.json')
binary_term = read(P2 + 'TERMINAL.json')
assert binary['status'] == 'STOP_LITERAL_F2_SPECIALIZATION_NOT_DEFINED'
assert binary['minimum_le4_nonbacktracking_walk_count'] is None and not binary_term['route_count_run']
rows.append(raw('ddp-stale-d8d4-c30-gf4-binary-restriction-fivecover-input-20261101',
    '8D4五cover输入门：accepted F4/C30字面矩阵不保F2³，240与1200均未构造',
    'Route-chart source transfer', 8, 4, 1100, 1200,
    'Only the proposed standard F2^3 restriction of the accepted literal GF4/C30 edge-local rule, before any ordinary5cover. Not all binary edge-local maps, alternative embeddings or general8D4 covers.',
    binary['status'],
    '120个edge-local GF4矩阵的非binary系数共284项（α152、α+1共132）；controller0/port0在noise0将binary e2映到(α,0,α+1)。该字面rule未定义F2³闭源，故不存在可继承的240邻接，NB≤4五cover容量未运行；不是“某个已造240图的cover无解”。',
    binary['next_step'],
    dict(conditional_base_order=240, conditional_cover_order=1200,
        accepted_source=dict(n=1920, degree=16, q=4, reproduction_only=True),
        binary_source_status=binary['binary_source_status'], source_rule=binary['source_rule'],
        counterexample=binary['witness'], minimum_NB_count=None, actual_pair=None,
        NB_capacity_gate_run=False, source_BFS=0,
        CPU=binary['CPU'], CPU_receipt_kind='measured subtotal; brief preparation/path failure not individually metered',
        previous_binary_global_matrix_exclusion_scope=binary['prior_exclusion'], terminal=True),
    evidence(P2, ['PRED.md', 'NOTE.md', 'RESULT.json', 'TERMINAL.json'])))

P9 = S + 'stale_record_transfer_d4D5/alternative41_ninecover_gate/'
nine = read(P9 + 'RESULT.json')
nine_term = read(P9 + 'TERMINAL.json')
assert nine['status'] == 'ALL_THREE_NEW_SOURCES_EXACT_NINECOVER_OBSTRUCTION'
assert [(x['source_id'], x['minimum_count'], x['tight_pair']) for x in nine['sources']] == [
    ('N1', 1, [11, 11]), ('N2', 3, [0, 0]), ('N3', 1, [1, 1])]
nine_sources = [{k: x[k] for k in ['source_id', 'actual_fetch_URL', 'input_vertices',
    'input_edges', 'input_degree_histogram', 'literal_edge_set_equals_old_Allwright1a',
    'minimum_count', 'tight_pair', 'tight_pair_walks', 'tight_pair_walk_length_histogram',
    'ordered_pairs_counted', 'nonbacktracking_walks_including_length0_total']} for x in nine['sources']]
rows.append(raw('ddp-stale-d4d5-messieres-three41-any-ninecover-capacity-20261101',
    '4D5目标369的新源对照：N1/N2/N3返回容量仅1/3/1，排各自任意普通九cover',
    'ordinary graph-cover transfer', 4, 5, 364, 369,
    'Only the actual October2026 Michel de Messieres N1,N2,N3 source graphs listed by Comellas, each41vertices/82edges. Any ordinary9sheet local-bijection cover of each fixed source, including arbitrary permutation voltages; not source editing, added fiber edges or all369vertex graphs. Old Allwright1(a) C9/affine exclusions are inherited without rerun.',
    nine['status'],
    '三个新source各枚长度0..5非回退walk19885条／1681orderedpair。最紧N1(11,11)=1与N3(1,1)=1均仅空路；N2(0,0)=3为空路及0–37–4–16–40–0两方向。每个槽不足9，任何普通9sheetcover从固定lift根只能到不足9个同fiber端点，故缺返回路线而非电压取值不佳；“至少一源过门”预测被推翻。',
    'STOP these three fixed-source ordinary9covers; no C9/S9 voltage solver or source-label variant. A new authorized rule must change actual source/routing structure, not merely the deck group.',
    dict(source_variants=nine_sources, prediction=nine['prediction'],
        required_sheet_endpoints=9, count_lengths=[0, 5],
        shortest_lift_projects_nonbacktracking_proof=True,
        source_D3_and_nonisomorphism='primary claim inherited; not source BFS/isomorphism checked',
        new_source_BFS=0, official_adjlistt_typo_404=True,
        corrected_adjlist_actual_downloads=3,
        first_parse_failure_preserved=True,
        charged_CPU=nine_term['charged_case_CPU_seconds'], CPU_budget=10,
        first_failure_charged_CPU=nine_term['previous_parser_failure_charged_CPU_seconds'],
        no_timer_reset=True, terminal=True),
    evidence(P9, ['PRED.md', 'NOTE.md', 'RESULT.json', 'TERMINAL.json',
        'INITIAL_PARSE_FAILURE_RESULT.json', 'INITIAL_PARSE_FAILURE_TERMINAL.json',
        'source_N1.ROUTE_CAPACITY.json', 'source_N2.ROUTE_CAPACITY.json',
        'source_N3.ROUTE_CAPACITY.json', 'run_once.py'])))

P70 = S + 'stale_record_transfer_d3D5/two_helper_threecut/'
first = read(P70 + 'RESULT.json')
first_term = read(P70 + 'TERMINAL.json')
second = read(P70 + 'adjacent_helpers_repair/RESULT.json')
second_term = read(P70 + 'adjacent_helpers_repair/TERMINAL.json')
assert first['complete'] and second['complete']
assert not first['hit'] and not second['hit']
assert first['configurations'] == 1663900 and second['configurations'] == 7366590
assert second['both_helpers_all_old_PASS'] == 168 and not second_term['active_processes']
rows.append(raw('ddp-stale-d3d5-afy70-threecut-twohelpers-repair-20261101',
    '3D5旧70源三匹配删边加两helper：非邻规则全NO；邻接加oldrepair修互距但168案损旧路线',
    'vertex splitting and matching', 3, 5, 70, 72,
    'One fixed literal AFY70 cubic/D5 source. Rule1 deletes exactly3disjoint old edges, adds2nonadjacent helpers and partitions6endpoints3+3. Rule2 uses the same3matching cuts, one nondouble old-old endpoint repair, partitions remaining4endpoints2+2 between adjacent helpers. No other edge edits or source changes.',
    'EXHAUSTIVE_TWO_FIXED_RULES_NO72',
    '第一规则166390匹配×10=1663900配置全遍；1663872先漏helper70→old，余28虽到全old≤5却helper互距6。新相邻helper＋oldrepair规则真实修复互距，2455530合法repair×3=7366590全遍：7365708漏helper70old、714漏helper71old；168案两helper到全old≤5且互距1，但全部old-old仍>5。首例cutIDs[0,5,7]、repair(0,4)、pins70[1,3]/71[2,56]留下oldpair(0,17)。不是未执行oldold检查就推NO。',
    'STOP both fixed AFY70 patterns; no further timer or nearby repair batch. Future research requires a changed structural premise or another source and must preserve the distinction between helper coverage and old-old damage.',
    dict(first_rule=dict(status=first['status'], matchings=first['matchings'],
        configurations=first['configurations'], first_failure_counts=first['first_failure_counts'],
        remaining_helper_pair_distance=first['remaining28_helper_pair_distance'],
        old_R4_union_is_diagnostic_not_necessary_filter=True,
        exact_check_scope=first['exact_check_scope']),
        adjacent_repair_rule=dict(status=second['status'], matchings=second['matchings'],
            valid_repair_choices=second['valid_repair_choices'],
            rejected_duplicate_repairs=second['rejected_duplicate_repairs'],
            configurations=second['configurations'], first_failure_counts=second['first_failure_counts'],
            both_helpers_all_old_PASS=168, all_remaining_old_old_rejected=168,
            first_old_failure=second['first_old_failure']),
        cumulative_measured_CPU=second_term['cumulative_case_measured_CPU_seconds'], CPU_budget=20,
        CPU_accounting_note=second['preparation_note'],
        source_validity_D5_BFS_repeated=False, full72root_batches=0,
        new_helper_route_tests_are_candidate_gate_not_source_reverification=True, terminal=True),
    evidence(P70, ['PRED.md', 'NOTE.md', 'PROOF.md', 'RESULT.json', 'TERMINAL.json',
        'adjacent_helpers_repair/PRED.md', 'adjacent_helpers_repair/NOTE.md',
        'adjacent_helpers_repair/PROOF.md', 'adjacent_helpers_repair/RESULT.json',
        'adjacent_helpers_repair/TERMINAL.json'])))

# Only one existing node needs its formerly pending review field corrected.
# Actual root disposition, not the older math-release snapshot, owns the review state.
d4id = 'ddp-d15-d4-current15552-source-gap-20261027'
d4 = copy.deepcopy(next(x for x in L0['rows'] if x['id'] == d4id)['source_record'])
CD = S + 'reviews/D16_D4_16389_FINAL_C_DISPOSITION.md'
CR = S + 'reviews/D16_D4_16389_FINAL_C_GEMINI_RAW.json'
cd = (R / CD).read_text()
assert '18981' in cd and '81f0a971-8801-49b0-aca1-dbf71b602fc0' in cd
assert 'math PASS' in cd and 'Global priority remains UNKNOWN' in cd
dm = d4['other_metrics']
review = dm['degree16_exact_new_scope_reviews']
review['freshC'] = dict(status='ACTUAL_SINGLE_DISTINCT_FRESH_C925_SUCCESS_ROOT_FULLTEXT_THREE_FACETS_PASS',
    actual_exec_cell=925, thread='81f0a971-8801-49b0-aca1-dbf71b602fc0',
    distinct_from_A_B=True, root_read_characters=18981,
    math='PASS', formal='PASS', binding='PASS', priority='UNKNOWN',
    old_scope_PASS_inherited=False, paid_retry=False, raw=CR, disposition=CD)
review['all_A_B_fresh_C_actual_received_and_root_disposed'] = True
for graph in dm.get('validated_graph_instances', []):
    if graph.get('n') == 16389:
        graph.update(external_fresh_C='ACTUAL_EXACT_SCOPE_THREE_FACETS_PASS_ROOT_DISPOSED',
            external_fresh_C_thread=review['freshC']['thread'])
d4['title'] = '16/D4/16389完整kernel实际Lean46；原目标A/B与distinctfresh C925全部actualPASS，priorityUNKNOWN'
d4['outcome_class'] = 'D16_D4_COMPLETE_KERNEL_A_B_FRESH_C_ACTUAL_THREE_FACETS_PASS'
d4['distance_text'] += ' 后续actualC925完整18981字已root接受math/formal/bindingPASS，thread81f0a971与A e4/B5da不同；A/B/finalC本scope全终态，globalpriority仍UNKNOWN，不增加已计152/43/46。'
d4['lesson_and_restart_condition'] += ' 当前原目标外审已闭合，勿恢复旧C925pending、重投或借旧scope；旧transport历史不删除。'
d4['evidence_paths'] = list(dict.fromkeys(d4['evidence_paths'] + [CD, CR]))
rows.append(d4)

rawpath = OUT / f'{LABEL}_ROWS.json'
rawpath.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
common = runpy.run_path(str(R / 'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
helper = common['helper']
# Canonical node API normally regenerates the entire index/query pack. The root
# has just prepended a human recovery block, so defer that broad regeneration.
helper.rebuild_index = lambda *args, **kwargs: None
helper.rebuild_query_pack = lambda *args, **kwargs: None
normalized = []
with (OUT / f'{LABEL}_NODE_CALLS.log').open('w') as log, contextlib.redirect_stdout(log):
    for source in rows:
        row = common['normalize'](source)
        row['goal']['baseline_date'] = source['baseline_date']
        common['write_node'](row)
        normalized.append(row)

L = read('research-wiki/DDP_METHOD_LEDGER.json')
assert {k:L[k] for k in counts_keys} == before_counts
existing = {row['id']:row for row in L['rows']}
newids = [row['id'] for row in normalized if row['id'] not in existing]
for row in normalized:
    existing[row['id']] = row
L.update(rows=list(existing.values()), record_count=len(existing), updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))] = len(rows)
(W / 'DDP_METHOD_LEDGER.json').write_text(json.dumps(L, ensure_ascii=False, indent=2) + '\n')

def table_row(row):
    safe = common['safe']
    title = f"[{safe(row['title'])}](experiments/{row['id']}.md)"
    ev = row['evidence_paths'][0]
    return ('| ' + title + ' | ' + safe(common['goal_text'](row)) + ' | '
        + safe(common['gap_text'](row)) + ' | ' + safe(row['exact_scope'])
        + '；' + safe(row['lesson']) + f'；[原始证据](../{ev}) |')

mdpath = W / 'DDP_METHOD_LEDGER.md'
md = mdpath.read_text()
# Correct only the existing D16 row; do not re-sort/re-render any family.
d4norm = next(row for row in normalized if row['id'] == d4id)
md = '\n'.join(table_row(d4norm) if f'](experiments/{d4id}.md)' in line else line
               for line in md.split('\n'))
md = md.replace(f'本页有{before_count}条记录；不以此宣称{before_count}种独立方法。',
    f'本页有{len(existing)}条记录；不以此宣称{len(existing)}种独立方法。', 1)
md += (f'\n\n<!-- {LABEL} -->\n## {NOW} 长期主表目标迁移门：最小增量\n\n'
       '| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n'
       '|---|---|---|---|\n' + '\n'.join(table_row(row) for row in normalized if row['id'] in newids)
       + '\n\n本增量为四个实验节点，不是四种独立新方法；没有新合法图、参数或具体Lean。\n')
mdpath.write_text(md)

links = '；'.join(f"[{row['title']}](experiments/{row['id']}.md)" for row in normalized if row['id'] in newids)
navigation = (f'<!-- {LABEL} -->\n'
    f'### 2026-11-01 实际迁移门终态：两8D4、三新41源与AFY70两规则\n\n'
    '两8D4均STOP：Loz1100单拆点95个唯一首步排全部254分区；F4/C30不保F2³，未造240、未运行五cover容量。'
    '不同来源N1/N2/N3的长度≤5非回退返回容量1/3/1<9，排各自任意普通九sheetcover，非一般369不存在。'
    'AFY70首规则1663900全NO；相邻helpers＋oldrepair新规则7366590全NO，168案已修helper互距却仍损旧点路线。'
    '所有batch已实际终态，不续timer、不增图；152／43／Lean46、旧n61暂停不变。D16原目标A/B/freshC925均actual三facetPASS，priorityUNKNOWN。\n\n'
    + links + '\n\n')
preserved = {}
for filename in ['index.md', 'query_pack.md', 'gap_map.md']:
    path = W / filename
    text = path.read_text()
    start = '<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->'
    end = '<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
    assert text.startswith(start) and end in text
    position = text.index(end) + len(end)
    prefix = text[:position]
    assert LABEL not in text
    text = text[:position] + '\n\n' + navigation + text[position:]
    if filename == 'index.md':
        m = re.search(r'^## Experiments \((\d+)\)$', text, re.M)
        assert m
        text = text[:m.start()] + f'## Experiments ({int(m[1])+len(newids)})' + text[m.end():]
        at = text.index('\n', m.start()) + 1
        entries = ''.join(f"- `exp:{row['id']}` — {row['title']} [no]\n"
                          for row in normalized if row['id'] in newids)
        text = text[:at] + entries + text[at:]
        text = re.sub(r'^- `exp:' + re.escape(d4id) + r'` — .*$',
                      '- `exp:' + d4id + '` — ' + d4norm['title'] + ' [partial]', text, flags=re.M)
    assert text[:position] == prefix
    path.write_text(text)
    preserved[filename] = dict(human_revision_block_preserved_exact=True, new_navigation_added=True)

helper.append_log(str(W),
    'STALE_RECORD_TRANSFER_TERMINALS_20261101: four scoped terminal experiment nodes added through existing canonical helper; '
    'two8D4 gates STOP, three new41source any9cover capacity deficits1/3/1, AFY70 nonadjacent and adjacent-oldrepair rules both exactNO; '
    'second rule repairs helper mutual distance but168 remaining configurations fail old-old routes. '
    'No graph/BFS/solver/Lean/web rerun. Existing D16 actualC925 PASS field corrected from real root disposition. '
    '152graphs/43pairs/Lean46 preserved; oldn61paused; original human recovery blocks byte-for-byte preserved, no fullWiki reimport.')

after = read('research-wiki/DDP_METHOD_LEDGER.json')
assert {k:after[k] for k in counts_keys} == before_counts
assert len(newids) == 4 and after['record_count'] == before_count + 4
assert all((R / row['wiki_path']).is_file() for row in normalized)
receipt = dict(status='PASS_CANONICAL_MINIMAL_TERMINAL_DELTA', updated_UTC=NOW,
    records_before=before_count, records_after=after['record_count'],
    records_added=4, records_updated=1, new_experiment_ids=newids,
    existing_review_status_corrected=d4id,
    canonical_helper='research/ddp/wiki_backfill_20261027/sync_ledger.py normalize/write_node; aris_repo/tools/research_wiki.py add_experiment',
    full_index_query_rebuild_deferred_to_preserve_human_blocks=True,
    raw_rows=str(rawpath.relative_to(R)), helper_log=str((OUT / f'{LABEL}_NODE_CALLS.log').relative_to(R)),
    original_human_navigation_blocks=preserved,
    counts_unchanged=before_counts, increments_graph_parameter_Lean_method=[0,0,0,0],
    source_validation_BFS_solver_Lean_web_or_paid_calls=0,
    source_scope='four experimental nodes; AFY70 two actual terminal rules combined in one, N1N2N3 combined in one',
    old_n61='PAUSED_UNCHANGED', D16_A_B_freshC='ACTUAL_SCOPE_PASS_PRIORITY_UNKNOWN',
    root_STATE_REPORT_progress_HTML_frozen_modified=False,
    writes_limited_to_Wiki_and_stage_wiki_sync=True, all_writes_complete=True)
(OUT / f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(receipt, ensure_ascii=False))
