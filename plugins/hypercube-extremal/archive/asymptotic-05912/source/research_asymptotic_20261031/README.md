# 渐近上界推进记录（2026-10-31）

目标为从项目基准 $0.5912405941884453\ldots$ 争取约 $0.01$ 的绝对降幅。**尚未取得新认证上界，百分位目标未完成。**

本轮证明和未闭合部分见根目录 [PROOF_PACKAGE.md](../PROOF_PACKAGE.md)。原成果文件未修改。

## 已完成的可核查工作

1. 补入汇编缺失的完整四维轨道表和独立完备性检查器。重新核对全部 $3,212,821$ 个代表，轨道大小之和与独立有标号计数同为 $1,226,436,381$。
2. 重新执行原 C++ 整数矩阵、COP 和带符号三次型检查，获得原最高分子 $523510268530411454208$。随后在新生成的全部 $828$ 个度分布包络上，用精确分数重算九组超几何势；最优值仍是原 $m=1024$ 的分数。
3. 实现 $sP$ 四次非负分解来认证边根三次型 $P$，以及与原四维核的联合 LP、完整四维评分、平方方向生成、精确有理修复。数学框架不依赖不完整五维语料。
4. 在正的完全正张量控制例中，分离 LP 均返回零最优值；直接边根计算和旗矩阵提升的数值核对误差在运行日志中逐轮保存。

## 实验及其边界

|实验|实际结果|解释|
|---|---|---|
|乘子分离|发现两个负配对方向|都化简为已有的 $p_4(p_5-p_6)^2$，不是新结构|
|原核整体缩放 + 乘子三次型|完成 24 轮，每轮扫描完整四维域；最佳浮点最高分约 $0.591240594146587$|表观收益约 $4.2\times10^{-11}$|
|上述候选精确多项式修复|两根型所需修复量约 $2.42\times10^{-10}$、$1.08\times10^{-10}$|保守修复预算超过表观收益，不能更新正式界|
|Gram 块、COP 项重新加权 + 动态方向|完成 15 轮扫描；最佳浮点评分约 $0.5912405942359262$；随后 GLOP 返回 ABNORMAL|未改善原基准；不是方法不可能性证明|
|把 Gram 块拆成各列|完成 4 轮全域扫描；有限主问题约 $0.5912405102$，全域最高分仍达 $1.3961$；随后数值异常|有限主问题失真很大，候选被全域反例否决|
|CLP 后端对照|限时返回 FEASIBLE；但原始系数恒等式残差超过 $344$，多项式在单位向量上为负|已拒绝该输出；其近零原始评分无效，未计入任何上界|

这些实验均未给出整个乘子锥的最优性证书，不能从阴性结果推出“四维方法不可能到达 0.58”。

CLP 输出的独立反例是根类型 $0$ 的 $P(e_4)\approx-3$ 和根类型 $1$ 的 $P(e_6)\approx-5.96$。见 [rejection_audit.json](experiments/joint_gram_columns_clp_primal/rejection_audit.json)。代码现会在评分前重算原始多项式系数、非负权重和单位向量值，并验证原 LP 约束；回归核查见 [primal_guard_regression.json](experiments/primal_guard_regression.json)。这也是为什么不能只依据求解器状态或漂亮的局部评分宣布突破。

## 新增五维外层路径实验

已实现三维根的六十维外层路径特征：按路径在平行外层行走一、二、三步，分别统计五条边的存在/缺失模式。它记录完整四维附件中的外层边。一个精确例子表明，根图和八条侧边完全相同的两个附件，新的全边路径频率仍可分别为零和 $1/24$；因此这不是对旧侧边特征的改名。见 [outer_layer_witness.json](q3_detour_v21/outer_layer_witness.json)。这不等同于证明它独立于全部其他旧旗核。

根目录证明包 Step 5 给出完整抽样引理：任意固定 PSD 路径核的五维平均至少为 $-D/(n-4)$。一个旧有限分布的负配对已经有理化，并由不导入探索代码的标准库程序直接重建路径验证，精确值约为 $-0.000147381522$。见 [exact_separation_receipt.json](q3_detour_v21/exact_separation_receipt.json)。该分布对部分旧 PSD 约束也有违约；不能据此宣称新模型优于已经闭合的旧模型。

