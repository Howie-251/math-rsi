---
type: idea
node_id: idea:ddp-math-challenges-and-records
title: "数学候选、经典挑战与已有严格范围"
stage: proposed
outcome: pending
added: 2026-10-29T15:20:37Z
based_on: ["paper:ddp-record-sources-20261026"]
target_gaps: ["gap:DDP1", "gap:DDP2"]
tags: ["ddp", "strategy-refresh", "proposal"]
---

# 数学候选、经典挑战与已有严格范围

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-29同Goal策略资料合并；不产生新数学／工程结果。

## Thesis
这是候选地图和进入条件，不是已证claim、难度排名或自动任务队列。原[registry](../../context/DD_PORTFOLIO_START_20261026/registry/cases.json)是唯一候选数据源；本页只建立证据导航，不另抄一套可能分叉的实时基线。12项是9项候选／挑战加3项继承成果，激活前按原registry与具体公开来源核对最优标记和门槛。

|参数|本次角色|已有实际证据|进入前必须继承的边界|
|---|---|---|---|
|(15,4)|现成未决|[ddp-d15-d4-current15552-source-gap-20261027](../experiments/ddp-d15-d4-current15552-source-gap-20261027.md)|648 free；一般非对称≤15点仍UNKNOWN。反演/≤5仿射线rawUNSAT及内禀36点、二择反射门的失败不排一般扩张。|
|(15,5)|现成未决|[ddp-d15-d5-current102060-source-slack-profile-20261027](../experiments/ddp-d15-d5-current102060-source-slack-profile-20261027.md)|810 free；当前源是102060。一般覆盖UNKNOWN，旧LP/MIP与成线子域分账，不自动续时。|
|(12,3)|不同机制候选|[ddp-wave5-hs850-branch-lift](../experiments/ddp-wave5-hs850-branch-lift.md)|固定HS850六参数已闭；十轨道放松只是有限失败。需要真实路径互补变化。|
|(16,3)|不同机制候选|[ddp-wave4-mizuno-d3-source](../experiments/ddp-wave4-mizuno-d3-source.md)|1920来源已借用分析，全16正则；无保边增点空位，不重做首次恢复。|
|(12,4)|不同机制候选|[ddp-d12-d4-current6156-source-20261027](../experiments/ddp-d12-d4-current6156-source-20261027.md)|6156/36936全12正则，free0。8000项只未过特定充分证书，不是8000图D4反例。|
|(11,6)|需新规则的迁移储备|[ddp-d11-d6-unique-onefault-star-exact2-20261027](../experiments/ddp-d11-d6-unique-onefault-star-exact2-20261027.md)|186033的固定mandatory9+至多2guards已完整排除；不排任意11邻域，不续该proxy。|
|(3,5)|经典挑战储备|[ddp-afy70-2fold-d6-capacity-20261027](../experiments/ddp-afy70-2fold-d6-capacity-20261027.md)|AFY70指定普通2重D6/3重D7 cover已排；不能外推整个(3,5)。|
|(4,3)|经典挑战储备|[ddp-published-quartic-cayley-census69orders-4d3-d4-20261028](../experiments/ddp-published-quartic-cayley-census69orders-4d3-d4-20261028.md)|已发表完整Cayley目录相应范围已过滤无改进；非Cayley仍开放，旧42子族不重跑。|
|(8,3)|经典挑战储备|[ddp-wave10-gq312-internal-cycles](../experiments/ddp-wave10-gq312-internal-cycles.md)|312两侧2-factor仅有限失败；4090普通坏对属于保存图，不是全族界。|
|(11,5)|继承成功|[ddp-h9-qline-d11-family-37631](../experiments/ddp-h9-qline-d11-family-37631.md)|37629..37631三例；后续同格须超过项目最好，署名与Lean状态保留。|
|(12,5)|继承成功|[ddp-h9-qline-d12-family-42377](../experiments/ddp-h9-qline-d12-family-42377.md)|42343..42402六十例；30个新形态失败同时漏原外围和新增点，不能归因仅新增60点。|
|(13,5)|继承成功|[ddp-d13-singlefault-star-family-51457-20261027](../experiments/ddp-d13-singlefault-star-family-51457-20261027.md)|51418..51457四十例；成功代理不是完整孪生，完整覆盖才是充分性。|

