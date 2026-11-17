# 757与766的共同末对、完整路径产品和实际双匹配

2026-11-05。本文忠实转写Root与授权作者冻结的推导，全部新数学为 **same-session、unreviewed/unaccepted**。主成果是一般fork排除、最大红路径产品及其真实反例、满balanced母体的双色实际匹配/Ferrers子类排除。仍无新的全局40/50/75/76改善；没有本轮外审或新SAT。

本文N_sig指完整有序rank-3模型的**最大避形人口**，不是forcing threshold。a16为747的既有有效文献上界输入；b25为756及换色模型的共同容量输入，沿用完整有序rank-3、no B5/R6/weak7限定域的人工接受与原same-family/provisional保证，25点存在性另有实际见证。记C=N_sig(7,6,6)、Q=N_sig(7,6,7)。40/50/75/76仍是原结构工作链，b25接受不连带升级整链或本稿状态。[C8原接受范围](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>) · [25点见证回执](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n756-professor-review-20261027/evidence/E21/verification.json>)。

## 1. 一般757型fork排除

固定n,r≥4。X为完整有序rank-3 signotope，禁B_r、R_n、weak(n)。路径长度计实际顶点；weak(n)禁止同实际首末点的两色路径长度和至少n+2，不要求内部不交。完整packet按abc、abd、acd、bcd至多一次变色，故单色路径对子序列遗传。

**定理1。** 设有实际路径

\[
P=R_{n-2}(a,\ldots,u,v),\qquad
Q=B_{r-2}(b,\ldots,u,v),
\]

其中u<v<z且χ(u,v,z)=R。则z不能是ambient实际R_(n−1)的源。

**证明。** 反设有实际出红路径R_(n−1)(z,x,y,…,t)。对每个w<z，若χ(w,z,x)=R，就前接w得到R_n，所以

\[
\chi(w,z,x)=B.
\tag{1}
\]

若χ(u,v,x)=R，则P+x是实际R_(n−1)(a,x)，而式(1)给实际B3(a,z,x)。它们同端且长度和n+2，违反weak(n)。故χ(u,v,x)=B。

若χ(v,x,y)=R，以v替换出红路径首点z得到实际R_(n−1)(v,t)。另一方面，P+z也是R_(n−1)，不能再后接t，所以χ(v,z,t)=B。实际B3(v,z,t)与前者同端，再次违反weak(n)。故χ(v,x,y)=B。

将x、y接到Q之后，新增两项恰为蓝色χ(u,v,x)、χ(v,x,y)，得到B_r，矛盾。证毕。

n4、r4边界中相关短路径可为两点；以上追加路径及三元组仍逐项成立。实际次序反向给首对/末对交换的版本；换色后交换红蓝帽参数及对应路径颜色，不保持原非对称参数不变地调用。

### 1.1 经典满核后接点的整族推论

设K无B_(r−1)、R_(n−1)，且达到经典容量

\[
|K|=\binom{r+n-6}{r-3}.
\tag{2}
\]

经典满容量末对定理给K的同一实际末pair(u,v)同时承接B_(r−2)、R_(n−2)。其满目录证明是：全部经典状态盒饱和，完整盒只归最大点，唯一coatom归倒数点，有向差迫实际末pair达到两色最高秩；Pascal分块同时取等又把实际供应运输到该末pair。这是已有全参数结果，并非本稿重新认领。[R23 §6](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>)。

若K<z且K∪{z}仍无B_(r−1)，则χ(u,v,z)不能蓝，否则延长共同蓝路径为B_(r−1)。所以该三元组红，定理1排除z作为ambient R_(n−1)源。这排除整个经典满核后接through族，不要求所有KKz三元组都红。

在757中取n7、r5，经典K人口为15。故K15后接z形成上述16点侧时，z不能是ambient R6源。

### 1.2 40点canonical caller的准确剩余

设canonical侧A为没有ambient入B4的点集，B为没有ambient出R6的点集。若|X|=40、A=K15∪{z}、z=max A，且K无R6，则上述fork迫z∈A∩B。沿用canonical覆盖A∪B=X、|B|≤25，计数得到

\[
|B|=25,\qquad A\cap B=\{z\}.
\tag{3}
\]

|A|=16超过经典no B4/R6容量15，故A确有R6。A内任何R6必须用z，并因z最大而终于z；所以z也不能是ambient B4源，否则连接给B5或R7。此处仍未排除唯一H入残余。受限K入本来就要求z之后有两个更大的A点，而z=max A使其为空；不把这个空类记作新的临界成果。一般满16侧及唯一H入支仍须继续处理。

## 2. 完整最大红路径的红join产品定理

取非空有序连续块X1<⋯<Xq，各自为完整signotope。保留块内染色，令跨两个或更多块的三元组全红，称为本节的**全红跨块join**。它与旧递归构造中混色的正/负join不同。

