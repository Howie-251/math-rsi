# 阅读顺序与结论范围

当前最大允许点数的结论为 N(7,5,6)=25、N(7,5,7)≤40、N(7,6,6)≤50、N(7,6,7)≤75 和 N(7,7,7)≤76。平面强迫阈值为 ES(7)≤77。74 只用于文中指定子类。

## 阅读顺序

1. 先读 [报告正文](../n7-upper-bounds-20261103.html)，再进入 [当前主稿](CURRENT.md)。八份当前主稿由四份数学原稿与各自的综合更新组成。
2. 优先核对“锁点替换与共同根排除”对 75、76 的证明，再读“依赖核对与单个 through 点排除”中的加强结论，随后读中性域临界层及共同根超额排除。共同根稿中的更强结论有其根序和参数适用范围。
3. [依赖原稿](DEPENDENCIES.md) 保留旧的统一补偿、双向加权、根排除、路径定位及重排等承重论证。[关联历史原稿](HISTORY_INDEX.md) 保留其他沿引用找到的数学原稿。历史稿中的 76、77、78 等阶段性数值均保存原字节，当前结论以报告与上述当前主稿为准。
4. [受限极值 25 的资料](sat-756/README.md) 包含 55 类反例的登记、旧检查回执和 25 点染色见证。各项 SAT 证书检查记录的适用范围见其原始收据。

## 正文与主证明的对应

- 排除 76 点共同根取等构型，得到 N(7,6,7)≤75，见 [锁点替换与共同根排除](source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)。
- 中性域中 w≥1 的子类满足 |X|≤74，见 [依赖核对与单个 through 点排除](source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md)。
- I=S∩T 为空时，|X|+max(|U|,|V|)≤75，见 [中性域临界层及饱和障碍](source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md) 第 1 节。
- 指定 regular 共同根序类中，核心点相对于锁点的重复对应产生额外扣除，见 [共同根超额排除](source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_COMMON_ROOT_EXCESS_EXCLUSION_20261104.md) 第 1–3 节。该类要求 w=0、扩张首末根集合非空并在 I 中共根、共同根避开两侧锁集，以及 I 中两类锁点的指定次序。该结论适用于该类，通常的双向加权界仍为 |X|+w≤76。

## 原始状态与完整性

原件保存了各自的审查及接受状态。后续结构证明仍是尚待独立数学审查的自然语言研究原稿。此次整理核对交付文件的字节、散列、导航和离线显示，未重跑求解或重放证书。

大型 CNF、DRAT 和服务器原文件按 [外部材料索引](sat-756/EXTERNAL-MATERIALS.tsv) 与 [55 类登记](sat-756/55-case-register.csv) 定位。空白包内路径表示该行产物未收录为独立文件。固定公式的历史检查回执有各自的证明绑定。

## 文献与路径

关于 N(7,4,7)=16，见 [Baek 2022 年 v1](../references/Baek-ETV-v1.pdf) 的 Theorem 2.8，平面对应 Theorem 1.7。Theorem 2.7 是杯帽定理，原稿中的旧编号保持原样。split 与下集状态见 [Baek–Balko SoCG 版](../references/Baek-Balko-SoCG-2025.pdf) 第 2、5.1 节。

[source-map.tsv](source-map.tsv) 和 [source-map.json](source-map.json) 对照原仓库路径、包内路径和 SHA-256。正文源位于 source/report.md，数学档案位于 proofs/source-tree，二者分别保存。原稿中的绝对路径及外部链接保持原样，可按映射寻找相应包内副本。
