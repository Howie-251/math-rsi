"""Upgrade the existing fixed-natural364 helper lower-bound node, add0."""
from pathlib import Path
import copy
import json
import runpy
import time

ROOT = Path(__file__).resolve().parents[4]
S = Path(__file__).resolve().parent
W = ROOT / 'research-wiki'
D = ROOT / 'research/ddp/two_successful_methods_20261101/retained_edge_transfer/natural364_cooperative_helpers14_read'
PREFIX = 'NATURAL364_HELPERS14_COMPLETE_TERMINAL_20261102'
SLUG = 'ddp-h3-364-helper-minimum13-20261027'
SPECIFIC13 = 'ddp-h3-helper13-tree-class-exclusion-20261027'
MARKER = '<!-- ' + PREFIX + ' -->'
started = time.process_time()
H = runpy.run_path(str(S / 'sync_source650_then_d4_binary_terminals_20261102.py'))
load, relative = H['load'], H['relative']
now = H['stamp']()
prep = load(S / 'NATURAL364_HELPERS14_PREPARED_UPDATE_20261102.json')
root = load(D / 'ROOT_DISPOSITION.json')
result = load(D / 'unicyclic_topology_gate/RESULT.json')
assert root['status'] == 'ROOT_ACCEPTED_FIXED_SOURCE_HELPERS1_TO14_PRESERVED_EDGE_NO_STOP'
assert root['all_numeric_terminal'] and root['final_case_CPU'] == 0.880238423 and root['casecap'] == 10
assert root['first_unexcluded_helper_count'] == 15
assert result['canonical_topologies_checked'] == 1930 and result['G1_rejected'] == 1910 and result['G2_rejected'] == 20
assert result['surviving_topologies'] == 0
assert all('first_min_ordered_size14_decorations' in row and 'raw_ordered_size14_decorations' not in row for row in result['by_cycle'].values())
assert result['case_CPU'] == 0.880238423 and result['new_numeric_CPU'] == 0.130238423
ledger_path = W / 'DDP_METHOD_LEDGER.json'
ledger = load(ledger_path)
assert ledger['record_count'] == len(ledger['rows']) == 460
positions = [i for i, row in enumerate(ledger['rows']) if row['id'] == SLUG]
assert len(positions) == 1
pos = positions[0]
before = copy.deepcopy(ledger)
historical = copy.deepcopy(ledger['rows'][pos]['source_record'])
assert historical == prep['proposed_source_record']['other_metrics']['historical_1to13_source_record_before_helpers14_20261102']
specific13_before = copy.deepcopy(next(row for row in ledger['rows'] if row['id'] == SPECIFIC13))
assert not (S / (PREFIX + '_RECEIPT.json')).exists()
old, human, index_before = H['page_snapshot'](MARKER)
md_before = (W / 'DDP_METHOD_LEDGER.md').read_text()
assert MARKER not in md_before
raw = copy.deepcopy(prep['proposed_source_record'])
raw.update({
    'outcome_class': root['status'],
    'new_lower_bound': False,
    'baseline_date': 'Inherited natural364/714 fixedhost and sourceD5 proof; not public364/728 or a new table comparison',
    'distance_text': '旧1..13保边/无oldold helpers严格NO和3276triples/81900(T,parent)缓存原样继承，不重跑。k14 tree由旧good0作纸面排除；剩14edge connectedunicyclic、a_h=4−d_H的必要拓扑域只需cycle3..7及depth3/2/2/1/1。实际1930canonical：G1全部helper到owner<=4排1910，G2仅parentdegree>=3的leaf到owner<=3再排20，0survivor；degree2parent不误套G2。first_min_ordered_size14_decorations只是first-min剪枝后的ordered计数，字段标签已改、数值/1930不重跑。固定自然364/714架构1..14关闭，minimumhelpers15/firstunexcludedorder379仅必要下界，不声称379存在、一般378图NO或任意finiteH不可能。case.880238423/10，0sourceBFS/旧mask/assignment/图/Lean/solver/ARIS。',
    'failure_or_result': 'Inherited1..13NO + k14treepaperNO + complete1930canonicalunicyclicG1/G2NO implyatleast15helpers inthisfixedpreserved-edge/no-oldold/max4/D5architecture only.',
    'positive_guarantees': [
        'Alloriginalsourceedges retained,noaddedoldold,max4,actual28degree3ports; notpublic364/728 all4regularsource.',
        'Old1..13strictscope andold3276/81900uniformgood0data areinherited unchanged. No oldsource/ball/mask orHallrerun.',
        'k14tree closesbyolduniformtripleobstruction,notanewtreeorportassignmentenumeration.',
        'Remainingk14H isconnectedunicyclicwith14edgesandspokecount4−degree; cycle3..7/attachmentdepthbounds,rootedmultisetsanddihedralcanonicalizationcoverallnecessarytopologies.',
        'G1checks allhelpers-to-owners,notonlyownerpairs. G2onlyforleafwithparentdegree>=3,neverdegree2. All1930canonicals areexcludedindependentlyofportassignment.',
        'Counterlabelisfirst_min_ordered_size14_decorations,notallrawordereddecorations; numbersunchanged,no rerun.',
        'Firstunexcludedk15/order379 isonlyanecessaryboundary,notconstructionornewrecord. Noautomatick15orclaimaboutH19/otherk>=15.'
    ]
})
m = raw['other_metrics']
m['native_stage_result'] = result
m['root_disposition'] = root
m['samecase_CPU'] = 0.880238423
m['case_cap'] = 10
m['new_numeric_CPU'] = 0.130238423
m['raw_ordered_field_interpretation'] = 'Correctedtofirst_min_ordered_size14_decorations; first-min prunedordered,notfullorderedrawdomain; no numeric rerun'
m['root_accepted'] = True
m['old_specific_k13_node_unchanged'] = SPECIFIC13
m['k15_search_authorized_or_run'] = False
m['H19_included'] = False
extra = [D / name for name in ['ROOT_DISPOSITION.json', 'NOTE.md', 'HELPER14_TERMINAL_SCOPE_REVIEW.md']]
assert all(path.exists() for path in extra)
raw['evidence_paths'] = list(dict.fromkeys(raw['evidence_paths'] + [relative(path) for path in extra]))
assert all((ROOT / path).exists() for path in raw['evidence_paths'])

