# 一次全中心暖MIP的真实终态：未改进，仍 UNKNOWN

实际状态为 `NO_VERIFIED_IMPROVEMENT_UNKNOWN`，不是无解或max864证明。唯一driver session96614、driverPID643512/child643515均已exit0/terminal，不重启、不换seed、不追加求解。没有生成新图。

## 实际模型及暖解接受

本次仅使用原作者15552简单源，一次parse作为矩阵输入；未重新生成source、查field/rank或验证源D4。完整15552 binary变量/15552旧pin行、232632单位incidence非零，目标min−sumx、容量16−olddegree（旧14点cap2、旧15点cap1），无whole27、targetdisjoint、保I32或小交换限制。模型保存在 `MODEL.json`、`MODEL_INPUT.npz`；这不等于解已超过旧864。

二元域在该source/fullN规则内不排多重复制可行解：继承全部center profile，每个中心至少有一个原degree15/cap1邻点，所以任何中心复制≥2都超该点容量。这里不推广一般16/D4构造。

原accepted864中心形成完整15552维0/1start，全部15552行先手检通过；一次 `passModel` 返回kOk，一次 `setSolution(HighsSolution)` 返回 `HighsStatus.kOk`。HiGHS原日志明确：`MIP start solution is feasible, objective value is -864`，所有bound/integer/row infeasibilities均0。没有将只给864个1的部分赋值冒作完整start；实际col/row primal vectors均完整。原失败import、线程修正API成功与累计成本均保留在上级API gate。

## 实际返回与阶段解释

HiGHS1.8.0单线程、time_limit60，唯一run返回：

* `HighsStatus.kWarning` / `HighsModelStatus.kTimeLimit`，message `Time limit reached`；
* primal−864，raw dual−2384，raw gap175.9259259%；
* MIP nodes0，原日志LP iterations21593，搜索停在根处理阶段；不能把nodes0说成模型没有读入或没有计算；
* 返回vector value_valid，完整binary与全部15552容量再手检通过，selected_count864、actualmaxload1。

raw dual与gap如实保存，不是独立核验的整数最优性证书。旧864是已接受旧incumbent，此次保住它不是新数学结果；限时未提高也不是完整全中心packing的NO。`BEST_HANDCHECK.json`保存真实returned中心集合，`RAW_SOLUTION.json`保存原returned全向量/原status。没有把旧解当新candidate，15k模型的改进问题仍OPEN。

## 成本与边界

root核定先前 local+postprocess=2.956499532CPU、API=4.322222089CPU，共7.278721621；本目录准备保守charge0.5后driver prior=7.778721621。wait4实收child60.516350CPU、driver0.004042643CPU，累计 **68.299114264/90CPU秒**。其中唯一solver run进程内计60.063838733CPU；不能把它另加一次。最终汇总见 `TERMINAL.json`。

source只是一次必要矩阵输入parse，没有源D4/旧16416BFS重验。全case0新graph/BFS、field、Lean、ARIS、安装/hash；一次passModel、一次setSolution、一次run、retries0。rawstatus、失败历史与Warm864均透明保留。停止本轮，不以剩余预算再开solver。
