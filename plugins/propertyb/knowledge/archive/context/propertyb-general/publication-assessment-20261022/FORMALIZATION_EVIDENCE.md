# 已实现形式化设计的快速定位（2026-10-22）

用途：为 ITP / CPP 投稿可评估性提供源码证据，不作录用预测、全量审计或首创性判断。本次仅只读定位源码和既有构建报告，没有执行 Lean、数学计算或外部模型。下列声明均在命名空间 `Aris4Math.General.RS`。

## 1. 实际顺序延迟重染算法到原始染色结论

- `formal/Aris4Math/General/RS/Algorithm.lean`：`FlipWitness`、`flippedAfter`、`finalColor` 定义按真实排列逐点处理的状态递归；`new_mono_pair_event`、`failure_covered` 证明实际算法失败被残余事件及真实单交边对事件覆盖；`bichromatic_of_not_failure` 回到每条原边的两色结论。
- `formal/Aris4Math/General/RS/ProbabilityBound.lean`：`rs_recoloring_failure_le_fin` 装配实际失败概率上界；`rs_recoloring_failure_le`、`propertyB_of_rs_bound` 经重标记作用于任意 `[Finite V]`，不仅是固定 `Fin n` 样例。
- 价值：它把“概率公式足够小”连接到真实过程和原题对象；可以展示算法不变量、失败见证及存在性抽取之间的形式化设计。
- 范围：这是 RS 重染过程的领域模块，不是任意随机过程的通用框架；底层定义标为 `noncomputable`，不能据此宣称已交付高效可执行染色器。最终准则覆盖任意有限简单 k 元超图，k≥2，带明确数值充分条件。

## 2. 有限 Bernoulli 立方体上的正关联工具

- `formal/Aris4Math/General/RS/Bernoulli.lean`：`bernoulli_harris` 对任意有限顶点类型、p∈[0,1]、任意实值单调函数证明 E[f]E[g]≤E[fg]；`bernoulli_harris_events` 推广到任意有限族递增事件；`bernoulliProb_all_edges_hit` 接到超图击中事件。
- 价值：函数版与有限事件族版是明确可抽离复用的概率引理，证明使用有限类型 empty/option 归纳，接口不含 k=5、k=17 或某个特定超图。
- 范围：这是同参数独立 Bernoulli 乘积分布的 Harris 正关联，即本证明所用 FKG 型工具；不能称已实现任意格上一般 FKG 定理或任意非齐次坐标参数版本。

## 3. 全局排列的精确相对次序计数与积分桥接

- `formal/Aris4Math/General/RS/OrderCounting.lean`：`orderPatternEquiv`、`relativeEventEquiv` 构造等价；`relativeEvent_ratio` 对任意所选顶点的相对秩事件给精确概率；`beforeAfter_ratio` 对任意不交 A、B 及外部枢轴 x 证明所有 A 在 x 前、所有 B 在 x 后的概率为 |A|!|B|!/(|A|+|B|+1)!，允许任意数量的无关顶点。
- `formal/Aris4Math/General/RS/PairProbability.lean`：`permProb_pairLocal`、`sampleProb_pairLocal_integral` 将真实排列事件接到区间积分；`sampleProb_pairEvent_formula` 给任意同大小边对的完整公式（交恰一点时为 `jk k p / 2^(2*k-1)`，否则为0）。配套积分在 `formal/Aris4Math/General/RS/Integral.lean`。
- 价值：可以集中讲述离散概率空间、有限计数、实数积分三种表达之间的可信转换。相对次序计数本身比 Property B 特例更一般。
- 范围：实际随机样本使用有限颜色、标记和均匀排列；积分是精确计算工具，不应宣传成已形式化独立连续优先级随机变量的整个测度论模型。

## 4. 原始对象结构归约与统一增长的端到端装配

- `formal/Aris4Math/General/Structure/Reduction.lean`：`exists_pair_covering_counterexample` 从任意反例内部构造点对覆盖反例；`propertyB_of_pushEdges` 负责商／合并后的染色回拉；`pairCovering_vertex_bound` 给真实点数约束。
- `formal/Aris4Math/General/Structure/Clique.lean`：`singleIntersecting_card_le_cliqueBudget`；`formal/Aris4Math/General/Structure/Turan.lean`：`gamma_eq_twice_singleGraph_edges`、`gamma_le_cliqueBudget`，将实际单交图的团界与 Turán 接到同一超图的坏边对数。
- `formal/Aris4Math/General/Structure/Main.lean`：`propertyB_of_structural_rs_bound` 把上述对象归约与实际概率定理连接，结构假设不是交给用户的证书。
- `formal/Aris4Math/General/Growth/Twelve.lean`：`rsBudget_characterization_twelve` 证明同一预算是全部正整数接受预算的最大元；`integerGain_two_twelve` 证明统一整数增益≥2；`propertyB_of_general_growth_twelve` 对全部 k≥12、任意裸 `[Finite V]` 与简单 k 元边集，仅由边数≤`rsBudget k + integerGain k (rsBudget k)` 导出 `PropertyB E`。接受参数和结构证书均内部产生。
- 价值：可展现组合归约、图论、实分析、最大整数预算／floor 增益的模块接口与最终量词保真。
- 范围：不是逐个 k 的样例接口，统一覆盖全部 k≥12；仍是这套 Property B 分析的领域性装配，未据此建立自动形式化任意增长界的通用工具。

## 既有核验和结论边界

既有 `context/propertyb-general/bridge-12-16-20261021/lean/REPORT.md` 记录指定模块构建 exit0、构建后 `formal/ReviewAuditGeneralGrowth12.lean` 原积分／最大预算／Bool 染色独立复述 exit0；所查核心导出及原题声明仅标准三公理。这里引用既有执行证据，本次没有重跑或给出第二台机器复现。

源码确有可供形式化论文解释的设计内容，尤其是实际重染过程、有限正关联、排列计数与精确积分桥接，以及无外置证书的最终装配。因此不能把它描述成“只有一个数学结论的薄包装”；是否形成足够强的 ITP / CPP 论文，仍须比较相关形式化工作，并选择清晰的方法叙事和可复用接口。重要数学形式化本身也可以是贡献，不以新 prover 算法为必要前提。

未查范围：没有全文审计所有证明体，没有调查这些接口是否已被 Mathlib／其他项目实现或是否适合上游化，没有核查小 k 锁点／旧 T32/T33 的全部模块，没有评价数学新颖性及具体会议的最新征稿要求。