**定理2。** 设第i块红高为h_i，全部最大红路径族为P_i；τ_i、ν_i分别是该完整族的物理点最小横截数与最大不交打包数。则全红跨块join合法，红高为Σh_i，全部最大红路径恰为各P_i的笛卡尔产品，且

\[
\boxed{\tau=\min_i\tau_i,\qquad \nu=\min_i\nu_i.}
\tag{4}
\]

蓝路径长度至少三时只能位于单块；跨块同端的最长蓝路径为两点。

**证明。** 四点全在一块时由旧packet合法；三点同块、一点外部时，新packet形如(c,R,R,R)或(R,R,R,c)；其余跨块型四项全红。因此所有新packet至多一次变色。

任一红路径在每块内的子序列是红路径，故总长至多Σh_i。反向，把各块任一最大红路径依次连接，所有接缝三元组全红，达到该和。达到总和就必须在每个块都达到h_i，故完整最大路径族正是产品。

若一个物理点集H没有在任何块中横截完整P_i，则每块都可选一条避开H的最大红路径，其产品也避开H。所以任何全局横截至少在某一块横截P_i，大小至少min τ_i；反向，横截最便宜的一块已击中每个产品，得到τ等式。

任何全局不交打包投影到每块都给局部不交打包，故ν≤min ν_i。反向，取d=min ν_i条局部不交路径，在每块任选d条并逐号连接，得到d条全局不交产品路径，得ν等式。

若蓝路径至少三点且跨块，取其中跨块三点的子序列；它应蓝，却按构造红，矛盾。因此蓝长路径只能在单块。两点路径可视为蓝，故跨块同端蓝高恰二。证毕。

### 2.1 六点因子与十二点767反例

令Z6=L3<R3，完整规则为LLL蓝、RRR红、LLR红、LRR蓝。其跨块四点packet分别为BRRR、RRBB、BBBR，均合法。任何四点都含相反色三元组，所以红/蓝高均三。

全部红三恰为9条LLR加一条RRR，共10条。任意两条相交：LLR的补集是蓝LRR，RRR的补集是蓝LLL，故不存在互补红三。全部R点是三点横截；任何两点若都在L，漏RRR；若一左一右，剩余两L加一R给漏边；若两点在R，剩余R加两L仍给漏边。因此完整R3族满足τ3、ν1。

取Z6全红join Z6。定理2给红高6、蓝高3、全部100条R6，τ3、ν1。块内同端两色长和至多6，跨块同端蓝2、红至多6，和至多8；故母体禁B6、R7、weak7，是实际767。它严格反驳普适

\[
\tau(\text{全部实际 }R_6)\le2\nu.
\tag{5}
\]

该十二点例还具有实际几何实现：两组整数坐标为

\[
\begin{aligned}
&(0,0),(1,1),(2,0),(10,100),(11,99),(12,100),\\
&(100,5000),(101,5101),(102,5200),\\
&(110,6100),(111,6199),(112,6300).
\end{aligned}
\]

全部220个整数方向行列式非零，逐三元组与符号join染色一致；这是既有Linux精确回执的范围。[INPUTS.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_join_product_counterexample_20261105/INPUTS.json>) · [全部行列式](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_join_product_counterexample_20261105/coordinate_determinants.json>) · [完整join12证书](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_join_product_counterexample_20261105/join12.json>)。

### 2.2 十一点766变体

取Z6全红join一个全蓝五点块。第二因子最大红路径是全部10个两点对，横截数4、打包数2。故产品红高5、蓝高5，全部100条R5，τ3、ν1。跨块同端蓝2、红至多5，块内两色和也至多7，故是实际766。

这说明即使在balanced766，全部R5的普适τ≤2ν也失败。[完整join11证书](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_join_product_counterexample_20261105/join11.json>)。旧706例未命中必须按有限样本重新定位：615例为空族、91例ν1并有二点cover，不能代表全域；旧报告和原运行记录不改，只在这里记录被实际反例否定的普适外推。

## 3. 满balanced母体的实际双色匹配与Ferrers排类

固定p≥4。X禁R_(p+1)、B_(p+1)、weak(p+2)，两个取向的短帽容量均以b为有效界，且|X|=2b。令S_R、E_R为全部实际R_p源、末，S_B、E_B为全部实际B_p源、末。

**定理3。** 有实际不交分划

\[
S_R\sqcup E_B=X=S_B\sqcup E_R,
\qquad |S_R|=|E_B|=|S_B|=|E_R|=b.
\tag{6}
\]

令

\[
L=S_R\cap S_B,\quad U=E_R\cap E_B,\quad
T_R=S_R\cap E_R,\quad T_B=S_B\cap E_B.
\]

