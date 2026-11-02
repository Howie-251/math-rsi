# actual650八FP端点转移：唯一feasibility窗口UNKNOWN

实际结果为 **UNKNOWN，无incumbent**。唯一HiGHS求解达到20秒限制，status1，message为 `Time limit reached ... primal_status is None`。它没有返回不可行结论，更没有可审阅的完整651图；不能把本次结果升级为FP-transfer整族NO。

## 本次问了什么

实际650/3250全10源、P130/F520、P的F-neighborhood twins、C79+C21+C30、旧A2/A3以及<=5纯hub排除均继承。新规则是八条FPcuts端点在F/P各互异，新z连八F及其中二P，余六P配三对PP修补。此规则超出旧保留全部删边端点且无旧旧补边的严格范围。

借助已保存的twin替路纸面条件，新根到F的三步覆盖精确化为原源B2(S)覆盖520个F；PP repairs不能补z到F的<=3路。没有把FP middlecritical=0当作删边安全。

## 实际模型

[模型数据](FP_MODEL.json)、[完整稀疏矩阵](FP_MODEL_MATRIX.npz) 和 [唯一源码](FP_once.py) 已保存。实际 **1170 binary / 1302行 / 90480非零项**：

* 1040个FP删边变量，F/P每端点选择数<=1。
* 130个star-P变量，star-P必须来自选中donor P。
* cuts总数8、star-P总数2。
* 520个F目标的source-R2覆盖下界>=1。

目标恒0，SciPy milp/HiGHS，threads1、time_limit20、presolve。R2只由既有普通A2 positivity加identity与literal adjacency获得；未重新计算walk矩阵或source BFS。SciPy提示threads未在其白名单中、会原样传给HiGHS；这不是求解启动失败，实际求解返回time limit状态。没有第二solver或第二窗口。

[实际solver返回](FP_SOLVER_RETURN.json) 的x/目标值/节点数/dualbound/gap均未给出，未检查infeasibility certificate。只能记录该次搜索无incumbent，不能推断覆盖行本身无解、共享整数条件不相容，或预测已被反驳。当前具体卡点是未取得可冻结的整数端口组。

## 未执行的阶段必须分清

没有incumbent，所以0次literal-selected-root F覆盖手检、0个frozenprototype、0/15 PP配对、0个新根/旧根BFS、0张651图。不能把15种配对写成已失败，也不能把没有候选归因于旧P路线损伤。

后续配对与候选代码已准备但未执行：已有PP边会保留为合法underdegree9分支，避免错误要求恰10度；仅三条PP均为新非边时m3255。若未来另获授权取得incumbent，需要冻结唯一8cut/2P后再按这15种配对实测，而非本次默认续算。

## 成本与停止

[事前预测](FP_PRED.md)、[actual结果](FP_RESULT.json)、[终态](FP_TERMINAL.json)、[源读取接口](SOURCE650_FP_TRANSFER_READ_GATE.md)。实际运行session64322/PID519415已exit0，HANDLE无active。

solver CPU **20.013963667秒**，全部本进程/库线程CPU **20.333854394秒**，无子进程。继承read1.50087698，加准备预留0.25，case累计 **22.084731374 / 45秒**。候选阶段未启动，剩余预算不自动续作第二模型/seed/原型。

source literal仅作新模型输入parse一次；0源D3验收、0旧allroot BFS、0新field/矩阵/rank、0图BFS、0Lean/外审/安装/哈希、新增图0。按授权STOP，整个新FP-transfer机制保持UNKNOWN。
