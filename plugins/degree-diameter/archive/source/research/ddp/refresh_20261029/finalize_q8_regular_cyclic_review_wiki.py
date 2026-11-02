"""Record actual external review and independent new finite-certificate check."""
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


review_prefix = ROOT / 'reviews/ddp/q8_degree_quotient_lift_20261029'
response = json.loads(review_prefix.with_suffix('.response.json').read_text())
review = response['structuredContent']
assert review['status'] == 'SUCCESS' and review['model'] == 'gemini-3.8-flash-high'
assert review['effort'] == 'high' and review['threadId'] == '1b9fe949-16c0-42c6-9d3d-5f2d22501a07'
assert 'SUPPORT' in review['content']
independent_dir = HERE / 'q8_cyclic_quotient_route_capacity/independent_mod4_check'
independent = json.loads((independent_dir / 'RESULT.json').read_text())
comparison = json.loads((independent_dir / 'PER_CASE_COMPARISON.json').read_text())
terminal = json.loads((independent_dir / 'TERMINAL.json').read_text())
assert independent['status'] == 'COMPLETE_COUNTS_MATCH' and independent['completed_quotients'] == 110
assert comparison['status'] == 'ALL110_PER_CASE_COUNTS_MATCH' and comparison['differences'] == []
assert independent['counts'] == independent['expected_counts']
assert independent['counts']['mod4_pass'] == 0
assert terminal['aggregate_CPU_seconds'] < 1

before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
q8_id = 'ddp-q8-k64-cube-external2factor-13d3-20261029'
current = next(row for row in before['rows'] if row['id'] == q8_id)
row = copy.deepcopy(current['source_record'])
row['other_metrics'].update(independent_mod4_verification_status='PASS_COMPLETE_COUNTS_MATCH',
    independent_mod4_verified_quotients=110, independent_mod4_per_case_differences=0,
    independent_mod4_CPU_seconds=independent['CPU_seconds'],
    independent_mod4_receipt_comparison_CPU_seconds=comparison['comparison_CPU_seconds'],
    new_cross_model_review_status='SUCCESS_SUPPORT', new_cross_model_review_receipt_recorded=True,
    new_cross_model_reviewer_model=review['model'], new_cross_model_reviewer_effort=review['effort'],
    new_cross_model_review_threadId=review['threadId'])
row['lesson_and_restart_condition'] = row['lesson_and_restart_condition'].replace(
    '跨模审阅与独立mod4小核对待真实结果，不预记通过。',
    '后续实际Gemini静态审阅SUCCESS/SUPPORT；独立Python元组实现110商逐case计数全部吻合。模2/模4始终仅为必要门，模8全余类才是实际相位覆盖。')
row['failure_or_result'] += '；后续独立Python元组实现110商逐case完全匹配20050/28/3104/0，0.40885343CPU；Gemini静态审阅实际SUCCESS/SUPPORT。只核新有限证书，未重验旧图或重新枚213798商。'
for variant in row['variants']:
    if variant['label'] == 'general8Q3_extra_degree_two_necessary_20261029':
        variant.update(cross_model_review_status='SUCCESS_SUPPORT',
                       actual_reviewer_model=review['model'], actual_reviewer_effort=review['effort'])
    if variant['label'] == 'entire_cyclic_deck_twofactor_quotient_and_joint_voltage_exclusion_20261029':
        variant.update(cross_model_review_status='SUCCESS_SUPPORT',
            actual_reviewer_model=review['model'], actual_reviewer_effort=review['effort'],
            review_threadId=review['threadId'],
            independent_mod4_verification_status='PASS_COMPLETE_COUNTS_MATCH',
            independent_quotients_checked=110, independent_per_case_differences=0,
            independent_check_CPU_seconds=independent['CPU_seconds'],
            comparison_CPU_seconds=comparison['comparison_CPU_seconds'],
            verification_scope='New finite110-case modulo4 certificate only; no old graph BFS or original213798 quotient reenumeration.',
            review_wording_disposition='Modulo2 and modulo4 are necessary gates only; modulo8 complete residues is actual phase coverage.')
