<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# 叶支付后的物理例外、全尾次序与强 Hall 整类

2026-11-18。本文按主会话及 `proof_lead` 当轮给定推导整理、展开符号并核对原接口，由指定 Sol worker 独占转写；不改前稿及其他工作者产物。状态为**同会话候选，unreviewed／unaccepted**，没有据本文登记外审或原题整证接受。本文没有运行新数学搜索；八参数重叠切片的实际计算另在 `reports/n866-overlap-order-20261118/` 保存，不由本稿代称通过。

本文的当前出口是：在同一个付叶中心后的真实母体中，物理删除中性口并重建全部路径，取得可核的严格 Hall 增益或真实混合端覆盖。尚未证明每个74点输入自动满足下述条件，故未得一般24截或新的无条件767界。

## 1. 同一母体、固定叶支付与保留孤点的端图

X 是完整有序 rank-3 signotope，禁蓝六、红七及 weak7。路径按实际点数计长；所有颜色、首末角色及删点都绑定同一实际 X。记原 X 全部实际红六的源、末点集为 S、E，令

$$U=S\cup E,\quad T=S\cap E,\quad u=|U|,\quad t=|T|.$$

固定[共同锁块稿§5.2](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md)的真实叶中心付费 J 及退役集 W。其全路径结论及记账为

$$J\subseteq U,\quad T\subseteq J,\quad W\subseteq U\setminus J,
\qquad |W|-|J|=B-t.\tag{1}$$

这里 B 是叶净收益，不是蓝色路径符号。W 的点未被物理删除，只是不再作 $X_J=X\setminus J$ 中任何实际红六的首末；它们仍可作为未标内部点。不能把母体改成 $X\setminus(J\cup W)$。

沿用[中性路径流稿§§1、4](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEUTRAL_PATH_FLOW_20261117.md)，定义

$$P=(S\setminus E)\setminus(J\cup W),\qquad
Q=(E\setminus S)\setminus(J\cup W).\tag{2}$$

H 是 $X_J$ 全部实际红六的首末二部图，顶点集合固定为 $P\sqcup Q$，**包括已经没有幸存路径的孤点**。一条边仅表示至少一条实际红六；未重建全部见证时，不能因选定代表路消失就删边。令 $\nu=\nu(H)$，则

$$|P|+|Q|=u-|J|-|W|=u+t-B-2|J|.\tag{3}$$

本文的中性池均取原 ambient 真中性点，因此避 U、J、W、P、Q。特别中性删集 Z 不删端图的登记顶点，只可能销毁它们之间的实际路径。

## 2. 物理删中性点的精确费用式

取任意有限真中性集 Z，在真实诱导域

$$X_{J,Z}=X\setminus(J\cup Z)$$

中重建全部实际红六。其首末图记为 $H_Z$，仍以原 $P\sqcup Q$ 为登记顶点并保留孤点。删点不能产生新路径，故 $H_Z\subseteq H$。定义

$$\nu_Z=\nu(H_Z),\qquad d_Z=|P|+|Q|-2\nu_Z\ge0.\tag{4}$$

取 $H_Z$ 的最小端点覆盖，与 J、Z 合并，确实截住原 X 的全部实际红六。登记费用为

$$\operatorname{cost}(Z)=|J|+|Z|+\nu_Z.$$

由式(3)—(4)直接得到

$$\boxed{2\operatorname{cost}(Z)=u+t-B+2|Z|-d_Z.}\tag{5}$$

这是该明确构造的费用恒等式，不是原红六超图最小横截的恒等式。基准 $|J|+\nu=25$ 时，只要

$$\boxed{\nu-\nu_Z\ge |Z|+1,}\tag{6}$$

就得到实际24截。若改删非中性端点，应重新说明登记顶点和基数，不能省略这一步而直接沿用中性 Z 的记账。

### 2.1 抽象删末点的无增益界，不能扩大为物理删点界

对于原抽象端图 H 及 $C\subseteq Q$，从一份最大匹配至多删去 |C| 条匹配边，故

$$\boxed{|C|+\nu(H-C)\ge\nu(H).}\tag{7}$$

这里 $H-C$ 只删除端图顶点 C 及其关联边。它没有删除实际母体中的任何内部路径点。

若把 C **物理删除**并在 $X_J\setminus C$ 中重建端图，某条终于 $Q\setminus C$ 的路径也可能以 C 点为内部点而消失。因此真实重建图可以严格小于抽象 $H-C$；式(7)不能被用来否定这种物理删除的额外收益。“窗口末点无增益”的旧结论只在抽象删列的范围成立。

## 3. 混合端覆盖与 Hall 缺额是同一个真实删后接口

任取 $A\subseteq P$。删除 J、Z 后，集合

$$\boxed{(P\setminus A)\cup N_{H_Z}(A)}\tag{8}$$

覆盖 $H_Z$ 的全部边：源在 $P\setminus A$ 的边由左端支付，源在 A 的边由其真实删后右邻居支付。两类角色物理不交。因此

$$\tau_{R_6}(X)\le |J|+|Z|+|P|-|A|+|N_{H_Z}(A)|.\tag{9}$$

这允许同一份覆盖混合选择纯源和纯末，而不是分别优化两个互不相容的端点方案。Hall 缺额形式为

$$\nu_Z\le |P|-\bigl(|A|-|N_{H_Z}(A)|\bigr).\tag{10}$$

若重建整个图并对 A 最优化，得到通常的二部匹配／覆盖恒等式；本文不把未知最优 A 当作已经给出的构造。下一节提供可由一份已知最大匹配认证的整类 A。

## 4. DM 闭包的严格 Hall 增益类

固定 H 的一份实际最大匹配 M，大小 $\nu$。令 $U_L\subseteq P$ 为它未配的全部左点，

$$\delta_0=|U_L|=|P|-\nu.$$

取 $A\subseteq P$ 满足三条可核条件：

