"""Record the requested updated expert delivery without changing research counts."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import importlib.util
import json

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
QUOTE='现在先帮我写一个可以给专家看的交付文档看看，给专家看看要怎么分析'


def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'aris_repo/tools'/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


helper,capture=module('research_wiki'),module('capture_filter')


def screen(text):
    assert not capture.screen(text),capture.screen(text)
    return text


ledger_path=WIKI/'DDP_METHOD_LEDGER.json'
ledger_before=ledger_path.read_bytes()
ledger=json.loads(ledger_before)
assert ledger['record_count']==374
assert ledger['validated_graph_examples_including_novelty_pending']==104
assert ledger['confirmed_publictable_graph_examples']==103
assert ledger['complete_Lean_graph_instances']==1
delivery=json.loads((HERE/'EXPERT_DELIVERY_2355_RESULT.json').read_text())
assert delivery['status']=='EXPERT_HANDOFF_UPDATED_AND_CHECKED'
assert delivery['package_files']==655 and delivery['package_bytes']==158537095
assert delivery['missing_checked_links']==[]
assert delivery['HTML_equals_source'] is delivery['archive_current_document_matches'] is delivery['download_mirrors_match'] is True
assert delivery['enhanced_16_model_status']=='PREPARED_NOT_SOLVED'
assert delivery['K2_14_status']=='UNKNOWN'
assert delivery['new_support_density_shared_lemmas_external_review']=='PENDING'
owned=[ROOT/'AGENTS.md',ROOT/'RESEARCH_BRIEF.md',
    ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',
    ROOT/'research/progress.html',
    ROOT/'expert_review_current/EXPERT_HANDOFF_20261029.md',
    ROOT/'expert_review_current/build_handoff_20261029.py']
owned_before={p:p.read_bytes() for p in owned}
brief=(ROOT/'RESEARCH_BRIEF.md').read_text()
assert '2026-10-30 00:02:14 UTC' in brief and '23:55' in brief
main=ROOT/'expert_review_current/EXPERT_HANDOFF_20261029.md'
assert '2026年10月29日23时55分 UTC' in main.read_text()[:300]
for suffix in ['.md','.html','.html.txt']:
    assert (ROOT/('expert_review_current/EXPERT_HANDOFF_20261029_2155'+suffix)).is_file()
comments=WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker='<!-- EXPERT_HANDOFF_2355_REQUEST_AND_CURRENT_ENTRY_20261029 -->'
note=f'''{marker}
## {NOW} 专家稿更新至23:55研究快照

用户明确要求：

> {QUOTE}

已按这项交付请求更新同一canonical主稿：[可编辑正文](../expert_review_current/EXPERT_HANDOFF_20261029.md)、[阅读HTML](../expert_review_current/EXPERT_HANDOFF_20261029.html)、[HTML源码](../expert_review_current/EXPERT_HANDOFF_20261029.html.txt)和[完整ZIP](../expert_review_current/EXPERT_HANDOFF_20261029.zip)。研究快照为2026-10-29 23:55 UTC，重点为16度诱导删点与14度K2合作覆盖。实际交付于2026-10-30 00:02:14 UTC完成；[原始交付回执](../research/ddp/refresh_20261029/EXPERT_DELIVERY_2355_RESULT.json)记录655文件、158537095字节、当前正文30/历史37/F5README10条本地链接通过，HTML源码相同、包内正文和下载镜像一致。没有在本次Wiki同步重做这些检查。

原21:55稿已独立保留为[历史正文](../expert_review_current/EXPERT_HANDOFF_20261029_2155.md)、[历史HTML](../expert_review_current/EXPERT_HANDOFF_20261029_2155.html)和[历史源码](../expert_review_current/EXPERT_HANDOFF_20261029_2155.html.txt)；原comments不删。

文稿汇总已有结果，不是数学研究产出，不新增图、方法或ledger记录。ledger374、数学合法104例/4参数、confirmed主表改善103例/3参数、具体公式图Lean1均保持。3750最新全球纪录仍待确认；增强16模型仅准备、主solver未启动，14K2仍UNKNOWN，最新support/density/shared-middle引理尚未外审，不能由早先PASS外推。

本次只同步唯一Wiki人工记录与当前交付入口。旧“专家包仍21:55”不再作为现行断言；root状态已于2026-10-30 00:02:14 UTC更新，本次随后最后重建canonical index/query。未改root文件/专家文件，未启动研究计算。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:out.write('\n\n'+screen(note))
gap_path=WIKI/'gap_map.md'
gap=gap_path.read_text()
assert '账本现374条实验／来源记录' in gap[:1800]
delivery_marker='<!-- EXPERT_HANDOFF_2355_CURRENT_DELIVERY_20261029 -->'
delivery_note=f'''{delivery_marker}
当前专家交付已完成，研究快照23:55 UTC：[正文](../expert_review_current/EXPERT_HANDOFF_20261029.md)／[HTML](../expert_review_current/EXPERT_HANDOFF_20261029.html)／[源码](../expert_review_current/EXPERT_HANDOFF_20261029.html.txt)／[完整ZIP](../expert_review_current/EXPERT_HANDOFF_20261029.zip)。用户要求“{QUOTE}”。[交付回执](../research/ddp/refresh_20261029/EXPERT_DELIVERY_2355_RESULT.json)为2026-10-30 00:02:14终态：655文件、158537095字节、30+37+10条链接通过。旧21:55稿已另存档，不再作为当前专家稿。交付不是新研究成果；增强16主solver未启动，14K2仍UNKNOWN，新引理未外审。计数374／104合法例／103confirmed／Lean1保持。
'''
if delivery_marker not in gap:
    anchor='<!-- INDUCED_K2_CURRENT_BATCH_20261029 -->'
    assert anchor in gap
    gap=gap.replace(anchor,screen(delivery_note)+'\n\n'+anchor,1)
gap=gap.replace('专家包仍21:55快照，恢复以本批、当前brief/progress及Wiki为准。',
    '专家主稿现已更新为23:55研究快照；21:55稿另行存档，研究实际状态仍读当前brief/progress及Wiki。',1)
gap=gap.replace('21:55专家包只是早先快照；恢复以本批与当前brief/progress为准。',
    '该段为22:34历史研究快照；当前专家稿已更新至23:55，恢复读当前brief/progress与Wiki。',1)
old='最新专家交付已完成（21:55 UTC研究快照）：[HTML](../expert_review_current/EXPERT_HANDOFF_20261029.html)／[可编辑正文](../expert_review_current/EXPERT_HANDOFF_20261029.md)／[HTML源码](../expert_review_current/EXPERT_HANDOFF_20261029.html.txt)／[完整ZIP](../expert_review_current/EXPERT_HANDOFF_20261029.zip)。'
new='早先21:55 UTC专家稿现已存档：[历史HTML](../expert_review_current/EXPERT_HANDOFF_20261029_2155.html)／[历史正文](../expert_review_current/EXPERT_HANDOFF_20261029_2155.md)／[历史源码](../expert_review_current/EXPERT_HANDOFF_20261029_2155.html.txt)。当前交付入口见上方23:55快照，不把同名当前ZIP当历史ZIP。'
gap=gap.replace(old,new,1)
gap_path.write_text(screen(gap))
with (HERE/'EXPERT_HANDOFF_2355_WIKI_HELPER.log').open('w') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Recorded exact user request and completedcanonical23:55 expertMD/HTML/source/ZIP delivery afterroot2026-10-30_00:02:14. Actualrootreceipt655files/158537095bytes/30+37+10links inheritedwithoutrechecking.21:55filesarchived. Documentationonly:ledger374,104/4,confirmed103/3,Lean1 unchanged; enhanced16solvernotstarted/14K2UNKNOWN/latestlemmasnotexternallyreviewed. Finalcanonicalindex/queryrebuilt.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))
assert ledger_path.read_bytes()==ledger_before
assert all(p.read_bytes()==data for p,data in owned_before.items())
query=(WIKI/'query_pack.md').read_text()
assert len(query)<=8000 and '23:55' in query and 'EXPERT_DELIVERY_2355_RESULT.json' in query
assert '专家包仍21:55' not in query
receipt=dict(status='PASS_EXPERT_HANDOFF_2355_DELIVERY_COMPLETE_FINAL_QUERY_REBUILT',
    updated_UTC=NOW,user_quote=QUOTE,research_snapshot_UTC='2026-10-29 23:55 UTC',
    canonical_main='expert_review_current/EXPERT_HANDOFF_20261029.md',
    historical_main='expert_review_current/EXPERT_HANDOFF_20261029_2155.md',
    final_ZIP_status='COMPLETE_ROOT_RECEIPT',package_files=655,package_bytes=158537095,
    checked_local_links=delivery['checked_local_links'],missing_checked_links=[],
    root_state_update_UTC='2026-10-30 00:02:14 UTC',
    canonical_helper='aris_repo/tools/research_wiki.py',
    final_query_rebuilt_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    query_chars=len(query),
    ledger_unchanged=True,record_count=374,new_experiments=0,new_methods=0,new_graphs=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    enhanced16_solver_started=False,D14_K2_status='UNKNOWN',
    latest_lemmas_external_review='NOT_COMPLETED',
    documentation_is_research_output=False,root_and_expert_files_modified=False,
    final_query_rebuild_after_root_update_pending=False)
out=HERE/'EXPERT_HANDOFF_2355_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),
    record_count=374,query_chars=len(query),final_query='COMPLETE_AFTER_ROOT_STATE'),ensure_ascii=False))
