# Property B 知识库：先找到可调用结论，再读完整证据

这里保存从 aris4math 提炼的数学知识和原始研究材料。实际工作从 [领域主技能](../skills/mathrsi-propertyb/SKILL.md) 开始；本目录不是另一个正在运行的 Goal，也不把历史命令作为当前执行指令。

## 三种阅读深度

1. **做决策与操作**：读 [bound-lab](../skills/propertyb-bound-lab/SKILL.md)、[certificate](../skills/propertyb-certificate/SKILL.md) 或 [literature](../skills/propertyb-literature/SKILL.md)，按当前义务选择方法。
2. **调用数学与经验**：读 [数学阅读地图](../skills/mathrsi-propertyb/references/mathematics/00-READING-AND-CALLING.md) 与 [实务地图](../skills/mathrsi-propertyb/references/practice/README.md)。那里有完整假设、公式、证明、实际输入连接、反例和重试条件。
3. **回到原始材料**：`archive/` 按原项目相对路径保存 wiki、证明、context 文本/源码、Lean 源及原文 PDF。新指南全部从本仓指向它；换机器不要求另一份 aris4math。

不要把“归档文件多”当作知识已被消化。正式指南负责路由和调用；原始全文用于复查精确论证、查看未被摘要覆盖的细节、追溯历史失败。完整文件清单及未纳入项在 [SOURCE_INVENTORY.json](SOURCE_INVENTORY.json)。阅读报告记录本次实际全文/定点阅读范围，不宣称上万文件都经重新数学审计。

## 核心工具入口

|需要解决的问题|直接进入|
|---|---|
|新M之后顶点域和低度保证变了什么|[反例归约与选锁](../skills/mathrsi-propertyb/references/mathematics/01-reduction-and-selection.md)|
|原H如何产生目录中的型；怎样增锁和投影|[真实迹与覆盖](../skills/mathrsi-propertyb/references/mathematics/02-actual-traces-and-coverage.md)|
|概率分母、方向、共同坏对、交叠扣除|[排列与弱对偶](../skills/mathrsi-propertyb/references/mathematics/03-permutations-bad-pairs-and-duality.md)|
|改成局部重染，哪种正负集合门可用|[signed修复与源态](../skills/mathrsi-propertyb/references/mathematics/04-signed-repair-and-sources.md)、[修复门全文](../skills/mathrsi-propertyb/references/mathematics/04a-repair-gates.md)|
|各局部最坏能否同时来自同一H|[共同结构与条件工具](../skills/mathrsi-propertyb/references/mathematics/05-shared-structure-and-conditional-tools.md)|
|统一k定理如何由实际H接到RS判据|[一般k完整正文](../skills/mathrsi-propertyb/references/mathematics/06-general-k-rs-and-growth.md)|
|通用及条件引理全库存|[L1–L117保真目录](../skills/mathrsi-propertyb/references/mathematics/08-complete-lemma-inventory.md)|
|失败输入说明什么，什么时候值得重试|[具体失败地图](../skills/mathrsi-propertyb/references/practice/failure-map.md)|
|减少计算或Lean等待|[计算效率](../skills/mathrsi-propertyb/references/practice/computation-and-efficiency.md)、[Lean实务](../skills/mathrsi-propertyb/references/practice/lean-practice.md)|

## 数学结果状态快照（2026-11-01整理）

|结果|可复用的证据层级|
|---|---|
|m(5)≥33、≥34|完整自然语言证明、端到端Lean源码、原命题与公理审计入口|
|m(5)≥35|完整自然语言候选与局部证书；完整Lean尚未闭合，保持暂停|
|m(5)≥36|仍有实质数学缺口，保留全部条件工具和暂停交接，不当作已得下界|
|m(6)≥67、m(8)≥267、m(9)≥543|计算机辅助论证、相应完整独核及指定静态审阅；没有对应Lean|
|m(7)≥131|424型完整双实现算术与数学候选；未将其它参数审阅移作本参数终审|
|m(10)≥1112、m(11)≥2275|合作者原证明、证书与既有重放，状态按原报告，不借用一般定理Lean|
|m(12)≥4664|664355必要参数实例；完整域重建及20例独立Fraction，并非全表第二概率实现|
|一般k≥12增长主定理|完整数学正文、端到端Lean及原命题审计；比较D/E与C.2逐点数值分别保留原范围|

具体审阅与重放范围在各来源报告里。新任务使用这些结果时先核实际前提；这份快照不是对所有原始材料的重新验收。

## 原材料怎样保存，什么没有复制

`research-wiki/` 全部实体及关系、`proofs/` 全文、`context/` 的 Markdown 与研究源码、`formal/` 的全部 Lean 源及固定 toolchain/manifest 已按原结构复制。保留本地论文PDF及合作者原稿/源码；已指名的可执行案例连同必要JSON一并纳入。旧文件中的时间、作者机路径与状态文字原样留作历史，不作为本技能的运行依赖。

未复制原工具链、`.lake`缓存、第三方软件克隆 `ref/software`、全部大型扫描日志/二进制和每一份历史JSON。故 archive 是可复用研究源码库，**不是原项目所有历史运行的完整复现包**。可直接执行的案例明确列在 certificate 技能与检查器地图中，已纳入其输入；其它旧脚本先按原文核依赖，不批量执行。大型缺失结果不会被新指南当作唯一证明来源；有需要时优先从已纳入源码在独立工作区重新产生，并说明成本。

原 archive 的 Markdown 还可能链接旧展示HTML、旧ZIP或未纳入的历史日志；这些是历史文档的引用，不是现行技能的承诺。现行技能与指南的链接单独实际检查，缺原材料的入口须更换为已纳入证明或明确说明缺项。

## 新研究怎样沉淀回来

任务的规格、新参数、日志和进行中义务写入任务自己的wiki。得到了可复用引理时，把完整假设、结论、证明和真实caller提炼成插件更新；失败则记录被否定的是哪条陈述、具体反例或失败输入、什么改变值得重试。Root在独立维护步骤核对后纳入本库，不让任务运行改动base。

维护时更新相应阅读地图与知识关系，保留原始证据。不要每一轮另建一个“终极经验.md”，也不要只更新导航而让源正文继续给出过时的结论。
