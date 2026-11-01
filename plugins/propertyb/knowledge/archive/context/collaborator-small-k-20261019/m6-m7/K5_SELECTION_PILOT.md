# k=5、M=35 的单位共度低度选点小型算术核对

这是主代理指定的固定参数pilot，不是完整m(5)≥36证明或新的研究Goal。审阅仍为same-family/provisional。假设一个简单五元、点对覆盖、恰35边的超图，v=18..25；不附加正则性。检验D从d0=ceil((v−1)/4)到15，s从2到10。

## 推导核对

记L={x:d(x)≤D}，r=|L|，Z=(D+1)v−175，T=4(D+1)−v+2。在L上的冲突图G以λ_xy≥2连边。最低度≥d0，外部点度≥D+1，所以

`d0 r+(D+1)(v−r)≤175`，即 `r≥ceil(Z/(D+1−d0))`（另取max(0,·)）。

由点对覆盖，`deg_G(x)≤Σ_{y≠x}(λ_xy−1)=4d(x)−(v−1)`。因此有三个同时成立的界：

- 逐点最大度：`2e(G)≤(4D−v+1)r`；
- 低度集总度：`Σ_{x∈L}d(x)≤175−(D+1)(v−r)=(D+1)r−Z`，故 `2e(G)≤(T−1)r−4Z`；
- 简单图：`2e(G)≤r(r−1)`。

取三者最小并向下取为偶数，得到合法`2e_upper`。负上界表示该r不可能，排除之。其他r取 `ceil(r²/(r+2e_upper))` 为Caro–Wei整数保证，再对r取min。这是安全加强；可行r是按这些必要条件留下的松弛域，未宣称每个r都能由真实超图实现。Z≤0时须保留r=0并把保证记0，不能遗漏零点情形。

连续版：Z>0时，`r+2e≤Tr−4Z`，且真实非空r有正分母。恒等式 `(Tr−8Z)²≥0` 推出 `r²/(Tr−4Z)≥16Z/T²`。故严格条件 `16Z>(s−1)T²` 保证整数α≥s。扫描中T始终正。离散版覆盖连续版的每一成功参数已由脚本逐项assert。

## 扫描结果

表中是每个s的最小可行D；`null`表示在指定D≤15域没有此保证。连续判据与有限r判据所得最小D **完全一致**；有限r处理没有降低本扫描的任一最小D。

| v | s=2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|18|null|null|null|null|null|null|null|null|null|
|19|null|null|null|null|null|null|null|null|null|
|20|10|null|null|null|null|null|null|null|null|
|21|9|null|null|null|null|null|null|null|null|
|22|8|null|null|null|null|null|null|null|null|
|23|7|8|null|null|null|null|null|null|null|
|24|7|7|8|null|null|null|null|null|null|
|25|7|7|7|7|null|null|null|null|null|

### v=25、D=7

`d0=6,Z=25,T=9,r≥13`。连续界是`400/81>4`，已保证5个度≤7且两两单位共度的点。有限r界为

`2e≤min(4r,8r−100,r(r−1))`，r=13..25。

所有r的Caro–Wei整数保证至少5；最差整数保证恰5，在r=20..25达到。特别r=25时`2e_upper=100`，`r²/(r+2e_upper)=5`。所以此套必要条件和Caro–Wei不会保证第6个，更不能给九单位锁。这个结论关于选点判据的能力，不是不存在更大实际单位集的结论。

### v=18 的边界

d0=5。D≤8时Z≤−13，可以没有低度点，故保证0。D=9时Z=5、T=24、r≥1，r=1留下且保证仅1。D=10..15有限r的最小保证也均恰1：例如r=v=18时简单图上界可成为活跃界，Caro–Wei仅给1。因而扫描的D≤15内没有保证两个单位共度低度点的选择。此处不能把“未通过选点判据”解读为真实超图无单位共度点，或18点可染路线不可行。

## 执行和产物

命令：`python3 context/collaborator-small-k-20261019/m6-m7/k5_selection_pilot.py`，退出0，运行远小于1秒。只用整数与Fraction；没有随机性、整图枚举或外部依赖。

- `k5_selection_pilot.py`：可重放实现。
- `K5_SELECTION_PILOT.json`：全部(v,D)参数、逐r上界/排除/精确分数、s2..10两种最小D。
- `k5-selection.log`：输出摘要及重点参数。

这些结果只验证低度单位锁的普适选择预算。后续仍须把真实锁的迹分类与概率界、全部原始输入分支及完整证明连接起来。
