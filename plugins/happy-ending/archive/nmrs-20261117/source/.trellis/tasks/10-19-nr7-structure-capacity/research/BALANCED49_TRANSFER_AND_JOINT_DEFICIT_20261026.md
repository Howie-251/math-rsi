# balanced49 的 signotope 迁移、共同取等与 H–R 联合缺额

日期：2026-10-26。本文是主会话提供数学内容的新研究草稿，由 native Sol/high 文档执行代理忠实转写；执行代理仅核对文本、来源路径及文档一致性，不生成新数学，不作独立数学审查。用户明确要求本轮跳过 Claude，实际 reviewer calls 为 0。本文新增迁移判断、定理整理和条件推论均为 **unreviewed / unaccepted**；未编译 Lean，未回放有限证书，未改变任务指针、current R27、历史、acceptance 或运行。

当前 scoped 上界 `b=25` 已于 2026-10-26 由用户正式验收，限定模型域为完整有序 rank-3 signotope、no blue-5、no red-6、no weak-7；审查保证仍为 **same-family/provisional**，实际 reviewer backend/model 与 effort 未知或不可验证。依据为 [C8 正式人工验收记录](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)。R26/R27 等旧文中的 “b25 待验收” 是当时历史，本文不将其复制为当前状态。该接受不包含外部 balanced49，也不是一般几何 Erdős–Szekeres 界的验收。

## 1. 对 balanced49 可迁移性的当前回答

已检查的 balanced49 语义分支中，尚未发现一个必须依赖平面可实现性的本质步骤；但现有平面定理不能直接应用于任意 signotope。这里的结论是对已读语义链的迁移判断，仍有抽象适配、完整 imports、四份有限证书及字节绑定义务，不能写成已经证明并接受 `C_7^{sig}≤49`。

### 1.1 原定理的输入确实是真实平面点

[ES8BalancedGeometry.lean:7](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES8BalancedGeometry.lean) 中的输入为：

```lean
structure Configuration (n : Nat) where
  point : Fin n → Point
  xOrder : StrictMono (fun i => (point i).1)
  generalPosition : ∀ u v w : Fin n, u < v → v < w →
    orient (point u) (point v) (point w) ≠ 0
```

紧随其后的 `Configuration.cup` 由真实 orientation 的正号定义。任意 ordered signotope 并不自动提供这些实点及坐标；不得导入一个未经证明的 stretchability 假设。需要抽出原语义证明实际使用的组合接口，再给当前完整模型建立适配定理。

本项目已接受的 756 上界 25 可以替代外部 `restricted25`，从而绕过其无关的几何证明分支。替代输入后，剩余人口界及最终 closure 仍必须逐项建立抽象 soundness 和同一实际配置的 frame，不能把外部整个几何 theorem 当作黑箱调用。

### 1.2 最终调用链与共同赋值

原最终链为：

```text
ES7FinalVerified.balanced50_exclusion
  → ES7ClosureExistence.exists_frame
  → ES7ClosureData.impossible
```

具体见 [ES7FinalVerified.lean:8,16](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7FinalVerified.lean)、[ES7ClosureExistence.lean:5](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureExistence.lean) 与 [ES7ClosureData.lean:16](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureData.lean)。`balanced49` 由任意更大配置选取 50 点并调用排除定理得到；选点归约见 [ES7CapacityStage.lean:19](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7CapacityStage.lean)。

[ES7ClosureRules.lean](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureRules.lean) 的八类 schema 是 `base / ambient / core / low / counting / terminal / packet / prefix`。同一个实际模型所诱导的同一份 assignment 必须同时满足全部 clauses。为不同 clause 选择互不兼容的路径、状态或核心，不构成 soundness。

### 1.3 本次源码取得的证明力与缺口

[取得收据](../../../../tmp/balanced49_transfer_20261026/retrieval_receipt_network.json) 与 [带行号短接口摘录](../../../../tmp/balanced49_transfer_20261026/source_interfaces.txt) 记录了七个文件：`ES8BalancedGeometry`、`ES7Geometry`、`ES7Terminal20Data`、`ES7Through14Data`、`ES7Through14Literal`、`ES7Joint17Data`、`ES7ClosureData`。总解压文本 10,418,072 字节，HTTP 收到 1,640,083 字节，全部文件的 CRC32 及发布者清单 SHA256 匹配。既有 helper、索引和收据字节保持不变；首次网络受限的失败另保留在 [初次失败收据](../../../../tmp/balanced49_transfer_20261026/retrieval_receipt.json)。这些检查只建立来源字节身份，不建立语义迁移或证书正确性。

`Through14Literal` 已取得但未回放。另三份超出本次 8 MiB 单文件取得范围的 Literal payload 仍缺失：

| 文件 | 声明解压字节数 | 发布清单 SHA256；未下载验证 |
| --- | ---: | --- |
| `ES7ClosureLiteral.lean` | 732,220,946 | `0c4ddc5ab3aa65bed742b9f34d1bab65589e70c2108c21d5b935d9086a0f08ed` |
| `ES7Terminal20Literal.lean` | 30,001,637 | `31dd7141eb732644b4c47ac628f1732aa93307c92c0294eb1bc67d5278d35e32` |
| `ES7Joint17Literal.lean` | 38,734,663 | `22950a14595f72b93a769261738d029b2aa27d04aa27e1f44fa2dce77775da2a` |

