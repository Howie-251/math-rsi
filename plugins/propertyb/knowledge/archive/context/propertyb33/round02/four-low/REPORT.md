# 23点四个六度锁：实际分类与47个直接染色分支

2026-10-13。本目录记录四低分支的增量；整体T33仍未完成。

`TwentyThreeFourLowActual.actual_representative`从实际H23、点对覆盖、33条边及四个不同六度锁点构造重标号后的50个局部代表之一。内部共度盈余为每点至多2，六个共度变量的完整域给56个有标签预算；允许四种三元迹重数各为0、1、2，四元迹为0、1。完整预算过滤得到464个有标签输入，并核验它们到50代表的置换。未假设实际三元迹互异，也未枚举整张超图。

`TwentyThreeFourLowBare.propertyB_of_counts`给其中47个非单位共度代表的严格未修正概率界。`TwentyThreeFourLowActual.propertyB_or_unit_counts`已将真实选点、完整分类、真实类型重数和这些界连起来：任意至少有四个六度点的实际H，或者已经得到Property B，或者进入前三个单位共度代表之一。后者的实际坏边对及自适应位置调用由后续FourLowUnit模块负责，本报告不将其记成已完成。

## 实际验证

- `structure-build.log`与`structure-import-audit.log`：实际迹重数上界。
- `catalog-build.log`：完整预算域到代表的内核验证，968 jobs成功。
- `bare-build.log`：47代表的严格概率界及实际counts调用，995 jobs成功。
- `actual-build.log`：真实输入到代表及上述二择一导出，1000 jobs成功。
- `ActualImportAudit.lean`、`actual-import-audit.log`：单独导入、实际导出类型和传递公理。两项导出均仅依赖propext、Classical.choice、Quot.sound。

复现时按`formal/README.md`设置项目ELAN_HOME/PATH，在formal中运行：

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeFourLowActual
lake env lean ../context/propertyb33/round02/four-low/ActualImportAudit.lean
```

生成器仅提出显式局部数据；类型覆盖、重标号、真实counts绑定及概率不等式都在Lean中核验。独立导入是本机执行，不是第三方独立重建。
