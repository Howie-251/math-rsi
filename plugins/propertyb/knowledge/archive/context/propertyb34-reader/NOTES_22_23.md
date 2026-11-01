# 22／23点阅读章节的来源与本轮编辑说明

2026-10-14。章节 `CHAPTER_22_23.md` 为单卷 HTML 的完整中文阅读稿，来源是既有规范候选与保存的精确证书；本轮没有恢复研究 Goal、启动搜索或运行 Lean。

## 主要来源

- `context/propertyb34/round01/middle-math/COMPLETE_TWENTYTWO.md`
- 同目录 `CANDIDATE_TWENTYTWO_SEVEN.md`、`CANDIDATE_LOW_BRANCHES.md`、`CANDIDATE_ONE_TWO_LOW_23.md`、`CANDIDATE_FOUR_FIVE_LOW_23.md`
- `context/propertyb34/round01/high-math/CANDIDATE_THREE_LOW_23.md`
- `context/propertyb34/round01/twentythree-seven-math/N23_MIN_SEVEN.md`
- 同目录 `LEAN_SELECTION_SIMPLIFICATION.md`、`N23_COMPLETE_DISPATCHER.md`、`FEW_SIX_FORMAL.md`、`SELECTION_FORMALIZATION.md`
- `context/propertyb34/round01/middle-lean/FOUR_PROMOTION_COVERAGE.md`
- `context/propertyb34-hour1-20261013/MIDDLE_PROGRESS.md`

二十三点零六度点采用新简化：六点总权最小的交换论证、偶数性和等号饱和，足以得到所需实际八度单位外点。不依赖旧的全局两个 K7 分类。

正文没有把旧候选末尾的历史“仍需跨家族审阅”等状态混入当前证明；Lean 范围由整书附录统一说明。22点没有引用未实际使用的 weighted-overlap quota。

## 原始JSON直接提取的数值

只读取各行 `final_bound`，无该字段时读 `joint.bound`，再无则读 `bound`，用精确 Fraction 求最大值。没有重做布局搜索。

- `THREE_LOW_FULL_22.json`：687/687 严格，最大 1518220083/1519375000。
- `SECOND_MIXED22_2_7_8.json`：765/765，最大 6263/6435。
- `SECOND_MIXED22_2_8_8.json`：12/12，最大 4055/4368。
- `SECOND_MIXED22_1_7_8.json`：1060/1060，最大 11233/11440。
- `MIXED_LOW_23.json`：36/36，最大 171377549549/171599931360。
- `ALL_FIVE_GRAPH_RESULTS.json`：29个完整严格图形共1601份证书，最大12153/12155；五个未全严格图形的边掩码分别为 `[3]`、`[3,5,6]`、`[9,6]`、`[3,5,9,6,10,12]`、`[17,6,10,12]`，正文转为 K2+3I、K3+2I、2K2+I、K4+I、K3+K2。
- `MIDDLE_DOUBLE_RESULTS.json`：22点七度共度4至7最大20421/20995；23点七度共度5至7最大39717/41990。

其余界和分类数量与上述规范候选逐项对照。

## 七低点收尾的解析简化

旧稿 `CANDIDATE_LOW_BRANCHES.md` 使用 `EXTEND_LOW_23_7.json` 的1432次完整提升及全六投影残型过滤，结果为空。阅读稿用一个直接双计数替代此最终空表检查，原表链接仍留作补充。

已成立前提：在不可染假设下，每个六低子集的实际迹计数都属于唯一残型；该残型恰有两条三元迹边，且没有至少四元的迹。

取七低集 S。若一条原始边在 S 上交四或五点，可选包含这些点的六子集，得到禁止的四/五元迹，故所有 S 迹至多三点。设原始边中 S 迹恰三元者有 b 条（按实际边计重数）。每条在七个删点视图中保留三元迹四次，每个视图恰两条，故 4b=14，矛盾。较小迹不贡献三元迹，较大迹已排除，全部贡献已覆盖。

主代理已独立核对并授权正文采用，认为这是既有共同块族删点守恒的直接实例。没有声称此新表述已经 Lean 形式化或由外部模型新审阅。