四个有限证明对应 through14、terminal20、joint17、最终 closure。完整 source build、import closure、binder 检查、抽象 frame 建立及有限 LRAT 回放均未执行。发布者报告的最终 axioms 中含 19 个 native 项，是发布者报告，不是本项目的再现结果。

## 2. 完整模型与替代几何接口的组合引理

### 2.1 模型、路径及参数口径

令 `X` 是有限全序集，`χ` 是全部递增三元组上的完备二染色。对任意 `a<b<c<d`，按

\[
(\chi(abc),\chi(abd),\chi(acd),\chi(bcd))
\]

排列的 packet 至多变色一次。来源约定 `R=cup`、`B=cap`。路径以连续三元组都同色定义，长度是顶点数；两点路径对两色都真空成立。

`NoWeak_n(X)` 禁止具有同一对实际左右外端点的异色路径，其顶点长度和为 `n+2`，**没有内部不交假设**。由保持端点的子路径截短，它等价于每一对实际外端点上的两色最长路径长度之和至多 `n+1`。

记

\[
N^{\mathrm{sig}}(n,r,s)
\]

为同时 no `B_r`、no `R_s`、no weak `n` 的最大避免规模；它不是 forcing threshold。限制到实际子集、反序、全局换色均保持 packet，并按相应颜色和方向保持 weak/cap 条件。

### 2.2 链闭包：连续三元组已经迫使全部三元组同色

设 `v_1<⋯<v_m` 是颜色 `c` 的路径。证明其任意三元组均为 `c`，从而所有子序列仍是同色路径。

对 `m` 归纳。`m≤3` 直接成立。设 `m≥4`，归纳假设给出前 `m−1` 点的全部三元组为 `c`。对 `i<m−2`，四元包

\[
(v_i,v_{m-2},v_{m-1},v_m)
\]

的第一项由归纳假设为 `c`，最后一项由原路径为 `c`。一个至多变色一次且首尾同色的 packet 必须四项全同色，所以 `χ(v_i,v_{m-1},v_m)=c`。`i=m−2` 的对应结论正是原路径的最后一个连续三元组。

再对任意 `i<j<m−1` 使用 packet `(v_i,v_j,v_{m-1},v_m)`。首项由归纳假设为 `c`，末项由上一段为 `c`，因而 `χ(v_i,v_j,v_m)=c`。至此所有含末点的三元组也成立，归纳完成。

这给出了 `cup_list_all / chain3_all` 在完整 signotope 中需要的替代接口。后续跳点和拼接使用的是这个同色子序列性质，不需要斜率或实坐标。

### 2.3 同端点禁止与对称操作

原 [ES7OrderedPaths.lean:85](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedPaths.lean) 的 `weak_heptagon` 在 `a,b≥2`、`a+b=9` 时，经几何 heptagon 得到矛盾。当前模型可直接用 `NoWeak_7` 排除同一实际端点上的这两条路径，不需要凸包。

原 reflection 在抽象模型中以全局颜色互补替代。若最终 frame 要求首三元组为 `R`，先换色规范化，然后必须在新染色中重新选取**整个** starter core。只给原核心换名，不能保证它仍是所需颜色的全部实际 starter 集。

## 3. 假设映射与真实 rank/state

### 3.1 语义接口映射

下表只记录已读源位置及适配责任，不把源中平面型签名当成已经完成的抽象定理。

| 语义环节 | 已有源文件、行号 | signotope 对应与状态 |
| --- | --- | --- |
| 四元包 | [ES7PacketSemantics.lean:8,13,44](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7PacketSemantics.lean) | `fan_identity/fan/packet_clauses` 的所需布尔结论由 packet 公理承担；无需复制 orientation 恒等式 |
| 同实际端点的异色路径 | [ES7NamedGeometry.lean:179](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean)、[ES7OrderedContract.lean:154 的 weak 分支](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean) | 直接由 `NoWeak_7`；保留同一左右端点及长度条件 |
| 诱导选择与顺序重编号 | [ES7OrderedSelection.lean:7,24,29,43,53](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedSelection.lean) | 颜色限制与全序嵌入；来源中的几何 `noGon` 改用当前 `NoWeak` |
| 实际标签和 incoming state | [ES7ActualState.lean:11,15,24,33,42,51](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean) | 这些主干结论接受任意 `cup`，是路径递推的组合事实 |
| 有限前缀的真实最大秩 | [ES7FiniteRanks.lean:7,11,37,45](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7FiniteRanks.lean) | 在全部实际前驱上取递归最大值，不可只保留有利前驱 |
| 状态名字的 chronology 扩张 | [ES7JointRealization.lean:60,71,93,100,127](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7JointRealization.lean) | 实际状态严格包含与实际点序相容；未活跃名字补成线性扩张，不依赖 slopes |
| 不对称容量 25 | [本项目 C8 人工验收](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md) | 已接受的 scoped `b≤25` 替代发布者 `restricted25`；保留 provisional assurance |
| 人口 13 / 19 / 16 | [ThroughSelection:37,96](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ThroughSelection.lean)、[OrderedSelection:87](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedSelection.lean)、[JointPopulations:125,173](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7JointPopulations.lean) | 有具体实际人口接口；有限证书和抽象 binding 尚待闭合 |
| 最终 closure | [ClosureConstruction:208](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureConstruction.lean)、[ClosureRules](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureRules.lean)、[ClosureData:16](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureData.lean) | 同一真实 frame、全部变量及八类 clauses 的精确绑定仍待完成 |

