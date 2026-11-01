# v21 分支已完整闭合

`formal/Aris4Math/TwentyOne.lean` 已编译并冻结，85 行。最终定理是：

```lean
Aris4Math.TwentyOne.twenty_one_propertyB
  (H : Simple5Hypergraph (Fin 21))
  (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
  PropertyB H
```

结论使用主文件中原始 `PropertyB` 定义。假设只有固定顶点数、点对覆盖及恰 32 条边，即原目标约化后的该有限分支；不存在未证明的 profile、概率界、删除量、类型计数或可染性前提。

证明使用已形式化的总度/共度约束选择一个度数在 5 至 7 的真实顶点。度数 5、6 时，`SmallLockProfiles.realizes_profile21` 提供真实单锁类型表，`ProfileApplication.propertyB_of_uncorrected_profile` 连同现有精确数值证书直接推出 Property B。

度数 7 时，真实顶点锁在零基位置 10，即 Numeric 的一基位置 11。`LinkWeightCertificates.v21_d7_deduction_11` 将真实坏 link 边对数量及两方向权重连接到 Numeric 删除量。`degree_seven_deduction` 给出通用修正概率桥所需的实际中心下界；`ProfileApplication.propertyB_of_corrected_profile` 将它与真实临界事件、类型表及 `Numeric.v21_d7_lt_one` 接到 Property B。

验证：`lake build Aris4Math.TwentyOne` 成功，最后实际模块编译 4.0 秒；6 条关键公理审计仅 `propext`、`Classical.choice`、`Quot.sound`，无编译警告。没有 `sorry`、`admit`、新公理或 `native_decide`。日志和结构化记录在 `.aris/traces/proof-checker/2026-10-06_run07/lean-twenty-one-*`。

原目标的其他顶点数和最终全局装配由主代理汇总。本文件只宣告 v21 有限分支完成，不将一个分支升级为原 `Target` 已完成。
