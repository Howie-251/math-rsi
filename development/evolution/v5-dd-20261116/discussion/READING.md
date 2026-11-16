# DD 最新两组参数成果精读与证据核查（D11 = 37,632，D12 = 42,433）

整理人：Gemini（主读与综合）  
日期：2026-11-16  
原件根前缀约定：若无特别说明，包内路径相对于 `source/DD_latest_two_parameters_20261116/`；原工作区快照前缀缩写为 `ORIG = originals/ar4math/research/ddp/expert15_20261114/d5_resume_20261115/`，`RW = ORIG/resume_workflow_20261115/`。当前已发布框架对照摘录相对于 `current-mathrsi/`（对应 `main` 提交 `80fd0ffcf291d39383dd7cec2e73f75dc2d875e0`，即含 Q7 演进的 `v5`）。

---

## 0. 阅读与核查覆盖边界声明

- **本人直接精读的原件**：
  - 顶层与可移植复验：`README.txt`、`RESULTS_SNAPSHOT.json`、`PROOF_AND_RESULTS.txt`、`TRAJECTORY.txt`、`MATHRSI_VERSION.txt`、`reproduce.py`、`verify.py`、`check_roots.cpp`、`checks/CLEAN_REPRODUCTION_RESULT.json`、`inputs/d12_additions.json`（前部结构与字段）。
  - 人工指令、轨迹复盘与代码评议：`originals/ar4math/DD_D5_SUCCESS_MECHANISMS_AND_NEW_BRANCHES_20261115.txt`、`TRAJECTORY_FEEDBACK_FOR_CODE_AGENT_20261115.txt`、`mathrsi_dd_trajectory_review_20261115_0915_1329.txt`、`ORIG/WHOLE_REVIEW_20261115_1153_DISPOSITION.txt`、`RW/CONTINUATION_COST_JUDGMENT.txt`、`RW/GEMINI_FLASH_DELTA_DISPOSITION_20261116.txt`。
  - D11（37,632）证明、文献、代码与绑定链：`originals/ar4math/research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/23056128_partial-folds-split-cayley-hexagon-H9-large-graphs-diameter-five.txt`（§1–6，尤其 Theorem 2.1、Lemma 3.1、Lemma 4.1、Theorem 5.1–5.2）、`ORIG/d11_weighted_plane_transfer/FACT_REPORT.txt`、`RW/h9_core_certificate_review.txt`、`RW/h9_joint_gate/batch202/RESULT.json`、`RW/h9_exact_binding/{RESULT.json,ATTEMPT_HISTORY.jsonl}`、`RW/H9_COMPLETION_PATH_REVIEW_20261116.txt`、`RW/h9_independent_completion/check.cpp`、`RW/h9_independent_completion/canonical37632/ONE_TAIL_NO_WITNESS.json`、`RW/h9_other_orientation/REPORT.txt`、`RW/h9_independent_completion/other37632/BINDING.json`、`RW/h9_n37632/{PROOF_AND_TRAJECTORY.txt,independent/RESULT.json}`、`RW/h9_explicit_cross_route_20261116/PROOF.txt`、`RW/h9_cross_minor_completeness_20261116/PROOF_AND_BINDING.txt`、`RW/h9_cross_finite_binding_20261116/RESULT.json`、`RW/h9_actual_source_bridge_20261116/{PROOF.txt,RESULT.json,STATIC_CHECK.json}`。
  - D12（42,433）证明、资源门、搜索代码与批次收据：`ORIG/d12_weighted_plane_cover/{RESULT.json,JOINT_MODEL_PROOF_MEMO.txt,EXTERNAL_RESOURCE_EXPLANATION.json,joint_cover/RESULT.json}`、`ORIG/d12_n42403/GEOMETRIC_MECHANISM.txt`、`ORIG/d12_blocking_family_continuation/{PORT_COST_INSIGHT.txt,GEOMETRY_SERIES_EXPLANATION.txt}`、`RW/d12_batch02/{RESULT.json,independent/RESULT.json}`、`framework_snapshot/plugins/degree-diameter/tools/d5_blocking_batch.cpp`。
  - 形式化（Lean）模块与编译记录：`formal/DegreeDiameter/Portfolio/SingleExtension.lean`、`ORIG/d12_n42403/formal/{SOURCE_CERTIFICATION_BOUNDARY.txt,FINAL_STATUS.txt}`、`RW/SOURCE_CERTIFICATION_PATH_JUDGMENT.txt`、`RW/h9_cross_lean_local_20261116/REPORT.txt`、`RW/h9_cross_geometry_lean_20261116/REPORT.txt`、`RW/h9_cross_kernel_lean_20261116/REPORT.txt`、`RW/h9_cross_star_lean_20261116/REPORT.txt`、`RW/h9_actual_normalization_20261116/PROOF_AND_BINDING.txt`。
  - 本地框架快照与当前 `v5` 全量对照：`framework_snapshot/` 下全部 13 个文件、`current-mathrsi/` 下全部 8 个文件，以及本目录 `PUBLIC_BASELINE.md` 和 `checks/REPORT.md`。