| 五维运行 | 图池最高评分 | 图池外反例评分 | 结论 |
|---|---:|---:|---|
| 原浮点候选加新路径核，8 轮 | 0.589830338598 | 0.599513902104 | 被精确反例否决 |
| 先补齐图约束再增添方向，24 轮 | 0.589210989601 | 0.598222027777 | 被精确反例否决 |
| 109 个旧块分别重调，并纳入前两批反例，20 轮 | 0.590269235285 | 0.599924141476 | 被精确反例否决 |
| 保留认证基准、加入删边图和第三批反例，16 轮 | 0.590340425874 | 0.605453791353 | 被精确反例否决 |
| 整个路径核对角严格限制为 0.03，14 轮 | 0.590778093361 | 0.592758148430 | 被精确反例否决 |
| 完整四维上包络限制为 0.60，20 轮 | 0.590973248695 | 0.592107175865 | 被精确反例否决 |
| 共享根方向核与完整上包络，24 轮 | 0.591173081355 | 0.591694619835 | 被精确反例否决 |
| 共享方向核，二阶段减少多余系数，续跑 8 轮 | 0.591056545652 | 0.592147155726 | 被精确反例否决 |

每轮都重新评分全部已知图；前两组图池有 592,825 张图，第三组另纳入 200 张反例。上表是有限图池的拟合结果，**不是渐近上界**。反例是完整、合法的一般五维图；并非只检查了某个奇方形子类。独立有理数评分收据在各 `*_holdout/exact_counterexample.json` 中。

反例中的 35–44 边图暴露出稀疏图取样不足的问题。已另生成并逐图检查 10,901 张随机删边子图；第四组保留原已认证四维矩阵整体作为可选基准，避免拆开其耦合三次项。去重后的图池共有 603,947 张图，但图池外一张 31 边图仍给出精确评分 $0.60545379135\ldots$。扩大图池尚未解决全域有效性问题。

随后完成了一个真正覆盖全域的子问题：对 99 个三维根类型枚举全部侧边和合法外层图，检查 42,655,632 个规范根附件，精确求出第四组候选 566 个方向的单附件线性极值。按根轨道大小加权，计数与独立完整四维计数 1,226,436,381 一致；1132 个极值见证均以整数运算复核。该候选新核的保守对角界由约 1.79036 收紧为 0.326718。见 [exact_diagonal_extrema.json](joint_q3_detour_blocks_r4/exact_diagonal_extrema.json)。这覆盖完整单附件域，**不覆盖完整五维评分域**；各方向极值加权后的核对角界也是上界，不是声称可以同时取得的最大值。

辅助谱矩阵实验也已保存：十九维非交换矩矩阵没有分离旧初始化分布；加入对角度数变量后的三十五维矩阵只有约 $-1.64\times10^{-6}$ 的负特征值，小于该分布对已有 PSD 块的违约量。它没有提供结构优势证据，也不是谱方法不可能性证明。

## 整核限制与共享方向

已将各方向最大值之和改成整个路径核的完整附件最高值，并用向上量化、逐根有理缩放和向下舍入严格限制实际权重。第四组候选的对角界进一步降至约 0.217249；第五组全部附件的实际对角不超过 $3/100$，完整重枚举与舍入检查见 [exact_cap_guard_verification.json](joint_q3_detour_caps_r5/exact_cap_guard_verification.json)。这些限制控制单附件，不能替代五维最高评分。

新发现的问题是：旧侧边模型把两个附件分别按根的自同构群取商，丢掉了它们共享的相对方向。新的核采用同一个根规范化，并对 $v_{ga}v_{gb}$ 使用同一个群元素 $g$ 求平均。它仍为 PSD，渐近抽样误差仍不超过 $D/(n-4)$。空根处，相同单点与相邻单点的核值可分别为 $1/16$ 与 $-1/16$，而旧单附件轨道号完全相同。

