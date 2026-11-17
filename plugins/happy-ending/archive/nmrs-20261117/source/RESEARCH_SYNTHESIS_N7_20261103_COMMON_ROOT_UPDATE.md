# N7 共根层更新：单例锁纤维与饱和中性核

2026-11-03。新证明在 \(n=3b+1\) 的共根临界层排除了多 owner 纤维以及锁序不合的配置，并构造出一个实际 \(b\) 点中性核，向所有外点提供逐点红五。新增数学为 **unreviewed / unaccepted**，推导和交叉核对均属同会话。[共根全供给证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

## 本轮排除与共同供应

上轮的加权界 \(n+w\le3b+1\) 使 \(n=3b+1\) 的候选必须 \(w=0\)。该层尚余内在共根 \(\min E_*=\max F_*=z\)，共根避开两锁集，\(I\) 内左锁全在 \(z\) 右，\(I\) 内右锁全在 \(z\) 左。新证明沿 \(z\) 严格切分，收集两侧全部实际红六相邻对的普通端口 \(L,R\)。任何从 \(L\) 到 \(R\) 的实际红五都与两外帽给出的同端蓝四形成 weak7。因此，删掉中间源容器的非 \(L\) 角色及末容器的非 \(R\) 角色会击中全部中间红五。[加权界与共根接口](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md) · [全路径覆盖](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

容量迫使角色覆盖数、其实际点像及端口下界同时取等。覆盖不能用两种角色重复计同一个点。若左 owner 也是左核内红五末点，或右 owner 也是右核内红五首点，便会重复计点。排除这两个交集后，容器取等迫每锁恰有一位 owner。全类排除针对任何一侧的多 owner 纤维，覆盖所用的端口集取自全部实际路径。[单例纤维定理](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

删点恰去掉全部 owner 与 \(D\) 内的 \(q\) 个覆盖点，留下实际 \(b\) 点换色 756 中性核 \(K\subseteq D\)。同一个 \(K\) 对任意外点 \(x\) 都满足，\(K\cup\{x\}\) 无红六，因而容量迫一条使用 \(x\) 的红五。取 \(x=z\) 得到共根的新红五。若 \(z\) 在该红五内部，它的两相邻点必须在每一对实际入根前驱、出根后继的外侧。这个位置条件仍不足以固定新红五的首末供给。[饱和中性核与插点限制](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

## 全锁序与 owner 的实际支撑

在 \(K\cup A_H\) 中，全部实际红五只能由左 owner 指向 \(K\cap R\)，容量迫一份饱和左 owner 的匹配。反序得到 \(K\cap L\) 到右 owner 的饱和匹配。结合已经饱和全部外端口的实际外匹配，每个左锁 \(\omega\) 得到不同的右根 \(s_\omega\)，满足 \(z<s_\omega<\omega\)。每个右锁 \(\psi\) 得到不同的左根 \(r_\psi\)，满足 \(\psi<r_\psi<z\)。因此全部左锁都在 \(z\) 右，全部右锁都在 \(z\) 左。对任一阈值，能够配给相应锁的严格在内侧根数不能少于锁数。反向位置或违反这项次序预算的整个配置类排除。这里包括 \(I\) 外的锁。[owner 匹配与全锁序](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

## 满侧的根数预算

记 \(f_{\rm full}\) 为缺额零的侧数。两旧根族由容量各自达到 \(1+\alpha\)、\(1+\beta\) 的根数下界。右满侧的实际纯前供迫共根 \(z\) 不属于旧首根族，左满侧反序排除 \(z\) 属于旧末根族。两族都在 \(I\setminus\Gamma\)，且至多共用 \(z\)，因此根数上界随每一个满侧各减一，给 \(q\ge f_{\rm full}\)。这排除 \(q=0\) 且至少一侧满，以及双满且 \(q=1\) 的整类配置。双满且 \(q\ge2\)、双正缺额且 \(q=0\) 仍开。无 owner 本身不保证侧满。[满侧根数定理](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

## 证明边界与人口账

11 点实际反例中，八点中性核对所有外点都有逐点红五，\(K\cup\{z\}\) 甚至同时有终于和始于 \(z\) 的红五，仍没有跨两侧的红五。该例的内在根族为空，且未达到全局 \(b=25\) 容量饱和。符合严格锁序的单例 owner 及无 owner 类仍开。剩余临界类需要把 \(K\cup\{z\}\) 的实际新红五与全部外端口相容地接起来，或直接排除临界人口下的内在共根。一般的匹配交换和经 \(z\) 的直接路径拼接都缺少这项实际兼容性。[策略反例与剩余接口](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

以既有 \(a=16,b=25\) 计，757、766、767、777 的人口工作上界仍为 **40、50、76、77**。加权工作界仍为 \(n+w\le76\)，其 \(w\ge1\) 子类满足 \(n\le75\)。全局 767、777 的 **75、76** 尚未得到。\(b=25\) 继承历史人工接受及其原 same-family/provisional 保证。[既有人口账](RESEARCH_SYNTHESIS_N7_20261103_AUDIT_AND_WEIGHTED_UPDATE.md)

本轮未运行外部 Claude、科研代码、枚举、求解或历史证书重放，未进行独立数学复审。[文档回执](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_CORE_DOCUMENT_RECEIPT_20261103.md)
