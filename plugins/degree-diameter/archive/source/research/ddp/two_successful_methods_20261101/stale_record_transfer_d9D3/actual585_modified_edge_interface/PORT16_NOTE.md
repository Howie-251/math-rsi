# 固定p0、owner-avoiding四corecut原型：完整必要门NO

结论严格限定于实际585源、p0为actualvertex **0**、四条顶点不交旧corecuts的所有endpoint owner都不是p0、新点连接八core端点及p0、其余64个绝对点任意perfectmatching。这一原型不能得到586点cap9/D3图。含p0-owner切边的原型仍OPEN；不借未经绑定的传递性推广到其他固定port，也不声称一般(9,3)不可增点。

## 为何新的端口门是必要条件

[独立纸面论证](SOURCE585_FOURCUT_PAPER.md) 继承actual源的唯一A-owner、A间唯一长度3路线与Steiner3-(65,9,1)。每条corecut u-v会毁掉owner(u)-u-v-owner(v)这条唯一3路。因两个owner都非p0，through-newstar路线至少4步；其他新增A-A matching也不能构成替代长度<=3路。因此最终matching被强迫包含该owner pair。

新根到A的长度<=3旧腿覆盖是八个core端点的C9并，再加p0。由强迫matching，新根经新增A-A边三步到达的partner已在另一cut端点的C9里，不能新增端口覆盖。每个cut两个C9恰交于两个owner，故其并为16。四个16并加p0要覆盖65个端口，必须四块不相交、每块不含p0，并覆盖其余64个A。

这里owner避p0限定不可去掉：若某cut的owner是p0，p0-z-v-owner(v)可以修复旧ownerpair，另一个owner的matching不再被迫，可能额外扩充新根A覆盖。旧readgate的core-target R2问题保留为未执行历史；本轮没有重建它。

## 实际完整输入域

程序只将原literal作为新模型输入parse一次，与旧BLOCKS作有限字面绑定，没有source D3/BFS/field/GQ重验。

* 2080条实际旧core边全部导出，各条C9交2、并16。
* 64条边有p0-owner；512条的C-union包含p0。这些边不在本必要分割域。
* eligible **1568**条，涉及448个core顶点，诱导度均为7；root的域数预测得到支持。
* cached `ports[0]` 映射到actual vertex0；mask位0..63的actual port标签完整保存，未把portindex当通用图标签。

[全部2080边绑定](PORT16_ALL2080_CORE_EDGE_BINDINGS.tsv) 保留真实端点、两个owner、C交并大小、p0标志、旧sigma标志与实际port labels。[完整eligible域](PORT16_ELIGIBLE_EDGES.json) 保留1568条实际边与64位mask。

## 搜索与旧排除如何合并

使用未覆盖端口最少候选的exactcover DFS；每条选边须mask完全包含于剩余端口，且两个actualcore标签不与已有cuts重合。每选一块覆盖16点，四块须恰覆盖64。

旧fixedsigma32条边全部保留，所以任意新旧混合组合都在域中。仅“完整四块都来自旧sigma32”的子域继承旧完整NO，不再单独求解；若搜索前三条均为旧sigma，最后一条被要求非sigma。实际该最后层过滤访问数为0，不是重新执行旧32边exactcover。

新/混合域共 **3697 DFS节点**，完整结束、0预算中断、0命中。3697个失败状态已记录计数，memo hit0。最大访问partial depth为2：这是exactcover的搜索深度，**不是声称求出了全1568边的最大packing数**。mask互斥时显式顶点互斥未额外拒绝任何边，仍保留该检查。所有未覆盖点的候选已完整考虑；结合旧四sigma子域NO，完整关闭本固定p0 owner-avoiding原型的必要条件。

## 成本、产物与停止

[事前PRED](PRED.md)、[唯一数值源码](port16_packing_once.py)、[实际结果](PORT16_RESULT.json)、[终态](PORT16_TERMINAL.json)。固定源和旧scope读取仍在 `SOURCE585_READ_GATE.{md,json}` 保留。

本轮actual进程 **0.880744877 CPU秒**；沿用read累计0.800336324，新增准备预留0.20，case累计 **1.881081201 / 20秒**。单worker，全部进程终态。新增匹配、586完整图、新根/旧根BFS、core-target R2、field、GQ、solver、外审、Lean均为0，新增图0。

完成即停止；不更换p0、不加入p0-ownercuts、不续sigma/匹配/删边参数。任何改变这一受限规则的下一问题由root另定。
