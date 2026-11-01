# 精确范围：23点低锁目录的稀疏证书表示

本轮变更不增加数学假设、不改变完整容量域或旧残型。需要审阅的是计算表示与原真实计数是否保持一致，不是把短pilot当完整分支。

直接读 `TwentyThreeSparseTrace.lean`、`TwentyThreeFiveLowPromotionData.lean` 中 `Reason/rowValid/rowValid_covered`、`TwentyThreeFiveLowPromotionCoverage0.lean`、`TwentyThreeFiveLowPromotion.lean`；六锁同构版本用一阶矩，对应 `TwentyThreeSixLowPromotionData.lean`。

稀疏列表 xs 的每项为(迹T,重数a)，允许相同T重复，`counts xs T`按加法累积，不去掉任何原始边重数。投影将每项T映到保留锁上的迹，仍保留列表重数。`projected_counts`证明投影后counts严格等于原定义Σ_{U:project(U)=T} counts xs U。正次矩在support(xs)上求和，重复key先由counts相加，support只使同一类型的矩计算一次；`moment_eq`和`moment_zero_eq_cardMass`连接原完整幂集公式。

每个完整容量分配行附一种证书：(1)某共度0；(2)某中心共度超额>2；(3)原newCounts与显式稀疏列表逐类型相等，某删除后的矩不可能等于任一旧残型；(4)原newCounts经显式置换等于一个新代表。`rowValid_covered`把四种情况统一成存在实际使用的删除点/新代表/置换；前两种用实际Feasible矛盾，第三种用同一个H的旧分类加矩不变性矛盾，第四种直接得到真实代表。

每个Coverage独立证明 `catalogue=rows.map Prod.fst`，然后核验每行Reason。实际caller由真实promotion完整入catalogue，取行证书，再在同一H上投影、调用旧分类。不得只核验保留下来的54/13行而跳过全容量域。当前完整覆盖内核构建由主代理执行；轻量5条pilot和coverage参数化actual接口不计作完整验收。

重点寻找：投影碰撞后平方是否被错误分开；支持以外正次矩是否漏贡献；共度0/超额证书是否忘记i≠j；置换方向；catalogue输入绑定；存在witness的量词；实际H上的删除是否与证书相同。已知边界不重复制造假想问题，模型认可不替代正式kernel构建。
