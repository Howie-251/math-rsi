# 八孔当前状态

2026-11-01。用户要求优先尽快完整关闭八孔。**完整八孔已关闭；完整T15及完整P6仍未证。**

当前已由独立GPT-6.1-sol high审计通过的完整T15硬轨道有24个：
`[0, 1, 2, 4, 5, 7, 8, 10, 13, 14, 15, 18, 19, 21, 23, 24, 25, 27, 31, 32, 35, 37, 38, 44]`。保证等级为相对于显式导入定理和有限证书的same-family/provisional。

当前剩余0个规范八孔配置，其中0个有(2,1)投影，
0个是原七轨道例外中的未关闭项。按规范目标1、7、31，剩余分别0、0、0。
这些是孔配置数，不是匹配数；每个已关闭轨道的量词覆盖其全部实现匹配。

当前整轨道(2,1)方案还需0个核心，剩余充分集为`[]`；空集表示这一分支已全部关闭。
最少轨道数未必代表最快证明路线：18、21、25三个核心可以替代困难核心26，
这条替代路线已在三个核心完整独立审计PASS后计入。任何候选核心只在其完整独立审计PASS后计入。

全部50个例外已由Q5自由孔邻点丰度、严格EP0换元和core1/core4关闭；234个可选边投影及50个规范几何均经独立审计核对。
完整自由终点分支早已关闭，当前剩余是被覆盖终点。

当前纳入的完整核心审计：`['T15_ALTERNATIVE_GROUP_REVIEW.json', 'T15_CORE0_FULL_REVIEW.json', 'T15_CORE15_FULL_REVIEW.json', 'T15_CORE1_FULL_REVIEW.json', 'T15_CORE23_FULL_REVIEW.json', 'T15_CORE24_FULL_REVIEW.json', 'T15_CORE27_FULL_REVIEW.json', 'T15_CORE4_FULL_REVIEW.json', 'T15_CORE5_FULL_REVIEW.json', 'T15_CORE8_FULL_REVIEW.json']`。
EP0后果审计：`EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json`；完整八孔汇总审计：`EIGHT_HOLE_FULL_REVIEW.json`。
此前十二核心基础见`T15_TWELVE_CORES_PROGRESS.md`。
复核账本、输入哈希和剩余记录见`eight_current_core_ledger.json`及
`remaining_eight_current_{1,7,31}.bin`。

完整八孔的精确陈述与依赖见`EIGHT_HOLE_FULL_CLOSURE.md`。
10、12、14、16、18孔仍保留于完整P6目标；只证明恰好18孔并不蕴含八孔。