1. $U_L\subseteq A$；
2. $N_H(A)$ 中每个右点都被 M 配中；
3. 这些右点的 M 伴根全部仍在 A。

于是

$$\boxed{N_H(A)=M(A\setminus U_L),\qquad
|N_H(A)|=|A|-\delta_0.}\tag{11}$$

证明：A 中已配左点的配偶当然属于 $N_H(A)$；反之，每个 $N_H(A)$ 右点已配，且其唯一 M 伴根按第三条件属于 A，故在 $A\setminus U_L$。M 的单射性给基数等式。原图孤点属于 $U_L$，没有被漏记。

现在物理删中性 Z 并完整重建 $H_Z$。若有

$$D\subseteq N_H(A),\qquad q=|D|,$$

使从 A 到 D 的**全部实际红六**都命中 Z，那么这些列在 $N_{H_Z}(A)$ 中消失，故

$$|N_{H_Z}(A)|\le |A|-\delta_0-q.$$

将此代入式(10)，得到

$$\boxed{\nu_Z\le\nu-q,\qquad
\operatorname{cost}(Z)\le |J|+\nu+|Z|-q.}\tag{12}$$

D 的列仍可从 $P\setminus A$ 收到幸存边。本结论**不要求这些列在整个图中孤立**：这些外部边在混合覆盖中已经由 $P\setminus A$ 支付，且式(11)的闭包把原未配缺额锁在 A 中，不能让外部绕行免费恢复被损失的匹配。

基准 $|J|+\nu=25$ 时，$q\ge |Z|+1$ 就给24费。特别，若一个中性口 z 认证支配 A 到两个不同末点列的全路径，取 $Z=\{z\}$、$q=2$ 即可。这是全见证支配条件，不能只选两条代表红六都经过 z。

## 5. 用实际头区间与全尾首点集合认证删列

上一节的 A 可进一步取付 J 后保留的 clean K 根，并同时满足式(11)的 M 闭包。clean 接口来自[clean 根原稿](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)：其每条 ambient 长红的第二点都是实际真中性 I 口；不能把一般 K 根或候选标签自动当 clean。

令 $\Gamma_X(A)$ 为 A 全部 ambient 真 I 邻口的物理并。每个实际头 $(a,b)$ 有完整未来红扇，且已证的物理区间表示可用于重建这个并。对 $e\in Q$，定义

$$T_J(e)=\{b:\ b\text{ 在原真中性口池，且 }X\setminus J
\text{ 中有从 }b\text{ 到 }e\text{ 的实际红五}\}.\tag{13}$$

这里量化该末点的**全部真实红五尾**，不是每列指定一个尾，也不要求尾在选定的五条流见证内。没有证明表明 $T_J(e)$ 本身是物理区间，本文不作这种称呼。

若 $D\subseteq N_H(A)$ 满足

$$\boxed{\Gamma_X(A)\cap T_J(e)\subseteq Z
\quad\text{对每个 }e\in D,}\tag{14}$$

则物理删 Z 后从 A 到 D 无实际红六。否则取一条幸存红六 $(a,b,x,y,c,e)$：clean 性使第二口 $b\in\Gamma_X(A)$；删去首点的红五尾在 $X\setminus J$ 中，故 $b\in T_J(e)$。式(14)迫 $b\in Z$，与该路径幸存矛盾。

因此式(14)是式(12)的充分认证。它允许 $T_J(e)$ 在 $\Gamma_X(A)$ 外还有其他尾源，也允许 $P\setminus A$ 到 D 有幸存绕行。所需检查只是实际头区间的物理并与每列全尾首点集合的交，不必先枚举每条完整红六。

若同一个 z 对至少两列都是区间并中唯一允许的尾首口，即这些交集均包含于 $\{z\}$，则基准25立即降到24。交集也可以为空；此时该列本来就不会成为删后 A 邻列，但仍应按同一原 H、A、M 记录，不能重选图以偷换缺额。

### 5.1 全尾窗口的正确消费位置

[clean 根原稿§17—§17.1](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)的共同口窗口给的是同一窗口内**所有幸存红五尾末的物理并**，不能逐口各付一次，也不能只登记一条指定尾。五个共同 K 根认证的窗口，其完整尾末并至多4；有真实红四根组时相应并至多1。原 ambient 认证根可以在 J 中，但尾族必须在真实 $X\setminus J$ 重建。

对保留 clean 根 A，若中性例外 Z 之外的全部第二口被已认证窗口覆盖，记这些窗口实际尾末并为 $Q_{\rm win}$。则删 Z 后 $N_{H_Z}(A)\subseteq Q_{\rm win}$，可在式(8)中直接支付 $Q_{\rm win}$。不同窗口的公共末点始终只按同一个物理并计费。

若要用式(12)声称匹配严格下降，仍须对选定 D、同一 M 闭包 A 认证式(14)，或另给实际删后邻域缺额。仅支付某些抽象列并引用式(7)，并不会自动得到额外节省。窗口费用与 DM 删列是两个可衔接的真实接口，不是可以重复扣除的两份独立收益。

## 6. clean 根、真口、纯末的共同独立集容量

回到一般 $m\ge6$。在同一 $Q_m$ 母体与同一实际 R7 分拆中，取整体物理不交的三池：clean K 长红根 A、具有实际红$(m-2)$出尾的真中性口 M、纯长红末 E。这里 M 是口池，不是上一节的匹配，以下把头图匹配数写为 $\nu_I$。

假定从 $A\cup M$ 到 E 完全没有任何 ambient 蓝$(m-2)$。在真实 I 头二部图 $I(A,M)$ 中令 $\nu_I=\nu(I(A,M))$。Kőnig 给该图最大独立集大小

$$\alpha(I)=|A|+|M|-\nu_I.$$

取达到此大小的 $A_0\sqcup M_0$，两池之间没有真实 I 头。按[原稿§19.4](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)的同一实际域证明，

