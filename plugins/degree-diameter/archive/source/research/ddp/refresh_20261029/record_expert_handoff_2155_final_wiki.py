"""Finalize the requested expert-delivery index in existing Wiki entries only."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
QUOTE = '现在先帮我写一个可以给专家看的交付文档看看，给专家看看要怎么分析'


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


ledger_path = WIKI / 'DDP_METHOD_LEDGER.json'
ledger_before = ledger_path.read_text()
ledger = json.loads(ledger_before)
assert ledger['record_count'] == 372 and ledger['complete_Lean_graph_instances'] == 1
assert ledger['validated_graph_examples_including_novelty_pending'] == 104
root_paths = [ROOT / 'AGENTS.md', ROOT / 'RESEARCH_BRIEF.md',
    ROOT / 'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',
    ROOT / 'research/progress.html']
root_before = {p: p.read_bytes() for p in root_paths}
brief = (ROOT / 'RESEARCH_BRIEF.md').read_text()
assert '21:59:17' in brief and '21:55' in brief and '专家交付已完成' in brief
main = ROOT / 'expert_review_current/EXPERT_HANDOFF_20261029.md'
assert '21时55分' in main.read_text()[:300]
for suffix in ['.md', '.html', '.html.txt', '.zip']:
    assert (ROOT / ('expert_review_current/EXPERT_HANDOFF_20261029' + suffix)).is_file()
    assert (Path('/mnt/data') / ('AR4MATH_EXPERT_HANDOFF_20261029' + suffix)).is_file()
observed_zip_bytes = (ROOT / 'expert_review_current/EXPERT_HANDOFF_20261029.zip').stat().st_size
experiment_names = sorted(p.name for p in (WIKI / 'experiments').glob('*.md'))
claim_names = sorted(p.name for p in (WIKI / 'claims').glob('*.md'))

comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = '<!-- EXPERT_HANDOFF_2155_FINAL_COMPLETED_20261029 -->'
note = f'''{marker}
## {NOW} 专家交付已完成并同步实际入口

用户本次原话：

> {QUOTE}

已完成21:55 UTC研究快照的[专家阅读HTML](../expert_review_current/EXPERT_HANDOFF_20261029.html)、[可编辑正文](../expert_review_current/EXPERT_HANDOFF_20261029.md)、[逐字HTML源码](../expert_review_current/EXPERT_HANDOFF_20261029.html.txt)和[完整可转交ZIP](../expert_review_current/EXPERT_HANDOFF_20261029.zip)。原件继续保存在global_user项目的expert_review_current，/mnt/data为聊天下载镜像。

主稿已纳入C33原/规范模型真实UNKNOWN、保全标号与静态审阅，ordinarycover六pair MITM和106个base/prefix继承，D13静态40/780/max40、P40两轮provider空定点，以及dominance只删96的终态；移除了“原B0覆盖尚未认证”的旧句。当前专家分析重点是C33共同路线和新的D13邻域/补路，小q8非循环对象作为储备。所有已述数值任务均终态，不由交付自动续旧timer。

现有打包检查报告472个文件、37条正文相对链接，HTML与源码逐字一致；源代码、字面数据和必要证据已随包提供。root将在本次Wiki入口同步后只刷新包内Wiki快照并重打包，不重复数学计算。

这是文档交付和入口同步，不是新数学成果；ledger372为来源/实验/变体记录，104例/4参数、confirmed103例/3参数、具体公式图Lean1及3750最新全球纪录待定均保持。原Goal仍ACTIVE，旧D2继续暂停。root状态已于21:59:17 UTC更新，本次未改AGENTS/NEXT/RESEARCH_BRIEF/progress或专家主稿/builder。
'''
s = comments.read_text()
if marker not in s:
    s += '\n\n' + screen(note)
old = '当前专家快照第五节末关于“未保证40组在原B0独立覆盖”的信息已由新静态40/40、780pair、容量证书补足，需由root在交付修订时更新；本writer只做Wiki与只读附件建议，不改主稿/专家包或root入口。'
new = '后续21:55专家快照已由root更新：静态40/40、780pair、容量证书及合作池provider全排均已写入，旧B0未认证句已删除；本writer只同步Wiki入口，不改专家包或root入口。'
if old in s:
    s = s.replace(old, new, 1)
comments.write_text(screen(s))

gap_path = WIKI / 'gap_map.md'
gap_marker = '<!-- EXPERT_HANDOFF_2155_DELIVERY_INDEX_20261029 -->'
gap = gap_path.read_text()
assert '账本现372条实验／来源记录' in gap[:1800]
gap_note = f'''{gap_marker}
最新专家交付已完成（21:55 UTC研究快照）：[HTML](../expert_review_current/EXPERT_HANDOFF_20261029.html)／[可编辑正文](../expert_review_current/EXPERT_HANDOFF_20261029.md)／[HTML源码](../expert_review_current/EXPERT_HANDOFF_20261029.html.txt)／[完整ZIP](../expert_review_current/EXPERT_HANDOFF_20261029.zip)。用户要求“{QUOTE}”。此索引只同步交付，不增加372记录或构造成果；root最新brief已确认交付完成，研究与停止范围沿用实际终态。
'''
if gap_marker not in gap:
    anchor = '- **DDP1**'
    assert anchor in gap
    gap = gap.replace(anchor, screen(gap_note) + '\n' + anchor, 1)
    gap_path.write_text(gap)

with (HERE / 'EXPERT_HANDOFF_2155_FINAL_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'User expert-delivery request quoted exactly; completed21:55 HTML/MD/source/ZIP linked in existing comments and gap index; root21:59:17 brief read back unchanged; documentation only, ledger372 and graph/formal counts unchanged.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))

assert ledger_path.read_text() == ledger_before
assert all(p.read_bytes() == before for p, before in root_before.items())
assert sorted(p.name for p in (WIKI / 'experiments').glob('*.md')) == experiment_names
assert sorted(p.name for p in (WIKI / 'claims').glob('*.md')) == claim_names
query_chars = len((WIKI / 'query_pack.md').read_text())
assert query_chars <= 8000
receipt = dict(status='PASS_EXPERT_HANDOFF_2155_DELIVERY_COMPLETE_FINAL_QUERY_REBUILT',
    applied_UTC=NOW, exact_user_quote=QUOTE, snapshot_UTC='2026-10-29 21:55 UTC',
    root_state_update_UTC='2026-10-29 21:59:17 UTC',
    delivery_status='COMPLETE', all_described_numerical_jobs_terminal=True,
    handoff_html='expert_review_current/EXPERT_HANDOFF_20261029.html',
    handoff_editable_text='expert_review_current/EXPERT_HANDOFF_20261029.md',
    handoff_html_source='expert_review_current/EXPERT_HANDOFF_20261029.html.txt',
    handoff_zip='expert_review_current/EXPERT_HANDOFF_20261029.zip',
    chat_download_mirror_prefix='/mnt/data/AR4MATH_EXPERT_HANDOFF_20261029',
    root_reported_packaged_files=472, root_reported_body_relative_links_checked=37,
    observed_pre_Wiki_snapshot_refresh_zip_bytes=observed_zip_bytes,
    brief_status='Existing root21:59:17 brief read back current; not modified.',
    documents_updated=['research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md',
        'research-wiki/gap_map.md', 'research-wiki/index.md',
        'research-wiki/query_pack.md', 'research-wiki/log.md'],
    helper='aris_repo/tools/research_wiki.py:append_log,rebuild_index,rebuild_query_pack',
    final_query_pack_characters=query_chars, final_query_rebuild_after_root_update=True,
    record_count=372, ledger_unchanged=True, new_records=0,
    new_experiments=0, new_methods=0, new_claims=0, new_graphs=0,
    mathematical_graph_examples=104, mathematical_parameter_pairs=4,
    confirmed_examples=103, confirmed_parameter_pairs=3, complete_formula_Lean_instances=1,
    latest3750_global_novelty='PENDING', goal_status='ACTIVE', old_D2='PAUSED',
    new_BFS=0, new_compilations=0, new_solver_calls=0, new_reviews=0,
    expert_main_builder_and_root_files_unchanged=True)
receipt_path = HERE / 'EXPERT_HANDOFF_2155_FINAL_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
for name in ['COOPERATIVE_CLIQUE40_WIKI_RECEIPT.json', 'COVER_MITM_D13_CALIBRATION_WIKI_RECEIPT.json',
             'SUCCESSFUL_D5_COVER_WIKI_RECEIPT.json', 'CONTROLLER33_CANONICAL_WIKI_RECEIPT.json']:
    p = HERE / name
    if p.exists():
        prior = json.loads(p.read_text())
        prior.update(final_query_rebuild_after_root_update_pending=False,
            root_state_update_UTC='2026-10-29 21:59:17 UTC', final_query_rebuilt_UTC=NOW,
            final_query_pack_characters=query_chars,
            final_delivery_sync_receipt=str(receipt_path.relative_to(ROOT)))
        p.write_text(json.dumps(prior, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    ledger_records=372, query_characters=query_chars, root_files_modified=False), ensure_ascii=False))
