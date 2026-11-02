# 广度构造第三轮：阶段汇总

截至本次汇总，实际新增公开下界仍为 **0**。本轮保存了若干失败的完整小图、关闭了明确的有限或单调范围，并取得两项已有文献提供的正向覆盖保证；尚无超过保存基线的完整合法图。最后一项四region联合试验也已终态，增益为零。没有生成42525/46656点route-chart提升，也没有生成728点binary lift。旧[专家说明](../../expert_review_20261027/STATUS.md)保持2026-10-27 03:15:51 UTC的冻结截点，不由本报告回写。

“完整图”表示有明确边表且完成对应核查，不等于满足目标。“partial state”表示保存了构造变量或原作者状态，未新展开大图。“UNKNOWN”不表示不可行。exact-NB5要求每个有序点对（含对角）都有恰五步非立即回退walk；其缺项数与普通距离大于五的无序坏对数不可混用。

## 已终态的范围

| 入口 | 产物类别 | 实际结论 | 关闭或保留的范围 |
|---|---|---|---|
| [256点状态移位图](debruijn256/REPORT.md) | 完整图，目标失败 | n=256、Δ=8、D=4；普通距离>3的无序对12354个。点对(27,73)给出度余量补边障碍。 | 只关闭固定旧边全部保留、仅填度余量以降到D3；不排除删边重连或其他状态图。 |
| [通用F3⁵ route chart与小群侦察](source_scout/SCOUT.json) | 已知充分条件＋固定族检查 | 324个约化五步字的rank5与逆相容已验。任意合法四价exact-NB5控制器C给出243|C|点、Δ12、D≤5。 | A5×C3全部四元逆闭Cayley控制器范围失败；F31⋊C6只关闭2926个二逆对组成，未排一般控制器。 |
| [175点五圈控制器](pentagon175_controller/REPORT.md) | 完整控制图，目标失败 | 最佳四正则图普通D=6、普通无序坏对315；exact-NB5有序缺项2696，逆一致标号通过。 | 四起点固定交换profile结束；不排整个骨架或所有175点控制器。未生成42525点图。 |
| [192点电压控制器](controller_lift192/REPORT.md) | 完整控制图，目标失败 | root独立核查普通D=6、普通无序坏对144；exact-NB5有序缺项2752。 | 仅完成固定六点基图、C4×C8电压的八起点有限profile；未穷尽完整电压空间，未生成46656点图。 |
| [F2⁴通用四步chart](binary_route_chart4/REPORT.md) | 完整规范参数空间排除 | 2419200个规范候选均无chart；root只对一个保存候选的全部108字作独立秩校准，一致。 | 关闭特定域/维数/步长/四逆标签/全部约化字通用的chart；不排其他route chart或一般(8,4)图。 |
| [三价NB控制器界](cubic_nb5_bounds/REPORT.md) | 数学必要条件＋小算术证据 | exact-NB4控制器n≤20；exact-NB5控制器n≤44，42/44仍开放。 | 不声称n≤40，也未构造42/44点图；奇数标签所需chart仍须另证，不能自动推出提升图。 |
| [585核批量增阶](tits585_batch_extension/REPORT.md) | 半径二数据＋严格子类预算 | 65个8-spoke全覆盖组与12个贪心首次全覆盖组均回到旧复制结构；650/715复制已知。每组自身二步支配的子类在Δ12下总点数≤796。 | 只闭独立二步支配组的预算范围；共享spoke或新点内边互助仍开放，不外推一般批量构造。 |
| [364核binary branching](binary_branch364/terminal.json) | 必要条件MILP，**UNKNOWN** | 固定364点核D5；需匹配击中34860条唯一长度五最短路。25秒求解无可行incumbent、无不可行证明。 | 没有728点候选；固定binary模板仍未排除，一般(5,5)更未排除。 |
| [H(9)来源与逐点状态](hexagon_partial_fold_scout/REPORT.md) | 已知完整图资料＋局部结构复现 | 取得作者41699点图、逐点witness及生成函数；从未正则化fold恢复Q/H(3)，局部度公式和63个twins邻居与成品一致。 | 是已知图的输入与结构核验，不是本轮新图或新纪录；未进行几何坐标重建或全源BFS。 |
| [H(9)四序greedy及强迫闭包](hexagon_partial_fold_greedy/REPORT.md) | partial state＋单调范围排除 | 四个固定序均零新增，仍为7959 splits、280 copies、41636点旧核心。root强迫闭包使全部25074个merged fibers均禁止新增。 | 固定原S、固定280 copies时，任何真S超集都不可能，即使任意重染；允许删旧split或改copies的一般联合范围仍开放。 |
| [H(9)四region联合MILP](hexagon_partial_fold_joint/terminal.json) | partial state＋四个局部子问题终态 | 四区均由HiGHS报告Optimal、gap=0；最佳仍为41636点，目标增益0，逐点度复算通过。 | 只结束区域外固定、四个预定区域内允许联合改态/copies的试验；不排整个部分折叠族。 |

