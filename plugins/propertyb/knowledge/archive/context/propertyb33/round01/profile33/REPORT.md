# 33边锁点接口与真实调用：22点两支、20点十一支

日期：2026-10-08。使用 ARIS `lean-formalize`，沿用原 Lean 4.24.0/锁定 Mathlib，未改工具链。

## 实际交付

以下声明已构建通过，且不是要求用户提供任意概率证书的空接口：

1. `ThirtyThree.TwentyTwo.six_six_propertyB`：任意22点、恰33边、点对覆盖的五元简单超图，给定实际共度1的六度/六度锁对，得到原 `PropertyB H`。
2. `ThirtyThree.TwentyTwo.six_seven_propertyB`：同样条件下给定六度/七度锁对，得到 `PropertyB H`。
3. `ThirtyThree.TwentyStandard.propertyB_of_standard_pair`：任意20点、恰33边、点对覆盖的五元简单超图，给定实际共度1锁对，且实际度数在显式十一配置列表中，得到 `PropertyB H`。列表为：
   `(5,5),(5,6),(5,7),(5,8),(6,6),(6,7),(6,8),(6,9),(7,7),(7,8),(7,9)`。

上述每个真实调用都从 H 构造完整实际类型表，转移实际排列概率，证明两锁点处的实际坏对扣除，再由逐位置严格界得到原对象的 Bool 染色。

**范围仍有限定**：此处未证明每个20点对象都有上述十一锁对之一；完整结构选择还包括(8,8)，需要额外普通link计数。22点(7,7)也不在本交付内。因此不宣称20点、22点或T33全域已完成。

## 最小兼容参数化

经主代理协调后修改六个旧模块，完整差异保存在 `compatibility.patch`，修改前版本保存在 `before/`：

- `Numeric.validProfile` 添加可选尾参数 `edgeCount := 32`，总重数改为此参数；空型总重数与自然有序边对上限同步为 `edgeCount` 及 `edgeCount * (edgeCount-1)`。
- `TypeCounting.RealizesProfile` 添加同名可选尾参数并传给 `validProfile`。
- `ProfileProbability`、`ProfileApplication`、`ProfileDeletion` 的实际调用签名允许隐式任意 `edgeCount`。
- `LinkWeightCertificates.realized_center_deduction` 同样参数化。

概率、双计数、删除、并集和染色证明的正文未改。原32边调用自动使用默认32，原构造器字段次序不变。整个旧 `Aris4Math.Main` 已重新构建成功，原主定理类型和标准三公理保持。

没有复制约600行概率引擎，也没有新增通用平台。给定真实 `RealizesProfile ... p 33` 后，现有应用定理自动推断33。受控cap的数学应用仍需原实际计数证据；本轮所有锁点应用使用 `emptyPairCap = none`。

## 新模块及接口

- `ThirtyThree/DoubleLockProfiles.lean`：复用旧11/12位置几何与类别定义，把实际四类计数扩展到总边数33。空类型是真实的 `34-d(x)-d(y)`，其他为 `d(x)-1,d(y)-1,1`。
- `ThirtyThree/DoubleLockAt.lean`：允许任意合法一基位置 `1≤a<b≤v`，真实度数不限6/7。`realizes_profile_at` 根据 H、边数33、共度1和有限数据有效性证明构造完整实际表，适用于20点10/11、11/12及22点11/12。
- `ThirtyThree/TwentyTwo.lean`：新33边数据和真实66/67调用。
- `ThirtyThree/TwentyStandard.lean`：20点前十一种完整局部分支。`standard_certificates` 对这十一项证明位置合法、数据有效、严格有理界、每无序坏对双向权重下界及数值扣除。`propertyB_of_standard_pair` 将它们绑定至实际 H。

有限数据有效性是具体调用者已用内核计算消除的输入，不是留给最终染色结论的额外假设。通用 `realizes_profile_at` 自身仍是接口，实际22/20调用才证明这些接口确实可以实例化。

## 数学变化

22点两支均修正两个锁点：

- (6,6)：两中心各至少一个坏link对，双向权重至少3/323；最终 `4155/4199 < 1`。
- (6,7)：左中心至少一个，右中心至少三个；最终 `441/442 < 1`。

原32边(6,6)可以不修正，新33边未修正界249/247大于1，所以没有机械沿用旧调用。

20点前十一配置在度数9时使用位置11/12，其余使用10/11。每个中心的坏对下界是 `(4*d - 19 + 2)/3`。位置10/11的每无序对最低双向权重为21/2210；位置11/12时左右最低权重分别为70/7293和5/663。内核证明这些权重适用于全部允许实际类型，且足以覆盖对应数值扣除。

所有扣除均进入C后逐位置重新取min(A,B,C')。没有将非活跃C的下降直接计作总界下降，没有枚举整图或染色。

## 构建与审计证据

在 `formal/` 中设置本项目 `ELAN_HOME` / `PATH` 后执行：

```sh
lake build Aris4Math.ThirtyThree.DoubleLockAt Aris4Math.ThirtyThree.TwentyTwo Aris4Math.Main
lake build Aris4Math.ThirtyThree.TwentyStandard
lake env lean ../context/propertyb33/round01/profile33/import-audit.lean
```

成功记录：

- `build-interface-r1.log`：六模块参数化及首个实际33边类型构造。
- `build-final-r2.log`：任意位置接口、22点两个caller和旧Main回归。
- `build-twenty-standard-r3.log`：20点十一配置与实际caller。
- `import-audit.log`：独立导入、真实导出类型、公理及展开Bool染色调用。

所有已交付导出、通用实际表构造及旧主定理的传递公理只有 `propext`、`Classical.choice`、`Quot.sound`。中间失败日志保留用于重现开发过程，最终成功日志覆盖当前源码；源码中无sorry、新增公理或native_decide。

这是本机增量重建和独立导入；不是另一机器重现，也不代表Grok/Gemini已经审阅这些最终源码。跨模型具体复核由主代理整合。

## 下一个实际连接

主代理/结构代理将20点实际结构选择分为本模块十一配置和(8,8)。前十一项直接调用 `propertyB_of_standard_pair`；(8,8)另用普通link加强。22点还需覆盖或解决(7,7)。本代理不改新Target/Reduction，也未宣称完整T33。
