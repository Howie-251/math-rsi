# pre-run：实际650保存系数的twin-class packet容量诊断

继承旧一次1170变量/20秒solver的UNKNOWN，无incumbent，不续timer，不读源/A2/A3，不新BFS。sole root numeric。模型FP_MODEL_MATRIX的520个F-coverage行只取非零1系数；1040cut列按真实F标签合为520 C_f（两列必须一致），130star_P列为D_p，不按twins合并。cut端点标签和旧65对Ptwins确定每类8个不同F。

可推翻预测：至少一个two-starP pair可通过以下必要上界；通过不证明真实覆盖。U=F\(D_p∪D_q)，类c需cost≥其starP数h_c、cost≤2、总cost8。m_c(1)为类内单包∩U最大大小；m_c(2)为类内不同F的双包并∩U最大大小。跨类重叠有利忽略，T=max Σm_c(cost)，T<|U|才能排该P pair。

等价优化而非近似：m1≤m2≤2m1，故边际m1和m2−m1非负递减。先满足h后剩6个cost，取最大6个可用边际，tie同class的first在second前，即取得小DP最优；最终按各类cost重新取相应单/双argmax，无需best single属于best pair。

一次完整8385个P pair，记录T/|U|/实际argmax包并覆盖大小。若任何局部argmax选择本身真实F-cover full，就保存8个F与2starP，停止容量批转构造评估；否则完成全域，若上界都失败可关F-cover子问题，若有upper survivor仅记UNKNOWN。上界不是新图，部分覆盖不计成果。

samecase45CPU：原22.084731374+已完成read.25+本prepare.2；新增native预算10含输入提取/compile/运行，worker8CPU（硬10），完成即停不自动第二批/solver/extraFPcuts。返回全部pair界或实际F-cover对象，0图/Lean/ARIS，命中实际F-cover后仍需F/P/newroot/oldold完整图与独立验收。
