唯一新source17平面normal=(1,0,4)的真实packing811对照已终态。

- 结果：INFEASIBLE_ONE_SOURCE17_BEST_PLANE_POOL_SOLVER_SCALE；一次SciPy status2 / HiGHS8，非超时。
- 实际池：1539点；324固定，1215点变量，3个合法cut binary；37908actualpin行。
- 旧810对照：43740pins不交，只违反新增≥487变量点行，差1。
- 成本：3.933452689 CPU秒／60，solver3.480811205／45；单worker，1次调用。
- 范围：仅此normal及固定其余18层的池，数值MIP证据；不是所有plane/非线性集合不可能。没有incumbent、dual、node count或独立UNSAT证书。
- 0图/BFS/旧边表/field/rank/Lean重验；不自动尝试第二plane。
