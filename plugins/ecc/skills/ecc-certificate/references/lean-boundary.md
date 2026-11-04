# 两套Lean工程：已核归约、显式进口与真实数据

先读 [formal原说明](../../../archive/source/formal/README.md)，再读实际声明。固定Lean4.34.1、mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`，不根据宿主已有旧Lean版本改锁。

## ECC43的实际原对象

`formal/ecc43/ECC/Basic.lean` 的Word n为Fin n→F₂，CodeExists要求实际Submodule、finrank=k及所有非零字重量≥d；MainClaim是否定CodeExists 43 10 17。实际矩阵数据经Packed/MatrixBridge得到子空间，不是用字符串或布尔摘要代替码。

阅读链：

1. `CatalogueData.lean`/`Catalogue.lean`/`CatalogueFacts.lean`：172实际矩阵、码字桥梁与每个MotherParameters。这个有限合法性已核内处理。
2. `Parity.lean`、`NoSmallDual.lean`、`MacWilliams.lean`、`Reduction.lean`：从任意原目标归约到满支撑母码，未把CatalogueReduction整体作为最终未证假设。
3. `Classification.lean`：E2＋CatalogueInequivalent把任意母码接到实际目录。E2与互异性仍显式输入。
4. `Coset.lean`：线性投影、陪集平移、覆盖及SavedPairWitnesses如何推出PairIncompatible，再反证StandardExtension。
5. `Main.lean`与`Corollaries.lean`：主结论及邻参数，实际下界矩阵经LowerBoundData/TableLowerBoundData接到前三精确值和45位区间。

最终 `mainClaim_of_external_results` 接四个参数：PublishedNonexistence41（E1）、PublishedClassBound（E2）、CatalogueInequivalent（实际目录两两坐标不等价）、∀i:Fin172, PairIncompatible(catalogueCode i)（全部母码的全称计算结论）。没有参数的CatalogueReduction已由这些数学进口中的前三项证明；这个真实进步和仍保留的外部计算不同。

更展开的 `mainClaim_of_scan_facts` 接实际F:Fin172→Finset(Word40)，每个母码的线性projection与hRetract、hCoverage以及hPairs。hCoverage对所有零投影偶代表声明“已在F，或有真实低权母码字”；hPairs是保存集合中所有pair的实际低权见证。普通扫描和pair文件为这些参数提供外部证据，工程没有在Lean内读取并验证全部历史流。

因此三种说法要准确选择：“归约已核内证明”成立；“172矩阵参数和相应下界接到实际声明”成立；“全部分类与2³²枚举已经无外部参数地内核证明”不成立。`#print axioms`仅标准三项不会显示theorem显式参数。

## ECC42与恰距离归一化

`formal/ecc42/ECC42/Main.lean`：

```lean
reduction_42_16_to_41_14 :
  CodeExists 42 16 13 → ExactCodeExists 41 14 14
nonexistence_of_proposition2 (hProp2 : Proposition2) :
  ¬ CodeExists 42 16 13
```

Main调用Parity→Shorten→Normalize。Proposition2为文献E3精确非存在；nonexistence_explicit把Fin41子空间和精确最小重量见证前提展开，再对任意Fin42子空间反证。它不是将E3声明为新增axiom后隐去来源，而是显式参数。下界[42,16,12]并未在该工程核内验距。

## 审计与当前执行

三个审计入口位于各自工程根目录：`archive/source/formal/ecc43/Audit.lean`、`archive/source/formal/ecc43/CorollariesAudit.lean`、`archive/source/formal/ecc42/Audit.lean`（路径相对插件根，均不在ECC/ECC42模块子目录中）。发布汇总为 `archive/source/verification/lean/RESULT.json`；对应类型/公理日志是同目录的 `ecc43-Audit.log`、`ecc43-CorollariesAudit.log`、`ecc42-Audit.log`，两次构建日志是 `ecc43-build.log`、`ecc42-build.log`。这些记录显示原发布从新副本build和三次import/type/axiom audit完成；没有sorryAx。发布者复用了固定mathlib缓存，没有复用本项目旧olean，不能描述为第二台机器复现。

本轮MathRSI插件未再次build Lean，只核读源码接口及复用日志。需要当前新构建时使用ecc-certificate的scratch命令；读取RESULT和每个实际audit日志，不只读build exit0。类型改变后重新核消费者、实际矩阵绑定及显式进口；只改文案不重跑全部历史扫描。
