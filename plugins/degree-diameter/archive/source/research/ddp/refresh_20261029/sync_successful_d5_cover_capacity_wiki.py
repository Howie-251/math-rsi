"""Record one aggregate experiment in the existing ordinary graph-cover family."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'aris_repo/tools' / (name + '.py'))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


helper = module('research_wiki')
capture = module('capture_filter')


def screen(text):
    assert not capture.screen(text), capture.screen(text)
    return text


directory = HERE / 'successful_d5_cover_d6_capacity'
result = json.loads((directory / 'RESULT.json').read_text())
assert len(result['sources']) == 3 and result['source_reads'] == 3
assert sum(len(s['roots']) for s in result['sources']) == 5
assert result['graph_bfs_runs'] == result['cover_graphs'] == 0
specs = [
    dict(n=37631, Delta=11, L6=186033, kmin=5, R6root=0, R6target=13489, R6count=4, R5target=102,
         public_base_n=37628, successful_prefixes=3),
    dict(n=42402, Delta=12, L6=364032, kmin=9, R6root=42324, R6target=796, R6count=8, R5target=53,
         public_base_n=42342, successful_prefixes=60),
    dict(n=51457, Delta=13, L6=538740, kmin=11, R6root=49949, R6target=1574, R6count=2, R5target=191,
         public_base_n=51417, successful_prefixes=40)
]
variants = []
for spec, source in zip(specs, result['sources']):
    assert source['n'] == spec['n'] and source['kmin'] == spec['kmin']
    witness = next(r for r in source['roots'] if r['root'] == spec['R6root'])
    assert witness['minimum_through_6'] == spec['R6count']
    assert witness['witness_through_6'] == spec['R6target']
    root0 = next(r for r in source['roots'] if r['root'] == 0)
    assert root0['minimum_through_5'] == 1 and root0['witness_through_5'] == spec['R5target']
    assert max(spec['R6root'], spec['R6target'], spec['R5target']) < spec['public_base_n']
    variants.append(dict(label=f"accepted_d5_source_{spec['Delta']}_n{spec['n']}_ordinary_cover_capacity",
        target=[spec['Delta'], 6], target_Delta=spec['Delta'], target_D=6, savedL=spec['L6'],
        baseline_scope='Saved D6 comparison value frozen inPREDICTION, not a fresh global-record survey.',
        source_n=spec['n'], source_m=source['m'], source_degree_min=source['degree_min'],
        source_degree_max=spec['Delta'], source_literal=source['source'],
        required_sheets_to_exceed_saved_D6_bound=spec['kmin'],
        R6_witness=dict(root=spec['R6root'], target=spec['R6target'],
                        NB_walks_through6=spec['R6count'],
                        exact_length_counts=witness['witness_6_by_exact_length']),
        D6_excluded_sheets_from_witness_at_least=spec['R6count'] + 1,
        all_D6_improving_ordinary_covers_excluded=True,
        R5_witness=dict(root=0, target=spec['R5target'], NB_walks_through5=1,
                       exact_length_counts_through5=root0['witness_5_by_exact_length'][:6]),
        D5_all_nontrivial_ordinary_covers_excluded=True,
        actual_DP_roots=[r['root'] for r in source['roots']],
        source_literal_reads=1, source_D5_BFS_repeated=0,
        count_units='Nonbacktracking base walks, not graph bad pairs or distinct lifted endpoints.',
        logical_prefix_extension=dict(successful_prefixes=spec['successful_prefixes'],
            public_base_order=spec['public_base_n'], public_bases=1,
            all_witness_labels_present_in_public_base=True,
            extension_basis='Retained-edge prefix walk-set inclusion into final graph; no additional root or count.',
            D6_improving_covers_excluded=True, D5_nontrivial_covers_excluded=True),
        cover_graphs_generated=0, solver_calls=0))

proof = ('For an ordinary k-sheet graph cover, shortest lifted paths project to NB base walks, and each base walk has a unique lift from a fixed lifted root. '
         'Thus a target with c NB walks throughD admits at mostc reachable points in its k-pointfiber, so c<k excludes diameter<=D. '
         'No regular/deck-Galois cover or regular source assumption is used.')
prefix = ('All six witness pairs are already labeled inside their respective originalpublic bases. '
          'For every retained-edge successful prefixGi, every NB walk between those fixed labels inGi remains the same NB walk inGfinal; hence the earlier count is atmost the saved final count. '
          'Nprefix<=Nfinal means floor(L6/Nprefix)+1>=floor(L6/Nfinal)+1=5,9,11. '
          'Therefore the final-source witnesses exclude every ordinary cover of all103 accepted prefixes and3 public bases that exceeds the respective savedD6bound. '
          'The R5 counts atmost1 likewise exclude k>=2 throughout these106 logical base graphs. No106-source computation is claimed.')
ident = 'ddp-successful-d5-sources-ordinary-cover-route-capacity-20261029'
row = dict(id=ident,
    title='三张成功D5源的NB容量：普通cover越D6界及非平凡D5整域排除，单调扩至全部prefix',
    family='ordinary graph-cover transfer',
    idea_family='idea:ddp-open-parameter-construction-20261026',
    record_type='fixed-source-exact-route-capacity-obstruction',
    target_Delta=None, target_D=6, savedL=None, target_is_multivalued=True,
    n=dict(actual=None, hypothetical=None), actual_D=None, actual_graph_Delta=None,
    actual_D_scope='No cover graph generated or graph diameter measured; inherited literal sources retain their acceptedD5 status.',
    ordinary_bad_unordered_pairs=None, ordinary_bad_target_D=6,
    scope='Computed only three finalaccepted literals37631/42402/51457 at the five prescribed DP roots. '
          'Unique-lifting NB bounds close ordinary covers atD6 sheet thresholds5/9/3 respectively and all nontrivial k>=2 covers atD5. '
          'Static retained-edge monotonicity extends this to103 successful prefixes plus3public bases without new counting.',
    failure_or_result='Actual NB<=6 witnesses0->13489:4<5,42324->796:8<9,49949->1574:2<11 (indeed excludesk>=3). '
        'Root0 NB<=5 witnesses102/53/191 eachhave count1. Three reads/five exactarc-DP roots, worker.123602CPU, compile+run.838358CPU. '
        'No sourceBFS, cover, solver, random choice or extra root. Logical106-graph scope is inherited, not recomputed.',
    positive_guarantees=[proof, prefix],
    lesson_and_restart_condition='Stop ordinary covers of these sources/prefixes at the statedD5/D6 thresholds; changing sheet count, voltage group or regularity cannot evade unique path lifting. '
        'Reopening requires changing base adjacency or projection rule, e.g. a genuine non-cover construction, with its own concrete coverage question. '
        'Do not mistake these NB-walk counts for ordinary bad pairs, sampled voltage failures or all-source BFS.',
    unclosed_gap='Changed adjacency, branched/non-cover maps, other bases and generalD6 parameter cells remain open. '
        'A new independent six-pair meet-in-the-middle witness check is pending; no Lean theorem or new graph is claimed.',
    other_metrics=dict(computed_final_sources=3, source_literal_reads=3, actual_NB_DP_roots=5,
        graph_BFS_runs=0, cover_graphs_generated=0, solver_calls=0,
        worker_CPU_seconds=result['worker_cpu_seconds'], aggregate_compile_run_CPU_seconds=result['aggregate_cpu_seconds'],
        count_units='Exact NB walks of lengths0..D from a fixed base root to a fixed target.',
        logical_successful_prefixes=103, logical_original_public_bases=3,
        logical_applicable_base_graphs=106, prefix_extension_static_confirmed=True,
        prefix_extension_new_computation=False, independent_MITM_status='PENDING',
        new_lower_bound_mathematically_verified=False, complete_Lean_graph_instance=False,
        new_graphs=0, independent_method_count_increment=0),
    variants=variants, outcome_class='complete-declared-source-ordinary-cover-route-obstruction',
    wiki_verdict='yes',
    report_paths=[str(p.relative_to(ROOT)) for p in sorted(directory.iterdir())
        if p.is_file() and p.suffix in {'.md', '.json', '.py', '.cpp'}])

report = '''# 成功D5源的ordinary-cover容量与保边prefix扩展

这是同一ordinary graph-cover transfer家族的一条新聚合实验，含三个source变体，不是新独立方法。实际只读三张final图、做5个规定根的NB弧消息DP；0BFS/cover图/solver，总编译+运行0.838358CPU。

D6：37631源0→13489的NB≤6为4，排k≥5；42402源42324→796为8，排k≥9；51457源49949→1574为2，排k≥3，因此排所有可越保存D6比较值所需的k≥11。保存比较值为186033/364032/538740，所需最小层数为5/9/11，非本次查新。

D5：root0到102/53/191各只有一条NB≤5，故三final源任何非平凡普通cover均不能D5。计数单位是NB走步，不是普通坏点对，也不声称所有target仅一条路或源只有空闭路。

普通覆盖的短路径投影必NB，每条基图走步从固定liftroot唯一提升，故c条走步至多命中targetfiber的c个点。小于k便严格阻断D≤D；适用于不正则source及非Galois普通cover。

prefix扩展已由静态单调性确认：全部见证标签在原publicbase内，103逐步保旧边，因此任意早期base/prefix的NB走步集合包含于final的相应集合。较小阶数要越同一保存D6界所需k不会小于final所需5/9/11。故相同界逻辑覆盖103成功prefix+3public bases；R5任意非平凡cover也全排。这不是106张图的新读数或重验。

独立6具体pair的MITM证据核对仍pending，结果后续另同步。数学构造104/4、confirmed103/3、Lean1不变。此实验使账本由371增372条记录，不增加独立方法数；普通cover之外的改边/分支映射与一般D6格未排。root负责最终状态后最后query。
'''
report_path = HERE / 'SUCCESSFUL_D5_COVER_WIKI_REPORT.md'
report_path.write_text(screen(report))
row['report_paths'].append(str(report_path.relative_to(ROOT)))
assert all((ROOT / p).exists() for p in row['report_paths'])
screen(json.dumps(row, ensure_ascii=False))
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 371
assert ident not in {r['id'] for r in before['rows']}
pending = HERE / 'SUCCESSFUL_D5_COVER_WIKI_ROWS.json'
pending.write_text(json.dumps([row], ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

gap_map = WIKI / 'gap_map.md'
gap_text = gap_map.read_text()
assert '账本现371条实验／来源记录' in gap_text[:1800]
gap_map.write_text(gap_text.replace('账本现371条实验／来源记录', '账本现372条实验／来源记录', 1))
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
s = comments.read_text()
old = '另一个D5-cover/D6-capacity问题处检查准备，未登记数值启动。'
new = '后续D5-cover/D6-capacity已实际完成三final源/5规定DP根检验，NB容量排除和静态prefix扩展见下节，不再记准备。'
if old in s:
    s = s.replace(old, new, 1)
marker = '<!-- SUCCESSFUL_D5_ORDINARY_COVER_CAPACITY_COMPLETE_20261029 -->'
if marker not in s:
    s += '\n\n' + marker + '''
## 成功D5源的普通cover容量实际完成

三final图只读各1次、5个规定根NB弧DP，总compile+run0.838358CPU，0BFS/cover/solver。D6见证为37631源0→13489的4条、42402源42324→796的8条、51457源49949→1574的2条，分别排k≥5/9/3，因而排越保存D6界所需5/9/11层。R5 root0到102/53/191各1条，排任意非平凡普通cover。走步计数不是普通坏点对。

全部见证已在publicbase内，保边prefix的NB集合包含于final；较小N要越同一界所需k不会下降。静态推导遂扩至103成功prefix+3publicbase，无新增算。只关闭这些base/prefix的普通cover指定D5/D6域，不排一般格或非cover改造。独立6pair MITM仍待实际回执。

同一ordinary graph-cover transfer家族新增1条聚合experiment、3source variants，账本372记录不是372种方法；构造104/4、confirmed103/3、Lean1保持。[本轮证据](../research/ddp/refresh_20261029/SUCCESSFUL_D5_COVER_WIKI_REPORT.md)。root最终更新后再重建query。
'''
comments.write_text(screen(s))
with (HERE / 'SUCCESSFUL_D5_COVER_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Added one aggregate experiment in existing ordinary graph-cover transfer family: three actual final-source NB gates, static106-base/prefix scope; independent six-pair MITM pending. Ledger372, independent methods and graph counters unchanged; final query waits for root.')

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 372
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_NEW_AGGREGATE_EXISTING_FAMILY_MITM_PENDING_QUERY_PENDING_ROOT',
    updated_UTC=NOW, experiment_id=ident, method_family='ordinary graph-cover transfer',
    record_count_before=371, record_count_after=372, new_experiments=1, independent_new_methods=0,
    actual_sources_read=3, actual_NB_DP_roots=5, NB_count_units='Nonbacktracking walks',
    graph_BFS_runs=0, cover_graphs_generated=0, solver_calls=0,
    compile_run_CPU_seconds=result['aggregate_cpu_seconds'],
    logical_successful_prefixes=103, logical_public_bases=3, logical_scope_graphs=106,
    prefix_extension_static_confirmed=True, prefix_extension_extra_computation=False,
    independent_MITM_status='PENDING', new_graphs=0, new_claims=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True, command=command, helper_stdout=run.stdout.strip())
receipt_path = HERE / 'SUCCESSFUL_D5_COVER_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=372, independent_methods_added=0, MITM='PENDING'), ensure_ascii=False))