在旧分布上，有 44 类根出现非平凡方向的负配对。根 1662 的一个方向已经有理化，并精确去除了整个不变子空间；独立标准库检查得到

$$-\frac{384230259128990903}{737869762948382064640}\approx-0.0005207291021.$$

见 [exact_separation_receipt.json](q3_oriented_arms_v21/exact_separation_receipt.json)。该分布本身还违反其他旧 PSD 条件，所以此结果不宣称对完整旧锥的严格优势。新增 C++ 特征、群不变性和四维包络重构均与独立 Python 计算核对，见 [receipt.json](q3_oriented_controls/receipt.json)。

## 从包络转向完整五维验证

对角平均给出完整四维上包络 $U$，但五维评分与其平均之间还差一个非负的配对损失。已实现全域包络扫描，并在第六至八组搜索中限制 $U\le0.60$；这仅是探索阶段的限制。第六组第 8 轮快照仍有 37 边图给出精确反例 0.591977635220，说明这个限制本身不够。

根目录证明包 Step 10 给出新的完整归约：固定阈值 $b$，枚举所有 $U>b$ 的四维面在五维立方体十个面位置上的相容部分赋值，累加超过 $b$ 的部分，并扣除已选面之间的非负配对损失。所有真实五维图都被覆盖。已实现浮点分支定界原型 [q5_pair_family.py](q5_pair_family.py)，包括重叠的零边和一边一致性、四圈检查、共同根匹配以及未完成分支上界。

单轨道控制中，独立评分确实复核了非零配对损失。对第六组快照和阈值 $b=0.599$，全部 133 个高分轨道、39,712 个有标号模式已完成搜索，所得放宽上界约为 0.599600。它比该候选的 0.60 包络紧，但远高于正式基准，而且仍是浮点结果。见 [report.json](pair_family_full_599/report.json)。不能将其记为新渐近界；它是全域验证工具的进展。

把阈值降到 $0.59$ 后，需要覆盖 6819 个轨道、2,446,321 个有标号模式。45 秒内完成三个首面分支，状态为 `UNKNOWN`；保留的上界仍约 0.60，不能报告已经完成定界。一个可行部分赋值的放宽评分约为 0.59691，其中忽略的旧边根损失约 0.00459，旧侧边损失约 0.00022。下一步最值得加入的是旧边根损失，而非单纯延长当前搜索。对应分解见 [omitted_gap_decomposition.json](pair_family_full_590/omitted_gap_decomposition.json)，具体归一化与实现计划见 [FULL_DOMAIN_NEXT.json](FULL_DOMAIN_NEXT.json)。

## 复现

完整复验原基准只需要 Python 标准库和 C++20 编译器：

```bash
python3 research_asymptotic_20261031/verify_baseline.py
```

输出保存到 [baseline/fresh_verification.json](baseline/fresh_verification.json)，输入哈希也在该文件内。这与根目录原有的一键脚本不同，实际重新运行完备性和评分检查。

探索程序需要 NumPy 与 OR-Tools。本机 `bootstrap_cached_environment.py` 可从已有 pip 缓存恢复到 `/tmp/cube_research_python`，不依赖联网安装。用于原始几何和评分的文件已按字节复制到 `vendor/`，其出处与哈希见 [SOURCE_MANIFEST.json](vendor/SOURCE_MANIFEST.json)。探索分布是旧研究的有限 LP 输出，只是初始化数据，不是完整对偶证书。

```bash
python3 research_asymptotic_20261031/multiplied_cubic.py \
  --distribution research_asymptotic_20261031/baseline/inherited_search_distribution.npz \
  --masks research_asymptotic_20261031/baseline/full_masks.bin \
  --output /tmp/c4_multiplier_reproduction

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 \
python3 research_asymptotic_20261031/cubic_cone_search.py \
  --source research_asymptotic_20261031/vendor \
  --certificate asymptotic_05912_flag_algebra \
  --masks research_asymptotic_20261031/baseline/full_masks.bin \
  --distribution research_asymptotic_20261031/baseline/inherited_search_distribution.npz \
  --output /tmp/c4_joint_reproduction --iterations 24 --seconds 240

python3 research_asymptotic_20261031/recover_cubic.py \
  research_asymptotic_20261031/experiments/joint_multiplied_cubic/best.json \
  --output /tmp/c4_exact_polynomial.json
```

