# 给查验者的交接：五元超图的 Property B 下界

交接日期：2026-10-06。项目：aris4math。

本项目提交的结论是 **m(5) ≥ 33**。目前已有完整书面证明、Lean 主定理，以及本机成功构建和公理核查记录。请独立检查下述命题、证明和形式化的对应关系；希望获得的是你自己的数学判断与复现结果。此前代理和模型的结论不作为你的推理前提。

## 1. 要查验的原命题

设 $V$ 为任意有限集合，$E\subseteq\binom V5$，且 $|E|\le32$。需要证明存在染色 $c:V\to\{0,1\}$，使

\[
\forall e\in E,\qquad 1\le\sum_{x\in e}c(x)\le4.
\]

即每条边同时包含两种颜色。边是五个不同顶点组成的集合，边集无重复；允许孤立顶点和空边集。没有预设顶点数、点对覆盖、正则性或两色人数均衡。

按 $m(5)$ 为不可二染色的有限简单五元超图最少边数的定义，这等价于 $m(5)\ge33$。本次没有提交 $m(5)=33$ 或33边反例构造。

**对象、量词和目标以 [FORMAL_SPEC.md](FORMAL_SPEC.md) 的 D1–D3、T 为准。** 原任务书 [ar4math_propertyb.pdf](ar4math_propertyb.pdf) 是路线来源；最终证明请看下面的单卷阅读版。

## 2. 推荐阅读顺序

| 顺序 | 文件 | 用途 |
|---|---|---|
|1|[PROOF_PACKAGE.html](PROOF_PACKAGE.html)|完整证明阅读入口；规格、三份引理、分类、严格界和 Lean 核验已内联，公式可离线阅读|
|2|[FORMAL_SPEC.md](FORMAL_SPEC.md)|单独核对原命题；重点看 T、R1–R4、F、M1–M3 和 LOCK 的量词|
|3|[formal/ReviewAudit.lean](formal/ReviewAudit.lean)|用原始边集重新写出命题，打印定义、主定理和传递公理|
|4|[formal/Aris4Math/Main.lean](formal/Aris4Math/Main.lean)|53行的主定理入口；查看七个分支怎样接回任意有限超图|
|5|[context/FORMAL_VERIFICATION_PROGRESS.md](context/FORMAL_VERIFICATION_PROGRESS.md)|数学义务、Lean 模块、已有构建证据的对应关系|

HTML 共八章：规格与约化、概率引理 P1–P9、19–23点结构、24–25点结构、主定理闭合、Lean 核验、逐位置精确算术、来源与辅助复算。第七章包含23组配置、534行逐位置有理数；其中21组成功，另外两组作为不成功配置保留，并说明证明如何处理它们。

数学规范源为 `FORMAL_SPEC.md`、`proofs/` 中三份文件，以及 `PROOF_PACKAGE.md` 中的汇总表。[PROOF_PACKAGE_FULL.md](PROOF_PACKAGE_FULL.md) 是合成阅读稿。若发现纸面问题，请同时指出原引理位置，不只引用生成的 HTML 行号。

## 3. 证明主线与值得重点核对的位置

总体路线是：任意反例 → 最小顶点反例 → 19–25点、恰32边、覆盖点对 → 选取锁点与固定位置 → 条件排列中的贪心染色 → 失败概率严格小于1 → 原超图可染。

