"""Merge the supplied strategy drafts through the existing ARIS Wiki helper.

This is documentation persistence only: no graph, solver, source audit or registry
mutation. The experiment ledger is deliberately read-only.
"""
from pathlib import Path
import contextlib
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
WIKI = ROOT / "research-wiki"
OUT = Path(__file__).resolve().parent
if (OUT / "WIKI_IMPORT_RECEIPT.json").exists():
    print(json.dumps({"status": "ALREADY_APPLIED_NO_WRITES",
                      "receipt": str(OUT / "WIKI_IMPORT_RECEIPT.json"),
                      "note": "Resume the same Goal from the effective plan; do not reimport enriched Wiki nodes."}))
    raise SystemExit(0)
sys.path.insert(0, str(ROOT / "aris_repo/tools"))
import research_wiki as helper
import capture_filter

STAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REF = "../../context/DD_PORTFOLIO_REFRESH_20261029"
PLAN = "../../context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md"
REG = "../../context/DD_PORTFOLIO_START_20261026/registry/cases.json"
ledger_text = (WIKI / "DDP_METHOD_LEDGER.json").read_text()
ledger_md = (WIKI / "DDP_METHOD_LEDGER.md").read_text()
ledger = json.loads(ledger_text)
claims_before = sorted(p.name for p in (WIKI / "claims").glob("*.md"))
assert len(ledger["rows"]) == 365
assert ledger["valid_new_graph_examples"] == 103
assert ledger["mathematically_improved_parameter_pairs"] == 3

def screened(text):
    findings = capture_filter.screen(text)
    assert not findings, findings
    return text

def add_section(path, marker, text, before_connections=False):
    raw = path.read_text()
    if marker in raw:
        return
    extra = screened(f"\n\n<!-- {marker} -->\n{text.strip()}\n")
    if before_connections and "\n## Connections\n" in raw:
        raw = raw.replace("\n## Connections\n", extra + "\n## Connections\n", 1)
    else:
        raw = raw.rstrip() + extra
    path.write_text(raw)

strategy = """本节点于2026-10-29定向合并新版机会选择草稿；这是同一个已明确恢复的 Goal 的策略，不是新数学结论。唯一有效计划仍是[原路径 RESEARCH_GOAL](%s)，新包是版本来源；候选只使用[原 registry](%s)的33项中12项本次角色，不建立第二候选库。

主目标是已授权开放参数中的完整合法新下界。旧27格是起始历史，不再是硬边界；D2、n61谱与旧队列继续暂停。默认最多两条主要数学机制，可只集中一条；经典挑战占其中一槽，有限工程诊断不成为第三条长期线。选题比较已有覆盖保证、真实自由选择、旧失败范围和可辨别下一问，不按点数、名气或纪录年龄推定容易。不锁定十五度，也不逐格轮流短搜。

继承103个不同阶数完整图、3参数，最好37631/42402/51457，具体图Lean实例0；这些不是本轮新成功，更不是103种独立方法。署名、首图独立核验和后续完整current-R4归纳分别按原证据保留。

有具体问题和有效反馈可深入同一机制，不要求每次发明新定理；局部坏对下降不自动触发追加seed。UNKNOWN保持开放，充分证书失败不冒全族排除。已核源与未变证据复用。研究动作按实际CPU quota/内存与单worker安排，不把55-CPU聚合配额当永久独占；[本机资源快照](../../research/ddp/refresh_20261029/RESOURCE_AND_EXISTING_DATA.md)只是读取时状态。

机会和旧边界见[数学机会节点](ddp-math-challenges-and-records.md)，有限工程提案见[网络价值节点](ddp-network-expansion-value-pilot.md)。反例方法继续复用[承重保证节点](ddp-counterexample-gates-20261026.md)；不重开旧n61研究。

## 本次导入来源与历史范围

[IMPORT_AND_APPLY](%s/IMPORT_AND_APPLY.md)、[策略草稿](%s/wiki_import/ddp-opportunity-selection-refresh.md)、[PRIOR_WORK_AND_DELTA](%s/PRIOR_WORK_AND_DELTA.md)。旧2026-10-26正文中的“27格／当前无新图”是启动时事实，已由本节开放表范围与103例继承状态替代；旧实验和反例不删除。本次只合并资料，不产生数学结果、不重新验证历史图。""" % (PLAN, REG, REF, REF, REF)

