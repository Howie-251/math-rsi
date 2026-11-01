# 二十二点最小度七：非B输入的非单交图最小度至少四

## 1. 定理与实际对象

设H是在22点上有35条互异五元边的点对覆盖超图，每点度至少七。以原边为顶点定义简单图Γ：两条不同原边相邻当且仅当交大小不等于一。**若H非B，则δ(Γ)≥4。** 等价地，只要这种H有一条原边的Γ度至多三，H就可二染。

这里不假定最高点度、点对共度上界或临界性。结论只排除非B输入中的小Γ度边，不是已经证明整个22点最小度七分支可染。

[无条件21/22点三度门](TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md)已证明：任意此点数、35条简单五边输入，只要有原边Γ度至多二就可染，不需要本稿点度或点对覆盖。因此只须考虑某条实际F满足qΓ(F)=3。

## 2. 实际q3边到完整有限必要域

固定F的五点编号0..4。其三个异常邻边与F的交迹只能为空或大小2/3/4；26个允许五位mask的三重多重集共有3276份标签，按S5坐标置换为91轨道。重迹允许重复，因为不同原边可有同一F迹。其余31条原边各只交F于一点，令其附件数为a_i，∑a_i=31；令h_i为三个异常迹包含Fi的重数，则

\[
d(F_i)=1+a_i+h_i\ge7,
\quad4a_i+\sum_{T\ni i}(5-|T|)\ge17.
\]

第二式只把17个外点的覆盖所需关联作必要下界，允许重复覆盖；没有把它当成外部边可任意实现的充分条件。

[完整22点域生成](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/PREFLIGHT.py)使用22点重新推导的锚点随机染色常数，得到546份锚尾，再由上述两条件留下26迹轨道/277份必要profile。[DOMAIN.json](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/DOMAIN.json)保存全部输入。每个实际q3输入经真实重标号必映到其中；反之这些整数profile不被宣称都能实现为H。

[旧16固定位置的22点计数](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/FIXED22.py)在自由17点、17!分母、零quota下核全部277份，247份给严格染色界，余30份；[完整结果](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/FIXED_RESULT.json)保留所有失败profile。没有从21点同位置的数值搬来22点证书。

## 3. 实际clean点与共同坐标运输

记三个异常迹大小和为s。三异常原边外部分的并最多15−s点，因此17外点中clean点至少s+2。F总度36+s，外总度139−s；全部点度至少七，所以存在实际clean点z，其度数介于七与

\[
6+\left\lfloor\frac{22}{s+2}\right\rfloor
\]

之间。z不在任何异常原边中；全部过z原边都为F-singleton。由paircover，正向量s_i=λ(z,Fi)≥1，∑s_i=d(z)，且s_i≤a_i。将同一35份原迹中s_i份singleton迹移到{z,Fi}，准确恢复这六锁视图。

[CLEAN22.py](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/CLEAN22.py)对30尾的保证度数范围完整生成1045个必要clean星，使用原五锁位置与六个旧插槽、22点/自由16点/16!、零quota；[CLEAN_RESULT.json](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/CLEAN_RESULT.json)为741 strict、304 nonstrict。此域是实际选择保证与全部允许星向量的松弛域，不是1045个实际超图。

[TRANSPORT.py](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/TRANSPORT.py)只用保持异常迹多重集的F坐标置换，同时搬运附件、clean星、35原迹及位置。因此这是同一原H的重命名，不要求H具有相应自同构。[运输结果](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/TRANSPORT_RESULT.json)将30份必要尾压到以下五标签源（编号是30尾中的索引）：

|source|三异常迹|附件a|
|---:|---|---|
|20|7,27,29|8,5,5,6,7|
|21|7,27,29|8,5,5,7,6|
|22|7,27,29|8,5,6,6,6|
|23|7,27,29|8,6,5,6,6|
|24|7,27,29|9,5,5,6,6|

该表只断言：若原H仍非B，则所选q3边的实际角色必在表中。它不是原H分类，也不保证表中某行存在实际实现。后续集合引理将五行全部直接染色，不需再对clean点逐一求矛盾。

## 4. 五个角色统一直接染色

三个mask7、27、29均含坐标0且还有别的F点。令F0红、其余四个F点蓝，则F和三异常原边都已proper。

外部L=V∖F恰17点。每条附着F0的原边给外四集A，其不全红即可proper；每条附着蓝F点的原边给带索引四集B，其不全蓝即可proper。同一F0下的A族互异，否则对应原五边相同；不同蓝anchor的B可以重复，必须保留原索引。

source20..23有八个A、23个B，[八红/至多24蓝通用引理](../../context/propertyb35-paper/round01/middle/eight_red_foursets_seventeen_20261020/PROOF.md)直接给外部10红7蓝，使所有这些原边proper。具体四源caller另见[实际八红连接](../../context/propertyb35-paper/round01/middle/twentythree_global_reduction_20261020/TWENTYTWO_Q3_EIGHT_CALL.md)。

source24有九个互异A、22个带索引B，[九红通用引理](NINE_RED_FOURSETS_SEVENTEEN.md)给至少65个外部合法染色。该引理的红坏并集上界13091，22蓝坏风险6292，总失败至多19383<19448。

因此五行都使全部35原边proper，与非B反设矛盾。q3边不可能存在；连同无条件q≤2门，得δ(Γ)≥4。证毕。

## 5. 精确核验、声明进口与范围

上述局部有限证书声明进口如下：

* [VERIFY22.py](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/VERIFY22.py)独立用22点锚阈值/点度/外点覆盖重生277域，再以另一cut组成法重生1045星域；逐35个不同原边索引、1190有序异边对、22 pivot重放全部1322份best，包含non-strict记录。[结果](../../context/propertyb35-paper/round01/middle/twentytwo_min7_gamma_four_20261020/VERIFY_RESULT.json)共29084行一致，CPU3.824944秒。本稿文档交付没有重跑旧域。
* 五标签运输及全部119份运输证书由上列TRANSPORT_RESULT记录；它保持同一H的所有标签和计数，不把各视图独立最坏状态拼合。
* 八红通用集合引理与[精确小核](../../context/propertyb35-paper/round01/middle/eight_red_foursets_seventeen_20261020/CHECK.json)已按其本身范围使用；九红小核见[SHORT_RESULT.json](../../context/propertyb35-paper/round01/root/nine_red_shadow_20261020/sol/SHORT_RESULT.json)，最小共同扣除2353。本稿最终直接染色不需要新增的175个clean8门，也不使用共同池列松弛见证。

九红短证的真实跨家族原回应保存在[GEMINI.json](../../context/propertyb35-paper/round01/root/nine_red_shadow_20261020/GEMINI.json)，独立读核和小算范围见[SHORT_AUDIT.md](../../context/propertyb35-paper/round01/root/nine_red_shadow_20261020/sol/SHORT_AUDIT.md)。Grok的[有效组件替代证明审阅](../../context/propertyb35-paper/round01/root/nine_red_shadow_20261020/GROK_REVIEW.json)也已返回end_turn，实际型号grok-4.7-build/xhigh；仅静态核组件证明及声明的source24连接，未执行程序、未重新读取q3完整分类，不冒充对短证或整个22点分支的审阅。未登记正式proof-checker验收。当前整篇为声明进口的纸面候选；这次范围不包含22点的最终染色、22点六度、23–25点或全局36命题。
