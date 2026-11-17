# 恢复入口：唯一交叠与双满纯角色已闭，转向未满多交叠

日期：2026-11-06。

本轮两个完整整类证明为[唯一交叠 PROOF](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/PROOF.md>) 与[双满纯角色 SATURATED_PURE_ROLES](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/SATURATED_PURE_ROLES.md>)。数学由主会话及同会话数学协作者推导核回；native Sol/high 仅忠实文档执行。状态为 **same-session、未外审、未接受**，不是独立审查。全局 757／766／767／777 工作界仍为 **40／49／75／76**。

## 1. 已完成的准确范围

对任意完整 767 母体，即禁 $B_6,R_7,\mathrm{weak7}$，设 $b$ 是 756 及换色 756 的共同有效整数容量，实际 balanced 容量 $C\le2b-1$。本轮证明

$$
\operatorname{Src}_{R_6}(X)\cap\operatorname{End}_{R_6}(X)=\{z\}
\quad\Longrightarrow\quad |X|\le3b-1.
$$

代 $b=25$，整个唯一交叠类至多 74 点。无需 $z$ 为极端点、无外跨假设、$D$ 排序、$D+z$ 安全，也不先依赖 $D$ 无红五或 $w=0$。

因此此前所有 75 点 $I=\{z\}$ 分支已经关闭：外跨路径、规范红闭包不逃逸、共享早末三路径、共享 $D$ 的安全点逆序选择、$D+z$ 安全与全区间桥同步，均不再是排除 75 点唯一交叠所必需的未闭义务。旧局部结果仍可作为工具保留，不能将旧报告当时的未闭状态改写为当时已闭。

双满纯角色定理另证明：$n=3b,|P|=|Q|=b,|I|\ge2$ 的整个类不存在。它先由同一完整 M0 系统与短帽满容量压出 $Z_\pm=\varnothing$、单例纤维、$\widehat E=\widehat F=I$；$i\ge3$ 用相邻 cuts 的实际 owner 集合组成 $b+1$ 点红短帽矛盾，$i=2$ 用一般纯源跨越引理和完整根扇导出以 $Q$ 点为源的实际红六矛盾。全程不调用匹配最优化，不把其他 owner 的私有红五偷写成纯 $D^3$。

旧 $I=\varnothing$ 整类已由[balanced 严格界 §5.1](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>) 排除 75 点。结合上述两个整类证明，任意当前 75 点残余必有

$$
|I|\ge2,\qquad |P|\le24\ \text{或}\ |Q|\le24.
$$

这不排除多交叠类，不能宣布全局 74／75。

## 2. 承重进口与完整调用链

参数无关 M0 的原件是[证明义务审计 §2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md>)。它给同一母体中的实际双向核、全部路径锁、每锁供应及强普通点性质，不先要求 $w=0$ 或特定人口层。

严格 balanced 容量的原件是[双色实际路径交替环与766严格界](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>)，其保证层级保持。

新证明的实际链条为：唯一交叠给 $n\le3b$；反设取等迫 $|P|=|Q|=b,|D|=b-1$；M0 补集计数与 strict 容量迫每侧缺额 1、owner／锁至多一；两满短帽直接消去 $D$ 的核内红五端点；内部 $S/T$ 红六及强普通点性质给 $z$ 两侧全 ambient 红扇；末／首对屏障迫两侧 owner、锁实际存在且 $a<\omega<z<\psi<b_0$；同一中间域 $D+a+b_0$ 迫实际 $R_5(a,D^3,b_0)$；真实 owner 供应兑现红六末对 $(a,\omega)$、首对 $(\psi,b_0)$，两帽给同端蓝四，违 weak7。

关键点不是锁标签的排列：正文先兑现实际 owner 锁对，再使用帽；中间红五的两个端点也由全部核内端点排除得到。

## 3. 下一主攻顺序

1. **抽象三满域的共同不相容或真实净增广。** [THREE_SATURATED_DOMAINS](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/THREE_SATURATED_DOMAINS.md>) 已将整个严格分离余类及 regular $e_L=1/e_R=1$ 整域归约为真正不交 $X=A\sqcup K\sqcup B$，三域各 $b$，外域实际756，$K\subseteq D$ 无红五，$A$ 无 ambient 蓝五末点、$B$ 无 ambient 蓝五首点。直接复用抽象 Bad± 非空与一般四端口，重点控制同一对纯末／纯源下的实际共同删集；不能独立挑路径或分别取最小值后拼合。原 M0 owners 可以非空。三满域共同实现尚未排除。

