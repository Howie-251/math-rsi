"""Complete the one current Wiki batch after root's actual terminal update."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
ROOT_UPDATED = '2026-10-30 03:01:31 UTC'
IDENTIFIER = 'ddp-k5-q16-f3four-actual-r4-voltage-route-gates-12d4-20261030'


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'aris_repo/tools' / (name + '.py'))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


helper, capture = module('research_wiki'), module('capture_filter')


def screen(text):
    assert not capture.screen(text), capture.screen(text)
    return text


turn = json.loads((HERE / 'SYMMETRY_AND_REAL_ROUTE_TURN_RESULT.json').read_text())
assert turn['status'] == 'SYMMETRY_AND_ACTUAL_ROUTE_BATCH_COMPLETE_NO_NEW_GRAPH'
assert turn['all_started_numeric_batches_terminal'] is True
assert turn['Goal_status'] == 'ACTIVE' and turn['old_D2'] == 'PAUSED'
for p in [ROOT / 'AGENTS.md', ROOT / 'RESEARCH_BRIEF.md',
          ROOT / 'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md']:
    text = p.read_text()[:10000]
    assert ROOT_UPDATED in text and 'SYMMETRY_AND_REAL_ROUTE_TURN_RESULT.json' in text
prefix = ROOT / 'reviews/ddp/k5_q16_actual_route_20261030'
review = json.loads(prefix.with_suffix('.response.json').read_text())['structuredContent']
assert (review['status'], review['model'], review['effort']) == ('SUCCESS', 'gemini-3.8-flash-high', 'high')
collision_path = HERE / 'k5_q16_actual_R4/COLLISION_WITNESS.json'
collision = json.loads(collision_path.read_text())
assert collision['provider_keys'] == 9 and collision['actual_value_histogram'] == {'0': 5, '4': 4}
assert collision['target'] == 162 and collision['missing_deck'] == 2
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 378
row = copy.deepcopy(next(r for r in before['rows'] if r['id'] == IDENTIFIER)['source_record'])
review_meta = dict(status='SUCCESS_SOUND_AS_STATED', actual_model=review['model'],
    effort=review['effort'], thread_id=review['threadId'],
    scope='Static support for tree gauge, all341 raw route images including backtracking, provider necessity, exact field/deck cache implementation and complete30x4096 assignment scope. Fixed K5/these F3^4 charts/ordinary Q16 only.',
    reviewer_reran_code_or_enumeration=False, calibration_BFS_roots=1,
    calibration_root_to_all6480_targets_compared=True, main_search_BFS_roots=0,
    all6480_source_BFS_claimed=False, negative_Lean_formalization=False,
    response=str(prefix.with_suffix('.response.json').relative_to(ROOT)),
    disposition=str(prefix.with_suffix('.DISPOSITION.md').relative_to(ROOT)))
variant = dict(label='saved_calibration_provider_collision_explanation_actual_static_review_20261030',
    status='EXACT_SAVED_WITNESS_STATIC_REVIEW_SUPPORTED_NO_NEW_ENUMERATION',
    scope=collision['scope'], voltages=collision['voltages'], source=0,
    target=162, target_base=0, missing_deck=2, missing_deck_name='r^2',
    field_coordinate=0, V4_coset=0, projected_provider_keys=9,
    actual_Q16_value_histogram={'identity': 5, 'r^4': 4},
    actual_distinct_deck_values=2, required_deck_values_in_coset=4,
    interpretation='Passing a projected provider count does not allow each target to choose independent voltages: these nine keys collide into only two values under the one common assignment.',
    graph_generation_or_BFS_or_search_repeated=False, actual_external_review=review_meta)
row['variants'] = [v for v in row['variants'] if v.get('label') != variant['label']] + [variant]
row['other_metrics'].update(actual_route_static_review=review_meta,
    saved_calibration_collision_provider_keys=9,
    saved_calibration_collision_distinct_deck_values=2)
suffix = '；保存校准目标162=(base0,r²,field0)虽有9个V4 provider，完整共同电压仅给e五次/r⁴四次，缺r²，解释路线重复而非缺少形式提供者。真实静态外审SUCCESS/SOUND AS STATED；外审未重跑枚举，校准只1根对6480目标比较，主枚举0候选BFS。'
if suffix not in row['failure_or_result']:
    row['failure_or_result'] += suffix
row['report_paths'] = list(dict.fromkeys(row['report_paths'] + [str(collision_path.relative_to(ROOT))] +
    [str(prefix.with_suffix(s).relative_to(ROOT)) for s in ['.prompt.md', '.response.json', '.DISPOSITION.md']] +
    ['research/ddp/refresh_20261029/SYMMETRY_AND_REAL_ROUTE_TURN_RESULT.json',
     'research/ddp/refresh_20261029/SYMMETRY_AND_REAL_ROUTE_TURN.md']))
assert all((ROOT / p).exists() for p in row['report_paths'])
screen(json.dumps(row, ensure_ascii=False))
raw_path = HERE / 'SYMMETRY_REAL_ROUTE_FINAL_WIKI_ROWS.json'
raw_path.write_text(json.dumps([row], ensure_ascii=False, indent=2) + '\n')
run = subprocess.run([sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'),
                      str(raw_path)], cwd=ROOT, capture_output=True, text=True, check=True)
after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 378
for key in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[key] == after[key]

comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = '<!-- SYMMETRY_REAL_ROUTE_FINAL_WIKI_20261030 -->'
note = f'''
## {NOW} 同步平移、C33与真实K5/Q16路线本轮收束

root03:01:31最终[总索引](../research/ddp/refresh_20261029/SYMMETRY_AND_REAL_ROUTE_TURN_RESULT.json)／[推导与选择](../research/ddp/refresh_20261029/SYMMETRY_AND_REAL_ROUTE_TURN.md)已成为恢复入口。15度同步fiber平移2880×768满秩、核0，不能据此把648端口压成一轨道或固定anchor；不排全部Aut，原整数K2仍UNKNOWN。C33指定11K3+跨块F2factor若普通D3，则F无三角分量；12个外部块需求超过实际8个，真实Gemini静态SOUND。旧无三角best仍缺28有序NB3，不续solver。

新12D4 K5/Q16/F3四维chart规则中，NB4充分证书0/4096和实际provider必要门30/4096严格分开。全部122880完整群赋值随后均在root0自身目标层失败，结合4066被必要门排除的投影，严格停止该固定实际D4族；不外推一般12D4或其他群/chart/base。一次失败6480/38880、12regular校准图只做1根BFS到全部6480目标，与缓存逐位一致、R4=4563；主搜索0候选、0图生成/0BFS。目标162的9个provider只占e与r⁴两个值，显出共同电压碰撞。实际路线外审SUCCESS/SOUND，但未重跑枚举；处置已纠正原回复“6480点全BFS”的歧义。

全部已启动数值和外审均终态。ledger378为实验／来源记录，新增K5聚合记录沿已有route-chart家族，不是独立方法数。合法104/4、confirmed103/3、具体公式Lean1、3750最新全球纪录pending均不变；同一Goal ACTIVE、旧D2暂停。专家02:02快照冻结，本轮不重包；无新构造或Goal完成声明。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:
        out.write('\n\n' + marker + '\n' + screen(note))
gap_path = WIKI / 'gap_map.md'
gap = gap_path.read_text()
assert '账本现378条实验／来源记录' in gap[:1800]
latest_marker = '<!-- SYMMETRY_REAL_ROUTE_CURRENT_20261030 -->'
latest = '''<!-- SYMMETRY_REAL_ROUTE_CURRENT_20261030 -->
当前研究批次已终态（root03:01:31 UTC）：[权威总索引](../research/ddp/refresh_20261029/SYMMETRY_AND_REAL_ROUTE_TURN_RESULT.json)／[推导与判断](../research/ddp/refresh_20261029/SYMMETRY_AND_REAL_ROUTE_TURN.md)。D15同步fiber平移核0，仅排该归约入口，全部Aut未排、原K2仍UNKNOWN。C33普通D3迫跨块F无三角分量，纸面证明获真实GeminiSOUND，一般无三角F仍开放，旧best缺28未修复。K5/Q16×该F3^4chart的NB4证书0/4096不足以排实际图；真实0..4路线provider门保留30/4096，再完整122880共同群赋值全失败于root0自身目标层，严格停止该固定实际D4族，不外推一般12D4。单失败校准图6480/38880、12regular，仅1根BFS与全部6480目标位比较R4=4563；主搜索0图/BFS。9个形式provider同电压仅落e/r⁴两值，外审实际SUCCESS/SOUND且处置明确证据层次。全部已启数值/外审终态，不接群/seed/旧timer梯子。378记录、104/4、confirmed103/3、Lean1；Goal ACTIVE/D2暂停，专家02:02稿冻结。

'''
if latest_marker not in gap:
    anchor = '<!-- CHART_ROUTE_K2_TRANSFER_CURRENT_20261030 -->'
    assert anchor in gap
    gap = gap.replace(anchor, screen(latest) + anchor, 1)
    gap = gap.replace('当前研究批次已终态（root01:52:40 UTC）',
        '历史研究批次已终态（root01:52:40 UTC；当前读上方03:01总索引）', 1)
gap_path.write_text(screen(gap))
with (HERE / 'SYMMETRY_REAL_ROUTE_FINAL_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Completed root03:01:31 final recovery/query sync. D15 synchronous translation kernel0 not allAut; C33 F triangle-free paper lemma actualreviewSOUND; K5/Q16 exactNB4 gate0 versus actualprovider30, then all122880 actual lifts fail. One calibration BFS root to6480 targets only, main search0BFS. Saved9provider collision and actualreview disposition attached to same row. Ledger378,1044,confirmed1033,Lean1;GoalACTIVE,D2paused,expert02:02snapshotfrozen;no new research or root/expert edits.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))
query = (WIKI / 'query_pack.md').read_text()
assert len(query) <= 8000
assert 'SYMMETRY_AND_REAL_ROUTE_TURN_RESULT.json' in query and '账本现378' in query
receipt = dict(status='PASS_SYMMETRY_REAL_ROUTE_FINAL_INDEX_QUERY_REBUILT',
    updated_UTC=NOW, root_state_update_UTC=ROOT_UPDATED,
    latest_batch='research/ddp/refresh_20261029/SYMMETRY_AND_REAL_ROUTE_TURN_RESULT.json',
    record_count=378, new_experiment_records_this_final_sync=0,
    new_independent_methods_claimed=0, all_started_numeric_batches_terminal=True,
    all_started_external_reviews_terminal=True, K5_actual_route_review=review_meta,
    saved_collision_provider_keys=9, saved_collision_actual_deck_values=2,
    new_accepted_graphs=0, valid_examples=104, valid_pairs=4,
    confirmed_examples=103, confirmed_pairs=3, Lean_instances=1,
    latest_20D3_global_novelty='PENDING', Goal_status='ACTIVE', old_D2='PAUSED',
    root_or_expert_files_modified=False, expert_snapshot_UTC='2026-10-30 02:02 UTC',
    canonical_helper='aris_repo/tools/research_wiki.py', query_chars=len(query),
    final_query_rebuilt_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    final_query_after_root_update_pending=False, helper_stdout=run.stdout.strip())
out = HERE / 'SYMMETRY_REAL_ROUTE_FINAL_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
earlier_path = HERE / 'SYMMETRY_REAL_ROUTE_WIKI_RECEIPT.json'
earlier = json.loads(earlier_path.read_text())
earlier.update(final_query_after_root_update_pending=False,
    final_receipt=str(out.relative_to(ROOT)), final_query_rebuilt_UTC=receipt['final_query_rebuilt_UTC'])
earlier_path.write_text(json.dumps(earlier, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(out.relative_to(ROOT)),
    record_count=378, query_chars=len(query)), ensure_ascii=False))
