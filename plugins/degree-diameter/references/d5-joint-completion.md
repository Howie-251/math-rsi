# $D=5$ 极小平面阻塞补全、部分折叠改色与有界批次核验

本参考供 [mathrsi-degree-diameter](../skills/mathrsi-degree-diameter/SKILL.md)、[dd-construction](../skills/dd-construction/SKILL.md)、[dd-transfer-diagnosis](../skills/dd-transfer-diagnosis/SKILL.md) 与 [dd-obstruction-certificate](../skills/dd-obstruction-certificate/SKILL.md) 在推进直径 $D=5$ 图构造、跨源迁移与点对覆盖验收时调用。方法与实证来自 `(12,5)` 的 `42,402 → 42,433`（31 个保边前缀）与 `(11,5)` 的 `37,631 → 37,632`（核心联合改色与换向修路）；完整只读原件与便携复验器位于 [dd-latest-two-parameters-20261116](../archive/dd-latest-two-parameters-20261116/README.txt)。

---

## 1. 保边扩张：极小核心平面阻塞集 $P$ + 全自由域尾部补全 $T$ 与折叠端口成本

### 何时使用与输入契约
- **适用条件**：当前完整简单无向图 $G$ 已满足最大度 $\le \Delta$、直径 $\le 5$；自由点集 $F = \{v \in V(G) : \deg_G(v) < \Delta\}$ 非空，且全自由点四步闭球并 $\bigcup_{v \in F} B_4^G(v) = V(G)$（若有任一目标点未被全 $F$ 四步到达，固定该 $G$ 的一切单新点保边扩张立即无解，直接返回漏点见证退出）。
- **几何核心接口**：$V(G)$ 划分为已绑定真实 $H(9)$ 部分折叠映射 $\pi: P_{\text{raw}} \to V_{\text{core}}$ 的核心 $V_{\text{core}}$，以及外围 $V_{\text{ext}} = V(G) \setminus V_{\text{core}}$（必须包含原作者附加点与此前已插入的全部新顶点）。

### 数学分解与真实端口计费（避免模板与配额误限）
1. **核心四步充分门只看 91 线命中**：设 $\Pi \cong PG(2,9)$ 为 $Q(6,9)$ 上的真实全奇异射影平面（含 91 条射影线）。对任意核心原点 $p$，极化线性形式 $x \mapsto \beta(p,x)$ 在 $\Pi$ 上的零集至少含一条线；只要所选核心端口集 $P \subseteq F \cap V_{\text{core}}$ 在 $\Pi$ 中的原像命中全部 91 条线，即存在选中原像 $x$ 使 $\beta(p,x)=0$，在 $H(9)$ 关联图中给出 $\le 4$ 步偶路径，经点线配对 $\sigma$ 与折叠 $\pi$ 投影不增距，从而 $\bigcup_{u \in P} B_4^G(u) \supseteq V_{\text{core}}$。
2. **证书域内的无损分解**：任何拥有平面 $\Pi$ 阻塞证书的合法邻集 $S \subseteq F$（$|S| \le \Delta$），必包含一个**包含极小（inclusion-minimal）**91 线命中子集 $P$；剩余 $T = S \setminus P$（$|T| \le \Delta - |P|$）可从**当前全部其余自由点 $F \setminus P$**（允许继续选 $\Pi$ 内未入 $P$ 的自由点）中共同选取，覆盖外围残余目标 $R = V_{\text{ext}} \setminus \bigcup_{u \in P} B_4^G(u)$。
   - **禁止强加的历史习惯**：不限制在旧 85 个 Rédei-15 模板或 702 轨道，不预设 `10+2` / `11+1` 固定配额，也不添加未经证明的 $|P|\ge 7$ 下界。同时，该平面证书是充分生成域而非全图必要条件：754 张平面全部穷尽只关闭该平面证书域，不能宣称任意 $G+z$ 不存在。
3. **按折叠后实际端口数 $|\pi(B)|$ 计费（而非 raw 点数 $|B|$）**：
   - 多个 raw 原点映到同一核心顶点只消耗新点 `1` 个度数预算。在 Frobenius 稳定且所用共轭对均未 split 的已绑定情形下，$f$ 个 $\mathbb{F}_3$-固定点与 $p$ 个二点共轭对共有 $|B| = f + 2p$ 个 raw 点，但实际端口数仅为 $|P| = f + p$。
   - **实证对照（`(12,5)` 系列）**：首图 `42,403` 在 `plane 340` 取 `17` 个 raw 点（5 固定 + 6 对）占 `11` 个核心端口，由单一外围守卫 `41421` 一次补齐全部 11 个外围缺口（`11+1`）；后续 `42,407`、`42,408` 取 **`18` 个 raw 点（2 固定 + 8 对）反而仅占 `10` 个核心端口**，留出 2 个外围槽位（`10+2`）；另有 `18` 个 raw 点（6 固定 + 6 对）占 `12` 个端口且自身已覆满外围（`12+0`）。生成排序必须按实际可用 pin 数与 $|\pi(B)|$ 评估，绝不能机械最小化 $|B|$。

