# E16 的完整 μ=0 层与 E16 并合

2026-11-15。**定理。** 设 $M$ 为 $Q_7$ 的任意 $56$ 边短匹配，$\delta_j$ 为第 $j$ 个坐标的位一面原偶孔数减原奇孔数，$\mu=\min_{0\le j\le6}|\delta_j|$。若 $\mu=0$，则存在包含 $M$ 每条原边的 $128$ 点全短 Hamilton 单圈。证明采用已审保边构造、大面代表的有限穷尽及一份经验真的 RUP 证书。 [原域与验收合同](MU0_FULL_DOMAIN_CONTRACT.md)

## 1. 假设反例并规范唯一平衡轴

每色恰有八孔。若有相邻孔，添该短边后由完整 E14 得到所需单圈。原孔独立时，至少两个平衡轴的输入由已审双平衡轴回代处理。于是反例只有一条平衡轴，把它送至外位 $6$，小面 $A$ 为位零侧，大面 $B$ 为位一侧。两面孔型分别为 $(a,a)$ 和 $(r,r)$，其中 $r=8-a$。平衡拼接处理 $a=3,4$。由于 $A$ 的两色非孔数相等且每条面内原短边覆盖一奇一偶，原跨边在 $A$ 的两色端口数相等，故原跨数为偶数。已审零跨及两跨的独立入口处理跨数为零与二。因此只需 $a\in\{0,1,2\}$ 且外轴至少有四条原跨边。 [唯一平衡轴归约及所用定理](MU0_UNIQUE_AXIS_REDUCTION.md) · [原域与归约独审](MU0_NORMALIZATION_REVIEW.md)

沿外轴给小面端口加配对，调用 $C_a$，再删配对并接回原跨边。所得覆盖 $A$ 的路径压到 $B$ 的异端口对，与 $B$ 的原内边构成接收匹配。其原孔恰为 $H\cap B$，规定压缩边可在完全图 $K(Q_6)$ 中。若大面某内切绝对孔差至多一，$C6^+$ 可接收。若内切差二且有一块至多少数一孔，参数化双桥可接收。逐路径展开都保留原边，只添短边。故反例允许逐个同步翻内位，将大面六个内轴的位一块都写成 $(p,p+g)$，$g\ge2$，且 $g=2$ 时 $2\le p\le r-4$。需要时全补六内位并交换色名，令 $\alpha$ 为物理奇、$\beta$ 为物理偶。翻位、全补和坐标置换均同时运输 $M$ 与两面的全部孔。 [参数化双桥](Q6_BALANCED_DELTA2_TRANSFER.md) · [真实匹配接收与展开](MU0_NORMALIZATION_REVIEW.md)

同一内轴上，小面的位一块写成 $(i,h)$，全局位一块按 $\alpha,\beta$ 为 $(x,y)=(p+i,p+g+h)$。有 $s=y-x=g+h-i\ge0$。唯一平衡轴排除 $s=0$。若 $s=1$，由 $g\ge2$、$i,h\le a$ 和上述差二界，所得 $(x,y)$ 仅可能为 $(2,3),(3,4),(4,5),(5,6)$。这些计数全落在无需全轴最小值前提的参数二、三中央差一门，故六个内轴均为 $s\ge2$。若 $s=2$，三个非中央差二整族只留下 $(3,5)$。若 $s=3$，单色三孔整族也可剥离。 [准确计数与各门量词](MU0_UNIQUE_AXIS_REDUCTION.md) · [中央差一扩展验收](../mu1_global_2026_11_15/q6_a8/ROOT_ACCEPTANCE.md)

## 2. 三个小面参数的同一大面代表表

