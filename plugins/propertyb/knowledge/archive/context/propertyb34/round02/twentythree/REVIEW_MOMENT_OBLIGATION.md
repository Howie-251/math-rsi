# 23点提升分类：本轮跨模型审阅的具体义务

项目 `/Users/rfy_naiveai/Desktop/aris4math`，只读。请审阅以下必要条件缩减是否
保持“同一个实际超图→完整局部目录→原染色”的方向；无需重新搜索概率布局，
无需审查无关软件边界。未完成的内核覆盖不能据此审阅记为通过。

对象是点对覆盖的简单五元H，23点、34边。所有选定锁点均为六度点。
`TwentyThreeFourLowClassified.actual_residual` 已从实际H推出完整8种四低残型
（允许重标号）。拟继续经五低、六低完整分类，最后由七次删除得到4b=14矛盾。

定义实际重数 μ_f(T)=#{e∈H.edges : {i : f(i)∈e}=T}。
按迹大小的p阶矩 M_{k,p}(μ)=Σ_{|T|=k}μ(T)^p。
任意锁置换σ只是双射地置换T，因此所有M_{k,p}保持不变。
p=1为原始边迹大小谱，p=2也可解释为同一k元迹的有序原边对数，含自配对。
**这里没有声称一二阶矩决定一般超图或任意局部型的同构类。**

4→5采用必要条件：每个实际四点删除的一、二阶矩等于某个上述残型的矩。
完整容量目录3573向量，901满足实际中心预算；只用一阶会剩249，
加二阶恰剩原54个输入（12轨道）。5→6只用五低两个残型的大小谱：
(12,16,4,2,0,0)、(13,13,7,1,0,0)。完整容量目录4863向量，
780满足实际中心预算；该必要条件恰剩原13个输入（3轨道）。
每个拒绝输入只指定一个删除，内核核验该删除必要条件蕴含归入新目录；
实际调用从同一H的旧分类构造这个必要条件，因而没有跨视图拼接独立假数据。

审阅重点：

1. `cardMoment_map/relabel/of_relabelled_counts` 的重标号方向和求和对象；
   多条原始边可具有同一迹，重数不得去重。
2. 弱化旧分类为矩条件后，实际输入仍满足；一般矩不完备无碍，因为正式
   `coverage` 必须对全部原容量向量证明此弱条件下仍覆盖完整新代表。
3. `actual_extension` 的成员关系、空迹/新单迹恢复、所选删除与旧分类均来自同一H；
   `actual` 先归一化旧锁，再提升同一个置换固定新点。
4. 最终七低结论在内部消去目录条件；不能将条件caller/probe当完整分支已完成。

实际源码：
- `formal/Aris4Math/ThirtyFour/TwentyThreeTraceShape.lean`
- `TwentyThreeLowPromotionBase.lean`（同目录）
- `TwentyThreeFiveLowPromotionData.lean`、`TwentyThreeFiveLowPromotion.lean`
- `TwentyThreeSixLowPromotionData.lean`、`TwentyThreeSixLowPromotion.lean`
- `TwentyThreeSevenLowCounting.lean`、`TwentyThreeManyLowComplete.lean`

数学/复算/状态：本目录 `CARD_SPECTRUM_REDUCTION.md`、`LOW_PROMOTION_EXPORT.json`、
`analyze_four_projection_invariants.py/.json`、`PROGRESS.md`。
一般不变性及Data/实际caller接口轻测已通过；正式完整coverage及数值串行构建
状态以最新主代理日志为准。请明确实际读了哪些文件、是否执行了命令，
具体指出反例或缺失义务；没有发现问题只表述为当前审阅范围内未发现。
