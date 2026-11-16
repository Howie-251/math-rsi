# MathRSI `v5` 后续维护（DD 37,632 & 42,433）更新方案与展示设计

主笔：Gemini（结合第二轮 Root 裁定与 `checks/WORKFLOW_TOOL_AUDIT.md` 定稿）  
日期：2026-11-16  
目标仓库分支：`/Users/rfy_naiveai/Desktop/MathRSI-v5-dd-20261116`（分支 `feat/v5-dd-followup-20261116`，演进记录 `development/evolution/v5-dd-20261116/EVOLUTION.md`）  
对照基线：`current-mathrsi/`（已发布 `main` @ `80fd0ffcf291d39383dd7cec2e73f75dc2d875e0`，即含 Q7 改动的 `v5`） vs 包内 `framework_snapshot/`（`2026-11-11 main` 本地整合分支）。

---

## 1. 对工作流工具审计（`checks/WORKFLOW_TOOL_AUDIT.md`）与边界取舍的明确确认

结合已核实的原始失败轨迹（`ROUTE_REPORT` 滞后导致下游误判零成果、`Gemini 036` 建议重开已退队的 `88452`、`D15` 已返回 `UNKNOWN` 仍标 `READY`、以及 `MAX8` 批次上限与机制耗尽混淆），**完全确认并支持** Root 与 Sol 审计确定的采纳边界：

1. **采用“可选既有 `STATE.json` 短当前事实读写/派发守卫（`base/tools/current_context.py`）+ DD 收据消费适配器（`plugins/degree-diameter/tools/extension_receipts.py`）”**：
   - 仅针对已有结构化 `STATE.json` 的持续任务按需启用（opt-in），不建立第二套全局状态库，不强制所有数学题目迁移 JSON，也不引入后台 watcher 或新调度器。
   - **必须带入三项实证修复与一项领域解耦**（均已在集成分支验证 7 项回归 PASS）：
     1. **Base 去领域化**：将 `families / accepted_orders / concrete_Lean_count` 派生计数从 `base/tools/current_context.py` 迁回 DD 插件侧，Base 只管通用的 `current_context` 原子替换、可选视图刷新、未消费 `terminal_result` 拦截与 `task / reuse / delta / new` 输入装配。
     2. **相对路径锚定修复（2 处）**：`current_context.py:request_text()` 中 `prior_reviews[].path` 与 `terminal_result` 统一相对于 `state_dir`（`STATE.json` 所在目录）解析；`d5_blocking_batch.py` 的 `build_plan() / execute()` 中相对 `latest_graph['edge_file']` 统一相对于 `state_path.parent` 解析，消除跨目录调用时的 `FileNotFoundError`。
     3. **源图真实身份绑定修复（1 处）**：`extension_receipts.py:consume()` 不能只查 `source.n in known`（否则会放行 `n=42402, m=1` 的错误源），必须同时核对所选已接受源记录的 `(n, m)` 及对应已接受源证据/路径绑定（历史收据对照其各自已接受检查点记录，无需引入全图哈希，也不要求旧收据源等于当前 `latest_graph`）。
2. **为什么修正版 `d5_blocking_batch.py / .cpp` 与 `extension_receipts.py` 应放入 `plugins/degree-diameter/tools/` 而非只塞 `archive/`**：
   - **明确回应此前分歧**：将特定家族工具放入 `plugins/degree-diameter/tools/` **并不等于冒充任意 $D=5$ 通用框架**——只要工具入口、代码守卫（`generator_domain == "d12_754_planes_core41356"`）与文档明确标定 `degree 12 / core < 41356 / 754 actual-ID planes` 并拒绝其他 family，`extension_receipts.py` 同样明确限定原逐点保边前缀检查器收据格式不作泛化。
   - **不可变归档 vs 可调用修正工具的分工**：`archive/dd-latest-two-parameters-20261116/` 是严格只读的原始证据包（保留了 `RAW_PLANES_ACTUAL_IDS.txt` 与历史未改源码，不能在其内部打路径或源绑定补丁）；把带入三项修复后的可执行版本放在 `plugins/degree-diameter/tools/`（与 `base/tools/current_context.py` 保持 `ROOT = parents[3]` 同构布局），才能直接读取归档内的 `RAW_PLANES_ACTUAL_IDS.txt` 和最新已接受图完成真实的家族有界续接。保留 `--plan-only`、`ACTIVE` 门、未消费 `terminal_result` 拦截、源变更失效拦截与 `independent_validation: PENDING`。