cases = [
    ((15,4), "现成未决", "ddp-d15-d4-current15552-source-gap-20261027", "648 free；一般非对称≤15点仍UNKNOWN。反演/≤5仿射线rawUNSAT及内禀36点、二择反射门的失败不排一般扩张。"),
    ((15,5), "现成未决", "ddp-d15-d5-current102060-source-slack-profile-20261027", "810 free；当前源是102060。一般覆盖UNKNOWN，旧LP/MIP与成线子域分账，不自动续时。"),
    ((12,3), "不同机制候选", "ddp-wave5-hs850-branch-lift", "固定HS850六参数已闭；十轨道放松只是有限失败。需要真实路径互补变化。"),
    ((16,3), "不同机制候选", "ddp-wave4-mizuno-d3-source", "1920来源已借用分析，全16正则；无保边增点空位，不重做首次恢复。"),
    ((12,4), "不同机制候选", "ddp-d12-d4-current6156-source-20261027", "6156/36936全12正则，free0。8000项只未过特定充分证书，不是8000图D4反例。"),
    ((11,6), "需新规则的迁移储备", "ddp-d11-d6-unique-onefault-star-exact2-20261027", "186033的固定mandatory9+至多2guards已完整排除；不排任意11邻域，不续该proxy。"),
    ((3,5), "经典挑战储备", "ddp-afy70-2fold-d6-capacity-20261027", "AFY70指定普通2重D6/3重D7 cover已排；不能外推整个(3,5)。"),
    ((4,3), "经典挑战储备", "ddp-published-quartic-cayley-census69orders-4d3-d4-20261028", "已发表完整Cayley目录相应范围已过滤无改进；非Cayley仍开放，旧42子族不重跑。"),
    ((8,3), "经典挑战储备", "ddp-wave10-gq312-internal-cycles", "312两侧2-factor仅有限失败；4090普通坏对属于保存图，不是全族界。"),
    ((11,5), "继承成功", "ddp-h9-qline-d11-family-37631", "37629..37631三例；后续同格须超过项目最好，署名与Lean状态保留。"),
    ((12,5), "继承成功", "ddp-h9-qline-d12-family-42377", "42343..42402六十例；30个新形态失败同时漏原外围和新增点，不能归因仅新增60点。"),
    ((13,5), "继承成功", "ddp-d13-singlefault-star-family-51457-20261027", "51418..51457四十例；成功代理不是完整孪生，完整覆盖才是充分性。"),
]
case_lines = []
for (d,D), lane, exp, boundary in cases:
    assert (WIKI / "experiments" / f"{exp}.md").exists(), exp
    case_lines.append(f"|({d},{D})|{lane}|[{exp}](../experiments/{exp}.md)|{boundary}|")
opportunity = """这是候选地图和进入条件，不是已证claim、难度排名或自动任务队列。原[registry](%s)是唯一候选数据源；本页只建立证据导航，不另抄一套可能分叉的实时基线。12项是9项候选／挑战加3项继承成果，激活前按原registry与具体公开来源核对最优标记和门槛。

|参数|本次角色|已有实际证据|进入前必须继承的边界|
|---|---|---|---|
%s

补充证据：[12D3十轨道放松](../experiments/ddp-wave5-hs850-orbit10-relaxation.md)、[6156固定C20切片](../experiments/ddp-d12-d4-wide-filter-c20-slice8000-20261027.md)、[AFY70三重cover](../experiments/ddp-afy70-3fold-d7-capacity-20261027.md)、[42点保旧边三助手](../experiments/ddp-polarity13-c3-freeports-threehelpers42-4d3-20261028.md)。目录过滤依赖已发表完整性，不是本项目新分类或一般图排除。

经典低度问题的历史与易陈述性只提供定性学术辨识度；没有知名度量表或成功概率。工业价值独立且尚未测。其它已授权参数仍可因真正新覆盖规则替换候选，不能因这12项形成永久队列。

## 来源与当前增量

[CASEBOOK](%s/CASEBOOK.md)、[PRIOR_WORK_AND_DELTA](%s/PRIOR_WORK_AND_DELTA.md)、[原机会草稿](%s/wiki_import/ddp-math-challenges-and-records.md)。本次只定向检索相关旧节点，没有重导365条账本或重新判定原图。H9当前30项缺项分类来自保存missing列表的只读提取：1358原外围与110新增是跨case出现次数， distinct并集581/46；不是事前注册的预测或新覆盖实验。后续投影检验须另按真实PRED/RESULT记录。""" % (REG, "\n".join(case_lines), REF, REF, REF)

