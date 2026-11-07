# N7 的 75、76 审计与正 through 子类推进

2026-11-03。同会话逐项审计在 75、76 人口工作证明的承重链内未发现实质缺口或循环依赖。新加权结果将 \(w\ge1\) 的 767 子类人口工作上界降到 **74**。757、766、767、777 的无条件人口工作上界仍为 **40、50、75、76**。新增数学保持 **unreviewed / unaccepted**。[依赖审计与完整加权证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md)

## 75、76 的证明账

审计逐项覆盖 16 项义务，从参数无关 M0、加权临界归约、全实际外端口和角色覆盖取等，经过实际 owner 匹配、满 \(J_-\) 和旧根排除，到实际 \(b+1\) 点替锁域和同一条私有红五。审计也核对了无 owner、空右供给、零中间缺额及初步匹配下界为负的边界。R20 的合法 chart 归约是独立输入，先取得 767 人口界后才用它传播到 777。历史 \(b=25\) 人工接受及其 same-family/provisional 保证沿用，历史证书与 chart 证明均未在此重新认证。[最终 75、76 证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md) · [R20 §4](.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)

## 单 through 临界类

设 \(t=n+w-3b=1\)。共根证明只在中间域删去 \(C_0=U\cap V\)，两侧实际外核仍保留这些点。对删去 \(C_0\) 的中间域重新做全供给覆盖，等号仍迫单例纤维、精确中性覆盖和真实外匹配。它们恢复替锁构造所需的 \(b\) 点外核及全锁序。[加权覆盖证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md)

普通首末邻点依旧能被旧根排除。through 点已在外核内，加入它不会增大该实际域。替锁后的 \(b+1\) 点实际域迫一条红六，其末前驱若是普通点就触发旧根矛盾，若是删去 through 后的中性覆盖点就有同端红五矛盾。剩下必须以一个 through 点 \(c_-<z\) 作实际末对前驱。反序迫一个不同的 through 点 \(c_+>z\) 作实际首对后继。两侧同用一个 through 点不可能，故 \(t=1,w=1\) 的整类配置排除。[两侧 through 见证](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md)

因此 \(w=1\) 时 \(n\le3b-1\)，而 \(w\ge2\) 已由 \(n+w\le3b+1\) 给相同人口界。取 \(b=25\)，正 through 子类为 \(n\le74\)，\(n=75\) 的候选必须 \(w=0\)。无条件加权界仍是 \(n+w\le3b+1\)。目前仍待处理 \(n=3b,w=0\) 的全局人口层、\(t=1,w\ge2\) 的加权层，以及 757 和 766 的低参数改进。[既有全局人口账](RESEARCH_SYNTHESIS_N7_20261103_7576_UPDATE.md) · [低参数前沿](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_THROUGH_CLIQUE_COUNTERFAMILY_AND_LOWER_PARAMETER_FRONTIER_20261103.md)

## 下一人口层与低参数尝试

现有两项界可并写为 \(n+\mathbf1[w>0]\le3b,\ n+w\le3b+1\)。若要把全局 767 界再降一，须处理 \(n=3b,w=0\) 的完整 \(t=0\) 层，前一层的共根分类在此没有兑现。加权 \(t=1,w\ge2\) 的两条实际红五仍缺同端延长，即便另有连接两 through 点的红五，根帽给的蓝三也只将总长度推到八。

757 的第二单位需要覆盖同时用两个新点才出现的实际蓝四。766 的四满核需要在同一母体协调两色全端点图，指定的实际载体边未必可延拓到完美匹配，两色供应也未必同端。本轮未取得这两项低参数的新增整类排除或人口下降。[证明稿 §5](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md)

本轮没有独立数学复审、外部 Claude 调用、科研运行、枚举、求解或历史证书重放。[文档核验回执](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_AUDIT_WEIGHTED_DOCUMENT_RECEIPT_20261103.md)
