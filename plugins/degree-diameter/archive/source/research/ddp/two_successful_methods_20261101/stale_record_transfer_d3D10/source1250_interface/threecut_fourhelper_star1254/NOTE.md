# 固定两cut＋四helper星：1865完整域终态

本轮实质改规则：不撤任何cut端点的helper连接。固定源Conder1250及两旧cut(0,1)/(869,1178)，第三cut(g,h)避原四pins，全部1865条；L0=1250接0/1，L1=1251接869/1178，L2=1252接g/h，C=1253接三leaves。无orientation/oldrepair/seed，实际n1254/m1881/all3regular输入与修改契约成立。本地同scope查询未定位旧strictNO或UNKNOWN；原A/B及4536 pin-transfer各自继承，不重跑。

P1在所有1865个实际候选中得到显式长度3 walk L0–C–L1–1178，保证1178的这条路线保住。因为centre在全部配置均失败，L0最短路BFS阶段没有进入，不能把显式walk称为已测最短距离。P2“至少一例四newrootsR10全过门”被完整域反驳：1865/1865都是CENTRE首阶段失败。调用[C,L0,L1,L2]=[1865,0,0,0]，oldroot候选验收0，没有完整合法1254图。

首第三cut为原edge5=(2,6)，centre1253到oldtarget886实际最短距离11，完整路径：1253–1250–0–3–7–15–31–79–175–303–552–886。它由一条helper-star边、一条端点spoke和九条保留source边组成。FIRST_FAILURE.json/FIRST_CENTRE_FAILURE.json保存字面路径与边角色；ordinary候选BFS已包括所有混合helper路线，没有借原图距离替代候选距离。per-config阶段/首缺点在CONFIG_RESULTS.tsv，ROUTE_CLASS_SUMMARY.json保存centre eccentricity与首反例区域统计；这些不是全缺点或坏对分布。

与前轮相反，端点责任确实全部保留，仍因新centre的覆盖失败而不能完成构造。只据这一轮不能说一般四helper或全部三matchingcut都无解；本轮只关闭冻结前两cut＋全部1865第三cut的K1,3规则。叶组的候选距离保持actual普通BFS语义；不在此冒称任何G覆盖条件充分或不充分。更强纸面公式由独立paperowner核定，不修改本次数值。停止此固定域，不第四cut/另base/seed自动续。

source literal成功parse一次，sourceD10/girth等有效性继承，sourceD10 BFS/field/solver/Lean/ARIS均0。新独立n1254源码编译一次成功，无启动失败；history+prep保守.8、compile.979828、native.034756、parent.002079729及最后只读摘要.1，合计1.916663729/20CPU。0新图/参数/Lean。
