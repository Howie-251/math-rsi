# 唯一一因子骨架候选：同 index 路由障碍

按 `PLAN.md` 及 `generate.py` 完整展开了一个、且仅一个指定候选：groups 为 `Z25∪{∞}`，25 个圆桌一因子，class `c=t mod5` 在双方同 index blocks `c,c+1,c+2` 上连接，bonus 颜色 0–4 再加 `c+3`。端口唯一采用按 `(对端group,对端block,color)` 排序后，以零基 rank 模四分配。不改动原 650 图或前一个 676 图。

度数公式和完整对象都成立。每 block 的基础 15 个关联加一个 bonus 关联恰为 16，每个 leaf port 得四条外边。520 个 leaves 形成 4 正则图，加 26 套树后是 676 点、1,690 边的简单连通 5 正则图。325 个 group pairs 中，260 对恰有三条叶边、65 对恰有四条；没有遗漏 group pair。

`candidate.edges` 经通用全源检查器及独立读取边表的 Python 全源 BFS 验证，直径为 **8**，共有 **103,041** 个无序点对距离超过五。因此此候选不构成 (5,5) 新下界，且缺陷明显多于前一个 676 候选的 2,172 对。head–head 通过不能解释为整体改善。

| 点对类型 | 距离超过五的无序对 |
|---|---:|
| head–head | 0 |
| head–block | 564 |
| head–leaf | 855 |
| block–block | 520 |
| block–leaf | 27,992 |
| leaf–leaf | 73,110 |
| 合计 | 103,041 |

全部有序距离谱（距离 0 至 8）为 `(676,3380,12424,37464,70520,126430,158822,47030,230)`。偏心率分布为 6:26 个顶点、7:500 个、8:150 个。

本实例的承重问题是每条叶边均保持 block index，因此普通叶路不能混合这五个 index。对已保存全部坏对作分类，无需重复 BFS：73,110 个 leaf–leaf 坏对中，**73,060 个为异 index**，仅 50 个为同 index。异 index 坏对的距离分布是 6:50,422、7:22,523、8:115；同 index 50 对全在距离六。这与父代理和数学代理正在整理的同 index 全骨架障碍相符；一般路由证明由独立的 `ROUTING_DIAGNOSIS.md` 给出，本报告不把一次候选计算外推到未证明范围。

完整颜色、块关联、端口关联和标签规则保存在 `candidate.parameters.json`；所有坏对在 `candidate.bad_pairs.tsv`；全图/分型距离谱、每点缺失数、26 个 head 距离谱在 `candidate.independent_validation.json`；异 index 分解在 `index_failure_diagnosis.json`。

实际主 profile 成本：生成 0.03415 CPU 秒，通用全源检查 0.01462 CPU 秒，独立 Python 检查和分型 0.53947 CPU 秒，共 0.58824 CPU 秒；另对已存坏对的轻量分类约 0.06 秒。总计远低于 30 CPU 秒上限。生成和分型程序返回 0；通用检查器返回 1，表示直径五不合格。没有部分范围、未退出进程、后续随机修复或新端口方案。

复算命令：

```text
python research/ddp/m2_factorization676/generate.py
computations/ddp/verify_graph research/ddp/m2_factorization676/candidate.edges 5 5
python research/ddp/m2_factorization676/validate.py
```