最后一个命令只认证多项式非负性，不认证密度上界。正式候选还必须恢复矩阵并完成全域整数评分。

五维部分新增的源程序、冻结候选和图池已复制到 `vendor_q5/`，原始位置与逐文件哈希见 [SOURCE_MANIFEST.json](vendor_q5/SOURCE_MANIFEST.json)。不依赖旧目录中的运行任务。原 109 块在全图池上的重构最大误差为 $3.34\times10^{-16}$；路径整数核与独立 Python 实现逐项核对了 3,600,000 个值。

下列命令在 `research_asymptotic_20261031/` 内运行：

```bash
python3 verify_detour_separation.py q3_detour_v21/exact_separation.json \
  --output /tmp/detour_separation_check.json

python3 q3_detour_features.py --source vendor_q5/search/frozen_v21 \
  --output /tmp/detour_moment_reproduction

python3 verify_detour_candidate.py --candidate joint_q3_detour_r2 \
  --witnesses joint_q3_detour_r2_holdout/witnesses.json \
  --output /tmp/detour_counterexample_check.json

python3 q3_detour_diagonal.py --candidate joint_q3_detour_blocks_r4 \
  --output /tmp/detour_complete_attachment_extrema.json

python3 verify_detour_cap_guard.py joint_q3_detour_caps_r5

python3 verify_oriented_separation.py q3_oriented_arms_v21/exact_separation.json \
  --output /tmp/oriented_separation_check.json

python3 q5_pair_family.py --candidate joint_q3_detour_unary_r6_snapshot \
  --output /tmp/pair_family_check --threshold 0.599 --seconds 30
```

第一条只依赖标准库，后两条使用本地恢复的 NumPy/OR-Tools 环境。`q3_detour_kernel.cpp` 由程序编译到 `/tmp`。约 493 MiB 的 `q5_frozen_v21_components/components.npy` 是可重建的发现阶段缓存，不属于正式证明依赖。

## 下一步

后端对照结果、已加入的全域反例和候选方向均已保存。若继续四维优化，需要控制病态和原始多项式恒等式残差，并用精确修复后的上界评价收益；不应继续追逐小于修复预算的末位变化。

外层路径核和共享方向核均已完成抽样证明及精确分离控制，整核对角与全域四维包络限制也已实现。当前主要缺口转为：使包含配对损失的完整五维放宽足够紧，并恢复可独立核查的整数上界。原型目前只扣除新路径核的损失，还可加入旧侧边和边根核中已证明非负的损失。应将相容部分赋值直接反馈为优化约束，并对遗漏面严格保持包络阈值；单纯反复扩大有限图池已经不足。所有反例均应保留。原已认证四维矩阵可以整体缩放，不能拆开其耦合三次项。

## 暂停记录（2026-11-02）

已按用户要求暂停，当前没有本任务的运行中计算。正式上界仍为 0.5912405941884453，未取得新的认证改进。

最新已补齐旧边根与侧边配对损失，建立部分面约束的线性优化，并加入路径与侧边状态的交叉 PSD 特征。独立几何和评分控制通过。第九轮系列的 12 次优化仍不断出现部分赋值违约；第十轮系列在 13 次成功保存的扫描后，最后一次 LP 尝试未通过。最后保存候选在 8444 条已选完整图/部分面约束上的评分约为 0.5902954154，但没有重新扫描原完整图池，也没有完成新的五维分离或精确认证；不能将其记作上界。

原八组候选都已被精确反例否决。此次交叉特征候选尚未接受同等独立反例检验。恢复工作时首先补齐这些检验，而不是将有限约束评分当成突破。详细暂停状态见 [RESEARCH_STATE.json](RESEARCH_STATE.json)。
