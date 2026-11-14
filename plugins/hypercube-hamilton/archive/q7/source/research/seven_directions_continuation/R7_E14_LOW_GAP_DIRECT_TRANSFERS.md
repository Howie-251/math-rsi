# E14 的差二边缘外切与小跨数归约

以下固定 $Q_7$ 的任意 $57$ 边短匹配 $M$。有相邻原孔时，先补入该短边并用 E12。以下差二命题均可假设原孔独立。孔型按固定的两种全局颜色 $\alpha,\beta$ 记。切向上的短镜像翻转颜色。本文为直接回代证明，待独立审计。 [E12 补全及平衡、差一门](R7_HIGHER_HOLE_CUTS.md) · [审计](R7_HIGHER_HOLE_CUTS_REVIEW.md)

## 1. 差二的供体与分居接收

取差二外切 $A:(r,r+2)$、$B:(s+2,s)$，其中 $r+s=5$。写 $W=H_B\cap\alpha$、$L=H_B\cap\beta$，令 $Y$ 为 $A$ 的全部 $\beta$ 原孔在 $B$ 中的短镜像。每个 $y\in Y$ 由 $B$ 的原内部短边覆盖，因为它既非原孔，唯一外短邻点又是原孔。选两枚不同标记 $y_1,y_2\in Y$。差二双桥证明第 2–3 节只用 $C_r$ 将供体压缩成实际路径，并抑制两个标记。所得 $K(B)$ 匹配 $F$ 的孔为 $W\cup L\cup\{y_1,y_2\}$。若局部圈恰避标记、保留 $F$ 且仅新增短边，按原证明两次展开即得所需 $128$ 点圈。这里 $C_r$ 的范围为 $0\le r\le5$，规定匹配允许长边和同色边。 [双桥及展开](R7_HIGHER_DELTA2_TWO_BRIDGES.md) · [双桥审计](R7_HIGHER_DELTA2_TWO_BRIDGES_REVIEW.md) · [$C_0$ 至 $C_5$ 导入范围](R7_HIGHER_HOLE_CUTS_REVIEW.md)

若 $B$ 的某内切两侧原孔净差 $\#\alpha-\#\beta$ 均为 $1$，且 $Y$ 分居，选每侧一枚标记。两侧加标记后的孔差均为 $2$，每侧调用完整五维差二避一工具。受控圈供体的选配对论证迫使压缩后的 $F$ 在该内切有正跨边，故其第 1 节的拼接适用。 [受控转移第 1–3 节](R7_CONTROLLED_CYCLE_DONOR_TRANSFER.md) · [联合审计](R7_MU3_CONTROLLED_AND_T63_REVIEW.md) · [双桥回代](R7_MU3_REMAINDER_UPDATE.md) · [五维差二避一及最终审计](<E:/新问题/research/six_directions/Q5_A10_FULL_REVIEW.json>)

## 2. 两种边缘差二外切整族

**$A:(5,7)$，$B:(2,0)$。** 取任一 $Y$ 分居的内切，存在性来自 $Y$ 有七个互异点。若 $W$ 也分居，两侧原净差均为 $1$，用第 1 节的分居接收。若 $W$ 同侧，从 $Y$ 每侧取一枚标记，异侧成为只含一枚指定省略孔的半面。此时 $F$ 四孔同色，调用已审六维 T44 的孤立指定省略孔工具，再按第 1 节展开。 [六维 T44 孤立省略孔](<E:/新问题/research/seven_directions/Q6_T44_SINGLETON_FORBIDDEN.md>) · [审计](<E:/新问题/research/seven_directions/Q6_T44_SINGLETON_REVIEW.md>)