则|T_R|=|T_B|=t，|L|=|U|=ℓ=b−t>0。在Y_R=X∖T_R中，全部R_p源为L、末为U，其**全部实际路径**端点二部图有完美匹配；蓝色对偶图来自Y_B=X∖T_B，也有L到U的完美匹配。两图没有共同边。

**证明。** 若同一实际点同时属于S_R、E_B，将其入蓝p与出红p连接，桥蓝给B_(p+1)，桥红给R_(p+1)，均不允许，所以S_R∩E_B为空。删除S_R后无R_p，由短帽容量得|S_R|≥b；删除E_B后无B_p，也给|E_B|≥b。总人口2b迫二者各b且覆盖全X。换色同理，得到式(6)。

两份分划给四块L、U、T_R、T_B，人口相减得两个through块同为t，另外两块同为ℓ。实际最小点不能是任色p路径末点，因此按式(6)属于L，故ℓ>0。

Y_R中一条R_p的源只能在S_R∩Y_R=L，末只能在E_R∩Y_R=U。Y_R人口2b−t=b+ℓ。任取其完整端点图的vertex cover，删除这些**实际物理点**后无R_p，剩余人口至多b，所以cover大小至少ℓ。两侧L/U各ℓ点，Kőnig定理给大小ℓ的匹配，即完美匹配；它也兑现每个L点确为源、每个U点确为末的完整身份。蓝色对偶相同。

若两图有共同边(l,u)，便有同端R_p、B_p，长度和2p≥p+4，违反weak(p+2)。所以两图边不交。证毕。

**Ferrers整类推论。** 若任一色图的源邻域按包含构成全序，则该完整满2b类不存在。

**证明。** 取该色的最大源邻域。由于该图有完美匹配，全部U都出现在某个邻域中；全序最大邻域因此等于U。另一色完美匹配在同一个源处有一条到U的边，与第一色共同，矛盾。证毕。

这排除的是明确Ferrers子类，尚未证明任意满母体都进入该类，不能认领C49。

### 3.1 实际交替四边的内部点限制

设有实际交替四边，红边l1→u1、l2→u2，蓝边l1→u2、l2→u1。红色两条实际p路径不能共享两个内部点x<y：否则路径遗传给红四(l1,x,y,u2)，与实际蓝p(l1,u2)同端，长度和p+4，矛盾。换色同理。

这只是交替四边上真实路径的共享内部点限制，不是完整匹配交换定理。任何重路由仍须补回失配原源，不能把单边改动直接称为增广。

## 4. 解析反检：没有共同末pair不迫747人口至多14

候选“747没有同末pair的R5/B3则人口≤14”是假的。取经典满K15，无B4、R6。其顶点state是2×4网格下集；15顶点恰占全部15下集。含右上角(2,4)的下集只能是完整矩形。状态单射，且u<v时D(v)不包含于D(u)，所以完整矩形只能归实际最大点t。

任一实际末pair若同时承接R5与B3，其末点state必含(2,4)，故必终于t。删t后，K14所有这种共同末pair都消失。再添最大新点z，将所有含z的三元组染红。新packet为RRRR或BRRR，旧pair路径不变，新末pair蓝高至多2；红高至多6、蓝高至多3，旧端点和至多8、新端z和也至多8。因此所得15点是合法747，仍无共同R5/B3末pair。

这是依赖完整经典状态目录的解析构造，不需枚举或几何坐标；本轮没有为它编造单独机器回执。满目录与有向差来源见 [R23 §6.2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>)。

## 附录：带额外蓝三的766型fork

设n,r≥4，X禁R_n、B_r、weak(n+1)，有P=R_(n−2)(a,…,u,v)、Q=B_(r−2)(…,u,v)，u<v<z且uvz红。再假定有实际B3(a,s,z)、出红R_(n−1)(z,x,y,…,t)与实际B3(z,w,t)。这些实际输入不能同时成立。

证明：R_n禁止给每个h<z的χ(h,z,x)=B。若uvx红，P+x为红n−1，与B4(a,s,z,x)同端，长度和n+3，违反weak(n+1)。若vxy红，以v替z得到红n−1(v,t)；而P+z不能接任何h>z，故χ(v,z,h)=B，取h=w得到B4(v,z,w,t)，同端再矛盾。所以uvx、vxy都蓝，Q+x+y为B_r。证毕。

n=r=6即766中的R4/B4共同末pair版本。两个额外B3尚无全50进入定理，仅保留为未闭caller，不记人口净收益，不生成额外证书。

## 5. 准确结论

上述工作关闭经典满核后接through族、满balanced的Ferrers子类，并给出通用2ν路线的真实反例；canonical40点caller仍是归约，非全类排除。一般工作链仍为40/50/75/76，未取得C49、Q≤C+b或全局74。实际证据与恢复点见 [VERIFICATION.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-757-766-structure-20261105/VERIFICATION.md>)、[NEXT_SESSION.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-757-766-structure-20261105/NEXT_SESSION.md>)。
