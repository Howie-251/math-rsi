# 事前预测：固定p0、无p0-owner删边的四corecut原型

状态：先准备，等待独立纸面结论；不在论证未通过时执行数值。沿用actual585与旧Steiner/R2证据，不新BFS/field/GQ/源D3。

映射绑定：cached BLOCKS 的 `ports[0]` 与旧partition的首个absolute都是实际585顶点label **0**；本门 p0 是该actualvertex0，port压缩index0也恰对应它，不从index猜label。

只研究固定p0=actualvertex0：删除四条顶点不交core边，新点连八个core端点和p0，其余64个A作perfectmatching。并限定每条cut的两个端点owner都不是p0。不涉及p0-ownercuts；后者的p0-z-v-A_v三步可修原owner pair，强制matching论证不同，仍OPEN。

每core点唯一A-owner。源A-A唯一3路与cut对应；在本限定子类，删除cut u-v后，其owner pair必须成为新增Amatching边。由此matching给新根三步增加的端口均已在八端点的C9并中。每corecut两C9交恰2、并16，故要覆盖其余64A，四16masks必须互不相交且全部避p0。

**正向可推翻预测：** 放开旧fixedsigma的32条core边约束后，全部实际coreedge域中存在四个真实顶点不交的16masks，可partition P\{p0}。若完整NO，仅排本固定p0无p0-owner原型，不外推一般四cut/一般586。

**域数预测：** 2080个实际coreedges中，两个端点C均不含p0的eligible边应有1568条，作用于448个core，诱导度7。该预测只用旧cachedC和新edge-domain统计检查；若不同保实际域并纠正，不硬筛至1568，不运行原sourceD3验证。

此前只读门的core-target R2建议保留为未执行历史；root现选择更前置的port16packing门，本轮不重建core-target R2。

数值获纸面支持后仅导出全部实际coreedge/masks、按64bit exactcover求首四块或完整NO/预算UNKNOWN。保实际cut labels与顶点不交。允许旧32边参与与新边混合的cover；但全四边均来自旧sigma32的子域继承旧NO，不再求解它。任何通过仅为必要门，不生成586图/匹配/新根或coreR2。

case累计20CPU，继承只读0.800336324，所有准备/执行/输出计入；单worker、无solver/编译需求。数值进程硬cap18，软返回预留，完成即停，不p1/seed/换sigma/续timer。