- **未逐份展开的重复性文件与未执行事项**：未逐一打开 `prefixes/n42404..n42433` 的 30 对独立 `CATALOG_ENTRY.json / PARAMETERS.json`、大二进制表内容、CNF 文本（`model.cnf`）或早先多轮 `018..036` 全部 JSON 回件；未在本会话运行图搜索、全根 BFS、Lean 编译或付费外部审阅。边集重建一致性、有限数组结构一致性与 161 / 31 指定根完整 BFS 消费同目录独立核查报告 `checks/REPORT.md`（总计约 5.05 CPU 秒，全部 exit 0）；工作流辅助脚本边界与三处路径/源绑定修复消费 `checks/WORKFLOW_TOOL_AUDIT.md`。

---

## 1. 核心新成果与基准边界：究竟新在哪里？

本次新增成果是**两个既有已研究参数 `(11,5)` 与 `(12,5)` 上的新下界构造**（源运行报告记录项目参数对仍为 `44`、新增参数对 `0`，源目录合法图版本记账由 `163` 经 `172` 增至 `195`，闭合具体图 Lean 实例仍记 `49`、新增 `0`；注：`195/44/49` 为源运行内部目录口径，未经全集重审不向公开主页扩报）：

| 参数 `(Δ, D)` | 本阶段起点图（本地前值） | 本包最终图 `(n, m)` | 相对本地前值增益 | 实时核对 Comellas 主表值（2026-11-16） | 相对公开主表增益 | 新增合法阶数序列 |
|---|---:|---|---:|---:|---:|---|
| `(11, 5)` | `37,631` (`205,329` 边) | **`37,632`** (`205,366` 边) | **`+1`** | `37,631` | **`+1`** | `37632`（1 个） |
| `(12, 5)` | `42,402` (`245,937` 边) | **`42,433`** (`246,309` 边) | **`+31`** | `42,352` | **`+81`** | `42403..42433`（31 个，分 `1+8+8+14` 四批） |

**必须严格区分的三条基准边界**（证据：`RESULTS_SNAPSHOT.json`、`PUBLIC_BASELINE.md`、`DD_D5_SUCCESS_MECHANISMS_AND_NEW_BRANCHES_20261115.txt` §1.6）：
1. **阶段增量 vs 对表总增益**：`(12,5)` 的对表 `+81` 包含此前本地 `42,342 → 42,402` 相对主表 `42,352` 已有的 `+50` 以及本阶段新增的 `+31`，不能把 `+81` 全部记为本轮搜索增量，也不能把 31 个同族前缀写成 31 种独立方法。
2. **主表核对 vs 全球优先权**：Root 于 2026-11-16 实时核对 Comellas 主表（含其 2026-11-12 更新记录），确认 `(11,5)=37,631`、`(12,5)=42,352`；这证明两图严格超过当次核对公开主表，但不构成穷尽预印本/数据集的全球优先权宣称（`global_priority: not established`）。
3. **当前领先项 vs 历史带日期亮点**：实时 Comellas 主表中 `(10,4)` 已升至 `2,612`（项目 `v4` 历史图为 `2,567`），`(16,4)` 已升至 `16,848`（项目历史图为 `16,416`），`(13,5)` 此前亦已知有更大公开图超过 `51,457`。因此展示层必须将 `(11,5)=37,632` 与 `(12,5)=42,433` 标为截至 2026-11-16 对主表的改进，同时保持旧亮点（如 `2,567`、`16,416`）的核对日期历史口径。

---

## 2. D11 (`37,632`)：核心改色重建、真实几何绑定与全体点对覆盖链

### 2.1 为什么不能用纯保边增点，核心到底改了什么？
- **固定颜色下的全平面空行障碍**（`ORIG/d11_weighted_plane_transfer/FACT_REPORT.txt`、`RESULT.json`）：在 `37,631` 源图（核心 `0..37470` 共 `37,471` 点，外围 `37471..37630` 共 `160` 点，全图 `2,471` 个余度点）上，沿恢复映射 `point_to_core11.u16.bin` 检查全部 `1,120` 个 $\mathbb{F}_3$-定义全奇异平面（364 flat + 756 nonflat），**每一个平面都至少有一条射影线没有任何余度 provider**（`retained = 0`，耗时 `0.198` CPU 秒）。因此照搬 D12 在固定源上找平面阻塞集立即无解。
- **回到 H(9) partial-fold 的联合改色构造**（文献：`23056128_partial-folds...txt` §2–5；生成器：`reproduce.py:construct_h9`、`RW/h9_n37632/generate.py`）：
  - 分裂 Cayley 六边形 $H(9)$ 有 $66,430$ 个点、$66,430$ 条线（每线 10 点、每点 10 线，关联直径 6），$\tau$ 为 4 阶对偶，$\varphi = \tau^2$ 为对合（固定子六边形 $H(3)$ 的 $364$ 个点与 $364$ 条线，其余点组成 $33,033$ 个二点 generic fibers $\{p, \varphi(p)\}$，商图 $F = \Gamma/\langle\tau\rangle$ 有 $33,397$ 点）。
  - 保持原图固定的 $|S| = 4,074$ 个 split fibers 不变（故折叠映射 $\pi: P \to \{0,\dots,37470\}$ 固定，核心点数 $33,397 + 4,074 = 37,471$），重新为每个 $f \in S$ 选取共同颜色 $c(f) \in \{0,1\}$（非 split 处 $\varepsilon = 0$，split 处 $\varepsilon(p)=\varepsilon(\varphi p)=c(f)$），定义双射 $\sigma_\varepsilon(p) = \tau(p)$（若 $\varepsilon(p)=1$）或 $\tau^{-1}(p)$（若 $\varepsilon(p)=0$）。
  - 核心无向边由 $p \neq q, q \in \sigma_\varepsilon(p) \implies \pi(p) \sim \pi(q)$ 生成（由 Rajiv Lemma 4.1，同一 fiber 两点不相邻故无自环；相邻 split fibers 同色成 $K_{2,2}$、异色成完美匹配 $2K_2$，从而颜色决定额外度数的分配位置）。
  - **实际改动幅度**：最终采用的 `other_orientation` 颜色相对原 `37,631` 源核心改变了 **105 个 split fibers**，使核心从原 `203,721` 条边变为 **`203,747` 条边（删去 186 条旧核心边、新增 212 条核心边）**。外围 `160` 个旧点（`37471..37630`）关联的 **`1,608` 条边原封保留**；新增顶点 `z = 37631` 连接 `11` 个固定 pins（`plane 605` 的 10 个核心端口 `48, 4182, 8315, 13413, 20704, 27995, 31375, 32268, 33171, 33663` 加共同外围修补锚点 `31`），总边数 $203,747 + 1,608 + 11 = 205,366$，最大度 `11`。
  - 因为删去了 186 条旧核心边，“原图所有旧边保留”的单调归纳对 D11 **完全不适用**。

