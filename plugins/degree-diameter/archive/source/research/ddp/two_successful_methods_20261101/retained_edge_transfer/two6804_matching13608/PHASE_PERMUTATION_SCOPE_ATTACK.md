# 两份6804：phase-permutation 容量模型的纸面反例攻击

本文件仅只读同目录 CONSTANT_PHASE 的 PRED/PAPER/RESULT，继承 actual6804 源的统一相位 profile；未读取源边表、重验 field/source D4、运行 BFS/solver 或生成13608图。以下支持 root 即将检查的符号模型，不把未返回的数值窗口写成已完成。

## 域与变量

源有12个相位，每相位567点。单步相位 walk 矩阵 Q 满足 `Q[i,j]=3` 当 j−i∈{±1,±4}，`Q[i,i+6]=1`，其余0（模12）。Q是对称 circulant，每行和13；此处是整数 walk 数，不是布尔邻接矩阵或有限域运算。

两份源全部保边，只加一个跨 copy perfect matching。模型仅允许 matching 把 phase r 的全部567点送到同一 phase π(r)，并在块内允许任意双射。144个 binary x_rs 表示 π；12条 row-sum=1、12条 column-sum=1 恰好给出12相位 permutation。每个这样的 permutation 都可在相等大小的 fibre 间补任意双射，但 x 不记录这些567点级双射。

不应加 x_rs=x_sr 或 π²=id：copy0→copy1 是 π，反向是 π⁻¹，不要求两个方向用同一个 π。也不应把这个模型称为任意跨层 perfect matching；同一源 phase 的点分散送往多个目标 phase 的匹配在域外。

## 一次 cross 的线性式正确

跨 copy 长度≤4的路含奇数次 matching 边，只有1或3。若3次 cross，总共至多1条旧边，而相邻两次 cross 的两个内部间隔不能都含旧边，故必有连续两次 cross。perfect matching 使这两步沿同一边原路返回，可消去。因此任何跨 copy R4 可达目标都有恰一次 cross、a+b≤3条旧步的路线。

固定 copy0 中某实际 root，其 phase 为 i。恰 a 条旧步到 phase r 的 prefix walk 数为 `(Q^a)[i,r]`。每个 prefix endpoint 通过 matching 到 phase s=π(r) 的某实际点；从该点恰 b 条旧步到 phase j 的 suffix walk 数仍统一为 `(Q^b)[s,j]`，不依赖块内怎样双射。因此

`C_ij(π)=Σ_(a,b≥0,a+b≤3) Σ_(r,s) (Q^a)_ir x_rs (Q^b)_sj`

精确计数这些“带一个指定 cross 的普通 walk”。Q⁰=I 必须保留；a=b=0给出直接 matching 边的一条路线。旧步回退、多条路线落在同一个 target 都会造成过计，正适合作 distinct target 数的必要上界；不能将 C 当精确点覆盖数或非回退词数。

故每个 phase j 的567个目标均在 R4，必要条件正是全部144个 C_ij≥567。模型 coefficients 对 x 线性；不需要3-cross的 x 三次项，因为这些短路已被上述消去覆盖。该证明没有交换 matching 与旧步的次序，也不假设 matching 是源图 automorphism。

Q 对称，反方向容量矩阵为 ΣQ^a XᵀQ^b=Cᵀ（交换 a、b）；因此检查全部144个 forward 槽已包括 reverse 容量义务。不能因源相位 circulant 就只检查 i=0：一般 π 不与相位平移交换，各 root phase 仍须全部保留。

## π(0)=0：只在容量模型中是合法 gauge

给任意 π 施输出相位整体平移 δ，即 π′(r)=π(r)+δ。由于 Q circulant，所有 C_ij 只发生输出列的循环置换；144个相同下界、row/column permutation 约束均保持。取 δ=−π(0)，可令 π′(0)=0。因此限制 x_00=1 不漏掉容量可行的 permutation；若这个规范域真 infeasible，未规范的整个 phase-block 容量域也 infeasible。

该论证不需要证明相位平移在真实6804点图上是 automorphism。相应地，不能据此宣称两个实际 matching 图必同构、规范后的点级路线仍相同，或将 source root 逐点固定。它只保容量可行性，而本轮 gate 正是容量 gate。

## verdict 的边界

若求得 binary π 并经 root 直接整数代入检查 row/column 与 min C≥567，仅支持“phase 容量必要条件存在可行点”。它没有指定567点级 matching，更没有保证不同 walk 的端点互异、真实跨层 R4 或13608/D4。正返回不生成 graph 也完全合理。

若求解器给真正 infeasible 状态，结合上述完整域/规范化，才可排除所有 phase-block permutations 及其任意块内双射；仍不排 phase-mixing matching、改旧边、多条跨层边或其他 source。time limit 且无 incumbent 是 UNKNOWN，不是 NO；objective0 的 raw bound 也不是路线不可行证明。

旧常数 phase offset 的328<567严格障碍不能直接替代这144槽模型：一般 π 使 prefix phase r 跨后变为 π(r)，不再有相同相位差卷积。它只是已关闭子族，无需重测，不能把328套给全部 permutations。

没有发现当前公式、一次 cross 分类、变量域或 capacity-only gauge 的实质缺口。数值编码/结果另由 root 唯一窗口及其实际回执负责，本文件不追加第二窗口，不认证公开优先权，也不计新图。
