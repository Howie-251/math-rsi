# 原35边反例搜索审计

2026-10-20 UTC。本轮只阅读已有程序、完整运行摘要和保存控制结果，检查现有环境的依赖可导入；没有运行新原H搜索、SAT求解、控制重跑、Lean或MCP，也未改导航。[AUDIT.json](AUDIT.json)保存本轮读取的精简证据。

## 结论

**已有可复用的通用原H COVER/SAT harness和严格非B控制；但现有保存目标搜索全部是32边，没有35边实际搜索覆盖。** 在本次核查的程序／日志中，未发现A1角色或25点低点混合的35边专用搜索及运行证据。旧120个不同32边样本不能迁作35边、A1或25点当前残支的探索。

因此当前反向路线不能称为“已经充分搜过”。值得做一次短、明确角色的A1原35边probe，避免只在局部概率松弛或signed门上反复试验。建议见第5节；本轮没有执行它。

## 1. 现有通用原H harness

入口为[search_counterexample_sat.py](../../../../../computations/search_counterexample_sat.py)，说明为[COUNTEREXAMPLE_SEARCH.md](../../../../../context/COUNTEREXAMPLE_SEARCH.md)。它对所有 $\binom nk$ 个k集设边变量，原生基数强制恰M边；可选全部点对覆盖，并可固定一条首边作重标号对称处理。

每份master模型给一份完整原H。独立color oracle对每条原边加入正、负两个子句，只固定一个点颜色，不限制平衡。若proper，保存实际红点集，直接逐边复核，然后加入“某条被选边在该染色下单色”的必要COVER cut。平衡oracle只提供更多有效cut，不能报告原H不可染。每条cut还通过颜色类内组合枚举及全五集位掩码扫描交叉核对。

oracle若返回不可染，代码另枚举全部 $2^{n-1}$ 份互补颜色代表核验；只有这一步确认后才输出 `COUNTEREXAMPLE_INDEPENDENTLY_EXHAUSTED`。求解预算耗尽记UNKNOWN；master UNSAT仍记 `MASTER_UNSAT_UNCERTIFIED`，没有无证书宣称全域排除。

当前CLI参数允许 `--edges 35`，不是只支持32；但三个迁移细节必须区分：

1. 默认边数仍32，必须显式改为35。
2. 仿射相位初值只在源码条件 `k==5 and 19<=n<=25 and m==32` 下启用。35边运行不会自动有已有相位seed。
3. `audit_saved_runs` 硬编码只接受 `uniformity==5 and edges==32`，且结构重放写死32。它会跳过35边摘要；不能把该审计PASS用于新35边run。

程序没有A1度谱、固定低点角色、单位星或25低点数参数。其degree/codegree目前只是候选输出／结构验证，不是master中相应的角色约束。加入这些约束需新的窄适配和独立角色验证，不能假装原CLI已有。

本轮实际仅运行依赖导入检查：`.venv-counterexample/bin/python`为Python3.14.6，`python-sat`1.9.dev15，Minicard和Minisat22均可导入。未调用solve，不把导入成功记作新的搜索／控制通过。

## 2. 已保存搜索的真实范围和最近运行

所有11份五元目标运行均在2026-10-06，边数全部32，最新目标摘要结束于07:50:06.631286 UTC。汇总如下：

|顶点数|运行数|候选记录数|不同有标签H数|范围|
|---:|---:|---:|---:|---|
|19|2|24|23|点对覆盖|
|20|1|22|22|点对覆盖|
|21|1|24|24|点对覆盖，无A1角色|
|22|1|18|18|点对覆盖|
|23|4|34|31|两次点对覆盖、两次未限制点对覆盖|
|24|1|1|1|点对覆盖|
|25|1|1|1|点对覆盖，无低点混合角色|
|合计|11|124|120|全部32边|

全部目标运行终态均为 `TIME_BUDGET_NO_COUNTEREXAMPLE`，累计2320条cut。每个候选都有保存的proper原染色；没有35边counterexample、没有目标域master UNSAT。24／25点分别只有一个实际候选，不能称深度探索。

[保存artifact审计](../../../../../results/counterexample-search/audit/artifact_audit.json)为PASS：不调用SAT，核124条记录、120个不同有标签32边H、2320条cut来源及后续候选满足此前cut。它只验证这些有限证据，不排除任一顶点数的完整对象域。本轮读取该原始JSON与各summary，没有重跑审计。

本次另外扫描本轮context、results和computations中现有小型JSON运行摘要，未找到k5/M35且具有原H反例oracle调用的运行记录；检索现有PySAT／CP-SAT入口只定位到上述原H程序。这个结论是本项目当前可见入口及日志的审计，不推断未保存或外部私有实验。

## 3. 本地51边非B及其他控制确已严格验过

[controls.json](../../../../../results/counterexample-search/controls/controls.json)保存七个正负控制，状态PASS。三角形、Fano、九点完全五元图不可染；相应删边或八点完全五元图可染。每份均有SAT和独立bitmask枚举结果。端到端CEGAR另找回三角形和Fano并独立穷尽，检验的不只是固定oracle。

最相关控制是17点、51条五边的Fano-parity构造。程序从七点循环Fano线生成每条线并上五个不交点对之一，共35边；再加五对中各选一点、偶数奇偶型的16个横截，共51条互异五边。所有51条literal边均在controls中可读取。独立遍历65536个互补颜色代表，保存结论为不可染。

