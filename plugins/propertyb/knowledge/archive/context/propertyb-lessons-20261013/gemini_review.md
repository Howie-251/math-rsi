# Gemini：两次Property B下界经验审阅

CLI选择模型：gemini-3.8-flash-high；effort：high（cli_selected_model_variant）；状态：SUCCESS；thread：`bbb8bd5a-0111-450a-aa56-39c8731852e0`。

### 审阅范围与执行声明

- **实际阅读文件**：
  - [`PROPERTY_B_RESEARCH_LESSONS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md)
  - [`PROPERTY_B_FAILURE_ATLAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md)
  - [`PROPERTY_B_NEXT_BOUND_PLAYBOOK.md`](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_NEXT_BOUND_PLAYBOOK.md)
  - [`MATH_TRANSFER.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/MATH_TRANSFER.md)
  - [`SMALL_VERTEX_34_NOTE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/SMALL_VERTEX_34_NOTE.md)
  - [`LEAN_AND_EXECUTION.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/LEAN_AND_EXECUTION.md)
  - [`check_boundary_arithmetic.py`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/check_boundary_arithmetic.py)、[`NO_LOCK_BOUNDARY_CHECK.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/NO_LOCK_BOUNDARY_CHECK.json)
- **执行命令与访问限制声明**：
  - 本次为**纯只读审阅**；
  - **未执行任何 shell 命令行**，未发起后台任务；
  - 未创建或修改任何文件，未访问 `aris4math_v2`，未重构或重编既有 Lean 链。

---

### 一、核心方法链条的可指导性评估

文档提炼的核心链条：
$$\text{实际 } H \longrightarrow \text{结构选点} \longrightarrow \text{完整有限分类} \longrightarrow \text{类型重数恢复} \longrightarrow \text{加权条件概率/配额扣除} \longrightarrow \text{原命题 Property B}$$
经核验，该架构不仅具备完整的数学闭环，且在实际 Lean 工程中已具备真实 caller，能够切实指导后续研究。

