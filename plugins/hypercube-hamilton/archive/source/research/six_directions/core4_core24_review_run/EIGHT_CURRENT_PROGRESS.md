# 八孔当前状态

2026-11-01。用户要求优先尽快完整关闭八孔。**完整八孔、完整T15、完整P6仍未证。**

当前已由独立GPT-6.1-sol high审计通过的完整T15硬轨道有21个：
`[0, 2, 5, 7, 8, 10, 13, 14, 15, 18, 19, 21, 23, 25, 27, 31, 32, 35, 37, 38, 44]`。保证等级为相对于显式导入定理和有限证书的same-family/provisional。

当前剩余2855个规范八孔配置，其中2805个有(2,1)投影，
50个是七轨道例外。按规范目标1、7、31，剩余分别700、1055、1100。
这些是孔配置数，不是匹配数；每个已关闭轨道的量词覆盖其全部实现匹配。

当前整轨道(2,1)方案最少再需3个核心，一个充分集为`[1, 4, 24]`。
最少轨道数未必代表最快证明路线：18、21、25三个核心可以替代困难核心26，
这条替代路线已在三个核心完整独立审计PASS后计入。任何候选核心只在其完整独立审计PASS后计入。

50个例外中，11个的EP0已审通过但仍依赖核心4；另39个EP0未证。
它们均未从剩余50中提前扣除。完整自由终点分支早已关闭，当前剩余是被覆盖终点。

本次新增接受的完整审计：`['T15_CORE0_FULL_REVIEW.json', 'T15_CORE5_FULL_REVIEW.json', 'T15_CORE8_FULL_REVIEW.json', 'T15_CORE27_FULL_REVIEW.json', 'T15_CORE15_FULL_REVIEW.json', 'T15_CORE23_FULL_REVIEW.json', 'T15_ALTERNATIVE_GROUP_REVIEW.json', 'T15_ALTERNATIVE_GROUP_REVIEW.json', 'T15_ALTERNATIVE_GROUP_REVIEW.json']`。
此前十二核心基础见`T15_TWELVE_CORES_PROGRESS.md`。
复核账本、输入哈希和剩余记录见`eight_current_core_ledger.json`及
`remaining_eight_current_{1,7,31}.bin`。

研究中的同面、双桥、四桥等局部分支不代替完整核心。当前继续研究核心残余及
七个例外轨道；10—18孔暂缓推进但未从完整P6目标删除。