$$D=A_0\cup M_0\cup E$$

没有红$(m-1)$：若从 clean 根发路，第二点必须落在真中性池中，便与无 I 头冲突；真中性点和纯末又不能发 ambient 长红。它也没有蓝$(m-2)$：不能从纯末开始、不能终真实长红根；若终于中性口，原红尾桥会迫一个被独立集排除的真实 I 头；余下到 E 的跨池型已由共同无蓝假设排除。

因此

$$\boxed{|A|+|M|+|E|-\nu(I(A,M))
\le N(m,m-2,m-1).}\tag{15}$$

蓝帽、长红身份、尾和纯末条件都属于同一个实际输入；不能分别选最大独立集和另一份无蓝末池后把两者相加。七参数可调用原 b25 工作进口；本文没有为该进口升级保证层级。

若只拿同一三元匹配中已有的前 j 根和前 j 口，这两侧本来就有 j 条互异真实匹配头，故 $\nu_I=j$，独立集人口仍恰 j；加后面的 $k-j+1$ 个原末点只恢复 k+1。**原有 j 对自身没有额外人口增益。**

要改变容量缺口，必须加入未用根、真口或纯末，重新核全部新旧和新新跨池无蓝边及头图匹配，实际使式(15)左边增大。仅把原有两组 j 点重命名、分别计数或换一份索引，不算增广。

## 7. 当前已闭条件类与仍未闭义务

本文已展开并接回真实费用的，是中性物理删后的式(5)、混合端覆盖式(9)、M 闭包下的严格 Hall 类式(12)、区间并与全尾首点的充分认证式(14)，以及共同无蓝三池的独立集容量式(15)。这些是按当轮给定推导写出的同会话条件结论，不是普适24费。

仍需在任意原74点输入中，实际产生满足 $q>|Z|$ 的闭包／列／全尾认证，或找到使共同容量域超过已知界的未用标签。若只得到原端图删列不等式、若忽略物理删除销毁内部见证、若只支配代表尾，均未完成这一原题连接。后续由 `proof_lead` 给出的数学补充继续写入本文件，不回写旧稿。

## 8. 共同双色次序直接输出实际端截

本节按主会话后补推导接入；其范围与§4的 DM 闭包不同，不要求先把端点基准固定为25。以下先取一般 $m\ge6$，令 $r=m-2$、$b=N(m,m-2,m-1)$ 为适用同模型容量界；应用七参数时为 r=5、b=25 的原工作进口。

仍固定叶付 J，**长红路径**在真实 $Y=X\setminus J$ 中重建，其全部首末位于旧纯 P、Q，登记孤点不删。另选物理真中性池 $\mathcal B$，每个 b 都有原 ambient 红 r 出尾，且 $\mathcal B$ 与 $P\cup Q$ 不交。可以先选原真中性 I 口，也可扩到全部满足真中性及实际出尾条件的口。定义

$$\mathcal L=P\sqcup\mathcal B.$$

在**同一个原实际 X** 中，用全部实际红、蓝 r 路建立图 $\mathcal D$：红 r 从 $\ell\in\mathcal L$ 到 $q\in Q$ 给有向弧 $\ell\to q$，蓝 r 从同样外端给反向弧 $q\to\ell$。图的顶点池 $\mathcal L,Q$ 物理不交；每弧保留实际同端路径见证。

按[严格容量原证明§§2—3](../../nmrs-20261117/source/reports/n766-strict-capacity-20261105/PROOF.md)的 weak-only 双色端图引理，没有双色共同边，也没有双色交替环。该进口不要求 $\mathcal L$ 整体早于 Q。当前有向图的边按两池交替，每个有向环必是这种交替环，故

$$\boxed{\mathcal D\text{ 是同一实际输入上的有向无环图。}}\tag{16}$$

这里**原 X 的短路存在**和**Y 中幸存长路重建**是两种不同操作。不能把任意短路在删点后的消失，倒写成它在原 X 从未存在；也不能把一条原长路在 Y 的消失当成整个首末边已消失。

取 $\mathcal D$ 任一拓扑理想 I，即沿弧前驱封闭的顶点集；称 I 中点为早点，其余为晚点。若晚 P 到早 Q 有红 r 弧，理想性便迫其晚源也在 I，矛盾。因此

$$C_I=(P\cap I)\cup(Q\setminus I)\tag{17}$$

截住 Y 的全部实际红$(m-1)$：任何避 $C_I$ 的这种长路源在晚 P、末在早 Q；删去一个内点后仍是同端红 r，给出被排除的弧。于是

$$\tau_{R_{m-1}}(X)\le |J|+\gamma(I),\qquad
\gamma(I)=|P\cap I|+|Q\setminus I|.\tag{18}$$

这是具体的端点支付构造。它不等同于三层标口网络的最小割 $\kappa$，也不宣称 I 的早晚顺序就是母体原物理点序；I 来自同一双色弧图的共同拓扑次序。

### 8.1 早口未配数给“公共序只差一”条件

在早 P 中选取一池 $A_I$，其点是原 ambient 真长红源的 clean K 根；不能仅因标签写作 K 就省掉这些实际身份。令

$$\mathcal B_I=\mathcal B\cap I,\qquad
N_I=(P\cap I)\setminus A_I,$$

并令 $\nu_I$ 为 ambient 真 I 头图 $I(A_I,\mathcal B_I)$ 的最大匹配数。

早 $\mathcal L$ 到晚 Q 没有蓝 r：否则对应反向弧从晚 Q 指向早 $\mathcal L$，违反理想性。因此§6共同独立集容量可在同一个实际域使用，给

$$|A_I|+|\mathcal B_I|-\nu_I+|Q\setminus I|\le b.$$

记早口的未配数为 $\eta(I)=|\mathcal B_I|-\nu_I$。由于 $|P\cap I|=|A_I|+|N_I|$，得到