**$A:(4,6)$，$B:(3,1)$。** 以 $B$ 的唯一少数原孔 $a$ 为内坐标零点，设 $w_i,y_i$ 分别为 $W,Y$ 在第 $i$ 位取一的点数。旧双桥门接收 $w_i\in\{2,3\},y_i\ge2$ 或 $w_i=0,y_i\le5$。若 $w_i=1$ 且 $1\le y_i\le5$，两内侧的原净差均为 $1$，用第 1 节的分居接收。若这些判据全部失败，则 $Y$ 在 $w_i\le1$ 的每一列取常值，在 $w_i\ge2$ 的每一列至多一个点取一。投影到后类列仍有六个互异点，至多一个为零，因此总占用至少五，后类列至少五个。取其中任意五列。六个 $Y$ 点相对于 $a$ 都是奇重量，在这五列上全零的至多一个。总占用至多五，所以恰一个在五列全零，其余五个各占不同的一列。奇性迫使 $Y$ 正好为 $a$ 的六个面内短邻点。于是 $a^*$ 的六个面内短邻点及唯一外短邻点 $a$ 都是原孔，而 $a^*$ 因独立性是非孔，无法由原短匹配覆盖。矛盾。 [旧双桥门](R7_HIGHER_DELTA2_TWO_BRIDGES.md) · [五列占用论证](R7_DELTA2_FIVE_STRONG_COLUMNS.md)

两段论证对给定孔集的每个实现短匹配成立。E14 差二外切按交换面与颜色只有上述两型及 $(3,5)/(4,2)$。因此，按差二外切归约只余中央型仍需检验接收几何。

## 3. 平衡内半面与双省略拼接

设某差二外切的接收面 $B$ 有一个内切，两侧原孔净差为 $0,2$。平衡侧每色至少一枚原孔，差二侧少数原孔至多一枚，且至少两枚 $Y$ 点在差二侧。选这两枚点作标记。压缩匹配 $F$ 的两内面分别为平衡孔型及净差四孔型，差二侧加标记后用完整五维 T44 或 T15，恰省略所选两点。 [五维 T44](<E:/新问题/research/six_directions/T44_Q5_CLOSURE_DRAFT.md>) · [T44 审计](<E:/新问题/research/six_directions/T44_Q5_CLOSURE_REVIEW.json>) · [完整五维 T15](<E:/新问题/research/seven_directions/Q5_T15_FULL_CLOSURE.md>) · [T15 审计，全部 165 标记轨道](<E:/新问题/research/seven_directions/Q5_T15_FULL_REVIEW.md>)

若 $F$ 有内跨边，内跨数为正偶数，因为两内面的孔数均为偶。配掉一侧跨端口、用对应局部圈、删端口配对并接回原内跨边，再把路径压给另一侧局部圈并展开，保留 $F$ 且恰省略两标记。若无内跨边，平衡侧取一枚与标记同色的自由孔 $x$。其短内镜像 $x'$ 异色，位于差二侧避两标记圈上。从该圈删除 $x'$ 的一条非规定短边 $x't$，再用五维完整平衡孔路径工具取得保留平衡侧规定匹配的 $x$–$t'$ 生成路。$x,t'$ 异色，两路由短桥 $xx',tt'$ 闭合。两种跨数下均得到第 1 节需要的接收圈。此处复用旧平衡侧自由根的零跨拼接，并将另一局部输入由避一换成避二。旧六维双省略易面稿中，标记和全部保留孔同侧时，另一侧无孔，使用其完美匹配拼接分支。 [五维平衡孔全工具](<E:/新问题/research/six_directions/Q5_A10_FULL_CLOSURE.md>) · [已审避一拼接](<E:/新问题/research/seven_directions/R7_ODD_BRIDGE_MARGIN_REVIEW.md>) · [六维双省略易面](<E:/新问题/research/seven_directions/Q6_TWO_AVOIDED_EASY_FACES.md>) · [易面审计](<E:/新问题/research/seven_directions/Q6_TWO_AVOIDED_EASY_REVIEW.md>)

对中央差二外切 $A:(3,5)$、$B:(4,2)$，第 1 节及本节的判据可分别用在两个供接方向。令任一内坐标位一面在 $A$ 的两色原孔数为 $(a,b)$，在 $B$ 为 $(c,d)$。在 $B$ 接收方向中，位一面的多数原孔、少数原孔、候选标记数为 $(c,d,b)$，总数为 $(4,2,5)$。在 $A$ 接收方向中相应为 $(b,a,c)$，总数为 $(5,3,4)$。对于每一方向和两个内面朝向，未被这两条判据剥离的输入须满足以下必要条件。