另一份[check_known_nonb_bounds.py](../../../../../computations/check_known_nonb_bounds.py)重新生成并比对这一边表，同时独立重算全部颜色的单色边直方图；结果在[known_nonb_bounds.json](../../../../../results/known_nonb_bounds.json)：

|非B控制|点数|边数|独立互补颜色代表数|proper染色数|
|---|---:|---:|---:|---:|
|Fano-parity51|17|51|65536|0|
|完全五元K9|9|126|256|0|
|Witt66|11|66|1024|0|

该第二程序还对原始／补孤立点控制共3908份有限锁布局，进行了17,129,009个pair权重比较，保存结果无矛盾。它攻击的是一般概率公式，不使用目标32／35边特有度数或link配额去套这些非B控制；补孤立点非B性由原核限制证明，没有虚报遍历更大颜色域。

这些控制足够证明本地有真正不可染的五元literal边表及可靠基本验收器，无需仅为本轮诊断再次生成。它们不属于35边A1／25低点谱，也不是当前目标的反例。

51边基线的原始文献依据可复用本地Aglave等2020 §1.1及Table2（[原稿](https://ajc.maths.uq.edu.au/pdf/76/ajc_v76_p073.pdf)），其中给Abbott–Hanson奇数阶构造和m(5)≤51。旧边表最初参考的网页是AI工作报告；其数学可靠性在本项目来自上述完整边表独立穷尽，不把该网页当primary文献。

## 4. 新参数下存在的实际H／signed例子不是反例搜索覆盖

本轮研究确有35边实际控制，不能与不可染搜索混淆：

- [24点pairing控制](../../middle/pairing_global/REPORT.md)给度谱7^20,8^3,11的35边点对覆盖H及明确proper染色；它反驳的是“匹配能命中20边”辅助保证。
- [25点many-six报告](../../twentyfive/many_six_scope_20261020/REPORT.md)有r19的仿射30线加五边实际H，证明大r域非空；它不是不可染反例。
- A1平坦源、core15、私有负布局等保存例子，若只有部分原边或固定signed接口，就没有覆盖原35边H的不可染性义务。
- [PG九正族countersearch](../../twentyfour/nine_positive_joint_negative_budget_20261020/countersearch_sol/REPORT.md)完整检查PG(2,3)九线正族的715输入，但目标是signed修复门，非原H／P6外17布局搜索。

这些例子支持结构边界和反例意识，不能将其对象数加进“已搜索35边非B候选H”的计数。

## 5. 最短值得做的真实反向probe（未执行）

优先一次A1而非再做无角色25点泛搜索：固定标签x=0、p=1、B={2,3,4,5}、U={6,…,10}、V9={11,…,20}，对全部20349个五集设边变量。保留恰35边和全部点对覆盖，追加原生exact-cardinality行：

$$d_x=6,\ d_p=7,\ d_b=d_u=8,\ d_v=9,$$
$$\lambda(x,b)=2\ (b\in B),\qquad
\lambda(x,y)=1\ (y\notin B\cup\{x\}).$$

这只是选定角色标签，不假设中心link分割、唯一坏源、私有边配置或未证signed门。**不要继承默认fixed-first-edge**：固定角色后，不能再无证要求{0,1,2,3,4}为边。可使用 `--no-fixed-edge` 或仅用经角色保持群证明无损的对称化。

先不加入当前正向候选证明的剪枝，避免反向探针只搜索我们喜欢的局部残模型。复用已有unrestricted oracle和cut逻辑，一次60–120秒墙钟／少量候选预算即可；每候选完整保存35边及独立角色、paircoverage、proper染色验收。若oracle报告UNSAT，按原全色域2^20互补代表复核，保留literal边集与不可染核验。未命中或master UNKNOWN只说明该次有限probe未得反例。

这需要一个很小的新角色适配及参数化保存审计器，不需新平台或包；上述harness本身可复用。若目的是最短无代码warmup，可直接显式 `--vertices 21 --edges 35 --no-fixed-edge` 做一次通用probe，但它不保证生成A1。相比旧25点只得到一个32边候选，A1角色约束是更有针对性的下一次原对象尝试。这里仅建议，没有启动。

## 6. 公开数值的本轮有限核对

2026-10-20重新读取primary [arXiv记录](https://arxiv.org/abs/2403.05674)，仍为2024-06-20的v3；其[原文Theorem1和Table1](https://arxiv.org/html/2403.05674v3)分别给m(5)≥32及上界51。本轮没有发现更强的新公开数值原文，但两次宽搜索不足以声称穷尽了当前公开纪录。项目已验的m(5)≥34与其后纸面候选，是项目结果范围，不冒充该2024文献数值。

2026-05-28的[Springer原出版页](https://link.springer.com/chapter/10.1007/978-3-032-18810-6_9)可读取元数据、摘要及参考文献：章节pp.173–181，引用2024 heuristic-search稿件；本轮页面仍只提供subscription preview，未取得完整章节或那个启发式稿件的边表／数值。因此这里保留“已直接核对的公开primary基线32…51，较新综述全文数值未核”的边界，不写成截至今日公认精确最新界。

本审计到此停止，不重复旧120样本、51边控制或当前局部表。
