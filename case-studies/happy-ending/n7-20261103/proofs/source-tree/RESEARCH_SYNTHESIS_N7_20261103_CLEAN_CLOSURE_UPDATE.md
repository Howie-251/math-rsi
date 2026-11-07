# N7 共根推进：旧根排除与任一 clean 侧闭合

2026-11-03。新的同会话工作证明排除了所有 \(q=0,1\) 的 \(n=3b+1\) 共根候选，也排除了这一临界层中至少一侧 clean 的全部配置。新增数学为 **unreviewed / unaccepted**。[本轮完整证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OLD_ROOT_EXCLUSION_AND_CLEAN_COMMON_ROOT_CLOSURE_20261103.md)

上轮全供给等号给出两个实际满 \(b\) 点 756 域 \(J_-,J_+\)。实际 owner 匹配还限制所有经过 owner 的红六相邻对，其中右 owner 作首对第二点时，首点必须在共根 \(z\) 左侧。反向，左 owner 作末对前驱时，末点必须在 \(z\) 右侧。这些限制直接来自实际红五和两外帽构成的同端禁形。[全供给覆盖与 owner 匹配](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

若 \(z\) 有一个旧首根见证 \((z,t_0)\)，则 \(t_0\) 是普通点。将它加到 \(J_-\) 迫一条终于 \(t_0\) 的红六。首帽迫其首点在 \(z\) 右侧，owner 限制定位第二点。增强末根 \(z\) 的扇可把它前接到这条红六的五点前缀，产生一个 \(J_-\) 无法承接的红六末点。反向排除旧末根。两族旧根于是都避开 \(z\)，容量计数给 \(q=|D|-b\ge2\)，不依赖哪一侧满。此前按满侧数扣根的界由此得到加强。[旧根排除与根数预算](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OLD_ROOT_EXCLUSION_AND_CLEAN_COMMON_ROOT_CLOSURE_20261103.md)

将 \(z\) 加到 \(J_-\) 同样迫一条实际红六，且只能终于 \(z\)。若其前驱在 \(P_H\cup B\)，就会恢复已排除的旧末根。若前驱在 \(U\setminus L\)，它与全部右供给的帽阻止相应的跨端口红五，因而可以从精确 \(q\) 点中性覆盖中删去。剩下 \(q-1\) 个点仍覆盖全部红五，违反容量。故该实际末对的前驱必为右 owner。反向，\(J_+\cup\{z\}\) 迫一个左 owner 作实际首对后继。任一侧 clean 时缺少所需 owner，整个配置排除，包括 clean 但缺额为正的情形。[clean 侧闭合](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OLD_ROOT_EXCLUSION_AND_CLEAN_COMMON_ROOT_CLOSURE_20261103.md)

剩余候选须 \(q\ge2\)，且两侧都带单例锁纤维。实际见证包括末对 \((b_0,z)\)、首对 \((z,a_0)\)，其锁位置满足 \(\psi(b_0)<b_0<z<a_0<\omega(a_0)\)。这些是双有锁余类的约束，该类仍待排除。

以 \(b=25\) 计，至少一侧 clean 的 767 子类满足 \(n\le3b=75\)。全局加权工作界仍为 \(n+w\le76\)，757、766、767、777 的无条件人口工作上界仍为 **40、50、76、77**。全局 **75、76** 尚未得到。[既有人口账](RESEARCH_SYNTHESIS_N7_20261103_COMMON_ROOT_UPDATE.md)

本轮未调用外部 Claude，未进行独立数学复审、科研运行、枚举、求解或证书重放。[文档核验回执](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OLD_ROOT_CLEAN_CLOSURE_DOCUMENT_RECEIPT_20261103.md)
