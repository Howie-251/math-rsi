# 固定v12312／seed11：一次directSAT仍UNKNOWN

本批没有SAT见证或UNSAT结果，也没有新图。已有CaDiCaL以合法分离argv `-t 19` 对同一个固定残余模型运行一次，返回 **exit0**，stdout明确打印 **`c UNKNOWN`**，没有形式`s`状态行。不能把它写成UNSAT或≤5extras不可能。

## 为什么换算法、没有换问题

两次HiGHS窗口均node0/timecap；本次 [PRED](PRED.md) 改成直接SAT feasibility，而不增加MIP timer、template、seed或参数。固定旧source设计v=12312、11个available seed、1744个initialholes，问题仍是从同3771个残余coverage列中选至多5个，覆盖全部holes。该解若存在且实际检查通过，才是总≤16 pins的16417候选入口。

现有binary实际位于项目`.tools/lean-4.24.0-linux/bin/cadical`，在运行前仅核文件／可执行权限并继承旧成功CLI；无install、help probe或额外solver调用。[NATIVE_EXECUTION.json](NATIVE_EXECUTION.json) 保存真实完整argv、PID及预算。

## 实际静态CNF对象

从既有current-R3 bitsets及残余mapping重建每个hole的完整positiveOR，未计算新球。1744个target包含currentclone targets，seed已覆盖行没有重加，未丢空行（实际emptyOR0）。重复列仍保留全部actualpin等价映射，真实变量区恰x1…x3771。

prefix counter `s(i,j)=3771+(i−1)·5+j`，i=1…3771、j=1…5；实际包含x→s1、prev阈值传播、x与前阈值提升、禁止x与prev5，以及firstprefix j>1=false。它是existential精确atmost5，不是把greedy10解当unit clauses。纸面接口见 [SAT_FEASIBILITY_INTERFACE_PAPER.md](SAT_FEASIBILITY_INTERFACE_PAPER.md)。

实际 **22626变量＝3771真实变量＋18855辅助变量**；**43219子句＝1744 holeOR＋41475 cardinality子句**。CNF及actualpin映射为：

- [FIXED_V12312_COVER_ATMOST5.cnf](FIXED_V12312_COVER_ATMOST5.cnf)
- [CNF_MODEL.json](CNF_MODEL.json)
- [REAL_VARIABLE_TO_ACTUAL_PIN.json](REAL_VARIABLE_TO_ACTUAL_PIN.json)

## 原始求解返回及结论边界

stdout明确记录19秒real-time limit并以UNKNOWN结束。实际搜索处理 **56159 conflicts、204313 decisions、44480436 propagations**，因此此算法已进入decision，与HiGHS原node0反馈不同；它仍没有完成判定。`SAT_STDERR.log`为空，未发生CLI格式错误或安装问题。

[SAT_STDOUT.log](SAT_STDOUT.log)、[RESULT.json](RESULT.json)、[TERMINAL.json](TERMINAL.json) 保留全部原始返回与统计。没有proof logging／proof checking，也没有把rawsolver结果提升为数学全族NO。因为没有SAT模型，真实pins／完整current16416 union的阳性分支、source读取、newroot路线及16417边表阶段均未进入，图／参数／Lean增量0。

即便未来得到SAT，仍须只解码前3771真实变量，检查extras≤5、currentpin资格、seed+extras≤16、实际全16416 R3并覆盖，再产图交fresh acceptance；单独SAT标签不能计新图。本批没有这样的标签或产物。

## 累计成本与停止

唯一driver1404451／nativechild1405698、session96788已终态。native actual CPU **19.009266秒**，parent **1.768622510秒**，新准备0.50；沿prior71.065033579，Ccase累计 **92.342922089 / 120 CPU秒**，含前面已保存的K5语法失败费用，没有reset。native hard20、parenthard24；实际solver调用1。

新ball、sourceD4／oldallrootBFS、field、Lean、ARIS、图均0。完整当前source未改，旧16416及专家包未改。完成STOP：不第二SAT、solver、seed、refreeze或新template；Goal是否继续及后续问题由root另定，本C路线不再计算。