完整图核查的具体凭据分别见 [175点](pentagon175_controller/best.independent_check.json)、[192点](controller_lift192/best.independent_check.json)。单调闭包的准确前提与25074项覆盖见 [root_monotone_closure.json](hexagon_partial_fold_greedy/root_monotone_closure.json)。有限profile失败不写成整个构造族不存在；必要条件通过也不写成已有图。

## 正向依据和最后一项有限联合试验

H(9)部分折叠与任意群短词搜索的区别在于已有完整的直径充分保证：任意点线双射把关联图中“点到线”的至多五步奇路径投影成点图路径。合法逐fiber着色给出这种双射，合并未split的fiber不增距；H(3)完整blowup与规定的普通twins继续保留D≤5。因此逐fiber自由选择S/c、逐H(3)点选择非负复制数时，覆盖本身不依赖试验运气，剩余难点是联合满足逐顶点度预算并提高阶数。解除PSL₂(8)轨道常值是合法的实质参数变化，但仍必须保持同一φ二点fiber内同色。详见 [THEOREM_SCOPE_REVIEW.md](hexagon_partial_fold_scout/THEOREM_SCOPE_REVIEW.md)。

当前保存(12,5)基线42342。作者旧成品41699尚差644点才可越线；移除63个普通twins后的核心41636尚差707点。无普通twins时，需|S|+Σc_H≥8946。剩余度总数大不代表能联合装填：上述固定S/copies的单调方向已经关闭，下一步必须允许先删后增或调整copies。

本轮最后一项有限联合任务是 [hexagon_partial_fold_joint](hexagon_partial_fold_joint/regions.json)：四个预定region分别为邻绝对H(3)点、merged且邻非绝对H(3)点、无H(3)邻点的split-0、无H(3)邻点的split-1。可变generic数量依次820、820、899、901，对应可变H(3)复制数数量1、1、28、28；不是新开全域长搜索。

该任务已完成四个顺序子问题，单worker总CPU约2.19秒。四区的局部旧目标为228、183、232、353，求解器均报告相同最优值、gap=0；返回的状态均未改变旧split、颜色或copies。逐点复算确认全体度数合法、区域外状态固定，最佳核心仍为41636，距离42343目标仍差707。没有优化事后twins，也没有展开新大图或运行BFS。见 [terminal.json](hexagon_partial_fold_joint/terminal.json)。

这是四个明确局部子问题的求解终态，不能提升为一般部分折叠不存在性定理；求解器Optimal也不等于新增图成果。本轮所有列出的试验现均已结束，没有据此自动扩大区域或追加起点。

原先单调试验与已终态控制器profile不因本任务自动续跑。本报告只汇总已有证据及已完成的有限任务，不更改wiki、HTML、旧专家截点或其他代理文件。