| 数学环节 | 请核对的实质问题 | 主要文件 |
|---|---|---|
|一般约化|合并不共边点后仍为五元边、去重不增边数；染色可拉回；补边保持反例性质；≤18点和≥26点的排除确实覆盖全部范围|`FORMAL_SPEC.md`；`Reduction.lean`、`SmallVertices.lean`、`Structure.lean`|
|概率对象|锁点和位置先于剩余随机排列选定，只固定位置；条件空间非空；失败确实被单交有序 critical pair 事件覆盖|`proofs/PROBABILITY_LEMMAS.md` P1；`Greedy.lean`、`Counting.lean`|
|无放回计数|自由/锁定中心分开；左右占位用联合条件计数；分母、可行域和零权重正确；固定单交边对没有多乘端点选择因子|P2–P5；`JointCounting.lean`、`EndpointCounting.lean`、`CriticalCounting.lean`|
|22/23点扣除|实际坏边对数量、双方向权重、同位置去重都得到证明；23点三锁最后中心的零权重例外至多一对；先在 C 项内扣除，再取三项最小值|P6–P9；`LinkDeletion.lean`、`LinkWeightCertificates.lean`、`TwentyTwo.lean`、`TwentyThree.lean`|
|选点与真实类型|22点66/67/77、23点66/677覆盖所有输入；表中重数来自实际边集；三锁无共同边的条件由选点提供|`proofs/STRUCTURE_19_23.md`；`LowDegree.lean`、`DoubleTripleLockProfiles.lean`、`TripleLockProfiles.lean`|
|24/25点分类|四锁三型、六锁九型的分类穷尽性有解析证明；七点论证保证避开不成功的六点型；同构标签可以对应到实际锁点|`proofs/STRUCTURE_24_25.md`；`BlockClassification.lean`、`K6Classification.lean`、`K6Traces.lean`、`LargeVertices.lean`|
|数值到原结论|真实条件事件与数值公式一致；严格界推出成功排列；成功染色满足原 Property B 定义；顶层无残留假设|`ProfileProbability.lean`、`ProfileApplication.lean`、`Greedy.lean`、`Main.lean`|

表内 `.lean` 文件均位于 `formal/Aris4Math/`。最紧的成功配置是23点677三锁，总界为 $645/646<1$，可优先手算这一分支。

纸面允许25点的八种成功六锁类型；Lean 的实际选择路线得到更强的限制，只需其中七种。核对时应比较各自选择定理的覆盖范围，不要求两条实现使用完全相同的中间分类列表。

全部超图、染色或排列的穷举不是本证明的前提。解析分类证明覆盖，Lean 内核计算处理明确的有限类型数据和有理数公式。此前整图搜索未发现反例，只是探索记录。独立发现并验证一个符合原定义的反例，就足以否定目标，不能以既有审阅意见排斥它。

## 4. 在你自己的机器上复现 Lean

### 环境与版本

