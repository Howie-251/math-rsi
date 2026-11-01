# 一般增长下界的完整 Lean 形式证明

对每个整数 \(k\ge17\)，一般下界主定理C已完成 Lean 形式证明：任意有限简单 \(k\) 元超图，只要边数不超过指定 RS 最大整数预算加上显式增长增益，就存在使每条原边同时含两色的 Bool 染色。最大预算的存在性、最大性、严格正参数见证、最小反例结构和增长余量均由证明内部构造。

指定主入口 `formal/Aris4Math/General/Growth/Main.lean` 已通过正式 Lake 构建；构建后的独立审计 `formal/ReviewAuditGeneralGrowth.lean` 直接展开原始最大预算、积分和染色定义，也已编译成功。七项传递公理审计均仅含 `propext`、`Classical.choice`、`Quot.sound`。

## 定义：原超图、最大预算与整数增益

**定义1（原超图与 Property B）。** 设 \(V\) 为任意有限集合，\(E\) 为由 \(V\) 的有限子集组成的有限集合。称 \(E\) 为简单 \(k\) 元超图，是指每个 \(e\in E\) 都满足 \(|e|=k\)。称 \(E\) 具有 Property B，是指存在 \(c:V\to\{\mathtt{true},\mathtt{false}\}\)，使每条 \(e\in E\) 中既有颜色为 true 的点，也有颜色为 false 的点。Lean 中分别对应 `Uniform`、`PropertyB` 和 `Bichromatic`，原对象表示为 `E : Finset (Finset V)`、`[Finite V]`。

**定义2（指定 RS 判据及其最大整数预算）。** 对整数 \(k\ge17\)，置

\[
d_k=2^{k-1},\qquad a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy.
\]

称正整数 \(M\) 被指定判据接受，是指存在 \(p\in[0,1]\) 满足

\[
\frac{M(M-1)}{d_k^2}J_k(p)<a_k(p)^{M/d_k}.
\]

令

\[
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d_k^2}J_k(p)<a_k(p)^{M/d_k}\right\}.
\]

这一定义组合 Radhakrishnan–Srinivasan 作者稿 Appendix A、Claim A.1（第26–27页）的正关联端项，与 §2.1、Claim 2.4 证明中第7页的未编号精确积分，再使用有向单交边对数至多 \(M(M-1)\)。原作者稿为 [Improved bounds and algorithms for hypergraph 2-coloring](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)。**\(B_{\rm RS}\) 是本文由组合判据定义的最大整数预算，并非原文的同名定理或记号。** 完整来源与纸面证明定位见 `PROPERTY_B_GENERAL_BOUND.html`。

Lean 中 `AcceptedAt k M p` 表示接受不等式及参数区间，`RSAccepts k M` 另要求 \(1\le M\)，`rsBudget k` 表示最大预算。其实现先在有限区间 \(M<k2^k\) 取上确界；`rsBudget_characterization` 证明这正是对全部正整数的最大值，区间截断不是外部假设。

**定义3（整数增益）。** 对自然数 \(k,M\)，令

\[
s(k,M)=\left\lfloor\frac{\sqrt M}{8(1+\log k)}\right\rfloor_{\!\mathbb N},\qquad
\Delta(k)=s\bigl(k,B_{\rm RS}(k)\bigr),
\]

其中 \(\log\) 为自然对数，\(\lfloor\cdot\rfloor_{\mathbb N}\) 为自然数下取整。Lean 中对应 `integerGain k M`；在本定理范围内被取整量为正，故与通常的整数下取整一致。

## 定理C：全部 k≥17 的原超图染色

**定理C（已形式化）。** 对每个整数 \(k\ge17\)，定义2的最大值存在，并满足

\[
2^k\le B_{\rm RS}(k)<k2^k,\qquad \Delta(k)\ge1.
\]

