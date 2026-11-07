# 00 基础、模型与依赖核对
日期：2026-10-19。新任务：迁移 N(7,r,s)：结构分解与容量上界。

## 0. 证据与接受边界
本任务的引理附有本轮数学推导；尚未独立科学审阅或正式验收。只读助手用于原始资料定位，不承担新定理审阅。旧任务、证明绑定、接受状态与运行均未改动。本轮未编写研究代码，未运行 SAT 或计算实验。

## 1. 模型
X 是有限全序集合，其每个三元组完整染成蓝 B 或红 R。rank-3 signotope 条件为：对 i<j<k<l，
chi(ijk), chi(ijl), chi(ikl), chi(jkl) 至多一次变色。
蓝对应 cap，红对应 cup；不用旧 CNF 分组名判断颜色。

q 点单色路径是 q 个递增顶点，其连续三元组均为该颜色；长度始终为顶点数。一点、两点路径的条件为空，两点路径同时是两种颜色。
weak n-gon 是共享左右两个外端点的异色路径，长度和 n+2；不另要求内点不交。
U(n,a,b) 表示无蓝 a 点路径、无红 b 点路径、无 weak n-gon 的此类 signotope 的最大点数。
以下通常 n>=3，a,b>=2。参数不必满足几何文献的 triplet 限制；退化边界 U(n,2,b)=U(n,a,2)=1。
颜色交换给出 U(n,a,b)=U(n,b,a)。纯顺序反转保持颜色；四点包次序反转，仍为 signotope。

## 2. 最新接受基础
只读核对截至 2026-10-19 的本地记录：
- 旧任务 research/cardinality-layer-theorem.md:21–31：接受到 C6，U(7,5,6)<=29。
- research/c6-formal-acceptance-20261016.md:3,9,19,32–40：C6 为所有规模的 e>=6 => m>=6；沿用 C1–C5。人类正式接受，review assurance 为 provisional，backend/model/effort 不可验证；0 fresh checker replay，重用 5 个 checked cases。
- research/evidence/c6-accepted-20261016/current_status.json：theorem_credit=true、certified_upper_bound=29，作用域如上。
- research/c8-parallel-search-20261017.md:23–31，以及 research/evidence/c9-c10-started-20261018/README.md:17–19：后续运行不产生新的接受界。C7 及更高行不能当作已接受定理。

旧目录的绝对位置：
D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/

旧结果保证仅按原有条件继承；本任务不宣称重验了旧证书。旧 757/766 数学稿是起点，不是新任务的独立审阅凭据。

## 3. Baek 定理的模型核对
原文：Jineon Baek, On the Erdos–Tuza–Valtr Conjecture，arXiv:2206.04260v2，
https://arxiv.org/pdf/2206.04260 。
Definition 2.1 在第3页允许任意完整有序三元组二染色；
Definition 2.2 在第4页以连续三元组定义路径，长度为顶点数；
Definition 2.4 在第4页以共同外端点及长度和 n+2 定义 weak n-gon。
Theorem 2.7 在第5页：binom(n-1,2)+2 个顶点保证蓝4、红n 或 weak(3,n-1)-gon之一。
所以它涵盖当前 signotope 子类，并给出 U(7,4,7)<=16；不是把几何定理直接外推。
Theorem 2.6 同页给一般二染色的 cap-cup 上界 binom(a+b-4,a-2)。

本任务只引用以上模型与定理。文中的其他猜想不作为前提。
另核对 Baek–Balko, SoCG 2025, Section 3 的 signotope 定义：
https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.html 。
其一般二染色反例和 signotope 猜想明确分开；不能把 split-gon 定理当作 weak-gon 定理。

## 4. downset 与计数
sigma_X(u,v) 为以同一终端对 (u,v) 结束的最长蓝、红路径长度各减一。
D_X(v) 为全部 sigma_X(u,v) 的下闭包；最小顶点的状态为空。
状态盒为 [a-2] x [b-2]。写成非增列高。

若 u<v，sigma_X(u,v) 不在 D_X(u)：否则存在 w<u，其 sigma_X(w,u) 同时支配这两个坐标，而 chi(w,u,v) 的颜色会延长相应路径，矛盾。
所以 D_X(v) 不包含于 D_X(u)，特别是各顶点状态不同。此证明不需要 signotope 或 weak-gon 条件。
若 Y 是诱导子配置，则 D_Y(v) 包含于 D_X(v)，但通常不相等。

n=7 时普通状态为空或包围盒宽高和<=6；其余为异常。
固定非空包围盒 (w,h) 的形状数 binom(w+h-2,w-1)，全盒形状数 binom(a+b-4,a-2)。
因此：
| (a,b) | 全部状态 | 普通 O | 异常目录 |
|---|---:|---:|---:|
| (5,6) | 35 | 25 | 10 |
| (5,7) | 56 | 26 | 30 |
| (6,6) | 70 | 30 | 40 |
| (6,7) | 126 | 31 | 95 |
| (7,7) | 252 | 32 | 220 |

始终有 M=O+e-m。这里 e 是实际占用异常数，m 是实际缺失普通数；表中最后一列不是实际 gap。
普通 O 也可直接按包围盒计数；不把其数值当作已证明极值。

## 5. 29 点等号与接近等号
对于重算状态后的任意 756 子配置 Y，C1–C6 给
- 若 e_Y<=5，则 |Y|<=25；
- 若 e_Y>=6，则 |Y|<=25+e_Y-6=e_Y+19。

所以 |Y|=29 强迫 e_Y=10,m_Y=6。
更一般，若 |Y|=29-d>25，则 e_Y>=10-d；至多 d 个异常状态缺失。
写 h=10-e_Y，对所有规模统一有
    29-|Y| >= min(h,4).                         (F0)
当 h<=4 用 C6；当 h>=5 用 C1–C5（e=0 时直接计数）。
颜色交换后对 765 同样成立。
这是从已接受层重新推导的结论，不搬用原配置的占用信息。