### 2.2 全体 $\binom{37632}{2}$ 点对距离 $\le 5$ 与 $D=5$ 如何闭合？
全图顶点划分为核心 $V_{\text{core}} = \{0,\dots,37470\}$（$37,471$ 点）与非核心 $R = \{37471,\dots,37631\}$（`160` 旧外围 + 新点 `z`，共 `161` 点）：

1. **核心—核心点对（$V_{\text{core}} \times V_{\text{core}}$ 全称定理 + 实际有限数据绑定）**：
   包内实际包含**两层互补深度**的数学证据（需向审阅与维护者准确区分）：
   - **第一层（Rajiv Lemma 3.1 + Theorem 5.1 + 缓存数组字面绑定）**（见 `PROOF_AND_RESULTS.txt`、`RW/h9_independent_completion/other37632/BINDING.json`、`checks/REPORT.md`）：
     对广义六边形任意点线双射 $\sigma: P \to L$ 及任意原点 $p,q \in P$，因关联图二分且直径 $\le 6$，$p$ 到线 $\sigma(q)$ 必有长度 $2j-1 \le 5$ 的奇关联路径（最长情形 $p - L_1 - a - L_2 - b - \sigma(q)$）。将中间线 $L_i$ 替换为 $r_i = \sigma^{-1}(L_i)$，因 $p,a \in L_1 = \sigma(r_1)$ 且 $a,b \in L_2 = \sigma(r_2)$、$b \in \sigma(q)$，删去相邻相等停留项即得 $G_\sigma$ 中长度 $\le 5$ 的点图 walk；再经 $\pi$ 合并非 split 对不增加 walk 长度，且向核心外添加边不破坏核心内部最短路。在此层表述下，“输入数组构成关联直径 $\le 6$ 的真实 $H(9)$”依托 `RW/h9_exact_binding/build.cpp` 从 $GF(9)$ 坐标的原始生成与 `BINDING.json` 的逐边核验（`203,747` 核心边完全一致）。
   - **第二层（2026-11-16 显式特征 3 叉积路由桥——在数学层消除了“抽象广义六边形直径 6”外部进口）**（见 `RW/h9_explicit_cross_route_20261116/PROOF.txt`、`RW/h9_cross_minor_completeness_20261116/PROOF_AND_BINDING.txt`、`RW/h9_cross_finite_binding_20261116/RESULT.json`、`RW/h9_actual_source_bridge_20261116/PROOF.txt`）：
     - 在 $K = \mathbb{F}_3[t]/(t^2+1)$ 上，对七维坐标 $p=(u,s,v)$ 定义二次型 $Q(p)=u\cdot v - s^2$、极化型 $\beta(p,q)=u\cdot V + U\cdot v - 2st$ 与叉积 $C(p,q)=(sU-tu+v\times V,\; u\cdot V - v\cdot U,\; tv-sV+u\times U)$（其首尾 6 分量恰为作者 Tits 六条 Grassmann 关系的残差）。多项式恒等式 $C(p,C(p,q))=-\beta(p,q)p - Q(p)q$ 与 $Q(C(p,q))=Q(p)Q(q)-\beta(p,q)^2$ 经符号检验及 Lean 内核验证成立。
     - 对任意非零 null 点 $X(p)$，无需假设秩下界，由 6 个坐标 pivot 的显式线性消元构造单射 $\ker C(X(p),\cdot) \hookrightarrow K^3$，故 $|\ker C(X(p),\cdot)| \le 9^3 = 729$。
     - 独立程序 `h9_cross_finite_binding_20261116/check.cpp`（`0.137` CPU 秒，PASS）在字面二进制表上穷尽核验：全部 `66,430` 个点非零、规范化（首非零坐标为 1）、$Q=0$ 且单射；全部 `66,430` 条线各含 10 个不同点，恰为前两点张成的完整 10 点射影直线且基叉积 $C(R,W)=0$；每点恰在 10 条线上，其邻接点并集 $S_p$ 恰有 `91` 个点。
     - 由规范化唯一性，$0$ 与 $S_p$ 的 $91 \times 8 = 728$ 个非零标量倍构成 `729` 个互异核向量，结合上界 `729` 迫使该映射**满射到整个 $\ker C(X(p),\cdot)$**。由此立即推出：(i) $C(X(p),X(q))=0$（$p\neq q$）必共处于某条实际缓存线 $T(l)$（长 2）；(ii) $\beta(X(p),X(q))=0$ 且 $y=C(X(p),X(q))\neq 0$ 时，$y$ 规范化后必在字面点表中有实际 `PointID` $r \notin \{p,q\}$，给出实际缓存路径 $p - l_1 - r - l_2 - q$（长 4）；(iii) 任意点 $p$ 到任意缓存线 $T(l)=\text{PG}(\text{span}(R,W))$ 可显式取正交点 $q \in T(l)$（如 $\beta(p,W)R-\beta(p,R)W$ 规范化），给出长度 $\in \{1,3,5\}$ 的字面关联 walk。
     - 最后沿 `other_orientation/sigma.i32.bin` 与 `pi.u16.bin` 运输，每个字面关联对 $(p,l)$ 映为停留或最终图的实际核心边。*（精确归属校正，见 `checks/D11_BRIDGE_AUDIT.md`：原桥接文引用的 `h9_core_route_certificate_20261116/route_core.py` 目录未随 455 文件包附带，故不将其报告的 `664,272 / 28` 步数拆分扩报为本轮重放结论；但数学上的“核心边或停留”包含关系 F5 无缺口——由 `reproduce.py:construct_h9` 从字面 `tau/colors/lines/pi` 直接构造双射 $\sigma$ 并插入全部关联的 $\pi$ 像，联合 `checks/independent_check.py` 对最终边集的独立逐边相等核验及 $\pi$ 满射检查共同支撑，历史 `check_other.py` 亦独立重建了全部 `203,747` 条核心边。）*
