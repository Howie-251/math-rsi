# Q4新候选入口：E1修复与实际使用

2026-11-04。按Opus审阅E1实现插件薄工具 `tools/check_q4_candidate.py`，不改冻结archive。只接受同一六块Q4模型的整数Gram因子：dimensions=[240,212,190,187,170,9]、face_root_masks=[0,1,3,6,7]、显式q5_cuts=[]，且状态顺序沿用该模型。任意其它旗定义/状态顺序/块/Q5模型需要对应数学和checker，不因维数相同自动等价。

接口为 `--certificate JSON --work-dir NEW_DIRECTORY [--n N] [--compiler CXX]`。工作目录须不存在且位于冻结archive之外。工具核矩形因子形状、整数、正分母、空Q5、根型和全部64位整数累加安全，计算Q=LL^T，再写target=-1调用原 `certificate_final_q4/verify_local.cpp`。原native重新构建几何与相容完成域，验证90179轨覆盖8421604有序层对，遍历13150453合法标记完成及3312331个对称代表，求真实精确最大值。候选中的upper/decimal/exact_local元数据均不参与求值或验收。

RESULT给约分的C、由本次实际六矩阵对角算出的M_F/M_v、未约分local最大值、worst graph、算术绝对界及可选n≥4的精确有限维界

`C + M_F/(n−3) + M_v(4n−6)/((n−2)(n−3))`。

PASS表示该输入在固定有限模型中已完整核验，不表示优于当前best，也不替代高维平均引理。父流程比较实际C并保留已接受best；有限n必须消费对应修正。工具只核验，不优化，不联网、不另建模型。

## 两个真实输入与命令

从MathRSI仓库根实际运行：

```sh
python3 -B plugins/hypercube-extremal/tools/check_q4_candidate.py \
  --certificate plugins/hypercube-extremal/archive/source/certificate_final_q4/certificate_control.json \
  --work-dir plugins/hypercube-extremal/evidence/candidate-final --n 100
python3 -B plugins/hypercube-extremal/tools/check_q4_candidate.py \
  --certificate plugins/hypercube-extremal/evidence/candidate-inputs/optimized-q4-only.json \
  --work-dir plugins/hypercube-extremal/evidence/candidate-optimized --n 100
```

首项冻结final输入未改；旧optimized原件为 `archive/source/certificates/Q4_optimized_certificate_20261028/certificate.json`。其六块/根型/整数Gram格式相同（矩形因子也合法），但缺少新接口明确要求的q5_cuts字段。`optimized-q4-only.json`只增加q5_cuts=[]，其余所有字段与原件精确相同，尤其矩阵、分母和旧值未变；PROVENANCE/USE记录来源及逐对象比较结果。没有改冻结证书。

两命令均exit0/PASS：

|输入|C|M_F|M_v|
|---|---|---|---|
|final|23662061277957791/40000000000000000|1288810336780277/1250000000000000|324664893404033/625000000000000|
|optimized|236634773493897/400000000000000|103106278757213/100000000000000|26018721256641/50000000000000|

两个不同实际最大值与新矩阵常数证明入口并非硬编码最终证书数值。n=100的精确修正界分别是16940000976891843289/27160000000000000000与237187882750674481/380240000000000000。逐次输入副本、生成整数矩阵、keys、编译/native命令与退出码/日志、RESULT保存在两个candidate运行目录；编译的可执行文件执行后删除，源代码仍在archive。

本次只跑两个有界完整Q4核验，没有重启搜索、完整研究Goal、Lean或优化器。旧final包装器保持原状，继续负责冻结证书重放；新同型候选使用新增工具。全局技能与复现文档由原插件作者接入，本作者未改其文件。