### 3.2 标签分离与 chronology 的组合证明

对实际 `u<v`，令 `maxEnding_c(u,v)` 是最后两点为 `(u,v)` 的实际 `c` 色路径的最大顶点数，定义

\[
\operatorname{label}(u,v)=
(\operatorname{maxEnding}_R(u,v)-1,
 \operatorname{maxEnding}_B(u,v)-1).
\]

令 `D(v)` 是全部 `label(t,v)`（`t<v`）在正整数网格中的向下闭包。则

\[
\operatorname{label}(u,v)\in D(v)\setminus D(u).
\]

属于 `D(v)` 直接来自定义。若也属于 `D(u)`，就存在 `t<u`，使 `label(t,u)` 在两个坐标上支配 `label(u,v)`。三元组 `χ(t,u,v)` 总有一个颜色 `c`；取实现 `maxEnding_c(t,u)` 的实际最长链并追加 `v`，就得到以 `(u,v)` 为末对、更长一位的 `c` 链。因此 `label(u,v)` 的该坐标严格大于 `label(t,u)` 的该坐标，矛盾。

于是不同实际点的 `D(v)` 不同。若两个不同实际状态有 `D(u)⊂D(v)`，则不能 `v<u`，否则分离标签反证该包含；因此严格包含与实际 chronology 相容。未活跃状态名可以补入此偏序的线性扩张。此处保留的是原 ambient 配置的状态，不是在被选子集中重新计算出的 ambient 状态。

## 4. 四份有限排除所需的准确人口接口

### 4.1 Through14：14 个实际 through 点加两端真实供

选择 14 个实际 `R_5` through 点，再选最小 through 点的四个实际前驱与最大 through 点的四个实际后继，共 22 点。ambient ranks 继续指原配置；14 点核心自身的内部 ranks 单独重算。不能把一个 ambient attainment 冒充 14 点内部见证。

模型入口见 [ES7ThroughMeaning.lean:11](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ThroughMeaning.lean)，选点见 [ES7ThroughSelection.lean:37](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ThroughSelection.lean)，证书入口 [ES7Through14Data.lean:19](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7Through14Data.lean) 为：

```lean
theorem impossible (c : Configuration n) (f : Nat→Nat) (m : Model c f) : False
```

### 4.2 Terminal20：20 点内部核心加同一条真实四点后继

实际 20 点核心内部 no `B_5`、no `R_5`，其最大点是 ambient `R_5` 的实际起点。把这一个起点的同一条实际路径的四个后继接到核心后，得到 24 点配置，所有相应 ranks 在这 24 点中重算。

见 [ES7OrderedSelection.lean:87](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedSelection.lean) 和 [ES7OrderedContract.lean:136](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean)。[ES7Terminal20Data.lean:19](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7Terminal20Data.lean) 的准确入口是：

```lean
theorem impossible (c : Configuration 24) (hyp : Hypotheses c 20) : False
```

### 4.3 Joint17：当前顶层仍专用于 balanced50

当前 [ES7JointPopulations.lean:125](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7JointPopulations.lean) 的顶层 `joint_seventeen_impossible` 专用于 `Configuration 50`，带 `noSix/noGon`。它在 both-start 集 `L` 与 both-end 集 `Z` 都至少 17 时各选 17 点，使用 40 个 low/high ambient ideal 名字，首两个名字有 mandatory 条件。

[ES7Joint17Data.lean:16](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7Joint17Data.lean) 的底层入口是：

```lean
theorem impossible (m : Model c 40 ES7JointCatalog.states)
    (hyp : Hypotheses m) : False
```

不能只读到底层参数化签名，就宣称已得所有 `n`、所有缺额域中的普遍人口 16 定理。当前需要的接口应在确切取等域中重建。

### 4.4 Closure50：全部 25 个实际 starter 与共同尾巴

设 50 点配置 balanced。先使首三元组为 `R`，再重新选择 `K=全部实际 R_5 starters`；在取等域中 `|K|=25`。取 `max K` 的一条实际 `R_5` 路径的四点尾巴，得到共同的 29 点选择。

这 29 个实际点的名字使用 35 个 state catalog 名字加四个 tail 名字，活跃名字范围小于 39；部分中间模型使用 40 个 slots。标签继续保留原 50 点 ambient ranks。core/low 路径分别在自己的真实内部配置计算。全部颜色、owner、labels、内部见证、尾巴和计数共用同一实际配置。见 [ES7BalancedSelection.lean:14,28,75](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7BalancedSelection.lean)、[ES7ClosureConstruction.lean:51,110,184,208](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureConstruction.lean)。

`9≤t≤13` 与内部 `R_5` sources 至少 6 是通过前三个人口接口推导的结果；最终 mixed prefixes 不是额外自由假设。prefix 的精确递推只适用于所有相关 ambient 前驱均保留的那些位置，不能把任意选择后的前缀都当作原 ambient 前缀。

## 5. 参数化共同饱和：四个实际集合与精确单纯形

本节是 [R7 §4 近饱和人口式](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) 的精确 slack 整理，不是新的全局数值上界。