2. **核心—外围与外围—外围点对（全部 161 个非核心根的完整 BFS）**：
   - 任何不全在 $V_{\text{core}}$ 内的点对 $(u,v)$ 至少有一端属于 $R = \{37471,\dots,37631\}$（共 `161` 点）。
   - 原独立检查器 `RW/h9_independent_completion/check.cpp`（输出 `RW/h9_n37632/independent/RAW_CHECK_RESULT.json` 与 `RESULT.json`，`0.856` CPU 秒）以及包根 `verify.py` / 本轮 `checks/REPORT.md`（`0.215` CPU 秒）直接从最终 `205,366` 条无向边重建邻接，核验简单性与全点度数 $\le 11$，并对 `37471..37631` 全部 **161 个根**运行到全图 `37,632` 点的完整 BFS：`unreachable = 0`，`maximum_checked_eccentricity = 5`。
   - 注意：候选生成时使用的“`plane 605` 命中 91 线 $\implies$ 核心四步覆盖”（`RW/h9_core_certificate_review.txt` 偶路径转换引理）在最终验收时甚至无需作为额外进口，因为新点 `37631` 本身就在这 161 个完整全图 BFS 根之中！
3. **直径下界 $D \ge 5$**：最大度 11、直径 4 的 Moore 界为 $M(11,4) = 1 + 11(1+10+100+1000) = 12,222 < 37,632$，故直径恰为 `5`。

### 2.3 D11 仍开放的精确边界（Lean 与终审）
- **已通过 Lean 内核的通用模块**（均仅依赖标准三公理 `propext, Classical.choice, Quot.sound`，无 `sorryAx` / `native_decide`）：
  - `H9CrossRouting.lean`（特征 3 叉积、范数、斜对称、极正交恒等式，`RW/h9_cross_lean_local_20261116/REPORT.txt`，18.11 CPU 秒）；
  - `H9CrossGeometry.lean`（$p\times q \neq 0$ 射影非退化与点到线显式正交投影，`RW/h9_cross_geometry_lean_20261116/REPORT.txt`，9.46 CPU 秒）；
  - `H9CrossKernel.lean`（6-pivot 消元给出 $\ker C(p,\cdot) \hookrightarrow K^3$ 单射，`RW/h9_cross_kernel_lean_20261116/REPORT.txt`，三次尝试共 27.60 CPU 秒）；
  - `H9CrossStar.lean`（`kernel_card_le` 与 `star729_surjective` 条件满射引理，`RW/h9_cross_star_lean_20261116/REPORT.txt`，2.03 CPU 秒）；
  - 另有 `F9Graph56862Field.lean`（九构造子字节域运算）。
- **未闭合的具体 Lean 缺口**（见 `RW/h9_actual_normalization_20261116/PROOF_AND_BINDING.txt` 与 `RW/h9_actual_source_bridge_20261116/PROOF.txt` §10 A–I）：
  - `H9CrossNormalize.lean` 在最终整体编译时触及进程剩余 CPU 上限（`SIGXCPU`, exit `-24`），未产出可用 `.olean`；
  - 字面 `66,430` 点/线/91-star 有限数据导入与核验定理、`other_orientation` 的 $\sigma/\pi$ 映射与 `664,300` 步运输、最终 `Fin 37632` 边表/度数证明，以及 `161` 个外围根在 Lean 内核中的五层可达证书（当前 `ROOT_RESULTS.jsonl` 只存离心率摘要，不含逐点 parent/depth 树）均尚未构建。
- **外部审阅边界**：`H9_GEMINI_RESPONSE.json` 遭遇配额错误；后续 `GEMINI_FLASH_DELTA_RESPONSE.json`（`gemini-3.8-flash-high`）完成了有实质内容的路线审阅并由 Root 处置纠偏（`RW/GEMINI_FLASH_DELTA_DISPOSITION_20261116.txt`），但原 Goal 合同要求的最终图终审仍保持开放。

