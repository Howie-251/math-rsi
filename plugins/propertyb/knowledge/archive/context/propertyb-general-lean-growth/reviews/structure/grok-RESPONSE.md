这条一般 Property B 结构链是闭合的。在所读范围内，没有发现会把最终 Bool 二染色结论推错的语义或数学缺口。剩余前提就是声明中的那个对所有可容许顶点数 `n` 的严格数值不等式。

## 阅读范围

全文阅读了 `formal/Aris4Math/General/Structure/{Definitions,Reduction,Clique,Turan,ProbabilityBudget,Main}.lean` 和 `formal/ReviewAuditGeneralStructure.lean`。接口只读了 `General/RS/Definitions.lean` 的 `Uniform`、`Bichromatic`、`PropertyB`、`singlePairs`、`gamma`，`Integral.lean` 的 `ak`、`jk` 及 `ak_pos`、`ak_le_one`、`jk_nonneg`，`ProbabilityBound.lean` 的 `propertyB_of_rs_bound`，以及 `Lift.lean` 的 `relabel` 与 `propertyB_relabel_iff`、`uniform_relabel_iff`。纸面读了 `CORE_THEOREM.md` 的定义 1–2、引理 2、引理 3.1 的有向因子形式，以及 `CLIQUE_REFINEMENT.md` 的 C.1 与 C.2。Mathlib 只核对了实际调用的 `offDiag_card`、`CliqueFree`、`CliqueFree.card_edgeFinset_le`、`mul_card_edgeFinset_turanGraph_le`、`dart_card_eq_twice_card_edges` 和 `rpow_le_rpow_of_exponent_ge`。

`build04.log` 与 `audit02.log` 只作阅读。前者记录 `Structure.Main` 构建成功；后者记录审计文件已展开，且 `exists_pair_covering_counterexample`、`pairCovering_count`、`gamma_eq_twice_singleGraph_edges`、`gamma_le_cliqueBudget`、`propertyB_of_structural_rs_bound`、`original_structural_criterion` 的公理均为 `propext`、`Classical.choice`、`Quot.sound`。本次没有运行 Lean，也没有重审概率核正文。

## 反译

两个顶层陈述的数学内容相同。`original_structural_criterion` 把 `cliqueBudget`、`jk`、`ak` 写成了显式公式；`propertyB_of_structural_rs_bound` 使用这三个定义。审计文件以 `exact` 衔接，而 `jk` 与 `ak` 的定义分别就是该积分和 `1-(1-p)^k`。分母里的 `: ℕ` 是团界的自然数归属，随后按实数做除法。

设 `V` 有限，`E` 是 `V` 上的有限边族，`k,N` 为自然数，`p` 为实数。若

- `k ≥ 2`，每条 `e ∈ E` 满足 `|e| = k`，且 `|E| ≤ N`；
- `0 < p ≤ 1`；
- 对每个自然数 `n`，只要 `k ≤ n` 且 `n(n-1) ≤ k(k-1)N`，就有

\[
\frac{\bigl(1-1/r_k(n)\bigr)N^2}{4^{k-1}}
\int_0^p(1-y^2)^{k-1}\,dy
<
\bigl(1-(1-p)^k\bigr)^{N/2^{k-1}},
\]

其中 \(r_k(n)=\max\{k^2-k+1,\lfloor(n-1)/(k-1)\rfloor\}\)，\(4^{k-1}=(2^{k-1})^2\)，

则存在 `c : V → Bool`，使每条边同时含 `true` 与 `false`。`p` 由调用者给出，并且必须对全部可容许 `n` 同时成立。空边族不需要这条数值假设：`k ≥ 2` 时，`n ≥ k` 与 `n(n-1) ≤ 0` 不能并存，全称前提为真，而空族本身满足 Property B。

## 链条核对

反例约化与引理 2 一致。若 `E` 不是 Property B，则经有限双射搬到 `Fin` 后，顶点数目最小的反例 `K` 仍是 `k` 元、边数至多 `N`、且不是 Property B。`Nat.find` 取到的可以是同预算下另一个最小反例；否定它的存在即可否定一切反例。未共边的两个顶点被合并后，边上单射保持每条像的基数为 `k`，像族边数不增。像族若可染，染色可沿合并映射拉回，因此像族仍是反例，并少一个顶点。最小反例因而满足点对覆盖。空族可染，所以反例边数为正，进而 `k ≤ n`。

点对计数用的是有序对。`offDiag` 的基数是 `s^2-s`，全体顶点给出 `n(n-1)`，每条边给出 `k(k-1)`。覆盖只保证并集包含全部有序点对，重边造成的重复使不等号朝向边侧，得到 `n(n-1) ≤ k(k-1)|K| ≤ k(k-1)N`。这与 \(\binom n2 ≤ |K|\binom k2 ≤ N\binom k2\) 相同。

团界与 C.1 一致，作用对象是单交图中的团，也就是一组两两恰交一点的真实原边。有公共点时，去掉该点后的剩余部分互不相交，每块 `k-1` 个顶点，故 `q(k-1)+1 ≤ n`，即 `q ≤ ⌊(n-1)/(k-1)⌋`。没有公共点时，固定一条边，每个点上至多 `k` 条边穿过一条避开它的边，得到 `q ≤ k^2-k+1`。二者取最大。空族在非空顶点集上落入公共点分支的空全称，基数 `0` 仍不超过该上界。`k ≥ 2` 使 `k-1` 为正，自然数除法就是下取整，并且 `r_k(n) ≥ k^2-k+1 ≥ 3`。

`gamma` 是有序单交对的个数。它与单交图的 dart 一一对应，而 dart 数等于无向边数的两倍，所以 `gamma = 2|E(S)|`。`CliqueFree (r+1)` 加上 Mathlib 的 Turán 松估计 `2r|E(T(m,r))| ≤ (r-1)m^2`，给出

\[
\gamma(K)\le\bigl(1-1/r_k(n)\bigr)|K|^2.
\]

系数非负，再放宽到 `N`，得到 `gamma ≤ (1-1/r_k(n))N^2`。这里的自然数不等式先成立，再原样送进实数；实除法只发生在最后除以 `r_k(n)`。

同一 `K` 进入已证的 `propertyB_of_rs_bound`。其接口就是

\[
1-a_k(p)^{|K|/2^{k-1}}+\gamma(K)\,J_k(p)/4^{k-1}<1.
\]

`0 < a_k(p) ≤ 1` 且 `J_k(p) ≥ 0` 已由积分文件给出。边数与 `gamma` 的上界都使失败概率上界变大，指数单调性用的是 `rpow_le_rpow_of_exponent_ge`。因此数值假设推出 `K` 可染，与 `K` 为反例矛盾，故原 `E` 可染。合并映射只负责制造最小反例；原宇宙上的 Bool 染色由这个反证存在，双射搬迁保持 Property B 的两个方向。

## 范围

与 C.2 的包装相比，形式化结果故意更弱，但与代码中的陈述相符。`r` 没有再与顶点数取最小，Gram 秩界没有进入证明。标量用的是 `(1-1/r_k(n))N^2`，没有再与平凡的 `N(N-1)` 取最小。结论是 Property B，量词停在上述充分条件，没有推出 `m(k) ≥ N+1`，也没有证明该数值不等式本身。