# Keep the original positive-local-theorem verdict: it is a necessary helper
# lower bound, never a graph/record PASS. Refresh only this node's duration.
helper = H['COMMON']['helper']
original_loader = helper._load_paper_frontmatter
nodepath = W / 'experiments' / (SLUG + '.md')
def target_meta(path):
    meta = original_loader(path)
    if Path(path).resolve() == nodepath.resolve():
        meta = dict(meta)
        meta['verdict'] = 'yes'
        meta['duration'] = 'k14followup0.880238423/10CPU; oldk13uniformdata inherited,notrerun'
    return meta
helper._load_paper_frontmatter = target_meta
try:
    row, rowfile = H['write_node'](raw, PREFIX)
finally:
    helper._load_paper_frontmatter = original_loader
ledger['rows'][pos] = row
H['persist'](ledger, rowfile, now)
node = 'experiments/' + SLUG + '.md'
summary = f'''\n\n{MARKER}
### {now} 原自然364 helper下界总节点升级：1..14关闭，至少15仍只是必要门

旧1..13严格NO/3276triples/81900(T,parent)完整继承，specific k13tree节点不改。14helper tree用旧good0纸面排，不重新枚树。剩单环必要域cycle3..7/depth3,2,2,1,1实际1930canonical；G1拒1910/G2再拒20，0survivor。G1为所有helper到owner，G2仅leaf parent度≥3，不能套degree2parent。原raw_ordered仅标签修为first_min_ordered_size14_decorations，数字/1930不变，0重跑。

严格范围固定自然364/714、保全部旧边、无新增oldold、max4/D5的1..14非空helper增广。不是任意finiteH或一般378图NO，不声称379存在；k15/order379仅最早未闭必要界，不安排k15梯，后续H19不混入。case.880238423/10，0sourceBFS/旧balls/masks/assignment/graph/Lean/solver/ARIS。

460→460/add0，0图/参数/Lean/方法增量，153/43/47与其它459rows/人工顶块保持。[原位helper总节点]({node})；[root终态](../{relative(D / 'ROOT_DISPOSITION.json')})；[scope review](../{relative(D / 'HELPER14_TERMINAL_SCOPE_REVIEW.md')})。

'''
H['update_pages'](old, human, summary, 0)
(W / 'DDP_METHOD_LEDGER.md').write_text(md_before + summary.replace('### ', '## ', 1))
after = load(ledger_path)
assert after['record_count'] == len(after['rows']) == 460
assert [r['id'] for r in after['rows']] == [r['id'] for r in before['rows']]
assert all(after['rows'][i] == before['rows'][i] for i in range(460) if i != pos)
assert next(r for r in after['rows'] if r['id'] == SPECIFIC13) == specific13_before
assert row['source_record']['other_metrics']['historical_1to13_source_record_before_helpers14_20261102'] == historical
H['unchanged_top'](before, after)
receipt = {
    'status': 'PASS_EXISTING_NATURAL364_HELPER_BOUND_NODE_COMPLETE_K14_UPSERT',
    'updated_UTC': now, 'records_before': 460, 'records_after': 460, 'records_added': 0,
    'updated_id': SLUG, 'canonical_node': relative(nodepath), 'row_path': relative(rowfile),
    'old1to13_source_record_preserved_exact': True,
    'old_specific_k13_node_preserved_exact': SPECIFIC13,
    'old3276_81900_rerun': False, 'k14_tree_paper_no_newenumeration': True,
    'unicyclic_canonical': 1930, 'G1_rejected': 1910, 'G2_rejected': 20, 'survivors': 0,
    'counter_label': 'first_min_ordered_size14_decorations', 'counter_correction_no_numeric_rerun': True,
    'fixed_architecture_closed_helpers': '1..14', 'first_unexcluded_helpers': 15,
    'first_unexcluded_order': 379, '379existence_or_general378NO_claimed': False,
    'local_theorem_verdict_not_graph_PASS': True, 'no_automatic_k15_or_H19_inclusion': True,
    'samecase_CPU_preserved': 0.880238423, 'case_cap': 10,
    'other459rows_preserved_exact': True, 'row_order_preserved': True,
    'human_top_blocks_preserved_exact': {name: True for name in H['FILES']},
    'index_experiments_before': index_before, 'index_experiments_after': index_before,
    'graph_parameter_Lean_method_increments': [0, 0, 0, 0],
    'graph_parameter_Lean_snapshot_preserved': [153, 43, 47],
    'full_rebuild_reimport': False, 'root_STATE_ROUND_HTML_recovery_modified': False,
    'new_math_solver_BFS_field_Lean_ARIS': 0,
    'modified_outputs': [relative(nodepath), 'research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md'] + ['research-wiki/' + name for name in H['FILES']] + [relative(rowfile)],
    'sync_process_CPU_seconds': time.process_time() - started, 'stop': True
}
receipt_path = S / (PREFIX + '_RECEIPT.json')
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'receipt': relative(receipt_path), 'before': 460, 'after': 460, 'add': 0, 'CPU': receipt['sync_process_CPU_seconds']}, ensure_ascii=False), flush=True)
