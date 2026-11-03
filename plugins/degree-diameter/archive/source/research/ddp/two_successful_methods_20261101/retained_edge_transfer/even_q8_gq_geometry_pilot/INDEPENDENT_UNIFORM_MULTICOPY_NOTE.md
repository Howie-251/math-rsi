# 独立攻击：uniform多copy后，同cap任意helper批次仍受同一二次障碍

2026-11-01。**声明范围内预测成立。** 纸面检查没有遗漏短路线或ownership开销；新的subset-owner toy共6291456配置、1953140个满足中心路线条件的配置，二次界反例0。含编译、唯一新toy执行和汇总共1.112874562 CPU秒／15。此结果是局部扩张不可能性，不新增图、Lean或公开优先权结论。

## 一般abstract host-code版本（不增加实验）

证明无需GF8坐标，也不需要预先固定k。对任意δ正则simple host H，只要中心code C满足：各N_H(c)两两不交，union恰为V(H)\D；D⊆C且D在C诱导图中孤立；C\D诱导matching T，就有一般结论

\[
|C\setminus D|\le\left\lfloor(\delta+k+2)^2/4\right\rfloor
\]

作为uniform k≥1完整复制后、保持cap δ+k且只追加新helper的D3必要条件。openN不交排除D到其他center的2步路线，C中孤立排除其1步路线，所以后文所用短路性质均来自此abstract接口。q8的乘积几何只负责给出该接口及|C\D|=R(R−1)，不是求和证明的额外前提。

**这个一般化仍不能套用旧P33或F9U10。** 继承已有metadata：q7 P33源160050，1650中心的pinunion105600，旧余54450点并非全部位于C；F9 U10源56862，810中心pinunion43740，旧余13122点也并非全部位于C。它们不满足D=V\unionN⊆C，可能有本证明未覆盖的自由旧pin路线。这里没有重测这些旧集合，也不宣称它们已有all-k jointbatch上界。

## 1. 继承的结构，以及uniform饱和实际给了什么

继承已接受源的结构，不重验域或投影：H为δ正则，完整中心code C=O×spread，|C|=R²，open N_H(c)两两不交，union恰为H\D。C_off=C\D的大小M=R(R−1)，其诱导图是matching T；D到C_off不存在1／2步source路线。D不属于任何center的openN。

给**每个**center恰好k≥1个clone，每个clone只连不可变的原N_H(c)，保持cap Δ=δ+k。这时每个旧非D点恰好收到k条clone边，degree恰Δ，不能再接新helper。D的degree仍δ，每个clone的原degree也为δ，各有k个spare。允许任意非空有限新helper集合B，以及B内部任意simple graph；只增加与这些新helper有关的边，所有此前存在的边均固定。

于是新helper的旧邻居只能来自D或现有clones。多个helper可以接同一个clone，也可以分别接同一baseclass的不同clones，不能再假设class唯一owner。

## 2. 多owner没有带来新的三步route类型

固定h∈B及旧c∈C_off。记S_c⊆B为至少邻接一个baseclass c现有clone的helpers，允许空集及任意多个owner。d_h为h在B内的degree，N_B[S]为集合S的闭邻域。

由于c是饱和旧点，没有helper–c边。按第一步分类：

1. **h先到旧D。** 余下两步沿旧source不能到c；D不邻接任何现有clone。若第二步改到新helper，最后一步仍不能接饱和的c。D有k个而非1个spare不改变这些路线长度。
2. **h先到baseclass e的现有clone。** 再一步到c要求c∈N_H(e)，即e=T(c)。若再经旧u到c，则u∈N_H(e)∩N_H(c)，由中心openN不交强迫e=c。e=c时确实有h–clone_c–u–c的长度3真Walk（取任意u∈N_H(c)）。若clone第二步改到新helper，最后一步又无法接c。此前的clones之间没有边。
3. **h先到新helper g。** 剩余两步能到c，只能g接baseclass T(c)的clone，再到c。经D或另一helper都不能完成最后一步。

因此精确的中心覆盖条件仍是

\[
h\in S_c\cup N_B[S_{T(c)}].
\]

充分方向也给出实际长度≤3的Walk：owner of c用共享旧邻点，owner of T(c)用长度2，neighbor of such owner用长度3。owner是哪个具体clone并不影响它的原N(c)。所有这些Walk不需要再增加未来顶点或旧边。

这里只分类helper到旧C_off的路线，是最终D3的必要条件，不是完整全点对D3的充分条件。

## 3. 正确的双计数与degree开销

令t=|B|>0，a_h=|{c∈C_off:h∈S_c}|。每个不同owned class至少要消耗h的一条不同clone边，内部helper边另消耗d_h，因此

\[
a_h+d_h\le\deg(h)\le\Delta.
\]