---

## 2. 版本定位与相对当前 `v5` 的精确改动矩阵

- **版本定位**：作为 **`v5 main` 后续维护** 落地（固定 `v5` tag 保持不变，`v6` 留待后续新进展），体例对齐 `docs/V4_CHANGES.md` 中的 `## Subsequent v4 maintenance on main`。保持 **10 Base 技能、6 领域、14 领域技能** 不变。
- **合并红线**：绝不用 `framework_snapshot` 覆盖 `v5` 技能全文！必须完整保留 `v5`（Q7）在 `base/skills/mathrsi-research/SKILL.md`（第 97 行）与 `base/skills/mathrsi-route-loop/SKILL.md`（第 92、116 行）的 `actual-input-coverage.md` 段落；同时**不拷入** `framework_snapshot` DD 技能中未随包附带的 `search-feedback.md / candidate_selection.py / search_operations.py` 死链引用。
- **归档与全局计数口径**：全量 **455** 个原件（含便携复生/核验脚本与两张最终边表）已就位于 `plugins/degree-diameter/archive/dd-latest-two-parameters-20261116/`，无需裁剪或追加哈希。源报告中的 `195 版本 / 44 参数 / 49 具体 Lean` 仅在内部溯源时如实标注为“源运行目录报告值”，未经全集独立复审**不向公开主页扩报该全局总数**。

### 具体文件改动清单

| 层级 | 仓库内目标路径 | 动作 | 核心内容与对接说明 |
|---|---|---|---|
| **Base** | `base/skills/mathrsi-research/SKILL.md` | 增量编辑 | 在 §Wiki 后接入可选 `current-context`（收件→写回短视图→派发）及“单批限额/`UNKNOWN` ≠ 充分域查尽”；保留第 97 行 Q7 段。 |
| **Base** | `base/skills/mathrsi-route-loop/SKILL.md` | 增量编辑 | Phase A / Phase D 同源读取当前事实快照与已停路线，按 `reuse / delta / new` 控制外审粒度；保留第 92、116 行 Q7 段。 |
| **Base** | `base/skills/mathrsi-research/references/current-context.md` | 新增 | 直接采用 `gemini/CURRENT_CONTEXT.md`（已同步相对路径基准与领域解耦后的真实契约）。 |
| **Base** | `base/tools/current_context.py` + 对应测试 | 新增（已净化修复） | 移除 DD 计数分支，修复 `prior_reviews[].path` 相对 `state_dir` 解析。 |
| **DD Plugin** | `plugins/degree-diameter/references/dd-methods.md`（或 Root 指定文件名） | 新增 | 直接采用 `gemini/DD_METHODS.md`（覆盖 D12 极小 $P$+全自由尾+折叠成本、D11 反例撤回前部+分量换向+共同锚点+核心/161 根混合覆盖、有限批次与共享 Lean 缺口、便携复验及专用批次工具调用）。 |
| **DD Plugin** | `plugins/degree-diameter/tools/{extension_receipts.py, d5_blocking_batch.py, d5_blocking_batch.cpp}` + 测试 | 新增（已修复） | 含 `(n, m)` + 已接受源证据绑定修复、`edge_file` 相对 `state_path.parent` 解析及 DD 侧计数派生；显式限定 D12/41356/754 平面域。 |
| **DD Plugin** | `plugins/degree-diameter/skills/{dd-construction, mathrsi-degree-diameter}/SKILL.md` | 增量编辑 | 接入上述 D12 / D11 方法与 `dd-methods` 参考，无缺失脚本死链；`dd-obstruction-certificate` 可选同步混合点对核验说明。 |
| **DD Plugin** | `plugins/degree-diameter/archive/dd-latest-two-parameters-20261116/` | 已就位（只读） | 完整 455 文件归档，提供 `reproduce.py`、`verify.py`、`check_roots.cpp`、直接输入、两张最终图与原始收据。 |
| **Docs / Site** | `docs/V5_CHANGES.md`、`README.md`、双语主页及 `development/evolution/v5-dd-20261116/EVOLUTION.md` | 编辑 | 记录 `v5 main` 后续维护、公开比较基准（含实时核对日期与旧图历史口径）及双机制可视化（见 §3）。 |

