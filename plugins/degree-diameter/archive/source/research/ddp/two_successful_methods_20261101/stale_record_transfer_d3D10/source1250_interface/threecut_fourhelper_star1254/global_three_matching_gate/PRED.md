# 全部三matchingcuts／四helper星：精确weighted-lastcut门

独立paper已支持：centre到oldtarget精确为2+d_G(全部6端点,t)；leaf i精确为min(1+d_G(Pi,t),3+d_G(othergroups,t))。这里不是逐个把删边T的group球换成G，而是整体weighted min的lastcut等式。actualcandidate oldold仍须检验。

冻结anchor原edge0=(0,1)，其余e1<e2与anchor及彼此顶点不交。继承source edge-transitive且star leaves可置换，anchored全域代表此固定source所有三matchingcut/整cut分leaf/K1,3拓扑；不代表所有四helper拓扑或一般3D10。预计1870 eligibleother、1743779 matchingpairs，按actualliteral核并执行实际域。

P1：已存固定域首例third(2,6)+second(869,1178)的centre坏点886，在sourceR8六端点并集仍缺；只做新DP表对照，不重跑此旧候选BFS。P2（可推翻）：全matching域至少一组通过centre及全部3leaf的exactR10覆盖门；它仍不保证oldold。

仅source literal parse1，closedballsR0..R9用bitset邻接递推，保存所有1250roots的R7/R8/R9及schema。这是新覆盖query，不是旧D10 sourcevalidity。每edge端点union E^k，centre条件E0^8|E1^8|E2^8=all；leaf i条件Ei^9|Ej^7|Ek^7=all。按centre→L0→L1→L2，到首失败；保存完整stagecounts、首缺点、cursor与操作数，不总坏对评分。

四门全过才生成actual1254graph，普通BFS绑4newroots，再所有1250oldroots到首fail/真hit。firstfullhit保存完整edges/recipe/allrootstats并停交fresh，未接受前0图/参数/Lean；无hit完整域NO仅是此源3matchingcuts/K1,3。budget未完UNKNOWN。单compile/run，累计starline cap30CPU继承fixed1.916663729＋newprep.5＋实际compile/parentchild，不reset，不换anchor/source/拓扑/seed。0oldD10验证BFS/field/solver/Lean/ARIS。
