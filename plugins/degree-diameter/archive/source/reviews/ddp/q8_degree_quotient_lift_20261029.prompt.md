请审阅本项目新提出的两个相互关联的数学结论，不运行任何数值/solver，不修改文件。使用已有本机资料，避免泛泛列方法。
1. research/ddp/refresh_20261029/q8_degree_budget_route_gate/PROOF.md：H含8个指定Q3，额外最大度2且D≤3，是否必额外恰2？关键outside≤18s+36，s=1时54<56，允许pencil内额外边。
2. research/ddp/refresh_20261029/q8_cyclic_quotient_route_capacity/PREDICTION.md, check.cpp, RESULT.json, prepare_orbits.py, CANONICAL_RESULT.json, VOLTAGE_LIFT_PREDICTION.md, lift.cpp。全部213798个2regular标签商是否完整覆盖244个Z8不变额外edge orbit，形式路径门排210609留3189，cubeAut48下110商；逐位电压穷举的mod2至少4、mod4至少2、mod8至少1是否保全全部合法D3解；ordinary loop±电压选1,2,3，halfturn固定4，cube邻标签extra电压非0，parallel两相位不同。用deck单位乘法可否将第一个奇普通电压规范1（不强排parallel），包括ordinary loop按±重新规范的情况。
重点攻击遗漏的walk、商类型、量词、对称规范/符号与合法性。若有错给最小具体反例或代码行；若正确给各结论准确scope。
目前共同电压检验结果以VOLTAGE_RESULT.json存在时为准；没有主1088图，不把形式通过当图。数学当前104例/4参数、confirmed103/3、具体公式Lean1，全球20D3新颖性待确认；这些数字不是本次要重验的内容。最后给支持/有条件支持/反驳结论及一项可实际改变下一步的意见。
