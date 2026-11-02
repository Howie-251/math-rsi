# 最后一次传播加强：同σ、同解域、5秒窗口

原60s/20s窗口均终态UNKNOWN，不续其原timer，不σ2。savedmask诊断反驳了tightrow独立不能铺的预测，row28→28可tile。容量Σ|packet|恰19时globalpointOR=full19强制所有选中packets两两不重叠，故将该行全部overlap-pair assignments显式加binary。它们是原CNF逻辑后果，域不变，只强化传播，不适用容量>19行。

可反驳算法预测：加入这些后果后5秒内可以得到此σ的确定SAT/UNSAT结果；若仍UNKNOWN到此收束，不再求解/布局/shift试验。same case继承91.137800205，prep.2、实际构建/parent/native均计入100CPU。无source/旧DP/BFS/field/Lean/ARIS。SAT再作actualpoint与完整图验收；任何普通/局部witness不计新图。
