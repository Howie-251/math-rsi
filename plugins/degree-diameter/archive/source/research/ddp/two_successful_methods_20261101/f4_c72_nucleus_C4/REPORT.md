# 72控制器＋nucleus C4：局部修复成立，远端路线置换冲突

新的规则把每个F4³ fiber加2个C4邻点，目标为22度4608点；它改变了旧自层覆盖机制，未套用旧controller≤68上界。

实际120个半线性conic置换全不同，指定port→reverseport恰24域；全部逆合成与正反C4shift union通过。随后两张指定72控制器都在唯一三步远端路线处发生严格冲突：Exoo有72条边的24域为空，Michel有108条。

小证明已够停止：Exoo edge0→51要求3个不同incoming方向仅映入2个剩余方向；Michel edge0→9要求至少2个方向仅映入同1方向，均违背置换的Hall条件。由于这些点对只有三步cross预算，内部C4步骤无法修复。

预处理0.628CPU；无survivor，因此0SAT、0纤维图、0新结果。正向机理分析由互补代理另存，不能把这两张控制器的失败扩张为整个新机制无望。

[实际gate证明](GATE_PROOF.md) · [事前预测](PRED.json) · [映射与反向检查](DOMAIN_CHECK.json) · [完整预处理结果](PREPROCESS_RESULT.json) · [Exoo Hall证据](Exoo72/HALL_OBSTRUCTION.json) · [Michel Hall证据](Michel72/HALL_OBSTRUCTION.json)。
