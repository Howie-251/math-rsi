# 23点 r=0 分支 Lean 交接

2026-10-13。范围：原始项目T33，23点、33边、点对覆盖、没有六度点。此整支已闭合到实际Property B；其他23点度数分支由主代理装配。

## 正式接口

```lean
import Aris4Math.ThirtyThree.TwentyThreeHighComplete

Aris4Math.ThirtyThree.TwentyThreeHighComplete.propertyB_of_no_sixes
  (H : Simple5Hypergraph (Fin 23))
  (cover : H.PairCovering)
  (edges33 : H.edges.card = 33)
  (noSix : H.sixVertices.card = 0) : PropertyB H
```

无剖面、位置信息、概率界、类型表或预选锁点作为额外假设。

## 连接图

实际总度预算 → 至少19个七度点 → 高共度≥4双锁，或λ3四锁，或诱导P3五锁 → 否则共度2图为团并且团大小≤7 → 至少四团的五锁或三团moment产生含大迹六锁 → 实际类型重数、真实配额和严格概率界 → 原Bool染色。

- `TwentyThreeHighPair`: λ≥4实际双锁PB。
- `TwentyThreeHighQuadData` / `HighQuad`: λ3的7个标签四锁型，实际选点与计数caller。
- `TwentyThreeHighPathData` / `HighPathCatalog` / `HighPath`: P3及P3+K2的52+63完整标签型，通用avoided-lock双配额。不是仅53个代表核验。
- `TwentyThreeHighReduction`: 在假定非PB时实际排除高共度和P3，从此前已验ClusterSelection获得FiveCase或SixCase。
- `TwentyThreeHighFiveData` / `HighFiveCatalog` / `HighFive`: 共度2图为空或一条边，32+41完整标签型。共享55高迹目录只用于先验完整覆盖，再按实际pair预算筛回73型；原JSON的extra=2未使用。
- `TwentyThreeHighSixProfiles`: 通用六锁profile与实际输入桥，参数v通用；主代理r1可复用，模块稳定。
- `TwentyThreeHighSixData` / `HighSixCatalog` / `HighSix`: 真实≥4迹先经48个匹配自同构归到三种规范支撑，余迹位10/7/2，由全部实际点对库存归入42+12+4=58输入，再明确重标号到22数值代表。21个bare，唯一原group4用avoided dual。与旧完整787域不同，但已在Lean证明压缩覆盖实际输入。
- `TwentyThreeHighComplete`: r0的完整统一入口。

## 执行与核验

在formal中设置项目ELAN_HOME与PATH，然后：

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeHighComplete
lake env lean ../context/propertyb33/round02/twentythree-selection/HighCompleteImportAudit.lean
```

两者实际exit0，日志为`high-complete-build.log`与`high-complete-import-audit.log`。独立导入中`high_branch_original_coloring`明确要求每条边染红点数1至4，完整调用原结论。7项导出传递公理仅标准三项，无sorryAx、未证新公理或native_decide。

主要有限模块的首次构建耗时：P3数值544秒、P3完整分类1186秒，五锁数值646秒/分类201秒，六锁数值247秒/分类177秒。已产出正式olean，未改变工具链或默认lake目标。数字是当次Mac并发状态下的模块墙钟，不当作跨机器预算保证。

完整证明解释与数据映射见`SIX_COMPRESSED_COVERAGE.md`、`HIGH_*_GENERATION.json`、`HIGH_SIX_CLASSIFICATION.json`及对应生成脚本。Python建议数据，最终有效性和覆盖均由Lean验证。

这份交接记录本机构建与独立导入，不称其他机器独立复现；同家族人工式解释审阅仍为provisional。跨家族最终审阅由root统一发起，未在本子任务单独调用外模。