$$\boxed{\gamma(I)\le b+|N_I|-\eta(I).}\tag{19}$$

故只要某个共同理想满足

$$\boxed{\eta(I)\ge |J|+|N_I|+1,}\tag{20}$$

直接支付 J、早 P、晚 Q 的费用至多 $b-1$。七参数 b25 时即为真实24截。这里没有额外假定 $|J|+\nu(H)=25$，也没有重复使用叶收益 B。

反过来，若74点反设未被24截排除，则每个合法共同理想及其早 clean 根选择都必须满足

$$\eta(I)\le |J|+|N_I|.\tag{21}$$

可先固定全域 clean 子池再按理想取交；下一节在这种固定选择下把理想优化精确消元。

### 8.2 实际口池的放宽与物理付费边界

若蓝 r 路终于 $b\in\mathcal B$，且倒二点 $a\in A_I$，蓝路的实际末对 $(a,b)$ 有完整未来红扇；将 a 前接 b 的原 ambient 红 r 尾，得到以 $(a,b)$ 为首对的实际红$(m-1)$。这正是一条 ambient 真 I 头，因此§6无头独立集的证明仍适用于扩大的 $\mathcal B$，不要求所有候选口预先登记在某一份匹配中。

若另外**物理支付中性 Z**，在相应剩余池中取同一构造时总付费必须写为 $|J|+|Z|$。充分条件相应要求早口未配数至少 $|J|+|Z|+|N_I|+1$；不能把 Z 所造成的端点退役或匹配下降既记进新图又再免费扣一次。若保留本节原 X 的双色弧图，其理想仍只给安全充分证书；若改建删后短路图，必须重新核容量域与全部实际路径接口，本文不自动替换两种图。

## 9. 用真口集合精确消去共同理想

固定全域 clean 子池 $A\subseteq P$，其点具有§8所需的原实际身份，令 $N=P\setminus A$。对每个拓扑理想 I，统一取 $A_I=A\cap I$、$N_I=N\cap I$，并记 $\nu_I=\nu(I(A\cap I,\mathcal B\cap I))$。所有头均是同一个原 X 的 ambient 真 I 头。

对 $T\subseteq\mathcal B$，令 $\Gamma_A(T)$ 是 A 中邻接至少一个 T 口的根；令 $\downarrow T$ 为 $\mathcal D$ 中含 T 的最小拓扑理想，即 T 及其全部有向前驱。有限二部图的 Hall 缺额公式给

$$|\mathcal B\cap I|-\nu_I
=\max_{T\subseteq\mathcal B\cap I}
\bigl(|T|-|\Gamma_A(T)\cap I|\bigr).\tag{22}$$

N 与 $\Gamma_A(T)\subseteq A$ 不交，因而

$$\begin{aligned}
&\max_{I\text{ 理想}}\bigl[
|\mathcal B\cap I|-\nu_I-|N\cap I|\bigr]\\
&\quad=\max_{I\text{ 理想}}\max_{T\subseteq\mathcal B\cap I}
\bigl[|T|-|(N\cup\Gamma_A(T))\cap I|\bigr]\\
&\quad=\boxed{\max_{T\subseteq\mathcal B}
\bigl[|T|-|(N\cup\Gamma_A(T))\cap\downarrow T|\bigr].}\tag{23}
\end{aligned}$$

最后一步的理由是：固定 T 后，所有可选 I 都包含 $\downarrow T$；所扣根数随 I 包含增加而单调不减，故最小理想 $I=\downarrow T$ 取得该 T 的最大值。反过来每个 T 的这个理想本身合法。这里最大值交换只用有限集合，不替换母体、不重选 p、不对不同口各用一份彼此不相容的次序。

所以若某一批真口满足

$$\boxed{|T|-|(N\cup\Gamma_A(T))\cap\downarrow T|
\ge |J|+1,}\tag{24}$$

它的共同前驱理想直接输出§8的实际24点横截（七参数）。有额外物理付费 Z 时右端改为 $|J|+|Z|+1$，并同步采用已经核清的新池及费用。

任意未排除的74点输入因此必须对**每个** $T\subseteq\mathcal B$ 满足

$$\boxed{|(N\cup\Gamma_A(T))\cap\downarrow T|
\ge |T|-|J|.}\tag{25}$$

这是同一个实际根池中的整批人口必要条件，右端非正时仅保留平凡非负性。被计根可以是非 clean 的 N 根，也可以是邻接 T 的 clean 根；前驱可沿若干交替弧到达 T 中另一个口。**不能据式(25)擅称每个被计根都对同一个指定口同时兼具“邻接”和“前驱”，更不能直接宣称已经构造逐口单射或匹配。**

式(23)—(25)把“寻找共同理想”的问题转成真实口集合及其共同前驱的可核接口，但尚未给所有原输入必有违反式(25)的口集。普适24费仍未闭；本文没有把这个精确消元本身当作数值下降。

## 10. 物理支付中性口与纯末后，重建真实短路的共同理想

本节把§8的原 ambient 短路图改为**删后真实短路图**，并补足相应容量证明。固定 $Y_0=X\setminus J$、旧纯端池 P、Q，以及固定 clean 子池 $A\subseteq P$、$N=P\setminus A$。取原真中性口池 $\mathcal B$，每口具有 ambient 红五出尾，且与 $P\cup Q$ 物理不交。clean、真实长红根、真中性、纯末及口的红五尾仍按**原 X**认证；不要求认证用的臂在 $Y_0$ 幸存。头图及 $\Gamma_A$ 也始终是原 X 的全部真实 I 头。

取 $Z\subseteq\mathcal B$、$D\subseteq Q$，物理支付

$$F=Z\sqcup D,\qquad j=|J|,\quad z=|Z|,\quad d=|D|,
\qquad Y_F=X\setminus(J\cup F).$$

