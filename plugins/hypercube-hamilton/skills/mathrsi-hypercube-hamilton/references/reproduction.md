# Complete bounded A10 replay

本入口重放A10最后五几何轨道的有限全称秩前提。它不是P6全部九层的大证书重算。无需编译器/第三方Python依赖，Python3标准库即可。

checker会写同目录结果，故先从只读archive复制完整A10组到scratch。仓库根执行：

```sh
run_dir=$(mktemp -d)
cp plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3* "$run_dir/"
python3 "$run_dir/A10_ORBIT3_UNIVERSAL_REVIEW_check.py"
```

本通配仅复制A10_ORBIT3组，约数MB，不复制其它巨型流或运行生产者。checker验证manifest原绑定、来源池对应行，检查1024短森林边唯一/短/避0/每点精确度/DSU无圈/端点配对；再核1024列都是K上的完全匹配。

它用新DSU遍历重算1024×1024连通位，逐行对比已存矩阵，然后以低列Gauss独立算GF2秩，忽略生产者高位消元组合。预期输出：

```json
{
  "status": "PASS",
  "selected_forests_checked": 1024,
  "matrix_bits_recomputed_DSU": 1048576,
  "matrix_bits_match_saved": true,
  "matrix_ones": 158674,
  "GF2_rank_low_column_gauss": 1024,
  "producer_elimination_artifacts_used": false,
  "complete_spectrum_exhaustiveness_checked": false
}
```

最后一项false是正确范围：全称证明只需1024合法选中森林满秩，无需证明17496来源池穷尽。存真实退出码、stdout和scratch生成的`A10_ORBIT3_UNIVERSAL_REVIEW_check.json`，正文由[mathematics](mathematics.md)的行空间及非零列论证消费。若缺文件先对照archive库存，不能跳过输入绑定；若位/森林/秩失败，保留见证回原义务，不把rank字段改成期望值。

原完整P6 checker依赖被省略的大流，不能以本仓metadata重放冒作全部P6 ready。本轮A10命令已实际完整执行，见[IMPLEMENTATION](../../../evidence/IMPLEMENTATION.md)。十二孔/十四孔及其它层的代码和报告可读；新重算须先取得其相应完整输入和资源授权。

## 新同型几何：参数化有限森林门

[check_forest_rank.py](../../../tools/check_forest_rank.py)由独立REVIEW_check的DSU/低列Gauss机制薄适配，不导入固定H、manifest或生产者消元。调用者显式提供dim、holes、forests与columns，省略集合用`--omitted`，旧单省点调用保留`--root`。二者择一，不能同时传。顶点标为0…2^dim−1，省略集合U非空且U⊆holes，K为补集，|K|须偶数且至少4；当前格式只用无符号字节，所以dim≤8。森林在U度0、K度1、holes−U度2，短边、无重边、无圈；root入口等于U={root}。列允许K完全图任意边，与CKN矩阵域相符。

设t=|K|，一条森林边数为2^dim−|U|−t/2，故无header记录宽度为该数的两倍bytes；每条column宽t bytes。每边编码两个升序端点（森林/列的边顺序不影响数学）。工具从森林路径重建端点匹配，不相信外部pair表；重建所有行列连通位并独立算GF2秩。

```sh
run_dir=$(mktemp -d)
python3 plugins/hypercube-hamilton/tools/check_forest_rank.py \
  --dim 5 --root 0 --holes 0 1 2 4 8 15 23 27 29 30 \
  --forests plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_rank_selected_forests.bin \
  --columns plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_rank_columns.bin \
  --output "$run_dir/rank.json"
```

`status=PASS`仅表示输入合法且计算完成；读取`universal_rank_gate_met`，只有rank=2^(t/2−1)才满足CKN全称充分门。缺秩输出保留合法池，不能判原命题假。CKN上界是外部文献进口，工具不证明它；行空间/非零列/森林展开仍按mathematics正文核对。工具仅核显式(H,U)的森林/列与秩，不独立规范化或运输H/U；十六孔必含e、禁对R等额外约束没有被工具验证，不能由当前PASS声称满足。

本轮参数化A10已实际执行，重建1048576位、1024合法森林/列、158674个1、独立秩1024，见[结果](../../../evidence/parameterized-a10-result.json)及[日志](../../../evidence/parameterized-a10.log)。它不读旧保存矩阵；先前冻结checker的逐位比对另有原证据。

## 发现候选与原生产者

候选发现由agent负责数学和短森林生成，不由checker冒充。原[A10_ORBIT3_UNIVERSAL_rank.cpp](../../../archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_rank.cpp)的CLI为`rank source_pairs.bin output_prefix.json`，从22-byte匹配流选择独立行，生成选中pair、columns、matrix、pivots、combos及source indices。对应短森林须用选中indices从原forest流提取并保持对齐；rank生产者本身不检查短森林合法。

源码硬编码K的22个标签、`array<unsigned char,22>`、11次交替遍历、1024位bitset与128-byte输出，以及make_basis(22)。新几何同t可在**任务副本**更新K/标签映射，重新生成符合度数的合法短森林池并写其端点pair流；t改变须同步改这些常数、递归基维数和输出宽度，不能只换K。也可以独立实现发现程序，最终由参数化checker核实际森林/列。没有声称原rank.cpp是通用producer，亦不要求其它领域使用rank路线。


## Q7固定计划与多省略核

Q7精选资产的源与缺件说明见[归档入口](../../../archive/q7/README.md)。冻结S3与S2_STRONG计划复验从仓库根运行：