在大面去掉外位，令 $L$ 是 $\alpha$ 的内位向量集，$V$ 是 $\beta$ 的内位向量集逐点六位全补。两组各 $r$ 点，$L$ 偶、$V$ 奇。大面孔独立等价于 $L,V$ 跨组禁距五。每个内轴的两组载荷为 $(n_L,n_V)=(p,r-p-g)$，合载至多 $r-2$。在极限列 $g=2$，$a=0$ 由全局差二门只准 $(3,3)$，$a=1$ 的局部界只准 $(2,3)$ 或 $(3,2)$，$a=2$ 的局部界只准 $(2,2)$。

对这些必要条件作重量归约，再求两组共同 $S_6$ 轨道。下表的模板均为偶组 $L$，奇组的三元计数范围见各模板证明。$a=1$ 的七边中包含一条含五元的奇组轨，$a=2$ 的四元项保留两轨。完整的 19、98、72 个轨道及其代表已独立重建。 [空小面基复核](MU0_A0_BASIS_REVIEW.md) · [两孔及四孔小面基复核](MU0_A12_BASIS_REVIEW.md)

| $a$ | 偶组模板及轨道数 | 合计 | 模板证明与冻结代表 |
| ---: | --- | ---: | --- |
| 0 | 零点加七边 $18$；八边 $1$；零点加六边和四元 $0$ | 19 | [模板](MU0_A0_WEIGHT_REDUCTION_REVIEW.md) · [代表](MU0_A0_BASIS_PREFLIGHT.json) · [基审计](MU0_A0_BASIS_REVIEW.md) |
| 1 | 零点加六边 $75$；七边 $23$；零点加五边和四元 $0$ | 98 | [模板](MU0_A1_WEIGHT_REDUCTION.md) · [代表](MU0_A1_BASIS_PREFLIGHT.json) |
| 2 | 零点加五边 $62$；六边 $8$；零点加四边和四元 $2$ | 72 | [模板](MU0_A2_WEIGHT_REDUCTION.md) · [代表](MU0_A2_BASIS_PREFLIGHT.json) |

每行代表的物理大面孔集是
\[
\{64\oplus x:x\in L\}\;\cup\;\{64\oplus63\oplus y:y\in V\}.
\]
第一组在 $B$ 的全局物理奇色，第二组在偶色。共同坐标置换 $\pi\in S_6$ 与六位全补交换，故可用同一次 $\pi$ 把两组送到其大面代表，把 $A$ 的实际孔和整个 $M$ 一并运输，且保持外位、两面标签、物理色和六个内差的负号。小面的孔位置由该次运输所定。另有独立的十九轨构造闭合 $a=0$，联合表保留这十九行。 [空小面构造独审](MU0_A0_FULL_CLOSURE_REVIEW.md)

## 3. 同一原反例给出联合公式的可行赋值

从经审的 `MU0_JOINT_NECESSARY.pb` 删除五条相邻内轴的全局有符号孔差排序。固定大面代表所需的置换可能改变该排序。其余源约束完全保留，加入一项允许表，顺序为物理孔变量 $h_{64},\ldots,h_{127}$，每行即 §2 的物理大面孔指示，共 $189$ 行。小面全部孔变量 $h_0,\ldots,h_{63}$ 仍在模型中，无固定孔锚点。原孔数关系逐色绑定 $B$ 的 $r$ 与 $A$ 的 $a$，故表中一行同时确定模型里的小面孔数参数。公式保留原来的 $29\,424$ 个变量，约束数从 $100\,055$ 到 $100\,051$。 [联合源构建](MU0_STRUCTURED_JOINT.py) · [行表与构建回执](MU0_STRUCTURED_JOINT.json) · [联合源差分及独立重建](MU0_STRUCTURED_SOURCE_REVIEW.md)