---

## 3. D12 (`42,433`)：极小平面阻塞集 + 全余度共同补全、折叠端口成本与保边归纳

### 3.1 真正产生突破的数学与表示变化
- **起点与旧瓶颈**：从已接受的 `42,402` 点、`245,937` 边源图（核心 `0..41355` 共 `41,356` 点，外围 `41356..42401` 共 `1,046` 点，余度点 `13,857` 个）出发。旧 `85` 个 Rédei-15 模板受困于共享关键端口瓶颈（最多 4 个独立星族；尝试 spoke 转移腾端口会导致原宿主产生 887 个距离 >5 坏对）。
- **大联合 SAT 的实测停滞**：在 `1,120` 个全奇异平面经廉价必要门筛剩 `754` 个平面（354 个空线排除，12 个强制端口 >12 排除；`ORIG/d12_weighted_plane_cover/RESULT.json`）后，将全部 754 平面激活变量、`1,046` 个外围目标与 `13,857` 个自由点的 `atmost12` 编码进单一 CNF（`429,919` 子句，`joint_cover/RESULT.json`），单次求解 `180.038` CPU 秒（整批 `180.491` CPU 秒）返回 `UNKNOWN`（0 模型、0 完整候选）。
- **无损分解（核心极小阻塞集 $P$ + 全自由域尾部共同补全 $T$）**（原件：`ORIG/d12_weighted_plane_cover/JOINT_MODEL_PROOF_MEMO.txt`、`ORIG/WHOLE_REVIEW_20261115_1153_DISPOSITION.txt`、代码 `framework_snapshot/plugins/degree-diameter/tools/d5_blocking_batch.cpp`）：
  1. **核心充分性仅依赖 91 线命中**：全奇异平面 $\Pi \cong PG(2,9)$ 含 91 条射影线。任意核心原点 $p$ 的极超平面 $\ker \beta(p,\cdot)$ 在 $\Pi$ 上必含一条线；只要所选核心端口集 $P$ 在 $\Pi$ 内的原像命中全部 91 条线，即有原像 $x$ 使 $\beta(p,x)=0 \implies \text{dist}_H(p,x)\le 4 \implies \text{dist}_G(u, \pi(x)) \le 4$，故 $B_4^G(P)$ 覆盖全部 `41,356` 个核心顶点。该定理**不依赖** Rédei-15 形状、702 轨道、Frobenius 稳定性或 `10+2` / `11+1` 固定配额。
  2. **证书域内的包含极小分解**：任何具备平面 $\Pi$ 阻塞证书的合法邻集 $S$（$|S|\le 12$），其平面内部分必包含一个**包含极小（inclusion-minimal）**91 线命中集 $P$（`d5_blocking_batch.cpp` 第 35 行 `essential == chosen` 检查），而剩余尾部 $T = S \setminus P$ 可从**当前全部余度点 $F \setminus P$**（含同平面内未选的其他可用点！）中自由选取至多 $12 - |P|$ 个点，共同覆盖外围缺口 $R = \{41356,\dots,n-1\} \setminus B_4^G(P)$。
  3. **排序与精确位集剪枝**：按平面当前可用 pin 数升序排列 754 张平面（使极小阻塞集分支树最小的受限平面最先被搜），`Tail::dfs` 对外围缺口行做精确 bitset 分支定界（`remaining == 1` 时直接按位与求交，第 57–59 行），一旦命中立即在当前完整图上运行 `g.bfs(hitpins, 4)` 校验覆盖全部 $n$ 个顶点（第 118 行）。
  4. **首图命中**：20 CPU 秒探针在第一张平面 `plane 340` 的第一个 11-pin 极小核心集 `P11` 上，立刻找到单一共同守卫 `41421` 同时补齐全部 11 个外围遗漏点，整批仅 `2.157` CPU 秒（native `0.067` 秒）产出 `42,403`（`ORIG/d12_n42403/GEOMETRIC_MECHANISM.txt`）。

### 3.2 Raw 几何点数 vs 折叠后真实端口成本（`PORT_COST_INSIGHT.txt`、`GEOMETRY_SERIES_EXPLANATION.txt`）
- 新顶点支付的度数预算是**经折叠映射 $\pi$ 去重后的实际图顶点个数 $|P|$**，而非平面内原始几何点数 $|B|$。
- 对 Frobenius 稳定且所用共轭对均未 split 的原像集 $B$，若有 $f$ 个 $\mathbb{F}_3$-固定点与 $p$ 个二点共轭对，则 $|B| = f + 2p$，而实际端口成本仅为 $|P| = f + p$：
  - `42,403` 首例：`17` 个 raw 点（`5` 固定 + `6` 对）占 **`11` 个端口**（`11+1` 配额）；
  - `42,407`、`42,408` 等例：**`18` 个 raw 点**（`2` 固定 + `8` 对）反而只占 **`10` 个端口**，为外围留出 `2` 个守卫槽（`10+2` 配额）；
  - 另有 `18` 个 raw 点（`6` 固定 + `6` 对）占 **`12` 个端口**，当其自身已覆盖全部外围时直接形成 `12+0` 合法邻集。
- 前 9 步的核心集与旧 `85` 个 Rédei-15 模板逐一比对，无一相等或互含——证实突破来自打开任意极小线阻塞表示并按真实折叠端口计费，而非旧模板复燃。

