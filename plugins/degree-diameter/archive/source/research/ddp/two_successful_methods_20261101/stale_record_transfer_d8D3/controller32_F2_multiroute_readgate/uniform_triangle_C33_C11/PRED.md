# pre-run：三角单元C33 × F2³固定ARC连接

上一C30插两点族已被controller普通路线容量关闭，所有chart调参都无用。改生成拓扑，不再m32插点/矩阵梯。以11个三角单元为controller（33顶点）是本三型模板超过253的最小量：3m*8>253要求m≥11。只试m11，不m12梯。

controller labels11*t+j，t0/1/2,j∈C11。A:0j→1j→2j→0(j+p)；B:0j→2j,1j→0(j+q),2j→1(j+r)。均为permutations，bar01/23按A/Ainv/B/Binv。p/q/r非零恰保证四邻点不同/no loops；共同phase平移为automorphism，unit scaling固定p=1，全部q,r1..10共100代表。不是32点Cayleygroup，两inversepair32障碍不套这里。

固定原ARC chart columns A0/1=[2,1,4], B2/3=[1,2,7], forwardoffsets[1,2,4,7]。选择它因为三角闭词003/030/300对全部纤维源满rank3；REPAIRED_ARC的030退化，故不把它也机械加进来。相邻controllerpair由已测fourarc pencil全8。新的预测P1：至少一个规范(q,r)实际全D3；P0同controller三角全8应始终保住。对三个type根j0、全部8个fiber源坐标，保全部ordinary controllerwords0..3的真实affineimageunion检查；phase平移覆盖其余j，不以x0或容量替代。

B samecase30CPU，前5.174706358+prep.3，worker10CPU。若hit才实际264/1056/max8边表+ordinary全264root producer BFS；fresh/最新public/Lean/ARIS另required。No只关fixedARC/三型C11voltage这100规范代表，不一般C33/8D3；完成立即STOP，不换m/q/r范围或另一chart。
