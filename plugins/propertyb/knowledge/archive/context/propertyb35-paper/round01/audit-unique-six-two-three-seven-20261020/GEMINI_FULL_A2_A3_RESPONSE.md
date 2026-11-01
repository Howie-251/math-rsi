### 总体审阅判定

- **判定结论**：**通过（`SOUND_MODULO_DECLARED_IMPORTS`）**。在明确声明的既有局部证书进口下，目标定理——**“21点、35条互异五元边、点对覆盖、最小度6、唯一六度点 $x$，且恰有 $a \in \{2,3\}$ 个七度点的超图 $H$ 具有 Property B”**——的纸面证明与有限域计算逻辑完整闭合，未发现数学漏洞、循环论证、集合漏项或不等式方向错误。
- **范围边界**：本结论仅限上述 21 点唯一六度、恰 2 或 3 名七度点（A2/A3）分支，不扩展至全 21 点或完整 $m(5) \ge 36$；不依赖旧 `T33/T34` 边临界性、$\Delta(\Gamma) \le 29$、threshold 图递归 $T(n,m,r)$ 或 degree-prefix DP。
- **静态核对与程序执行声明**：
  - **静态数学与代码核对**：已独立完成下述全部主链证明文本、公式推导、源码逻辑及 JSON 证书结构的静态核对。
  - **程序重跑状态**：**未执行任何程序或 Shell 命令（只读静态审阅，无命令执行）**。各 JSON 回执仅作为静态检查对象，不声称本次重新运行了脚本。

---

### 一、实际阅读范围回执（全文核对 vs 接口核对）