同class内多条clone边、D pins或diagonal clone pins只会继续消耗degree，不会削弱这个下界。不同helpers同时拥有同一class时，每个helper各自支付一条边，正好由各自的a_h记账；无需唯一owner，也无需估计每class的k²总slot。

对每个c，覆盖B及闭邻域的并集上界给

\[
t\le |S_c|+|S_{T(c)}|+
\sum_{h\in S_{T(c)}}d_h.
\]

闭邻域之间可能重叠，只会让右边过计数，方向始终正确。对全部M个c求和，T是置换，所以

\[
Mt\le\sum_{h\in B}a_h(d_h+2)
\le\sum_{h\in B}(\Delta-d_h)(d_h+2).
\]

对整数d，恒有

\[
(\Delta-d)(d+2)
=\frac{(\Delta+2)^2}{4}
-\left(d-\frac{\Delta-2}{2}\right)^2
\le\left\lfloor\frac{(\Delta+2)^2}{4}\right\rfloor.
\]

最后求和并除以t>0，得到

\[
\boxed{R(R-1)\le\left\lfloor(\Delta+2)^2/4\right\rfloor.}
\]

t=1也直接包含，无需回到旧unused或active-owner论证。旧单helper的R²下界仍可能更强，但本次没有依赖它。

## 4. 必须丢弃旧唯一owner的辅助结论，但不影响新二次界

多owner时，“每class非空”已经不成立。实际新toy的简单witness为M4、t4、内部helper图无边，owner-subsets依次为[全部4个helpers,空,全部4个helpers,空]，T按0↔1、2↔3配对。每个helper都能覆盖全部4个旧center，但两个class未使用。各helper a=2、d=0，最小cap2，恰有M4=floor((2+2)²/4)。

M6/t3也有相同类型witness：[全部3个helpers,空]重复三次，内部无边，a=3、d=0、cap3，M6=floor25/4。

这两例反驳的是把旧“unused不可能”的论证直接扩到多copy，并非本次预测的反例。新证明恰好不使用该辅助命题。

## 5. 唯一新有限实验及实际计数

每class owner是t-bit任意subset。内部helper graph枚举所有simple图，edge mask按i<j字典序。对所有配置检验上面的精确center覆盖条件；对通过者取实际a_h、d_h及该抽象模型的最小cap=max_h(a_h+d_h)，逐项核局部计数、求和链和二次界。

|M|t|配置数|满足center覆盖|其中有empty class|其中有multi-owner class|最小cap|
|---|---|---:|---:|---:|---:|---:|
|4|4|4194304|1486232|37920|1485696|2|
|6|3|2097152|466908|66304|466098|3|

两批合计6291456配置、1953140个route-valid配置，反例0。104224个route-valid配置含empty class，所有这些也含multi-owner。cap分布及具体witness保存于INDEPENDENT_UNIFORM_MULTICOPY_TOY_RESULT.json。

toy没有强加实际k-copy每class可用slot总数，它刻意允许所有owner subsets，是一个更宽的必要关系模型；实际clone pin容量若另加只会删除配置。a+d是它表示的最小degree成本，不冒称toy已实现全部source顶点或全图D3。实际执行是新C++ subset-owner枚举，未调用或重跑旧1078182配置的singleton-owner程序。

编译exit0，用0.891177866 CPU；toy exit0，用0.203202561 CPU；含driver汇总总1.112874562 CPU。RESULT、TERMINAL及stdout/stderr均已终态，0solver、0新图、0BFS、0旧field/projection、0Lean。

## 6. 两个q8机制的精确范围和生成决策

|源|R|δ|被排除的uniform k|最大被排cap|M|该cap二次界|下一cap二次界|
|---|---:|---:|---|---:|---:|---:|---:|
|balanced|65|81|1..45|126|4160|4096|cap127给4160|
|Payne|64|80|1..44|124|4032|3969|cap125给4032|

因此这些k范围内，完成全部C的uniform复制并饱和旧非D之后，任何非空有限helper batch都无法在同cap下保持D3，哪怕batch内部任意连接、cloneclass多owner。这取代“k≥2唯一owner失效所以旧方法不能说”的未决状态，但不改旧文档的历史。

下一cap127/125只使此粗界取等、不再排除；它没有构造意义，也没有授权生产或搜索。本轮不生成k2或其他图，不计record，不声称新公开定理优先权。

结论只关闭uniform完整饱和、旧adj固定、保持同cap的上述追加模型。**不排除**nonuniform copies、饱和前联合生成、改旧边、更高cap、不同初始code或整个A族。下一代若继续，应实质改变上述饱和/路由接口；本次不自动派这些新动作。所有root状态、已有singlehelper/one-copy历史与计数均未修改。

当前远程B/C的三个原目标仍只为q8 source80/81及clone82；这个新增局部lemma不因此算作额外已外审内容、具体Lean实例或新纪录。
