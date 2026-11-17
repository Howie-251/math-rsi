# 外臂短证的下一边界：4+4和5+4均有局部SAT见证

日期：2026-11-12。本次仅在用户新授权的下一边界范围内运行。**17点共点4+4与18点共点5+4均SAT，且已逐物理子集独立核实。** 因而不能把当前5+5外臂短证的局部排除原样推广为4+4或5+4版本；本结论不声称这些局部染色能扩成75点ambient对象，不单独证明d=28可行。

| 项目 | 17点共点4+4 | 18点共点5+4 |
|---|---|---|
| A | (6,7,8,9) | (6,7,8,9,10) |
| B | (9,10,11,12) | (10,11,12,13) |
| 公共点 | 9 | 10 |
| 入a1外红六 I | (1,2,3,4,5,6) | (1,2,3,4,5,6) |
| 出末B外红六 O | (12,13,14,15,16,17) | (13,14,15,16,17,18) |
| 变量／子句 | 1496／83362 | 1734／120987 |
| 外置Kissat退出码 | 10 | 10 |
| 求解秒数 | 0.06531 | 0.06526 |
| 独立物理子集数 | 131054 | 262125 |
| 完整packet数 | 2380 | 3060 |
| 同端点对数 | 136 | 153 |
| 最长红／蓝路 | 6／5 | 6／5 |
| 物理核验秒数 | 0.8813 | 1.6482 |

两模型均满足：完整rank-3 packet；无R7、B6、weak7；A、B各自红路；冻结两条外红六；A不能结束蓝四，B不能开始蓝四；T=A∪B不作蓝五首末；任何T到T之间无蓝四（内部点任意）；无终于公共点左侧且倒二点在T的红六，无始于公共点右侧且第二点在T的红六。17点模型中央两臂长度均为4，18点模型中央臂长为5和4。

这两条外红六分别接最左A与最右B，**不是原19点内臂试验里均接公共点的两条红六**。未对无标记外端点添加冷性，也不要求所有ambient T在局部诱导域内为真through。全部条件在同一份实际染色上同时核验。

17点完整680个三元颜色在 [shared17/colors.tsv](shared17/colors.tsv)，核验在 [independent-verification.json](independent-verification.json)。18点完整816个三元颜色在 [shared54-18/shared54/colors.tsv](shared54-18/shared54/colors.tsv)，核验在 [shared54-18/independent-verification.json](shared54-18/independent-verification.json)。两份审计均列出全部蓝四、蓝五、红六和每一实际端点对的可达红蓝长度；weak长度和至少9的列表为空。

独立核验脚本不导入生成器：先检实际DIMACS赋值，再导出并重读颜色表，完整枚举大小2至n的每个物理子集，从实际连续三元组重算两色路径，并逐端点检查所有长度组合。两个模型全部16项检查为true。SAT求解时虽保留了求解器proof.drat输出，但它不是UNSAT证书；本次两个案例均无UNSAT声明，不需要DRAT排除信用。

所有计算在权威Linux目录 `/data/ktqiu_hdd/math_agent/reports/n767-neutral29-common-pivot-inner19-20261112/next-boundary` 及其 `shared54-18` 子目录执行。Python为 `/opt/anaconda3/envs/forktqiu3/bin/python3.12`，外置求解器为 `/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`；受控进程保留PID、超时标志、退出码、源／CNF／可执行文件hash。17点控制器／核验PID为1316713／1316799，18点为1316842／1316971；均已完成，没有运行中的任务。

核心颜色SHA256：

- 17点：`2dbe1ef5550ef9bb2e730bd6fbf1ee205f3d0c04f4488ba892c0bcd1e32a04c7`。
- 18点：见 `shared54-18/independent-verification.json` 的 `shared54/colors.tsv` 绑定。

两案的原CNF、原模型、spec、runtime、独立脚本和审计均在此目录；`evidence.tar.gz` 包含两案首次下载时的完整原始证据。只需复算时，可复制到新的Linux目录，分别运行两处 `verify_colors.py`，不需重新求解。没有运行18点严格分离4+4，没有外审，没有主稿修改或新Goal。
