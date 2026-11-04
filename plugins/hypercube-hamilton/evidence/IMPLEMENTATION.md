# Implementation and real use — 2026-11-04

插件新增一个实质领域技能及数学、失败、复现references；原科学正文/源码/报告/账本保留，A10_ORBIT3完整小证书随仓。其它大流明确省略，范围在archive库存，不声称整题直接重放。

本轮实际从仓库archive复制A10组到独立scratch，运行原独立checker（没有执行生产者）：

```sh
mkdir -p development/evolution/v3-20261104/hypercube/a10-run
cp plugins/hypercube-hamilton/archive/source/research/six_directions/A10_ORBIT3* development/evolution/v3-20261104/hypercube/a10-run/
python3 development/evolution/v3-20261104/hypercube/a10-run/A10_ORBIT3_UNIVERSAL_REVIEW_check.py
```

真实exit0，Python标准库，5.100547秒。读取[完整stdout](a10-replay.log)和[生成结果](a10-independent-result.json)：1024森林短边/无圈/度数/配对与来源对齐，1024合法列，重新计算全部1048576连通位，与保存矩阵逐位一致，158674个1；低列Gauss独立GF2秩1024。未使用生产者高位消元。不是仅metadata或对已存矩阵求秩。

该结果交verify消费A10全称秩准则的有限前提；外部H22秩上界及非零列/路径展开语义仍由正文承担。17496来源池穷尽不是该证明前提，结果字段false保留。

本轮实际核P6_FULL_CLOSURE/P6_FULL_REVIEW、A10完整证明/进口与checker、十二孔极大化正文及已有失败材料；未逐条重审全部96节点证明，没有重跑数百万局部证书。整题P6仍沿原same-family/provisional、显式进口、无Lean状态；不能把本轮A10有限独立复算迁移成全题重算或跨家族验收。

本次复现路径在当前克隆成立且原archive未被程序写入。具体运行记录也在development/evolution/v3-20261104/hypercube/USE.json；源历史pending表述不回写。

## Opus H1/H2修订的实际使用

量词笔误已将原猜想改为任意**匹配**M⊆E(Q_n)。新增`tools/check_forest_rank.py`提供A10同型的参数化有限核验，dim/root/holes/forests/columns显式输入，K/森林记录宽度/列宽度/CKN所需秩由参数推出；不导入固定manifest或保存矩阵，不执行生产者。

实际A10命令见复现reference，exit0，结果[parameterized-a10-result.json](parameterized-a10-result.json)：1024合法森林、1024合法列、1048576位DSU重建、158674个1、低列Gauss rank1024、universal_rank_gate_met=true。先前固定checker逐位比对旧矩阵的证据仍保留。

另以Q3、root7的合法小几何实际检查不同维数/根/孔和非1024门，保存[same-type small result](small-geometry/RESULT.json)及具体二进制输入。该小例仅检查工具参数接口；不是新数学成果。工具支持CKN完整匹配矩阵的A10同型度数约束；十六孔必含边/禁对不是已核字段。新候选发现的原rank.cpp、其22/1024硬编码与改法已点名，未假装通用生产者。