补充证据：[12D3十轨道放松](../experiments/ddp-wave5-hs850-orbit10-relaxation.md)、[6156固定C20切片](../experiments/ddp-d12-d4-wide-filter-c20-slice8000-20261027.md)、[AFY70三重cover](../experiments/ddp-afy70-3fold-d7-capacity-20261027.md)、[42点保旧边三助手](../experiments/ddp-polarity13-c3-freeports-threehelpers42-4d3-20261028.md)。目录过滤依赖已发表完整性，不是本项目新分类或一般图排除。

经典低度问题的历史与易陈述性只提供定性学术辨识度；没有知名度量表或成功概率。工业价值独立且尚未测。其它已授权参数仍可因真正新覆盖规则替换候选，不能因这12项形成永久队列。

## 来源与当前增量

[CASEBOOK](../../context/DD_PORTFOLIO_REFRESH_20261029/CASEBOOK.md)、[PRIOR_WORK_AND_DELTA](../../context/DD_PORTFOLIO_REFRESH_20261029/PRIOR_WORK_AND_DELTA.md)、[原机会草稿](../../context/DD_PORTFOLIO_REFRESH_20261029/wiki_import/ddp-math-challenges-and-records.md)。本次只定向检索相关旧节点，没有重导365条账本或重新判定原图。H9当前30项缺项分类来自保存missing列表的只读提取：1358原外围与110新增是跨case出现次数， distinct并集581/46；不是事前注册的预测或新覆盖实验。随后已执行的投影检验按真实PRED/RESULT追加原twist实验：30/30原外围单独不可覆，新增单独10可覆，五个两guard项原外围仍0；冻结存在预测REFUTED，CPU0.703871411，0新球/BFS/solver/图。该结果不覆盖移除新增点后新释放的guard域，不自动启动联合重排长搜。见[投影报告](../../research/ddp/refresh_20261029/H9_PROJECTED_GUARD_REPORT.md)与[静态review](../../research/ddp/refresh_20261029/ANALYSIS_PROJECTED_GUARD_REVIEW.md)。

## Key risks
候选不是成功承诺；UNKNOWN不排除，子域失败不外推，旧成果不重复计数。工程收益未经本项目试验。


<!-- D3_REFRESH_TERMINAL_20261029 -->
## 2026-10-29 D3对照更新

(16,3)原1920 source/controller已复用；新80平行／160错位33-controller域虽完成一次实质附着改变，最终均有严格端点容量反例，无2112图。F5固定正对照36转向／500pencil成立，但3750/20度尚未绑定公开门槛或边表，不计新纪录。细节沿[原source](../experiments/ddp-wave4-mizuno-d3-source.md)与[同一33附着记录](../experiments/ddp-source30-triangle-attachment33-endpoint-capacity-20261029.md)。当前两域停止，不据它们排一般(12,3)/(16,3)或自动续矩阵扫描。


<!-- F5_LITERAL_ACCEPTED_20261029 -->
## 后续数学结果已落地

F53750点20regular／D3完整图已独立all3750roots接受，另列[实际图节点](../experiments/ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029.md)。总合法实例104／4参数，旧confirmed公开主表103／3保留，新20D3最新global纪录待确认；只主张超过已核对September2026 published2783多967。完整固定公式图Lean现1：Fin3750阶数／degree≤20／真实Walk恰D3全部kernel通过；旧103图Lean仍0。Lean文本解析等同性和恰20正则未证，不冒充结论。两种10度限噪声各100失败属同机制变体，不回退正图、不虚增独立方法。原registry现34项，新增实际20D3记录，仍非全部必做队列。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

