### 澄清与修正

1. **撤回结论 C 的不可能性断言，重划已证与待证边界**
   * **结论 C 修正为：未知（开放）。** 明确撤回上条回复中“不对”及末句“该框架不可能消去 $\sqrt{\ln k}$”的无定理支撑断言。
   * **原因与严格边界**：固定 $s$ 个锁点不仅约束 $s$ 个锁位置，还会通过迹划分 $T\subseteq[s]$ 与剩余自由度 $r_T=k-|T|$ 改变**所有自由位置 $h$** 上的条件超几何分布 $w_h(T,U)$。**已证事实**是：现有文件仅对固定小 $k$ 给出了 0–3 锁的有限有理计算，未包含任何 $k\to\infty$ 的渐近定理；**待证问题**是：当锁点数、位置布局、共度扣除或多布局对偶随 $k$ 联合缩放时，能否改变领先常数乃至消去 $\sqrt{\ln k}$，目前既无正面证明，也无不可能性定理。

2. **文献归属澄清（相对 CK vs 已有文献）**
   * 有限点数上的离散超几何计数与逐位置取 $\min$ 机制已在 Grill–Linzmayer (2024, arXiv:2403.05674v3, §2 式 6–8) 中建立（见 [propertyB_k8_k9_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_k8_k9_proof.md#L11) 与 [PROPERTY_B_SMALL_K_TRANSFER.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md#L3)）。
   * 上条所列“相对 [CK2013_FULLTEXT.txt](file:///Users/rfy_naiveai/Desktop/aris4math/context/general-method-discussion-20261021/CK2013_FULLTEXT.txt) 的新分析内容”仅指相对于 CK 原文连续三区间松弛的数学收紧，**不能等同于本项目首次创新**。

3. **验证 root 推导：对（完全成立）**
   * 在 [CK2013_FULLTEXT.txt](file:///Users/rfy_naiveai/Desktop/aris4math/context/general-method-discussion-20261021/CK2013_FULLTEXT.txt#L152-L161) 中，对 $x\in[-p/2,p/2]$ 有 $1-p^2 \le 1-4x^2 \le 1$，故中心积分满足
     $$(1-p^2)^{k-1} \le \frac{1}{p}\int_{-p/2}^{p/2}(1-4x^2)^{k-1}\,dx \le 1.$$
   * 当 $p=O(\ln k/k)$ 时，$(k-1)p^2=O(\ln^2 k/k)=o(1)$，故 $(1-p^2)^{k-1}=1+o(1)$；同时 $M(M-1)/M^2=1-1/M=1-o(1)$。
   * 因此，**仅靠精确计算该中心积分与将 $M^2$ 替换为 $M(M-1)$ 这两处精细化，确实无法改变 CK 估计的领先渐近常数**；但这不限制共享坏对扣除、多锁条件分布或新相关性分析带来实质改进的可能。

4. **层次 A（统一有限参数条件定理）是否保持原结论**
   * **完全保持原结论（对）。** 上述渐近与文献归属修正不影响层次 A：从 [propertyB_m6_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_m6_proof.md)、[propertyB_m7_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_m7_proof.md)、[propertyB_k8_k9_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_k8_k9_proof.md) 提炼出的 **0–3 锁有限参数可染定理**（含点对覆盖窗口、Caro–Wei 选锁判据及 $\sum_h\min(A_h,B_h,C_h-D_h)<1$）在有限参数下严格成立，并完整、统一地解释 $k=6\dots 9$ 的全部数值实例。