---

## 3. README / 主页文案与可视化定稿建议（供 `mathrsi_github` 落地）

遵循第二轮裁定：
1. **D11 核心覆盖叙述与显式源认证桥（对齐 `checks/D11_BRIDGE_AUDIT.md`）**：任意点线双射 $\sigma$ 的奇关联路径转换（Rajiv Lemma 3.1）加字面 $\sigma/\pi$ 绑定给出主干直观，同时由特征 3 叉积恒等式、三坐标核单射与 `check.cpp` 对每点实际 `91-star` 的有限检查构成显式源认证桥，无需另假设抽象 $H(9)$ 的关联直径。核心边包含关系由 `reproduce.py` 直接构造双射 $\sigma$ 与 `checks/REPORT.md` 独立逐边比对（及原 `check_other.py`）联合支撑，不单独归给未重构 $\sigma$ 的 `independent_check.py`，亦不扩报缺席目录 `route_core.py` 的 `664,272 / 28` 细分计数。4 个通用特征 3 Lean 模块已编译，具体 `Fin 37632` 实例 Lean 仍开放。
2. **公开表措辞纪律**：严格表述为**“超过当次（2026-11-16）核对的 Comellas 公开表值”**，绝不写成“刷新了公开主表”或暗示公开维护表已收录更新。突出 `(11,5) = 37,632`（较当次表值 `37,631` 增 `+1`）与 `(12,5) = 42,433`（较阶段起点 `42,402` 增 `+31`、较当次表值 `42,352` 高 `+81`）；保留 `(10,4) = 2,567`、`(16,4) = 16,416` 的原核对日期口径（实时表已为 `2,612`、`16,848`）；**不在主页扩报未经全集复审的 `195/44/49` 目录总数**。

### 3.1 结果对照表（可直接用于 `README.md` / `V5_CHANGES.md` / 主页）

| Parameter `(Δ, D)` | MathRSI Order `n` (Edges `m`) | Phase Start | Comellas Table | Gain vs Table | Verification & Formal Scope |
|---|---|---:|---|---:|---|
| **`(11, 5)`** | **`37,632`** (`205,366`) | `37,631` (`+1`) | `37,631` *(live 2026-11-16)* | **`+1`** | True-$H(9)$ odd-path / $\sigma,\pi$ core theorem + all 161 exterior/new BFS roots; generic `H9Cross*` Lean modules compiled, concrete `Fin 37632` Lean open |
| **`(12, 5)`** | **`42,433`** (`246,309`) | `42,402` (`+31`) | `42,352` *(live 2026-11-16)* | **`+81`** | Accepted `42,402` $D\le 5$ source + edge retention + all 31 added BFS roots (plus 31 prefix receipts); generic `SingleExtension` Lean proved, source Lean open |
| `(10, 4)` *(historical)* | `2,567` (`12,835`) | `2,557` (`+10`) | `2,566` *(at 2026-11-05; `2,612` live)* | `+1` *(dated)* | All-roots BFS + concrete Lean completed (`2,558`, `2,567`) |
| `(16, 4)` *(historical)* | `16,416` | — | *(surpassed live: `16,848`)* | dated | Preserved historical construction in DD archive |

### 3.2 中英文精炼正文（无防御性赘语、无未核全局总数）