network = """状态：未执行的有限工程提案；数学新下界仍是主目标。本提案不创建性能实验结果、不改数学完成标准、不成为第三条永久主线。

先选既有三族之一，复用原公开完整源、中间图、项目最终图，明确把点作为何种设备、每点总端口r以及端点／网络链路占用。端口账P=rn−2m、变化ΔP=ar−2b只是假设下的潜在端点槽位，不等于服务器容量、吞吐或时延收益。原空余端口若已接业务，新增网络边也可能挤占业务端口；新增设备与链路成本必须计入。

只有先定路由、需求、链路容量与公平预算，才作一次有界诊断。旧业务保持与新增容量分开；固定最短路、逐跳ECMP和所有最短路径均匀分流不能混用名称。样本负载可以作诊断，不能代替严格图直径；没有排队／硬件模型不称实测延迟，没有布局不称线长或能耗收益。

可复用的数学对象为[11D5](../experiments/ddp-h9-qline-d11-family-37631.md)、[12D5](../experiments/ddp-h9-qline-d12-family-42377.md)、[13D5](../experiments/ddp-d13-singlefault-star-family-51457-20261027.md)和[字面生成器／families](../../research/ddp/more_graphs_20261027/delivery/families.json)。这些旧实验验证图构造，不验证本提案的网络性能。

## 背景来源与未执行边界

以新包[SOURCES W6–W8](%s/SOURCES.md)为继承阅读范围：[Slim Fly研究组页](https://spcl.inf.ethz.ch/Research/Scalable_Networking/SlimFly/)、[Jellyfish NSDI官方摘要](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/singla)、[PolarFly作者摘要](https://arxiv.org/abs/2208.01695)。本次Wiki合并未重新访问这些页面、未声称全文复算，不将文献性能比例移植到本项目，也不因D2网络背景重开D2求解。

完整待执行定义见[ENGINEERING_PILOT](%s/ENGINEERING_PILOT.md)、[原提案草稿](%s/wiki_import/ddp-network-expansion-value-pilot.md)。首次诊断可支持、反驳或保持未决，结果都只属于声明规模／路由／负载；进一步工程投入取决于实际问题与人工意见。尚未创建任何性能experiment或claim。""" % (REF, REF, REF)

gap_intro = """<!-- REFRESH_20261029_GAPS -->
# 当前机会与未决义务 — 2026-10-29策略应用

同一Goal已按用户明确授权恢复ACTIVE；唯一计划为[原路径](../context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md)。365条实验／来源记录、103个阶数图、3参数、完整具体Lean实例0均继承，不是本轮新增。旧D2暂停；以下旧“当前”段仅作历史。

- **DDP1**：开放参数完整新构造。12项角色只是导航，见[机会地图](ideas/ddp-math-challenges-and-records.md)与[原registry](../context/DD_PORTFOLIO_START_20261026/registry/cases.json)。主攻最多两条机制，不逐格轮流短搜。
- **DDP2**：已有覆盖保证如何共同实现。6156源全正则、186033固定one-fault已排；15度一般非对称单点覆盖仍UNKNOWN，rawUNSAT的对称／成线子域不可外推。H9缺项须分原外围／项目新增与端口占用，不能假定仅新增60点致败。相关[策略](ideas/ddp-open-parameter-construction-20261026.md)／[承重反例](ideas/ddp-counterexample-gates-20261026.md)链接旧实验，不恢复已闭批次。
- **DDP3**：保边扩张是否产生端口及性能价值，尚无本项目测量。仅[有界未执行提案](ideas/ddp-network-expansion-value-pilot.md)，不占第三条永久线，不计数学新下界。

最新人工原话见[comments](DD82_PROGRESS_AND_COMMENTS_20261018.md)；数学、审阅、公开采用、Lean与工程分账。实际资源读原计划链接快照，约每小时反馈不强制换题。新材料是计划来源，不是第二Goal／Wiki。此段是策略同步，未运行求解／BFS／构图。

---

"""
screened(gap_intro)
gap_path = WIKI / "gap_map.md"
if "REFRESH_20261029_GAPS" not in gap_path.read_text():
    gap_path.write_text(gap_intro + gap_path.read_text())

