# Port-preserving family的独立scope推导；实验方向已收束

用户最新要求已停止1152局部修补。本记录只保存此前完成的数学计数和验证范围，没有执行S枚举、2520关系筛、survivor验证或图生成。P5存在性在本代理处未检验，不能写成可行或不可行；不等待或自动验收任何survivor。

## 为什么关系数恰为2520、S恰为8重

V=F2⁴，原边0→18参数T、b，输入pair方向k=T⁻¹b=8。取S∈GL4(2)，令T'=S*T、b'=S*b，则输入方向始终为k。对应二邻接线性关系为

`R(x)=T'x+<b'>`。

它确定一个非零输出方向B=<b'>（15种），以及三维quotient间的线性同构

`V/<k> -> V/B`。

每对quotient有|GL3(2)|=(8−1)(8−2)(8−4)=168个同构，故不同关系恰有15×168=2520个。任意上述quotient同构都能lift成可逆T'，并以S=T'T⁻¹实现，计数没有遗漏。

对一条给定关系，T'在三条补空间basis的像各能独立加b'；k的像必须恰为b'而不能为零，所以每条关系恰有2³=8个可逆matrix lifts。等价地，原关系的output stabilizer是

`S(z)=z+f(z)b`，其中f:V→F2线性且f(b)=0。

这种f恰8个，均可逆，因此20160个S以严格8-to-1映到2520个关系。

16个input rows的两点bitmask tuple是完整关系标识；两个参数有完全相同的16-row tuple当且仅当关系相同，故理论去重应恰8重。每条关系内部又因R(x)=R(x+k)只有8种不同row，每种出现两次；这是input-pair对称性，不能和上面的参数8重混为一谈。这里无affine offsets，也没有把任意八对之间的非线性置换算作GL3同构。

## 理论上哪些保护检查可能变化

对固定72控制图，self的全部≤4closedwalk均free-reduce为空，故其deterministic linear/affine drift为identity/零；只需保护branch像空间并集。无参数验证，仅从路径支持可知：

* 非闭tight四路若不经过0–18，列与rank不变；只有经过该边的原unique4路径需要重检。反向路线的rank相同，可按reverse pair去重，但不能把不同路径只按labelword合并，因为此处只有一条边变更。
* 一般单边改动只可能影响端点及其旧邻居的self≤4walk。此族额外固定输入return方向8，使0的其他邻居经过 `u–0–18–0–u` 的像也保持。因此只有N[18]={0,8,18,37,67}这五个self槽可能变化；其余67个沿用原保护事实。这里没有计算或验证五槽的candidate plane masks。
* 目标slot0→10原全部短路恰为AACA(0020)和DCC(322)，后者不经过变化边、rank3不变。offset0下两个proper linear subspaces不可能覆盖16点，所以长四路AACA变为rank4是完整目标fiber覆盖的必要条件，也足以覆盖该单slot；不能代替其他slot的覆盖。

上述三类条件即使有共同survivor，也只是保护范围和目标slot的条件，不是1152图D4证明。按最新指示，本代理不再执行这些检查，不扫描更多损坏槽、不重BFS，也不另开模板。