#### 1. 本次全文阅读并逐节核对的文件（U01–U16 及核心支撑证明）
- **U01 主稿**：[TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN.md)（全文 1–175 行，§1–9）
- **U02 $\Gamma\min 4$ 证明**：[TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN_MINIMUM_NONUNIT_DEGREE_FOUR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN_MINIMUM_NONUNIT_DEGREE_FOUR.md)（全文 1–311 行，§1–8）
- **U03 $q_4$ 低中心门报告**：[REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/REPORT.md)（全文 1–89 行）
- **U04 新 $c_{14} \to \text{cap } 13$ 证明**：[PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md)（全文 1–86 行）
- **U05 强共度归约报告**：[REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_high_degree_pair_gates_20261020/REPORT.md)（全文 1–131 行）及源码 [VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_high_degree_pair_gates_20261020/VERIFY.py)、[ACTUAL_A3_TRIPLES.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_high_degree_pair_gates_20261020/ACTUAL_A3_TRIPLES.py)、[ACTUAL_A3_TAIL.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_high_degree_pair_gates_20261020/ACTUAL_A3_TAIL.py)
- **U06 三重四核与 $n_4 \le 13$ 证明**：[PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_quad_core_multiplicity_three_20261020/PROOF.md)（全文 1–134 行，含 §4 共同 $x$-star 与 §7 $n_4 \le 13$）
- **U07 任意六度星平衡计数证明**：[PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_degree_six_star_count_20261020/PROOF.md)（全文 1–116 行）
- **U08 度敏感共同 middle 容量引理**：[CAPACITY_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_joint_moment_frontier_20261020/CAPACITY_LEMMAS.md)（全文 1–63 行）
- **U09 共同 middle 恒等式**：[GLOBAL_TWO_FLIP_SHARED_MIDDLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md)（全文 1–196 行；主链仅用 §1–2 精确恒等式与 $f(s)$ 差分凸性）
- **U10 全局两翻路径修复**：[GLOBAL_TWO_FLIP_PATH_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md)（全文 1–288 行）
- **U11 全局单翻私有对修复**：[GLOBAL_PRIVATE_PAIR_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_PRIVATE_PAIR_REPAIR.md)（全文 1–158 行）
- **U12 六单位八度池定理**：[SIX_UNIT8_POOL_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md)（全文 1–95 行）
- **U13 两个 `NO_CRITICAL` 算法与输出**：[NO_CRITICAL_FILTER.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_FILTER.py)（全文 1–73 行）、[NO_CRITICAL_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_CHECK.py)（全文 1–84 行）、[CHECK_ASSEMBLY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/CHECK_ASSEMBLY.py)（全文 1–20 行）、[NO_CRITICAL_SURVIVORS33.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_SURVIVORS33.json)（全文 1–1166 行）、[NO_CRITICAL_CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_CHECK.json)（全文 1–642 行）、[ASSEMBLY_CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/ASSEMBLY_CHECK.json)（全文 1–20 行）
- **U14 $q=3$ 组装验证脚本**：[VERIFY_ASSEMBLY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/three_nonunit_direct_repair_20261020/VERIFY_ASSEMBLY.py)（全文 1–87 行）
- **U15 $q=4$ 低中心验证脚本**：[VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/VERIFY.py)（全文 1–76 行）、[INDEPENDENT_VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/INDEPENDENT_VERIFY.py)（全文 1–69 行）、[FIVE_LOCK_FULL5.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/FIVE_LOCK_FULL5.py)（全文 1–47 行）
- **U16 $c_{14}$ 验证脚本**：[VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/VERIFY.py)（全文 1–50 行）
- **额外全文阅读的声明进口证明与核心算术库**：
  - 通用 $q_\Gamma(F) \le 2$ 定理：[TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md)（全文 1–206 行）
  - 条件排列概率引理：[PROBABILITY_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md)（全文 1–370 行）
  - 无放回注入概率实现：[independent_structure_bounds.py](file:///Users/rfy_naiveai/Desktop/aris4math/computations/independent_structure_bounds.py)（全文 1–195 行）
  - 旧 $t \in \{15,16\}$ 饱和门证明：[PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_c3_high_degree_saturation_20261020/PROOF.md)（全文 1–107 行）
  - 一般删星森林秩 $\ge 11$ 证明：[TWENTYONE_A1_BALANCED_STAR_FOREST.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md)（全文 1–238 行，主链仅调用 §3–5 通用秩引理与 Hunter 树不等式）
  - 低度强点对与 `677` 接口背景：[REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_edge_intersection_repair_20261020/REPORT.md)（全文 1–147 行）、[REDUCTIONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/REDUCTIONS.md)（全文 1–97 行）

#### 2. 仅作接口核对（未全文逐行读完底层大型 JSON/旧脚本）的进口项
- `U12` 所引用的 `unique6_no7/UNIQUE6_NO7_PROOF.md` 及其底层 26 个五邻点残轨道/三份六邻点严格证书（已在 `U12` 的静态源码核查表中核对其调用前提不含自由点度数或无七度点假设，未重读 `unique6_no7` 原文及 `FIVE_DOMAIN.json` 全文）。
- `U05` 所引用的 `DOUBLES.json`（仅读前 200 行及生成脚本 [initial_pilot.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/initial_pilot.py)、回执 [FIXED_REPLAY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/FIXED_REPLAY.json)，确认覆盖 $d_1 \in \{6,7,8\}, d_2 \ge d_1, \lambda \ge 5$）及 $(9,9)$ 五份双锁固定证书。
- `U04`、`U06`、`U02`、`U03` 的发现端脚本（`PILOT.py` 等）及大型证书 JSON（如 `FIVE_LOCK_FULL83.json`、`SIX_LOCK_COMMON_STAR47.json`、`FULL_RESULT.json`、`DOMAIN.json`）：已通过阅读各自的验证脚本（`U14`、`U15`、`U16`）确认其域重建与固定证书重放逻辑，未全文读取大型 JSON 数据体。

---

### 二、八项对抗攻击点的逐项数学核查

#### 1. 定理假设到 $a, b, e$、角色及完整 16 度谱的推导（无隐藏前提）
- **推导核验**：设非 B 超图 $H$ 有唯一六度点 $x$、$a \in \{2,3\}$ 个七度点、$b$ 个八度点，其余 $h = 20 - a - b$ 个点度 $\ge 9$。由 $\sum_{v \in V} d(v) = 35 \times 5 = 175$ 得
  $$6 + 7a + 8b + 9(20 - a - b) + e = 175 \iff e := \sum_{v \in V} \max(d(v)-9, 0) = 2a + b - 11 \ge 0.$$
  由点对覆盖，$\lambda(x, v) \ge 1$（$\forall v \ne x$），且 $\sum_{v \ne x} (\lambda(x, v) - 1) = 4 d(x) - 20 = 4$。若 $r$ 名七度点与 $x$ 共度 $\ge 2$，它们至少消耗 $r$ 份行盈余，故八度点中至多 $4 - r$ 名与 $x$ 共度 $\ge 2$，至少 $b - (4 - r)$ 名八度点与 $x$ 共度为 1。
- **调用 `U12` 的合法性**：[SIX_UNIT8_POOL_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md) 仅要求 $n=21, M=35$、简单五元、点对覆盖、$\deg(x)=6$ 且存在 6 名与 $x$ 共度 1 的八度点。非 B 迫使 $b - 4 + r \le 5 \implies 11 - 2a \le b \le 9 - r \le 9$，从而 $e \le 2a - 2 - r \le 4$。
- **16 度谱无遗漏**：因为 $h = 20 - a - b \ge 20 - 3 - 9 = 8 \ge 4 \ge e$，$e$ 的任意整数分拆均可填入 $h$ 个 $\ge 9$ 度点中。对 $r \ge 0$ 取并集（即遍历全部 $11 - 2a \le b \le 9$），A2（$a=2, e \in \{0,1,2\}$）恰有 $1+1+2=4$ 谱，A3（$a=3, e \in \{0,1,2,3,4\}$）恰有 $1+1+2+3+5=12$ 谱，共 16 谱。全过程未使用 `T34` 临界性或 $q_\Gamma(F) \le 29$。

#### 2. $\Gamma\min 4$（`U02`）：实际 $F \to 91\text{ 轨} \to 83\text{ 键} \to 4\text{ 尾} \to 47\text{ 共同 }x\text{-star}$ 的无损性
- **$q_\Gamma(F) \le 2$ 排除**：由 [TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md) 直接给出，该定理对任意 21/22 点 35 边简单五元超图成立，无需点对覆盖或度数假设。
- **$q_\Gamma(F) = 3 \to 91\text{ 轨} \to 83\text{ 键}$**：
  - $F$ 上的允许异常迹（大小 $\in \{0,2,3,4\}$）共 $1+10+10+5=26$ 个，无序可重复三元组共 $\binom{28}{3}=3276$ 个，在 $F$ 顶点的 $S_5$ 重标号下分为 91 个不相交轨道（由 [VERIFY_ASSEMBLY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/three_nonunit_direct_repair_20261020/VERIFY_ASSEMBLY.py#L21-L26) 独立展开验证）。
  - 其余 31 条原边与 $F$ 恰交一点，附着向量 $\vec{a}$ 满足 $\sum_{v \in F} a_v = 31$。在每個轨道代表上完整检查所有满足 $\sum a_v = 31$ 的非负整数向量（不对 $\vec{a}$ 作稳定子约化），随后加上实际度条件 $d_v = 1 + a_v + h_v \ge 6$、$\#\{v \in F : d_v = 6\} \le 1$ 及 $\sum_{v \in F} \max(d_v - 9, 0) \le e \le 4$，精确得到 83 个必要键。
  - 79 个键由固定 16 布局菜单的零配额五锁证书严格排除（最大界 $139/143 < 1$），仅余 A、B、C、D 四键。
- **四尾到 47 个共同 $x$-star 六锁键（含 C-A2 核查）**：
  - A、B、C、D 中 $F$ 各点度数均 $\ge 7$，故唯一六度点 $x \notin F$；且三条例外迹均非空，故过 $x$ 的 6 条原边全部与 $F$ 相交。
  - 每个非空例外迹大小 $\in \{3,4\}$，若作为 $x$ 边会在 $F$ 上消耗 $|T|-1 \in \{2,3\}$ 份 $x$ 行共度盈余（连同其余 5 条 $x$ 边在 $F$ 上的盈余，选一个三迹至少使 $F$ 上 $x$ 行盈余为 $3+5-5=3$，选一个四迹为 $4$，选两个多迹 $\ge 5 > 4$ 不可能）。
  - **C-A2 核查**：在 C 中，$F$ 度数为 $(8,10,10,9,9)$，局部高点盈余为 $2$，$F$ 内仅有 $v_0$ 一个八度点。若 C 处于 A2（$a=2$），则 $e=2, b=9$；由六 unit8 池定理，至少 $9-5=4$ 名八度点与 $x$ 非单位，其中至少 3 名在 $F$ 外，消耗至少 3 份 $x$ 行盈余，留给 $F$ 的 $x$ 行盈余至多 $4-3=1$。因此 C 在 A2 下不仅不能选多迹，而且 6 条单迹 $x$ 边在 $F$ 上的唯一加倍点只能是 $v_0$，得到的唯一键已包含在 C 的 5 个全单迹键（从而包含在 C 的 35 键）之中，**无 C-A2 遗漏**。
  - 47 个六锁输入均从同一个实际 $x$-star 拆出（$\nu_{2m} = \mu_m - c_m, \nu_{2m+1} = c_m, \sum c_m = 6$），且全部使用**零配额**证书（最大界 $428/429 < 1$），不存在共同星不相容或重复扣除。

#### 3. 固定锁点排列界与原 $H$ 染色、$S_5/S_4$ 运输、无放回分母及 1190 有序异边对
- **指向原 $H$ 染色**：由 [PROBABILITY_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md) §P1–P7，对原超图 $H$ 固定 $s$ 个锁点位置并均匀排列其余 $N = 21 - s$ 个自由点，贪心染色失败事件包含于 $\bigcup_{k=1}^{21} Q_k$，且 $\Pr(Q_k) \le \min(A_k, B_k, C_k - \ell_k)$。只要总和 $<1$，必存在一条排列使贪心输出为原 $H$ 的合法二染色。
- **运输一致性**：无论是 `U02` 的 $S_5$、`U03` 固定 $x=0$ 的 $S_4$、还是 `U04` 保持侧集 $\{A,B\}$ 的 8 阶群，群作用均只是对原 $H$ 已选锁点的重命名：代表元上的迹重数、附着数 $\vec{a}$、度数向量与锁点位置通过逆置换 $\pi^{-1}$ 同步搬回原 $H$ 的实际顶点，不要求 $H$ 具有自同构。
- **无放回分母与 1190 有序对**：在 [independent_structure_bounds.py](file:///Users/rfy_naiveai/Desktop/aris4math/computations/independent_structure_bounds.py#L50-L128) 中：
  - 自由中心 $k$：单边端点权重为 $r (a)_{r-1} / (N)_r$；有序边对权重为 $(a)_{r-1}(b)_{q-1} / (N)_{r+q-1}$（公共交点唯一确定，无 $rq$ 因子；当 $r+q-1 > N$ 时为 0）。
  - 锁定中心 $k$：单边端点权重为 $(a)_r / (N)_r$；有序边对权重为 $(a)_r (b)_q / (N)_{r+q}$（当 $r+q > N$ 时为 0）。
  - 每次复算均将库存展开为 35 个带独立索引的原边 stub，遍历 $35 \times 34 = 1190$ 个有序异边对 $(i \ne j)$，与按类型聚合的 $\mu_T(\mu_U - \mathbf{1}_{T=U})$ 完全等价。

#### 4. $c_{14}$ 门（`U04`）：cross 库存作为 valid middle 上界，以及 $c=14, t \ge 15$ 时调用旧接口的合法性
- **单向包含方向正确**：对 $|G \cap J| = 3$，令 $A = G \setminus J = \{0,1\}, B = J \setminus G = \{2,3\}, K = A \cup B$。任何满足 $F \cap G = \{g\}, F \cap J = \{j\}, g \ne j$ 的 valid middle 边 $F$ 必避开 $G \cap J$，故其精确 $K$-迹必属于四个 cross pair $\{5,6,9,10\}$ 之一；反之，精确 $K$-迹为 cross pair 的原边还可能交 $G \cap J$。因此
  $$t := \mu_5 + \mu_6 + \mu_9 + \mu_{10} \ge c(G, J) \ge 14.$$
- **$c(G,J)=14$ 但 $t \in \{15,16\}$ 时调用旧饱和门的合法性**：核查 [generic_c3_high_degree_saturation_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_c3_high_degree_saturation_20261020/PROOF.md) 全文（§"Actual H to the complete small domain" 第 36–68 行），该定理仅在四锁集合 $K = A \cup B$ 上建立精确迹库存，其域生成与 183 份**零配额**固定证书**只使用 $t = \mu_5 + \mu_6 + \mu_9 + \mu_{10} \in \{15,16\}$、$\mu_3 \ge 1, \mu_{12} \ge 1$、$K$ 内六点对 $\lambda \le 4$ 及 $\sum_{v \in K} \max(d_H(v)-9,0) \le 4$**，从未要求这 $t$ 条边避开 $G \cap J$。因此当 $c(G,J) = 14$ 而 $t \in \{15,16\}$ 时，直接落入该已证域并获得原 $H$ 染色；余下 $t = 14$ 由 `U04` 的 7812 标签 / 1144 代表零配额证书（最大界 $34904/36465 < 1$）闭合。故非 B 下必有 $C_3 \le 13 n_3$。

#### 5. $q_4$ 低中心门（`U03`）与 $\Gamma\min 4$ 的无循环性及 A3 前提对齐
- **无循环性**：`U02` 证明 $\delta(\Gamma) \ge 4$ 仅依赖 `U12`（六 unit8 池）与通用 $q \le 2$ 定理，不依赖 `U03` 或 `U05`。`U03` 仅针对单条过 $x$ 的边 $F$ 假设 $q_\Gamma(F) = 4$（即恰有 4 条其他边与 $F$ 交集大小 $\ne 1$，其余 30 条与 $F$ 恰交一点），完全不要求 $\Gamma$ 的其他顶点度 $\ge 4$。
- **前提对齐**：在同一个非 B 的 A3（或 A2）超图 $H$ 中，对任意过唯一六度点 $x$ 的原边 $F$：
  1. $F \setminus \{x\}$ 各点度 $\ge 7$，七度点数 $\le a \le 3$，且 $\sum_{v \in F} \max(d(v)-9,0) \le e \le 4$（由 §1）；
  2. $F$ 内 10 个点对的原共度 $\le 4$，故在 4 条例外迹中每对至多出现 $4-1=3$ 次（由 `U05` 强共度门）；
  3. 过 $x$ 的 6 条边覆盖其余 20 点，总重复成本为 4，故含 $x$ 的例外迹满足 $\sum_{T \ni x} (|T|-1) \le 4$；
  4. $a_0 = d(x) - 1 - h_0 = 5 - h_0$。
  [VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/VERIFY.py) 与 [INDEPENDENT_VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/INDEPENDENT_VERIFY.py) 在全部 $\binom{29}{4} = 23,751$ 个带标号四异常迹多重集（1563 个固定 $x$ 的 $S_4$ 轨道）上保留每个锚点的完整失败集（未将阈值当作单调尾），筛选后仅余 40 个带标号输入 / 5 个联合轨道，再由 [FIVE_LOCK_FULL5.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/FIVE_LOCK_FULL5.py) 以零配额固定证书全部严格排除（最大界 $233003/240240 < 1$）。

#### 6. 点行 $\tau_v$ 下界不除二、整数域完整性与两个 `NO_CRITICAL` 算法的独立性
- **$\tau_v$ 不除二**：总 $\tau = \sum_{\{u,w\} \in \binom{V}{2}} \binom{\lambda(u,w)-1}{2}$ 对全部 210 个无序点对求和。固定最大度点 $v^*$（$d(v^*) = \Delta$），与 $v^*$ 关联的 20 个无序点对 $\{v^*, u\}$（$u \ne v^*$）是全部 210 个无序点对的**子集**，而其余 190 个无序点对的项均 $\ge 0$。对任意整数 $\lambda \ge 1$ 恒有 $\binom{\lambda-1}{2} \ge \lambda - 2$（$\lambda=1,2,3,4$ 时分别为 $0 \ge -1, 0 \ge 0, 1 \ge 1, 3 \ge 2$），故
  $$\tau \ge \tau_{v^*} = \sum_{u \ne v^*} \binom{\lambda(v^*, u) - 1}{2} \ge \sum_{u \ne v^*} (\lambda(v^*, u) - 2) = 4\Delta - 40,$$
  即 $\tau \ge \max(0, 4(\Delta - 10))$，绝不应除以 2。
- **两个 `NO_CRITICAL` 算法的独立性与完整性**：
  - [NO_CRITICAL_FILTER.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_FILTER.py) 按递归整数分拆生成 16 谱，遍历 $\tau \in [0,140], t \in [0, 13], m \in [0, \lfloor(140+\tau-6t)/3\rfloor]$；其中 `TT[n1]` 仅在第 54–55 行用于统计旧对照计数，第 57–65 行的新证明主链完全使用 `pb = box(n1)`。また，当 $0 \le t \le 13$ 时，$2t \le 26 < 35$，第 46 行的 `aa, bb = divmod(2*t, 35)` 恒给 `aa = 0`，从而 `wedge = 0` 恒成立，第 51 行 `if 3*wedge > 4*tau` 对 $t \le 13$ 永不触发，未删去任何整数点。
  - [NO_CRITICAL_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_CHECK.py) 完全不定义或导入 `T`，改用超出 9 度重数直方图生成 16 谱，按 $n_1 \in [397, 525], t \in [0, 13], m \in [0, \lfloor(W-n_1-4t)/3\rfloor]$ 及奇偶性恢复 $\tau, n_2, n_0$，并用 35-slot 精确动态规划验证全部 1051 个 $X$ 状态的盒上界 `kn[X]` 与闭式公式 (4) 逐项相等；仅在末尾 `assert` 处与已存 202/33 列表比对，不依赖旧表作过滤。

#### 7. 共享预算 $\sum C_j = P$、凸盒最值、贪心分配方向与阈值 $2722720$
- **共同预算与凸盒上界**：由 `U09` 恒等式，$P = \sum_{j=0}^4 C_j = \sum_{F \in H} \sum_{g<h \in F} t(F,g)t(F,h) \le \sum_{F \in H} f(s(F))$，其中 $f(s)$ 差分 $f(s+1)-f(s) = s - \lfloor s/5 \rfloor$ 非降，故 $f$ 凸。由 `U02` 知 $\delta(\Gamma) \ge 4$，故每盒 $s(F) = 34 - q_\Gamma(F) \in [0, 30]$，且 $\sum_{F \in H} (30 - s(F)) = 2(595 - n_1) - 140 =: X \in [0, 1050]$（迫 $n_1 \le 525$）。在 $0 \le s(F) \le 30$ 与固定和下，将内部点向边界 $\{0, 30\}$ 推不减目标函数，故至多一个内部盒 $30 - v$（$X = 30u + v$），式 (4) 给出的 $B(n_1)$ 是 $P$ 的精确凸松弛上界。
- **五容量与贪心方向**：由 `U08`、`U04`、`U05`，同一 $H$ 的五类 valid middle 计数满足 $0 \le C_j \le U_j$（其中 $U = (33n_0, 35n_1 - K_d(n_1), (24+\lfloor e/2\rfloor)n_2, 13n_3, 4n_4)$）且 $\sum_{j=0}^4 C_j = P \le B(n_1)$。在两翻期望中，权重 $w = (36, 120, 330, 792, 1716)$ 严格递增且全正，因此在约束 $0 \le C_j \le U_j$ 与 $\sum_{j=0}^4 C_j \le B(n_1)$ 下最大化 $\sum_{j=0}^4 w_j C_j$ 的精确最优解即为按 $j = 4, 3, 2, 1, 0$ 贪心填满至总预算 $B(n_1)$ 的分配 $\hat{C}$。这给出了原 $H$ 目标值的安全上界：
  $$L(H) = 3432 n_1 + \frac{1}{2}\sum_{j=0}^4 w_j C_j(H) \le 3432 n_1 + \frac{1}{2}\sum_{j=0}^4 w_j \hat{C}_j.$$
- **阈值 $2722720$ 与严格性**：在 `U10` 中，$n=21, k=5, M=35, a=10, D=\binom{21}{10}=352716$ 时，$\mathbb{E}X = \frac{70}{57}$，修复充分条件 $\mathbb{E}X + \frac{\mathbb{E}S + \mathbb{E}Z/4}{10} < 2$ 两边同乘 $5D = 1763580$（或对 $2L$ 同乘 $10D = 3527160$）恰为
  $$L < 1763580 \times \frac{44}{57} = 2722720 \quad (\text{等价于 } 2L < 5445440).$$
  A2 四谱在完整必要域上的最大 $L$ 为 $2719626 < 2722720$（严格余量 $\ge 3094$），故 A2 整支直接闭合。

#### 8. 六条实际 $x$ 边与 33 个剩余键在同一 $\Gamma$ 中的互斥矛盾
- 在 A3 分支中，若存在满足定理假设的非 B 超图 $H$，其非单交图 $\Gamma$ 的边数为 $E(\Gamma) = \binom{35}{2} - n_1(H) = 595 - n_1(H)$。
- 一方面，$H$ 的度谱与矩参数必须落在 `U13` 筛出的 33 个必要聚合键（[NO_CRITICAL_SURVIVORS33.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_SURVIVORS33.json)，主稿明确指出这 33 个键是必要聚合参数元组而非实际 $H$ 同构类）之一；逐键核查确认全部 33 个键的 $n_1 \in \{523, 524, 525\}$，故必有
  $$E(\Gamma) = 595 - n_1(H) \in \{70, 71, 72\} \implies E(\Gamma) \le 72.$$
- 另一方面，对**同一个**非 B 超图 $H$ 的**同一个**图 $\Gamma$，由 `U02` 知所有 35 条原边满足 $q_\Gamma(F) \ge 4$；而过唯一六度点 $x$ 的 6 条原边均满足 `U03` 的全部局部条件，故非 B 迫使这 6 条边的 $q_\Gamma(F) \ne 4$，结合 $q_\Gamma(F) \ge 4$ 得 $q_\Gamma(F) \ge 5$。由 $\Gamma$ 的握手定理：
  $$2E(\Gamma) = \sum_{F \in H} q_\Gamma(F) \ge 6 \times 5 + 29 \times 4 = 146 \implies E(\Gamma) \ge 73.$$
- $73 \le E(\Gamma) \le 72$ 在同一图 $\Gamma$ 上直接矛盾，故 A3 分支亦完整闭合。

---

### 三、明确进口台账（Declared Imports Ledger）

| 编号 | 进口命题 / 模块 | 在本证明中的作用 | 本次核查级别 |
|---|---|---|---|
| I01 | 条件排列多锁定概率引理（[PROBABILITY_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md)） | 将严格固定位置证书 $\sum_{k=1}^{21} \min(A_k, B_k, C_k - \ell_k) < 1$ 转化为原超图 $H$ 的合法二染色 | **全文数学核对 + 注入公式代码核对** |
| I02 | 21/22 点通用 $\delta(\Gamma) \ge 3$ 定理（[TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md)） | 在 `U02` 中排除 $q_\Gamma(F) \le 2$ | **全文数学核对** |
| I03 | 一般删星非 1 交图森林秩 $\ge 11$ 引理（[TWENTYONE_A1_BALANCED_STAR_FOREST.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md) §3–5） | 在 `U06` §7 中配合通用六度星下界 $C \ge 164896$ 推出 $n_4(\bar{H}) \le 6$ | **全文数学核对** |
| I04 | 旧 $t \in \{15,16\}$ 三交饱和门（[generic_c3_high_degree_saturation_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_c3_high_degree_saturation_20261020/PROOF.md)） | 在 `U04` 中覆盖 $c(G,J) \ge 14$ 且 cross 迹总数 $t \in \{15,16\}$ 的情形 | **全文数学与调用接口核对**（183 份固定证书 JSON 未重跑） |
| I05 | 六单位八度池定理（`U12`）底层 `unique6_no7` 的 26 个五邻点残轨道与三份六邻点证书 | 在 `U12` 中通过六份五视图共同包含数离散 join 为空，排除 $\ge 6$ 名 unit8 邻点 | **`U12` 全文核对 + 旧模块接口核对**（确认无自由点度数或无七度假设） |
| I06 | 选定度 $\le 9$ 的强共度双锁门（`DOUBLES.json` 及 $(9,9)$ 五份双锁证书） | 在 `U05` §6 中与 118 域高点双锁/四份三锁及 $\lambda(x,h)=5$ 解析证明合并，给出全局 $\lambda \le 4$ | **接口与回执核对**（`U05` 全文及 `VERIFY.py` 全文已核） |

**结论**：主稿 [TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN.md) 及其支撑链 `U01`–`U16` 在上述准确范围内无需修改源码或数学表述，可直接作为 `sound-modulo-imports` 候选归档。