### 3.3 逐步前缀验证、最终 31 根覆盖与源距离继承边界
- **操作性质**：从 `inputs/d12_source42402.edges`（`42,402` 点、`245,937` 边）起，按 `inputs/d12_additions.json` 依次插入 `z_0=42402, ..., z_{30}=42432`，每步连接 12 个当时度数 $<12$ 的互异旧点（包括此前新增且仍有余度的顶点），**不删改任何旧边**，最终 `42,433` 点、`246,309` 边。
- **两套完整覆盖证据均齐备**：
  1. **历史逐前缀归纳（证明全部 31 个中间阶数 `42403..42433` 均合法）**：分存四份独立收据（`d12_n42403` 1 步 + `d12_blocking_family_continuation` 8 步 + `d12_batch01` 8 步 + `d12_batch02` 14 步的 `independent/RESULT.json`，独立脚本 `verify_prefixes.py` 不共享作者缓存），每步核验全点度数 $\le 12$、旧边零删减，并在当时前缀 $G_{i+1}$ 上对新根 $z_i$ 做完整 BFS 确认偏心率 $\le 5$。
  2. **包根便携终图覆盖（直接证明最终 `42,433` 图合法）**：`verify.py` 与本轮 `checks/REPORT.md` 核验 $E(G_0) \subseteq E(G_{31})$（故所有 $\binom{42402}{2}$ 对旧—旧顶点距离 $\le 5$ 由 $G_0$ 单调继承），并在最终图 $G_{31}$ 上对 `42402..42432` **全部 31 个新增顶点**运行完整 BFS（`0.057` CPU 秒，最大偏心率 `5`），覆盖所有 old–new 与 new–new 点对。结合 Moore 界 $M(12,4) = 17,569 < 42,433$ 得 $D = 5$。
- **继承前提与 Lean 边界**：
  - **数学继承进口**：`42,402` 源图本身的 $D \le 5$ 作为已接受历史源进口继承（溯源至 Zenodo `42,342` 公开源 + 60 步保边 R4 序列，且项目存有 `42,377` 阶全 `42,377` 根独立 BFS 收据 `independent_all_source_BFS_42377.json`；见 `RW/SOURCE_CERTIFICATION_PATH_JUDGMENT.txt`）。
  - **形式化未闭缺口**：`formal/DegreeDiameter/Portfolio/SingleExtension.lean` 已给出无 `sorry` 的通用条件定理 `singleVertexExtension_diameterAtMostFive_of_parentDepth`，但其显式依赖 `hdiam : DiameterAtMost G 5` 与 `cert : ParentDepthCertificate G pins 4`。旧 `42,342 / 42,402` 源图无闭合 Lean 定理（`ORIG/d12_n42403/formal/SOURCE_CERTIFICATION_BOUNDARY.txt`）；`D12N42403Increment.lean` 在 GPFS 环境下三次尝试共 `1.007` CPU 秒后遭遇 `lean` 进程 `SIGSEGV`（exit `-11`，无证明错误诊断；见 `FINAL_STATUS.txt`）。此后正确将其归口为**单一家族共享源认证缺口**，不再为后续 `+30` 个前缀重复编译带相同缺口的 wrapper。

---

## 4. 失败路线、成本演变与人工/Root 纠偏轨迹

### 4.1 失败与限定否证路线（为什么失败、何时止损、暴露了什么问题）
依据 `mathrsi_dd_trajectory_review_20261115_0915_1329.txt` 与 `TRAJECTORY_FEEDBACK_FOR_CODE_AGENT_20261115.txt`：
1. **前期偏离（12 小时零出图）的真实原因**：此前给定的 15 项主池集中在 $D=3,4$ 与 $D=8,9$（无 $D=5$），且大量任务在满度源上强行“删边 + 补点 + 大 SAT 修旧路”。2026-11-15 人工指令（`DD_D5_SUCCESS_MECHANISMS_AND_NEW_BRANCHES_20261115.txt`）明确将主线拉回“$D=5$ 可扩张源筛选 + 保边四步覆盖”，同时保留约 1/3 预算给新点小网络（N1）与直接生成（N2）。
2. **具体受限否证与 `UNKNOWN` 账本**：
   - `(5,5)` 660 源：30 余度点全部 `142,506` 个 $\le 5$ 子集穷尽无解（最高 654/660）；相邻双新点 $K_2$ 模型求解器报 UNSAT（无外部证书）。
   - `(15,5)` 102,060 源：810 自由端口选 $\le 15$ 的唯一 SAT 跑满 `300.003` CPU 秒 `UNKNOWN`；5,000 次启发式共同候选与 2,390 次定向修复出现“修好指定纤维却在别处漏掉 296 点”的跷跷板效应，按约停算。
   - `(14,5)` 88,452 克隆线：全自由 `C` 模型 `298.269` CPU 秒 `UNKNOWN`；有界构造仅将中心从 4,698 增至 4,797（阶数 `93,249 < 94,186` 基线），09:15 全局重评撤下队列；后又通过 `94,186` 含 15 个 12 度点而 `88,452` 最小度为 13 的度数反证，严格排除了保边完整邻域克隆祖先假设（无需开同构搜索）。
   - 跨直径/代数探针：`441→882` `(4,6)` 拆分（`122.141` CPU 秒最坏仍 42,992 坏对，固定 A 容量不足，全 A 门 `60.315` 秒 `UNKNOWN`）；`2810` 两层匹配 `(8,5)`（`14,050` 代表坏对零净改善，10:30 重评叫停）；`(9,5)` 二次必要门（`5.299` 秒相容但非构造性，按约即停）；`PGL(2,13)` 偶对合（`3.077` 秒 91 例全 No）；`Loz1100` 模 5 恒同电压阻碍、`684/252/2810` 普通覆盖短返回词不足、$F_{23}$ 标量（`1.352` 秒 1,587 例 No）与圆锥曲线（`1.940` 秒 12,720 例 No）。
   - **关键工作流诊断（“否证接力”风险）**：虽然每个小否证数学上准确且单次仅几秒 CPU，但“排除一个子族 $\to$ 自动接下一个相近子族”在选题、协调和外审上消耗了大量墙钟周转，却未产生更接近完整图的共同覆盖机制。