而且存在同一个严格参数见证 \(0<p\le1\)，使定义2的接受不等式在 \(M=B_{\rm RS}(k)\) 成立。对任意有限集合 \(V\) 与任意简单 \(k\) 元超图 \(E\)，若

\[
|E|\le B_{\rm RS}(k)+\Delta(k),
\]

则存在 \(c:V\to\{\mathtt{true},\mathtt{false}\}\)，使每条原边同时含两色。因此，若 \(m(k)\) 表示不可二染简单 \(k\) 元超图的最少边数，则

\[
\boxed{m(k)\ge B_{\rm RS}(k)+1+\Delta(k).}
\]

**形式证明。** `rsBudget_characterization` 给出全体正整数中的最大性，`rsBudget_parameter` 给出实际正参数见证，`seed_le_rsBudget` 与 `rsBudget_lt` 给出两端界。`propertyB_of_general_growth` 对任意原 `E` 构造染色，`non_propertyB_edges_ge_general_growth` 给出等价的不可染边数下界。完整独立复述 `GeneralGrowthAudit.original_complete_statement` 同时展开了积分、最大性、增益和原 Bool 两色见证；`original_noncolorable_lower_bound` 则展开原不可染命题。上述声明均已编译，并接受构建后的传递公理检查。∎

最终主接口如下；它没有点对覆盖、顶点数、度数、概率上界或内部证书前提。

```lean
theorem propertyB_of_general_growth {V : Type u} [Finite V]
    (E : Finset (Finset V)) {k : ℕ} (hk : 17 ≤ k)
    (hu : Uniform E k)
    (hE : E.card ≤ rsBudget k + integerGain k (rsBudget k)) :
    PropertyB E
```

## 证明：真实输入到增长下界的完整连接

**引理1（实际最小反例的点对覆盖）。** 设 \(k\ge2\)，\(N\) 为自然数。如果存在有限简单 \(k\) 元超图，边数至多 \(N\) 且不可二染，则存在一个顶点数最小的此类反例 \(K\)，记其顶点数为 \(n\)。该反例覆盖每个不同顶点对，并且

\[
n(n-1)\le k(k-1)|K|\le k(k-1)N.
\]

**证明。** 若不同点 \(x,y\) 从未同处一条边，则把 \(y\) 合并到 \(x\)。合并映射在每条原边上单射，故保留 \(k\) 元性；去重只会减少边数。商超图的任意两色染色都可拉回原图，因此商仍不可染，却少一个顶点，与最小性矛盾。随后对实际有向顶点对作有限集合并集计数，即得不等式。Lean 声明为 `exists_pair_covering_counterexample`、`pairCovering_count` 和 `pairCovering_vertex_bound`，源码 `formal/Aris4Math/General/Structure/Reduction.lean`。∎

**引理2（同一反例上的单交团与有向计数）。** 对顶点集大小为 \(n\) 的有限简单 \(k\) 元超图 \(K\)，\(k\ge2\)，以实际原边为顶点，恰交一点的不同边相邻。令

\[
r(k,n)=\max\left\{k^2-k+1,\left\lfloor\frac{n-1}{k-1}\right\rfloor\right\}.
\]

则该图的每个团至多有 \(r(k,n)\) 个顶点。若 \(\gamma(K)\) 计实际**有向**单交边对，则

\[
\gamma(K)\le\left(1-\frac1{r(k,n)}\right)|K|^2.
\]