### 5.1 一般参数与相反 source/end 不交

设 `ℓ≥3`，balanced 配置 `X` 同时 no `R_{ℓ+1}`、no `B_{ℓ+1}`、no weak `n`。假设相关的两种不对称类——一色 no `ℓ`、另一色 no `ℓ+1` 且 no weak `n`——均有有效上界 `b`，换色也成立。

设 `M=|X|`，`S_c/E_c` 分别为 ambient 的实际 `c` 色 `ℓ` 路径起点、末点集，并令

\[
d=2b-M.
\]

相反两色满足

\[
S_R\cap E_B=\varnothing,
\qquad S_B\cap E_R=\varnothing.
\]

例如若 `v∈E_B∩S_R`，取终到 `v` 的 `B_ℓ` 与始于 `v` 的 `R_ℓ`。设入链末前驱为 `u`、出链第二点为 `w`。若 `χ(u,v,w)=B`，入链接 `w` 得 `B_{ℓ+1}`；若为 `R`，`u` 前接出链得 `R_{ℓ+1}`。另一对换色同理。

### 5.2 四个人口界与两条精确恒等式

`S_R` 内部不能有 `B_ℓ`：其末点仍有 ambient `R_ℓ` 出链，在连接处一色延长入链，另一色延长出链，均违反 balanced。`X\S_R` 内没有 `R_ℓ`，因为任何该路径的起点按定义应在 `S_R`。因此这两个实际配置各属于相应不对称类，规模都至多 `b`。换色、反序给出其余三组，故

\[
M-b\le |S_c|,|E_c|\le b,
\qquad d\ge0.
\]

定义非负 slack：

\[
a_c=|S_c|-(M-b),\qquad
e_c=|E_c|-(M-b),
\]

\[
z_R=|X\setminus(S_R\cup E_B)|,\qquad
z_B=|X\setminus(S_B\cup E_R)|.
\]

利用相反 source/end 不交，准确得到

\[
\boxed{a_R+e_B+z_R=d},\qquad
\boxed{a_B+e_R+z_B=d}.
\]

例如第一式左侧等于 `|S_R|+|E_B|−2(M−b)+M−|S_R|−|E_B|=2b−M`。每一项都是同一个实际 `X` 的非负整数。

### 5.3 缺额零与缺额一

若 `d=0`，两式迫使

\[
S_R=X\setminus E_B,
\qquad S_B=X\setminus E_R.
\]

四个实际集合

\[
L=S_R\cap S_B,\quad
T_R=S_R\cap E_R,\quad
T_B=S_B\cap E_B,\quad
Z=E_R\cap E_B
\]

互斥并覆盖 `X`。每个 source/end 集大小均为 `b`，因此存在 `t` 使

\[
|T_R|=|T_B|=t,
\qquad |L|=|Z|=b-t.
\]

若 `d=1`，每一对相反集合的 slack 三元组恰为

\[
(a,e,z)\in\{(1,0,0),(0,1,0),(0,0,1)\}.
\]

用相应的两个补核心表述，就是规模 `(b−1,b)` 且不交、规模 `(b,b−1)` 且不交，或规模 `(b,b)` 且交一实际点。因而不能说任意 49 点 balanced 都有两个不交的 25 点核心。

### 5.4 人口输入如何进入同一取等域

在上述 `d=0` 取等域中，若 through 人口界 `t≤α` 和 `min(|L|,|Z|)≤γ` 都有效，则

\[
b-\gamma\le t\le\alpha.
\]

若 terminal 核心界 `β` 适用于实际 `K=S_R`，从 `K` 删除全部内部 `R_ℓ` sources `I(K)`。余下配置无内部 `R_ℓ`，并继承 `K` 无 `B_ℓ`；若余下非空，其最大点仍是原 ambient `R_ℓ` starter。故 terminal 接口给出 `|K\I(K)|≤β`，从而

\[
|I(K)|\ge b-\beta.
\]

只有在人口迁移及其确切取等域 binding 成功后，才可代入

\[
b=25,\quad\alpha=13,\quad\gamma=16,\quad\beta=19
\]

得到

\[
9\le t\le13,\qquad |I(K)|\ge6.
\]

这些数值本身没有矛盾：区间非空。最终共同 closure 排除仍是必需步骤。

## 6. 实际内禀覆盖上的联合缺额定理

本节以参数为先，重写 [R26 §2 的实际批量覆盖](RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md)，同时加入一个有效 balanced 界 `c`。没有把原 X80 的所有取等式直接替换成 X79。

### 6.1 参数、实际锁定族与两个配置

设 `n≥6`，`b` 是 `N^{sig}(n,n−2,n−1)` 及换色类的有效上界，`c≤2b` 是 balanced 类

\[
C_n^{\mathrm{sig}}=N^{\mathrm{sig}}(n,n-1,n-1)
\]

的有效上界。`D_n` 为 [R7 §3.2](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) 的残余类：no `B_{n−2}`、no weak `n`，内部不存在同时是 `R_{n−2}` 终点和 `B_{n−3}` 起点的 junction。

假设每个 `D_n` 配置的全部实际 `R_{n−1}` 路径都有一个规模至多 `q` 的横截集。这里 `q=5` 只在 `n=7` 由 R7 的五点横截使用，不推广为任意 `n` 的已知数值。

