# N7 证明审计与加权工作界更新

2026-11-03。完整有序 rank-3 signotope 的 757、766、767、777 人口工作上界依次为 **40、50、76、77**。本轮将 767 的加权工作界改进为 \(n+w\le3b+1\)，并把下一人口临界层归结为一类增强根共根接口。新增工作证明均为 **unreviewed / unaccepted**，同会话核对和文档核验已分别记录。[既有人口界更新](RESEARCH_SYNTHESIS_N7_20261103_UPPER_BOUND_UPDATE.md)

## 证明账

| 模型 | 参数工作上界 | 代入现行容量 |
| --- | --- | --- |
| 757 | \(N_{\rm sig}(7,5,7)\le a+b-1\) | 40 |
| 766 | \(N_{\rm sig}(7,6,6)\le2b\) | 50 |
| 767 | \(Q_{\rm cap}=N_{\rm sig}(7,6,7)\le3b+1\) | 76 |
| 777 | \(F_{\rm cap}=N_{\rm sig}(7,7,7)=Q_{\rm cap}+1\le3b+2\) | 77 |

\(a=16\) 与 \(b=25\) 是既有容量输入。\(b=25\) 继承历史人工接受及原 same-family/provisional 保证。\(F_{\rm cap}=Q_{\rm cap}+1\) 来自独立的合法 chart 归约支路。该支路用完整 packet 证明删 pivot 并换色的上界方向，另以加最左蓝点兑现反向。[历史输入记录](RESEARCH_SYNTHESIS_N7_20261103.md) · [证明义务审计](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)

同会话审计覆盖了原完整低前驱补偿及其承重依赖的 15 项义务。所列范围内未发现实质缺口或循环依赖。参数无关的 M0 推导明确了两次真实换核所需的假设，另补写扩域不交和中间匹配像的计数。这样可在任意 \(w\) 的加权层使用完整双向接口，不借用旧临界层的小缺额分类。[原人口工作证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md) · [审计及推导补写](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)

## 加权下降与下一人口层

\(w\) 是实际中性域 \(D\) 内同时终止和启动红五的点数。新证明先取两核真实交集中删掉这 \(w\) 个点后的同一份中间红五匹配。增强末根族纳入前驱在 \(T\) 的全部实际红六末对，增强首根族纳入后继在 \(S\) 的全部实际红六首对。它们仍有完整根扇及头尾替换。严格交错时在两根间隙同时增广两侧实际 756 核，左侧丢失的低前驱边由右核增广偿还，右侧丢失的高后继边由左核偿还。严格分离时增强根定义直接排除污染端口。共根若已在锁集里，切分无需再扣一次根。若共根不在锁集中，至多扣一次。由此排除全部 \(t=n+w-3b\ge2\)，得到 \(n+w\le3b+1=76\)。原单向补偿的任意 \(w\) 推广保留作交叉核对。[双向补偿及增强根证明](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

因此 \(w\ge1\) 的 767 子类满足 \(n\le75\)。在全局人口临界层 \(n=3b+1\) 上，先由新加权界得到 \(w=0\)。对不在锁集的共同实际根 \(z\)，仍可在 \(z\) 两侧严格切分并作双向补偿，只额外扣掉 \(z\) 一次。共同匹配交会数至少为 \(t-1+\delta_l+\varepsilon_h-\mu\)，其中 \(\delta_l\) 数 \(I\) 内位于 \(z\) 左侧的左锁，\(\varepsilon_h\) 数 \(I\) 内位于 \(z\) 右侧的右锁。故这两种锁位置均排除。最终人口临界接口为
\[
\begin{gathered}
t=1,\qquad w=0,\qquad
\min E^+=\max F^+=z\in I\setminus\Gamma,\qquad \mu=0,\\
\Omega\cap I\subseteq(z,\infty),\qquad
\Psi\cap I\subseteq(-\infty,z)\qquad(\rho=0).
\end{gathered}
\]
这里 \(\Gamma\) 是两锁集在 \(I\) 内的并，\(\rho\) 是两锁集交集数，\(\mu\) 是中间域相对 \(b\) 的非正截断。锁的位置结论限于 \(I\) 内。现有结论未得到全局 **75、76**，人口账维持 **76、77**。[共根剩余接口](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

策略反审进一步确定了根的内在性。令 \(E_*,F_*\) 取全部实际红六相邻末对、首对的根，要求根在 \(I\)，相邻点在 \(S\cup T\)。在上述临界余类中，若有早于 \(z\) 的末根或晚于 \(z\) 的首根，其实际相邻对会触发原根族或增强根族，故 \(\min E_*=\max F_*=z\)。两个极值只依赖母体路径，纯换核、换锁集或换代表无法移动它们。下一步可直接证明临界人口与这对内在共同极值不相容，或在加入 \(z\) 后的实际 766 中间域证明红五匹配增广仍能连接两侧供给。后一路线须兑现一单位新增的实际供给，目前仍待证。

## 757 和 766 的当前结构义务

三块实际反例族给出 \(3p-2\) 点合法母体，其红 \(p\) 点 clique 中每一点都实际结束并启动 \(R_p\)。它排除了仅靠单色 through clique 和双向供应得到禁形的路线。766 的满层需要两色四满核的共同约束，并需证明指定实际端点边与同一份匹配相容。757 的双点增广须覆盖两新点一起才触发的实际 \(B_4\)。两项均未产生人口下降。[反例族与低参数前沿](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_THROUGH_CLIQUE_COUNTERFAMILY_AND_LOWER_PARAMETER_FRONTIER_20261103.md)

本轮未进行独立数学复审、外部 Claude 调用、未公开研究材料外传、科研运行、枚举、求解或历史证书重放。文档回执只记录文件核验。[文档回执](.trellis/tasks/10-19-nr7-structure-capacity/research/N7_WEIGHTED_ROOT_UPDATE_DOCUMENT_RECEIPT_20261103.md)