解压 `aris4math_review_bundle.zip`，进入其中的 `aris4math_review/`。先安装 Lean/elan 并保证 `elan`、`lake` 在终端 PATH 中，可按 [Lean 官方安装说明](https://lean-lang.org/install/) 完成。建议用 VS Code 打开包内的 `formal/` 文件夹。

- Lean：`leanprover/lean4:v4.24.0`，由 `formal/lean-toolchain` 指定。
- Mathlib：v4.24.0，对应提交 `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`。
- 所有依赖的实际版本由 `formal/lake-manifest.json` 固定；复现时保留该文件，不运行 `lake update` 改动依赖版本。
- 项目证明源码为39个文件、9,100行，含空行和注释；不含 Mathlib。另附一个独立审计入口 `ReviewAudit.lean`。

### 构建和审计命令

从解压后的项目根目录运行：

```sh
cd formal
lean --version
lake exe cache get
lake build Aris4Math.Main
lake env lean ReviewAudit.lean
```

第一行版本输出应为 Lean 4.24.0。`cache get` 下载依赖的预编译缓存；包内没有本项目的 `.olean` 或 `.lake/build`，首次构建需要从所交付源码生成项目证明。默认 `lake build` 的目标也已设为 `Aris4Math.Main`。

如果复用一个已有构建产物的目录，并希望强制重建本项目，可以在 `formal/` 中运行：

```sh
lake clean aris4math
lake build Aris4Math.Main
lake env lean ReviewAudit.lean
```

指定包名的 `clean` 只清理本项目构建目录，保留下载的依赖。无需照搬历史 README 中作者机器的 `/Users/.../.tools/elan` 路径；压缩包不携带工具链二进制或依赖缓存。原始模型报告中的作者绝对路径仅为历史记录，可按包内对应的相对目录查找。首次取工具链和依赖需要联网，下载失败应单独记录为环境问题。

### 应当看到的结果

构建与审计命令均应以退出码0结束。审计会展示：

1. `Simple5Hypergraph`：`Finset (Finset V)`，每条边恰有5个顶点。
2. `PropertyB`：存在布尔染色，每条边的 true 顶点数介于1与4。
3. `Target`：任意有限顶点类型、边数至多32，没有其他结构前提。
4. 三个原主声明和 `ReviewAudit.original_statement` 的实际类型。
5. 各声明的传递公理列表，仅为 `propext`、`Classical.choice`、`Quot.sound`，顺序不重要。

`ReviewAudit.original_statement` 使用 `[Finite V]` 和原始边集 `E` 重新书写原题，再调用主定理，便于查验而不只相信 `Target` 的名称。它是一份命题对照入口，不是第二份独立数学证明。请读其具体类型，并留存你实际运行的命令、版本、退出码和完整输出。

现有主证明未使用 `sorryAx`、项目新增公理或 `native_decide`。标准三公理对应命题外延性、经典选择和商类型基础。形式化结论以这些标准基础及 Lean 验证工具可信为前提。语言命题与定义的对应仍请人工确认。

## 5. 可选的纸面数值复算

从包的根目录运行以下 Python 程序，使用 Python 3.10 或更新版本即可，所列程序仅依赖标准库：

```sh
python3 computations/enumerate_pair_partitions.py
python3 computations/reproduce_bounds.py
python3 computations/check_probabilities_by_permutations.py
python3 computations/independent_structure_bounds.py
```

主计算使用 `Fraction`，结果见 [results/reproduced_bounds.json](results/reproduced_bounds.json)。部分命令会重写包内对应的 `results/` 文件，建议在解压副本中运行并保留原包用于对照。小排列检查和局部型枚举用来核对公式实现；一般计数公式、结构选择和类型覆盖的数学证明仍需分别检查。Python 结果没有作为公理导入 Lean。

## 6. 已有证据和审阅的范围

| 记录 | 已经做了什么 |
|---|---|
|[原最终构建及导入审计](.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.log)|本机成功构建 Main、另行导入并打印定义、类型和传递公理；同目录保留构建日志与退出码记录|
|[本次交接审计](context/handoff/local-review-audit.log)|本机运行随包提供的 `ReviewAudit.lean`；运行详情与退出码见同目录 JSON|
|[Grok 最终审阅](context/reviews/research/grok_lean_main_r8.json)|核对原 Target、约化、七分支调用和22/23点真实输入，所读范围未发现具体缺口；只读源码和已有日志，未自行构建|
|[Gemini 最终审阅](context/reviews/research/gemini_lean_main_fresh_r10.md)|核对原题、约化、分支、类型重数、link 扣除、联合计数和染色还原，所读范围未发现具体问题；同样未自行构建|

Grok 的实际返回模型为 `grok-4.7-build/xhigh`；Gemini 为全新会话 r10，CLI 记录 `gemini-3.8-flash-high/high`。此前失败的 Gemini 调用不计为有效审阅。模型审阅属于辅助查错；本交接没有把它记成人类同行评审，也没有把“未发现问题”说成绝对无错担保。

截至本交接，项目没有已识别的未闭合证明义务；你的独立查验尚未进行。ARIS 在这里用于管理文献、证明义务、审阅与上下文，最终判断应落在原命题、实际证明项和可复现结果上。

## 7. 建议怎样反馈

不必写长篇评语，说明实际查了哪些部分即可。可按下面的格式返回：

```text
查验人 / 日期：
实际阅读：哪些章、哪些 Lean 模块；哪些部分未检查。
命题对齐：原题与 Lean 定义、顶层结论是否一致；理由。
复现：系统、Lean 版本、命令、退出码、日志；是否重建了项目源码。
数学意见：未发现问题 / 存在具体疑问 / 发现错误（附推导）。
具体定位：文件 + 定理名或公式编号 + 有问题的步骤。
影响范围：原命题、形式化、纸面推导，还是仅表述/运行环境。
```

发现数学疑问时，请给出最短的出错推理链、缺失条件或确切反例；发现编译问题时，请附第一条相关错误及完整命令。纸面论证与 Lean 证明若有差异，应分别记录其影响，不从其中一份通过直接推断另一份每句都正确。

## 8. 转交材料

直接转交整个 `aris4math_review_bundle.zip` 即可。解压后先打开本文件与 `PROOF_PACKAGE.html`。包内包括规范源、三份引理、39个证明源文件、独立审计入口、锁定版本文件、计算程序与结果、关键日志及相关来源材料；不包含作者的本机工具链和缓存，也不需要 Grok、Gemini 或 ARIS 账号才能查验。

附带的 `context/reviews/spec_v0.1.md`、`spec_v0.2.md` 是早期规格快照，只用于追溯；其中沿用的相对链接按项目根目录定位，当前规格以根目录 `FORMAL_SPEC.md` 为准。

只发送 HTML 足够阅读书面证明；需要独立重建 Lean 时，请发送完整压缩包。
