# 20点33边的12种锁对：结构覆盖已形式化

日期：2026-10-07。

源码为 `formal/Aris4Math/ThirtyThree/TwentyStructure.lean`，定理为
`Aris4Math.ThirtyThree.exists_two_locks_of_twenty`。

输入仅为实际简单五元超图H、有限顶点类型、点对覆盖、恰33边、恰20点。结论为存在不同x,y且共度1，度数属于：

| d(x) | d(y) |
|---|---|
| 5 | 5、6、7、8 |
| 6 | 6、7、8、9 |
| 7 | 7、8、9 |
| 8 | 8 |

这12种配置覆盖所需选点，未预设低度点、锁对或剖面存在。

## 证明的实际连接

在全体顶点中选实际最小度x，记d=d(x)。点对覆盖给出d≥5；求和20d≤165给出d≤8。令W为x的共度1伙伴集合，由通用共度盈余计数得s=|W|≥38−4d。

最小性确保所有顶点度≥d。如果W中全部度>b，则实际总度至少20d+(b+1−d)s。对四种最小度分别取：

| d | b | s的下界 | 假设所有伙伴度>b时的总度下界 |
|---|---|---|---|
| 5 | 8 | 18 | 100+4×18=172 |
| 6 | 9 | 14 | 120+4×14=176 |
| 7 | 9 | 10 | 140+3×10=170 |
| 8 | 8 | 6 | 160+1×6=166 |

全部严格超过165，因此各分支均有合格伙伴。下界d≤d(y)由x的全局最小性给出。

## 实际核验

在原有锁定Lean环境的 `formal/` 目录运行：

```sh
lake build Aris4Math.ThirtyThree.TwentyStructure
lake env lean ../context/propertyb33/round01/twenty-structure/ImportAudit.lean
```

`build.log` 保存模块构建成功（退出0）。`ImportAudit.lean` 独立导入新模块，实际用于Fin20输入，并将四组自然数范围核对为明确12种数对；审计退出0，`import-audit.log` 保存结果。最初将整个12项析取交给omega引起的超时保存在 `import-audit-initial-timeout.log`；改为四个自然数区间分别化简后通过。传递公理只有 `propext`、`Classical.choice`、`Quot.sound`。

没有修改旧模块，没有新增公理、`sorry` 或 `native_decide`。本模块只证明结构覆盖；12种剖面的实际类型重数、真实坏对扣除、概率界和20点Property B由后续模块连接。跨模型审阅由主代理统一记录。