任取无 `B_{n−1}`、无 `R_n`、无 weak `n` 的实际配置 `X`，其容量记为

\[
Q_n^{\mathrm{sig}}=N^{\mathrm{sig}}(n,n-1,n).
\]

定义

\[
S=\operatorname{Src}_{R_{n-1}}(X),\qquad H_0=X\setminus S.
\]

对 `s∈S∩Src_{B_{n−2}}(X)`，令 `T(s)` 为从 `s` 出发的**全部**实际 `R_{n−1}` 终点，`Q(s)` 为从 `s` 出发的**全部**实际 `B_{n−2}` 第二点。定义

\[
F=\{s:T(s)\cup Q(s)=\{o(s)\}\},\qquad
O=o(F),\quad O_H=O\setminus S,\quad O_S=O\cap S.
\]

全部替代见证均参与此定义。`o(s)` 是唯一实际出口，不是为每个 owner 随便选择的一个出口。取

\[
K=(H_0\setminus O_H)\cup F,
\qquad D=S\setminus O_S.
\]

### 6.2 `K` balanced，且每个不同出口给一个 neutral

任何实际 `R_{n−1}` 的终点都不能启动 `B_{n−2}`。在入链末前驱、共同点、出链第二点组成的 joining 三元组处，红会延长为 `R_n`，蓝会延长为 `B_{n−1}`。因此 `F∩O=∅`。同一 joining 也说明 `S` 内部无 `B_{n−2}`：取该蓝链末点的 ambient `R_{n−1}` 出链即可。

`K` 内部无 `R_{n−1}`。如果起点在 `H_0`，与其没有 ambient `R_{n−1}` 出链矛盾；如果起点在 `F`，其唯一允许终点是已经在 `K` 外的 `o(s)`。`B_{n−1}` 与 weak `n` 从 `X` 遗传，所以 `K` balanced。

对每个不同 `o∈O`，在纤维 `o^{-1}(o)∩F` 选择最早实际点 `c_o`。其所有 `B_{n−2}` 第二点都是 `K` 外的 `o`，因此 `c_o` 不是 `K` 内部 `B_{n−2}` 起点。

若内部有 `R_{n−2}` 链终于 `c_o`，设末前驱为 `u`，取 ambient `B_{n−2}(c_o,o,…)`。`χ(u,c_o,o)` 不能为蓝，否则 `u` 前接该链得到 `B_{n−1}`；因此为红。将原入链后接 `o` 得到实际 ambient `R_{n−1}`。其首点若在 `H_0`，违反 ambient 无源；若在 `F`，它属于同一出口纤维且严格早于 `c_o`，违反最早性。因此 `c_o` 也不是内部 `R_{n−2}` 终点。

不同出口对应不同代表。令

\[
\operatorname{Neutral}(K)=K\setminus
(\operatorname{Src}_{B_{n-2}}(K)\cup\operatorname{End}_{R_{n-2}}(K)).
\]

上述两个 source/end 集在 balanced `K` 中不交，否则 joining 给 `B_{n−1}` 或 `R_{n−1}`。它们的两个补集均属于相应不对称容量类，所以

\[
|K|+|\operatorname{Neutral}(K)|\le2b,
\qquad |\operatorname{Neutral}(K)|\ge|O|.
\]

因此

\[
\boxed{|K|+|O|\le2b}.
\]

这里只按每个不同出口得到一个 neutral；没有声称 `F` 的所有点都 neutral。

### 6.3 `D` 满足完整残余条件

`D` 继承 `S` 内无 `B_{n−2}`，并继承 no weak `n`。反设其内部有 `R_{n−2}` 终于 `v`，且有 `B_{n−3}` 路径 `(v,x,…,w)`。因 `w∈D⊆S`，取其 ambient `R_{n−1}` 出链 `(w,z,…)`。

设蓝路径末前驱为 `y`。`χ(y,w,z)` 若红，则 `y` 前接 ambient 红链得到 `R_n`，故为蓝。原蓝链追加 `z` 成为 ambient `B_{n−2}`，其首对仍为 `(v,x)`。

此时 `v` 同时具有 ambient `R_{n−1}` 出、`R_{n−2}` 入和 `B_{n−2}` 出。R7 §3.1 的三链桥接对任意不同的红终点和蓝第二点给矛盾，所以全部这些终点和第二点必须是同一实际点，亦即 `v∈F` 且 `x=o(v)`。但 `x∈D⊆S` 又迫 `x∈O_S`，与 `D=S\O_S` 矛盾。因此 `D` 确属所需残余类。

### 6.4 精确覆盖与共同缺额恒等式

实际集合关系是

\[
K\cap D=F,\qquad K\cup D=X\setminus O,
\]

所以

\[
\boxed{|X|=|K|+|D|+|O|-|F|}.
\]

令

\[
f=|F|,\quad o=|O|,\quad s=2b-c\ge0,
\quad\kappa=c-|K|\ge0.
\]

取命中 `D` 中全部实际 `R_{n−1}` 路径的**最小**横截集 `T`，令 `τ=|T|≤q`，`Y=D\T`。`Y` 属于相应不对称类，故 `|Y|≤b`，并且 `|D|=τ+|Y|`。

设联合缺额

\[
\Delta=c+b+q-|X|.
\]

