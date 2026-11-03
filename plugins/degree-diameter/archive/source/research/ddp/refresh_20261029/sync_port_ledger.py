"""Persist the already completed port-only diagnostic; do not run it again."""
from pathlib import Path
import contextlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "aris_repo/tools"))
import research_wiki as helper
import capture_filter

wiki = ROOT / "research-wiki"
ledger_before = (wiki / "DDP_METHOD_LEDGER.json").read_text()
result = json.loads((HERE / "PORT_LEDGER_RESULT.json").read_text())
assert result["status"] == "PORT_ACCOUNT_ONLY_COMPLETE"
assert not result["throughput_test_run"]
assert not result["latency_test_run"]
assert not result["routing_simulation_run"]
metrics = """Status: PORT_ACCOUNT_ONLY_COMPLETE; pending-performance.

This records the root's completed symbolic diagnostic on the accepted (13,5) family. No new graph or graph revalidation was performed. Under uniform router radix r>=13, one undirected network edge consumes one port at each endpoint, so the potential endpoint slot count is P=rn−2m.

|Saved graph|n|m|Added routers|Added network links|Change from original|
|---|---:|---:|---:|---:|---|
|Original|51417|324451|0|0|0|
|Intermediate|51437|324651|20|200|20r−400|
|Final|51457|324863|40|412|40r−824|

For integer radix13..20 the final potential slot count decreases; integer r>=21 is necessary for a positive change. At r=21 the formula gives16 potential additional slots. The illustrative r=16 case is173770→173690→173586, a final reduction184; it names no commercial device. CPU_seconds=0.002019220000000002, inherited from the actual result receipt.

throughput_test_run=false; latency_test_run=false; routing_simulation_run=false; graph_verification_repeated=false. No hardware/endpoints/capacities or performance baseline is bound. No new degree–diameter lower bound. This non-mathematical experiment is not a new method-ledger row.

Evidence: [script](../../research/ddp/refresh_20261029/port_ledger.py), [result](../../research/ddp/refresh_20261029/PORT_LEDGER_RESULT.json), [report](../../research/ddp/refresh_20261029/PORT_LEDGER_REPORT.md), [existing literal family](../../research/ddp/more_graphs_20261027/delivery/families.json).
"""
reasoning = """Partial progress on the network-value proposal: the port-accounting subtask is complete, while performance is pending. More graph vertices and retained network edges do not imply more endpoint slots. Even a positive symbolic slot balance would not prove throughput/latency gains or fair equipment cost. Conversely the negative balance for r<=20 is conditional on the declared router model and is not a general engineering impossibility.

No routing, load, hardware or endpoint-placement simulation was executed. The next performance step would require those explicit assumptions and its own bounded authorization; this record does not start that step. Original graph authorship and all103 accepted examples/3 cells/Lean0 remain inherited.
"""
assert not capture_filter.screen(metrics + reasoning)
slug = "ddp-network-d13-symbolic-port-ledger-20261029"
with (HERE / "port_ledger.wiki.log").open("w") as log, contextlib.redirect_stdout(log):
    helper.add_experiment(str(wiki), slug=slug,
        title="D13 accepted family: symbolic port account complete, performance pending",
        idea="idea:ddp-network-expansion-value-pilot",
        verdict="partial", confidence="high", date="2026-10-29",
        hardware="Existing family metadata only; no hardware measurements",
        duration="Actual recorded process CPU0.00201922s; not wall-clock reconstruction",
        metrics=metrics, reasoning=reasoning,
        provenance="research/ddp/refresh_20261029/PORT_LEDGER_RESULT.json; research/ddp/refresh_20261029/PORT_LEDGER_REPORT.md; research/ddp/refresh_20261029/port_ledger.py; research/ddp/more_graphs_20261027/delivery/families.json",
        tags=["ddp", "engineering-diagnostic", "port-only", "pending-performance"],
        update_on_exist=True)

idea_path = wiki / "ideas/ddp-network-expansion-value-pilot.md"
raw = idea_path.read_text()
old_added = helper._load_paper_frontmatter(idea_path)["added"]
thesis = raw.split("## Thesis\n",1)[1].split("\n## Key risks\n",1)[0]
thesis = thesis.replace("状态：未执行的有限工程提案；数学新下界仍是主目标。本提案不创建性能实验结果、不改数学完成标准、不成为第三条永久主线。",
    "状态：D13符号端口账本已完成，性能仍pending；数学新下界仍是主目标。本提案没有吞吐／延迟结果，不改数学完成标准、不成为第三条永久主线。")
marker = "## 已完成的端口子实验，性能仍待检验"
if marker not in thesis:
    thesis += "\n\n" + marker + "\n\n[exp:" + slug + "](../experiments/" + slug + ".md)复用原51417／中51437／终51457三张已验图的保存n,m。新增40台设备／412条网络边给ΔP=40r−824；整数r≤20槽位减少，r≥21才可能净增。CPU0.00201922。它只是端口记账，不是路由、吞吐、延迟或硬件性能模拟；性能和公平成本判断仍未执行。\n"
with (HERE / "port_ledger.wiki.log").open("a") as log, contextlib.redirect_stdout(log):
    helper.upsert_idea(str(wiki), "ddp-network-expansion-value-pilot",
        "保边扩张的网络价值：端口诊断与待检验性能",
        description="端口子任务已执行；未有吞吐／延迟证据，不计数学新下界。",
        stage="piloted", outcome="pending", thesis=thesis,
        risks="Symbolic spare-port balances are model dependent; performance, cost and endpoint placement remain pending. No industrial benefit is established.",
        tags=["ddp", "engineering-diagnostic", "pending-performance"],
        based_on=["paper:ddp-record-sources-20261026"], target_gaps=["DDP3"],
        update_on_exist=True)
    idea_path.write_text(re.sub(r"(?m)^added: .*", f"added: {old_added}", idea_path.read_text(), count=1))
    gap = wiki / "gap_map.md"
    gap.write_text(gap.read_text().replace(
        "**DDP3**：保边扩张是否产生端口及性能价值，尚无本项目测量。仅[有界未执行提案]",
        "**DDP3**：保边扩张的D13符号端口账已完成，尚无本项目性能测量。仅[有界端口诊断／待性能提案]",1))
    helper.append_log(str(wiki), "2026-10-29 D13 port-only diagnostic persisted as non-mathematical experiment; idea piloted/pending-performance, no positive industrial claim. Method ledger365/graph103/cells3/Lean0 unchanged.")
    helper.rebuild_index(str(wiki))
    helper.rebuild_query_pack(str(wiki))

assert (wiki / "DDP_METHOD_LEDGER.json").read_text() == ledger_before
assert len((wiki / "query_pack.md").read_text()) <= 8000
meta = helper._load_paper_frontmatter(idea_path)
assert meta["stage"] == "piloted" and meta["outcome"] == "pending"
assert not capture_filter.screen((wiki / "experiments" / f"{slug}.md").read_text())
assert not capture_filter.screen(idea_path.read_text())
receipt = dict(status="PASS_PORT_ONLY_SYNC", experiment_id="exp:"+slug,
    idea_id="idea:ddp-network-expansion-value-pilot", performance="pending",
    method_ledger_rows=365, new_method_ledger_rows=0,
    valid_graph_examples=103, improved_cells=3, complete_Lean_graph_instances=0,
    computations_rerun=0, query_pack_chars=len((wiki / "query_pack.md").read_text()),
    project_direction_from_current_brief=True,
    command="python research/ddp/refresh_20261029/sync_port_ledger.py")
(HERE / "PORT_WIKI_RECEIPT.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(receipt,ensure_ascii=False))
