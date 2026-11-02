# 已找到support的单次最大容量LP（2026-11-01）

继承唯一MIP终态：HiGHS OPTIMAL、incumbent改变6、数值bound5.999999999999806、gap0，实际整数811；这是求解器证据，不是形式化排除≤5的证明。既有55个r≤2精确LP不重跑。

本批将MIP已经出现的17个正层作为固定support：retained=[31,59,60,72]各81；其余13=[16,17,30,32,35,42,43,44,45,58,61,73,74]允许0..81。只进行1次LP最大化总中心数，原target约束不变。事前预测：在同一support中最大容量严格超过811，故原MIP的+1仅是阈值，不是可用容量上限。若LP最优≤811，推翻这一预测并停止，不作权重hillclimb或第二次优化。

注意：固定retained4时完整admissible集合另包括64、71，但本次按已找到support约束不加入这两层。返回全部15层admissible列表和pair shared-target/port/actual chart，13层LP最优不能冒作15层最优。root后续可据接口设计实际W-plane点集，但本批不生成点集/大图。

单worker、现有scipy.linprog/HiGHS，总≤5CPU含import/prep，精确有理primal/dual证书。输出每层rational权重、逐层下取整的一个精确可行整数容量（只是必要条件）、原目标floor上界。0新MIP、0大图读取/BFS/Lean/整层packing重跑，不改retained，不自动再求更稀疏配置。