把实际覆盖式逐项代入，得到

\[
\boxed{\Delta=
\kappa+(q-\tau)+(b-|Y|)+(f-o)}.
\]

四项都非负：前三项来自有效容量及横截界，最后一项来自像集大小 `o≤f`。此外 neutral 预算给

\[
o\le2b-|K|=s+\kappa.
\]

因此

\[
|X|\le c+b+q,
\qquad
\boxed{f\le s+\Delta-[(q-\tau)+(b-|Y|)]}.
\]

后式由 `f=o+Δ−κ−(q−τ)−(b−|Y|)` 与 `o≤s+κ` 相消得到；不能在另一处重复收取同一 `F` 的费用。

### 6.5 联合取等迫使同一满核心与私人横截见证

当 `Δ=0` 时，每一非负项均为零，故

\[
|K|=c,\qquad\tau=q,\qquad |Y|=b,
\qquad f=o\le s.
\]

任意一个规模为 `q` 的最小横截集都给出实际的满 `b` 核心 `Y=D\T`。对每个 `t∈T`，最小性保证存在实际 `R_{n−1}` 路径 `P_t`，满足

\[
V(P_t)\cap T=\{t\}.
\]

否则删去 `t` 后仍为横截集，违最小性。因此每条 `P_t` 的其余 `n−2` 个点均在**同一个** `Y` 中。各 `t` 是对应私人见证的核外点，内部路径见证允许相互重叠。这是共同实际见证条件，不是 `q` 个互不关联的容量陈述。

此外 `D⊆S`，所以同一满核心 `Y=D\T` 的每个点，乃至 `D` 的每个点，都仍启动一条实际 ambient `R_{n−1}` 路径。上述 `q` 条私人路径 `P_t` 位于 `D` 内；这些 ambient 后续路径不必位于 `D`，也不必有共同终点。七点临界情形的实际共同对象因此是：25 点满核、五个私人 `R_6` 扩展，以及从每个核心点启动的 ambient `R_6` 后续路径，全部嵌在同一个 `X`。

若 `c=2b−1`，则 `s=1`，联合取等时 `f=o∈{0,1}`。`F` 空则 `O` 空；`F` 单点则只有一个出口和一次修正。没有包含至少两个锁定 owner 的分支，也没有多个 owner 共用同一个出口的取等分支。反序给另一个独立结论，不把两方向费用相加。

### 6.6 条件 `b=25,c=49,q=5` 下的 X79 实际三分支

在 balanced49 完整迁移成立的条件下，假设实际 `|X|=79`，则

\[
|K|=49,\qquad |D|=30,\qquad |Y|=25,\qquad\tau=5,
\qquad f=o\in\{0,1\}.
\]

若 `F={v_*}`、`O={z_*}`，纤维证明给 `|Neutral(K)|≥1`，而 `|K|+|Neutral(K)|≤50` 给反向不等式，所以准确有

\[
\operatorname{Neutral}(K)=\{v_*\}.
\]

于是

\[
K\setminus\operatorname{Src}_{B_5}(K),\qquad
K\setminus\operatorname{End}_{R_5}(K)
\]

是两个实际 25 点核心，其交集恰为 `{v_*}`；对应的 `Src_{B_5}(K)` 与 `End_{R_5}(K)` 各有 24 点。此处只固定 `Src_{B_5}/End_{R_5}` 这一对方向；一般单纯形分别作用于每一对相反 source/end，不能据此同时固定另一对。这个 singleton 分支比一般 49 点配置强：一般的 one-deficit 单纯形仍允许 24 点与 25 点两个不交核心。

因为 `D=S\O_S` 且 `|D|=30`，有 `|S|=30+|O_S|`。三个内禀分支为：

| 锁定与出口位置 | 实际人口 | 实际 `K` |
| --- | --- | --- |
| `F=∅` | `|S|=30, |H_0|=49` | `K=H_0, D=S` |
| `F={v_*}, z_*∈H_0` | `|S|=30, |H_0|=49` | `K=(H_0\{z_*})∪{v_*}` |
| `F={v_*}, z_*∈S` | `|S|=31, |H_0|=48` | `K=H_0∪{v_*}` |

反序可分别得到 ambient `R_6` 终点人口为 30 或 31；不能把源与终的两个费用直接相加。这是必要的共同饱和分类，既不是存在构造，也不是矛盾。

## 7. canonical H–R 的同一次操作强化

### 7.1 实际操作前提与集合

采用 [R7 的 canonical 分解](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) 及 [R26 §4 的共同替换](RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md)。设同一实际 `X=H⊔R` 满足：`H` balanced；`H` 端封闭，即没有 ambient `R_{n−1}` 路径的两个实际外端点都落在 `H`，其内部允许离开 `H`；每个 `H` 中 ambient `R_{n−1}` source 都有实际 ambient `R_{n−2}` 入链及 `B_{n−2}` 出链。canonical `R` 为相应实际残余类。不能把这些 ambient 供应改写成 `H` 内部供应。

定义

\[
S_R=R\cap\operatorname{Src}_{R_{n-1}}(X),
\]

\[
W=R\cap\{\text{H-origin ambient }R_{n-1}\text{ 的实际终点}\},
\qquad U=R\setminus(W\cup S_R).
\]

取全部 `F∩R`，或其任意实际子集 `A⊆F∩R`，并设

