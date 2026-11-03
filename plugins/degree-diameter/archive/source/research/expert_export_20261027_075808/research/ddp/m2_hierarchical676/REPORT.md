# 单个 676 点层次扩张：完整验收未达到直径五

按 `PLAN.md` 和确定性 `generate.py`，从公开 650 图新增一个 group head、五个 block heads 和二十个 leaves。只生成了一个候选，无随机种子、候选队列或后续修复。

40 条删除边确实构成 matching，80 个旧叶端点互异，且全部原单删损伤均为 45。所选端点覆盖全部 25 个旧 groups：20 组各三个端点，五组各四个。每对旧 groups 原有叶边删除后至少保留两条，强于要求的一条。每个新 leaf 接四个旧端点，新增树按五个 blocks、每个四个 leaves 排列。

`candidate.edges` 是完整 676 点、1,690 边对象。所有顶点均为五度；图简单、连通。新增标签为 head 650，blocks 651–655，leaves 656–675。原边序、40 条删除边、每个新 leaf 的四个旧邻居以及全部树边保存在 `candidate.parameters.json`。

独立通用 `verify_graph` 和重新读完整边表的 Python 全源 BFS 一致得到直径六、2,172 对距离超过五。因此这个对象不是新的 (5,5) 下界。

| 点对类型 | 距离超过五的无序对 |
|---|---:|
| head–head | 0 |
| head–block | 6 |
| head–leaf | 170 |
| block–block | 14 |
| block–leaf | 776 |
| leaf–leaf | 1,206 |
| 合计 | 2,172 |

按新旧分解：old–old 1,309 对，new–old 863 对，new–new 0 对。更具体地，新 head–旧 block 有六对，新 head–旧 leaf 有 36 对，新 block–旧 head 为零，新 block–旧 block 有 14 对，新 block–旧 leaf 有 262 对，新 leaf–旧 head 有 17 对，新 leaf–旧 block 有 81 对，新 leaf–旧 leaf 有 447 对。旧 head–旧 leaf 有 117 对，旧 block–旧 leaf 有 433 对，旧 leaf–旧 leaf 有 759 对。

全部有序距离谱（距离 0 至 6）为 `(676,3380,13520,53622,183518,197916,4344)`。五个顶点偏心率为五，其余 671 个为六。完整距离分型、新增 26 个顶点的距离谱、每点缺失数保存于 `candidate.independent_validation.json`；全部 2,172 个坏对及原标签保存在 `candidate.bad_pairs.tsv`。

这次实例确实实现了预置层次、全部 head–head 覆盖与度数守恒，但它们未控制其他类型的距离。特别是删除旧叶边造成 1,309 个旧–旧坏对，新增连接没有全部修复；新旧不同层之间也有缺失。这仅诊断这个确定性候选，不排除整个层次构造机制。

实际成本：生成 0.07104 CPU 秒，通用检查 0.01279 CPU 秒，独立 Python 全根检查及分型 0.44737 CPU 秒，总约 0.53120 CPU 秒，低于本次 30 CPU 秒上限。生成程序返回 0；通用检查器返回 1，含义是直径五不合格；独立分型程序返回 0，表示完整验收完成。没有超时、部分范围或未完成队列。

复算命令（运行生成命令会确定性重写本候选文件，并不修改原 650 图）：

```text
python research/ddp/m2_hierarchical676/generate.py
computations/ddp/verify_graph research/ddp/m2_hierarchical676/candidate.edges 5 5
python research/ddp/m2_hierarchical676/validate.py
```