2. **Regular dD=1 纯增强的近三满域同步。** 使用共享同一 K 的两满红短帽 $K+j,K+k$、跨 z 的真实桥、全量跨根蓝五和新 K 内端口，取得一次实际净增广、同端蓝四或 D 端点红六。在这一指定余类内双方纯角色都至多23；该数值不能外推到全部75点输入，也不能把蓝五端点 a/b0 自动换成 j/k。

3. **严格交错欠额的共同末端实现。** 一侧饱和下，内部根与不同 ordinary 点已经精确一换一；纯计数继续沿同一公式推进会抵消。保留一般 b,e 必要不等式，处理最高旧双根与 ordinary 的实际共同实现，不能把它写成新数值界，也不能未经证明少付一单位。

合法换根仍为独立备选，不冒称覆盖当前全部余类。唯一交叠与双满纯角色已经整类关闭，不重开旧数值 caller。

## 4. 已冻结接口与范围备查

实际全域残余为**75 点、$|I|\ge2$ 且至少一侧纯角色未满的输入**。在这一真实残余内重新兑现 M0、完整路径与共同增广接口。一侧 $|P|=b$ 或 $|Q|=b$ 的整个类仍未排除，不能从双满定理外推所有一侧满的输入。

[MULTI_ROOT_FRONTIER §§1–8](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/MULTI_ROOT_FRONTIER.md>) 已给指定严格交错、一侧 $|P|=b,|Q|=b-e$ 的一般必要定理：两侧单例纤维，$\widehat E=I\setminus\Omega$，$y_f=z_h\in\widehat E\cap\widehat F$，$\Omega\cap I>y_f$；每个内部根消耗不同实际 ordinary 点，$h-2+r_1\le\kappa_+=e-\delta-c_+$，且 $i\le2e+2-\delta-c_+$。最后根再耗一单位尚未证，不得写 $h\le\kappa_++1$ 或一侧饱和全排；不代数值拆 case。下一义务是这些实际端口、ordinary 点与最高旧双根的共同末端实现。

不能把唯一交叠下的 $\alpha+u+\delta=1$、唯一 owner 或共用单点红扇外推到多交叠；也不能在纯角色未满时继续假设 $Z_\pm=\varnothing$、全部旧根等于 $I$ 或满核普通增广为空。后继若使用本轮的实际路径引理，须重新证明原输入满足其条件。

另有已冻结的一般工具[FOUR_PORT_AUGMENTATION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/FOUR_PORT_AUGMENTATION.md>)：$r\ge5$，纯末 $q$ 在纯源 $p$ 之前，中性 $C\subseteq(q,p)$ 的两单点域 $C+q,C+p$ 无 $R_r$，则任意实际入 $q$／出 $p$ 的四个相邻端口同时加入仍无 $R_r$，从红短帽容量 $\beta$ 得 $|C|\le\beta-4$。每个中性点若有 ambient 双向蓝 $r$ 供应，安全条件自动成立；全部新增组合已逐类覆盖。

其原多交叠 caller 为 $|P|=|Q|=25$ 且 $\min Q<\max P$ 的75点条件例证，给区间外 $D$ 点至少 $4-i$；该整个双满输入现已由更强定理关闭，不再作为当前残余方向。一般四端口定理保留，但在纯角色未满的输入上须另证双向蓝供应或安全条件，不能自动调用原 caller。

四端口稿 §6 的 Bad± 定理已经提炼为上述抽象 $A/K/B$ 条件，证明仅用 $A_0=A\setminus T,B_0=B\setminus S$；旧 clean 严格交错只是特殊 caller，不是必要前提。全部单点红六失败集 $\mathrm{Bad}_\pm$ 各自非空，但未证明共享一点。对同一对纯末／纯源 $q<p$，实际并集 $E=(\mathrm{Bad}_-\cup\mathrm{Bad}_+)\cup(K\setminus(q,p))$ 满足 $|E|\ge4$；若要全排，仍须找到同一对 $q,p$ 使 $|E|\le3$，尚未证明。不把两侧单点失败或各自最小删集自动合为共同增广。

新[SEPARATED_ROOTS](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/SEPARATED_ROOTS.md>) 对 $n=3b,w=0$、增强根严格分离 $x_e>y_f$ 做完整实际覆盖取等。结论为 $|D|\ge b$、纯 $D$ 的 $b$ 点红短帽、两个 $b$ 点蓝短帽，以及 $\Omega>x_e,\Psi<y_f$。两个蓝短帽交集恰为 $A_H\sqcup B_H$，实际覆盖只到 $X\setminus(\Omega\cup\Psi)$；不能漏掉 owner 重叠或缺席锁而当成三核不交分划。

因此 $b=25$ 时，严格分离的 $|D|\le24$ 整类已排除。其原双满纯角色推论现也由双满整类定理覆盖；$|D|\ge25$ 的严格分离余类现经全替锁进一步达到 §3 的真正三满域统一接口，仍未全排。

