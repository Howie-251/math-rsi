# 第二三角因子对应的线图上界

2026-10-30读取原始论文PDF：Stijn Cambie、Wouter Cames van Batenburg、Rémi de Joannis de Verclos、Ross J. Kang，Maximising line subgraphs of diameter at most t，arXiv:2103.11898v2，第2页Theorem 2。原文：https://arxiv.org/pdf/2103.11898 。正式期刊 DOI：https://doi.org/10.1137/21M1437354 。

读取范围：摘要、引言中的h_t定义、第2页Theorem 2；没有重新证明或复核全文证明。原PDF已保存为CAMBIE_ET_AL_2022.pdf，pypdf仅提取全文到同名.txt供定位。

原定理：最大度至多3的多重图若有至少23条边，其线图直径大于3，即h_3(3)=23。

本项目的应用：C=I并F，I与F均为边不重合的三角因子时，C是三正则二部图H的线图，|V(C)|=|E(H)|。故若C直径至多3，则|V(C)|≤22；又三角因子使阶数为3的倍数，得到≤21。这一范围足以停止F=11K3的33点尝试，不用枚举22点三正则图。

这属于已发表上界在当前构造机制上的应用，不登记成新的线图上界。一般F的无三角必要条件另由controller33_second_triangle_factor/PROOF.md第4–5节自含推导，不依赖本引用；其一般C33仍开放。