三项支付物理不交。保留旧左端池 P，不注销任何孤根；右端池为 $Q_F=Q\setminus D$，口池为 $\mathcal B_F=\mathcal B\setminus Z$。删点后全部实际红六的首末仍在 $P\sqcup Q_F$，但必须在 $Y_F$ **完整重建**，不能只保留或删除旧代表路。

定义 $\mathcal D_F$：顶点为 $P\sqcup\mathcal B_F\sqcup Q_F$，在 $Y_F$ 中有实际红五从 $\ell\in P\cup\mathcal B_F$ 到 $q\in Q_F$ 时放弧 $\ell\to q$；有实际蓝五时放反向弧 $q\to\ell$。所有路径均按同一个 $Y_F$ 的真实颜色存在性登记。weak-only 交替环引理仍适用于诱导域 $Y_F$，故 $\mathcal D_F$ 是 DAG。

取其任一前驱封闭理想 I。晚 P 到早 $Q_F$ 无红五，因而

$$C_F(I)=(P\cap I)\cup(Q_F\setminus I)\tag{26}$$

截中 $Y_F$ 的全部红六：否则一条避该集合的红六从晚 P 到早 $Q_F$，删一个内点所得同端红五仍在 $Y_F$，与理想性冲突。因此

$$\tau_{R_6}(X)\le j+z+d+\gamma_F(I),\qquad
\gamma_F(I)=|P\cap I|+|Q_F\setminus I|.\tag{27}$$

### 10.1 跨池无蓝只需在真实删后域内核验

令 $A_I=A\cap I$、$\mathcal B_I=\mathcal B_F\cap I$、$N_I=N\cap I$，在 ambient 真实头图 $I(A_I,\mathcal B_I)$ 取最大独立集 $A_0\sqcup B_0$。早 $P\cup\mathcal B_F$ 到晚 $Q_F$ 在 $Y_F$ 中无蓝五，否则反向弧违反理想性。下面直接核验

$$V=A_0\cup B_0\cup(Q_F\setminus I)$$

在其真实诱导颜色中无红六、无蓝五；这足以调用同模型 b25 容量，不需要声称相应跨池蓝路在原 X 也不存在。

若 V 内有红六，其首点只能在 $A_0$：真中性口与纯末均不作 ambient 红六源。该根的 clean 身份迫第二点为真中性口，故落在 $B_0$，产生独立集所排除的真实 I 头，矛盾。

若 V 内有蓝五，它不能从纯末开始，也不能终于 $A_0$ 的真实红六源；分别与原 X 的入红／出红见证作标准桥接，均会得到原 X 禁止的蓝六或红七。若蓝五终于 $b\in B_0$，令倒二点为 w，取 b 的原 ambient 红五出尾、次点为 v。桥 $\chi(w,b,v)$ 蓝会后延该蓝五成蓝六，故桥红，前接 w 成实际红六。因此 w 不能是中性口或纯末，只能在 $A_0$。同时蓝五末对 $(w,b)$ 迫完整未来红扇，将 w 前接 b 的红五尾便得实际红六首对 $(w,b)$；这是独立集排除的真实 I 头，仍矛盾。余下蓝五只能从 $A_0\cup B_0$ 到 $Q_F\setminus I$，但这条路本身完全位于 $V\subseteq Y_F$，已由上述**删后**跨池无蓝排除。

这个证明允许原 X 中另有经过 J 或 F 的跨池蓝五；它们不在 V 内，不妨碍 V 是真实短帽容量域。另一方面，尾和角色的 ambient 见证可以经过已付点，因为桥接反证是在原 X 中完成，不能反称这些见证是 $Y_F$ 的幸存流。

记 $\nu_I=\nu(I(A_I,\mathcal B_I))$，由 Kőnig 独立集大小及 b25 得

$$|A_I|+|\mathcal B_I|-\nu_I+|Q_F\setminus I|\le25.$$

于是令 $\eta_F(I)=|\mathcal B_I|-\nu_I$，有

$$\boxed{\gamma_F(I)\le25+|N\cap I|-\eta_F(I).}\tag{28}$$

付费为 $j+z+d$，不能因为 D 既是纯末标签又销毁其他短路，就在式(27)外再次免费扣除 d。下一两节分别给端图失邻和共同前驱释放的准确净收益。

## 11. 任意根集的 Hall 松弛与物理失邻恒等式

回到 $Y_0$ 的全部真实红六端图 H，固定左 P、右 Q，并令 $\nu=\nu(H)$。本节允许 Z 为任意原真中性删集，不必已列入口池 $\mathcal B$；仍取 $D\subseteq Q$、$F=Z\sqcup D$。令 $H_F$ 为 $Y_F$ 的全部实际红六端图，登记左 P、右 $Q\setminus D$ 并保留孤点。因此

$$N_{H_F}(A')\subseteq N_H(A')\setminus D
\quad\text{对每个 }A'\subseteq P.$$

为避免与固定 clean 池 A 混同，本节用 $A'$ 表示**任意**左点子集；它无需 clean 或 DM 闭包。定义原图的 Hall 松弛