\[
Z=o(A)\cap(H\cup U),\qquad
E=o(A)\cap(S_R\setminus W),
\]

\[
a=|A|,\quad u=|U|,\quad w=|W|,\quad z=|Z|,\quad e=|E|.
\]

使用同一次实际配置

\[
K_A=((H\cup U)\setminus Z)\cup A.
\]

### 7.2 全部实际替换义务与共同 neutral

`K_A` 中的 `R_{n−1}` 必须按实际起终点逐支排除：`H→H` 违反端封闭；`H→U` 违反 `W` 定义；`U` 中没有 ambient `R_{n−1}` source；`H→A` 不可能，因为 `A` 为 `B_{n−2}` source，而 `R_{n−1}` 终点不能启动该蓝链；`A` 出发只能到唯一出口，该出口已删除或在 `K_A` 外，并且不在 `A`。`B_{n−1}` 与 weak 从 `X` 遗传，因此 `K_A` balanced。

对 `W∪o(A)` 中的每个不同出口，在“所有到该出口的 H-origin `R_{n−1}` 实际源”与“A 中映到该出口的实际源”这个共同候选集内，选最早代表。H 候选利用既有入红、出蓝和 R7 三链，迫使其全部 `B_{n−2}` 第二点等于该出口；A 候选由锁定定义得到相同结论。

这些代表自身是 `B_{n−2}` source，故不能成为任何 `R_{n−1}` 终点，也不会在删去的 `Z` 中。对应出口位于 `K_A` 外，所以代表无内部 `B_{n−2}` 出链。若有内部 `R_{n−2}` 入链，joining 不能蓝，否则得 `B_{n−1}`；红则追加出口，得到同终点、更早起点的 ambient `R_{n−1}`。首点在 `H` 或 `A`，就属于共同候选集而违最早性；在 `U`，则违反 ambient 无源。

不同出口代表不同；`W` 与 `o(A)` 重合时只取一次，不能双计。于是同一次 `K_A` 满足

\[
|\operatorname{Neutral}(K_A)|\ge|W\cup o(A)|=w+z+e.
\]

这正是可以共同使用两个容量式的实际操作前提，不是把各自成立的独立不等式相加。

### 7.3 同一缺额上的代数强化

令

\[
h=|H|,\qquad\delta_H=c-h,\qquad s=2b-c.
\]

实际操作的规模是

\[
|K_A|=h+u-z+a.
\]

由 `|K_A|≤c` 得 `δ_H≥a+u−z`。另一方面，同一 neutral 预算给

\[
h+u-z+a+w+z+e\le2b=c+s,
\]

所以 `δ_H≥a+u+w+e−s`。连同 `δ_H≥0`，得到

\[
\boxed{\delta_H\ge
\max\{0,a+u-z,\ a+u+w+e-s\}}.
\]

若在实际 `R` 中取最小横截集 `T_R`，记 `τ_R=|T_R|≤q`、`Y_R=R\T_R` 且 `|Y_R|≤b`，则

\[
c+b+q-|X|=\delta_H+(q-\tau_R)+(b-|Y_R|)
\]

进而

\[
\boxed{c+b+q-|X|\ge
(q-\tau_R)+(b-|Y_R|)
+\max\{0,a+u-z,\ a+u+w+e-s\}}.
\]

各项来自同一个 `H⊔R` 和同一次 `K_A`，不是不同分解给出的独立节省。

### 7.4 联合取等、`s=1` 的两个 canonical 分支

设 `Δ=0`、`s=1`。由 `z≤a`，第一支 `a+u−z≤0` 迫使 `u=0,z=a`；第二支给

\[
a+w+e\le1.
\]

若 `A=∅`，则 `z=e=0`，所以 `|W|≤1`。若 `A` 单点，则 `z=1,w=e=0`；此时 `U=∅`，唯一出口落在 `H` 中。故两个必要分支为：

1. `A=∅` 且 `|W|≤1`；
2. `|A|=1`、唯一出口在 `H`、`W=∅`。

所有集合都来自同一个实际 `X`。这只是必要分支分类，没有矛盾。反序得到另一个单独的分类，不能把两方向以及 §6 的 `F` 费用再次相加。

## 8. 数值口径与为什么必须重基准到 79

先保留参数式，再代数值。当前已接受的输入是 scoped `b=25`；旧 [R7](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) 与 [R20](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) 的研究草稿链给出的当前完整模型上界为

\[
C_7^{\mathrm{sig}}\le50,\qquad
Q_7^{\mathrm{sig}}\le80,\qquad
N^{\mathrm{sig}}(7,7,7)\le81.
\]

本文不把这些旧迁移草稿重新称为新增正式接受。只有在 balanced49 的抽象适配、有限证明和共同 binding 全部闭合后，`c=49` 才是有效输入，届时上述参数定理给

\[
Q_7^{\mathrm{sig}}\le49+25+5=79,
\qquad N^{\mathrm{sig}}(7,7,7)\le80.
\]

这里仍是最大避免规模。经既有 projective/root 几何归约所对应的 forcing 上界为 **81**，不是 80。原几何接口见 [ES7ProjectiveTransfer.lean:79,140](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ProjectiveTransfer.lean)、[ES7CapacityStage.lean:45](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7CapacityStage.lean)，研究侧旧衔接见 R20。

