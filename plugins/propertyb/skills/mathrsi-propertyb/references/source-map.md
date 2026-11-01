# Property B 来源、阅读与执行地图

本插件的数学与代码资源都在 MathRSI 内，不再要求配置一个外部 PROPERTYB_SOURCE_ROOT。原始材料见 [knowledge/archive](../../../knowledge/archive)，实际选择范围见 [知识说明](../../../knowledge/README.md) 与 [文件清单](../../../knowledge/SOURCE_INVENTORY.json)。单题工作区另建或沿用原目录，归档只读。

## 从问题到正文，不从目录猜结论

|问题|正式指南|回看原始来源|
|---|---|---|
|合并不共边点、顶点上端、整数选锁|[归约/选锁](mathematics/01-reduction-and-selection.md)|[原L1–L12及后续库存](../../../knowledge/archive/research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md)、[小k迁移](../../../knowledge/archive/research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md)|
|真实迹、empty/singleton、重标号、递归域|[真实迹与覆盖](mathematics/02-actual-traces-and-coverage.md)|[ThirtyThree源码](../../../knowledge/archive/formal/Aris4Math/ThirtyThree)、[原研究经验](../../../knowledge/archive/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md)|
|精确排列与共同坏对|[概率/弱对偶](mathematics/03-permutations-bad-pairs-and-duality.md)|[完整证明目录](../../../knowledge/archive/proofs)、[失败地图](../../../knowledge/archive/research-wiki/PROPERTY_B_FAILURE_ATLAS.md)|
|signed修复、源态、owner与共同容量|[signed](mathematics/04-signed-repair-and-sources.md)、[完整门目录](mathematics/04a-repair-gates.md)|[36条件工具](../../../knowledge/archive/research-wiki/PROPERTY_B_CONDITIONAL_TOOLKIT_36.md)|
|Gram/秩/共享列等结构规约|[共同结构](mathematics/05-shared-structure-and-conditional-tools.md)|[一般方法综合](../../../knowledge/archive/research-wiki/PROPERTY_B_GENERAL_METHOD_SYNTHESIS.md)|
|RS判据、一般增长与文献基线|[一般k正文](mathematics/06-general-k-rs-and-growth.md)|[正式来源地图](../../../knowledge/archive/context/propertyb-general/formal-exposition-20261021/SOURCE_MAP.md)、[规范证明](../../../knowledge/archive/proofs/propertyb-general)|
|新参数算术/独核/效率|[实务入口](practice/README.md)、[检查器](practice/checker-capabilities.md)|[六元](../../../knowledge/archive/context/propertyb-m6-67-progress-20261029)、[七元](../../../knowledge/archive/context/propertyb-m7-131-20261029)、[十二元](../../../knowledge/archive/context/propertyb-k12-4664-20261029)|

数学整理页保留定理假设、完整公式和证明/实际caller。原wiki的状态快照可能早于其后修复，以知识说明和对应最终报告解释日期；不能据旧“已在途”恢复一个后台任务。

## 查源码与核声明

Lean库在 [formal](../../../knowledge/archive/formal) 中保留原模块结构、toolchain及manifest。一般Growth与五元ThirtyThree是不同主模块；完整原题审计文件同目录保留。对新调用先看实际声明，而非仅grep定理名。数学正文里的来源位置能定位实际接口；条件wrapper编译成功不等于已经构造了条件。

现行案例所需输入已纳入仓库；执行时复制相应archive子树到任务工作副本，在副本中保存新输出。其余历史脚本保留为研究源码，不保证每份旧日志与JSON都在；先读对应报告和输入引用。不能以缺历史日志为理由重新搜索一个已证明定理，也不能冒称整个历史工程都可一键重放。

## 本次提炼的阅读与验证范围

数学作者系统阅读L1–L117库存及关键原证明，实务作者核读失败/效率/Lean来源并运行指定案例；Root核对归档、公式接口、文献版本图、具体数学计数与端到端调用。精确阅读边界在仓根 development/propertyb-rebuild/ 的 MATH_READING_REPORT.md、PRACTICE_READING_REPORT.md 与最终VALIDATION中。归档保存不等于本轮把每个旧文件重新审计了一遍。

来源原文保留，新的数学结论只按原证据范围引用。所有跨模型回应保留实际模型、读取范围和是否运行命令；开发审阅不是新数学终审，也不能将七元未审状态变为已获跨家族认可。
