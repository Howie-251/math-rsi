# 事前预测：actual650的八FP端点转移

唯一源是 d3d4_transfer/source650.implicit_adj.txt，650/3250全10，P130/F520、65对P的F-neighborhood twins，PP为C79+C21+C30。源D3、A2/A3普通walk计数、<=5纯hub NO继承，不重新验收或误用同名650源。

**预测：** 存在八条FP cuts（8F/8P端点各互异）与两个选中donor P，新点邻八F及二P，能在三步覆盖全部520F。新规则的PP repairs不能参与z到F的<=3路；已继承的P-twin替路证明把删边后F-only覆盖精确转化为原源B2(S)。因此这是可由旧A2+identity+adj形成的明确必要/精确新根F门，不预言新根P或全部旧旧D3成功。

一次HiGHS/scipy feasibility：1040条FP binary与130个star-P binary；F/P cutend各<=1，starP<=该P的donor选择，sum cuts8、sum starP2，520个F-target R2覆盖>=1，objective0。threads1、time_limit<=20，只有一个solve，不切seed/Q/原型。rawINFEASIBLE只记录数值MILP证据，不作certified全族NO。若有incumbent手工绑定binary/端点/源literal选定10spoke的真实F覆盖后冻结唯一原型。

余六donor P完整枚15pairings。每pair已是旧PP边时保留其合法underdegree9，不丢弃或补重边；只有三对都为新非边才m3255，全程目标maxdegree<=10。实际最终651图先新z BFS3，再八donor P优先，后其余旧根到首失败；首完整651根PASS即保存图与全部rootstats并停止交root独验。每pair存实际PP新增、degreehist、stage、首失败shortestpath。首oldold失败仅诊断同一pair的源旧<=3路线（使用旧A2/A3+literal，不sourceBFS）。15无hit只关闭该frozenprototype，不关闭全部FP-transfer族。

累计cap45CPU，继承read1.50087698，新准备保守0.25，所有imports/父子/失败/输出纳账。单worker、进程硬40、候选阶段软38，0安装/field/旧BFS/solver重试/Lean/外审。完成即停。