假设有 §1 的原反例，按 §2 共同运输到一行。给物理孔变量赋运输后实际的孔指示，给计数、阈值旗标和桥源旗标赋同一物理输入上的真实值。全孔独立来自原孔预处理，每个非孔的非孔短邻由其实际匹配边给出。大面、全局孔型及同一原输入的供接角色满足剩余源约束。如果某条被源约束剥去的入口在实际输入上成立，就有相应的保边全短圈，与原反例假设矛盾。此赋值还满足新增大面表。共同坐标置换保持短边，等价于将任何保边圈沿逆自同构拉回给原输入。 [源约束必要性及逐项绑定](MU0_NORMALIZATION_REVIEW.md)

| 冻结输入 | SHA-256 |
| --- | --- |
| `MU0_JOINT_NECESSARY.pb` | `c3922789fddf1ec764ea5a9260bd0cfc315b068e783c1fac6f7d989b8d2839f4` |
| `MU0_A0_BASIS_PREFLIGHT.json` | `db2f7a47c191a4d6b7c39584d08071f3b8f1bb2d60b87dd6252b0f6a29cb26ab` |
| `MU0_A1_BASIS_PREFLIGHT.json` | `052d703172b57b365016ad70a598b5ad9241d8171cfab54484b7553319307306` |
| `MU0_A2_BASIS_PREFLIGHT.json` | `5b8d596fd2f8f32ebb4162f5adb47bd2c8f7c8eac9ce1038d0d7d5705871e11b` |
| `MU0_STRUCTURED_JOINT.pb` | `6e37bc98707b75beb29f9d37aa0c8f9a2e72acfa2672dc8bd263763185734d30` |

## 4. 联合公式的不可满足证书

冻结的联合 PB 通过已审阈值编码编译为 $132\,945$ 个布尔变量、$1\,506\,761$ 条子句。任意源可行赋值可取每个整数变量的真实阈值及等值指示，按已审编码满足原线性条件、允许表及析取。新增大面表有 $189$ 个行选择字面量。每行的字面量蕴含对应 $64$ 个物理孔位的值，另有一条子句要求至少一行被选。任意源可行赋值选择其匹配行，即满足新增的 $189\cdot64+1=12\,097$ 条子句。独立复核从实际联合 PB 逐字节重建 DIMACS 和变量映射，并从 189 行逐条复核新增表的编码。 [阈值编码审计](../mu1_global_2026_11_15/certificates/audit_edge_cnf.md) · [本次 CNF 构建回执](certificates/mu0_structured_joint.build.json) · [独立 CNF 重建](MU0_STRUCTURED_CNF_REVIEW_check.json)

Glucose4 对冻结 CNF 求解约 $42.309$ 秒并生成 $21\,116\,326$ 字节的证明。官方 DRAT-trim 对同一份原始 CNF 和全证明核验约 $28.062$ 秒（外层墙钟），退出码为零，日志含 `s VERIFIED` 且证明核心的 RAT 引理数为零。核验回执为 `VERIFIED_RUP_UNSAT`。独立绑定重新核对源 PB、CNF、证明、工具、官方日志和回执的摘要。 [求解回执](certificates/mu0_structured_joint.solve.json) · [官方验真回执](certificates/mu0_structured_joint.verify.json) · [官方日志](certificates/mu0_structured_joint.verify.log) · [终端独立绑定](MU0_STRUCTURED_PROOF_REVIEW_check.json)

