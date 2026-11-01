# Lean 排列计数模块

## Claim

本模块证明条件排列计算中的三个通用计数事实。设 $\alpha$ 为任意有限类型，$N=|\alpha|$，$s\subseteq\alpha$，$r=|s|$。排列 $\sigma:\alpha\simeq\alpha$ 的方向是“顶点到位置”。

1. 对任意有限标签类型 $\iota$ 和两条单射 $a,b:\iota\hookrightarrow\alpha$，满足全部 $\sigma(a(i))=b(i)$ 的排列有 $(N-|\iota|)!$ 个。
2. 对任意 $|t|=|s|=r$，满足 $\sigma(s)=t$ 的排列有 $r!(N-r)!$ 个。
3. 对任意允许位置集 $L\subseteq\alpha$，满足 $\sigma(s)\subseteq L$ 的排列有 $\binom{|L|}{r}r!(N-r)!$ 个。因此在全部排列上均匀抽取时，该事件的概率为

$$
\frac{\binom{|L|}{r}}{\binom Nr}.
$$

## Status

**PROVABLE AS STATED；上述一般命题已经 Lean 内核核查。**

源文件为 [Counting.lean](../formal/Aris4Math/Counting.lean)。本文件描述的是一般计数模块，不是主定理 $m(5)\ge33$ 的 Lean 证明，也没有宣称 P2–P4 已经全部形式化。

2026-10-06，`lake build Aris4Math.Counting` 成功，模块本身编译耗时 2.7 秒。八条导出定理的 `#print axioms` 都只有 `propext`、`Classical.choice`、`Quot.sound`；没有 `sorryAx`、新增公理或 `native_decide`。实际日志见 [lean-counting-build.log](../.aris/traces/proof-checker/2026-10-06_run04/lean-counting-build.log)。

## Assumptions

- 类型 $\alpha$ 有限且带可判等关系。此接口方便使用 `Finset`，不限制有限超图的数学范围。
- 第一个命题的两个标签映射必须都是单射，分别保证锁定顶点互异和指定位置互异。扩展成完整排列的存在性在证明中构造，不作为假设。
- 第二个命题要求 $|s|=|t|$。第三个命题不要求 $r\le |L|$；容量不足时二项式为零，与事件为空的计数一致。
- 允许空类型、空边子集、锁定所有顶点。定理没有排除这些情况，也没有通过有限测试代替一般证明。

## Notation and interfaces

全部声明位于 `Aris4Math.Counting` 命名空间。

| Lean 声明 | 已证明的内容 |
|---|---|
| `card_fixing` | 逐点固定 $s$ 的排列数为 $(N-r)!$ |
| `card_agreeing` | 在 $s$ 上与任意给定参考排列一致的排列数为 $(N-r)!$ |
| `card_prescribed_images` | 任意两条单射规定的全部点像条件的计数 |
| `card_preserving` | 将 $s$ 保持为自身的排列数为 $r!(N-r)!$ |
| `card_mapping` | 用成员关系刻画的任意同大小目标集合纤维计数 |
| `card_image_eq` | 用 `s.map σ.toEmbedding = t` 表达的同一精确计数 |
| `card_image_subset` | 指定点全部进入允许位置集的精确计数 |
| `image_subset_ratio` | 上述计数除以全部排列数后的二项式比 |

`image_subset_ratio` 的左右两端都是精确有理数。它不引入测度论概率定义；左端直接是有限均匀样本空间中的“事件个数 / 总个数”。

## Proof Strategy and Dependency Map

1. `fixingEquivSupported` 将“固定 $s$ 的排列”与“仅能移动补集点的排列”建立显式双射。使用 Mathlib 的 `card_perms_of_finset`，补集有 $N-r$ 个点，得到 `card_fixing`。
2. 将排列与参考排列的逆复合，把点像相等条件化为逐点固定条件。对于任意两条单射，先在其像之间构造双射，再用有限集合等基数保证补集可配对，得到完整参考排列。这证明 `card_prescribed_images`，没有假定扩展计数。
3. `preservingEquiv` 将保持 $s$ 的排列双射到“$s$ 内的排列 × 补集内的排列”。分别用 Mathlib 的 `Fintype.card_perm` 计数，得到两个阶乘之积。
4. 对同大小的 $s,t$，构造一个将 $s$ 映到 $t$ 的参考排列；逆复合将映射纤维搬回保持 $s$ 的纤维。由此得到 `card_mapping` 和 `card_image_eq`。
5. `imageSubsetEquiv` 按实际占据的位置子集分解事件：目标子集 $t$ 取遍 $L$ 的所有 $r$ 元子集；每个纤维均有 $r!(N-r)!$ 个排列。`Finset.card_powersetCard` 给出目标子集数 $\binom{|L|}{r}$。依赖和式是类型层的精确分割，不依赖枚举输出。
6. Mathlib 的 `Nat.choose_mul_factorial_mul_factorial` 给出 $N!=\binom Nr r!(N-r)!$。在有理数中消去严格非零的阶乘乘积，得到 `image_subset_ratio`。

证明使用任意有限类型的双射、基数、阶乘恒等式，没有展开任何具体 $N!$ 个排列，也没有将待证的排列公式放入前提。

## 与项目概率引理的关系

- `card_prescribed_images` 直接核查锁定 $s$ 个互异点到互异位置后，原排列样本空间大小为 $(v-s)!$。
- `image_subset_ratio` 是 P2b 使用的“指定的 $r$ 个自由点全部位于 $a$ 个允许自由位置”二项式比的通用核心；取 $L$ 为端点前方的自由位置即可。
- 已知自由点 $x$ 的指定位置条件本身可由第一个计数定理得到 $(N-1)!/N!=1/N$。本模块尚未单独声明并形式化这个归一化推论。

## Remaining bridge

以下应用步骤尚未在这个模块完成，不能因核心公式已核查就省略：

1. 将真实的“锁定顶点到给定位置”的子样本空间，显式双射到剩余自由顶点与剩余自由位置之间的等势双射；顶点集合与位置集合最初是不同子集，不能仅靠文字把它们当成同一个类型。
2. 将超图边的“最后点 / 第一点在位置 $k$”事件与 `image_subset_ratio` 的集合事件对应，包含锁定点的先后兼容性和不可能情形。
3. P2a 对 $r$ 个可能的自由端点作互斥分割，并在每个固定端点纤维内应用一次计数。
4. P3/P4 的两个不交指定点集，分别落在前后两个不交允许位置集的联合计数。需证明第二次条件抽取的剩余可用位置数，以及前方占位不改变后方允许位置数；本模块没有把这个结论当作已证。
5. 将最终事件精确计数接入 `Greedy.lean` 的 `criticalPermutations`，再接入主模块有限事件上界接口。结构选点和最后的数值界仍是其他义务。

## Reproduction

从 `formal/` 目录执行：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build Aris4Math.Counting
```

使用本项目既有 Lean 4.24.0 和 Mathlib v4.24.0 固定版本；没有修改 `lakefile.toml`、`lake-manifest.json`、全局配置或主模块。新增 import 的缓存按模块提取，复现不需要运行项目 Python 概率计算器。
