# Implementation and real use — 2026-11-04

本插件新增一个实质领域技能及数学/失败/复现references；Root将它接入现有prepare/route-loop/prove/verify/handoff。原件218文件/57.4MB随仓，不需要作者原目录完成最终Q4核验。

本轮实际调用（仓库根；执行到development下的scratch）：

```sh
python3 plugins/hypercube-extremal/archive/source/tools/verify_final_q4.py --work-dir development/evolution/v3-20261104/hypercube/erdos-run
```

真实exit0，Python标准库、`/usr/bin/g++ -O3 -std=c++17 -UNDEBUG`编译原checker。3.436秒含Gram重建/编译/完整枚举，不能当作整个研究时间。完整stdout保留[final-q4-replay.log](final-q4-replay.log)。

核验六组整数Gram、零Q5项、64位安全；独立几何覆盖8421604有序Q3层对/90179轨道，枚举13150453合法补全、计分3312331切片代表，最大283944735335493492/480000000000000000，最坏图3602350111。没有使用大优化表，没有只跑prepare-only。

此使用关闭冻结最终证书的有限全域可移植重放义务，返回verify时仍需消费高维平均证明。整理层实际对照了guide02、最终包装器/完整输出、原报告和关键history；本轮没有重跑优化、跨模型数学终审或Lean，不提升原数学保证。原理论全文及搜索历史随archive保留，未读无关历史不称已审。

父caller读取该日志后应接受局部score有限前提，并保留解析桥梁及其文献/人工审阅状态。这个有界用例验证当前路径、输入和输出可消费；不声称MathRSI整体成功率或速度已评测。

## Opus E1/E2修订的实际使用

冻结verify_final_q4绑定历史值，只承担旧证书重放。新同型候选由[check_q4_candidate.py](../tools/check_q4_candidate.py)以target=-1完整求最大值，重算当前C/M_F/M_v；两份不同证书的实际结果与最小字段规范化见[candidate-inputs](candidate-inputs/README.md)，不再将冻结wrapper写作通用候选接口。

archive省略项已据实际库存更正：5个生成bin，合计451339260 bytes。原materialize要求其全部存在，不适用于当前精简副本。新增[materialize_search.py](../tools/materialize_search.py)实际在临时目录恢复278逻辑文件，恰好跳过这5项，prepare_data/generate_models/evaluate/model/full_meta/full_C/keys别名均存在，exit0。[输出](materialize-search-result.json)保留，临时副本已删除。

后续prepare_data、生成四表、编译OpenMP evaluate.so及column_lift --no-q5的cwd/参数/依赖已写入复现reference；本轮未执行表生成或优化，不声称NumPy/SciPy私有API或OpenMP环境已就绪。原archive科学文件未改。

Opus003记录修正：旧`materialize-search-result.json`的`key_aliases_present`由作者在物化后另一次读取追加，并非当时脚本原输出；旧文件原样保留。现脚本自身枚举并检查后续必需的19项别名，输出`required_aliases_checked`、`missing_required_aliases`及`key_aliases_present`，有缺失即非零退出。新临时目录实际物化exit0，[v2原生结果](materialize-search-v2-result.json)无缺失，[完整stdout](materialize-search-v2.log)由本次脚本直接产生；副本随后删除，未生成五表或运行优化。