### 返回与验收契约
- 每次插入 $z_i$ 后，下一步必须在**更新后的完整图 $G_{i+1}$** 上重算自由度与外围（含 $z_i$）的四步 provider。
- **全点对覆盖（二选一均严格完备，无需重跑源图全部旧根）**：
  - *逐前缀归纳*：已接受源 $G_0$ 满足 $D\le 5$ + 每步零删旧边、全点度数 $\le \Delta$ + 每步在 $G_{i+1}$ 上对新根 $z_i$ 运行完整 BFS 达全图偏心率 $\le 5$（证明整串中间图均合法）；
  - *终图直接覆盖*：核验 $E(G_0) \subseteq E(G_k)$、简单性与最大度 $\le \Delta$，并在**最终图 $G_k$ 上对全部 $k$ 个新增顶点运行完整 BFS**（如 `42,433` 图只需跑 `42402..42432` 共 `31` 个根，`0.06` CPU 秒即可覆盖一切含新点的点对，旧—旧点对由 $G_0$ 保边单调继承）。配合 Moore 界 $M(12,4)=17,569 < 42,433$ 得精确直径 `5`。

---

## 2. 核心改边与恢复：H(9) 部分折叠联合改色、反例撤回前部、分量换向与混合点对覆盖

### 何时触发
当固定源图的现有颜色使所有已知几何平面的某些射影线失去自由度 provider（例如 `(11,5)` 的 `37,631` 源在全部 `1,120` 张 $\mathbb{F}_3$ 全奇异平面上均出现空行，耗时仅 `0.20` CPU 秒即可完整确诊），纯保边平面阻塞路线为空，但源核心来自 $H(9)$ 四阶对偶 $\tau$（$\varphi = \tau^2$）的部分折叠 $G(S,c)$ 时启用。

### 四步可执行工作流与实证转折（`(11,5) 37,631 → 37,632`）

1. **联合求解颜色与核心阻塞端口 `(c, P)`**：
   - 保持固定的 split 纤维集 $S$（`|S|=4,074`，从而合并映射 $\pi: P_{\text{raw}} \to \{0,\dots,37470\}$ 固定不变），将每个 $f \in S$ 的颜色变量 $c(f) \in \{0,1\}$、全奇异平面选择及 91 线命中端口 $P$、连同保留旧外围关联边（`1,608` 条）后的全图度数上限 $\le 11$ 放入同一必要+核心充分模型。
   - **依据**：极化零点偶路径转换 $\beta(p,x)=0 \implies \text{dist}_H(p,x)\le 4 \implies \text{dist}_{G_{\sigma_c}}(p,x)\le 4$ 对**任意**点线双射 $\sigma_c$ 成立，无需固定旧颜色。实测单次 SAT（`0.25` solver CPU 秒）给出 `plane 605` 的 `10` 个核心端口与合法颜色，留 `1` 个新点尾部槽位。
2. **用单槽严格反例立即撤回固定前部（禁止围着坏对总数空转调尾）**：
   - 按真实 $H(9)$ 关联表、$\tau$、$\sigma_c$ 与 $\pi$ 重建 `37,471` 点核心并接上 `160` 个旧外围点及 `10`-pin 新点 $z$ 得候选 $G_0$。因核心改边（如删旧边、加新边），**旧外围点之间的最短路不再自动保持**，必须检查全部 `160` 个旧外围根 + 新根 $z$（共 `161` 根）。
   - 若剩 `1` 条允许新边 $z\text{–}a$（$a \in F \setminus P$），加边后任意点对距离精确等于
     $$d_{G_0 + za}(u,v) = \min\bigl(d_0(u,v),\; d_0(u,z)+1+d_0(a,v),\; d_0(u,a)+1+d_0(z,v)\bigr).$$
   - **快速否证判据**：若存在任何坏对 $(u,v)$（$d_0(u,v) > 5$）满足 $d_0(u,z)\ge 5$ 且 $d_0(v,z)\ge 5$，或满足上述 $\le 5$ 不等式的唯一旧顶点 $a$ 已满度，则固定当前 $(c,P)$ 的**一切单边尾部补全严格无解**。
   - **真实案例**：首方向候选经 161 根检查暴露出 `7` 对距离 6 坏对，其中旧外围对 `(37546, 37618)` 满足 $d_0(u,z)=4, d_0(v,z)=5$，唯一能缩短该对的锚点 `a = 37618` 度数已满 `11`。据此在 `0.21` CPU 秒内严格关闭该前部方向，立即停止调尾。
