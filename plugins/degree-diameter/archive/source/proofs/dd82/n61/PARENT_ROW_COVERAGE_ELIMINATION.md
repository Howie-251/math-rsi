# 无三角双缺陷根的统一父行与闭邻覆盖消元

2026-10-19。**Local paper，未计算、枚举或新增外审。** 本稿同时保留h5/h6的共同、不同R端口及Wi交叠，不按父色或交格大小分类。统一容量与零行传播现已用于完整排除h6特殊父点QP相邻的范围，见第4节；没有排除全部h5/h6。

## 1. 原图范围与矩阵

在同一61点八正则直径二图中，取非邻双缺陷根u、v；两根无三角，所选双缺陷在各端孤立，其他双缺陷不假定孤立。沿用S、U、V、R及真实Δ。原边至多一个共同邻点迫S独立；根无三角使U、V独立且S不接U/V。记

\[
E=A[U,V],\quad L=A[U,R],\quad M=A[V,R],\quad
T=A[S,R],\quad H=A[R],\quad D=\Delta[S,R].
\]

T的三行各有六个1，允许交叠。设

\[
\alpha=\Delta[u,R],\quad\beta=\Delta[v,R],\quad
\alpha_V=E^T\mathbf1-\mathbf1,\quad
\beta_U=E\mathbf1-\mathbf1,\quad k=T^T\mathbf1,
\quad\lambda=\alpha+\beta-k,\quad\tau=D^T\mathbf1.
\]

α、β、α_V、β_U均为0/1。层度式给

\[
L^T\mathbf1=\mathbf1+\alpha-k,\quad
M^T\mathbf1=\mathbf1+\beta-k,\quad
L\mathbf1=7\mathbf1-E\mathbf1.
\]

令B=Δ[U,R]，B′=Δ[V,R]。以下两式没有把每个父点的缺陷另行选择：

\[
\boxed{B=L(H+I)+EM-J,\qquad (H+I)T^T=J+D^T.} \tag{1}
\]

它们直接数同一原图的一、两步路线。

## 2. 一次消去全部S父点贡献

U到各层的真实缺陷分别满足

\[
\begin{aligned}
\Delta[U,V]\mathbf1&=2\mathbf1+L\beta-Lk,\\
\Delta[U,S]\mathbf1&=Lk,\\
\Delta[U,U]\mathbf1&=E\alpha_V+L\alpha-Lk,\\
\Delta[U,v]&=\beta_U.
\end{aligned}
\]

相加并用总行和4，得到统一父行容量

\[
\boxed{B\mathbf1=2\mathbf1-\beta_U-E\alpha_V-L\lambda.} \tag{2}
\]

V侧只需交换L/M、α/β及E/Eᵀ。式(2)保留所有真实父点项；共同W端口与两个不同W端口的贡献确实不同。

虽然λ在普通W点取−1，矩阵L diag(λ)、M diag(λ)逐项仍非负：该点没有U/V邻点。实际收费只有：单侧C端口每条父边收费1，共同C端口收费2，仅属一个Wi的共同W端口收费1；单侧W端口及属两个Wi的共同端口收费0。因此(2)是一条真实非负容量限制，不能用负λ虚增预算。

将(1)右乘Tᵀ，消去同一H，得到

\[
\boxed{BT^T=LD^T+EMT^T-\beta_U\mathbf1^T.} \tag{3}
\]

逐点即Δ(x,Wi)=δ_i(N_R(x))+Σ_{y∈N_V(x)}|Wi∩N_R(y)|−β_U(x)。最后一项前的实际父边交数不能省略；它正是先前多处过强覆盖推断的风险所在。

## 3. 交叠修正与可直接使用的零行推论

令C为不属于任何Wi的R点集，O为属于两个Wi的点集。因α、β≤1，k≤2，所以
\[
\mathbf1_C=\mathbf1-k+\mathbf1_O.
\]

把(2)与(3)的三列和结合，得到

\[
\boxed{
L\tau+B\mathbf1_C+E\alpha_V+L\lambda+EMk
=2\mathbf1+2\beta_U+B\mathbf1_O.} \tag{4}
\]

式(4)两边所列各项均非负。Wi不交时O为空，右侧只余2+2β_U；有交叠时必须保留B1_O，不能把不交分支的上界直接扩大。

一个统一的真实零行结论是：若某x∈U满足
\[
\beta_U(x)+(E\alpha_V)_x+(L\lambda)_x=2,
\]
则由(2)及非负性，B的x行全部为零。再由(3)，其每组覆盖都满足
\[
\delta_i(N_R(x))+\sum_{y\in N_V(x)}|Wi\cap N_R(y)|=\beta_U(x).
\]
特别地若β_U(x)=0，则x的全部R邻点没有任何S重复，而且x的每个V邻点都不接Wi中的点。该结论同时处理不同端口、共同端口和交叠；无需另按配色证明。共同单W端口稿中x、y的R零行正是它的一个实例。

## 4. 实际应用与继续传播的止点

[特殊父边排除](H6_SPECIAL_PARENT_EDGE_EXCLUSION.md)现在给出一个完整、位置无关的应用：h6的两个UV度2父点Q、P不能相邻。反设QP为边，式(2)使Q的R缺陷行全零；式(3)的三个覆盖同时迫Q的R邻集中至少两份S重复。真实父边排除这些邻点接P，而根传播使每份重复都成为Q与残余端口a的共同邻点，与Q的零行矛盾。证明允许共同/不同端口、C/W及Wi交叠，不使用已完成的端口位置排除。故UV=P4⊔3K2整个骨架关闭，只余2P3⊔2K2；不是再次细分端口。

后续零行传播不能无条件迭代。若x∈U满足Δ(x,R)=0，普通C点c的两个实际父点为φ(c)、ψ(c)，交换式给

$$\sum_{r\in N_R(x)}\Delta(r,c)+\sum_{y\in N_V(x)}\Delta(y,c)
=\Delta(x,\phi(c))+\Delta(x,\psi(c)).$$

仅当右侧两个真实父缺陷均为零时，才能逐项把零传播到孩子。QP已排除后的不同双W端口范围，各父点R预算为1或2，没有新的零行可直接启动；共同单W端口虽有零行，右侧父缺陷却未被证明全零。没有因此得到另一完整排除。

这里已把父点容量、三份闭邻覆盖及交叠修正放在同一套原图等式中，并产生上述真正的完整排除；等式本身仍不是充分生成规则。

当前尚未由(2)–(4)统一排除剩余h5/h6。例如允许的h5不交、互异W端口位置使α_V=β_U=0、Lλ=Mλ=0，父行总量仍为2，容量本身不矛盾；这只说明该消元没有立即闭合，不声称相应实际图存在。难点仍是这些非负缺陷和父点覆盖能否来自同一组无向R内部边。到此停止增加弱式，不按颜色或交格细分，也不据此启动计算。
