"""Record the requested expert handoff in existing entries only.

No experiment, graph, proof compilation, solver, review or hash is run.
"""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
sys.path.insert(0, str(ROOT / 'aris_repo/tools'))
import capture_filter
import research_wiki as helper

stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
quote = '现在先帮我写一个可以给专家看的交付文档看看，给专家看看要怎么分析'
marker = '<!-- EXPERT_HANDOFF_20261029_USER_REQUEST -->'
ledger_path = WIKI / 'DDP_METHOD_LEDGER.json'
ledger_before = ledger_path.read_text()
ledger = json.loads(ledger_before)
assert ledger['record_count'] == 368
assert ledger['complete_Lean_graph_instances'] == 1
claim_names_before = sorted(p.name for p in (WIKI/'claims').glob('*.md'))
exp_names_before = sorted(p.name for p in (WIKI/'experiments').glob('*.md'))
handoff_names = ['EXPERT_HANDOFF_20261029.md', 'EXPERT_HANDOFF_20261029.html',
                 'EXPERT_HANDOFF_20261029.html.txt', 'EXPERT_HANDOFF_20261029.zip']
for name in handoff_names:
    assert (ROOT / 'expert_review_current' / name).is_file(), name

comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
note = f'''{marker}
## {stamp} 用户要求最新专家交付文档

用户本次原话：

> {quote}

已整理最新[专家阅读HTML](../expert_review_current/EXPERT_HANDOFF_20261029.html)、[Markdown正文](../expert_review_current/EXPERT_HANDOFF_20261029.md)、[逐字HTML源码](../expert_review_current/EXPERT_HANDOFF_20261029.html.txt)与[可转发ZIP](../expert_review_current/EXPERT_HANDOFF_20261029.zip)。旧20261028稿保留为历史，不能继承其中暂停／Lean0状态。新稿的三个专家问题是F5六平面互补机制的迁移、受限噪声的共同覆盖障碍，以及关键端口释放时怎样保持完整短路。

这是交付整理与入口同步，没有运行新构图、BFS、求解器、Lean编译或外审。同一Goal仍ACTIVE；数学合法实例104例／4参数、原confirmed主表103例／3参数、完整具体公式图Lean1、新20D3最新全球纪录pending1保持。原103图Lean仍0，文本解析等同性和恰20正则未在Lean证明；不把材料整理计为新数学成果／方法或实验节点。

当前署名使用Ryosuke Mizuno，原审阅文本保持原样并补充说明。唯一有效计划和恢复入口仍在原路径；本次未创建第二计划或知识库。
'''
assert not capture_filter.screen(note)
text = comments.read_text()
if marker not in text:
    comments.write_text(text.rstrip() + '\n\n' + note)

brief_path = ROOT / 'RESEARCH_BRIEF.md'
brief = brief_path.read_text()
brief_marker = '<!-- EXPERT_HANDOFF_20261029_LINK -->'
brief_note = f'''{brief_marker}
专家交付入口（2026-10-29）：[阅读HTML](expert_review_current/EXPERT_HANDOFF_20261029.html)／[正文MD](expert_review_current/EXPERT_HANDOFF_20261029.md)／[转发ZIP](expert_review_current/EXPERT_HANDOFF_20261029.zip)。按用户“{quote}”整理；三个问题为F5六平面迁移、受限噪声共同障碍、关键端口释放与完整短路。本次只整理与链接，未运行新实验，不改变ACTIVE、104/4、confirmed103/3、Lean1及最新全球纪录pending口径。
'''
assert not capture_filter.screen(brief_note)
if brief_marker not in brief:
    boundary = '<!-- REFRESH_20261029_CURRENT_END -->'
    assert boundary in brief
    brief_path.write_text(brief.replace(boundary, brief_note+'\n'+boundary, 1))

with (HERE/'EXPERT_HANDOFF_WIKI.sync.log').open('a') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), '2026-10-29 expert handoff request recorded verbatim in existing comments; latest HTML/MD/ZIP linked in existing brief. Documentation only; ACTIVE, ledger368, validated104/4, confirmed103/3 and complete formula Lean1 unchanged; no experiment or claim nodes created.')
    helper.rebuild_query_pack(str(WIKI))

assert ledger_path.read_text() == ledger_before
assert sorted(p.name for p in (WIKI/'claims').glob('*.md')) == claim_names_before
assert sorted(p.name for p in (WIKI/'experiments').glob('*.md')) == exp_names_before
assert quote in comments.read_text() and quote in brief_path.read_text()
query_chars = len((WIKI/'query_pack.md').read_text())
assert query_chars <= 8000
receipt = dict(status='PASS_EXISTING_ENTRIES_HANDOFF_ONLY',
    applied_UTC=stamp, exact_user_quote=quote,
    documents_updated=['research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md','RESEARCH_BRIEF.md'],
    handoff_paths=['expert_review_current/'+n for n in handoff_names],
    helper='aris_repo/tools/research_wiki.py:append_log,rebuild_query_pack',
    record_count=368, new_records=0, new_experiment_nodes=0, new_claim_nodes=0,
    validated_graph_examples=104, validated_parameter_pairs=4,
    confirmed_publictable_examples=103, confirmed_publictable_cells=3,
    complete_deterministic_formula_Lean_graph_instances=1,
    latest_global_record_status='pending', goal_status='ACTIVE',
    new_experiments=0, new_BFS=0, new_compilations=0,
    new_solver_calls=0, new_external_reviews=0,
    ledger_unchanged=True, experiment_and_claim_node_sets_unchanged=True,
    query_pack_chars=query_chars,
    command='python research/ddp/refresh_20261029/record_expert_handoff_wiki.py')
(HERE/'EXPERT_HANDOFF_WIKI_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
