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

[check_forest_rank.py](../../../tools/check_forest_rank.py)由独立REVIEW_check的DSU/低列Gauss机制薄适配，不导入固定H、manifest或生产者消元。调用者显式提供dim、root、holes、forests与columns。顶点标为0…2^dim−1，root∈holes，K为补集，|K|须偶数且至少4；当前格式只用无符号字节，所以dim≤8。森林在全顶点减root上：K度1、holes−root度2，短边、无重边、无圈。列允许K完全图任意边，与CKN矩阵域相符。

设t=|K|，一条森林边数为2^dim−1−t/2，故无header记录宽度为该数的两倍bytes；每条column宽t bytes。每边编码两个升序端点（森林/列的边顺序不影响数学）。工具从森林路径重建端点匹配，不相信外部pair表；重建所有行列连通位并独立算GF2秩。

```sh
run_dir=$(mktemp -d)
python3 plugins/hypercube-hamilton/tools/check_forest_rank.py \
  --dim 5 --root 0 --holes 0 1 2 4 8 15 23 27 29 30 \
  --forests plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_rank_selected_forests.bin \
  --columns plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_rank_columns.bin \
  --output "$run_dir/rank.json"
```

`status=PASS`仅表示输入合法且计算完成；读取`universal_rank_gate_met`，只有rank=2^(t/2−1)才满足CKN全称充分门。缺秩输出保留合法池，不能判原命题假。CKN上界是外部文献进口，工具不证明它；行空间/非零列/森林展开仍按mathematics正文核对。这里限定A10同型度数；十六孔必含e、禁对R等额外约束没有被工具验证，不能由当前PASS声称满足。

本轮参数化A10已实际执行，重建1048576位、1024合法森林/列、158674个1、独立秩1024，见[结果](../../../evidence/parameterized-a10-result.json)及[日志](../../../evidence/parameterized-a10.log)。它不读旧保存矩阵；先前冻结checker的逐位比对另有原证据。

## 发现候选与原生产者

候选发现由agent负责数学和短森林生成，不由checker冒充。原[A10_ORBIT3_UNIVERSAL_rank.cpp](../../../archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_rank.cpp)的CLI为`rank source_pairs.bin output_prefix.json`，从22-byte匹配流选择独立行，生成选中pair、columns、matrix、pivots、combos及source indices。对应短森林须用选中indices从原forest流提取并保持对齐；rank生产者本身不检查短森林合法。

源码硬编码K的22个标签、`array<unsigned char,22>`、11次交替遍历、1024位bitset与128-byte输出，以及make_basis(22)。新几何同t可在**任务副本**更新K/标签映射，重新生成符合度数的合法短森林池并写其端点pair流；t改变须同步改这些常数、递归基维数和输出宽度，不能只换K。也可以独立实现发现程序，最终由参数化checker核实际森林/列。没有声称原rank.cpp是通用producer，亦不要求其它领域使用rank路线。
