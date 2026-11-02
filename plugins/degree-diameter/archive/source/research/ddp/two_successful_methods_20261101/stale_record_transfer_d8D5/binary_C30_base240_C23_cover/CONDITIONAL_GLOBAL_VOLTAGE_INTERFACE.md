# 保22eq的全局电压采样：正确性与终态口径

**纯paper，未新算。** 已有28920个unordered packets、2699760条NB flows均distinct；min66，diagonal81..97。21条非零边的局部解仅critical packet满23，故下一规则应随机化全局自由边，而非继续局部坏pair修补。

固定关键packet的22个独立差方程 `Aθ=b`（rank22）。取其确切RREF/pivot：独立均匀选择**全部**nonpivot edge电压，再按方程唯一回填pivot。自由变量与解一一对应，故这是该affine解空间的均匀采样。960边表示有938自由变量；树gauge后是721−22=699。前者含239个不影响cover性质的vertex-gauge方向，但诱导的cover分布等价，无需为了这批额外改写gauge实现。148条critical support以外的free edges也必须赋值，不能默认0。

每个样本都应逐字面满足22eq；据已有构造，critical packet必满23。这是编码/回填检查，不是另一次发现。保存选定的22条差方程/路径indices、pivot约定以及固定32组完整电压，批前冻结生成规则，逐组验**全部28920** packet的精确phase union；不按score选下一电压、重启seed或hillclimb。32无命中只能记这些样本失败与全局搜索UNKNOWN。特定22条路径被指定取值也**不是**任意可行cover的WLOG，不能将此affine slice当全C23域。

条件化后还须正确解释“distinct”：`θ=θ0+Nz` 时path相位是 `fθ0+(fN)z`。若差d位于rowspan(A)，则dθ在整个slice固定；固定为0的路径仍永远碰撞。因此旧unrestricted flowdistinct不保证此slice仍全可分。无需现在另算：有失败时只能称所选电压的phase collision；若未来另证conditional collapse，也只约束该slice，不能回写成原NB path容量不足。

建议每sample保留一组简短类别统计：

- 全28920的full23数量、最小phase覆盖与首缺phase/pair；
- 240个diagonal的覆盖分布（必须含空walk的phase0）；
- 现成NB数量为最小66的packet类，以及其它off-diagonal按已有path-count分桶的覆盖分布；
- critical packet恒23与22eq残量检查。

diag的闭路及其反向相位成±对，off-diagonal反向packet取负，均可复用旧unordered cache；不得假设不同packet统计独立来外推成功率。这样能区分局部稀疏电压留下大量零holonomy、低pathcount下的phase碰撞和更广的cross覆盖失败，而不把“原始路径不足”作为解释：原容量门已经全过。

若某一固定全局赋值全packet满23，则确实给出同一电压下全部base pairs/23phases的D≤5证据，可导出5520 literal交root验收；单packet成功不够。若32组无hit，按本批停止，不关任意ordinary C23 cover，也不换base/fold/field。本文没有新增参数、图、BFS、field、solver、Lean、外审或其它数值计划。
