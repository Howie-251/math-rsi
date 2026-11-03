# 固定15552源的 full-vertex full-N clone packing：只读接口

状态：READ_INTERFACE_CONFIRMED，未运行新packing、solver、source/field/BFS、Lean或外审。旧16416接受证据只读继承，不修改其代码、图、回执或专家包。保守只读准备计费2/3CPU秒，覆盖未单独计时的小文件阅读与写出；不冒作全量实测CPU。

## 1. 原构造假设核实，以及 false-twin 术语边界

实际生成器为 `../degree16_plane864/produce.py`。它一次读取原作者简单邻接行 `research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt`，对每个 center 直接使用 `neighbors=adj[c]`，只添加 new_j–w（w∈该旧邻域），保留全部116316条旧边，0 new–new边。

所以“每个新点复制原15552源中中心 v 的完整简单开邻域 N_G(v)”正确。它不复制 loop-completed 关系、不把 virtual-self 补回，也不随着已加入clone更新邻域。

严格术语须区分：这可称**冻结源的完整邻域克隆**。若旧中心 v 邻接另一个被选中心 u，则最终旧 v 会得到 clone_u 这个额外新邻点，而 clone_v 没有任何新邻点；所以 clone_v 与旧 v **未必在最终图中仍是 false twins**。这一术语限制不影响实际 full-N 规则、度数模型或距离引理。不同复制点若中心相同，则它们彼此是最终图的 false twins。

