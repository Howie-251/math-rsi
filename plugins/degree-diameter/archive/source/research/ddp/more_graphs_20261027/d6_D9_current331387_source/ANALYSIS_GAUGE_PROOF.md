# (6,9)331387 源规范化及6959控制的纸面桥接

本文件使用已恢复的小C绑定、scout gauge算术与既存49-phase容量结果，不重复下载、重算常数、枚词、构图或BFS。公式及数值证据以 [ANALYSIS_GAUGE.json](ANALYSIS_GAUGE.json)、[PROVENANCE.json](PROVENANCE.json) 为准。

## 固定源及左／右边约定

Rodriguez/Canale源使用phase49、normal素数6763、action41，RIGHT乘法

(j,n)(k,t)=(j+k,n·41^k+t)。

三正元为(25,1254),(18,541),(47,4642)。source小C按GEN*vertex发边，即此群的left-Cayley边；目标producer按vertex*GEN发边。对这一单底点、inverse-closed Cayley模型，g→g^-1把left边变为right边（generator取逆仍在S中），所以两种模型图同构。这个结论不作为任意多底点lift的左右约定转换。

sourceD9继承公开完整图；未运行C、下载大图或重验旧BFS。

## phase、共轭与scale

25在Z49中的逆为2。令j'=2j，旧j=25j'，则a'=41^25，RIGHT law仍为
(j',n)(k',t)=(j'+k',n·a'^k'+t)。
source phases因此变成1、36、45。scout已核41^49=1、41^7=569≠1，故exactorder49；a'=184也有exactorder49。

RIGHT translation共轭为

(0,c)(j,b)(0,c)^-1=(j,b+(a'^j−1)c)。

为使首normal b1=1254归零，c=b1/(1−a')，不是未经约定的相反号。已有实际算术给c=2654，三个shifted normals为[0,3868,5184]。第二项非零，故共同乘3868^-1=3100，得到规范源

g1=(1,0)，g2=(36,1)，g3=(45,1512)。

这些步骤是源群同构／自同构，完整保留源图。第二项非零是实际条件，已由scout验证；没有把“次normal总能归一”当作任意三normal赋值的一般结论。若另一个无关赋值第二项为零，不能据此丢掉它，但它不属于本次固定source-normalized控制的完备性主张。

## 新field参数与连通性

source6763之后下一个1 mod49素数为6959（scout的小算术receipt已存），目标阶49·6959=340991。仅将source规范化后的normal整数[0,1,1512]原样代入；这是一条冻结的控制规则，不是从F6763到F6959的field embedding或覆盖定理。

对任意目标素数p及合法actionα（本轮要求exactorder49），取同样三个规范正元。由RIGHT law，

g1^-36·g2=(0,1)。

因此生成子群包含全normal加法群Fp；g1又生成全部phase C49，所以全群连通。这个证明不借旧source连通或直径。phase±1、±36、±45即1、48、36、13、45、4，彼此不同且非零，故inverse-closed connection set为六个不同非单位元素，每项模型simple六正则。真逆始终为(-j,-b·α^-j)，应从目标正元重新计算。

## 全primitive actions与碰撞范围

6959-1=49·142，共有φ49=42个exactorder49 actions。抽象群之间的phase重标通常会改变固定三phase、normal比例或generator角色；没有额外证明时，不能只测试一个action就替代全部42个。这只是本轮42个固定λ控制，不是freeλ或全部degree6 Cayleysets的枚举，允许其中出现图同构重复。

旧field中两个route endpoints碰撞，可能只是某个整数／cyclotomic表达式在mod6763下为零。除非证明该差是适用于所有目标action的普遍恒等式，不能外推到6959及其42个actions。反之，目标某一action的缺项也只直接反驳那个控制；完整42项终态才覆盖本次固定field、fixedλ规则。

既存 [controller容量](controller_capacity/RESULT.json) 给NB≤9总prefix2929687，所有49槽raw至少58581≥6959。它仅通过必要容量；不是field不同端点数，更不是全图D9证书。Cayley左平移在完整目标上传递，实际identity完整BFS的ecc才等于全局D；producer单独负责数值评价和首次完整候选验收。

本paper新常数计算、wordscan、图、BFS、solver均为0。source规范化及连通证明可作为producer同一family记录的证据，不新增独立方法。
