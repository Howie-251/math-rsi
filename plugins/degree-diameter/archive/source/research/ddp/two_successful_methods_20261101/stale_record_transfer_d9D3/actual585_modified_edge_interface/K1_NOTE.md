# 固定p0的k=1原型：必要端口packing完整NO

本批完整排除固定 actual p0=vertex0、恰一条cut含p0-owner的四corecut规则：删四条不交core边，新根连八core端点及p0，其他64绝对点作perfectmatching。结论只用必要端口覆盖失败，不生成586图，不声称检查了core损伤或旧旧点对。

## 继承的纸面接口

[OWNER_P0_NEXT_INTERFACE](OWNER_P0_NEXT_INTERFACE.md) 与 [K1_MATCHING_INTERFACE_PAPER](K1_MATCHING_INTERFACE_PAPER.md) 证明：唯一p0-owner cut的另一owner记a，四个16-mask必须两两不交、并大小64，唯一遗漏绝对点t必须与a配对，另外三cut的ownerpairs强制匹配。三强制对加a-t涉及八个不同的非p0绝对点，剩56点可完配；这只是必要接口，没有图D3保证。

## 实际域与完整性

复用旧ALL2080与ELIGIBLE输入，导出64条owner-p0 cut、1568条far cut，不重源、几何、k0或旧sigma搜索。65位mask严格沿原port索引：旧64位mask左移1，bit0=actualvertex0；owner旧表的无p0 union是15位，再补bit0成16位。保全部far边，包括旧sigma单边，因为本轮含一owner的新k1组合不是旧k0四far子域。

对每个owner，初始有49个未覆盖端口，需三条far16覆盖48个、恰留一个。MRV对最受限端口完整分支：用每条可用far边覆盖它，或将它作为唯一漏点；若已选三far仍未使用漏点分支，则剩余单点自动作为t。actual八core标签同时检查互异。没有失败状态memo，避免把相同port并但不同core pin的core覆盖混为一谈。

[实际DOMAIN](K1_DOMAIN.json) 保留64owner完整标签/65位mask与far表引用；[64个owner阶段](K1_OWNER_DOMAIN_STAGES.tsv) 给逐域完整终态。全部 **64/64** owner域完成，共 **3200 DFS节点**，没有预算中断，**必要端口packing=0**。

事前P1“至少存在一个k1端口packing”被反驳。P2“至少一个端口packing同时满足新根core覆盖”**未进入、未检验**，不能误写为core失败。因为没有端口packing，源literal parse=0、新core-target R2 support build=0，所有core阶段行只有表头。没有通过微调某个missing t或换p0继续。

## 结果与成本

[预言](K1_PRED.md)、[唯一数值源码](K1_once.py)、[结果](K1_RESULT.json)、[终态](K1_TERMINAL.json)、[packing/core阶段](K1_ALL_PACKING_CORE_STAGES.tsv)。scope-reader独立只读了域、omit分支、标签和core阶段接口，没有重复数值。

actual进程 **0.355276196 CPU秒**，继承case1.881081201，新增准备0.20及独立scope-reader0.30，累计 **2.736357397 / 20秒**。单worker，进程已exit0，无活跃句柄。0BFS、0field、0sourceD3验收、0core支持、0剩56匹配、0图、0solver/Lean/外审。

本数值NO仅为fixedp0=actual0的k1子域；k0的既有数值NO和k>=2的独立纸面结论由root统一处置，不篡改其历史记录，也不借未核的源传递性推广至其他p0。一般585改边、其他repair、其他新根pin形状与一般(9,3)仍不在本结论内。按授权STOP。
