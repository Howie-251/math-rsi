#!/usr/bin/env python3
"""Apply this refresh to the existing plan and case registry, preserving history."""
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil

PROJECT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent
ACTIVE = PROJECT / "context/DD_PORTFOLIO_START_20261026"
existing_registry = json.loads((ACTIVE / "registry/cases.json").read_text())
if existing_registry.get("refresh_source") == "context/DD_PORTFOLIO_REFRESH_20261029/registry/cases.json":
    print("ALREADY_APPLIED_NO_WRITES: keep newer local research and registry evidence")
    raise SystemExit(0)
stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
archive = ACTIVE / "archive" / ("before_refresh_" + stamp)
archive.mkdir(parents=True, exist_ok=True)
for name in ["RESEARCH_GOAL.md", "registry/cases.json"]:
    dest = archive / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ACTIVE / name, dest)

original = (SOURCE / "RESEARCH_GOAL.md").read_text()
body = original
for name in ["CASEBOOK.md", "ENGINEERING_PILOT.md", "PRIOR_WORK_AND_DELTA.md"]:
    body = body.replace("`" + name + "`", "`context/DD_PORTFOLIO_REFRESH_20261029/" + name + "`")
body = body.replace("`registry/cases.json`", "`context/DD_PORTFOLIO_START_20261026/registry/cases.json`")
header = f"""# 当前同一 Degree Diameter Goal 的唯一有效计划

生效日期：2026-10-29；用户已明确按新版恢复，同一 Goal 为 ACTIVE。
实际读取路径保持 `context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md`。
本次来源：`context/DD_PORTFOLIO_REFRESH_20261029/IMPORT_AND_APPLY.md` 及新版交付稿；新包只作来源，不是并行有效计划。
合并前的本机原计划完整保留于 `{archive.relative_to(PROJECT)}/RESEARCH_GOAL.md`。旧27格硬边界、初始M1/M2优先队列及历史“当前”段不再派发任务；原始结果、人工意见和严格停止范围保留。

## 本机继承与实际资源约束

- 唯一 Wiki：`research-wiki/`；唯一恢复入口：`context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md`；同一报告：`research/progress.html`。
- 最新本地成果以 `research/ddp/more_graphs_20261027/delivery/families.json` 为准。本次读取仍为103个不同阶数图、3参数，最强37631/42402/51457，完整具体图Lean实例0。交付后的专家材料保留，不作为新数学结果。
- 原始作者署名、首图独立检查和后续完整current-R4归纳的实际范围不变；不逐图重复已核准源的全源BFS或跨模型审阅。
- 本机 ARIS 通过 `.aris/installed-skills-codex.txt` 解析；不安装或升级依赖。主模型及代理继承当前配置，不由材料包强制切换。
- 跨模型审阅沿用本机 Antigravity，按原授权请求 `gemini-3.8-flash-high`、`high`，保留实际回执；失败或空返回不算通过，不自动重试付费失败。
- 形式化继续锁定 Lean 4.24.0，沿用原formal工程，不添加sorryAx、未证公理或native_decide。新结果最终仍须实际绑定图与正确性证明，不让历史形式化阻塞数学发现。
- 数值资源以当前CPU affinity、cgroup quota、内存与其他作业为准；本轮先单worker。恢复时资源核对保存于 `research/ddp/refresh_20261029/RESOURCE_AND_EXISTING_DATA.md`，不把55核写成独占或永久配置。
- 严格已排范围不重跑；一般十五度非对称域仍UNKNOWN，既有canonical/成线/反射有限批次不自动续时。D2、n61谱、h5/h6等旧队列继续暂停。
- 原用户禁止主动计算、保存或汇报哈希/校验和的规则不变。完整旧历史和原人工comments留原位。

以下正文是合并后的研究循环、选题与验收要求，和本节共同构成唯一有效计划。

---

"""
(ACTIVE / "RESEARCH_GOAL.md").write_text(header + body)

path = ACTIVE / "registry/cases.json"
registry = json.loads(path.read_text())
proposal = json.loads((SOURCE / "registry/cases.json").read_text())
by_key = {(c["degree_cap"], c["diameter_cap"]): c for c in registry["cases"]}
family = json.loads((PROJECT / "research/ddp/more_graphs_20261027/delivery/families.json").read_text())
for draft in proposal["cases"]:
    key = draft["delta"], draft["diameter_limit"]
    if key not in by_key:
        case = {"id": f"d{key[0]}_D{key[1]}", "degree_cap": key[0], "diameter_cap": key[1]}
        registry["cases"].append(case)
        by_key[key] = case
    case = by_key[key]
    case["refresh_20261029"] = draft
    case["baseline_order"] = draft["public_lower_bound_snapshot"]
    case["baseline_as_of"] = draft["baseline_checked_on"]
    case["table_url"] = draft["baseline_source"]
    case["opportunity_lane"] = draft["priority_lane"]
    case["activation_status"] = "not_automatically_dispatched"
    local = draft.get("local_best_reported")
    if key[1] == 5 and str(key[0]) in family["families"]:
        local = max(family["families"][str(key[0])]["example_orders"])
        case["local_verified_best"] = local
        case["local_best_evidence"] = "research/ddp/more_graphs_20261027/delivery/families.json"
    case["minimum_record_improving_order"] = max(case["baseline_order"], local or 0) + 1
    if case.get("research_status") == "NOT_STARTED":
        case["research_status"] = "consult_inherited_experiments_not_a_fresh_queue"

registry["scope_before_refresh_20261029"] = registry["scope"]
registry["scope"] = proposal["research_scope"]
registry["snapshot_date"] = "2026-10-29"
registry["refresh_source"] = str((SOURCE / "registry/cases.json").relative_to(PROJECT))
registry["refresh_status"] = "merged_into_existing_registry; candidate list is not an automatic queue"
path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n")
print("Active plan:", (ACTIVE / "RESEARCH_GOAL.md").relative_to(PROJECT))
print("Preserved archive:", archive.relative_to(PROJECT))
print("Registry cases:", len(registry["cases"]), "refreshed candidates:", len(proposal["cases"]))
