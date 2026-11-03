# Uniform triangle C33/C11：固定生成族纸面接口

状态：**生成族、逆端口、对称归一化及局部 fibre 覆盖接口支持。** 尚未证明任一参数的全部 controller/fibre pairs 在三步覆盖。本文没有生成 controller、枚举 words/参数、运行 field/图/BFS/solver/Lean 或外审。

## 1. 字面 controller 规则及简单性

顶点为 `(τ,j)`, `τ∈{0,1,2}`, `j∈C11`。四端口为 `0=A, 1=A⁻¹, 2=B, 3=B⁻¹`，其中

`A(0,j)=(1,j)`，`A(1,j)=(2,j)`，`A(2,j)=(0,j+p)`；

`B(0,j)=(2,j)`，`B(1,j)=(0,j+q)`，`B(2,j)=(1,j+r)`。

两者都是置换。字面 inverse 为

`A⁻¹(0,j)=(2,j−p)`，`A⁻¹(1,j)=(0,j)`，`A⁻¹(2,j)=(1,j)`；

`B⁻¹(0,j)=(1,j−q)`，`B⁻¹(1,j)=(2,j−r)`，`B⁻¹(2,j)=(0,j)`。

因此 reverse 标签固定为 `bar(0)=1, bar(1)=0, bar(2)=3, bar(3)=2`。

所有端口均改变 type，故无 loop。各顶点到某一个其它 type 的两个邻点，只会分别因 `p=0`、`q=0` 或 `r=0` 而重合；跨不同 type 不会重合。因此 `p,q,r≠0` 恰保证四邻不同。controller 此时有 33 点、每点 4 邻，是简单四正则图。

每个 j 的三个点有字面三角

`(0,j) —A→ (1,j) —A→ (2,j) —B⁻¹→ (0,j)`。

非零 p 还给 `A³(τ,j)=(τ,j+p)`，故仅 A/A⁻¹ 边就能连接所有 33 点。此处 A 的遍历性质只说明连通，**不说明 A 是全 controller 的 graph automorphism**。

## 2. 三类根及 100 个规范参数的完整性

对任意 `c∈C11`，`T_c(τ,j)=(τ,j+c)` 与 A、B 及它们的 inverse 交换，并保留所有 port labels。若 fibre charts 是本任务指定的全局端口矩阵/offset，不依赖 j，则 `T_c` 保持 fibre 坐标不变也提升为实际 fibre 图 automorphism。

所以需要的 controller 源根恰可取 `(0,0),(1,0),(2,0)` 三类代表；这里不把三种 type 合并为一类。对于未由满 noise rank 直接解决的目标，仍要对八个源 fibre 点分别作 image union。

对非零 unit λ，`S_λ(τ,j)=(τ,λj)` 给参数族间的保 port-label 同构

`(p,q,r) ↦ (λp,λq,λr)`。

取 `λ=p⁻¹`，所有非零三参数都归到 `(1,q/p,r/p)`。因此固定 p=1、`q,r∈{1,…,10}` 的 100 个参数覆盖原族全部同构类；不要求这 100 个参数彼此非同构。该归一化没有更换 fibre chart，也没有使用额外 type 置换。

## 3. 固定 ARC chart 的 inverse 与同层覆盖

按输出噪声约定

`step_d(x,t)=L_d x+t v_d`，`x∈F2³`, `t∈F2`。

给定 `L_0=L_1=A_f`，其列为 `[2,1,4]`；`L_2=L_3=B_f`，其列为 `[1,2,7]`；整数码按 e1,e2,e3 的二元坐标解释。实际 offsets 为 `[v_0,v_1,v_2,v_3]=[1,2,4,7]`。

也就是 `A_f` 交换 e1/e2 并固定 e3；`B_f` 固定 e1/e2，将 e3 送到 `e1+e2+e3`。两者各自平方为 I，且

`A_f v_0=v_1`、`A_f v_1=v_0`，`B_f v_2=v_3`、`B_f v_3=v_2`。

故每条端口关系与对应 reverse 关系真正互逆。controller 四邻不同，offsets 非零，所以若实际 fibre 图严格按此契约构造，每点会有四端口各两点、共八个不同邻点，且没有 self-loop；这一度数账不代替全 D3 检查。

三角的三个起点分别给闭 controller words `003`、`030`、`300`。对 word `(d1,d2,d3)`，noise columns 为

`L_d3 L_d2 v_d1, L_d3 v_d2, v_d3`。

将上面的字面线性作用代入，三词的列分别是

- `003`：`e2, e1, e1+e2+e3`；
- `030`：`e2, e1+e2+e3, e1`；
- `300`：`e1+e2+e3, e2, e1`。

三组均是基。因此对每个源 fibre 点 x，相应闭三词的 affine image 是全 F2³，三个 type 的同 controller 层均已全八点覆盖。这是列式符号推导，不是新增 word/field 枚举；也不沿用 R chart 上退化的 `030`。

输出 directions `{e1,e2,e3,e1+e2+e3}` 是同 chart 的 Fano 4-arc，完整 inverse 已在上式说明，因此相邻 controller 层另由 [binary pencil 引理](../ADJACENT_BINARY_PENCIL_PAPER.md) 全八点覆盖，无须某一条相邻三词独自 rank 3。

## 4. 尚需实际判断的范围

同层和相邻层的局部满覆盖不保证非相邻 controller 层。其余目标仍须按实际 typed 路径，对每个源 fibre 点 OR 所有长度至多 3 的真实 image；可使用 [packet 剪枝](../CONTROLLER32_PACKET_PRUNING_PAPER.md) 的同一逻辑，但不能用 goodword 数、仅 x=0 或各 image 大小替代 union。

若这个固定 p=1、100 个 `(q,r)`、固定 ARC charts 的整个族为 NO，只关闭该族，不推到其它 m、其它拓扑、R/混合 charts、非 permutation port 接口或一般 8D3。264 只是此接口的点数，本文没有声称已构造 264/D3 图，也没有新增图、参数或 Lean 计数。