若要将几何 forcing 上界推进到 80，需要 `Q_7^{sig}≤78`，或 balanced `C_7^{sig}≤48`，或一个额外且统一有效的联合净缺额。本文的新参数定理尚未证明这种普遍正的 `Δ`，所以不发布新的 accepted 数值界。

原 primitive50/80 分析必须重基准：假想 79 点配置允许一单位 balanced 缺额，并允许 0/1 锁定 owner。X80 所迫的旧零缺额、空锁定族等式不能直接代换成 X79。应使用 §6 的三分支与 §7 的两种 canonical 形态，保留同一实际满 25 核心、五条私人 `R_6` 见证及真实跨 H/R 路径。

## 9. 后续方向：可核验门槛与停止条件

### P0. 先闭合 fixed-byte 抽象证书适配

抽出小而必要的语义接口，以本项目已接受 b25 替换外部 restricted25；保持原 CNF、变量映射、source checks 和有限 LRAT 绑定。四个 Models 都必须映入同一实际 `χ`，并保留 ambient labels、内部 ranks、真实 owner、共同路径和同一尾巴。

完整 import closure、binder 检查、编译和回放应作为受控 Linux 工作执行；本文没有执行，也未改变接受状态。除非绑定失败暴露必须重建的对象，不先启动新搜索。门槛是四个实际适配和有限证明闭合，接受仍需明确办理，不能从源码哈希匹配自动升级。

### P1. 直接攻击共同极值目标

在 `c=49` 条件闭合后，联合排除同一 `X` 中的 `K49 + D30 + 同一个25核心 + 五条私人R6见证 + 每个核心点的ambient R6后续路径 + 0/1出口`，或直接证明 `Δ≥1`。这些 ambient 后续路径不强加共同终点，也不冒充 `D` 内部 attainment。优先只按 §6 三种内禀出口位置及 §7 两种 canonical 分支划分，不扩张任意人口网格。

若新不等式只是独立计数，或者为了得到它付出的删除/补点恰消耗全部收益，则停止该推进，不将其记作净改进。

### P2. 富 H 条件下的四横截或 tradeoff

研究 `H49` 成立时是否有条件 `τ(R)≤4`，或 `τ(R)=5` 是否迫使 `|H|≤48`。必须使用真实跨 H/R 路径以及 R7 fan 端点不等式 `a+b≤n−1`。不声称一般残余 `D` 都有四点横截。

R7 的 single-extender 反例已说明仅凭 fiber 数不足以得到所需横截结论。若较弱接口出现实际反例，应修正前提，不能忽略反例或将它排成人为例外。

### P3. 一缺额下的四核心共同分类

用 §5 的 one-deficit 单纯形同时细化四个核心，研究这些核心能否共同嵌入所需残余。先区分保留的 ambient incoming labels 与内部 attainment，再寻求一次真正共享的实际操作。一般 49 点的 24+25 不交核心分支，与 §6 singleton 强迫的两个 25 核交一点分支，不能混用。

若分类仍只得到独立人口界，或没有覆盖全部实际分支，便不足以推出新数值。只有完整覆盖所有情形并给出真实净缺额，才进入新的数值主张。

当前明确开放的目标是：**balanced49 迁移闭合之后，共同排除 §6.6 的全部三个内禀分支，从而证明 `Q_7^{sig}≤78`。** 本文未完成这一步。

## 附录：主要本地来源与外部发布入口

| 角色 | 本地主要来源 |
| --- | --- |
| scoped b25 当前正式状态 | [c8-formal-acceptance-20261026.md](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md) |
| 完整 signotope 三链、残余、五横截、近饱和 | [RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) |
| 全局旧衔接和 canonical H–R 前提 | [RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) |
| 内禀 K/D 覆盖与共同最早代表操作 | [RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md](RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md)；其 b25 待验收文字保留为历史 |
| 来源比较上下文 | [R20_NOVELTY_COMPARISON_20261023.md](R20_NOVELTY_COMPARISON_20261023.md) |
| ZIP 中央目录和原始来源清单 | [central_index.json](../../../../tmp/schroeder_comparison_20261021/selected_sources/central_index.json)、[formal/MANIFEST.json](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/MANIFEST.json) |
| 本次七文件身份核对与遗漏义务 | [retrieval_receipt_network.json](../../../../tmp/balanced49_transfer_20261026/retrieval_receipt_network.json)、[source_interfaces.txt](../../../../tmp/balanced49_transfer_20261026/source_interfaces.txt) |
| Through14 已取得的有限证明文本 | [ES7Through14Literal.lean](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7Through14Literal.lean)；未编译、未回放 |
| 来源几何解释接口 | [ES7Geometry.lean](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7Geometry.lean)、[ES8BalancedGeometry.lean](../../../../tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES8BalancedGeometry.lean) |

发布者外部入口为 [Erdős–Szekeres companion](https://michaelschroeder.ai/research/ErdosSzekeres/companion) 与 [Zenodo DOI 10.5281/zenodo.22842891](https://doi.org/10.5281/zenodo.22842891)。下载原 URL、每次 HTTP 范围、CRC32、SHA256、未取得文件的清单声明哈希均见取得收据。发布者的 native/final axiom 计数和构建报告仍只作发布者报告；本文没有把它们改写成本项目的再现或正式接受证据。