3. **连通分量整体补色换向（保度数与核心证书、修复旧外围路径）**：
   - 由 Rajiv Lemma 4.1 / Theorem 5.1，顶点度数仅取决于相邻 split fibers 是同色（$K_{2,2}$）还是异色（完美匹配 $2K_2$）。因此在 split 纤维相邻图的任一连通分量上将 $c$ 整体取反 $c \mapsto 1-c$，**全图每点度数与核心 91 线四步证书严格不变**，但异色对之间的完美匹配方向反转。
   - **选向准则**：优先尝试与已合法源图真实颜色汉明距离较小的分量方向，再核实际边与距离；较小色差是选向线索，不是最大保边或保距定理。在 `37,632` 中，对唯一的 `4,060` 点连通分量整体补色（14 个孤立点取旧色），使相对 `37,631` 源的改色 fiber 数从 `3,955` 降至 **`105`**（核心删 `186` 边、增 `212` 边），实测修好全部 `4` 对旧外围坏对，仅剩 `3` 对涉及新点 $z$ 的距离 6 点对。
4. **全体剩余坏对的精确共同锚点交集**：
   - 对剩余涉 $z$（或外围）坏对，直接对每个坏对允许的合法锚点集 $\{a \in F\setminus P : \min(d_0(u,z)+1+d_0(a,v), d_0(u,a)+1+d_0(z,v)) \le 5\}$ 求交集。`37,632` 实例在 `2,409` 个余度候选点上求交得到 `161` 个共同合法锚点，取最小编号 `31`，加边 `(31, 37631)` 后 161 根复核 `0` 坏对闭合。

### 混合全点对覆盖契约（供 `dd-obstruction-certificate` 核验）
当核心发生改边而外围边不变时，完整点对证明由以下两块严丝合缝拼成（**不是抽样**）：
1. **`Core × Core`（`0..37470`）**：由真实 $H(9)$ 关联结构（点线关联直径 $\le 6$）上任意点线双射 $\sigma$ 的奇关联路径转换（$p - L_1 - a - L_2 - b - \sigma(q) \mapsto p - \sigma^{-1}(L_1) - a - \sigma^{-1}(L_2) - b - q$，删相邻停留，Rajiv Lemma 3.1）加折叠映射 $\pi$ 不增距给出，并用独立绑定程序核验 $\sigma$ 双射、fiber 颜色常值及由字面 `lines / sigma / pi` 生成的核心边与最终图核心子图逐边相等（`203,747` 条边）。*（归档内另有基于特征 3 叉积恒等式与字面 91-star / 729 核向量满射的显式源路由推导备查。）*
2. **`Core × Exterior` 与 `Exterior × Exterior`（一切至少含一个非核心点 `37471..37631` 的点对）**：在最终图字面边表上对全部 `160` 个旧外围点与新点 `37631`（共 **`161` 个根**）执行完整全图 BFS，确认 `visited = 37,632` 且偏心率 $\le 5$；再由 Moore 界 $M(11,4)=12,222 < 37,632$ 定出直径恰为 `5`。

---

## 3. 有界批次终止语义、已刷出前缀回收与家族级共享 Lean 边界

- **终止状态严格区分**：
  - `BATCH_LIMIT_REACHED`：达到调用者设定的本批实例上限 `max_new`，**绝不表示机制耗尽**；父调度按边际成本（如 `(12,5)` 连续四批 `P_tail_checks` 从 `1 → 1,084 → 10,871 → 88,500` 递增）在续派下一有界批与转攻新参数间抉择，不设自动无限循环。
  - `UNKNOWN_*_AFTER_ACCEPTED_GRAPH` / `UNKNOWN_*`：触及单批 CPU 或墙钟上限（如 `d12_batch02` 完成 14 个前缀达 `42,433` 后在搜 `42,434` 时触 20s CPU 上限）；**已完整刷出并通过独立核验的前缀照常验收保留**，未完成的下一步记 `UNKNOWN`，既不算成功也不算不存在性证明；半行截断 JSON 不计作候选。
  - `COMPLETE_NO_IN_CURRENT754_SUFFICIENT_PLANE_DOMAIN`：仅关闭当前图在此 754 平面充分证书域内的单步扩张，不排除全图空间。