**English (`README.md` / `docs/V5_CHANGES.md` / English page):**
> **Degree–Diameter ($D=5$): `N(11,5) ≥ 37,632` and `N(12,5) ≥ 42,433`** *(subsequent `v5` maintenance on `main`; produced in a local `2026-11-11 main` + DD workflow run)*.  
> Checked against the live Comellas degree–diameter table on November 16, 2026, two explicit simple graphs improve known $D=5$ entries: `(11,5)` reaches **`37,632`** (`+1` over `37,631`, `205,366` edges) and `(12,5)` advances from our prior `42,402` graph through 31 consecutive extensions to **`42,433`** (`+31` in this phase; **`+81`** over the table's `42,352`, `246,309` edges). Earlier highlights such as `(10,4) = 2,567` and `(16,4) = 16,416` retain their original comparison dates alongside newer public entries (`2,612` and `16,848`).  
> - **`(12,5)` minimal plane blockers and folded port cost**: Rather than restricting to 85 fixed Rédei-15 templates or rigid `10+2` role splits, the search enumerates inclusion-minimal 91-line blocking sets $P$ in totally isotropic $PG(2,9)$ planes, prices degree usage by folded core pins $|\pi(B)|$ instead of raw points $|B|$ ($18$ raw points with $2$ fixed points and $8$ conjugate pairs cost $10$ ports, beating $17$ raw points at $11$ ports), and completes remaining peripheral $R_4$ targets over all current spare-degree vertices $F \setminus P$.  
> - **`(11,5)` partial-fold recoloring, component orientation, and exact anchor intersection**: Because fixed source colors left empty provider lines on every known plane, split-fiber colors $c$ on the $4,074$ split fibers and `plane 605` core ports were solved jointly, rebuilding the $37,471$-vertex core (`-186 / +212` core edges). After a strict single-anchor obstruction (`(37546, 37618)` forcing saturated vertex `37618`) ruled out tail tuning on the initial orientation, complementing the $4,060$-fiber connected component reduced color flips against the source from `3,955` to `105` while preserving all vertex degrees, repairing all four old-exterior distance-6 pairs; intersecting legal anchors across the remaining three bad pairs closed `37,632` at anchor `31`.  
> - **Portable verification and Lean boundary**: Bundled `reproduce.py` and `verify.py` deterministically rebuild both edge sets from direct inputs and check all uncovered vertex pairs (`161` full BFS roots for `37,632` paired with the explicit characteristic-3 cross-routing / 91-star and $\sigma,\pi$-bound core theorem; `31` added BFS roots plus exact edge retention over the `42,402` source for `42,433`). Generic Lean theorems (`SingleExtension` and characteristic-3 `H9CrossRouting / Geometry / Kernel / Star`) compile with standard axioms only, while concrete source and graph-instance Lean assembly remain open.

**中文（双语页面 / 中文维护说明）：**
> **度数—直径问题（$D=5$）：`N(11,5) ≥ 37,632` 与 `N(12,5) ≥ 42,433`**（`v5 main` 后续维护；产自基于 `2026-11-11 main` 的本地 DD 工作流运行）。  
> 对照 2026-11-16 实时核对的 Comellas 公开表，两张显式简单无向图超过当次公开表值：`(11,5)` 构造出 **`37,632`** 点（较当次表值 `37,631` 多 **`+1`**，`205,366` 边）；`(12,5)` 由项目前值 `42,402` 连续保边扩张 31 步至 **`42,433`** 点（本阶段增 `+31`，较当次表值 `42,352` 高 **`+81`**，`246,309` 边）。`(10,4)=2,567` 与 `(16,4)=16,416` 等早期亮点保留各自核对日期的比较口径（当前公开表已分别为 `2,612` 与 `16,848`）。  
> - **`(12,5)` 极小平面阻塞集、折叠端口计费与全余度共同补全**：放开旧 85 个固定 Rédei-15 模板及硬性核心/守卫配额，枚举全奇异射影平面 $PG(2,9)$ 的包含极小 91 线命中集 $P$，按折叠映射后的实际端口数 $|\pi(B)|$ 计费（18 个几何原点含 2 固定点 + 8 共轭对时仅耗 10 个端口，优于 17 原点的 11 端口），并在当前完整图的全部余度点 $F\setminus P$ 中共同补齐外围四步覆盖。  
> - **`(11,5)` 部分折叠联合改色、分量换向与精确锚点交集**：固定源颜色在 1,120 张平面上均遇空行障碍后，对 4,074 个 split fibers 的颜色与 `plane 605` 的 10 个核心端口联合求解并重建 `37,471` 点核心（核心边 `-186 / +212`）。首方向因坏对 `(37546, 37618)` 迫使唯一锚点落在已满度的 `37618` 而被严格排除单边修尾；随后对 4,060 点连通分量整体补色换向，在逐点保持度数不变的前提下将相对源图的改色数由 `3,955` 压至 `105`，修好全部 4 对旧外围超距点对，再对剩余 3 对涉新点坏对求精确共同锚点交集（取锚点 `31`）完成构造。  
> - **便携复验与形式化边界**：归档包内 `reproduce.py` 与 `verify.py` 从直接输入确定性复生两张最终边表并覆盖全部待检点对（`37,632` 由显式特征 3 叉积路由/91-star 及字面 $\sigma,\pi$ 绑定的核心全称定理 + 全部 `161` 个外围/新根完整 BFS 闭合；`42,433` 由 `42,402` 源保边继承 + 全部 `31` 个新增根完整 BFS 闭合）。通用条件/代数 Lean 模块（`SingleExtension` 及特征 3 `H9CrossRouting / Geometry / Kernel / Star`）已通过内核检查且仅依赖标准三公理；具体源图与整图实例 Lean 仍开放。

### 3.3 双面板机制 SVG 图解规格（供 `mathrsi_github` 绘图实现）

- **Panel A（左）— `(12,5) 42,402 → 42,433`：Folded Port Pricing & Unrestricted Free-Tail Completion**
  - **视觉主轴**：左侧 `PG(2,9)` 91-line isotropic plane $\xrightarrow{\pi}$ 中间 `Core (41,356 vertices)` + 右侧 `Growing Periphery (1,046 → 1,076 vertices)`。
  - **关键数字对比框**：
    - `17 raw pts (5 fixed + 6 pairs) → 11 core pins + 1 tail guard`（首图 `42,403`：`plane 340` 的 `P11` + 单守卫 `41421` 一次补齐全部 11 个外围缺口）；
    - `18 raw pts (2 fixed + 8 pairs) → 10 core pins + 2 tail guards`（raw 点更多但折叠端口更省）；
    - `18 raw pts (6 fixed + 6 pairs) → 12 core pins + 0 guards`（核心集自身兼覆外围）。
  - **底部边际耗损微图**：4 个有界批次随余度消耗的搜索检查量 `P_tail_checks`：`1` (`+1`) $\to$ `1,084` (`+8`) $\to$ `10,871` (`+8`) $\to$ `88,500` (`+14`, 触 20s CPU 预算停于 `UNKNOWN`，不冒充耗尽)。
- **Panel B（右）— `(11,5) 37,631 → 37,632`：Core Recoloring, Component Flip & Hybrid Pair Cover**
  - **上半部（三步决策转折）**：
    1. `Canonical Orientation`（`3,955` flips）：`7` bad pairs (`d=6`)；`(37546, 37618)` forces `deg=11` vertex `37618` $\implies$ **Strict 1-Anchor Refutation (stop tuning tail)**；
    2. `4,060-Component Flip`（`105` flips vs source, `-186/+212` core edges, identical degree vector）：**4/4 old-exterior bad pairs healed**, only `3` $z$-pairs remain；
    3. `Exact Anchor Intersection`（over `2,409` spare-degree candidates）：`161` common anchors survive $\implies$ pick `anchor = 31` + `10 pins` on `plane 605` = **`37,632` (`0` bad pairs)**.
  - **下半部（$2\times 2$ 全点对覆盖分块）**：横纵均切分为 `Core (0..37,470)` 与 `Exterior + z (37,471..37,631, 161 roots)`：左上 `Core × Core` 标 `True H(9) odd-path + literal σ/π binding`；其余三块合并标 `Complete BFS from all 161 roots (0.22 CPU s)`。