新[REGULAR_COMMON_ROOT](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/REGULAR_COMMON_ROOT.md>) 保持旧 $\Gamma$ 与增强根定义，限于 $n=3b,w=0$、regular 共根 $\min E^+=\max F^+=z\notin\Omega\cup\Psi$、$\Omega\cap I>z,\Psi\cap I<z$，并聚焦 $e_L=e_R=0,d_D=1$。旧加权定理先给 $u=v=0,H=\varnothing$；本轮排除 $\widetilde C\setminus C_D$ 有额外点的整个类，再排除有任一旧根 $z\in\widehat E\cup\widehat F$ 的整个类。

该 regular 分支的精确未闭口为 $\widetilde C=C_D$、$z\notin\widehat E\cup\widehat F$：指定替锁域加 $z$ 中的入／出红六都用实际末对 $(j,z)$、首对 $(z,k)$，端口仅在这两个指定域内唯一；有 $R_5(j,K^3,k)$，$K$ 为 $b-1$ 点红短帽，而已得同端蓝三只使长度和为 8。$K+j,K+k$ 各为 $b$ 点红短帽，删端口后的两蓝短帽补域由严格 balanced 容量迫两侧 $I_{<z},I_{>z}$ 非空。因此余类必 $|I|\ge3,|D|\ge b+1$，数值为 $|D|\ge26$。

纯增强定义还给真实末对 $(q_0,z)$、$q_0\in Q$ 与首对 $(z,p_0)$、$p_0\in P$，所以 $q_0<z<p_0$。这里用 regular 的 $\Omega\cap I>z,\Psi\cap I<z$ 排除相邻点仍在 $I$，否则会重新成为旧 hat 根。这仅是额外实际入口，尚无新的排除。

同一前沿稿 §§9–15 在**另一个作用域**补强该纯增强余类：$C_-$ 中所有 ambient 末对 $(h,r\le z)$ 只能为 $(j,z)$，$C_+$ 对偶，不能扩成全部 ambient 端口唯一；两个 $2b$ 点补域给实际 $u<r<z<s<v$，$u\in K\setminus V,v\in K\setminus U$，只有 ambient 入／出红五，不能冒充 $D$ 内 V/U 身份。纯 Q/P 端口对任意入 $q_0$、出 $p_0$ 路径给全量 $B_5(a,q_0,z,p_0,b_0)$；至少一侧满足所有端口都在 K，且至少有一份 $B_5(F_-^4,q_0)$ 或 $B_5(p_0,F_+^4)$，不能默认两侧同时成立。

该 regular 余类若 $|D|=b+q_{\rm def}$、$q_{\rm def}\ge1$，则实际 balanced 补域给 $|P|,|Q|\le b-q_{\rm def}-1$，数值两侧都≤23；并有 $i\ge q_{\rm def}+2$。这仅限该余类，不能写成全部75点残余的结论。最小未闭义务是同步两个 K 内新端口、全量蓝五与共享 K 的两满红短帽，取得实际 b+1 红短帽、同端蓝四(j,k)或 D 端点红六；不能把 a/b0 自动替换成 j/k，也不能采用已撤回的跨三元组红色推断。

这没有关闭纯增强共根 D 桥。旧 $e_L=1,e_R=1$ 分支已由三满域稿整体归约，并有最小旧首／末端口约束；regular 左余量的实际跨域红六末前驱只可能在 $A_H\sqcup C_-$，相应私有红五还迫一个高根位于 $(z,t_*]$。这些共同实现尚未排除，非 regular 共根及其他未覆盖多交叠范围也仍留开。

目标仍是从任意剩余 75 点输入构造完整实际混合分划／净收益，或推出矛盾。多交叠全类尚未闭合，尚无新的无条件人口下降。

本目录仅采用已冻结的多交叠归约；尚在主会话推导而未冻结的其他候选不作为结论或允许进口。

合法换根仍为独立备选；[上轮 ROOT_AND_M0_INTERFACES](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-crossing-and-joint-roots-20261106/ROOT_AND_M0_INTERFACES.md>) 保留三合法根条件覆盖等历史接口。没有因本轮唯一交叠排除而自动完成该共同覆盖，也不能假定任意内部 pivot 合法。

## 5. 执行边界

本轮只在本新目录写文档，不修改上轮文件、旧证据、任务状态、接受记录、封存产物或在跑作业。没有外审、科研代码、solver、证书重放或新的 Goal，也没有自行设置预算。

用户当前禁止外部审查、末对图优化与局部数值搜索。后继不为已闭合的 75 点唯一交叠或双满纯角色重开这些工作，不继续旧局部小例。项目科学运行目标仍为 Linux，历史 raw UNSAT 的保证不因本轮解析证明改变。
