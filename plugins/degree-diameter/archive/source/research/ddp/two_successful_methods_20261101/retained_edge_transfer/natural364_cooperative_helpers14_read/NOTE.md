# 固定自然364的保边合作：旧1–13范围推进到1–14

本阶段没有378点新图。继承旧28 freeports两两距5、R2的28个13点cell划分、3276个三port R4与81900个三port+parent R3的统一零good结果，均未重跑。

14helper tree只有2总空槽，所有叶仍至少1port，因helper到任何portowner须Hdist≤4而tree径≤4。半径2中心必须4枝、第二层9叶，至少一枝有3叶，其parent/centre无port；外国叶cell只能由own≤3ports R4填满，旧zero-good立即排除。

于是14helper只剩14edge connected unicyclic H，a_h=4−degH，每个旧port用一次。先提出两可推翻的路线预测门：G1所有helper到每owner≤4；G2若leaf parent度≥3，它最多1oldport，旧R4(T)+R3(p) zero-good迫该leaf到每owner≤3。parent度2不能偷套G2。

唯一cycle c及最远cyclevertex给挂树深界4−floor(c/2)，只需c3..7。按rooted children multiset≤3、cycle-root branches≤2、cycle rotations/reflection规范，完整枚得1930个14点单环拓扑。G1排1910，G2再排20，0幸存。因此固定自然364/714、保全部oldedges、无新增oldold、max4/D5的1–14helper合作整个范围NO。

这是新范围排除，不是任意finiteH或一般378图NO，也不声称15helper存在。不生成portassign或大图；sourceBFS/旧balls/旧Hall/solver/Lean/ARIS均0。case .880238423/10CPU。original raw_ordered计数名称已修正为first-min ordered，未重跑数值；1930 canonical总数不变。

后续改为全部helper都有oldports的Petersen细分骨架，直接针对叶/无port父点造成的覆盖弱点；不是自动k15梯。具体metric与完整assignment另记，不能把本NO移过去。