**证明。** 一个单交族若有公共点，删去公共点后各边两两不交，故族大小至多 \(\lfloor(n-1)/(k-1)\rfloor\)；若无公共点，经典线性交族计数给出 \(k^2-k+1\)。Lean 的 `singleGraph` 直接使用原边子类型。`singlePairsDartEquiv` 把实际 `singlePairs K` 与该图的 darts 建立显式双射，证明 `gamma_eq_twice_singleGraph_edges`，然后调用固定 Mathlib 的 Turán 定理。最终 `gamma_le_cliqueBudget` 从 uniformity 内部给出所需界。源码为 `formal/Aris4Math/General/Structure/Clique.lean` 和 `formal/Aris4Math/General/Structure/Turan.lean`。此处的标准 Turán 接口见锁定版本 Mathlib 的 `Mathlib/Combinatorics/SimpleGraph/Extremal/Turan.lean` 中 `CliqueFree.card_edgeFinset_le`、`mul_card_edgeFinset_turanGraph_le`；有向计数接口为 `Mathlib/Combinatorics/SimpleGraph/DegreeSum.lean` 中 `dart_card_eq_twice_card_edges`。∎

**引理3（同一个已接受参数的增长余量）。** 设整数 \(k\ge17\)、\(M\ge2^k\)，且定义2的接受不等式在参数 \(p\) 成立。置 \(s=s(k,M)\)。对每个满足

\[
n(n-1)\le k(k-1)(M+s)
\]

的自然数 \(n\)，都有

\[
r(k,n)>1,\qquad
(2+2\log k)s+2<\frac{M}{r(k,n)}.
\]

此外，同一参数满足

\[
-2\log k<\frac{M}{d_k}\log a_k(p).
\]

**证明。** `acceptedAt_parameter_control` 从实际接受不等式推出最后一个对数界。`pow_two_ge_fourth` 对自然数 \(k\ge16\) 归纳证明 \(k^4\le2^k\)，于是 \(\sqrt M\ge k^2\)、\(\sqrt M>8\)。由 \(\log k\le k-1\) 和下取整性质可得 \(s\ge1\)、\(s\le M\)，以及

\[
(2+2\log k)s\le\frac{\sqrt M}{4}.
\]

引理1的计数与 \(M+s\le2M\) 给出 \(r(k,n)\le2\sqrt M\)。因此

\[
(2+2\log k)s+2<\frac{\sqrt M}{2}\le\frac{M}{r(k,n)}.
\]

Lean 声明为 `integerGain_bounds`、`cliqueBudget_le_twice_sqrt`、`integerGain_log_slack`；源码为 `formal/Aris4Math/General/Growth/Elementary.lean`、`formal/Aris4Math/General/Growth/Slack.lean`。∎

**定理C的证明链。** 取 \(M=B_{\rm RS}(k)\)，使用最大预算内部提供的严格正参数 \(p\)。若目标边数范围内存在反例，引理1给出实际点对覆盖反例；引理2在同一个反例上削减 \(\gamma\)。引理3的严格余量与 `rs_increment_of_log_slack` 的对数增长估计，证明新增 \(s\) 条边的代价可由这一削减吸收。因此，沿用同一个 \(p\)，已经形式化的实际 RS 失败概率仍严格小于1，进而提取实际成功样本及原顶点集上的 Bool 染色，矛盾。结构入口为 `formal/Aris4Math/General/Structure/Main.lean`，增长装配为 `formal/Aris4Math/General/Growth/Main.lean`。∎

上述概率层复用已完成的 `formal/Aris4Math/General/RS/ProbabilityBound.lean`：共同初态／资格位／排列样本、实际失败覆盖、正关联、初始单色边平均、单交对精确积分及成功样本提取均在同一证明依赖链内。此次没有把这些结论重新作为未证概率前提。

## 核验：指定主构建与独立原题审计

|核验对象|实际结果|证据|
|---|---|---|
|结构主链 `Aris4Math.General.Structure.Main`|正规构建成功；独立原结构判据审计通过|`context/propertyb-general-lean-growth/structure/build04.log`、`context/propertyb-general-lean-growth/structure/audit02.log`|
|增长主链 `Aris4Math.General.Growth.Main`|正规 Lake 构建成功，2574 jobs；实际主定理已生成|`context/propertyb-general-lean-growth/build-main01.log`|
|构建后独立原题审计|`ReviewAuditGeneralGrowth.lean` 编译 exit 0，展开最大预算、原积分及 Bool 染色|`formal/ReviewAuditGeneralGrowth.lean`、`context/propertyb-general-lean-growth/final-audit01.log`|
|七项传递公理|均仅 `propext`、`Classical.choice`、`Quot.sound`|`context/propertyb-general-lean-growth/final-audit01.log`|