针对向更高下界迁移，总结中指出的以下工程事实与边界极其关键，能直接避免无效工作：
1. **包装层参数写死风险**：[`MultiLockRecovery.actual_recovered`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/MultiLockRecovery.lean) 虽然在任意边集上通用，但外层包装 [`realizes_recovered`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/MATH_TRANSFER.md#L53) 显式写死了 `33`；下一档必须新增泛化包装，不可直接复用。
2. **默认参数隐患**：[`Numeric.validProfile`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean) 与 [`TypeCounting.RealizesProfile`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/TypeCounting.lean) 虽然已带参数，但缺省值为 `32`；新调用者必须显式传递边数。
3. **自然常量同步**：34 边时自然有序单交对上限为 $34 \times 33 = 1122$（非旧 1056），双锁单位共度空迹基数为 $35 - d(x) - d(y)$（非旧 $34 - d(x) - d(y)$）。

---

### 二、关键概念与边界辨析核验

1. **发现阶段 242 strict vs 最终 234 bare + 9 dual**（`no_issue_found`）：
   - [`PROPERTY_B_FAILURE_ATLAS.md#L124-L131`](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L124-L131) 精确区分了两阶段：发现阶段的 242 代表严格是在总/纯 link 配额扣除下的结果；最终 Lean 实现中，234 个代表属于无需额外配额删除的 bare 分支，9 个代表走非负 LP dual 证书分支（包含临界型 group212，界为 $19439/19448 < 1$），合计覆盖全部 243 个轨道代表。文档明确指出“不能误把发现阶段 242 写成 242 个 bare”，定性准确。
2. **七锁固定窗口失败 vs 方法全局不可能**（`no_issue_found`）：
   - [`PROPERTY_B_FAILURE_ATLAS.md#L115-L121`](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L115-L121) 明确记录了 25 点 $K_7$ 的 22 构型在固定窗口（10..16）下有 10 型未过（如 Fano 型 $1871/1870 > 1$）；这仅排除了“固定小窗口内任意七锁可直接通过”，并未否定七锁/多锁方法本身。最终通过八锁结构平均选点成功闭合。区分了“有界搜索未命中”与“数学上不可行”。
3. **压缩 $K_{4,7}$ 反模型 vs 超图反例**（`no_issue_found`）：
   - [`PROPERTY_B_FAILURE_ATLAS.md#L105-L109`](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L105-L109) 准确指明：二部图 $K_{4,7}$ 是对“两步路径 $\le 10$ 与颜色容量压缩条件”的局部反模型，证明仅凭该松弛条件无法保证选出合规 $C_4$；但这并非可扩充为 23 点 33 边的超图，更不是 Property B 的反例。这及时终止了在弱松弛条件上的徒劳推导。
4. **重计算并发争抢 vs 缓存 12 秒过度外推**（`no_issue_found`）：
   - [`LEAN_AND_EXECUTION.md#L91-L109`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/LEAN_AND_EXECUTION.md#L91-L109) 记录详实：本机 10-core/32GB 下多重进程并发导致 swap 激增至 25GB，造成恢复与裸界模块墙钟膨胀至 5337s 与 6961s（系统争抢而非纯计算复杂度）；最终 Main 构建 12.5 秒是全部 `.olean` 依赖已完成后的增量组装，绝非全图从零编译只需 12 秒。该总结有效防止了对机器开销的两个极端误判。

---

### 三、独立数学复核：34 边 17/18 点与 21/24/25 点

#### 1. 17/18 点正交叠推导独立复算（核验一致）
在平衡二染色空间（红 $\lfloor v/2 \rfloor$，蓝 $\lceil v/2 \rceil$）中：
- 单条 5 元边单色概率：
  $$p_{17} = \frac{\binom{8}{5} + \binom{9}{5}}{\binom{17}{5}} = \frac{56 + 126}{6188} = \frac{182}{6188} = \frac{1}{34}, \qquad p_{18} = \frac{2\binom{9}{5}}{\binom{18}{5}} = \frac{252}{8568} = \frac{1}{34}$$
  恰好导致 34 边的朴素并集界 $34 \times (1/34) = 1$ 失效。
- 任意两条不同 5 元边 $e, f$（交数 $t = |e \cap f| \in \{0,1,2,3,4\}$，并集大小 $u = 10 - t$）：
  - 当 $t \ge 1$ 时，$e, f$ 只能同色；在样本空间 $\binom{v}{\lfloor v/2 \rfloor}$ 中，同时单色的染色数为 $\binom{v-u}{\lfloor v/2 \rfloor - u} + \binom{v-u}{\lfloor v/2 \rfloor}$。
  - 当 $t = 0$ 时，$e, f$ 只能异色（因两色容量均 $< 10$）；同时单色的染色数为 $2\binom{v-10}{\lfloor v/2 \rfloor - 5}$。
- 逐项复算结果（与 [`SMALL_VERTEX_34_NOTE.md#L19-L24`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/SMALL_VERTEX_34_NOTE.md#L19-L24) 完全一致）：
  - $v=17$（总样本 24310）：$t=0 \to 70$；$t=1 \to 1$；$t=2 \to 10$；$t=3 \to 55$；$t=4 \to 220$。最小频数为 $1$（在 $t=1$ 处）。
  - $v=18$（总样本 48620）：$t=0 \to 140$；$t=1 \to 2$；$t=2 \to 20$；$t=3 \to 110$；$t=4 \to 440$。最小频数为 $2$（在 $t=1$ 处）。
- 故对于任意不同两边，正交叠下界均严格为：
  $$P(A_e \cap A_f) \ge \frac{1}{24310}$$
- 由简单并集界（仅合并 $e, f$ 两个事件）：
  $$P\left(\bigcup_{g \in E} A_g\right) \le \sum_{g \in E} P(A_g) - P(A_e \cap A_f) \le 34 \times \frac{1}{34} - \frac{1}{24310} = \frac{24309}{24310} < 1$$
  **结论**：该纸面推导无需容斥原理的三重交截断，逻辑严密，结果严格。

#### 2. 21/24/25 点度数变化独立推导（核验一致）
设边数 $m = 34$，点对覆盖超图的总度为 $\sum d(x) = 5 \times 34 = 170$，$4d(x) \ge v - 1$：
- **$v=21$**：$\delta \ge \lceil 20/4 \rceil = 5$。总度 $21 \times 8 = 168 \le 170$。
  - **新特征**：允许全体度数 $\ge 8$（T33 中 $21 \times 8 = 168 > 165$ 强制 $\delta \le 7$）。
  - 若 $\delta = 8$，超出 $21 \times 8$ 的总超额仅为 $170 - 168 = 2$。度序列只能为刚性的 $8^{19}9^2$ 或 $8^{20}10^1$。
- **$v=24$**：$\delta \ge \lceil 23/4 \rceil = 6$。若 $r$ 个六度点、$t$ 个七度点，则 $6r + 7t + 8(24 - r - t) \le 170 \implies 2r + t \ge 22$。
  - **新特征**：$2r + t \ge 22$ 允许 $r = 0$（T33 中 $2r + t \ge 27$ 强制 $r \ge 3$）。
  - 若 $r = 0$（无六度点），总度下界 $24 \times 7 = 168$，超额仅为 2。度序列只能为 $7^{22}8^2$ 或 $7^{23}9^1$。
- **$v=25$**：$\delta \ge \lceil 24/4 \rceil = 6$。$6r + 7(25 - r) \le 170 \implies r \ge 5$。
  - **新特征**：保证至少 5 个六度点（T33 保证 $\ge 10$ 个，T32 保证 $\ge 15$ 个）。
  - 若恰有 $r = 5$ 个六度点，总度恰好为 $5 \times 6 + 20 \times 7 = 170$，故其余 20 点全部恰为七度；且每个六度点的共度超额 $\epsilon_x = 4(6) - 24 = 0$，与所有其他 24 点共度全部刚性为 1。

---

### 四、会改变后续执行的具体修正与建议

#### 1. 20 点单位伙伴度数上界的补充修正（需更新）
- **位置**：[`PROPERTY_B_NEXT_BOUND_PLAYBOOK.md#L24`](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_NEXT_BOUND_PLAYBOOK.md#L24) 及 [`MATH_TRANSFER.md#L159`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-lessons-20261013/MATH_TRANSFER.md#L159)
- **事实分析**：
  在 $v=20, m=34$ 中，中心 $x$ 的单位伙伴集 $W$ 大小满足 $|W| \ge 38 - 4d$。总超额为 $170 - 20d$。伙伴度数满足 $d(y) \le d + \lfloor (170 - 20d)/|W| \rfloor$。
  - 当 $d = 8$ 时，$|W| \ge 6$，超额 $10$，$\lfloor 10/6 \rfloor = 1 \implies d(y) \le 9$（文档已正确指出新增 $(8,9)$）。
  - **遗漏点**：当 $d = 7$ 时，$|W| \ge 10$，总超额为 $170 - 140 = 30$。此时 $\lfloor 30/10 \rfloor = 3 \implies d(y) \le 7 + 3 = 10$！
    而在 T33 中，总超额为 $165 - 140 = 25$，$\lfloor 25/10 \rfloor = 2 \implies d(y) \le 9$。
- **建议**：在 20 点伙伴度数变化说明中，除指出 $\delta=8$ 伙伴可达 9 度外，补充“$d=7$ 时单位伙伴上界也由 9 度增至 10 度（潜在 $(7,10)$ 配置）”，避免后续构建 20 点双锁表时遗漏该新行。

#### 2. 23 点 $r=3$ 容斥余量的显式提炼（可选改良）
- **位置**：[`PROPERTY_B_NEXT_BOUND_PLAYBOOK.md#L45`](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_NEXT_BOUND_PLAYBOOK.md#L45)
- **内容**：文档敏锐指出了 $r=3$ 时 $t \ge 8$ 仍能选出 2 个共同单位高点。
- **建议**：可将“每个六度点 $\epsilon_x = 2$，最多排除 2 个非单位伙伴；3 个六度点合计至多排除 6 个；$8 - 6 = 2$ 必保 2 个共同单位高点”这一初等论证直接固化在指南正文，便于后续直接作为选点引理的 Lean 形式化骨架。

---

### 五、审阅结论

本次经验总结与失败地图严格求实，客观区分了**已验证定理、纸面推导、局部反模型与性能开销**，未发现阻断性数学漏洞或伪证明问题（核心链条 `no_issue_found`）。提出的“先差分整数预算与选点、再做局部诊断、最后按实测内存调度重任务”的方法具有高度的可操作性，能够切实指导下一阶段工作。

