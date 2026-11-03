# K2模型与一次批次入口（尚未调用solver）

源固定为actual94186/657452、最大度14、已知D5。新增两个相邻helper，旧邻集A/B分别至多13点。每个cap1旧点不得同时进入A和B，15个cap2点可被两侧共用。全部3685个free点均保留，不合并selector。

旧旧距离保留，new-new距离1。任一helper到旧目标t的最短路，可把到最后一个helper的前缀压成0或1步，因此精确覆盖条件为

    R4(A) union R3(B)=V，R4(B) union R3(A)=V。

每个root/target行直接OR相应side的R4 selector与另一side的R3 selector。两侧各自的at-most13序贯计数器只计原selector，不计aux。容量1条款为¬A_j∨¬B_j；容量2无此互斥。

## 已执行准备

route gate只新增3685个R3，全部目标有25..119个R3 provider，T0为空。旧R4未重算。`common.py`还核对同序R3逐行包含在旧R4内，使用完整94186位mask，尾位不计。

唯一确定性greedy每步选最大“own R4新覆＋opposite R3新覆”，平局A优先、旧label小优先。每步合法usage及side pin数均保持，最多26选，无重启或swap。最终A/B各13点，完整两root分别缺3881、3559个旧目标；没有一侧单独R4全覆。这里只是一次对照，不据此排K2。

初始模型含global最稀combined-support256目标、legacy9754中最稀128目标及其最小label，去重后338目标、676条精确root行。模型103180变量、203308子句，7370个原selector。它是保全所有真解的松弛，不是完整94186×2覆盖模型。`INITIAL_ROWS.json`保存具体行，`GREEDY_CONTROL.json`保存完整选择及遗漏标签。

## 审核后的唯一调用

准备阶段没有solver。root审核后可显式调用

    python run_reviewed_once.py --solve

该入口拒绝已有HANDLE或SOLVER_TERMINAL，最多6轮，共享solver CPU60秒和含gate/准备的整批90CPU；每轮窗口至多15秒及剩余预算，并保留启动/限时误差余量。真实CPU由本轮RLIMIT_CPU和CaDiCaL的-t控制。proc.wait观察窗口超时只记录并继续poll同一PID，不kill、不增call；后来若真实code10仍完整验收。只有真实终态UNKNOWN才停止，不重试同模型。每个SAT模型都先核side/oldslot及全部94186两rootmask；局部行满足绝不当成全覆盖。

每轮SAT后还分别检查A、B自己的R4并。若任何一侧已完整覆盖，立即保存单helper94187参数；若两root全覆，保存K2的94188参数。两种hit均待root唯一独立验收，程序不导出图或跑新BFS。

若SAT候选仍缺目标，每侧最多取256个最低combined-support的真实违反目标，添加同一原始覆盖row。没有假设当前未加目标已满足。round文件、原始输出、完整遗漏标签及精确新增行均保存。最多轮数或预算耗尽只能UNKNOWN；partial-row UNSAT记rawUNSAT，未当成认证定理。

`run_reviewed_once.py`只读既存R3/R4，不再读source或重算球。原单helper MIP不恢复。准备与未来solver分开，当前无solver HANDLE。

## 后续明确授权的同批剩余预算模式

原两轮实际已运行：round1 SAT但全mask失败并加512精确行，round2在15CPU硬限UNKNOWN；原结果保留。父级随后明确授权在同一60/90预算余量内继续，首个窗口不再机械限制15。新入口`--resume-remaining-budget`从stage2历史继承solver19.21988/whole28.25784697、2calls及1188active rows，首call为round3、约39秒。该模式只写新RESUME文件，详细累计公式、历史保留和未启动状态见`RESUME_CODE.md`及`RESUME_PLAN.json`。此段修订不追改上面的原策略记录，也不意味着已经启动续跑。
