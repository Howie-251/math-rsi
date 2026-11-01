### 所读材料与执行声明

- **实际读取文件**：
  1. [CORE_THEOREM.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CORE_THEOREM.md)（全文，1–164 行）
  2. [UNIFORM_INTEGER_GAIN.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)（全文，1–141 行）
  3. [CLIQUE_REFINEMENT.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CLIQUE_REFINEMENT.md)（全文，1–73 行）
  4. [RS2000_FULLTEXT.txt](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/root/RS2000_FULLTEXT.txt)（1–800 行含原稿第 4–7 页，以及 1050–1222 行含末尾附录 A.1）
  5. [BASELINE.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/literature/BASELINE.md)（全文，1–186 行）
- **程序运行声明**：**未运行任何程序或脚本**，全程为纯静态数学推导与逐行核算。

---

### 逐项对抗式审阅结论

#### A. [CORE_THEOREM.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CORE_THEOREM.md)：无附加结构前提闭合与同一 RS 算法下的项相容性
- **结论：完全成立，无数学漏洞。**
- **同一 RS 算法下 FKG 与精确有向单交积分可同时使用**：
  对照 [RS2000_FULLTEXT.txt](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/root/RS2000_FULLTEXT.txt#L158-L312)（原稿第 4–7 页）与 [Appendix Claim A.1](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/root/RS2000_FULLTEXT.txt#L1183-L1217)（第 26–27 页），两项估计定义在**完全同一个概率空间与延迟重染过程** $(\chi_0, b, t)$ 上：
  1. 最终存在单色边的事件被划分为两个全局子事件的并：$\mathcal{E}_1$（存在边初态单色且终态保持同一颜色）与 $\mathcal{E}_2$（存在边终态变为某色 $c$、但初态并非全为 $c$，这已涵盖初态全红、终态全蓝的边）。对最外层仅做一次 $\Pr(\mathcal{E}_1 \cup \mathcal{E}_2) \le \Pr(\mathcal{E}_1) + \Pr(\mathcal{E}_2)$ 的并界，二者无需互相独立即可相加。
  2. $\mathcal{E}_1$ 仅依赖 $(\chi_0, b)$：由于每个顶点至多翻转一次，初态单色边 $f \in M(\chi_0)$ 终态未翻色当且仅当 $\forall x \in f, b_x = 0$（若有 $b_x=1$，最早时刻者被处理时该边必仍单色从而触发翻转）。条件于 $\chi_0$，各 $f \in M(\chi_0)$ 的事件 $\{\exists x \in f: b_x = 1\}$ 是独立 Bernoulli 变量 $b$ 的递增事件，正关联（文中第 60 行给出的坐标归纳证明完整正确）结合 $x \mapsto a_k(p)^x$ 的凸性与 Jensen 不等式给出 $\Pr(\mathcal{E}_1) \le 1 - a_k(p)^{m/2^{k-1}}$。
  3. $\mathcal{E}_2$ 中，若 $f$ 最后翻蓝的初态红点为 $x$、触发边为初态全红且到 $t_x$ 仍全红的 $g \ni x$，则 $(f \cap g)\setminus\{x\}$ 中若有其它点 $z$，必初态为红且终态为蓝，从而在 $t_x$ 前已翻转，与 $g$ 在 $t_x$ 时仍全红矛盾，故必有 $|f \cap g| = 1$（且 $f \ne g$）。固定有向单交对 $(f,g)$ 与 $t_x = t$，在三个不交点集 $\{x\}$、$f\setminus\{x\}$、$g\setminus\{x\}$ 上对初态红集 $S \subseteq f\setminus\{x\}$ 互斥求和并关于 $t \in [0,1]$ 积分，精确等于 $2^{1-2k} J_k(p)$。对红蓝两色与 $\gamma(H)$ 个有向单交对作并界即得 $\gamma(H) 4^{1-k} J_k(p)$。
- **从任意有限简单 $k$ 元超图闭合原染色、无额外结构前提**：
  [引理 2](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CORE_THEOREM.md#L98-L112) 在所有边数 $\le M$ 的非 Property B 有限简单 $k$ 元超图中取**顶点数 $v$ 最小**的反例 $H$（实际边数 $m \le M$）。若存在不共边的两点，合并后每条边仍含 $k$ 个不同顶点，去重后边数 $m' \le m \le M$ 且仍非 B，与 $v$ 最小矛盾。从而 $\binom{v}{2} \le m\binom{k}{2} \le M\binom{k}{2} \implies v \le v_k(M)$，无需对原输入预设点对覆盖或补边。[引理 3](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CORE_THEOREM.md#L114-L147) 由关联矩阵 $AA^{\mathsf T} = (k-1)I_q + J_q \succ 0$ 得 $\omega(S(H)) \le v$，再由补图独立集期望（Caro–Wei）与 Cauchy–Schwarz 得 $\gamma(H) \le (1-1/v)m^2$，结合 $m \le M, v \le v_k(M)$ 的单调性闭合定理 A。

---

#### B. [UNIFORM_INTEGER_GAIN.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)：$k \ge 17$ 的旧最优整数预算定义、严格 $+1$ 与取整
- **结论：完全成立，无数学或取整漏洞。**
- **整数预算定义与取整语义**：
  $B_{\rm RS}(k)$ 直接在正整数集 $\mathbb Z_{\ge 1}$ 上定义为满足旧精确判据 $\frac{M(M-1)}{d^2}J_k(p) < a_k(p)^{M/d}$ 的最大整数 $M$。由 [证明四](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md#L112-L128)，$M_0 = 2^k, p = 1/k$ 时 $a_k(1/k) > 1/2$ 且 $\frac{M_0(M_0-1)}{d^2}J_k(1/k) < \frac{4}{k} \le \frac{4}{17} < \frac{1}{4} < a_k(1/k)^2$，故可受集非空且含 $2^k$；又由 [证明一](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md#L30-L56) 知 $M \ge 2^k$ 时必有 $p > 1/k^2 \implies J \ge \frac{1}{2k^2} \implies a^\kappa > \frac{\kappa^2}{4k^2}$，从而 $\kappa < 2k$（即 $M < k2^k$）且 $\kappa \log a > -2\log k$。有限非空整数集的最大值 $B_{\rm RS}(k)$ 必然存在且有实际见证 $p \in (0,1]$，无需任何连续优化器可达性假设。
  旧判据最多保证边数 $\le B_{\rm RS}(k)$ 可染，即 $m(k) \ge B_{\rm RS}(k) + 1$；新证明对 $M = B_{\rm RS}(k)$ 证明定理 A 在整数边数预算 $N = M + 1 = B_{\rm RS}(k) + 1$ 严格成立，故边数 $\le B_{\rm RS}(k)+1$ 均可染，直接等价于 $m(k) \ge B_{\rm RS}(k) + 2$，不存在实数阈值取整歧义。
- **逐行不等式核验**：
  - [第 61–70 行](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md#L61-L70)：在 $x=17$ 处，$\sum_{j=0}^5 3^j/j! = 1+3+9/2+9/2+27/8+81/40 = 92/5 = 18.4 > 17 \implies \log 17 < 3$；右端 $8(17)+4(17)\log 17 < 340$，左端 $2^{17/2} = 256\sqrt{2} > 256\times 7/5 = 358.4 > 340$，结合对数导数 $>0$ 知 (5) 对所有 $x \ge 17$ 成立。
  - [第 75–108 行](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md#L75-L108)：$v_k(N) \le 1 + k\sqrt{N} \le 2k\sqrt{M}$ 给出 $\frac{1}{v} \ge \frac{1}{2k\sqrt{M}} > \frac{4+2\log k}{M}$；代入 $\log R \le \frac{2}{M} + \frac{1}{M-1} - \frac{1}{v} \le \frac{4}{M} - \frac{1}{v} < -\frac{2\log k}{M} < \frac{\log a}{d}$，严格闭合 $\frac{g_k(N)}{d^2}J < a^{(M+1)/d}$。

---

#### C. [CLIQUE_REFINEMENT.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CLIQUE_REFINEMENT.md)：公共点二分团界与增长增益 $\lfloor \sqrt{B_{\rm RS}(k)} / (8(1+\log k)) \rfloor$
- **结论：对全范围 $k \ge 17$ 完全成立，未发现数学错误或反例。**
- **公共点二分团界核查（[第 5–27 行](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CLIQUE_REFINEMENT.md#L5-L27)）**：
  设 $S(H)$ 中 $q$ 点团对应 $q$ 条两两**恰交一点**的 $k$ 元边：
  1. 若有公共点 $x$，各边去掉 $x$ 后的 $(k-1)$ 元集两两不交（否则两边交集 $\ge 2$），故 $q(k-1)+1 \le v \implies q \le \lfloor \frac{v-1}{k-1} \rfloor$。
  2. 若无公共点，固定团中一边 $e$。对每个 $x \in e$，存在团中不含 $x$ 的边 $f_x$；团中所有含 $x$ 的边与 $f_x$ 恰交一点，且不同边在 $f_x$ 上的交点必互异（否则同时含 $x$ 与该交点，交集 $\ge 2$），故含 $x$ 的团内边数 $d_x \le |f_x| = k$，从而 $q - 1 = \sum_{x \in e}(d_x - 1) \le k(k-1) \implies q \le k^2 - k + 1$。
  3. 结合 $v \le v_k(N)$ 及单调性，$\omega(S(H)) \le r_k(N)$ 与 $\gamma(H) \le g_k^*(N)$ 对边数 $\le N$ 的最小顶点反例恒成立。
- **增长增益核查（[第 29–70 行](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CLIQUE_REFINEMENT.md#L29-L70)）**：
  - 对 $k \ge 17, M \ge 2^k$，$s = \lfloor \frac{\sqrt{M}}{8(1+\log k)} \rfloor \ge 10 \ge 1$ 且 $N = M+s \le 2M$。
  - 由 $(v_k(N)-1)^2 < v_k(N)(v_k(N)-1) \le k(k-1)N$ 两边开方并除以 $k-1$ 得 $\frac{v_k(N)-1}{k-1} < \sqrt{\frac{kN}{k-1}} \le \sqrt{\frac{17}{8}M} < 2\sqrt{M}$；同时 $k \ge 17 > 16 \implies k^2 - k + 1 < k^2 \le 2^{k/2} \le \sqrt{M} < 2\sqrt{M}$，故 $1 < r_k(N) \le 2\sqrt{M}$。
  - 对数上界 $\log \frac{N^2(1-1/r)}{M(M-1)} = 2\log(1+\frac{s}{M}) + \log(1+\frac{1}{M-1}) + \log(1-\frac{1}{r}) \le \frac{2s+2}{M} - \frac{1}{r}$，配合 $(2+2\log k)s + 2 \le \frac{\sqrt{M}}{4} + 2 < \frac{\sqrt{M}}{2} \le \frac{M}{r}$ 严格给出 $< -\frac{2s\log k}{M} < \frac{s\log a}{d}$，闭合 $m(k) \ge B_{\rm RS}(k) + 1 + \lfloor \frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)} \rfloor$。

---

#### D. 仍需比较的强文献基线（防止将相对 RS 改进误升格为世界最优）
当前定理 B 与 `CLIQUE_REFINEMENT.md` 证明的是**相对于指定 `RS-FKG-exact + γ ≤ M(M-1)` 判据**（即 $B_{\rm RS}(k)+1$）的严格统一增益。要在选定范围 $K$（如 $k \ge 17$ 或其子集）宣称新的世界最优无条件一般下界，根据 [BASELINE.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/literature/BASELINE.md) 仍须与以下强文献基线比较或合成：

1. **Grill–Linzmayer (2024, arXiv:2403.05674v3) 连续逐点取小判据（[BASELINE.md §5.1](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/literature/BASELINE.md#L88-L98)）**：
   $$C_k(M, \gamma) = \min_{x \in [0, 1/2]} \left( 2M x^k + \gamma \int_x^{1-x} u^{k-1}(1-u)^{k-1}\,du \right) < 1 \quad (\gamma = M(M-1)).$$
   该判据虽在一阶项用线性并界 $2Mx^k$（弱于 RS-FKG 的 $1-(1-(1-p)^k)^{M/2^{k-1}}$），但在积分内对一阶、二阶项逐点取 $\min$（截去了 $[0,x]$ 与 $[1-x,1]$ 上的二阶尾积分，并自动涵盖 Pluhár 2009 的纯二阶阶乘界）。需核实在目标范围 $k \ge 17$ 上，$B_{\rm RS}(k)$（或新界）是否恒不低于 $C_k(M, M(M-1)) < 1$ 给出的整数界；或者直接将本文的新结构界 $\gamma(H) \le g_k^*(M)$ 代入 $C_k(M, g_k^*(M)) < 1$ 同步获得对 $C_k$ 基线的严格提升。
2. **Grill–Linzmayer (2024) 离散逐位置取小包络（[BASELINE.md §5.2](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/literature/BASELINE.md#L100-L120)）**：
   对所有未被点对覆盖下界 $S_k(v) = \lceil \frac{v}{k}\lceil \frac{v-1}{k-1}\rceil \rceil \le M$ 和平衡二染色界排除的顶点数 $v \ge 2k-1$，离散随机排列判据 $D_k(v, M, M(M-1)) < 1$ 在有限 $v$ 上严密优于连续积分 $C_k(M, M(M-1)) < 1$。在宣称具体 $k$ 的绝对数值下界前，必须确认新界是否超过该无锁离散包络（或同样将 $\gamma \le \min\{M(M-1), (1-1/r_k(v))M^2\}$ 嵌入 $D_k(v, M, \gamma)$ 的全域 $v$ 包络中直接对比）。
3. **Grill–Linzmayer (2024) 局部度/共度与一至三锁加强及 Aglave et al. (2020)（[BASELINE.md §5.3–5.4, §6](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/literature/BASELINE.md#L122-L148)）**：
   在小 $k$（原文算至 $k=5\dots 9$，本地合作者材料含 $k=6\dots 11$）有基于度数/共度扣除 $\gamma \le \sum_i [d_i(d_i-1)-r_i(r_i-1)]$ 与一、二、三锁分流的更强数值；若目标范围 $K$ 限制在 $k \ge 17$，需明确说明 $k \ge 17$ 不与已发表的 $k \le 9$ 锁点数表重叠，并核查 Grill–Linzmayer (2026) 综述全文（[BASELINE.md 第 152、181 行](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round01/literature/BASELINE.md#L152)标注未读）中是否给出了 $k \ge 17$ 的新通用闭式或数表。

---

### 必要修改建议

1. **A、B、C 数学正文无需作勘误性修改**：三份文件中的定理陈述与证明链条在 $k \ge 17$ 上均已严密成立。
2. **可选可读性微调（[CLIQUE_REFINEMENT.md 第 39–41 行](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CLIQUE_REFINEMENT.md#L39-L41)）**：若将 `CLIQUE_REFINEMENT.md` 并入正式主证明，可在第 39 行显式写出 $(v_k(N)-1)^2 < v_k(N)(v_k(N)-1) \le k(k-1)N$ 再两边开方除以 $k-1$，并在第 41 行顺手点明 $k^2-k+1 < k^2 \le \sqrt{M} < 2\sqrt{M}$，使读者无需自行核对 $r_k(N)$ 两个分支的上界。
3. **基线定位表述保持准确**：在合并主规格时，保持 `UNIFORM_INTEGER_GAIN.md` 与 `CLIQUE_REFINEMENT.md` 现有的审慎表述（明确标注为相对 `RS-FKG-exact` 预算 $B_{\rm RS}(k)+1$ 的统一整数增益），若要升格为 $k \ge 17$ 上超越全部现有文献的无条件界，建议同时给出相对 Grill–Linzmayer (2024) 连续/离散判据的比较或将 $g_k^*(N)$ 同步接入该判据。

