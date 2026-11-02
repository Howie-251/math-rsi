# 事前预测与条件执行：固定15552源的全中心 binary packing

原始准备状态为 PREPARED_NOT_RUN。现root已实际接受local及postprocess完整NO，并明确授权本目录唯一一次MIP：342个恰4-blocker新中心的四元组均不同、maxgroup1，4out5in也被必要条件排；未生成候选。本授权只启动下面一次global，不能续局部交换梯。

固定实际源为原15552/116316简单图，不以16416图为链式source。每个旧中心至多一个clone，变量x_v∈{0,1}，全15552变量/15552旧pin行；A_G为冻结旧N incidence，约束 `A_G*x≤16−degree_G`，目标min `−sum x`。旧degree14点cap2、degree15点cap1均保留。解除整W27、controller-target-disjoint与固定I32不变约束；不是I33whole-block追加。

**可推翻正向预测：** 单次暖启限时运行可能返回>864的完整binary可行解。API确认不保证搜索速度或改进。known864只是已接受旧解，不是新图，不复现旧16416图。

代码在实际运行时只读原作者adjlist一次构造CSC incidence，并从accepted `degree16_plane864/PARAMETERS.json:source_center_labels`形成15552维完整0/1start。手检binary、全部15552行和old864后，构造bundled `_Highs`/`HighsLp`，唯一passModel，唯一 `setSolution(HighsSolution)`，检查返回kOk；失败即UNKNOWN停止，不重启。实际启动前固定OPENBLAS/OMP/MKL/NUMEXPR线程为1，HiGHS threads=1；一次run，time_limit≤60，childhard≤80且扣除累计prior，预留结果/候选写出CPU。不设未知first-improvement选项，不callback、不换seed、不追加模型。

累计D4case cap90CPU，必须含localgate整体（2.783706889，其中read2已包含）、postprocess实际CPU、API gate整体4.322222089（含原importkill），本代码准备保守charge0.5，以及实际global parent/child所有CPU。调用driver必须显式给 `--prior-total-cpu`，其值包括上述全部已用成本与prep，不是新timer。若root给实际prior不同，以root核定实际账为准。驱动使用wait4记child CPU；非正常退出与所有失败均保留，不重置。

root当前核定 local+postprocess 合2.956499532、API合4.322222089，授权prior为7.278721621；加本目录准备charge0.5后，driver输入 **7.778721621**。原read2已在local账里，不能再加一次。全局模型不限制保留I32，也不限制小交换；若改进需重选多个旧中心，仍在本域内。

二元域在本固定source/fullN构造里不丢多重复制解：已完成的全15552 center profile显示每个N_G(v)中至少4个当前zero-residual旧点w。当前L0(w)≤1且d_G(w)≤15，R0(w)=16−d_G(w)−L0(w)=0迫d_G(w)=15、原cap(w)=1。故每个中心至少有一个原cap1邻点；若同中心复制≥2次，该点负载≥2，无论其余中心如何重选都超cap1。这是继承完整profile的纸面结论，不重算profile，也不推广一般16D4。

输出MODEL.json/MODEL_INPUT.npz、原HiGHS日志、手检warmstart与setSolution实际返回、node/primal/dual/rawstatus/bestx、HANDLE/CHECKPOINT/RESULT/TERMINAL。只有returnedvector通过binary及全部cap手检且sum>864，才一次生产这个best中心集合的完整新graph、参数、旧N角色、degree/load和true-Walk/prefix证明；原15552旧边全保、0newnew。producercandidate须root安排fresh验收，不提前计图/Lean/record。

若未改进，保留真实time/optimal/error与best；即便rawOPTIMAL，也仅记未经独立最优性证书核验的solverstatus，不将其写成已证明max864。若运行无可读best，不用旧864假装solver新返回。源D4/非D3与generic fullN Walk/oldretraction只import既有事实，0旧sourceD4/field/rank/BFS/Lean/ARIS/安装/hash。

入口：`run_global_once.py --root-authorized --prior-total-cpu <all_prior_including_prep>`。当前仅stdlib语法解析，未执行此命令。
