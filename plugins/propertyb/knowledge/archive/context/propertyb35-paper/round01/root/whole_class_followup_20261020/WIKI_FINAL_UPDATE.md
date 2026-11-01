# 本轮知识收口

本轮只更新研究wiki及本交接记录。没有修改数学规范、AGENTS、NEXT、PROGRESS、BRANCH或checkpoint，没有创建或升级claim。八个主要数学类仍开放；25点多六度支的剩余核心为r=3…6且所有原边低迹至多2。

## 有效审阅同步

以下四个既有实验均保持`verdict: partial`、`confidence: medium`，纸面结果按drafted/provisional记录：

- `research-wiki/experiments/propertyb36-marked-partition-m17-20261020.md`
- `research-wiki/experiments/propertyb36-nine-or-more-six-common-budget-20261020.md`
- `research-wiki/experiments/propertyb36-eight-or-more-six-analytic-20261020.md`
- `research-wiki/experiments/propertyb36-seven-and-small-low-traces-20261020.md`

以`REVIEW_RECONCILIATION.md`的14:37 UTC处置为准：Grok1285有效end_turn，实际grok-4.7-build/xhigh，静态核SMALL/SEVEN及M17/宏星接口；Gemini授权fresh retry1 cell1286有效SUCCESS，CLI选择gemini-4-argon-high/high，静态全文核SMALL/SEVEN/EIGHT、宏星和M17，并手核实际算术。Root已全文处置；两者均未执行程序或Lean。早先未完成调用未计认可；旧r9摘要的s3更正仍指向原处置，不改变规范证明。

## 两个集中保存的partial实验

`research-wiki/experiments/propertyb36-pure-pair-structure-and-unit8-boundary-20261020.md`集中记录r6两条条件结构及旧八锁边界。r6全三重完美匹配类至多2；若恰两类，则每类高超额至少2且外部重复成本满足δ≥T_C+1。完整13650标记筛到4684键，r3/4/5/6余39/1228/351/20；r3须区分旧已完成DP非严格33和旧未处理6。r4…6只是冻结菜单失败，不是所有布局最优失败，也不是实际H反例。完整CPU11.340919秒，profile0.888407秒。

`research-wiki/experiments/propertyb36-paired-four-partition-analytic-gate-20261020.md`集中记录19点任意两份四四块划分的联合补色失败上界15228，并收纳新24点全四低原边实际caller。通用门不依赖新增矩阵目录；实际caller用较粗16212已足够。新规范`proofs/propertyb35/TWENTYFOUR_FOUR_LOW_EDGE.md`给出24点至多35简单五边pair-cover中，存在至少四低原边即可染，因而nonB低迹≤3且r≥13子类可染。其新scope尚待跨模型审阅，不能继承25点旧意见，也不等于完整24点验收。

## 工具与失败边界入口

- `research-wiki/PROPERTY_B_CONDITIONAL_TOOLKIT_36.md`：在既有组内加入15228解析门及24点caller、r6两条共同匹配结构，并同步有效审阅范围；没有另造重复工具组。
- `research-wiki/PROPERTY_B_FAILURE_ATLAS.md`：新增第21项，保存4684键冻结旧菜单失败的完整范围、未处理项及重新启动条件。

所有实验写入前均经`capture_filter`，机械筛查为clean；使用规范`research_wiki.py add_experiment`创建/更新实验及关系，复用既有idea，未手工改graph。最后由helper追加收口log并重建index/query_pack；query_pack为5464字符。未重跑数学程序、旧DP或24点小核。
