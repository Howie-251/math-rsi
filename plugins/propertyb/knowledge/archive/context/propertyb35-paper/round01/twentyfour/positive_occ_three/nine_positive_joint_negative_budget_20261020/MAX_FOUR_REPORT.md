# 九正门四重点子域交付

完整正文为 [NINE_POSITIVE_OCCURRENCE_FOUR.md](NINE_POSITIVE_OCCURRENCE_FOUR.md)。九正四集、至多三负三、负三加负四至多二十、L≤18、D7，存在正出现恰四次的点时，全部输入可修复。

复用旧七个E=3型和86个E≥4型，不生成新正族域。CHECK_MAX_FOUR.py 从旧七型重建实际点，直接横截与32项容斥一致，再计算不同二目标扩展前三项、最大三目标扩展，对每型540份完整负预算参数全部严格。E3最小余量23，旧86宽堵155<178；M2零宽堵65<80；M2≥7三横截14>12。因此全部四重点分支最小计数余量2。

运行：

    python3 context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/CHECK_MAX_FOUR.py

原始结果 CHECK_MAX_FOUR.json；确定性新参数复算不冒充跨模型验收。九正一般门仍剩最大正出现恰三的分支。
