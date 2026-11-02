# 全三matchingcuts／四helper星：完整源内规则NO

这是根据lastcut精确公式新开的全域门，不是固定1865域的timer续算。固定anchor edge0=(0,1)，其他与anchor不交的原边实际1870；取e1<e2且二者顶点不交，实际matchingpairs1743779。继承原source edge-transitive与star叶可置换，anchored域覆盖此固定source全部三matchingcut/整cut端点归一leaf/四helper K1,3规则；不覆盖其他四helper拓扑，也不排一般3D10。

sourceparse一次，仅绑定1250/1875/simple3regular及实际edge labels。closedballsR0..R9用邻接bitset递推，是新覆盖问题数据，不跑sourceD10验证BFS。保存全部1250roots的R7/R8/R9至SOURCE_R7_R8_R9.bits（600000bytes），BALL_SCHEMA.json定义radius7/8/9→root0..1249→20个uint64 little-endian，末word仅34位。DP675000次wordOR、edgeunion112500次wordOR；实际cover访问24513703 words。已存固定样例cuts[0,5,1515]的target886确实不在sourceR8六端点并集中，P1得到支持，未重跑旧候选BFS。

精确cover门：centre用三个edge端点R8并；leaf i用本edgeR9与另外两edgeR7并。依次centre/L0/L1/L2。完整1743779/1743779配置全部centre失败，stagecalls与firstfails均[1743779,0,0,0]，allfourpass0。P2存在四新根cover配置被反驳；leaf阶段是NOT_ENTERED，不能称其各自失败。新候选生成/actual新根BFS/旧根候选验收均0。STAGE_FIRST_FAILURES.json存首缺点，PER_FIRST_EDGE_STAGE_COUNTS.tsv存每e1完整阶段计数，cursor=-1/-1，无预算截断。

本结论只需已证centre公式；整体leaf weighted-lastcut公式也被独立paper支持，但本轮未用到leaf门的正/负数值。不能把d_T(Pi,t)每项独立换成d_G(Pi,t)；对应精确关系是整体min(1+ownG,3+othersG)。oldold距离不由这些新根条件自动保证；本批因centre全失败根本未进入oldold。

停止此固定source的整个三matchingcuts/K1,3规则，无换source/anchor/seed/拓扑或第四cut自动续。独立compile一次、native一次均成功；继承fixed1.916663729，新prep.5、compile1.052862、native.039517、parent.002197244、只读摘要.1，总starline3.611239973/30CPU。sourceD10验证BFS/field/solver/Lean/ARIS均0；0新图/参数/Lean。原1865候选BFS的1.916663729费用完整继承，没有reset。