specs = [
    ("ddp-open-parameter-construction-20261026", "多参数度数—直径构造：按机制与研究价值选择机会", "active", strategy, ["DDP1", "DDP2"]),
    ("ddp-math-challenges-and-records", "数学候选、经典挑战与已有严格范围", "proposed", opportunity, ["DDP1", "DDP2"]),
    ("ddp-network-expansion-value-pilot", "保边扩张的网络价值：有限且未执行的诊断提案", "proposed", network, ["DDP3"]),
]
with (OUT / "wiki_refresh.sync.log").open("a") as log, contextlib.redirect_stdout(log):
    for slug, title, stage, thesis, gaps in specs:
        screened(thesis)
        path = WIKI / "ideas" / f"{slug}.md"
        old_added = helper._load_paper_frontmatter(path).get("added") if path.exists() else None
        helper.upsert_idea(str(WIKI), slug, title,
            description="2026-10-29同Goal策略资料合并；不产生新数学／工程结果。",
            stage=stage, outcome="pending", thesis=thesis,
            risks="候选不是成功承诺；UNKNOWN不排除，子域失败不外推，旧成果不重复计数。工程收益未经本项目试验。",
            tags=["ddp", "strategy-refresh", "proposal"],
            based_on=(["paper:ddp-record-sources-20261026",
                       "paper:mizuno2026_new_lower_bounds",
                       "paper:przybocki2026_doubly_saturated_ramsey"]
                      if slug == "ddp-open-parameter-construction-20261026"
                      else ["paper:ddp-record-sources-20261026"]),
            target_gaps=gaps, update_on_exist=True)
        if old_added:
            path.write_text(re.sub(r"(?m)^added: .*", f"added: {old_added}", path.read_text(), count=1))
    for _, _, exp, _ in cases:
        helper.add_edge(str(WIKI), "idea:ddp-math-challenges-and-records", f"exp:{exp}", "tested_by",
            "继承的该候选来源／旧构造试验，仅标原实验实际范围；不是2026-10-29新候选策略的成功验证。")
    for exp in ["ddp-d12-d4-wide-filter-c20-slice8000-20261027", "ddp-wave5-hs850-orbit10-relaxation", "ddp-afy70-3fold-d7-capacity-20261027", "ddp-polarity13-c3-freeports-threehelpers42-4d3-20261028"]:
        helper.add_edge(str(WIKI), "idea:ddp-math-challenges-and-records", f"exp:{exp}", "tested_by",
            "继承对应固定域旧证据；充分筛、有限失败、完整排除与原参数未决分列。")

add_section(WIKI / "papers/ddp-record-sources-20261026.md", "REFRESH_20261029_SOURCE_SCOPE", """## 2026-10-29材料的来源读取范围

本次复用[更新包SOURCES](../../context/DD_PORTFOLIO_REFRESH_20261029/SOURCES.md)中主表选定条目／相关说明的读取快照（包记查阅日2026-10-29、页面最后变更2026-10-28）；这是继承材料的来源说明，本次Wiki合并未重新上网或核验整个公开表。动态基线只在[原registry](../../context/DD_PORTFOLIO_START_20261026/registry/cases.json)维护，12项角色不是完整分类或必做清单。后续激活与新纪录声明仍需核当时来源。既有103例／3格及Lean0不因此改变。""", True)

