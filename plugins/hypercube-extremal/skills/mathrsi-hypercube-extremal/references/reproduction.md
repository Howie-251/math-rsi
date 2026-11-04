# Final Q4 certificate replay

从仓库根调用，Python仅标准库，须有现成g++或clang++支持C++17。无需NumPy/SciPy/LP。程序从archive读取，输出全放工作区。

```sh
run_dir=$(mktemp -d)
python3 plugins/hypercube-extremal/archive/source/tools/verify_final_q4.py --work-dir "$run_dir"
```

包装器重建六个LLᵀ整数矩阵，验证q5_cuts为空、维数/分母/安全小数/对角常数、64位绝对安全；编译原verify_local.cpp并从几何枚举完整域。预期末尾含：

```text
PASS: independent coverage of all 8421604 ordered Q3 layer pairs by 90179 disjoint automorphism orbits.
PASS: all 13150453 legal marked completions enumerated.
PASS: all 3312331 symmetry-reduced representatives verified by direct integer counting.
EXACT_MAX 283944735335493492 / 480000000000000000
WORST_GRAPH 3602350111
FULL_DOMAIN_VERIFICATION_PASS
```

`--prepare-only`明确不执行全域，不能用它替代以上成功。`--compiler /path/to/compiler`选择编译器；编译失败是运行环境问题，不当作数学失败。真正整数得分超出阈值时保留具体图并回候选生成；不改阈值伪造PASS。

读取退出码及完整日志，保存编译器/工作目录和覆盖范围。得到的结论是这份冻结证书的全部局部式；高维平均仍依赖[mathematics](mathematics.md)。包中的大优化系数表不必重建，也没有被此命令使用。

本轮实际重放：[IMPLEMENTATION](../../../evidence/IMPLEMENTATION.md)。若准备接续搜索，先复制需要的科学源码/输入到新任务scratch；原程序可能覆写同目录JSON，不能对archive原件执行生产者。被省略的系数表见[库存](../../../archive/INVENTORY.json)，当前仓库不宣称所有历史优化可直接重跑。

## 新候选的完整精确接受

冻结`verify_final_q4.py`刻意绑定历史C/M_F/M_v，只用于重放旧证书。新候选使用插件工具，参数不是新的数学模型声明：必须仍为**相同状态顺序**的240/212/190/187/170五根面块+9顶点块，根掩码0/1/3/6/7，整数矩形Gram因子，显式`q5_cuts=[]`。

```sh
run_parent=$(mktemp -d)
python3 plugins/hypercube-extremal/tools/check_q4_candidate.py \
  --certificate plugins/hypercube-extremal/archive/source/certificate_final_q4/certificate_control.json \
  --work-dir "$run_parent/candidate" --n 100
```

work-dir须为尚不存在的目录。工具检查形状/整数PSD/64位安全，以原C++的target=-1模式完整重建几何、求所有合法图的最大值；`RESULT.json`返回当前C/M_F/M_v和可选n≥4精确修正界，不消费候选自报bound。输入副本、矩阵、keys及编译/执行命令和输出留在该目录。维数相同但状态置换不同也不能直接用；模型变化须证明对应关系或修改几何checker。

本轮两份不同实际候选均已重放：final给23662061277957791/40000000000000000；历史optimized给236634773493897/400000000000000，并各自重算不同M_F/M_v。[完整命令与结果](../../../evidence/candidate-inputs/README.md)保留旧optimized缺q5_cuts字段的副本规范化记录，原件未改。

## 接续搜索：可物化，后续重建及优化本轮未执行

原包按SHA去重，许多逻辑路径只在原inventory中。它的materialize_research会读取所有stored_path，遇本仓省略五表即失败。替代入口复制现有原件，恢复所有可用别名，并明确跳过外层库存登记的五表；不是隐藏缺件后启动搜索。

```sh
search_dir=$(mktemp -d)
python3 plugins/hypercube-extremal/tools/materialize_search.py "$search_dir"
cd "$search_dir/research/optimization_20261028_q4"
python3 prepare_data.py
g++ -O3 -std=c++17 -UNDEBUG generate_models.cpp -o generate_models
./generate_models
g++ -O3 -shared -fPIC -fopenmp evaluate.cpp -o evaluate.so
cd ../q5_empty_moment_20261028
python3 column_lift.py --no-q5 --rounds 20 --prefix replay_control
```

`prepare_data.py`从keys恢复Q3索引pair_index.bin和edges/vertex_flag_codes；generate_models从keys/edges/pair_index/face_pair_lookup重建graphs、shadows、face_indices、vertex_indices，必须在该cwd执行。其完整表约451MB，不能用抽样表替代。已有face_block/full_C/full_meta等逻辑别名由物化恢复，不必再次生成。

搜索需NumPy/SciPy，且column_lift导入SciPy私有`scipy.optimize._highspy._core`；历史NumPy2.4.2/SciPy1.17.0不保证当前环境兼容。evaluate.cpp使用OpenMP，须选择支持`-fopenmp`的GNU g++或正确配置OpenMP的Clang；macOS系统`g++`实际常为Apple Clang，不能据名称假定可编译。model.py以ctypes加载固定名evaluate.so，使用本机C++/Python一致的ABI。

模型从相邻optimization目录读q5control_best.npz，--no-q5同时禁止初始额外cuts和动态Q5切面；目录名不扩大模型范围。历史certify_lift.py会覆写certificate.json/result.json，只能在此新副本按源码导出同型整数Gram候选，随后用上节check_q4_candidate完整重验，保留已接受best。

本轮实际仅运行物化：278逻辑路径恢复，恰好跳过五表，脚本自身检查19项准备/生成/evaluator/model/全部face块/初始化及column_lift必需别名，missing_required_aliases为空，[脚本原生结果](../../../evidence/materialize-search-v2-result.json)。**没有执行上述表重建、共享库编译或优化**，不声称搜索运行时已就绪；运行前按当前任务预算与真实依赖决定，不自动重启旧研究。
