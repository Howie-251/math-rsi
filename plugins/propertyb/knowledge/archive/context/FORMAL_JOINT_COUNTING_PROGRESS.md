# Lean 联合计数及真实条件排列样本空间

## Claim

设有限顶点类型有 $N$ 个元素，$A,B$ 是不交的指定点集，$L,R$ 是不交的允许位置集。令 $r=|A|$、$q=|B|$、$a=|L|$、$b=|R|$。本模块证明

$$
\#\{\sigma:\sigma(A)\subseteq L,\ \sigma(B)\subseteq R\}
=\binom ar\binom bq r!q!(N-r-q)!.
$$

在全部排列上归一化，得到

$$
\Pr[\sigma(A)\subseteq L,\ \sigma(B)\subseteq R]
=\frac{\binom ar\binom bq}{\binom Nr\binom{N-r}q}.
$$

模块进一步将这两个公式接到**真实锁定条件下的原排列子样本空间**。给定有限标签集 $I$，以及两条单射 $u,t:I\hookrightarrow V$，定义

$$
\Omega=\{\sigma\in\operatorname{Perm}(V):\forall i\in I,\ \sigma(u(i))=t(i)\}.
$$

令 $F=V\setminus u(I)$、$P=V\setminus t(I)$，自由点数 $N=|V|-|I|$。模块构造并核查

$$
\Omega\simeq\{\tau:F\simeq P\},
$$

且该双射把原排列映到其实际限制：每个自由点 $x$ 的像仍然是 $\sigma(x)$。对于 $A,B\subseteq F$ 和 $L,R\subseteq P$，上述联合计数和归一化公式在 $\Omega$ 内直接成立。没有将自由顶点和自由位置默认为同一个子集，也没有假定两组事件独立。

## Status

**PROVABLE AS STATED；上述一般联合计数、条件样本双射和条件概率比已完成 Lean 内核核查。**

源文件：[JointCounting.lean](../formal/Aris4Math/JointCounting.lean)。2026-10-06 最终执行 `lake build Aris4Math.JointCounting` 成功，新模块编译耗时 5.1 秒。十一项主要导出声明的 `#print axioms` 均只有 `propext`、`Classical.choice`、`Quot.sound`。日志：[lean-joint-counting-build.log](../.aris/traces/proof-checker/2026-10-06_run05/lean-joint-counting-build.log)。

这完成了 P3/P4 所需的一般联合位置计数核心及真实条件样本空间桥。**具体超图 critical-pair 事件的识别、自由中心因子 $1/N$、结构分支及主目标 T 的完整 Lean 闭合不在本模块中。** 用户要求的最终完成标准仍是原始主命题的完整 Lean 证明。

## Assumptions

- 顶点和位置类型有限，带可判等关系。
- 两组指定点不交；两组允许位置也不交。源不交性用于将标签合并成单射，目标不交性用于目标标签的单射与纤维分割。
- 两种类型不同的一般版本接受一条明确的参考双射。锁定版本在内部构造该参考双射，不要求调用者额外假定其存在。
- 允许空点集、空允许位置集、所有点已锁定、允许位置容量不足。容量不足通过二项式零值体现，不使用未经定义的负阶乘或 $0/0$。
- 并未对允许位置要求覆盖整个自由位置集合；因此可以留出中心或其他禁止位置。

## Proof Strategy and Dependency Map

1. `disjointEmbedding` 将两个不交源集合用和类型 $A\sqcup B$ 标号，得到真实单射。
2. 固定两个精确目标子集 $T,U$，其大小分别为 $r,q$。每个满足 $\sigma(A)=T$、$\sigma(B)=U$ 的排列，在两个源集合上唯一诱导两条双射 $f:A\simeq T$、$g:B\simeq U$。`jointImageEquiv` 将事件显式双射到这两条双射及其点锁定纤维。
3. 每一纤维用此前已核查的 `Counting.card_prescribed_images` 计数，为 $(N-r-q)!$。两条双射分别有 $r!$、$q!$ 个，得到 `card_joint_image_eq`。
4. `jointImageSubsetEquiv` 按实际占据的两个位置子集分解允许位置事件。由 $L\cap R=\varnothing$，所有所选 $T\subseteq L$、$U\subseteq R$ 自动不交。目标子集数分别为 $\binom ar$、$\binom bq$，因此得到 `card_joint_image_subset`。
5. 利用一般阶乘恒等式