七项审计分别覆盖最大预算刻画、正参数见证、任意接受预算的增长调用、完整原超图增长定理、不可染边数下界，以及两项独立原题复述。没有 `sorryAx`、新增未证公理或 `native_decide`。2574 是 Lake 依赖任务计数，包含缓存与重放，不是新模块数。

以上证据属于本机正规构建与构建后独立导入，未声称第二台机器或他人已经复现。

## 复现：固定环境与精确入口

环境沿用 Lean 4.24.0。`formal/lean-toolchain` 与 `formal/lake-manifest.json` 固定依赖；Mathlib 提交为 `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`。

在项目根目录执行：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.General.Growth.Main
lake env lean ReviewAuditGeneralGrowth.lean
```

独立审计只导入实际增长主入口，并打印 `AcceptedAt`、`RSAccepts`、`rsBudget`、`integerGain`、`Uniform`、`PropertyB`、`Bichromatic` 的定义、原题声明和传递公理。默认 `lake build` 的旧主模块不能代替这里的指定增长入口。

## 与纸面证明的关系及审阅范围

本次形式化的是 `PROPERTY_B_GENERAL_BOUND.html` 中全部 \(k\ge17\) 的增长主定理C，保留相同 \(B_{\rm RS}\)、相同 \(\Delta(k)\) 及完整原超图量词。形式实现采用两处更短的论证：单交团只需公共点／无公共点二分所得的较弱统一界，省略纸面可用的 Gram 秩加强中间式；自然数范围的 \(2^k\ge k^4\) 使用从16开始的归纳，替代更强实变量估计中的导数论证。这两处简化足以推出同一个主定理。

比较定理D、E继续保留为已审阅的纸面结论，本次没有顺带完成它们的 Lean 形式化。原 RS 核心／17元试点报告 `PROPERTY_B_GENERAL_LEAN_PILOT.html` 和所有旧证据完整保留；旧35／36研究继续暂停，独立编码理论项目保持隔离。

结构链的 Grok 与 Gemini 审阅均已有效完成，在实际读取范围内未发现实质问题。两者静态读取六个新增 Structure 模块、独立原题审计及构建／公理日志；没有运行 Lean。实际返回分别为 `grok-4.7-build/xhigh`、`stopReason=end_turn`，以及 `gemini-4-argon-high/high`、`status=SUCCESS`。逐项处置见 `context/propertyb-general-lean-growth/reviews/structure/DISPOSITION.md`。

完整主定理C的 Gemini 终审已有效 `SUCCESS`，实际 CLI 选择为 `gemini-4-argon-high/high`，effort 来源为 `cli_selected_model_variant`。该审阅读取全部14个新增 Structure／Growth 模块、原题规格、独立审计及日志；既有 RS 底层算法／排列计数仅核导出接口，没有重跑 Lean，也没有审阅比较定理D／E。其结论为原量词、最大预算、正域 floor、同一个参数见证及原 Bool 染色均已接齐，未发现实质问题。原始回应见 `context/propertyb-general-lean-growth/reviews/final/gemini-RAW.json`。

完整主定理C的 Grok 指定终审也已有效完成，实际返回 `grok-4.7-build/xhigh`、`stopReason=end_turn`。它全文读取14个新增模块、独立原题复述、规格及构建／公理记录，既有 RS 概率核仅核所需接口，没有运行 Lean；独立反译全域最大预算、正整数增益及原超图染色后，未发现实质问题。两家最终原回应、准确范围及主代理处置见 `context/propertyb-general-lean-growth/reviews/final/DISPOSITION.md`。
