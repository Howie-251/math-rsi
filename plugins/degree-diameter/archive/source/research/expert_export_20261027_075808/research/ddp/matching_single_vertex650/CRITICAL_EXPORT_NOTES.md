# 650 点源图的完整单删边损伤列表

2026-10-26。源为 `research/ddp/m1_degree5_transfer/rithwik650_source.edges`，实际头 `650 1625`。仅复用已核对的五层共同边 DP 导出数据，不生成候选、不执行搜索或重复单删边 BFS，不修改旧证据。

`critical_upto5_pairs.txt` 首行为 `650 1625 110125`。随后恰 1625 行，每行为 `eid count encoded_pair...`；eid 从 0 起，与源边表顺序相同，编码为 `x*650+y`、x<y。每个列表完整包含删除该边后距离超过 5 的所有无序点对，包括原距离小于 5 的损伤；列表严格递增、无重复。全部 1625 个 count 与先前 `source650_diagnosis/diagnosis.edge_damage.tsv` 逐项相等。

代码 `export_critical_pairs.cpp` 从已使用的 650 诊断 DP 派生，冻结每一层并对边集合去重。递推证明见 `research/ddp/m1_matching_joint/CRITICAL_UPTO5_EXPORT.md`。范围仅为各条边单独删除的损伤，不能当作多边共同删除的完整损伤集合。

终态记录 `critical_export.json`：COMPLETE、退出码 0，0.047721 CPU 秒 / 0.0507145 墙钟秒。无在途作业。

复现已编译程序：

```
research/ddp/matching_single_vertex650/export_critical_pairs research/ddp/m1_degree5_transfer/rithwik650_source.edges research/ddp/matching_single_vertex650 29
```
