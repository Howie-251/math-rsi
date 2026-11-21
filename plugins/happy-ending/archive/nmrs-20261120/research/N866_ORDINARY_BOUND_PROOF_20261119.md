<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# 普通 N(8,6,6) 的全域状态势证明与 Linux 检查证据

2026-11-19。本稿独占维护，只装配本轮普通问题及其实际证据。
**本轮已完整接回普通上界58，因而原59目标已完成。**
H≤9、H≤10、H≤11的原件及上游已独立复核；H11还完成第二次全公式重建及
实际DRAT检查。所有科研程序、求解和证明检查均在权威Linux
`<private-artifact-root>` 执行；没有外审。本稿的“检查成功”指实际DRAT检查、
公式重建和数学接口核验，不是外部评审结论。

## 1. 原问题与本证的准确量词

设X为任意原普通866母体：一个完整的有序rank-3 signotope，
无蓝六点路径、无红六点路径，也无同一实际首末的蓝五点／红五点路径对。
最后一种实际共端路径对就是本项目普通weak8的禁止接口。
以下不限制中性点数、Δ、低池交数、中央人口或某个预先挑选的中心。

单色路径按原自然递增顺序读取连续三元组；在signotope中，同色路径的所有三元组
同色。这由四点packet至多一次变色递推：两个相邻同色三元组迫相应四包全同色，
再逐次插入中间点。因此蓝／红五路若共用首末，不能再共用内部点，
否则其首、该内部点、末这同一三元组须同时两色；所得禁止形确使用八个不同实际点。

本稿证明的是：任何上述原X都有 `|X|≤58`，并保留预算9、10逐层闭合的真实证据。

## 2. 同一原母体的70态势，而非分别选择的两份投影

对实际pair x<y，令

$$r_c(x,y)=\max\{|\pi|-1:\pi\text{为色c路径，末pair为}(x,y)\}.$$

禁六使 `1≤r_c≤4`。记 `d(x,y)=(r_B(x,y),r_R(x,y))∈[4]²`，
并对每个实际点y定义理想

$$P(y)=\downarrow\{d(x,y):x<y\}\subseteq[4]^2.$$

首点的P为空。若x<y，则

$$d(x,y)\in P(y)\setminus P(x).\tag{1}$$

若它属于P(x)，可取u<x使两色入秩均不少于d(x,y)；
真实三元组χ(u,x,y)的那个颜色沿u,x,y严格增长，反而使d(x,y)该坐标
至少比自己大一，矛盾。所以P在原X上单射。

4×4格理想恰有 `binom(8,4)=70` 个。按四列高度
`λ1≥λ2≥λ3≥λ4`、`0≤λi≤4` 编码。证据统一使用0基state id：
按 `combinations({1,…,8},4)` 的字典序列四元组 `w=(w1,w2,w3,w4)`，置

$$\boxed{\lambda=(w_4-4,\ w_3-3,\ w_2-2,\ w_1-1).}$$

这里w、λ的四元分量都按1至4书写，state id仍从0开始。
这个目录和所有差格在程序中与原metadata逐项核对。

令每个目录码的洞变量为h_I：该码不在P(X)中时取真。由于P单射，

$$\boxed{H=\sum_I h_I=70-|X|.}\tag{2}$$

实际三元组χ(x,y,z)=c还给

$$r_c(x,y)<r_c(y,z).\tag{3}$$

式(1)、(3)、原packet及真实共端路径，是后面所有局部核的共同输入。
这不是把不同方向的标签独立最优化，也没有把一个存活洞向量当原X。

## 3. 四矩形的四条真实三路拼成同首末五／五

中央36态指含22而不含33的理想。写成

$$\lambda=(2+d_1,2+d_2,a_1,a_2),$$

两个因子 `D=(d1,d2)`、`A=(a1,a2)` 独立属于2×2理想六态
`00,10,11,20,21,22`。取两个跨度

$$I_0=[00,21],\qquad I_1=[10,22].$$

D、A各取一个跨度，得到四矩形Q00、Q01、Q10、Q11。
每份矩形的四角分别是L、R、B、U，其中L为共同低端、U为共同高端，
R只提高A、B只提高D。

