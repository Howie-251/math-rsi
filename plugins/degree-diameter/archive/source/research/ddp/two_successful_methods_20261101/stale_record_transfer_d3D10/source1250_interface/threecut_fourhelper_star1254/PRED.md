# 三cut四helper K1,3：保留所有端点覆盖责任

Pre-run：不重跑旧A、5614个旧B或新4536的11178 pin-transfer。限定canonical目标3D10两节点与本source接口的历史查询未定位同一规则的strictNO或UNKNOWN；这只是本地未定位，不称无人研究。

固定源Conder1250，两旧cut(0,1)/(869,1178)，第三旧边(g,h)顶点避开前四pins。删3cuts；L0=1250接0,1，L1=1251接869,1178，L2=1252接g,h；C=1253连三leaf。无repair、无orientation、新旧端点均保helper spoke。n1254/m1881/cubic，第三边预测1865，按实际literal完整域运行。

P1：L0–C–L1–1178是实际长度3 walk，故旧A缺点1178不会因撤spoke丢失。逐候选核此实际短路；若L0进入BFS再报告精确距离，不把显式walk误称已测最短路。
P2（可反驳）：至少一个第三边能让4newroots全部R10覆盖。它不是oldold保证。实际ordinary BFS按C→L0→L1→L2到首失败，4pass才逐1250oldroots至首fail/真全图hit。不借原G的leaf球，不作候选传递性归全。

首hit保存1254/1881全边表、literal生成recipe/allrootstats，交fresh后才计图；全1865失败仅关此固定两cut/四helper星域。保存每配置阶段及首失败pair实际最短路/边角色，不做总坏对评分。预算独立case20CPU含history/prep/compile/parentchild，history+新prep保守0.8CPU；一次sourceparse仅输入绑定，0原sourceD10/BFS/field/solver/Lean/ARIS。不第四cut/新base/seed自动续。