### 4.2 实测计算成本变化（严禁伪造“框架提速倍数”）
- **D12 随余度耗损的真实搜索成本曲线**（`RW/CONTINUATION_COST_JUDGMENT.txt`、`RW/d12_batch02/RESULT.json`）：
  - 大联合 CNF（改表示前）：solver `180.038` CPU 秒 / whole `180.491` CPU 秒 $\to$ `UNKNOWN`（0 图）。
  - 首图探针（`42402 → 42403`）：whole `2.157` CPU 秒 / native `0.067` 秒，`P_tail_checks = 1`，独验 `1.051` CPU 秒。
  - 第一续批（`42403 → 42411`，8 图）：whole `4.671` CPU 秒 / native `2.167` 秒，`P_tail_checks = 1,084`，独验 `1.151` CPU 秒，因 `MAX8_ACCEPTED` 停。
  - `d12_batch01`（`42411 → 42419`，8 图）：whole `6.053` CPU 秒 / native `3.568` 秒，`P_tail_checks = 10,871`（**增约 10 倍**），独验 `1.167` CPU 秒，因 `BATCH_LIMIT_REACHED` 停。
  - `d12_batch02`（`42419 → 42433`，设上限 32 图 / 20 CPU 秒）：实际完成 **14 图**，whole `19.043` CPU 秒 / native `16.538` 秒，`P_tail_checks = 88,500`（**再增约 8 倍**），独验 `1.622` CPU 秒；在搜 `42,434` 时触预算以 `UNKNOWN_WHOLE_CPU_LIMIT_AFTER_ACCEPTED_GRAPH` 停止，父调度主动收束同参收获。
  - **口径纪律**：`180.5s UNKNOWN` 与 `2.16s 命中` 不是受控同算法基准测试，且不含前期建模、失败试错和 LLM 协调时间，绝不能相除宣称“系统提速 80 倍”；相反，`P_tail_checks` 从 `1 → 1,084 → 10,871 → 88,500` 清晰量化了连续增点消耗自由端口后的边际难度上升。
- **D11 转折链的精确算力账**：
  - 固定颜色 1,120 平面空行门 `0.198` s $\to$ 联合改色 SAT（46,249 变量 / 111,376 子句）solver `0.254` s / whole `1.151` s 命中 `plane 605` $\to$ 真实几何绑定累计实测 `10.335` s（保守计 12 s，含两次实现 bug 修复）$\to$ 第一方向 161 根独验及单锚点严格反例 `1.443` s（发现 `(37546,37618)` 距 6 迫使唯一锚点为已满 11 度的 `37618`，见 `ONE_TAIL_NO_WITNESS.json`，**立即停止在固定前部上调尾部**）$\to$ 翻转 4,060 点连通分量方向（相对旧色差异从 `3,955` 降至 `105`）生成 `0.989` s + 独验 `1.048` s（4 对旧外围坏对全修好，仅剩 3 对涉 `z` 坏对）$\to$ 在 2,409 个合法锚点中求精确共同交集得 161 个解（取 `31`），最终生成 `0.732` s + 161 根独验 `0.856` s 通过。

### 4.3 关键人工反馈与 Root 对外部审阅的纠偏
1. **状态漂移修复（最确定的工程缺陷）**：`TRAJECTORY_FEEDBACK_FOR_CODE_AGENT_20261115.txt` 指出，`42403..42411` 已出图后 `ROUTE_REPORT.md` 仍停在早期 split 阶段，`Gemini 036` 甚至建议重开 09:15 已撤下的 `88452` 路线。这直接催生了本地“收件先更新唯一短 `current_context`、再生成下游任务/审阅输入”的修复。
2. **Root 对外部模型过强假设的两次关键驳回**（证明了为何绝不能把审阅意见直接当硬约束）：
   - `WHOLE_REVIEW_20261115_1153_DISPOSITION.txt`：采纳极小 $P$ + 全自由尾部探针，但**驳回** `Gemini 029` 未经验证的 `|P| >= 7` 限制（代码保留 `0..12`）、单平面预选限制（保留全部 754 平面）、60 CPU 秒扩预算建议，以及无冲突分析支撑的“90% 是编码假象”归因。
   - `RW/GEMINI_FLASH_DELTA_DISPOSITION_20261116.txt`：消费路线意见，但**驳回** `Gemini Flash` 提出的“只选 14 个整轨道”（轨道大小 24/48 大于预算 15，若采纳会直接杀光所有非空候选！）及“相同支持直方图蕴含覆盖/LP 等价”的错误推断。

---

## 5. 实际运行的 MathRSI 版本归属与时间线（严防事后因果倒置）

