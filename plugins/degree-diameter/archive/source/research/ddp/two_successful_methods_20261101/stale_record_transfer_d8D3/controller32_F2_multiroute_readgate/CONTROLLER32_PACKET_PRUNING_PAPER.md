# Typed C32 的精确 packet 剪枝

状态：**支持以下条件下的 exactness。** 本文只核数学接口，不做 controller/word 枚举、数值、图生成、BFS、field、solver 或 Lean；不把局部 word 计数当作新图结果。

## 1. 使用的 actual-model contract

controller 是简单四正则图，每点四条 outgoing darts，各有确定的实际 reverse dart。typed ARC/R charts 的每条 completed affine step 都与实际图边一致，并具有完整 true-inverse 关系。

此外，每条 `p : s → t` 在 t 输出 chart 中，其实际 noise offset 与可用 `q,bar q` 二步返回 offsets，满足 [相邻 binary pencil 引理](ADJACENT_BINARY_PENCIL_PAPER.md) 的同坐标 Fano 4-arc contract。因此，对每个源 fibre 点 x，相邻 controller 层 t 的全部八个目标点都已能在至多三步到达。

这里不能仅由两个 charts 分别“拥有一个 4-arc”的名称推断跨 chart contract；必须是上面同一 endpoint 坐标下的实际 offsets 与完整逆关系。以下剪枝复用这个已满足的 contract，不另检矩阵。

## 2. 为什么可以不生成立即 controller 折返的三词 packet

对实际 controller 路径 `p,q,r`：

- 若 `q` 是 p 的 reverse，则前两步返回源 controller，第三步终点为源的邻点。
- 若 `r` 是 q 的 reverse，则后两步返回 p 的终点，它也是源的邻点。

因此，每个含相邻 inverse 的三词，其整个 fibre image 都落在一个已由 pencil 引理完整覆盖的相邻 controller 层。省去这些 packet 不会损失任何尚未完成的目标层，也不会改变相邻层的完整覆盖结论。

这并不声称 controller 折返在实际 fibre 图中也一定是同一条边折返。它可能改变 fibre 点；省去它的理由是该目标层已有全八点覆盖证明。

四个端口且每条 dart 有唯一 reverse 时，无相邻 inverse 的三词有 `4·3·3=36` 个。这里 reverse 必须取当前 controller 上的实际 inverse dart；只有实际端口约定保证逆标签全局一致时，才能直接比较固定 label。不能把任意同 label 或未经确认的 label 置换当作 reverse。

保留长度 0、1、2 的全部词以及这 36 个三词，再把所有相邻 controller 层标记为 full，和保留全部长度至多 3 的词具有完全相同的覆盖判定。controller 简单性保证上述“邻点”不同于源 controller；同层覆盖仍须由保留的词判定。

## 3. Rank-three 快捷标记与余下的精确判定

对每个保留的实际 typed word w，写其 fibre 输出为

`M_w x + c_w + N_w α`，其中 α 是该 word 各步的二元 noise 参数。

若一个长度 3 的 word 的 **noise matrix** `N_w` rank 为 3，则对每个源 x，它的 image 都是整个 F2³，可直接把该 endpoint controller 层标 full。这里不是检查 `M_w` 的 rank，也不能使用尚未按该 typed controller 路径复合的旧 chart noise matrix。

对于其余目标层 t，必须对每个源 fibre 点 `x ∈ F2³` 分别计算

`C_(s,t)(x) = OR_(w:s→t, length≤3 retained) imageMask(M_w x+c_w+N_w α)`。

全局 D≤3 当且仅当每个源 controller s、每个 x、每个尚未 full 的目标 controller t 都得到八位全满。保留 word 的长度 0 项也必须计入，它提供到自身的零步 walk。

只检查 x=0 不够：不同 word 的 `M_w` 可以不同，随 x 改变的相对 affine 平移可能改变 union。分别具有相同 rank 或相同 image 大小，也不保证它们的并覆盖相同点。word 数、rank-three word 数或各 image cardinality 之和均不能替代逐 x 的实际 OR。

若 completed steps 允许相同完整 vertex-label holding，删除这些停留得到长度不增的真正 Walk；不得删除 controller 相同但 fibre 不同的合法步骤。其余 true-inverse/simple-edge contract 仍须实际模型满足。

结论仅是这个 simple typed C32 模型下的精确覆盖加速，不保证任何 controller/chart 选择成功，也不把先前 goodword 数量预测的反例改写成正结果。没有引入额外生成架构或新参数域。
