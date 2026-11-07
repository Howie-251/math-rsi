# N7 人口工作界更新：全局 75、76

2026-11-03。替锁构造排除了 \(n=3b+1\) 的整个共根临界层，完整有序 rank-3 signotope 的 767、777 全局人口工作上界从 \(76,77\) 降到 **75、76**。新增数学为 **unreviewed / unaccepted**，证明推导和交叉核对均在同一会话内完成。[本轮完整证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)

## 人口与加权账

| 模型 | 参数工作上界 | 代入现行容量 |
| --- | --- | --- |
| 757 | \(N_{\rm sig}(7,5,7)\le a+b-1\) | 40 |
| 766 | \(N_{\rm sig}(7,6,6)\le2b\) | 50 |
| 767 | \(Q_{\rm cap}=N_{\rm sig}(7,6,7)\le3b\) | 75 |
| 777 | \(F_{\rm cap}=N_{\rm sig}(7,7,7)=Q_{\rm cap}+1\le3b+1\) | 76 |

\(a=16,b=25\) 是既有容量输入。\(b=25\) 继承历史人工接受及其原 same-family/provisional 保证。777 的精确等式沿用独立的 R20 合法 chart 归约，先证明 767 人口界，再将其传播到 777。[历史输入](RESEARCH_SYNTHESIS_N7_20261103.md) · [R20 §4](.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)

加权工作界仍为 \(n+w\le3b+1\)，其中 \(w\) 是实际中性域 \(D\) 内同时终止和启动红五的点数。合用两项得到 \(n\le\min(3b,3b+1-w)\)。[加权工作证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

## 最后一单位人口的兑现

加权界先把 \(n=3b+1\) 压到 \(w=0\)，增强根分类只留一个非锁共根 \(z\)。全供给覆盖给实际 \(b\) 点 756 域 \(J_-\) 和实际 \(q\) 点中性红五覆盖 \(C_D\)，且每个右锁有恰一位 owner。旧根排除引理再给所有旧末根严格晚于 \(z\)。[全供给覆盖与单例纤维](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md) · [旧根排除 §1–3](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OLD_ROOT_EXCLUSION_AND_CLEAN_COMMON_ROOT_CLOSURE_20261103.md)

从 \(J_-\) 删除全部右 owner，等数换入右锁，再加共根 \(z\)。得到的实际域有 \(b+1\) 点，全部在 \(S\cup U\) 中，故无蓝五，容量迫一条实际红六。末点不晚于 \(z\)。如果末前驱在 \(S\)，这个实际末对给出不晚于 \(z\) 的旧末根，矛盾。否则末前驱是 \(U\setminus L\) 中的覆盖点。其末帽和每一个实际右供给首帽组成同端蓝四，排除它通向任何右供给端口的实际红五。因此可从 \(C_D\) 删除这个前驱，剩下 \(q-1\) 点仍击中 \(D\) 中全部红五，违反换色 756 容量。等价地，把前驱加回未删的 \(b\) 点中性核，容量迫出同一条实际红五。精确端点覆盖保证它从这个前驱到某个右供给端口，恰与两外帽构成同端禁形。[替锁构造与两类末前驱](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)

本轮结果覆盖前轮尚余的双有锁配置。前轮的 \(76,77\) 及余类记录保留为历史状态；其中满核身份和旧根排除仍是承重引理。[前轮 clean 侧更新](RESEARCH_SYNTHESIS_N7_20261103_CLEAN_CLOSURE_UPDATE.md)

本轮未进行独立数学复审、外部 Claude 调用、科研代码运行、枚举、求解或历史证书重放。[文档核验回执](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DOCUMENT_RECEIPT_20261103.md)
