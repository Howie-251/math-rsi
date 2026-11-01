# 21点、33边分支：数学论证与 Lean 完整连接

2026-10-08。

## 已成立结论

`Aris4Math.ThirtyThree.twenty_one_propertyB`：任意 `Simple5Hypergraph (Fin 21)`，若覆盖全部不同点对且恰有33条边，则 `PropertyB H`。顶层只保留这三个实际输入；没有剖面、概率不等式、度数窗口、选择的锁点、类型表或三重度假设。

这是 T33 最小反例约化的一条分支。整体 T33 的其他点数仍由主线程分别处理。

## 真实输入链

- `TwentyOneStructure.lean`：总度165、共度盈余、实际边与伙伴排除，选出全部二锁/三锁结构。实现与记录由 reduction 子代理完成，见相邻 `twentyone-structure/REPORT.md`。
- `TwentyOnePairs.lean`：任意共度双锁的实际四类型分割；13个高共度型使用原始三界，6个低共度型使用实际加权扣除。`TwentyOnePairAssembly.lean` 从结构范围自动选取已证明的实际 caller。
- `TripleProfiles.lean`：实际八类 signature 数目，经真实度/共度/三点共度分割方程证明 inclusion–exclusion 恢复；删去零重数行保留真实表。
- `TwentyOneTripleData.lean`：24个带标签输入，覆盖 588、677、678 及777的全部未排序共度组合和三点共度。内核验证几何有效性、各位置精确界与最终严格和。`computed` 是同一公式表的可规约值，`p_eq_computed` 逐项以 `rfl` 绑定原实际计数公式。
- `TwentyOneDeletion.lean`：有限槽的阈值亏损引理。真实全部关联有序异边对求半亏损；两个方向合计一次无序亏损，保留全部类型容量。同类型容量为 `count*(count-1)/2 = choose(count,2)`。真实坏对数至少 q 后，实际删除重量至少 `q*c - 全部关联槽亏损`，具体有限表只核对所用阈值。
- `TwentyOneTriples.lean`：接真实三锁；两种777共边型的中锁使用 `OrdinaryLink` 得至少两个普通坏对。真实表的正重数行证明普通边的类型恰为纯单锁，因此实际损失至少 `252/12155`。这项替换中锁的原扣除，未重复相加。
- `TwentyOne.lean`：有限参数覆盖、实际三锁绑定与结构分支装配，最终返回原超图的 Bool 染色。

## 核验

环境沿用项目固定 Lean 4.24.0 与现有 Mathlib manifest；未升级依赖。

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.ThirtyThree.TwentyOne
lake env lean ../context/propertyb33/round01/twentyone-math/import-audit.lean
```

成功证据：

- `build-pairs-r2.log`：全部19个二锁实际 caller 构建成功。
- `build-deletion-r1.log`：阈值亏损定理与实际权重绑定构建成功。
- `build-triples-r5.log`：24个三锁有限表及实际 `propertyB_of_triple_data` 构建成功。
- `../twentyone-structure/twenty-one-build.log`：最终 `TwentyOne` 清洁构建成功。
- `import-audit.lean` / `import-audit.log`：独立文件导入，展开有限边集、五元性、点对覆盖以及实际 Bool 染色；最终声明、三锁 caller、阈值扣除、原32边 Main 均只有标准三公理。原 T32 仍可作为 unchanged `Aris4Math.Target` 使用。

没有 `sorry`、新增公理或 `native_decide`。有限计算处理固定局部类型与有理数，不枚举超图或染色。

## 数学与独立算术材料

完整论证 `proofs/propertyb33/TWENTY_ONE.md`。数值资料：`PARTIAL_BOUNDS.json`、`REMAINING_ROUTES.json`、`ORDINARY_SEVEN.json`。相应 Python 在 `computations/propertyb33/round01/twentyone_*.py`。

所有使用的各位置 A/B/C 都与展开33个边类型、独立标号注入公式逐项一致；两个 ordinary 权重另经 falling-factorial 计数复算。`PAIR_SCAN.json` 仅记录22个候选放置的探索，未声称全体放置最优。

Gemini B3 实际阅读此纸面证明及独立材料并未发现缺口，未执行构建。Grok B3 的阅读范围是20点与25点资料，不能算作21点审阅。新 Lean 完整链的跨模型最终审阅由主线程安排；模型意见不替代上述内核证明与命题对照。