若L到R有红三路、R到U有红三路，而L到B有蓝三路、B到U有蓝三路，
两次拼接分别得到从同一L到同一U的红五和蓝五。
拼缝颜色确实被迫：A线pair的蓝秩在3、4，红秩在1、2；
D线pair的蓝秩在1、2，红秩在3、4。
红路A→D转角不能蓝，蓝路D→A转角不能红，均由(3)排除另一色。
各边中点可以是不同实际点，首末仍是同一份L、U业主。

因此四角全占时至少一条指定色三路缺失。
对两个跨度，指定蓝三路都有规范中点20，指定红三路都有规范中点11；
检查两个相邻差段的另一颜色坐标不增，就由(3)强迫指定颜色。
故边线缺指定色三路时，该规范中点是真洞。

四份完整支撑如下；每行含四角及四条边各自的规范中点：

|矩形|八个列高码|
|---|---|
|Q00|2200,4321,2211,2221,3321,4200,4300,4320|
|Q01|2210,4322,2211,2222,3322,4210,4310,4320|
|Q10|3200,4421,3211,3221,3321,4200,4400,4420|
|Q11|3210,4422,3211,3222,3322,4210,4410,4420|

## 4. 四次收费必须落在四枚不同实际洞

对每份矩形：有角洞便选一个角洞；四角全占便选一条失败边的规范中点洞。
四份角集合互不交；角、行中点、列中点三类互不交；不同线的中点不同。
唯一可能重复的费用是一条边界线被两份全角矩形同时选择。

这不可能。此时该线上四个边界点 `00<10<21<22` 全占。
线上任一颜色pair秩仅有两个可用级，故不存在单色四点路；
两个连续三元组χ(00,10,21)、χ(10,21,22)必须相反。
同一条线在两个矩形中所需颜色相同，因此两跨度至少有一个已经
由其边界中点供应指定色三路，不能同时作为失败边收费。

所以四份矩形到所选真洞是单射。对任意非空矩形子集J，

$$\boxed{\sum_{I\in\bigcup_{j\in J}Q_j}h_I\ge|J|.}\tag{4}$$

这就是全部15个Hall费用；特别中央至少四洞。
若U含m码，`Σ_(I∈U)h_I≥t` 等价于：每个m−t+1元子集至少含一洞。
程序据此生成2876条全为正洞文字的CNF子句。
没有只取四份孤立静态行而丢掉共同收费。

