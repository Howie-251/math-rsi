# N7 的 \(t=0\) 人口层更新

2026-11-03。本轮得到空 \(I\) 的参数子类界，厘清严格交错的取等结构，并校准三条未闭合路线。新增数学均为 **unreviewed / unaccepted**。[完整证明与障碍](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)

## 新子类界

设 \(b\) 是 756 和换色 756 的共同有效容量，\(S,T\) 为母体红六的首、末点集，\(I=S\cap T\)，\(D\) 为其余点。\(U,V\) 分别为实际 \(D\) 中红五的首、末点集。若 \(I=\varnothing\)，则 \(S\cup U,T\cup V\) 各受容量 \(b\) 约束，\(D\setminus U,D\setminus V\) 各受换色容量 \(b\) 约束。相加得到
\[
n+\max(|U|,|V|)\le3b.
\]
所以 \(I=\varnothing\) 且 \(D\) 有任一实际红五时，\(n\le3b-1\)。取 \(b=25\)，这一个子类满足 \(n\le74\)。若 \(I=\varnothing\) 且 \(n=3b\)，则 \(S,D,T\) 都恰有 \(b\) 点，\(D\) 无红五。四类逐点私有红五、蓝五均在各自的实际增广域内兑现，仍需联合证明它们的端点相容性。[空 \(I\) 界与三满核](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)

## 剩余的 \(t=0\) 结构

在 \(n=3b,w=0\) 的严格交错情形，双向间隙补偿给精确端点覆盖及两侧满核。低左纤维在中间核可保留最早 owner，右侧反序，因此中间核不保证纯中性。将低锁加到对侧满核会迫实际蓝五，其首点既可能是 owner，也可能是中性末覆盖点。换锁后仍缺对新增红五的控制。满侧重核可排除严格交错的一侧满，但整个双正缺额类仍开。[实际取等与插锁障碍](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)

严格分离的条件性切分若只给共用一个根的两外帽，就只有同端蓝三加红五，总长八。无额外锁补偿的共根切分在 \(t=0\) 可允许 \(m+1\) 个覆盖角色，旧单例证明所需的等号尚未兑现。单侧空根族也可能有 \(I\ne\varnothing\)。因此下一人口层仍须处理这些根序以及空 \(I\) 的三满核。[其他根序边界](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)

## 路线校准与人口账

十点实际 767 表明 \(I=\varnothing\) 时 \(S\) 可以有红五。四个合法蓝根 chart 都有 \(w=0\) 的实际例也说明，普遍换根无法保证产生正 through。两例都缺少临界人口的共同饱和。[空 \(I\) 和合法换根反例](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)

独立混合取向的相邻双点复制若要保留所需帽，所选点集必须同时无 \(R_p,B_p\)。因此其大小至多 \(\binom{2p-4}{p-2}\)，从满 766 出发时，\(p=5\) 最多得到 \(2b+20\) 点 767。取 \(b=25\) 是 70 点，无法用现有 767 界排除 50 点 766。757 仍缺命中全部联合新蓝四的双点证书。[复制族阻断与 757 边界](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)

下一步先检验同一母体的三满核能否协调四类私有供应，再分别处理严格交错的保留 owner 和强制蓝五、严格分离同端路径所差的一顶点。反复沿用 \(t=1\) 的取等条件易停在局部最优，\(t=0\) 的共根预算与 \(I\ne\varnothing\) 的空根情形也仍需覆盖。757 的联合蓝四交换与 766 的两色端点兼容继续作为独立方向。

无条件工作链仍为 \(a+b-1,2b,3b,3b+1\)。沿用历史 \(a=16,b=25\)，得到 **40、50、75、76**。既有正 through 界保持，空 \(I\) 且 \(D\) 有红五是本轮的新 74 子类。全局 74、75 仍待证。历史容量人工接受及 same-family/provisional 保证沿用，本轮未进行独立数学复审、外部 Claude 调用、科研运行、枚举、求解或证书重放。[既有人口账](RESEARCH_SYNTHESIS_N7_20261103_7576_AUDIT_WEIGHTED_UPDATE.md) · [文档核验回执](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_DOCUMENT_RECEIPT_20261103.md)
