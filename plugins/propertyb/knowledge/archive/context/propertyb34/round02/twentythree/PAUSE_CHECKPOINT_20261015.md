# 23点 Lean 暂停检查点（2026-10-15）

用户已暂停 T34 / m(5)≥35 的 Lean Goal。停止新增实现、探测和数值诊断；本页只保存当前边界，后续研究转入独立的 36–40 数学诊断目录。

## 已闭合的真实分支

`TwentyThreeManyLowComplete.propertyB` 已经主代理正规构建通过：原 23 点简单五元超图、点对覆盖、恰 34 边、至少七个六度点，推出原 Property B。77 个覆盖块、完整容量域绑定、5→6 实际提升及最后实际边迹双计数均已接通。该声明无外部局部分类或概率证书前提；传递公理仅标准三项。请保留全部已通过数据和证书缓存，不重复构建旧未优化数值版本。

## 恰六低支：源已写齐，尚未通过完整构建

`TwentyThreeExactlySixLowComplete.lean` 已有原始输入到结论的生产源码。条件接口探针 `six-extra-normalized-complete-r2` 通过（7.31 秒、2.29 GiB）；它将尚未验证的有限覆盖和严格概率接口作为参数，故不能算完整分支通过。

实际无损自同构规范化保持六低残型、固定第七点，将唯一可能的双共度位置移至 0。核验域从每度 331 向量减为 none 的 37 加 some 0 的 49，共 86，未遗漏实际输入。五个其他双共度位置源保持历史文件，不进入生产依赖。

主代理最新正规结果：

- `TwentyThreeHighPromotion` PASS，约 2.8 秒。
- `TwentyThreeSparsePromotion` PASS，约 3.8 秒。
- `TwentyThreeSixLowExtraCatalogueData` PASS，约 5.6 秒。
- `TwentyThreeSixLowExtra7Data` PASS，约 14.6 秒。
- **`TwentyThreeSixLowExtra7Numeric` 180 秒未结束，主代理终止；不记 PASS。** 原日志保留。暂停指令到达后尚未开展其最小数值展开诊断。

最短正式清单为 `EXACT_SIX_SERIAL_MANIFEST.txt`（暂停时 46 targets）。后续纯七度 17 型、纯八度 18 型、31 布局联合型、86 向量的分块覆盖、完整 catalogue 绑定及最终 actual 仍需正规核验。31 布局缓存源已经拆成 8 份 Rows 和 7 份实际罚项，数值含非零罚项，不能套用其他联合证书的零罚项结论。

## 恰二低支：新通用接口与源码，完整连接未做完

`TwentyThreeFewLowActualBase.lean` 轻测 `few-low-actual-base-r2` PASS（2.19 秒、标准三项）：一般低/高角色输入及 restrict/comp，实际强共度接口，以及从真实 H 到已验四锁 19 残型的 `two_low_four`。

`TwentyThreeRoleMoments.lean` 轻测 `two-low-role-moments-sparse-r1` PASS（2.69 秒、标准三项）：按低/高标签数分组的迹重数矩、根点质量平方矩、角色保持置换不变性、实际重标号绑定，以及稀疏和与完整幂集和的等价。尚未主代理正规构建。

已有有限域诊断（只在旧数学可行输入域内，不替代新的 Lean 完整容量域）：

- 4→5：1638 原提升，全部角色投影过滤后 554；一阶角色矩已经保留同样的 554。
- 5→6：13878 原提升，完整过滤后 172；一阶矩 206、一二阶矩 180，再加根点平方矩恰为 172。
- 6→7：2733 原提升，完整过滤后 1；一阶角色矩已经保留该唯一型。

诊断脚本和 JSON：`diagnose_two_low_projection.py`、`diagnose_two_low_eight.py`、`TWO_LOW_PROJECTION_DIAGNOSIS.json`、`TWO_LOW_EIGHT_DIAGNOSIS.json`、`TWO_LOW_EIGHT_SQUARE_DIAGNOSIS.json`。

`export_two_low_continuation.py` 已从旧保存布局/精确证书导出 139 个纯型、43 个联合型的新源码，没有开展新布局搜索。分组和残型见 `TWO_LOW_CONTINUATION_EXPORT.json`。这些新的 Data / Numeric / caller 均**尚未构建**。仍缺完整容量枚举、逐行拒绝/代表见证、实际投影不变量条件、5→6→7 提升，以及从已选共同单位七度点到原染色的最终装配。r=0、1、3、4、5 也没有因此闭合。

## 恢复顺序

1. 先核对 Goal 与用户授权；暂停期间不自动恢复 Lean。
2. 复用已通过 Extra7Data，对 Extra7Numeric 首个证书分解：剖面合法、配额、容量罚项、最终 A/B/C 各自小探针。检查有界量词的 Decidable 来源；主代理在另支发现 `∀ U∈chosen` 的泛型 Fintype 枚举，可用 `Finset.decidableDforallFinset` 消除，但本模块尚未证实同一根因。
3. 若单型可控，按型分块或使用 CachedRows 精确桥；保持原 certificates 签名，先实测再推广，不整批加长超时。更新最短 manifest 交由主代理唯一正规构建。
4. 完成恰六低全支后，再推进恰二低分支的容量/不变量覆盖与 actual 连接。已验 3→4 分类、80 严格项和 ≥7 全支冻结。

这里只保存真实检查点；m(5)≥35 尚未获得完整 Lean 验收。
