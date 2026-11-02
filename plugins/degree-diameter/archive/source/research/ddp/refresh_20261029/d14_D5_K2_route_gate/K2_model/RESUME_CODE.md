# 同一K2批次的剩余预算续跑：供root审核，未执行

本轮父级明确授权修订原“首个15CPU UNKNOWN立即停”的策略：round1已有真实SAT及完整94186两root反例，已加512条原始精确行；round2只在15CPU硬限终态UNKNOWN，而原总预算仍余40.78012 solver CPU、61.74215303 whole CPU。依据是实际共同覆盖反馈和未用预算，不是遗漏数下降；没有重置Goal、source、候选域、60/90总预算或6call上限。

## 保留历史

`stage2_history/`保存原SOLVER_RESULT、SOLVER_TERMINAL、HANDLE、CHECKPOINT、round_02.cnf以及旧driver版本。根目录的原SOLVER_RESULT/TERMINAL/HANDLE也保持原样。PRED以追加policy revision记录本次授权，不覆盖原15秒策略的历史文本。

新显式入口为

    python run_reviewed_once.py --resume-remaining-budget

本次代码准备没有执行该入口，没有创建RESUME_HANDLE，没有新solver调用。

## 两种状态来源不得混淆

* 预算取自原最终SOLVER_RESULT：solver19.21988，whole28.25784697，calls2。whole已经包含gate/prep7.814843227及旧driver，不再相加。
* 模型行状态取自旧CHECKPOINT：1188条active rows。这个checkpoint是在round1后写的，其4.216792 solver CPU并未包含round2，绝不拿来当预算基线。
* 首个续跑是round3，直接使用已归档的round_02.cnf，header为103180变量/203820子句。没有丢掉512条新增行，也不重建原稀行模型。

## 累计公式

新进程的child CPU只包含它新启动的solver，记为S_new；新Python进程完整自身CPU记为D_new（从process birth计，含imports、解析和新行生成）。

    cumulative_solver = 19.21988 + S_new
    cumulative_whole  = 28.25784697 + D_new + S_new

没有再次加gate/prep，没有遗漏旧round2 CPU。总calls从2起，循环round3至6，最多再4call。

显式resume模式取消原每call15秒帽，窗口为

    floor(min(60-cumulative_solver-1, 90-cumulative_whole-2))。

首个窗口为39秒；输入加载只消耗whole预算，不改变当前solver余量，正常准备后仍为39。每次写完CNF后重新计算窗口，不能把生成CPU当作仍可用的solver时间。RLIMIT_CPU=(window,window)，CaDiCaL -t同window。

## 停止与证据

观察timeout只在RESUME_LIVE_ROUND中记录，继续poll原PID，不kill、不新开call；后来若code10仍完整验收。真实UNKNOWN或rawUNSAT终态立即停；只有真实SAT且全94186反例才添加新精确行并允许下一call。原side≤13、oldslot检查、单side R4意外命中检查及全两root验收保持不变。

新终态只写RESUME_SOLVER_RESULT、RESUME_SOLVER_TERMINAL、RESUME_HANDLE；新反例状态只写RESUME_CHECKPOINT。其rounds保留原两轮并追加新轮，报告prior/new/cumulative CPU与calls。原阶段UNKNOWN历史不被静默覆盖，也没有把未决问题说成已排除。
