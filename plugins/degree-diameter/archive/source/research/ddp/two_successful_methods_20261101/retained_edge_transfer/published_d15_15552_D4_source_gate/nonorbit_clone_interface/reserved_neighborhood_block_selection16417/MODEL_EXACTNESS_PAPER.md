# 固定v0=0 lookahead模型的精确性

这里只核已执行模型的数学含义，不重读源图、验证field、枚参数、BFS或再solve。模型与literal由实际输出绑定；raw限时结果不是最优性证明。

## 全部旧pin条件，不是completed-target近似

固定原15552简单图G，对controller i取accepted offsets的27个中心C_i。定义

    A[w,i]=|{c∈C_i : w∈N_G(c)}|。

代码从原literal邻域逐中心计数，没有强制A只能0/1，也没用T(i) disjoint替代完整oldN；即使邻域共享olddegree14点，实际load照计。

额外中心v0=0只有一个新clone，向真实N0=N_G(0)每点增加1；因此选块y的最终旧点度为

    d_G(w)+sum_i A[w,i]y_i+1_(w∈N0)。

故最大旧度≤16当且仅当每一原row满足 `A[w,*]y≤16−d_G(w)−1_N0(w)`。新clone自身degree等于sourcecenter原degree14/15，无其他度数障碍。非保护olddegree14容量2允许两次load；保护点为给未来clone留1slot而减到1，完全是精确账，不是额外保守剪枝。

## 相同rowcoeff压缩取mincap是等价约束

同组所有原rows的完整192维A行完全相同，所以对任意y它们的左值相同。要求该共同左值不超过组内全部caps，恰等价于不超过其中最小cap。保全15552原row→group映射可回查保护标志、source_degree、actualcap和compressedcap；没有只保一条较松cap或漏protectedrow。216组的压缩不会漏解，也不会造解。

## y0=0、sum≤32与max目标的含义

额外center0已固定，而block0的W27也含center0；本规则要求865不同中心，因此y0=0是必要distinctness条件，不是任意禁块。已有source全中心profile还保证N(0)中存在olddegree15/cap1点，保护后该rowcap0也会禁止block0；无需为此重算profile。

变量binary，sumy≤32且objective min−sumy。这个优化问题的最优值为−32 **当且仅当** 存在32块的该保留N0选择；返回任何手检32的可行向量即可positive，不必等证明最优。反之，求解超时只返回31不能排32；rawOPTIMAL31也必须保其solver/认证边界，不当一般图上界。模型有实际手检warm31，数学上已可行，因此不是把31不满足的硬sum=32模型误称暖启成功。

## 与旧private16416图的区别

原I32只用于手检start，未固定其余变量。若新32块命中，实际865centers是该新块集的864个点再加原center0，图只保全部15552旧source边；不保证保private16416的clone边。N0预留保证第865clone加入前其中每旧pin度≤15。无newnew边，度数和full-N generic真Walk/oldretraction即可给D4及非D3、任意prefix；这不继承旧不同literal的fresh接受。

本次实际best31、kTimeLimit，故这些positivecaller未执行、未写图。只关闭本轮单次窗口，不关闭固定v0 family或全source clone模型。
