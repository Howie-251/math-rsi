# k≥12 解析扩展的规范正文同步

日期：2026-10-21。范围：将 [ANALYTIC_EXTENSION.md](ANALYTIC_EXTENSION.md) 的完整解析推导合并至四份规范纸面源；未修改图、HTML生成器、RESULTS_FIGURE、Lean、导航或wiki。

数学来源为已由主线程逐行核对的解析扩展，以及 fresh 审阅的 [PROOF_AUDIT.md](PROOF_AUDIT.md)：U0–U6、37项义务全部覆盖，结论 `PASS_WITH_DECLARED_IMPORTS`，`review_independence: same-family`、`acceptance_status: provisional`。本次同步不扩大该审阅的独立性；同步开始时本轮Grok审阅仍在途，具体结果由主线程另行记录。

## 已合并的正文

- `proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md`：定义B.1、引理B.1及B.4的范围改为k≥12；B.1证明沿用原文，B.4改用二项式前三项证明a_k(1/k)>3/5，得到4/k≤1/3<9/25<a²。引理B.2、B.3和定理B仍为独立的k≥17加一结论，原陈述与证明逐字保留。
- `proofs/propertyb-general/CLIQUE_REFINEMENT.md`：定理C范围改为k≥12，保留相同Δ公式并加强Δ≥2。新完整证明直接控制s≥2、r_k(M+s)≤3√M和√M≥64>24，随后用同一严格接受见证及实际超图推论C.2完成转换；不依赖旧B.2/B.3的17起点证明。
- `proofs/propertyb-general/BASELINE_COMPARISON.md`：定义D.1、定理D及D.2/D.3的比较范围改为k≥12。D.2使用12、13双奇偶起点及步长2归纳证明v>4k²；D.3保留同参数支配证明，并逐一写清三个接受集合的非空性。零锁测试定义D.2及从定理E起的全部正文逐字保留，k≥256起点不变。
- `proofs/propertyb-general/LITERATURE_COMPARISON_TABLE.md`：主定理C及五项包络范围改为k≥12，Δ≥2；明确现有端到端Lean仍只覆盖k≥17，新增12≤k≤16纸面已证、Lean补充进行中。本次未运行或改写Lean，未宣称新增范围已形式化。

## 备份与实核

修改前四份原文各普通复制一次至 [before-paper/](before-paper/)；未覆盖或更新备份。

对备份与成稿执行程序比较，四文件原有锚点、公式编号和链接目标均逐项按原顺序完整保留；显示公式定界符成对。另对以下未涉及部分执行逐字比较，全部通过：

1. UNIFORM的引理B.2、B.3及定理B整个区块；
2. CLIQUE的引理C.1、推论C.2及其证明；
3. BASELINE自零锁测试定义D.2起至文件末尾的全部正文，包括定理E、引理E.1–E.4及文献定位。

主线程将另行逐diff复核并生成最终HTML；本同步记录不将未执行的图、HTML或Lean验收记为完成。
