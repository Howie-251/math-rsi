# 来源、阅读深度与本次未做的工作

查阅/整理日期：2026-10-29。**材料中的选题优先级、并行安排和工程试验方案是本次建议；不是来源已经证明的最优研究策略。**

## A. 用户提供的材料（研究状态的首要依据）

- **P1** `EXPERT_HANDOFF_20261028.md/html`：本次完整读取正文。最新3参数/103阶数、验证与Lean状态、十五度模型边界、暂停状态来自此文。保留原文副本于`upstream/`。
- **P2** `EXPERT_HANDOFF_20261028.zip`中的`history/DDP_METHOD_LEDGER.md`：本次按所选参数/机制检索对照，没有重审全部数学证据。6156源已恢复、186033 one-fault已排、小参数旧范围据此登记；原文副本保留。
- **P3** 原`DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md`：完整读取并保留原稿，作为严格标准与workflow的继承依据。初始27格与初始方法优先级被后来授权和本次策略取代。
- **P4** `DD_HANDOFF_REVIEW_NOTES_20261028.md`：上一轮助手的只读统计，明确未重跑图、SAT或Lean；本次只用作可追踪补充。
- **P5** 交付包`results/families.json`、`FINAL_RESULTS_PROOF.md`、`README.md`及选定模型/候选报告：保留小份原始副本。提供覆盖与接口上下文，不表示本次新独立验证。

上下游证据目录原位于用户现有工程；本包不重新收录大型边表、完整球缓存/CNF/工具链。原文相对链接需要原工程或原交付ZIP，链接在本包不能直接打开不等于原证据不存在。

## B. 本次外部核对（只作公开事实与方法背景）

### W1. Comellas主表

https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html

读取选定条目与页面说明；最后变更标注2026-10-28。表为最大已知构造，粗体表示最优。警告值与详情可能延迟同步。`registry/cases.json`只记本次选择的条目，不是整表快照，不宣称全网新颖性已穷尽。

### W2. D3条目说明

https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html

读取(4,3)、(8,3)、(12,3)、(16,3)的相关说明。历史文献与源生成方式为经典挑战/机制对照提供依据；本次未重新下载或验证它们的全部图。1920点源被公开描述为16正则，因而固定cap16、保旧边单点扩张无余度是直接推论。

### W3. D4条目说明

https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html

主表本次(12,4)为6156，而详情相关项仍含旧5832说明；不把旧详情当作6156源。项目最新账本已恢复6156，因此本项目源状态优先据P2。

### W4. D5条目说明

https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html

用于(3,5)70点的历史入口及D5来源导航；本次未独立穷尽(3,5)全部文献、未声称给出了严格最新上界。

### W5. D6条目说明

https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g6.html

读取(11,6)186033条目，公开说明保留182618点源边、增加3415点，部分新点互连。仅说明该类机制有外部先例；本项目对同源指定one-fault域的失败来自P2，不能忽略。

### W6. Slim Fly研究组项目页

https://spcl.inf.ethz.ch/Research/Scalable_Networking/SlimFly/

读取网页的设计动机、端点连接、路由与评估介绍。支持“总radix与网络连接数要区分，网络价值不止直径”的背景；没有本项目图的实测性能。本次未将项目页中的性能比例移植到本项目，也未分析其PDF图表。

原论文：Maciej Besta and Torsten Hoefler, *Slim Fly: A Cost Effective Low-Diameter Network Topology*, SC 2014。

### W7. Jellyfish原会议页面

https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/singla

Ankit Singla, Chi-Yao Hong, Lucian Popa, P. Brighten Godfrey, *Jellyfish: Networking Data Centers Randomly*, NSDI 2012。

本次读取官方摘要和论文元信息；支持逐步扩容、路由/布线等工程问题的重要性。未完成全文复算，不用其结果替本项目作性能背书。

### W8. PolarFly作者预印本摘要

https://arxiv.org/abs/2208.01695

Kartik Lakhotia et al., *PolarFly: A Cost-Effective and Flexible Low-Diameter Topology*, 2022。

本次读取作者摘要：模块化与可扩张是其研究内容。未据此宣称本项目D5拓扑优于D2网络；也不因参考该文重启旧D2求解。

## C. 本次明确没有执行

没有新的图生成、全源BFS、覆盖求解、rawUNSAT认证、Lean构建、网络仿真、计量知名度调查、商业硬件选择或发布。没有访问用户远端工程进行写入。全部新优先级与工程问题均为可供后续研究的建议。