完整纸证原件为
[纯铰稿E.4—E.7](N866_PURE_HINGE_REALIZATION_NEXT.md)；
实际无辅助变量导出程序为
[export_hall.py](../SOURCE_MAP.md#excluded-sources)。

## 5. 所有fresh局部行都作用于同一原X

设某个有限码集S全部实占。每码取其唯一实际P业主，
对理想可比pair使用式(1)的实际共享pair格，对可比三／四点使用
同一个原χ、(3)及原packet，按真实单色路径存在性设置R4/R5变量。
若原局部CNF的实际DRAT证明成功UNSAT，便不能让S全部实占，因而得到通用行

$$\boxed{\bigvee_{I\in S}h_I.}\tag{5}$$

本轮每个可导出通用行的fresh core均有：原full query的实际DRAT成功；
core CNF的另一次实际DRAT成功；仅负占用units、没有正洞unit；
其余子句逐条确在原immutable baseline；纯局部schema逐句通过，
不含外部物理码、继承洞行或threshold counter。

对这些纯局部核，格转置T并交换两色，保持全部条件。
再令 `ρ(i,j)=(5−i,5−j)`、`K(I)=ρ([4]²\I)`。
原实际自然序反转、势改K、pair格改ρ，满足

$$K(B)\subsetneq K(A),\qquad K(A)\setminus K(B)=\rho(B\setminus A)
\quad(A\subsetneq B).$$

相邻原格p、q反向变成ρ(q)、ρ(p)，每色严格增长仍成立；
四包反读保持变色次数，共端两条路反转后仍共端。
R4/R5按变换后实际路径重新定义，不机械交换旧辅助变量。
所以(5)同时有I、T、D=K、DT四个通用像。
原core DRAT核在原CNF上检查；D/DT是经逐子句schema核验的数学运输，
不虚报一份尚不存在的变换后CNF DRAT。

原271行由独占拷贝的原standalone verifier全量fresh回放；
新增208行的59个原核由自包含bundle再次fresh回放；
H10所用96轨feed的25个原核在独立H9审计中全部重新DRAT并核schema。
H11较新162轨feed则另逐原核重放，不沿用旧96轨的计数。

## 6. 全域full base是必要公式，SAT存活不等于母体

原full base对70码的理想可比pair设唯一共享差格变量，
对可比三点设原χ变量，加入逐色严格增长和可比四点packet。
它还由真实四路、五路的前向蕴涵强制R4/R5，禁止同源同末的双色R5。
洞门控保证含未占码的路径约束不会被误当真实路径。
未占pair的无条件唯一格变量可独立选任一非空差格，其他未触发DP置假。
因此任一原母体的实际状态、χ及实际路径，都能扩充成该必要公式的一个赋值。

公式只保留原对象的一部分必要关系；UNSAT足以排原对象。
本轮任何SAT投影、SAT局部模型或未闭分支，都没有被写成原signotope或几何构造。

另两个纯原P事实用于全域query：全局首点P=0000；第二点唯一末pair格11，
故P=1000。这两码都必须实占，对应洞文字单位子句−1、−2。
这是同一原实际P的断言；全域H10、H11证书没有把真P与混合切端条件混用。

H9较小的独立矩阵另用了低17／高17各至少一洞；该事实也有势层面的纸证。
若17个低态全占，空态业主a早于其余16人。低态缺22，任一后pair格有一坐标1，
所以全部终于该pair的真实三元组只能取另一富色g；四包迫g两色分别传递。
g单色五链前添a给原六路，故两色末链秩注入[4]²；16人全占迫44秩点，
其双色四链各前添同一a得到共首末五／五，矛盾。故低最多16；
用第5节K和真反序的合法势运输，高也最多16。

full base原有正向前缀计数器s_(i,j)：前i码中若至少j洞，则s_(i,j)真。
输入、继承、增长子句由实际洞计数直接满足。加 `¬s_(70,b+1)` 就强制 `H≤b`。
不需要精确H、额外Δ、中央孔型或某一选定实际前后端。

## 7. 本轮已经核验的三个预算层

|预算|已核状态|直接对应的普通人口界|
|---|---|---|
|H≤9|独立新725变量、5997子句公式；26个fresh原核重核、旧CNF逐字重建、重新AE及DRAT均PASS|n≤60|
|H≤10|69208变量、2168896子句full base；575通用行、2876 Hall、两首态单位、预算unit−69207；AE20、实际DRAT0并VERIFIED；上游及query独立重建PASS|n≤59|
|H≤11|69208变量、2168962子句full base；641通用行、相同Hall/端条件、预算unit−69208；AE20、实际DRAT0并VERIFIED；42个新源核／162轨、query重建及第二次full DRAT均PASS|n≤58|

H10源CNF SHA256：
`b47b58b2da4a29dfeb2b3122a25cff8f42ef9c6e69cc6d52d41e997aaab2eb32`；
实际100341770字节DRAT：
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]

H11源CNF SHA256：
`4ac85311d51cc9cc731a60d5d189101554e319ed3a861f1a6d78a5f3681e1497`；
实际269214281字节DRAT：
`7d7703f258757851b40f5251d77647f591d4dc75961eedb77cb6da39d62572d6`。

H10独立审计逐字核对full base前缀，并将全部附加子句作为multiset重建：
575行＋2876 Hall＋两条实际首态unit＋一条预算unit，既无漏项，也无额外假设。
H11采用同一接口，只多66条已冻结新通用轨行并提高预算一单位。

## 8. 从checked公式接回普通界

反设原普通母体n≥59。由(2)，其实际P图有H≤11。
第2—6节为同一原X构造了full base及其每条附加约束的真实赋值，
因此该H≤11 query应可满足；但其实际UNSAT证明已经DRAT检查成功，
且独立完整重建后的第二次实际DRAT检查也成功，矛盾。
所以

$$\boxed{N(8,6,6)\le58.}$$

这一步没有要求原X首先落入1750目录。1750枚举仅用于产生、覆盖并验证一些
全域通用行；最终预算query已经对全部70态同时量化，允许任意中央／外侧分布。

预算10的同一论证先给普通≤59；预算11进一步排除全部59点母体。
H11第二次完整重建后的实际DRAT检查耗时279.878秒、返回0并唯一VERIFIED；
本稿另对冻结162轨的42个原核全量重新DRAT，核1982个非占用子句原base成员，
641行及full query附加约束逐项相符。这些回执已经完成，不是运行中推断。