```sh
python3 -B plugins/hypercube-hamilton/archive/q7/source/archive_inventory/replay_key_checks.py
```

需要只核一族时传`--check S3`或`--check S2_STRONG`。此入口在临时工作副本消费随仓输入，原件保持只读。S3有18,049计划，S2_STRONG有19,718；读取真实exit、stderr与运行结果，比较数学字段而不要求CPU秒相等。它复核固定计划与其输入，不重新生成整个历史几何域、不求Hamilton圈、不重算底层rank。两族重叠，计划数不能相加当原Q7覆盖率。可移植命令已在本轮开发副本实际运行，记录见[证据维护](../../../../../development/evolution/v5-q7-20261114/evidence/)。

随仓T63 target04是六核中的一个精确实例，H={0,3,5,10,15,20}、U={0,5,20}、K=Q5\H。运行参数化多省略消费者：

```sh
run_dir=$(mktemp -d)
python3 -B plugins/hypercube-hamilton/tools/check_forest_rank.py \
  --dim 5 --omitted 0 5 20 --holes 0 3 5 10 15 20 \
  --forests plugins/hypercube-hamilton/archive/q7/source/research/seven_directions_continuation/R7_MU3_T63_TARGET04_RANK/target04_forests.bin \
  --columns plugins/hypercube-hamilton/archive/q7/source/research/seven_directions_continuation/R7_MU3_T63_TARGET04_RANK/target04_columns.bin \
  --output "$run_dir/t63-rank.json"
```

本轮已实际完整重算target04，结果见[单核结果](../../../../../development/evolution/v5-q7-20261114/evidence/t63-target04-full.json)；其余五套新核的二进制未随精选归档，不承诺在当前克隆重放六核。此核应有4096合法森林、4096完全匹配列、16,777,216个实际重建连通位和GF2秩4096。工具从真实森林重建26端点的13对配对，不相信独立保存的pair/matrix/rank。`universal_rank_gate_met=true`在完整CKN进口、非零列和展开论证共同供给后，支持该精确(H,U)上任意完全匹配F的29点圈；不能单凭CLI返回升级其它五核或完整T63。

工具不计算某Q7标记集到target04的同构。使用原登记消费者中的共同映射时，核H完整六点与U指定三点一起送对，并运输局部规定边；只匹配H而省点组不同不得调用。原六核完整定理与首选回代见[原主证](../../../archive/q7/source/research/seven_directions_continuation/R7_MU3_T63_NEW_RANK.md)。原独审重算六核与本轮参数化重算单核是不同证据，准确运行范围由本轮[evidence](../../../../../development/evolution/v5-q7-20261114/evidence/)实收结果说明。

本说明只给消费者入口，不自动授权新的生产者、完整Q7搜索或大矩阵批次。输入缺件先读归档清单；一条计划失败先返回其确切桥源/孔/标记字段或数学前提，不能把冻结消费者改成总是返回期望值。

## Q7 完整 E16（≥56 边）随仓核验与外部轨迹边界（v6）

`v6` 新增的完整 E16 包与已合入的 290 份基线导入位于 [archive/q7-e16](../../../archive/q7-e16/README.md)（`v5` 的 `archive/q7/` 保持原样不变）。从仓库根运行（仅需 Python 3 标准库）：

```sh
python3 -B plugins/hypercube-hamilton/archive/q7-e16/check_e16_bundle.py
```

该入口在不修改只读 `archive/q7-e16/` 的前提下完成四项检查：
1. 逐个核对随仓全部 261 份 E16 原件与全部 290 份已合入基线导入文件的字节长度和 SHA-256；
2. 独立复算 `μ=0` 大面 `19 + 98 + 72 = 189` 行独立孔表的奇偶性、非短邻性与位串哈希 `0f6dce217ea…`，并核对 `MU0_STRUCTURED_JOINT.pb`（`100,051` 条约束）；
3. 在临时副本实际执行 `MU0_A0_BASIS_REVIEW_check.py`（穷举 4,950 带标号对 → 19 个 `S6` 轨道）、`MU0_A0_PLANS_REVIEW_check.py`（19 条 `a=0` 计划）、`MU0_A12_BASIS_REVIEW_check.py`（`98 + 72` 个 `S6` 轨道）及 `Q6_A8_FULL_REVIEW_check.py`（41 个残余轨道与奇纤维）；
4. 若当前 Python 环境装有 `ortools`，额外从 `MU0_JOINT_NECESSARY.pb` 运行 `MU0_STRUCTURED_JOINT.py` 校验逐字节重建。

**省略的 10 份大 `.cnf`/`.drup` 证书说明：** `even.drup`（201.55 MB）、`odd.drup`（109.65 MB）等全部 10 份 E16 CNF/DRUP 文件（共 532.49 MB）与 Windows `drat-trim.exe` 按 `<50 MiB` 普通 Git 规则统一省略并逐项登记在 [q7-e16/INVENTORY.json](../../../archive/q7-e16/INVENTORY.json)（随仓保留官方 `drat-trim.c` 源码、全部 `.pb` 源模型、CNF 编译器与原验证回执）。哈希清单不代替 DRUP 轨迹重放；完整轨迹重放需从外部研究归档 `R-S-n=7(2).rar` 提取该 10 份文件并用编译后的 `drat-trim` 核验。本轮实际执行输出见 `development/evolution/v6-c4free-rs7-20261117/checks/q7-e16.json`。
