# Controller32 × F2³：多route接口只读门

结论：**已读旧严格范围没有关闭 controller-specific 的多rank2路线联合覆盖。** 关闭的是四个固定逆标签的通用“全部36个约化三词各自rank3”要求；同一个32点controller的实际字面输入/路线分组与其联合覆盖终态，本次有限读取未定位。不能从此声称32控制器存在、256点图可构造，或全历史无人做过。

## 继承的实际源与逆约束

原成功源 `refresh_20261029/f5_full_d20_D3/PARAMETERS.json` 有30个controller顶点、四个全局ports，bar=[1,0,3,2]；directions依次e1/e2/e3/(1,1,1)。`generate.py` 真正一步是

    (u,x) -> (C[u][p], T_p x + lambda * directions[bar(p)])。

偏移不是 directions[p]。原F5的矩阵为

    T0=[[0,2,4],[1,0,0],[0,1,3]]
    T1=[[0,1,0],[4,0,3],[2,0,1]]
    T2=[[2,3,1],[0,4,1],[1,0,1]]
    T3=[[2,1,2],[3,3,4],[3,4,4]]。

这是F5字面值的读取，不是把它们mod2或核算新域。所读MATRICES_AND_PENCILS元数据已接受四个真实inverse ports、方向相容、六平面pencil合并125且全部source坐标覆盖；不重验这些旧结果。F5矩阵的逆关系只在原域继承，不能默认逐系数mod2仍逆/可逆。

30*q³是原controller30的阶数公式；q2时只给条件数240，不是256。256必须另外有32点controller；本门不选它。原简单quartic controller需 C[C[u][p]][bar(p)]=u、四port邻点不同且无loop。对F2一步 x->A_p x+lambda*v_p，真反向必须 A_bar=A_p^-1、v_bar=A_p^-1 v_p（负号在特征2消失），不能独立挑反向planes。一般edge-local原规则还需 T_e l_p=l_q、T_reverse=T_e^-1；固定四global maps只是其特例。没有执行任何新matrix rank/inverse测试。

## 旧排除究竟说了什么

`breadth_20261027_wave5/binary_route_chart3/REPORT.md` 及 search.cpp：四个固定逆标签，所有GL3(F2)两生成矩阵及非零方向在唯一规范化后197568输入，全部36约化长度3词rank3的通用chart不存在；最佳28/36，报告有Fano商空间纸面矛盾。该报告**明确写“不外推其他多route覆盖、edge-local矩阵或一般degree8/D3图”**。它没有选controller、更没有controller32的actual pair-wise union检查。

Mizuno源报告中的 n<=31 是另一个 **q3、相邻靠pencil、每非邻pair靠至少一个good-rank3 NB3** 的证书计数界；报告也明确不是所有q3图的上界。不能把31当F2联合子空间覆盖的controller上界。

因此若执意要求每个controllerpair各拿一条满秩word，旧严格失败仍继承，不重跑；若让同一pair多个低秩实际word共同覆盖，不能借上述NO直接关掉。

## 最小未闭问题，不是新构造或大筛选

三步word w=abc 的真实像为

    L_w*x + Im[A_c A_b v_a, A_c v_b, v_c]，L_w=A_c A_b A_a。

抽象线性空间中，三个rank2平面 x1=0、x2=0、x1+x2=0 的并确可覆盖F2³（共同一条线）。这只反驳“全低秩并集必漏”的推理，**没有实现任何controller或inverse-compatible route packet**。若各word的L_w不同，零源x=0的平面并覆盖也不能代替全部8个source坐标的coset覆盖。

唯一下一接口问题：**在一个先冻结的实际controllerpair及其真实<=3路线包、和满足真实反向约束的binary port maps上，各source x的全部实际仿射像之并是否等于八点F2³？** 可被一个source坐标/target缺点推翻；若只靠rank2，需检查实际planes/cosets如何补足，不能只相加rank2容量或自由拼接反向maps。必须含shorter routes；controller立即反向不必是fiber中的立即回退，未经证明不能只保36约化词来冒全覆盖。

本次未定位可冻结的同source C32字面输入，因此还没有实例化这一单pair测试，更没有枚word/选controller/出图。若将来有既定输入，先只问一个局部包；局部通过也不代表所有controllerpairs（含对角/相邻）通过。当前STOP，不派controller筛选/field ladder/大图搜索。

## 读取范围与费用

只读原F5 PARAMETERS/generate.py、MATRICES_AND_PENCILS元数据、binary chart REPORT/search.cpp、Mizuno source REPORT，以及现有账本中相关D3节点字段；未重新导入/重建Wiki。两段有计时的账本读取载荷CPU为0.659147412与0.823640078，合1.482787490；不再做检索。将启动/静态整理计入后保守收束记1.6CPU，较1.5计划约多0.1，已明报root；不重置成本。0source parse/BFS/新field算术/word枚举/controller生成/solver/Lean/ARIS/HTTP，0新图/参数。只写本门md/json，不改Wiki/STATE/pages。