1750分支的完整覆盖及“中央精确30”都不是上面全域证明需要假设的条件。
它们分别是通用行的产生途径和另一份独立结构结果。
中央精确30的原件与机器证书入口为
[中央30编码与状态](../source/reports/n866-scalar-grid-20261119/ENCODING_AND_STATUS.md)、
[中央30证书索引](../SOURCE_MAP.md#excluded-sources)。
本全域58证明不借用该中央上界，也不借用C30构造。

## 9. 证据、复放与保留范围

工作目录：
[Linux回放程序及本地控制证据](../SOURCE_MAP.md#excluded-sources)。
稳定交付入口为
[普通58证据说明](../source/reports/n866-ordinary58-20261119/README.md)、
[核验边界说明](../source/reports/n866-ordinary58-20261119/VERIFICATION.md)。
两份最终full-query独立回执可直接打开：
[H10完整重建与第二次DRAT](../SOURCE_MAP.md#excluded-sources)、
[H11完整重建与第二次DRAT](../SOURCE_MAP.md#excluded-sources)。
本稿作者的上游原核及数学接口独立回执为
[H10上游](../SOURCE_MAP.md#excluded-sources)、
[H11上游](../SOURCE_MAP.md#excluded-sources)。

已完整读回并逐文件核SHA的叶子小证据为
[4.55MB小证据包](../SOURCE_MAP.md#excluded-sources)、
[319文件本地字节校验回执](../SOURCE_MAP.md#excluded-sources)。
包SHA256为 `a94b38b8b2732fd8dd2086b5a2b3cc123cc543659dc6e4165f673525536e51e6`。
解包目录中可直接阅读
[H11全域checker原日志](../SOURCE_MAP.md#excluded-sources)、
[solver原日志](../SOURCE_MAP.md#excluded-sources)，
以及42份fresh原小核、各自DRAT和重核日志。
例如一份13态抽取小核的
[CNF](../SOURCE_MAP.md#excluded-sources)、
[DRAT](../SOURCE_MAP.md#excluded-sources)、
[语义及运输核验](../SOURCE_MAP.md#excluded-sources)
及[再次DRAT原日志](../SOURCE_MAP.md#excluded-sources)
均已本地保存。这是实际抽取核，不声称已证明全局最小。

核心独立回放脚本为
[H9直接预算审计](../SOURCE_MAP.md#excluded-sources)、
[H10全部上游与query审计](../SOURCE_MAP.md#excluded-sources)、
[H11冻结feed与query审计](../SOURCE_MAP.md#excluded-sources)。

权威Linux独立回执分别在本工作目录下
`h9-independent01/VERIFICATION.json`、`h10-upstream-independent01/VERIFICATION.json`、
`h11-upstream-independent01/VERIFICATION.json`。
三份均已真实PASS。
H10、H11完整full-query原件在
`reports/n866-m32-mask-kernel-20261119/global-h10/`、`global-h11/`，
各有manifest、原CNF、原DRAT、solver/checker日志及独立公式重建回执。

旧271包为 `reports/n866-joint-label-order-20261117/merge271.tgz`；
208行全核自包含包为 `reports/n866-m32-mask-kernel-20261119/evidence-bundle.tgz`。
二者在本轮独占目录解包实际回放，不修改旧封存目录。
完整full-query合并包由全核作者维护，稳定交付目录为
`reports/n866-ordinary58-20261119/`，包名
`global-h10-h11-proof-bundle.tgz`；含两份原proof、baseline、全部输入快照、
两份完整重建回执和上游原核。服务端包大小168233569字节。
实际分块读回和最终整包哈希状态以
[包校验清单](../SOURCE_MAP.md#excluded-sources)
及稳定README为准；文件存在或partial均不计作完整读回。
Linux原件已经存在，下载状态不替代前述数学和实际DRAT结论。

此前10626中央四洞＋外侧六洞枚举，独立回放100942计数DAG节点后得到1750必要投影；
这些数值保存为可复用中间证据，而不再作为本轮全域结论尚缺的枚举覆盖。
自己的同scope H10 CEGAR已在全域H10独立重放PASS后按调度有序停止，
91轮已核池、所有证明／日志与停止回执均保留；没有触碰其他作者运行任务。