当前中心标签逐 j 为

    i=j//27, r=j%27,
    offset=(r%3)+9*((r//3)%3)+27*(r//9),
    center=81*I32[i]+offset,  newlabel=15552+j。

这对应 W={x1=0} 的27个 offset，I32 的完整字面表在 accepted `PARAMETERS.json` 与 `controller_pack32_gate/SELECTED_BLOCKS.json`。新 Lean Definitions 的 `center_label`、`label_new`给同一公式；graph 直接是 `FullNeighborhoodClones.graph F3Graph15552.graph center`。accepted独验的 `ALL864_ACTUAL_ROLE_BINDINGS.tsv` 逐行给 actual old center、newlabel、完整旧simpleN和 full_N_equal；本任务仅读其schema及首行，不重新逐行校验已接受数据。

## 2. 整个 W27 与 disjoint-controller-targets 仅为充分选择

先前选择完整 W27，是为了用五个实际 kernel 的横截性一次证明同层27个邻域不交；I32 的五目标 T(a) 两两不交，再保证不同所选层的 pins 不交。两者提供方便的 load≤1 证书。

它们不是 full-N cloning 必须满足的条件。旧 `INDEPENDENT_PLANE_INTERFACE_NOTE.md` 已明确保留 point-level、partial-plane、不同 center sets 和 degree14点load2的可能；不能把这个保留范围说成新的未发现结构。

已存在的 controller 门是 `CONTROL_PACKING_RESULT.json` 的 FOUND31（未穷尽、非最优）和 `controller_pack32_gate/RESULT.json` 的 zero-objective FOUND_GE32（不是max32证明）。其变量是192个 whole-W27 blocks、约束是192个 completed-target rows。它们都不是下面的15552个旧中心变量问题。当前只读 source-gate 目录、原始scope及定向canonical检索，未定位该 whole-source 非整层模型已执行的 strictNO、UNKNOWN或实际 packing结果；“未定位”不作全repo或文献不存在证明。

## 3. cap16 的精确度数条件

本次仅提出“一旧中心最多复制一次”的二元模型。对每个旧顶点 v∈V(G)，设 x_v∈{0,1}；选中后新clone只有 N_G(v) 这些旧邻点。令

    L(w)=sum_{v : G.Adj(w,v)} x_v。

既有 `FullNeighborhoodClones.degree_old` 与 `degree_new` 给精确等式

    deg_final(old w)=deg_G(w)+L(w),
    deg_final(clone_v)=deg_G(v)。

源实际degree14:648、degree15:14904，全部新clone度14/15，因此最终 maxdegree≤16 **当且仅当**

    对全部15552个旧 w，L(w)≤16−deg_G(w)。

即旧degree14点的容量为2，旧degree15点容量为1。矩阵就是冻结旧simple邻接 incidence A_G，二元可行域 `A_G x ≤ 16−d_G`；目标候选是 `sum x > 864`。这一步不需要 center 独立，不需要所有clone邻域两两不交，也不要求整27-plane或target-controller集合不交。

accepted I32×W27 的864点是此模型的已知可行选择：实际12924个旧pins各load1、2628个旧点load0，已独验并形式化接受。本任务不重新校验该incumbent。若后续做新模型，应允许替换此864集合，而不只是固定它后追加一个 I33 whole-plane；后者是另一个更窄模型。此次没有增加多重复制变量或第二模板。

## 4. 真 Walk D4 与前缀对任意中心集合适用

此处只引用并检查既有 generic 引理，不记作新定理。实际源最小度14，故无孤立点；其 unconditional `F3Graph15552FullExact` 已给真实 Walk≤4 与非D3。对任意有限 center list（不要求 W、target-disjoint 或独立）：

* 源中心间旧路径长度≥2时，仅替换两端，内部仍全为旧点，长度不增。
* 两中心相邻时，两clone可用 `clone_v–old w–old v–clone_w` 三步；因此无需中心独立，且3≤4。
* 两不同角色中心相同时，取一个旧邻点，以两步相连；自己的clone到旧中心也用此两步。

这正是缓存 `FullNeighborhoodClones.diameterAtMost` 的 D≥3、source-no-isolated 接口。本新模型若通过度数条件，D4上界无需重新证明 field/rank 或逐rootBFS；所有上述 Walk 内部仅使用旧源，任意clone前缀亦保持≤4。实际新字面图仍须另绑定到选择与旧N，不以公式可行冒作已产图。

collapse 把每clone送回旧中心，是graph homomorphism；旧图又完整嵌入。故 `old_walk_bound_iff` 保持每个旧旧点对的全部Walk长度界，源的非D3继承到任意这些克隆图。所以该构造在cap16可行时，真实直径仍恰4。

## 5. 已读实际证据及下一决策边界

可直接复用的本地输入位置（均为项目原相对路径；本门不复制或再绑定）是：

* **旧simple adjacency：** `research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt`。每行首列为旧vertex label，其余列就是已删virtual-self的完整旧N；已接受degree14/15从该literal继承。此处未定位另一份必要的 standalone sparse-adj cache；不需要由affine/field重新生成。
* **冻结864个实际center labels：** `degree16_plane864/PARAMETERS.json` 的 `source_center_labels`，顺序即新role j；`selected_controller_labels` 与 `ordered_offsets` 保留其原I32/W27来源。完整role→center decoder见第1节，亦由 `formalization/EXTERNAL_BINDING_RESULT.json` 接到同一typed公式。
* **每role完整旧N：** producer `degree16_plane864/ALL864_ROLE_BINDINGS.tsv` 的 `source_center_label`、`frozen_full_source_N`；独验 `degree16_plane864/independent_acceptance/ALL864_ACTUAL_ROLE_BINDINGS.tsv` 的 `old_center_label`、`actual_old_simple_neighbors`。后者还含实际degree14/15、actual edgecount、full_N_equal与old_center_excluded。两者都能直接作为旧clone删除时的邻域模板。
* **旧degree/现load/threshold：** accepted `PARAMETERS.json` 给源degree14:648/15:14904；`RESULT.json` 给现oldload0:2628/1:12924。未定位独立保存的逐vertex load/threshold数组。需要时，逐旧vertex的d_G就是原literal行邻点数，L0(w)是上述864个冻结N中出现次数；因此无需读新16416完整边表、球、field或源验证即可形成精确 `R(w)=16−d_G(w)−L0(w)`。

对root拟定的有限后续操作，可直接用这些同源数据作必要且充分的度数判定：append旧中心v要求 `1_N(v)(w)≤R(w)` 全部w；删除旧clone j后加中心v,t要求 `1_N(v)(w)+1_N(t)(w)≤R(w)+1_N(center_j)(w)` 全部w。本门二元域还须保持新的中心选择符合未选/互异条件；这些公式仅记录接口，**未测试任何append或swap**。这也不是把源改为16416再复制其已扩大的邻域：所有 N 仍冻结在原15552源。

未定位名为 `FINAL_PROOF.md` 的plane864独立文件；实际证明入口是 accepted `degree16_plane864/PROOF.md`、`independent_acceptance/NOTE.md`、`formalization/FINAL.json`、`ROOT_FULL_LEAN_DISPOSITION.json`，以及实际新 Definitions/Inputs/Exact/Audit。原 producer `RESULT.json` 的当时 pending 状态是历史快照，不能覆盖随后 root/fresh/kernel 已接受事实。

该只读门确认完整旧N incidence 模型成立，未确认存在>864的新选择。任何实际新packing只在root另行授权后开始；本次不派I33、非整层search、solver或图，不改变source/数学/Lean计数。650若有正向候选优先其验收。本门STOP。