- 位一面原孔净差为 $1$ 时，全部候选标记同侧。
- 净差为 $2$ 的一侧含至多一个少数原孔，且对侧平衡并有孔时，差二侧至多有一个候选标记。

例如 $B$ 接收方向若 $c-d=2$ 且 $d\in\{0,1\}$，则余域要求 $b\le1$。反向若 $b-a=2$ 且 $a\in\{0,1\}$，则余域要求 $c\le1$。换位零面同理。差二侧有两枚少数原孔时，本节的局部孔型变为五维 T26，须另查准确带标记接口。以上为逐坐标的必要条件，中央差二整族尚须覆盖。

## 4. 小跨数与低差边界

- 若某外方向恰一条规定边 $pq$，取 $p\in A,q\in B$。颜色计数保证 $B$ 有一枚与 $q$ 异色的原孔 $u$，其镜像 $v$ 与 $p$ 异色。$p,q$ 对各自面内短匹配自由。P6 分别给 $p$–$v$ 和 $q$–$u$ 生成路，由两条短桥 $pq,vu$ 合圈。此推论不需要孔数限制。 [P6](<E:/新问题/research/six_directions/P6_FULL_CLOSURE.md>) · [审计](<E:/新问题/research/six_directions/P6_FULL_REVIEW.json>)
- 任一方向零条规定边可用 P6/R6 两面拼接，任一方向恰两条规定边可用已审 F14，后者量化 $|M|\ge57$ 且有二重方向的所有输入，包含两种端口颜色关系。 [零跨圈拼接](R7_HIGHER_HOLE_CUTS.md) · [F14 第 5 节](<E:/新问题/research/seven_directions/R7_THREE_FREE_PAIRINGS.md>) · [F14 审计](<E:/新问题/research/seven_directions/R7_THREE_FREE_PAIRINGS_REVIEW.md>)
- 平衡外切 $(a,a)/(7-a,7-a)$ 在 $2\le a\le5$ 由 B 整族关闭。交换面后 $a=0,1$ 时，小面任一内切绝对孔差至多一，因此大面只要有一个绝对孔差至多一的内切就命中 Q+。按本切剩余的大面各内方向绝对孔差至少二，且原外跨数至少四。 [B](R7_HIGHER_HOLE_CUTS.md) · [Q+](<E:/新问题/research/seven_directions/R7_NEAR_BALANCED_BLOCKS.md>)
- 差一外切 $(1,2)/(6,5)$、$(2,3)/(5,4)$ 由 D 整族关闭。边缘 $(0,1)/(7,6)$ 在大面原内孔净差为 $(0,1)$ 或 $(-1,2)$ 时，选大面一枚多数孔 $u$，使去掉 $u$ 后两个内半面的绝对孔差至多一。在前型可取任意多数孔，在后型取差二侧的多数孔。以单孔面调用 $B_1$ 生成终段，大面删 $u$ 后用 $C6^+$ 接收，余下展开沿用旧单孔面转移。此充分条件下剩余的边缘外切，大面每刀的两侧原净差分别至多 $-2$、至少 $3$。中心差一 $(3,4)/(4,3)$ 仍按单侧平衡半面与桥镜像、或 UO 的两面内切和同一标记条件检查。 [D](R7_HIGHER_HOLE_CUTS.md) · [旧单孔面转移](<E:/新问题/research/seven_directions/R7_TWELVE_HOLE_SINGLETON_TRANSFER.md>) · [单孔面审计](<E:/新问题/research/seven_directions/R7_TWELVE_HOLE_SINGLETON_REVIEW.md>) · [中心](R7_FOURTEEN_CENTRAL_TRANSFER.md) · [UO](<E:/新问题/research/seven_directions/R7_UNBALANCED_OUTER_TRANSFER.md>)

所有剩余条件只相对这里列出的接口。更高差外切及既有整族仍可另行剥离。 [联合台账](R7_JOINT_COVERAGE_SCOPE.md)
