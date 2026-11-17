# 主线接受记录｜E16 的完整 μ=1

2026-11-15。主代理全文读回最终证明与整装独审，并核对源模型和 CNF 的独立重建及两份实际 RUP 验真回执，接受**完整 E16 的 $\mu=1$ 整族**。

设 $M\subseteq E(Q_7)$ 是短匹配，$\delta_i$ 是第 $i$ 个坐标的位一面原偶孔数减原奇孔数。若
\[
|M|=56,\qquad \min_{i=0,\ldots,6}|\delta_i|=1,
\]
则存在包含 $M$ 全部原边的 $128$ 点全短 Hamilton 单圈。 [最终证明](delta2_extension/MU1_STRUCTURED_CLOSURE.md) · [整装独审](delta2_extension/MU1_STRUCTURED_CLOSURE_REVIEW.md) · [机器回执](delta2_extension/MU1_STRUCTURED_CLOSURE_REVIEW.json)

相邻原孔加短边回 E14。两种中央差一切分别用旧差一门和六维 $A_8$、$B_4$ 的扩展门。独立原孔的两个边缘型中，单孔小面由冻结 CNF 的 RUP 证书闭合。三孔小面先用跨层参数双桥剥离，再把大面余域归约至四个重量模板及 23 个共同坐标置换代表。小面保留符号变量，23 个代表同入一份 CNF。两分支均经官方 DRAT-trim 验真，直接构造与坐标逆变换保留同一份原匹配的全部边。证明未枚举原匹配。 [六维工具验收](q6_a8/ROOT_ACCEPTANCE.md) · [跨层双桥独审](../mu0_global_2026_11_15/Q6_BALANCED_DELTA2_TRANSFER_REVIEW.md) · [大面代表独审](delta2_extension/STRUCTURE_BASIS_REVIEW.md) · [联合 CNF 独立重建](delta2_extension/union_certificate/audit_union_rebuild.json)

本结论是计算辅助证明。终审为 **PASS · same-family · provisional · sound-modulo-imports**。官方 DRAT-trim 对单孔小面和三孔小面联合 CNF 分别用时约 105.471 秒、13.954 秒，均返回 `VERIFIED_RUP_UNSAT`。 [单孔回执](certificates/edge_a0.verify.json) · [单孔日志](certificates/edge_a0.verify.log) · [三孔回执](delta2_extension/union_certificate/a1_large_face_union.verify.json) · [三孔日志](delta2_extension/union_certificate/a1_large_face_union.verify.log)

- 最终证明 SHA-256 `7905459b73129a6cbbd2460a560a7cbfd89801ae3eca4c1f5269680fa54df527`。
- 整装独审 SHA-256 `77f021509def02ac33ecfb1917e7e2d3a6dc9f5ed29d394fbadd42446522bb97`。
- 独审机器回执 SHA-256 `e1c7b2cf1fe67f2130c699006e28ebb32ded0cb20123bbcc1bb14256a61acfa2`。

E16 的 $\mu=1,2,3,4$ 已整族闭合，$\mu=0$ 仍待证明。最高完整孔层为 E14，覆盖至少 57 条原边的全部七维短匹配。完整 E16 与 $R_7$ 仍开放。