$$s(A')=|P|-|A'|+|N_H(A')|-\nu\ge0,\tag{29}$$

其中非负性来自原图的混合端覆盖。再定义真实失邻列

$$L_F(A')=N_H(A')\setminus N_{H_F}(A'),\qquad
\ell_F(A')=|L_F(A')|.\tag{30}$$

这里一列失邻意指从 $A'$ 到该列的**全部**实际红六见证均被物理支付命中，不是某份代表路消失；支付 D 的列当然属于失邻列。

实际横截构造为

$$J\cup Z\cup D\cup(P\setminus A')\cup N_{H_F}(A').$$

这五项物理不交，故其登记基数**恰好**为

$$\boxed{\operatorname{cost}_F(A')
=j+z+d+\nu+s(A')-\ell_F(A').}\tag{31}$$

它是这个具体混合覆盖的费用恒等式，不是最小红六横截本身的恒等式。证明只需将
$|N_{H_F}(A')|=|N_H(A')|-\ell_F(A')$ 代入该覆盖基数。

对 $A'$ 最优化，二部图的覆盖恒等式给

$$\min_{A'\subseteq P}\bigl(|P|-|A'|+|N_{H_F}(A')|\bigr)
=\nu(H_F).$$

所以又有精确关系

$$\boxed{\max_{A'\subseteq P}
\bigl(\ell_F(A')-s(A')\bigr)=\nu-\nu(H_F).}\tag{32}$$

§4的 DM 强 Hall 类只是 $s(A')=0$ 的一个可认证特例；并非所有有用根组都必须先补成 DM 闭包。特别，窗口方法产生的任意 clean 根组可直接代入式(31)，但必须支付它的原 Hall 松弛，不能假定该松弛为零。

若基准 $j+\nu=25$，式(31)给充分条件

$$\boxed{\ell_F(A')\ge s(A')+z+d+1
\quad\Longrightarrow\quad\tau_{R_6}(X)\le24.}\tag{33}$$

相应地，在同一基准下，若仍无24截，则对所有合法物理 F 及所有 $A'\subseteq P$ 必有

$$\boxed{\ell_F(A')\le s(A')+z+d.}\tag{34}$$

若基准不是25，应保留式(31)的 $j+\nu$，不能直接套用式(33)—(34)。一般无24残余式是
$\ell_F(A')\le s(A')+z+d+(j+\nu)-25$。

### 11.1 付费列与未付列的内部损失分开记账

令

$$q_{\rm paid}=|N_H(A')\cap D|,\qquad
q_{\rm internal}=\ell_F(A')-q_{\rm paid}.$$

第二项计的是原有邻列中**没有直接支付**、却因内部见证全部毁掉而失去 $A'$ 邻接的列。式(33)等价于

$$\boxed{q_{\rm internal}\ge
s(A')+z+(d-q_{\rm paid})+1.}\tag{35}$$

因此付费邻列自身最多抵消对应费用；额外节省必须来自未付列的真实失邻。若支付某个不在原 $N_H(A')$ 内的末点，其费用仍在 d 中，不能当作免费。无24时则式(35)左端至多其右端减1。该区分正容纳“物理删末点会销毁其他列的内部路径”，又不把抽象删列误算为额外收益。

## 12. 固定真口批次的共同前驱释放：删短路的准确净收益

现在固定§10的 P、clean A、$N=P\setminus A$、口池 $\mathcal B$ 及 ambient 头图。令 $\mathcal D_0$ 按 $Y_0$ 内**全部**实际红五／蓝五构造，方向同§10；不是§8直接在原 X 构的 ambient 短路图。对 $F=Z\sqcup D$，$Z\subseteq\mathcal B$、$D\subseteq Q$，按 $Y_F$ 内全部短路重建 $\mathcal D_F$。删点不产生新路径，故

$$\mathcal D_F\subseteq\mathcal D_0[
P\cup(\mathcal B\setminus Z)\cup(Q\setminus D)].\tag{36}$$

包含可能严格：即使一条弧两端都未删除，全部内部短路见证也可能被 F 命中，导致该弧消失。因此不能仅在抽象 $\mathcal D_0$ 删除端标签而代替真实重建。

任取同一批保留真口 $T\subseteq\mathcal B\setminus Z$，令 $\downarrow_0T$、$\downarrow_FT$ 分别为这两个 DAG 中的全部前驱闭包（包含 T 自身）。由式(36)有 $\downarrow_FT\subseteq\downarrow_0T$。固定计费根集

$$C(T)=N\cup\Gamma_A(T)\subseteq P,$$

其中 $\Gamma_A(T)$ 是 ambient 真 I 邻接，不因某份头臂碰到 F 就随意删边。定义

$$\begin{aligned}
g_0(T)&=|T|-|C(T)\cap\downarrow_0T|,\\
g_F(T)&=|T|-|C(T)\cap\downarrow_FT|,\\
\rho_F(T)&=|C(T)\cap(\downarrow_0T\setminus\downarrow_FT)|.
\end{aligned}\tag{37}$$

由于计费根均在未删的 P 中，同一物理根池与同一头图保持固定，集合差直接给

$$\boxed{g_F(T)=g_0(T)+\rho_F(T).}\tag{38}$$

这是**固定 T** 的精确式；不允许左右两侧分别另选最优口集或另换 clean 池后仍声称该等式。$\rho_F(T)$ 计“释放根”：该根原是 T 的前驱，删后已经没有任何 $\mathcal D_F$ 有向路径从它到 T 中任一点。无须物理删除该根，但必须毁掉全部新图中的相关有向路径；一条代表链断开不足以认证释放。计费根若仍能到 T 的另一个口，便仍在闭包内，不能计入 $\rho_F(T)$。

### 12.1 由删后最小理想输出24截

§9的 Hall 消元逐字适用于新的 DAG、剩余口池与同一 ambient 头图，给

$$\max_{I\text{ 为 }\mathcal D_F\text{ 理想}}
\bigl[\eta_F(I)-|N\cap I|\bigr]
=\max_{T\subseteq\mathcal B\setminus Z}g_F(T).\tag{39}$$

特别对任意固定 T，取 $I=\downarrow_FT$；Hall 缺额至少该 T 给出的项，因此式(27)—(28)直接得到

$$\boxed{\tau_{R_6}(X)
\le25+j+z+d-g_F(T)
=25+j+z+d-g_0(T)-\rho_F(T).}\tag{40}$$

故完整充分条件为

$$\boxed{g_0(T)+\rho_F(T)\ge j+z+d+1
\quad\Longrightarrow\quad\tau_{R_6}(X)\le24.}\tag{41}$$

作为纯逻辑充分条件，旧共同次序恰差一即 $g_0(T)=j$ 时，物理只付一个纯末 $z=0,d=1$，若能释放至少两个计费根 $\rho_F(T)\ge2$，式(40)会给费用至多24。所付纯末本身不属于计费根池 P，费用1只支付一次。**但在原端点饱和 $j+\nu=25$ 的硬类内，这一全红五图阈值实际不可达，不能当作可产生净收益的出路。**下一小节给出保留旧红六剪短见证的严格屏障；§13改用更稀疏的真实红六／蓝五图。

### 12.2 无24时的普适残余不等式

若原输入仍没有24截，则对每份合法物理支付 $F=Z\sqcup D$ 及每个 $T\subseteq\mathcal B\setminus Z$，式(40)迫

$$\boxed{g_0(T)+\rho_F(T)\le j+z+d,
\qquad\rho_F(T)\le j+z+d-g_0(T).}\tag{42}$$

在 $F=\varnothing$ 时恢复 $g_0(T)\le j$；记旧缺额松弛 $\delta(T)=j-g_0(T)\ge0$，则一般残余式为
$\rho_F(T)\le z+d+\delta(T)$。特别 $g_0(T)=j$ 时，任何未排除的物理支付必须满足 $\rho_F(T)\le z+d$。

这与§11的匹配失邻恒等式是两种不同的可核收益：一项重建全部**红六端边**并核原 Hall 松弛，另一项重建全部**红五／蓝五短路弧**并核固定口批次的共同前驱释放。二者可在同一物理输入上比较或组合证书，但不能把同一删除自动视作两份可相加收益。本文仍未证明每个74点输入必违反式(34)或式(42)，也未执行这些检测或登记新24数值结论。

### 12.3 更正：全红五图在端点饱和时的单付屏障

设原端图满足 $j+\nu(H)=25$。只物理付一个中性点 w 时，任一旧 $Y_0$ 红六若不含 w 就完整幸存；若含 w，w 不是该路首末，删去这个内点后仍有**同一首末的真实红五**在 $Y_0\setminus\{w\}$ 幸存。故旧 H 的每条边仍是新全红五图的红弧。任何新全红五图理想的端截 $C_F(I)$ 都已经覆盖**旧 H**，所以

$$|C_F(I)|\ge\nu(H),\qquad
j+1+|C_F(I)|\ge26.\tag{43}$$

若只物理付一个纯末 $w\in Q$，对旧 H 中不终于 w 的每条边，同样剪去至多一个内点就保留同端红五；终于 w 的边已经由支付 w 覆盖。因此 $C_F(I)\cup\{w\}$ 覆盖旧 H，给

$$1+|C_F(I)|\ge\nu(H),\qquad
j+1+|C_F(I)|\ge25.\tag{44}$$

结合式(28)，对全红五图任何固定 T，单付中性时 $g_F(T)\le j$，单付纯末时 $g_F(T)\le j+1$。于是当 $g_0(T)=j$，后者必有 $\rho_F(T)\le1$；“单付纯末释放至少两根”的充分阈值在该饱和类内为空。式(38)—(42)作为固定图体系中的恒等式／条件式仍然正确，但不能据此声称全红五图已提供单付降24的实际机制。该屏障只用了旧红六的剪短见证，比单纯说 DAG 不保证释放更强。

**一般剪短屏障。** 本段暂以 H 表示 $Y_0$ 全部实际红 r 路的首末图，左 P、右 Q；共同 DAG 则使用全部真实红 k 短路作为相应正向弧，其中 $2\le k\le r$。固定物理支付 $F=Z\sqcup D$，$D\subseteq Q$，$Z\cap(P\cup Q)=\varnothing$；七参数的 Z 仍按原真中性池选取。对未付端对 $(p,q)\in P\times(Q\setminus D)$，定义稳健端图

$$\begin{aligned}
(p,q)\in E(H_F^{\rm rob})\quad\Longleftrightarrow\quad
&\text{存在一条旧 }Y_0\text{ 红 r 路 }R\text{ 从 p 到 q，}\\
&|\operatorname{int}(R)\cap F|\le r-k.
\end{aligned}\tag{44a}$$

此处是**每个端对存在一份**满足预算的见证，其他见证可以被多次命中。删去其已付内点后至少保留 k 点，首末仍在；同色路径的保端点子序列仍同色，故可取一条 $Y_F$ 的同端红 k。该子序列性质由 signotope 的单色路径闭包给出；$k=2$ 时颜色条件为空。因此 $H_F^{\rm rob}$ 的每条边都是新全短红图的一条红弧。

任何该全短红图理想给出的端截 C 都必须覆盖 $H_F^{\rm rob}$。各支付池物理不交，故这类构造的费用下界为

$$\boxed{j+|F|+|C|\ge j+|F|+\nu(H_F^{\rm rob}).}\tag{44b}$$

若对**每个**旧端对 $(p,q)\in E(H)$、$q\notin D$，均有式(44a)的某份见证，则 $H_F^{\rm rob}=H-D$（保留孤点），从旧最大匹配最多损失 $|D|$ 条边，得到

$$\boxed{\nu(H_F^{\rm rob})\ge\nu(H)-|D|,
\qquad j+|F|+|C|\ge j+\nu(H)+|Z|.}\tag{44c}$$

回到七参数 $r=6,k=5$，该充分的稳健性条件准确写成

$$\forall(p,q)\in E(H),\ q\notin D,
\quad\exists R\in\mathcal R_6^{Y_0}(p,q):
|\operatorname{int}(R)\cap F|\le1.$$

若它成立，旧全红五理想覆盖即使支付多点也不能低于原 $j+\nu(H)$。所以要让该方法产生严格增益，**必要**存在一个未付旧端对，使其**所有**旧红六见证的内部都至少被 F 双击：

$$\exists(p,q)\in E(H),\ q\notin D,
\quad\forall R\in\mathcal R_6^{Y_0}(p,q):
|\operatorname{int}(R)\cap F|\ge2.$$

这只是必要条件，不是节省费用的充分条件：该对还可能有其他幸存红五，其他稳健边也可能维持匹配数。不能只展示某一条旧红六被双击，更不能把破坏一条代表路写成整对已失效。

一个可直接检查的较弱屏障是：固定旧最大匹配 M，若其中至少 $\nu(H)-|F|$ 条边仍有式(44a)的稳健见证，则式(44b)仍给构造费至少 $j+\nu(H)$；在基准25时已足以阻止**这类全短红图理想构造**给出24费。这里没有把该方法的费用下界误作原超图最小横截的下界。以下稀疏红六图不自动承受这些旧红五弧约束。

## 13. 稀疏的真实红六／蓝五共同 DAG

为去掉§12.3中不必要的红五残余约束，以下另建一套图，所有前驱与释放符号均重新定义，**不与旧全红五图混用**。仍固定 P、Q、clean A、$N=P\setminus A$、真口 $\mathcal B$、ambient 真实头图，物理支付 $F=Z\sqcup D$，$Z\subseteq\mathcal B$、$D\subseteq Q$，真实剩余域为 $Y_F$。

定义 $\mathcal E_F$ 的顶点为 $P\sqcup\mathcal B_F\sqcup Q_F$，只保留两类弧：

* $p\to q$：$p\in P,q\in Q_F$，且 $Y_F$ 中有一条实际红六从 p 到 q。
* $q\to v$：$q\in Q_F,v\in A\cup\mathcal B_F$，且 $Y_F$ 中有一条实际蓝五从 v 到 q。

不放口池 $\mathcal B_F$ 发出的红弧，也不放指向非 clean 根 N 的蓝弧；其余红五与蓝五弧均不需要。每条红六删一个内点仍给同端红五，故

$$\boxed{\mathcal E_F\subseteq\mathcal D_F,
\qquad\mathcal E_F\text{ 是 DAG}.}\tag{45}$$

这是同一个实际 $Y_F$ 的图包含，不依赖另选一份与原时间不相容的顺序。特别 N 在 $\mathcal E_F$ 中无入弧，是源点池；$\mathcal B_F$ 无出弧，是汇点池，均允许孤点。

### 13.1 同一个理想同时给实际端截与短帽容量

任取 $\mathcal E_F$ 的前驱封闭理想 I。晚 P 到早 $Q_F$ 没有幸存红六，所以

$$C_F^{(6,5)}(I)=(P\cap I)\cup(Q_F\setminus I)\tag{46}$$

直接截住 $Y_F$ **全部真实红六**；这一步不再要求所有同端红五都不存在。另一方面，早 $A\cup\mathcal B_F$ 到晚 $Q_F$ 没有 $Y_F$ 蓝五，否则对应蓝反弧违反理想性。取 $A\cap I$ 与 $\mathcal B_F\cap I$ 的 ambient 头图最大独立集，§10.1的同一实际诱导域证明仍成立：红六由 clean／无头排除，蓝五的端点角色与 ambient 尾桥排除各非跨池型，唯一跨池型由这份新图理想排除。

令 $\eta_F^{(6,5)}(I)$ 为该早口池相对早 clean 根的头图未配数。于是

$$\boxed{\begin{aligned}
\tau_{R_6}(X)&\le j+z+d+|P\cap I|+|Q_F\setminus I|,\\
|P\cap I|+|Q_F\setminus I|
&\le25+|N\cap I|-\eta_F^{(6,5)}(I).
\end{aligned}}\tag{47}$$

这里省掉指向 N 的蓝弧不损失容量证明，因为其共同独立集域只使用 clean 根；省掉口池红弧不损失端截证明，因为幸存红六的源只在 P。两种删减都须如此逐一接回实际调用处，不能只凭“图更稀疏”就断言同一结论。

### 13.2 新图中的精确消元与固定批次释放

令 $\widehat\downarrow_FT$ 为 $\mathcal E_F$ 中含 $T\subseteq\mathcal B_F$ 的最小前驱理想，定义

$$\widehat g_F(T)=|T|-|(N\cup\Gamma_A(T))\cap\widehat\downarrow_FT|.$$

对同一新图应用有限 Hall 消元，有

$$\boxed{\max_{I\text{ 为 }\mathcal E_F\text{ 理想}}
\bigl[\eta_F^{(6,5)}(I)-|N\cap I|\bigr]
=\max_{T\subseteq\mathcal B_F}\widehat g_F(T).}\tag{48}$$

令 $\mathcal E_0$ 是 $Y_0$ 上按同一规则构造的基图。物理删点不会产生红六或蓝五，故 $\mathcal E_F$ 是 $\mathcal E_0$ 相应诱导删点图的子图。固定同一保留口批次 T，令

$$\widehat\rho_F(T)=|(N\cup\Gamma_A(T))\cap
(\widehat\downarrow_0T\setminus\widehat\downarrow_FT)|.$$

于是与旧图分别成立的精确关系为

$$\boxed{\widehat g_F(T)=\widehat g_0(T)+\widehat\rho_F(T),
\quad\tau_{R_6}(X)\le
25+j+z+d-\widehat g_0(T)-\widehat\rho_F(T).}\tag{49}$$

所以若 $\widehat g_0(T)+\widehat\rho_F(T)\ge j+z+d+1$，即输出实际24截；无24时则对每份合法支付及每批保留真口必须有

$$\boxed{\widehat g_0(T)+\widehat\rho_F(T)\le j+z+d.}\tag{50}$$

此处旧端图红六被物理删除销毁后，其残余同端红五**不再自动放入红弧**，故§12.3的全红五单付屏障不能直接搬到 $\mathcal E_F$。这正允许图的红端约束随真实匹配损失消失，但并未证明任何给定原输入必能释放所需根数。仍须在同一 $Y_F$ 上核全部幸存红六、全部相关蓝五及全部前驱路径，才能据式(49)认领收益；本文没有据新图的定义本身宣布24费已经普适成立。