for slug in ["ddp-counterexample-gates-20261026", "ddp-breadth-20261027"]:
    add_section(WIKI / "ideas" / f"{slug}.md", "REFRESH_20261029_PRECEDENCE", """## 2026-10-29策略适用说明

以下2026-10-26/27“当前0新图／27格／快速比较”是历史阶段记录，不是现在的结果或自动派发队列。当前继承103例／3参数、Lean0，开放表范围与[新版策略](ddp-open-parameter-construction-20261026.md)适用。反例只攻击具体承重保证；有实际问题可深入，不强迫机械短试／快速换题。旧实验和暂停D2边界保留，不重跑历史。""", True)

launcher = (ROOT / "context/DD_PORTFOLIO_REFRESH_20261029/GOAL_LAUNCHER.txt").read_text().strip()
comment = f"""## {STAMP} 用户明确恢复同一Goal，并应用新版策略

以下为用户本次采用的恢复入口原话，来源：[GOAL_LAUNCHER](../context/DD_PORTFOLIO_REFRESH_20261029/GOAL_LAUNCHER.txt)。新包原GOAL_UPDATE_MESSAGE的“仅应用后保持暂停”是先前步骤，本次明确恢复覆盖该等待状态；不改写旧暂停记录。

{chr(10).join('> ' + line for line in launcher.splitlines())}

执行记录：唯一有效计划仍[原RESEARCH_GOAL](../context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md)，原稿由root按日期归档，新包不成为第二计划。原registry保留27项历史并合为33项，12项有本次角色，不自动派发。Wiki复用旧多参数策略及反例节点，新增机会地图和未执行工程提案各一，不创建claim／实验账本行。数学继承103例／3参数（37631/42402/51457），完整具体图Lean0；公开采用和审阅范围按原记录。6156已恢复且全正则、186033固定one-fault排除、十五度一般非对称UNKNOWN及全部旧有限域边界继续继承。

本次Wiki资料应用本身没有数学计算、BFS、求解、构图、工程仿真或付费调用。资源仍引用[本机快照](../research/ddp/refresh_20261029/RESOURCE_AND_EXISTING_DATA.md)：128逻辑CPU affinity不等于55-CPU cgroup聚合quota的永久独占，内存按实际300GiB上限和当前用量，研究先单worker。root后续真实实验另以其PRED/RESULT记账；不把读取旧missing列表的分类当成新预注册预测。"""
comments = WIKI / "DD82_PROGRESS_AND_COMMENTS_20261018.md"
comments_text = comments.read_text()
old_intro = "最新状态见文末按时间追加的记录，以及 [research/progress.html](../research/progress.html)。Goal **ACTIVE**，当前任务为Degree/Diameter Portfolio（4≤Δ≤12，D=3/4/5）；旧n61与D2任务已暂停。"
new_intro = "最新状态见文末按时间追加的人工记录，以及 [research/progress.html](../research/progress.html)。Goal **ACTIVE**，2026-10-29已明确按新版恢复同一Degree/Diameter Portfolio；开放参数范围以[唯一有效计划](../context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md)为准，最初27格仅作历史，旧n61与D2继续暂停。"
if old_intro in comments_text:
    comments.write_text(comments_text.replace(old_intro, new_intro, 1))
add_section(comments, "REFRESH_20261029_HUMAN_RESUMPTION", comment)

plan_path = ROOT / "context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md"
add_section(plan_path, "REFRESH_20261029_WIKI_APPLIED", """## 本次唯一Wiki应用定位

新版三份idea／策略草稿已最少合并：更新`idea:ddp-open-parameter-construction-20261026`，新增`idea:ddp-math-challenges-and-records`与未执行`idea:ddp-network-expansion-value-pilot`，复用`idea:ddp-counterexample-gates-20261026`及原paper/experiment节点。12项候选只链接本计划同目录`registry/cases.json`；新包不另成数据库或第二计划。人工明确恢复原话保存在`research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md`的2026-10-29条目。原365条账本、103例／3参数、具体图Lean0及真实资源约束不变；本次资料同步不是新研究成果。""")

