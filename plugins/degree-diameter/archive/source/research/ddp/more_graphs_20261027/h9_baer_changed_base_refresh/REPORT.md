# Baer早期失败刷新：44项完整无解，无新增

current42398/245889边。首stable410批中source_n<42398的52个失败＋1已接受项，按当前degree筛去9项（8旧失败＋已接受项，合法复制0），冻结44项；不重跑同42398既有失败、nonflat34或nonstable2。

44项全部完成：12个cap2完整exact≤2无解，32个cap1完整无单anchor。0UNKNOWN、0未试、0新图；每个实际mandatory检查的core遗漏为0。source整轮未变化，stale_items.json为空，早期prefix当前legal项均已刷新。P“至少一个早期失败因新路径转可行”被本轮完整0hit反驳。

父＋全部child＋冻结计时2.934614CPU秒，44nativeprepare、0selectedverify（无hit）、0全源BFS/互审/MIP/Lean。delivery59/42398未修改。完整逐项native证据在items/，literal scope见frozen_items.json，当前degree阻塞见degree_skips.json。

本报告仅汇报该stale-prefix刷新，不自行扩大结论。全世界Baer分类、其它同base失败与本结果的fixedsource singlevertex关闭推论由root统一合并；不排cooperative新点、其它blocking sets或rewiring。到此停止。