依据 `MATHRSI_VERSION.txt`、`framework_snapshot/development/evolution/main-dd-feedback-20261114/EVOLUTION.md` 与 `dd-workflow-20261115/EVOLUTION.md`，本次运行**既不是旧 `v2`，也不是当前已发布的 `v5`（`80fd0ffcf`）**，而是本地整合工作树 `math-rsi-integrated`（分支 `integrate/main-dd-feedback-20261114`），其精确分期如下：

1. **底盘来源（2026-11-11 `main` 快照）**：来自用户提供的 `math-rsi-main (2).zip`，对应固定 `v4` 标签 + 其后 `main` 上的两项 `v4` 维护（`global-reassessment.md` 全局进展重评 + PR #19 ECC 节点协议）。它**不包含** 2026-11-14 从 Q7 提炼发布的 `v5`（因此 `framework_snapshot` 中完全没有 `actual-input-coverage.md` 及其在 `mathrsi-research` / `mathrsi-route-loop` 中的调用段）。
2. **第一阶段（`42403..42411` 命中时，2026-11-15 13:30 暂停前）**：运行在 `2026-11-11 main` + 2026-11-14 合入的旧本地 `fix/dd-search-feedback`（`residual_cover.py`、`candidate_selection.py`、`search_operations.py` 及 DD 技能搜索反馈段）之上。首图 `42,403` 与前 8 步续接由任务目录内临时 C++ 程序（`minimal_frontier_completion/frontier.cpp`、`d12_blocking_family_continuation/continue.cpp`）完成，**早于** `current_context.py` 与 `d5_blocking_batch.py` 的编写。
3. **第二阶段（2026-11-15 本地工作流维护后，产出 `42412..42433` 与 `37,632`）**：针对专家轨迹评议，新增了 `base/tools/current_context.py`、`current-context.md`、`extension_receipts.py`、`d5_blocking_batch.py/.cpp` 及 `d5-blocking-batches.md`。随后恢复同一 Goal，跑出 `d12_batch01`（`42412..42419`）、`d12_batch02`（`42420..42433`）以及 `h9_n37632`（`37,632`）。
4. **第三阶段（2026-11-16 晚到可靠性补丁与打包适配器——严禁倒果为因）**：
   - 2026-11-16 在 `dd-workflow-20261115/EVOLUTION.md` 后半部追加的多项防呆补丁——包括 `write_current` 自动刷新 `current_context_view`、`in_flight.*.terminal_result` 未消费拦截、已消费收据列表防零新增回退、`stage / search_started` 细化字段、以及 `d5_blocking_batch.py:execute()` 检查计划源是否已被更新前缀取代——**均晚于 `42,433` 和 `37,632` 的首次发现**，属于事后工程加固，不能归因为产生两张新图的原因。
   - 包根 `reproduce.py`、`verify.py`、`check_roots.cpp` 则是 2026-11-16 整理交付包时编写的纯确定性可移植重建与核验脚本，未参与原搜索。

---

## 6. 四项关键接口问题及审阅裁定落盘

1. **D11 核心覆盖与显式源认证桥（已核 `checks/D11_BRIDGE_AUDIT.md`）**：独立窄范围核读支持 §2.2 的显式源认证桥数学结论——特征 3 叉积恒等式、三坐标核单射与 `check.cpp` 对每点实际 `91-star` 的有限检查共同保证构造中间点与共同线均落在字面缓存内，无需另假设抽象 $H(9)$ 的关联直径；F5 运输包含关系由 `reproduce.py:construct_h9`（构造双射 $\sigma$ 与核心边）联合 `checks/REPORT.md` 独立逐边相等比对（及历史 `check_other.py`）共同闭合，不单独归于未重构 $\sigma$ 的 `independent_check.py`，亦不将缺席目录 `route_core.py` 的 `664,272 / 28` 细分计为本轮重放。具体整图 Lean 实例与最终外审仍保持开放。
2. **专用工具入 `plugins/degree-diameter/tools/` 的职责理由（已对齐）**：`archive/` 保存不可变原始历史原件，无法承载路径修复与收件守卫；将修正后的 `d5_blocking_batch.py/.cpp` 与 `extension_receipts.py` 放入 `plugins/degree-diameter/tools/`（显式钉死 `d12_754_planes_core41356` 家族门与原逐点保边收据格式，拒绝不匹配 family），可配合 455 文件归档内保留的 `RAW_PLANES_ACTUAL_IDS.txt` 直接服务真实的家族有界续接，既不篡改归档也不冒充任意 $D=5$ 通用框架。Base 侧保留迁出 DD 计数并修复相对路径后的可选 `base/tools/current_context.py`。
3. **`framework_snapshot` 技能死链与 `v5` 合并红线（已裁定）**：`framework_snapshot` 中 DD 技能引用的 `search-feedback.md / candidate_selection.py / search_operations.py` 未随 455 文件包附带且不在 `v5` 仓内，不拷入这些悬空脚本引用；Base 与 DD 技能均在当前 `v5` 上增量修改，完整保留 `v5` 的 Q7 `actual-input-coverage.md` 段落。
4. **归档位置与全局目录数口径（已裁定）**：全量 **455** 个原件（含两张最终图与便携复验脚本）已完整归档于 `plugins/degree-diameter/archive/dd-latest-two-parameters-20261116/`，无需裁剪或追加哈希。源报告中的 `195/44/49` 仅记为源运行报告口径，未复审全集前不向公开主页扩报。
