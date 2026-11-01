# 25点33边：真实六锁/八锁结构归约已验证

日期：2026-10-08。源码：`formal/Aris4Math/ThirtyThree/TwentyFiveStructure.lean`。

## 交付接口

命名空间为 `Aris4Math.ThirtyThree.TwentyFiveStructure`。

主结构定理 `exists_six_large_or_eight_triples` 接受实际H、25点、恰33边、点对覆盖，返回以下两者之一：

1. 存在六点锁集S，全部顶点度6，`H.UnitCodegrees S`，且实际 `H.multiTraces S` 含至少四点的块。
2. 存在八点锁集S，全部顶点度6，`H.UnitCodegrees S`，每个实际多点块至多三点，实际三元块至少5个，并且每个锁点都属于某个三元块。

它没有使用14型分类或数值界作为前提，因而可作为后续六锁大块/八锁分类的真实入口。所有对象沿用旧 `Traces`、`TraceRecovery` 中的 `UnitCodegrees`、`multiTraces`，没有引入第二套超图或块定义。

## 已闭合的计数链

- `sixVertices_card_ge_ten`：由最小度6和总度165，证明真实六度点至少10个。
- `exists_ten_six_degree_unit`：选出真实十点W，并使用旧的通用25点六度刚性引理证明其点对共度1。
- `trace_pairs_sum`：真实块的二元子集族是W全部点对的无交分解，因此 Σ_B C(|B|,2)=C(|W|,2)。
- `trace_incidence_le_six`：实际块数通过每个点的真实degree分拆，得到 Σ_B |B|≤6|W|。
- `ten_le_triple_count`：当|W|=10且所有块大小2或3，恒等式 2ΣC(|B|,2)=Σ|B|+3t 给出90≤60+3t，所以t≥10。此为一般计数证明，不枚举块族。
- `eight_subsets_containing_triple`：固定三元块B包含于恰21个八点子集。证明显式建立 S↦S\B 到(W\B)五点子集的双射，再内核计算C(7,5)=21。
- `exists_eight_subset_preserving_five_triples`：交换两次有限求和，全部45个八点子集保留的三元块总计21t≥210；若每个至多4，总计至多180，矛盾。
- `retained_trace` / `exists_eight_actual_triples`：保留下来的完整三元块确实是原H在新S上的实际截面，不是抽象子族。
- `every_point_in_triple`：八锁中若某点不属于三元块，则至少需要七个不同的二元块覆盖其余锁点；这些都来自不同含该点的实际边，与度6矛盾。

大块分支将原真实大块补入一个六点子集，保留其完整实际截面。小块分支将平均选出的八点子集和全部上述结论一起返回。

## 后续分类对接

对返回的八点S，使用已有 `TraceRecovery.labelBlock S label` 将

    (H.multiTraces S).filter (fun B => B.card = 3)

映到Fin8。三元性、至少5个、每点被覆盖来自本模块；任意不同块交至多一点来自旧 `H.multiTraces_inter_card_le_one S unit`，标签映射保持这些性质。然后由分类代理补齐14型覆盖与对应实际数值剖面。

本模块没有重复实现14型分类，没有证明25点Property B，也没有修改旧文件。

## 实际核验

使用项目现有锁定Lean环境，在 `formal/` 运行：

```sh
lake build Aris4Math.ThirtyThree.TwentyFiveStructure
lake env lean ../context/propertyb33/round01/twentyfive-structure/ImportAudit.lean
```

模块构建及独立导入审计均退出0。日志为 `build.log`、`import-audit.log`；独立审计实际将最终结构定理用于Fin25、33边输入。

打印的关键声明传递公理只有 `propext`、`Classical.choice`、`Quot.sound`。没有 `sorryAx`、新增公理或 `native_decide`。首次标量choose化简及截面等式重写遗漏的失败记录保存为 `build-initial-error.log`、`build-subset-error.log`，现已修复。

这是增量构建及独立导入，不是另一台机器复现。跨模型审阅由主线程统一安排。