with (OUT / "wiki_refresh.sync.log").open("a") as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), "2026-10-29 refresh: merge 3 strategy drafts into 1 existing + 2 proposed idea nodes; 12 case evidence links; human resumption recorded; no claims, experiments or ledger rows added; 365/103/3/Lean0 retained.")
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))

# A small delta lint: the installed CLI has no lint subcommand. Do not claim a
# fresh all-history proof/schema audit or fix unrelated historical warnings.
errors = []
nodes = {}
for directory in ["papers", "ideas", "experiments", "claims"]:
    for p in (WIKI / directory).glob("*.md"):
        m = re.search(r"(?m)^node_id:\s*(.+)$", p.read_text())
        if m:
            node_id = m.group(1).strip().strip('"')
            if node_id in nodes:
                errors.append(f"duplicate node_id {node_id}")
            nodes[node_id] = p
new_ids = [f"idea:{x[0]}" for x in specs]
for node_id in new_ids:
    p = nodes[node_id]
    text = p.read_text()
    meta = helper._load_paper_frontmatter(p)
    for field in ["type", "node_id", "title", "stage", "outcome", "added", "based_on", "target_gaps", "tags"]:
        if not re.search(rf"(?m)^{field}:", text):
            errors.append(f"missing {field}: {node_id}")
    if meta.get("type") != "idea" or meta.get("outcome") != "pending":
        errors.append(f"wrong idea status {node_id}")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if "://" not in target and not target.startswith("#"):
            if not (p.parent / target.split("#")[0]).exists():
                errors.append(f"missing local link {node_id}: {target}")
edges = [json.loads(line) for line in (WIKI / "graph/edges.jsonl").read_text().splitlines() if line.strip()]
edge_keys = []
for e in edges:
    if e["from"] in new_ids:
        edge_keys.append((e["from"], e["type"], e["to"]))
        if not e["to"].startswith("gap:") and e["to"] not in nodes:
            errors.append(f"dangling edge {e['to']}")
        if e["to"].startswith("gap:") and e["to"][4:] not in gap_path.read_text():
            errors.append(f"dangling gap {e['to']}")
for node_id in new_ids:
    if not any(x[0] == node_id for x in edge_keys):
        errors.append(f"orphan touched idea {node_id}")
if len(edge_keys) != len(set(edge_keys)):
    errors.append("duplicate touched edges")
assert (WIKI / "DDP_METHOD_LEDGER.json").read_text() == ledger_text
assert (WIKI / "DDP_METHOD_LEDGER.md").read_text() == ledger_md
assert sorted(p.name for p in (WIKI / "claims").glob("*.md")) == claims_before
assert len((WIKI / "query_pack.md").read_text()) <= 8000
assert not errors, errors
receipt = dict(status="PASS_INCREMENTAL_LINT", applied_UTC=STAMP,
    updated_idea_ids=[new_ids[0]], new_proposed_idea_ids=new_ids[1:],
    reused_counterexample_id="idea:ddp-counterexample-gates-20261026",
    inherited_case_rows=12, linked_existing_experiments=16,
    ledger_records=365, new_ledger_rows=0, valid_graph_examples=103,
    mathematically_improved_parameter_pairs=3, complete_Lean_graph_instances=0,
    new_claims=0, new_mathematical_or_engineering_computations=0,
    query_pack_chars=len((WIKI / "query_pack.md").read_text()),
    lint_scope="Touched idea schema, canonical IDs and edge targets, local idea links, duplicate node IDs, unchanged experiment ledger and claim files, query budget. Historical proof/content audit not rerun.",
    lint_errors=errors,
    effective_plan="context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md",
    canonical_registry="context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    command="python research/ddp/refresh_20261029/apply_wiki_refresh.py")
(OUT / "WIKI_IMPORT_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(receipt, ensure_ascii=False))
