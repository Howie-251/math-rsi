# 原始输入：双配额实际调用

这是本轮MathRSI技能行为试用，不是重启Property B或ECC旧研究。

给定有限集合 $S,Q$，实数 $a_{qs},w_s,z_s,c_s,b_q,\delta_q$，满足
$$0\le z_s\le c_s,\qquad \sum_s a_{qs}z_s\ge b_q,\qquad \delta_q\ge0.$$
目标是复用Property B数学库L7一般quota修复引理，证明有效weighted-cost bound
$$\sum_s w_sz_s\ge\sum_q\delta_qb_q-\sum_sc_s\max\{0,\sum_q\delta_qa_{qs}-w_s\}.$$
然后用 $S=\{s\},Q=\{1,2\}$、所有 $z,c,w,a,b,\delta=1$，检查把两个单独下界直接相加为什么不合法，修复界怎样接回这个实际输入。

授权范围：只复用已证引理及caller；独立精确整数/分数计算；先局部verify，再返回原prove调用完成总目标。无旧工程写入、Lean、付费review或外部文献调查。若未正规运行proof-checker，不能生成或声称PROOF_AUDIT。

产物唯一写域是本目录。用户已提供准确命题和已知引理定位，采用主技能允许的短证明/既有方法入口，直接prove；不为本任务新造route-loop或全套prepare。
