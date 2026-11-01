# 实际四点库存的六pair成本与外行共同预算

设 $H$ 为21点五元点对覆盖超图，所有点对共度至多四。记
$$\kappa(\ell)=\binom{\ell-1}{2},\qquad\tau=\sum_{x<y}\kappa(\lambda(x,y)).$$
取四个不同实际原点组成 $K$，令 $\mu_T$ 为35条原边在 $K$ 上的exact迹重数。六个K内inclusive共度及其成本为
$$\lambda_{ij}=\sum_{T\supseteq\{i,j\}}\mu_T,\qquad
q_K=\sum_{i<j\in K}\kappa(\lambda_{ij}).$$
则 $\tau\ge q_K$。若 $\tau=q_K$，所有不完全在K内的实际点对共度均至多二；这是剩余非负成本全为零，不是对库存可实现性的额外假设。一般余预算 $R=\tau-q_K$ 同时支付全部K外点对及全部K到外点的点对成本。

更精确地，每个 $i\in K$ 的17个到K外点的行共度和为
$$S_i=4d(i)-\sum_{j\in K\setminus\{i\}}\lambda_{ij}.$$
六个K内pair和四组K到外点的17项行**彼此不交**，所以
$$\tau\ge q_K+\sum_{i\in K}h_{17}(S_i),\qquad
h_{17}(S)=\begin{cases}
+\infty&S<17\text{ 或 }S>68,\\
\max(0,S-34,2S-85)&17\le S\le68.
\end{cases}\tag{1}$$
证明与18／19项凸行成本相同：$\kappa(1..4)=(0,0,1,3)$，逐项下界 $0,x-2,2x-5$，三段分别以一／二、二／三、三／四达到。`PILOT.py` 另用17次四值整数DP核全部可行和及不可行边界。

若degree谱保证至少一个最大度点必在K外，该点整行与六K内pair不交，但可与上述四个17项外行重合。此时安全的额外界是
$$\tau\ge q_K+\max\left(\sum_i h_{17}(S_i),\max(0,4D-40)\right),$$
不能把两项再相加。判断“必在K外”只用真实degree重数：全H的D点数超过K内D点数。

## 运输及旧十度四点六余尾

任意K重标记同时运输所有exact迹、degree、inclusive六pair及所选锁位置。$q_K$ 和(1)不变，不需要H自同构。旧三四锁证明仍只按保留A/B侧的D8运输；新的不依赖A/B侧的外点星局部证明可另以S4运输完整库存及证书，二者不能混称同一个群。

旧 $10^4$ 六个失败标签中，S4第一轨四个标签的 $q_K=8$，第二轨两个标签的 $q_K=9$。这六个值由原exact库存计算，不只看四个cross pair成本。故 $\tau\le7$ 时六失败均不可能出现；其余304标签已有独立严格固定证书，直接得到这些低τ实际caller的cap12。

在本次13谱的63余键中，ID84的唯一τ6键及ID89的τ7键因此无需新外点池门；ID89的τ8只可能留下第一轨的四标签。完整旧310域和证书原样导入，未重新扩表。

## 低余预算的共享列接口

对每个实际外点z，记 $c_T(z)$ 为其经过的K-exact迹T原边数，原度 $d(z)=\sum_T c_T(z)$。所有17个原外点共享同一组原边，因此
$$\sum_{z\notin K}c_T(z)=\mu_T(5-|T|),\qquad
\lambda(z,i)=\sum_{T\ni i}c_T(z),$$
以及
$$\sum_{z\notin K}\sum_{i\in K}\kappa(\lambda(z,i))\le R.\tag{2}$$
最后一式不为每个外点重复分配R份预算；所有17视图共用一次R。

当 $R\le2$ 时，不在K内的pair共度均至多三，至多R个K到外点pair可共度三。令 $t_i$ 为第i个K行中共度三的外点数，则
$$\sum_i t_i\le R,\qquad
\#\{z:\lambda(i,z)=1\}=34+t_i-S_i,\qquad
\#\{z:\lambda(i,z)=2\}=17-(34+t_i-S_i)-t_i.$$
这些整数个数必须非负。因此大多数真实七度外点对K的各行至多二；有任一K行共度三的七度外点至多R名。此处只导出必要共享计数，未把可行视图多重集说成实际H。
