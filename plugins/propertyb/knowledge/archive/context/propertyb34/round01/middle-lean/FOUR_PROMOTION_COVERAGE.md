# 23点三锁到四锁：实际覆盖与严格／残型分流

`TwentyThreeFewLowFourData/Numeric/Coverage/Classified.lean` 连接已有的实际三锁表、逐边迹提升恒等式和80个严格四锁项。这里只处理度数标签 `[6,7,7,7]` 与 `[6,6,7,7]` 的局部四锁；不包含后续五锁分类，不证明完整23点分支。

生成器 `generate_fewlow_four_coverage.py` 枚举旧非空迹上的提升整数，逐项限制在实际旧迹重数以内，并按新增点度数7及其与旧锁的共度上界剪枝。`BoundedAllocations.mem_enumerate`、`PromotionCatalog.actual_mem_of_old` 已证明这种剪枝保留每个实际提升向量；枚举的是局部迹重数，不是超图。空迹提升由新点的实际度数减去其余提升数恢复。`PromotionReconstruction.extend_actual` 将所得全部16个新迹重数与同一个实际H连接，包括空迹和新增单点迹。

一低表有460个满足容量的提升向量，其中246个满足全部新旧点对共度为正；规范化到73个四锁代表。二低表相应为167、66及48。规范化只使用保持六度／七度角色的置换（一低6种，二低4种）。Python已检查每个被选置换的方向以及原始计数重建；记录见 `FOUR_PROMOTION_COVERAGE_REPLAY.json`。Lean的 `coverage0` 至 `coverage5` 对每类全部容量向量逐项核验，点对覆盖在实际caller中提供正共度前提。

`TwentyThreeFewLowFourClassified.OneLow/TwoLow.residual_of_noB` 把规范代表连接到已构建通过的80个严格项actual counts caller，排除47+4及28+1个严格代表，完整保留22及19个残型。`actual_residual` 进一步组合实际3→4覆盖与这些排除：给定实际四锁嵌入、原三锁实际计数、第四点度数7及新增点对共度上界，在 `¬PropertyB H` 下，得到一个保持低／高度角色的重标号，其真实计数等于保留残型。这里原三锁计数可由已核验 `TwentyThreeFewLowBase.actual_oneLow/actual_twoLow` 提供；后续调用者仍需选出所需实际锁点、验证共度条件，并处理41个残型。

## 当前核验状态

本组Data、Numeric、Coverage及Classified均已由唯一正规构建者核验通过，生成器与已验源码保持同步。Data r26用时4.5秒；Numeric r37用时46秒；r39的实际Coverage用时1.4秒、Classified用时10秒，最终1055 jobs成功。两个`actual`、两个`residual_of_noB`及两个`actual_residual`的传递公理均仅 `propext`、`Classical.choice`、`Quot.sound`，已包含全部有限覆盖与80个严格项的实际调用依赖。

本执行者已读取日志 `../twentyone-lean/build-23-four-data-r26.log`、`build-23-four-numeric-r37.log`、`build-23-four-classified-r39.log`（后两者同目录）的成功记录及最终六项公理审计。没有启动独立或并发Lean构建。已证明范围是上述带实际三锁计数和新增度数／共度条件的3→4覆盖及严格／残型分流；41个残型的后续处理及完整23点分支仍未完成。

实际匹配使用独立 `actual_of_covered` 引理，先以抽象提升向量完成查表、置换和实际计数绑定，再由 `actual` 代入真实提升数。`covered` 在实际调用模块局部设为irreducible并保留显式类型，避免推敲真实H表达式时展开整张符号目录。此处理仅改变证明组织，不改变Data或Numeric；分流模块也保持抽象代表上的证明与真实调用分离。