- **家族级共享形式化缺口集中记账**：
  - 通用条件定理（如 `SingleExtension.lean` 的 `singleVertexExtension_diameterAtMostFive_of_parentDepth`，或特征 3 代数/核上界模块 `H9CrossRouting / Geometry / Kernel / Star.lean`）通过内核检查，**不等于具体源图（如 `42342/42402` 的 $D\le 5$ 或 `Fin 37632` 的有限表/外围证书）已完成具体图 Lean 认证**。
  - 将缺失的具体源图定理与有限证书绑定列为**该家族共用的单一待办认证项**；在共享源前提闭合前，禁止为每个新增 `+1` 前缀重复编译带相同未闭假设的 wrapper，也不把编译器崩溃（如 GPFS 上 `SIGSEGV`）或配额中断改写成数学反例或已认证计数。

---

## 4. 随仓工具与便携复验调用契约

### 4.1 便携确定性构造与完整指定根核验（适用于两张最终图）
无需求解器或原机器路径（`verify.py` 需 `g++` C++17），输出写入当前任务临时目录，保持插件归档只读：

```bash
ARCHIVE="/path/to/MathRSI/plugins/degree-diameter/archive/dd-latest-two-parameters-20261116"
OUT="/task/dd-verify-out"
python3 "$ARCHIVE/reproduce.py" --compare --output-dir "$OUT/reconstructed"
python3 "$ARCHIVE/verify.py" --output-dir "$OUT/verified"
```

- **输入与返回**：从 `ARCHIVE/inputs/` 重建 `37,632` 与 `42,433` 边表，与 `ARCHIVE/graphs/` 逐边集合比对一致，并执行 `161` 根（D11）与 `31` 根（D12）完整 BFS（合计约 3 秒墙钟），写出 `CHECK_RESULT.json`。

### 4.2 逐前缀保边收据消费与 `(12,5)` 专用有界续批工具
完整初始化字段、原平面数据位置、源 checkpoint 绑定与终止语义见[有界批次与收件](d5-blocking-batches.md)。
当持续任务启用了 [current-context 契约](../../../base/skills/mathrsi-research/references/current-context.md) 且 `STATE.json` 含 DD 家族状态时，可调用以下两个薄工具（均位于 `plugins/degree-diameter/tools/`）：

1. **消费已核验的逐前缀收据**：[extension_receipts.py](../tools/extension_receipts.py)
   - **Caller 与前提**：父调度已审阅作者 `RESULT.json` 与独立前缀检查器 `independent/RESULT.json`（`status == "PASS"`）。
   - **校验与写回**：核对源图 `(n, m)` 及对应已接受源证据绑定、每步度数/简单性/零删旧边/当步新根完整 BFS 与终图逐边 `MATCH`，幂等合并 `accepted_orders` 并更新 `current_context`（重读旧收据不会抹去同图后续产生的零新增 `UNKNOWN` / `No` 停止记录）。它不重跑 BFS，也不自动认证源 Lean。
   ```bash
   python3 /path/to/MathRSI/plugins/degree-diameter/tools/extension_receipts.py \
     --state /task/STATE.json --family 12,5 \
     --author /task/batch/RESULT.json --independent /task/batch/independent/RESULT.json \
     --acceptance-basis "父调度已核全部前缀独验、保边及终图逐边一致；42402源D5沿用；具体源Lean仍开"
   ```
2. **`(12,5)` 绑定平面域专用有界批次驱动**：[d5_blocking_batch.py](../tools/d5_blocking_batch.py)（配 [d5_blocking_batch.cpp](../tools/d5_blocking_batch.cpp)）
   - **严格适用范围**：**仅限已绑定的 `(12,5)`、`core < 41356`、原始 `754` 张实际平面 ID 输入（`RAW_PLANES_ACTUAL_IDS.txt`）家族**；切勿将其当作任意度数或任意 $D=5$ 源图的通用搜索器。需要 POSIX 环境与 `g++`。
   - **安全门与返回**：`--plan-only` 只读核对最新已接受前缀文件头（相对 `edge_file` 按 `STATE.json` 所在目录解析），不建目录、不搜索；实际运行要求 `STATE.status == "ACTIVE"`、无未消费 `terminal_result`、且计划源仍为当前最新已接受阶数。输出标记 `independent_validation: "PENDING"`，须交独立前缀核验通过后再由 `extension_receipts.py` 收件。
   ```bash
   python3 /path/to/MathRSI/plugins/degree-diameter/tools/d5_blocking_batch.py \
     --state /task/STATE.json --planes /task/RAW_PLANES_ACTUAL_IDS.txt \
     --output /task/d12_next_batch --max-new 8 --cpu-limit 20 --wall-limit 480 --plan-only
   ```
