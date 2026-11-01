# 20点33边分支已完整形式化

日期：2026-10-08。

## 实际导出结果

`formal/Aris4Math/ThirtyThree/Twenty.lean` 中的
`Aris4Math.ThirtyThree.twenty_propertyB` 证明：

    ∀ H : Simple5Hypergraph (Fin 20),
      H.PairCovering → H.edges.card = 33 → PropertyB H。

顶层没有剖面、锁点存在、坏对计数、概率上界或数值验证的额外前提。输入H按已经形式化的12配置选点定理处理：前11种实际调用 `TwentyStandard.propertyB_of_standard_pair`，(8,8)调用本轮完成的 `TwentyEight.propertyB_of_eight_eight`。

`Assembly.lean` 已真实消除19和20两个分支。它现在证明：

    Target33 ↔ RemainingGoal，

其中RemainingGoal仅包含21≤v≤25的恰33边点对覆盖超图。**RemainingGoal尚未证明，完整T33尚未解决。** 范围缩小由实际19、20点定理支持，不是重定义原目标。

## 新的关键连接

### CustomDeletion

`CustomDeletion.propertyB_of_custom_deletion` 复用原真实类型/排列事件接口及原有向坏对删除集合，允许一个独立证明的loss函数。它要求每个实际修正中心的loss受其真实删除权重总和支配，其他位置loss=0，并要求重新计算的逐位置min总和严格小于1。

因此它不修改旧 `Numeric.deduction`，也不会将非活跃C项的下降错误当成总界下降。所有条件在88实际caller中消除。

### TwentyEight

固定剖面为20点、锁位置10和11、实际度数(8,8)、共度1。`realizes_profile_at` 从H构造正确的四类真实重数（18、7、7、1），而非将类型表作为额外证书传入最终定理。

每个中心的普通坏对至少4、全部坏对至少5由 `OrdinaryLink` 从H推出。`IncidentWeightBound` 将全部实际双向权重下界21/2210传入真实边；普通边通过 `type_at` 证明只含当前锁点，双向权重精确等于126/12155。

由此每个中心的实际可删除权重至少：

    5·(21/2210)+4·(126/12155−21/2210)=1239/24310。

两个中心分别在各自位置删除真实坏对；原无序到有序不重叠定理保证一个位置没有重复删除。其他位置loss为0。

`certificates` 在内核中核验该实际剖面的有限有理数公式：

    Σ_k min(A_k, B_k, C_k−loss_k)=2421/2431<1。

最后调用CustomDeletion和原随机贪心存在性接口，返回H的原Bool合法染色。

## 构建及命题审计

在项目原锁定环境的 `formal/` 目录运行：

```sh
lake build Aris4Math.ThirtyThree.CustomDeletion
lake build Aris4Math.ThirtyThree.TwentyEight
lake build Aris4Math.ThirtyThree.Assembly
lake env lean ../context/propertyb33/round01/twenty-complete/ImportAudit.lean
```

对应日志为 `custom-build.log`、`eight-build.log`、`assembly-build.log`、`import-audit.log`，全部退出0。Assembly构建真实包含Twenty及Nineteen，而非构建旧默认Main。独立导入审计重述20点原命题的Bool染色结论，实际调用新twenty_propertyB；并将21–25点剩余输入接回任意顶点类型的Target33。

新CustomDeletion、88分支、完整20点分支和Target33↔RemainingGoal的传递公理均只有 `propext`、`Classical.choice`、`Quot.sound`。没有 `sorryAx`、新增公理或 `native_decide`。

本轮没有修改旧Numeric/Profile实现。相关6个旧通用模块的可选edgeCount泛化由其他代理完成，当前构建使用其真实新接口；本报告不将他人报告的旧Main回归称作本代理自行重跑。

这是现有缓存上的增量构建及独立导入，不是另一台机器复现。跨家族审阅及其意见处置由主代理另行记录。
