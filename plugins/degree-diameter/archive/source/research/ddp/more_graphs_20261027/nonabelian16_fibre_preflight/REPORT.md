# D8×C2的uniform Aut＋two-shift纤维被AAAA必要条件排除

事前预测“非交换commutator能补出第四bit，使重复标签四步覆盖全部16点”被**完整960项枚举**反驳。真正Aut共有64个，每个15个非单位h，成功数0，最大端点数12。按约定停止这一统一纤维族，不进入其余25紧词、edge-local、其它group或大图搜索。

## 固定72控制器及比较层次

继承现存 `breadth_20261027_wave11/binary72_tight_words/required_words.json`：原72控制器来自 `breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json`，逆标签 `[3,2,1,0]`、含26种真正unique4紧词；aaaa和其逆词各对应18个有序控制槽。这里只读取该小词表，没有重导控制器、旧1152图或旧枚举，更没有BFS。

目标是(Δ,D)=(8,4)，假想n=72×16=1152。此轮只检查必要的AAAA纤维容量，**actual n、actual D均null，未生成图**。原F2⁴ companion cyclicbasis成功AAAA仅作继承对照，没有重算。

## 群约定、归约和完整枚举

元素id `i+4j+8k` 表示 rⁱsʲtᵏ，i∈Z4、j,k∈Z2，乘法为

`(i,j,k)*(u,v,w)=(i+(-1)^j*u mod4, j xor v, k xor w)`。

原关系 `R(x)={φ(x)g0,φ(x)g1}` 令f0(x)=φ(x)g0、h=g0⁻¹g1，ψ(z)=g0⁻¹φ(z)g0，则四步端点等于

`f0^4(x) * ψ³(h)^e0 * ψ²(h)^e1 * ψ(h)^e2 * h^e3`。

左乘f0⁴(x)不改变端点个数；ψ仍是Aut，反过来取g0=1可实现任意ψ。因此枚举全部ψ及h≠1已覆盖任意g0，无须再乘16个offset。h=1只有一个分支，显然不能满足16覆盖。

枚举生成元images(R,S,T)：R必须保持order4，S/T必须平方为1，再检查SRS=R⁻¹及T与R/S交换；将每个normalform映射到RⁱSʲTᵏ，只有16元素bijection保留。order预筛576个triples，presentation合格128个，其中64个bijection；另逐一校准所得map与全部群乘法相容。order4预筛不丢任何真Aut。

对64×15=960项逐个计算全部16个ε有序产品，覆盖数分布：

|不同端点数|case数|
|---:|---:|
|2|192|
|4|320|
|7|128|
|8|192|
|12|128|
|16|0|

完整枚举计时CPU0.016543秒，单worker；无新依赖、哈希或形式化工作。代码 `check.py`、完整统计 `RESULT.json`、空成功表 `successful_cases.json`均保存。

## 一个max12具体反例

`max12_fixture.json`给ψ(r)=rt、ψ(s)=rs、ψ(t)=t及h=s。方向序列ψ³(h),ψ²(h),ψ(h),h的ids为 `[15,14,5,4]`。16个ε端点按字典序为

`[0,4,5,1,14,10,9,13,15,11,10,14,1,5,6,2]`。

其中0011与1100均落id1，0100与1011均落id14；缺ids3、7、8、12。该Aut确实非平凡且存在非单位commutators，但没有得到独立的16种端点。这只是完整枚举最大值的一份可读fixture，不被当作独自证明全族排除；全scope由960项完整枚举给出。

严格关闭范围：固定D8×C2、每个global标签采用一个uniform automorphism和两个rightshifts、同标签AAAA四次、无额外内部translation通道。未排除别的非交换16点群、任意二邻接关系、edge-varying relations或其它控制器；按本任务不自动展开这些变体。整族已在首个必要词失败，所以不需计算另25词或完整1152覆盖。