$$
N!=\binom Nr\binom{N-r}q\,r!q!(N-r-q)!
$$

并在有理数中消去非零阶乘乘积，得到 `joint_image_subset_ratio`。源不交性保证 $r+q\le N$；没有将这个不等式当作遗漏的外部前提。
6. `jointBijectionEquiv` 用一条明确的参考双射搬运位置坐标，证明同一公式适用于不同的有限顶点、位置类型。搬运保留两个目标集合的大小和不交性，最终计数不依赖参考双射的选择。
7. `lockedEquivFree` 使用 Mathlib 已核查的 `Equiv.Set.compl`，将原点锁条件与在自由顶点到自由位置之间任取双射精确对应。`lockedEquivFree_apply` 证明其点值与原排列一致。
8. 将联合事件通过这一双射搬运，得到 `card_locked_joint_subset` 和 `locked_joint_subset_ratio`。最后将第二组源、目标均取空集，得到单侧条件概率 `locked_image_subset_ratio`。

以上步骤是任意有限规模的双射及基数定理，不展开具体的全排列，不依赖 Python 输出，也没有把待证联合公式放进假设。

## Lean Interfaces

全部声明位于 `Aris4Math.JointCounting`。

| 声明 | 接口 |
|---|---|
| `card_joint_image_eq` | 两个精确目标子集的联合纤维计数 |
| `card_joint_image_subset` | 两个允许位置集合的精确计数 |
| `joint_image_subset_ratio` | 均匀排列上的二项式比 |
| `card_joint_bijection_subset` | 不同顶点、位置类型的精确计数 |
| `joint_bijection_subset_ratio` | 不同类型上的同一二项式比 |
| `lockedEquivFree` | 原锁定排列子空间到自由双射空间的双射 |
| `lockedEquivFree_apply` | 每个自由点的实际像保持一致 |
| `card_free_vertices` | 自由点数为原点数减锁点数 |
| `card_locked_joint_subset` | 原锁定排列子空间内的精确联合事件计数 |
| `locked_joint_subset_ratio` | 以原锁定排列总数作分母的联合事件比 |
| `locked_image_subset_ratio` | 同一样本空间的单侧事件比，供 P2b 使用 |

典型调用取原类型为 `Fin v`、锁定标签为 `Fin s`。`vertices` 与 `positions` 都是 embedding；事件中的两组源集合是自由顶点 subtype 的 Finset，两组目标集合是自由位置 subtype 的 Finset。外层样本仍是满足全部锁条件的 `Perm (Fin v)` 子类型，不是另换了问题的样本空间。

## Remaining bridge to P2–P4

1. 为每条超图边定义其自由部分，并把它转换成自由顶点 subtype 的 Finset；为给定中心位置定义严格前方、严格后方的自由位置集合。
2. 对锁定中心，证明边对单交在该中心、锁点先后条件正确时，critical-pair 事件恰等于两个自由点集分别落入前后允许位置的事件；证明不兼容条件下事件为空。这才能把 `locked_joint_subset_ratio` 的一般公式认作具体 P4 权重。
3. 对自由中心，加入“指定公共点落到中心位置”这一额外锁，证明新旧样本空间之间的事件对应和总数比 $1/N$。随后用本模块的联合公式得到 P3，且需要核查无额外的 $r_Tr_U$ 因子。
4. 单边自由端点 P2a 还要把不同可能端点分割为互斥事件；锁定端点 P2b 还要核查锁定点兼容性。一般单侧条件位置概率本身已由 `locked_image_subset_ratio` 完成。
5. 将上述事件计数接到 `Greedy.lean` 的 `criticalPermutations`、全部类型边对的上界及主模块最终有限事件存在性定理。主定理未由本模块单独得到。

## Reproduction

从 `formal/` 执行：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build Aris4Math.JointCounting
```

复用 Lean 4.24.0 和项目固定 Mathlib 版本。`Counting.lean` 保持上一轮冻结内容，主模块、lakefile 和 manifest 未改。