| 实际终端与复核文件 | SHA-256 |
| --- | --- |
| `certificates/mu0_structured_joint.cnf` | `9371c1c91efeb0555b1a568e884611e61bcf183348eb66bc2316208685e47b68` |
| `certificates/mu0_structured_joint.map.json` | `96133bb3dac978772789e5ca7eff078cf3f941dbe96737f688d3a349e936caf4` |
| `certificates/mu0_structured_joint.build.json` | `02ad37f9af26221f1f98ea5d6f89250f62ba3ac0ce745f651163dcb3021d38d8` |
| `certificates/mu0_structured_joint.solve.json` | `ef6bba70d2723d6624a1cde304515b5c80d5c14921c4defa31689bd70e789d26` |
| `certificates/mu0_structured_joint.drup` | `a16947d033fea515d476d79b031e6b2508cf275fd05e5026c03079c86bc7dabf` |
| `certificates/mu0_structured_joint.verify.json` | `bddad665bb30edda4f0814ecfa27f9482bb8a162640875adaeac5595b6a0c929` |
| `certificates/mu0_structured_joint.verify.log` | `1cecd01b276829c15ae87828ecfe56121e6811a9e108683c5852debc9a8b5dd2` |
| `MU0_A12_BASIS_REVIEW.md` | `260804d738495fb58e9a6d5e95a9b7546f55aa40af6a377d7e9e25909709093f` |
| `MU0_STRUCTURED_SOURCE_REVIEW.md` | `41f887dd8150f017bd0fe8c2bdc990df1c66e663a23ff1112ebe0ce1b8a204fe` |
| `MU0_STRUCTURED_SOURCE_REVIEW_check.json` | `2250075068f1a28269e9a460a5413023ef9e050fceaa8209aeb5c90c469dfc39` |
| `MU0_STRUCTURED_CNF_REVIEW_check.json` | `60430c8f9155ee0d12fb2da287225977b5f2f0750d2a1db1ad7375cbbaaa7712` |
| `MU0_STRUCTURED_PROOF_REVIEW_check.json` | `416b94fa74d47493911bd85a967498edf12b4e0907ce22e924ac945a1de53b84` |

冻结 CNF 不可满足，故联合 PB 也不可满足。由 §3，任何余下的实际反例都会给联合 PB 一份可行赋值，矛盾。再合 §1 的直接构造，得到全部 $56$ 边短匹配的 $\mu=0$ 层。计算部分只穷尽局部来源组的大面轨道，并编译与检验联合公式。原匹配由任意实际输入固定，直接构造和逆自同构都保留其全部边。$\square$

## 5. 完整 E16

**推论。** $Q_7$ 的任意至少 $56$ 边短匹配延拓到一条保留全部原边的全短 Hamilton 单圈。

已审完整 E14 处理至少 $57$ 边。设 $|M|=56$。若有相邻原孔，补一条短边成 $57$ 边，调用同一定理。因此只需处理独立原孔。按旧孔差上界的规范，逐位翻转使原两色来源组 $U,W$ 满足 $n_U(j)-n_W(j)=|\delta_j|$，再取七位来源组 $L'=W,V'=\overline U$。两组各八点且同奇偶，第 $j$ 列合载为 $8-|\delta_j|$。同偶时每组总重至少 $14$。同奇时若某组含全体七个单位向量，则相应的中心（对 $L'$ 是零点，对 $V'$ 是全补中心）因原孔独立而非孔，七个短邻却全是孔，与实际原匹配覆盖该点矛盾。因此每个奇组至多六个单位向量，至少两点重三或以上，总重至少 $12$。若 $\mu\ge5$，七列合载至多 $21$，与两种下界 $28$、$24$ 均矛盾。 [E14 总审](../R7_MU1_CENTRAL_T1_AND_E14_REVIEW.md) · [孔差上界 §4](../R7_E16_INITIAL_REDUCTION.md) · [独审 C01–C04](../R7_E16_INITIAL_REDUCTION_REVIEW.md)

所以 $\mu\in\{0,1,2,3,4\}$。定理处理零，其余四值分别调用已审完整层。这些层都量化实际的任意 $56$ 边短匹配，输出保有全部原边的一条全短单圈。结合完整 E14，即得所述阈值。$\square$ [完整 $\mu=1$](../mu1_global_2026_11_15/ROOT_ACCEPTANCE.md) · [完整 $\mu=2$](../R7_E16_MU2_FULL_REVIEW.md) · [完整 $\mu=3$](../mu3_hard_first_2026_11_15/ROOT_ACCEPTANCE.md) · [完整 $\mu=4$](../R7_E16_MU4_FULL_CLOSURE_REVIEW.md)

