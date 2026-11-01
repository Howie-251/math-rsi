# 普通link坏对及其真实加权连接

日期：2026-10-08。源码：`formal/Aris4Math/ThirtyThree/OrdinaryLink.lean`。

## 结论及实际范围

命名空间 `Aris4Math.ThirtyThree.OrdinaryLink`。

`ordinaryEdges H x y` 是H中包含x且不包含y的实际边集。`ordinaryBadPairs H x y` 是其 `powersetCard 2` 中在x以外还有共同点的真实无序边对。

`ordinaryBadPairs_eq_filter` 证明其恰等于：

    (H.badLinkPairs x).filter (fun p => p ⊆ ordinaryEdges H x y)

因此它直接连接既有LinkDeletion的坏对集合，而非新建与H无关的数字参数。

无须点对覆盖、无须总边数约束，即已证明：若x≠y且codegree(x,y)=1，则

    4·(degree(x)−1) ≤ 3·|ordinaryBadPairs H x y| + (|V|−2)。

在20点、degree(x)=8时得到普通坏无序对至少4个。边数33和另一个顶点的度数都不是此局部计数的前提。

## 计数为何不需要普通link覆盖底集

普通边精确有degree(x)−1条，每条在V\{x,y}中贡献4个顶点关联。对每个底集顶点的关联数n使用 n≤C(n,2)+1（n=0也成立），求和后由通用 `LinkCounting.sum_common_card` 转成真实无序边对的共同顶点计数。

这些共同顶点位于x之外。不同五元边至多交四点，故扣去共同x后每对贡献至多3。没有共同的其他点者贡献0。于是得到上述预算。

## 加权接口

`enhanced_bad_weight_lower` 假设：

- 全部真实坏对至少q个；
- 其中普通坏对子集至少r个；
- 全部坏对的双向权重至少c≥0；
- 普通坏对的双向权重至少a≥c。

结论为：

    q·c+r·(a−c) ≤ Σ_{p∈H.badLinkPairs x} unorderedWeight w p。

它对每个坏对计基础c，仅对普通子集追加a−c，因此不会重复删除一个坏对。`enhanced_directed_bad_weight_lower` 用旧 `directed_bad_sum` 将结论直接翻译为真实有向删除集合上的权重总和；双向权重不再额外乘2。

具体caller `weight_lower_of_twenty_degree_eight` 已从H的点对覆盖、20点、degree(x)=8、与y共度1自动推出q≥5、r≥4。剩余前提仅是实际w的两类权重界：全部≥21/2210，普通≥126/12155。结论是

    1239/24310 ≤ Σ_{p∈H.badLinkPairs x} unorderedWeight w p。

下游需把真实条件排列权重代入并证明这两个前提，随后接 `critical_sum_le_link_deletion` 或对应已实现剖面接口。本模块不宣称这些权重已经在实际20点配置上求出，也不单独证明20点Property B。

## 实际构建

使用原锁定环境，在 `formal/` 运行：

```sh
lake build Aris4Math.ThirtyThree.OrdinaryLink
lake env lean ../context/propertyb33/round01/ordinary-link/ImportAudit.lean
```

`build.log` 是当前源码成功构建日志，退出0。`ImportAudit.lean` 独立导入模块，打印实际类型/公理，并以Fin20输入调用普通坏对计数和具体有向加权界；审计同样退出0，结果在 `import-audit.log`。

所有打印的核心声明传递公理均只有 `propext`、`Classical.choice`、`Quot.sound`。未新增公理、`sorry` 或 `native_decide`，未修改旧模块。首次实现时的自然数强制转换和判定实例错误保存在 `build-initial-error.log`，已通过局部化简修复。

这是增量构建及独立导入，非另一台机器的复现。跨家族审阅由主线程统一安排。
