# Conder1250：三 cut／四 helper 星形的范围与路线攻击

本次仅只读既有 source1250 接口、旧 two-helper 证明/节点及固定 object4536 transfer 终态范围；未读取源边表、生成候选、运行 BFS/solver/Lean/ARIS。有限本地检索未定位同一 source 的 1254／三 matching-cut／K1,3 helper 星形 strict NO。此结论仅为未定位旧同域排除，不是全球检索。

## 冻结规则及旧结论边界

原 source G 是实际 ConderC1250.2，1250/1875、全三度、published D10，均继承。固定两条 cut {0,1}、{869,1178}；第三条遍历已绑定的 1865 条避开这四端点的源边。三条 cut 顶点互斥，记端点对 P1,P2,P3。新增三叶 l1,l2,l3 和中心 c；每叶接本条 cut 的两个端点和 c，中心仅接三叶。所有六个旧端点保留为 helper pins，不撤 pin、不加旧旧 repair、不改 P4 规则。

度账为 n=1254、m=1875−3+6+3=1881，全部三度。第三边全集只闭合这个固定前两 cut 的子域；源 edge-transitivity 不能自动把所有三 cut 集合都归到这两个指定 cut。

旧 5614 个 B 对象只含两 cut、两个相邻 helper；旧 11178 终态只含固定 object4536、保护 x–1178 的 pin-transfer/旧旧 repair。两者均不是本架构。旧 B 全 NO 不给本架构自动的距离支配：第三叶新增了从另两叶经中心到第三对旧端点的三步通道，旧 B 没有这条通道。把第三 cut 加回并删除两个 helper，也不能据此构造一个到所有旧点距离不增的映射。

旧 B 的失败仍可成为必要义务，而非全域否定：同一下述 last-cut 论证在权1/2时也成立。若对应前两 cut 的 own-pair B 在目标 t 上失败，则它在 source 中已有 d(P1,t)>9、d(P2,t)>8；新 l1 要修复 t，只能由第三对提供 d(P3,t)≤7。这里应使用对应 own-pair B，不能把 object4536 的混合 pin 分配或其目标1058直接当同一根。

## 修正：整体 weighted min 可以精确换回 source G

令 T=G−三条 cut。直接按 helper 树分解可得，对任意旧点 t，

`d_new(li,t)=min(1+d_T(Pi,t), 3+d_T(P\Pi,t))`，

`d_new(c,t)=2+d_T(P,t)`，其中 P=P1∪P2∪P3。

各个 d_T(Pi,t) 一般不能单独换成 d_G(Pi,t)。但以此断言整个 weighted min 不能换，是过强限制；root 的 weighted-lastcut 引理成立，精确结论是

`d_new(li,t)=min(1+d_G(Pi,t), 3+d_G(P\Pi,t))`，

`d_new(c,t)=2+d_G(P,t)`。

证明：给 group i 权1，其余两组权3。T⊂G 先给 weighted-T 最小值≥weighted-G 最小值。取达到 weighted-G 最小值的起始 pin p∈Pj 及 G 路径。若不经过任何 cut，直接得到新图路线。否则取最后一条 cut，设它属 group k，原路径到该 cut 上游端的前缀长 L，越过此边后接无 cut 尾段。新图直接从 li 沿 helper 树到该 cut 下游 pin，代价 wk，再接该尾段。只需 wk≤wj+L+1。唯一可能权升2的情形是 j=i、k≠i；三 cut 的端点互斥使 L≥1，恰好足够。其余情形权不升。这给反向不等式。中心所有 pin 权同为2，证明更直接。

因此四个新根 R10 的精确 source 条件为：每叶 `R9_G(Pi)∪R7_G(P\Pi)=V(G)`，中心 `R8_G(P)=V(G)`。可以使用已绑定的 source 距离支持实现它们；无需为此反复计算删边 T 的每个球。该化简不表示每个单独球保持不变，也不表示 source 本身重新验收。

## 四个新根全过仍不代替旧旧距离

对两个旧点 u,v，新图距离精确为以下路线的最小值：留在 T 中的 d_T(u,v)；经同一叶的 `d_T(u,Pi)+2+d_T(Pi,v)`；经两个不同叶/中心的 `d_T(u,Pi)+4+d_T(Pj,v)`（i≠j）。最短路不必重复经过中心，所以该菜单完整。

这里留在旧点中的 T 路线不能无条件替成 G 路线：被删 cut 的单边路线长度1现需经本叶长度2。源距离10的旧点对若失去所有≤10替代路线，仍可变成11，即使四个新根均已覆盖；四根覆盖没有逐旧点对的闭包推论。因此一条 branch 保住某根、乃至四个新根全过，都只进入下一验收阶段。完整候选还需全部旧根普通 BFS 或另一份完整旧旧证明；这不是要求重跑原 source D10。

本文件不宣称现已有这种旧旧反例，也不继承单边细分 A 的全局 D11 上界给整个新架构。实际失败点、路径和最终直径由新候选实测给出。若 1865 个第三边完整失败，只是固定这两 cut 的星形规则 NO；预算未完为 UNKNOWN。0新图/参数/Lean计数。

依据：`source1250_interface/NOTE.md`；旧 `d3_D10_conder1250_edge_insertions/ANALYSIS_PROOF.md`；Wiki `ddp-conder1250-edge-subdivision-two-cut-helper-family-20261027` 与 `ddp-stale-d3d10-conder1250-frozen4536-protected1178-thirdcut-pintransfer-complete-no-20261101`。未修改这些历史文件。
