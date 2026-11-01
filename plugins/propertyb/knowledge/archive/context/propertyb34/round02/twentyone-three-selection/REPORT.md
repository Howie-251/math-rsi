# 三七度点：实际五锁选择与共同单位邻居

本次完成的是21点、34边、最小度7、恰有三个七度点且假设不可二染色时的实际选点接口；不是整个 r=3 染色分支。

取实际三七度点嵌入 f，并令 L 为八度点集。已有度数预算给出 |L|≥13。每个七度中心对八度点的共度是1或2，三个中心的总超额至多24。记 P(u) 为与八度点 u 共度1的七度中心索引子集，则 Σu|P(u)|≥3|L|−24≥15。三个元素的所有子集大小总和为12，因此必有两个不同八度点具有同一个非空模式。它们与三七度点的全部共度分别相同。

更强地，任一七度中心的共同单位八度邻居至少 |L|−8≥5。已有 unit_eights_structure 因而把上述两八度点的相互共度直接固定为2，而不只是≤2。这消除了旧五锁数值域中末二共度1的半支。根代理正在核查缩小后的完整代表覆盖，本记录不代替该覆盖。

源码依赖顺序：

1. TwentyOneSevenThreeSelectionWeights.lean：有限加权鸽巢；全部非空模式权重12，排除全模式后的权重9。
2. TwentyOneSevenThreeSelection.lean：实际 H 的超额预算、模式重合及共度2；select 从原假设构造实际三七度及两八度点。
3. TwentyOneSevenThreeSelectionCommon.lean：在额外残型条件“内部三七度共度均2，所有重复非空模式均为全模式”下，外部超额降到18，推出至少四个与三七度均单位相交的实际八度点，且这些八度点两两共度2。
4. TwentyOneSevenThreeSelectionFive.lean：select_five 输出实际 Fin5 嵌入，度数 [7,7,7,8,8]，后两点具有相同非全2模式，后两点共度2，全部锁对共度≤2。pair_eq_two 可单独供后续残型接口调用。

轻量联合探针 ThreeSelectionFiveProbe.lean 已通过，11.06秒，峰值约1.33 GiB；五个关键导出的公理依赖仅 propext、Classical.choice、Quot.sound。原始日志在 ../twentyfive/three-selection-five-r2.log。正规 Lake 构建由根代理统一排队；未把本机轻量通过写成完整 T34 验收。