paths = [str(review_prefix.with_suffix(s).relative_to(ROOT)) for s in ['.prompt.md', '.response.json', '.DISPOSITION.md']]
paths += [str(p.relative_to(ROOT)) for p in sorted(independent_dir.iterdir())
          if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py'}]
row['report_paths'] = list(dict.fromkeys(row['report_paths'] + paths))
assert all((ROOT / p).exists() for p in row['report_paths'])
screen(json.dumps(row, ensure_ascii=False))
pending = HERE / 'Q8_REGULAR_CYCLIC_FINAL_REVIEW_WIKI_ROWS.json'
pending.write_text(json.dumps([row], ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
old = '跨模审阅与独立mod4小核对均待真实结果，不提前登记通过。数学104/4、confirmed103/3、Lean1和371账本行保持，无新图/方法/claim。'
new = '后续真实回执：Gemini 3.8 Flash High/high静态审阅SUCCESS/SUPPORT；独立Python元组实现110商逐case完全吻合，20050/28/3104/0，合0.40885343CPU。审阅处置明确模2/模4仅为必要门，不采纳“充要必要链”措辞；本次只核新有限证书，未重验旧图或重枚213798商。数学104/4、confirmed103/3、Lean1和371账本行保持，无新图/方法/claim。'
text = comments.read_text()
assert old in text
comments.write_text(text.replace(old, screen(new), 1))
report_path = HERE / 'Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_REPORT.md'
with report_path.open('a') as output:
    output.write(screen('\n\n## 后续审阅与独立核对已完成\n\n' + NOW +
        '：实际Gemini回执SUCCESS/SUPPORT，模型gemini-3.8-flash-high、effort high，thread1b9fe949-16c0-42c6-9d3d-5f2d22501a07。'
        '独立Python元组实现110商全部逐case一致，20050/28/3104/0，0.40414894CPU；仅比较已有receipt另0.00470449CPU。'
        '模2/模4只为必要门，模8才是实际覆盖，已按处置收窄审阅措辞。此段取代本简报此前pending字段；不关闭一般非循环辅助图或整个13D3格。\n'))
with (HERE / 'Q8_REGULAR_CYCLIC_FINAL_REVIEW_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Final actual Gemini SUPPORT and independent110 per-case modulo4 PASS recorded on the existing q8 experiment; no new graph/claim; final query rebuild waits for root state update.')

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == after['record_count'] == 371
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_FINAL_EVIDENCE_QUERY_PENDING_ROOT_UPDATE', updated_UTC=NOW,
    updated_existing_experiment=q8_id, record_count=371,
    cross_model_review_status='SUCCESS_SUPPORT', actual_reviewer_model=review['model'],
    actual_reviewer_effort=review['effort'], review_threadId=review['threadId'],
    independent_check_status=independent['status'], independent_cases=110,
    independent_per_case_status=comparison['status'], independent_per_case_differences=[],
    independent_CPU_seconds=independent['CPU_seconds'], receipt_comparison_CPU_seconds=comparison['comparison_CPU_seconds'],
    independent_total_CPU_seconds=terminal['aggregate_CPU_seconds'],
    full_C8_family_excluded=True, whole_13D3_parameter_cell_closed=False,
    general_noncyclic_twofactor_open=True, target_graph_examples=104, target_parameter_pairs=4,
    confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    new_graphs=0, new_claims=0, new_methods=0, research_jobs_rerun=0,
    final_query_rebuild_after_root_update_pending=True,
    command=command, helper_stdout=result.stdout.strip(),
    source_review=str(review_prefix.with_suffix('.DISPOSITION.md').relative_to(ROOT)),
    independent_receipt=str((independent_dir / 'TERMINAL.json').relative_to(ROOT)))
receipt_path = HERE / 'Q8_REGULAR_CYCLIC_FINAL_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=371, final_query='WAITING_FOR_ROOT_UPDATED'), ensure_ascii=False))
