没有发现数学或接口问题。`twenty_one_propertyB` 与 `twenty_five_propertyB` 都只从原始超图、点对覆盖和恰 33 条边推出 `PropertyB`；它们仍不等于 T33，因为 `RemainingGoal` 明确是 \(22\le v\le 24\)。

## 21 点

唯一六度分支盖住了。`exists_locks_of_twenty_one` 先按最小度 5、6、7 分开。唯一六度点 \(x\) 时，度预算排除“其余全是至少 8”：\(6+8\cdot20=166>165\)。所有七度点与 \(x\) 的共度都不是 2 时走 \((6,7)\) 二锁；二锁表含 \(\lambda=1,3,4,5,6\)，\(\lambda=2\) 不在这张表里。若至少还有另一个七度点，共度至少 3 走 \((7,7)\)，否则五个 \((6,7,7)\) 配置由 `covers677` 覆盖，\(1\le\lambda(y,z)\le2\) 且 \(t\le\lambda(y,z)\)。七度点也唯一时，其余点恰好是 8；\(x\) 的坏伙伴至多 \(4\cdot6-20=4\)，两条公共边的外部顶点至多 \(3\cdot2=6\)，并集至多 10。该七度点的共度 1 伙伴至少 12，差集仍非空，得到 \((6,7,8)\)、共度 \((2,1,1)\)、三点不共边。

两个 ordinary 特殊型的扣除合法，而且是替换中间位置，不是再加一次。带标签后它们是四行 `boost`：\((1,1,1),t=1\)，以及 \((2,1,1)\) 的三种锁顺序。中间锁在一基位置 11，度为 7，且与另一把锁共度为 1。`ordinary_bad_pair_budget_of_codegree_one` 在 19 点底集上给出 \(4\cdot6\le 3B+19\)，所以普通坏对至少 2。实现出的重数表里，避开该伙伴的六条边都是纯 \([11]\)。位置 11 两侧各剩 9 个自由位，双向权重是

\[
2\frac{\binom94\binom94}{\binom{18}4\binom{14}4}=\frac{126}{12155}.
\]

两条普通坏对给出 \(252/12155\)。`enhanced_directed_bad_weight_lower` 用 \(q=0,r=2,c=0\)，只从这一个子族取下界；其余坏对权重非负，同一无序对只进入一次。这些对的交点数不是 1，实际临界概率为 0，减掉的是 \(C\) 里已经计入的记账权重。另外 20 个三锁型和 19 个二锁型走阈值惩罚：每个实际坏对至多按阈值计入一次，缺口由全部关联槽的非负惩罚补回，同型容量是 \(m(m-1)\) 个有序对。`validProfile` 要求各行正重数之和为 33。

## 25 点

活路径不假定种子已经在输入里。`exists_six_large_or_eight_triples` 只接收 \(H\)、点对覆盖、\(|E|=33\) 和 \(|V|=25\)。最小度至少 6，六度点至少 10 个，并且彼此共度全是 1。十个六度点上若有大小至少 4 的块，就落入六元分类的代表 6、7、8；否则至少有 10 个三元块。这里 \(\sum\binom{|B|}{2}=\binom{10}{2}=45\)，块点次之和至多 60，故三元块至少 10。每个三元块落在 21 个八元子集中，45 个八元子集不可能全都至多 4 个三元块，所以某个八元集至少有 5 个。没有更大块时，每个点都落在某个三元块里。

`classify_eight` 对任意这样的线性三元族先证明存在两个不交三元块和一条同时各交一点的横跨块，再标成 \(\{0,1,2\},\{3,4,5\},\{0,3,6\}\)，也就是一基的 \(123,456,147\)。之后 `extensions_complete` 才枚举与种子相容的 16 个候选的全部线性扩张，`checkWitnesses` 把每个可容许扩张双射到 14 个代表之一。`classify_seed_eight` 只在这一步之后使用。

实际痕迹由 `labeled_traces_recovered` 恢复：大块之外、未被大块覆盖的全部二元块都进入 `pairCompletion`。`recoveredCount 33 6` 把空迹、单点迹和每个块的重数 1 接到真实边纤维；空迹公式是 \(33\) 减去块数再减去各单点重数。八元表与三个六元大块表都由 `validProfile _ 33` 约束总重数，`numeric_counts` 对每个标签子集核对恢复重数。两端无校正中心、无空对上限，`totalBound<1` 经 `propertyB_of_uncorrected_profile` 回到原来的 Bool 计数染色。六元大块表只把既有分析表的空迹重数加 1，并且对 33 边公式重新核过。

## 装配与公理

`FiniteGoal` 仍是 \(19\le v\le 25\)。`finite_goal_of_remaining` 按等式调用 19、20、21、25，剩下的 \(\omega\) 只能落到 22、23、24。因此

\[
\mathrm{Target33}\leftrightarrow\mathrm{RemainingGoal}.
\]

两条导入日志是既有记录，不是这次执行。它们打印的 `twenty_one_propertyB`、`propertyB_of_triple_data`、`realized_threshold_deduction`、`twenty_five_propertyB` 以及两边的 `numeric_counts`、`strict` 都只依赖 `propext`、`Classical.choice`、`Quot.sound`。源码里的数值证明是 `decide +kernel`。`Assembly.lean` 末尾有三条约化连接定理的 `#print axioms`，该输出不在已读日志中，这次也没有执行。

## 阅读与未执行

读了 `TWENTY_ONE.md`，`TwentyOne.lean`、`TwentyOneStructure.lean`、`TwentyOnePairAssembly.lean`、`TwentyOnePairs.lean`、`TwentyOneTriples.lean`、`TwentyOneTripleData.lean`、`TwentyOneDeletion.lean`、`TripleProfiles.lean` 的计数恒等式，以及 ordinary 扣除所调用的 `OrdinaryLink`、`CustomDeletion`、`ConditionalUnion.pair_sum_le_weighted_deletion`。25 点读了 `TwentyFive.lean`、`TwentyFiveStructure.lean`、`EightClassification.lean` 的一般归一化与 `extensions_complete`、`EightTraceClassification.lean`、`TraceProfileBridge.lean`（`RowCertificate` 是其中的定义，没有同名文件）、`EightProfiles.lean`、`SixLargeProfiles.lean`，以及 `recoveredCount`、`pairCompletion`、`empty_typeCount_eq` 和 `propertyB_of_uncorrected_profile`。`Assembly.lean`、当前 `FiniteGoal` 和两份导入日志已读。

没有运行 Lean 或 Python，没有打开 `build.log`、`build-monolithic.log`、`eight-build.log`、`six-build.log`。中止日志不作为失败，旧成功日志也不作为这版代码的执行证据。14 个代表的具体有理数和 21 点各表的分数没有手算，它们由上述已接通的内核证书承担。B4 的 22 点稿没有重审。
