# 历史材料导航与来源

以下文件是完整原文副本，仅在本包中使用较短文件名。原文件的日期、运行身份、结论和历史建议均未修改。阅读进展以主报告注明的快照为准；旧文件中的“仍运行”“下一步启动”不是现在的作业状态或本包指令。

共同原目录：`/inspire/hdd/global_user/mahaitong-240108120090/mathagent`，下称B；`B/degree_diameter_sat`下称R。最新回收位于`B/formal_loop`。这些路径用于出处追溯，专家理解报告不需要访问服务器。

## n59：主线

| 包内文件 | 原文件/目录 | 建议关注 |
|---|---|---|
| [08-28 c3/c5](n59/20260828_c3_c5.md) | B/N59_C3_RAW_UNSAT_AND_C5_THEORY_UPDATE_20260828.md | 六置换覆盖、343任务完备性、c5a/c5b短证明 |
| [08-31 固定父集](n59/20260831_fixed_parents.md) | B/N59_C1_PARTIAL_RAW_UNSAT_AND_THEORY_HANDOFF_20260831.md | 1077结构根；整类关闭与尚未尝试范围 |
| [09-03 coarse V3](n59/20260903_coarse_v3.md) | B/N59_M0_M1_COARSE_V3_RAW_UNSAT_AND_THEORY_HANDOFF_20260903.md | 可变父矩阵、13分拆、128切片与67 RAW |
| [09-05 lowtail V4](n59/20260905_lowtail_v4.md) | B/N59_C1_Q2LE8_LOWTAIL_V4_PARTIAL_RAW_UNSAT_AND_THEORY_HANDOFF_20260905.md | 61逻辑范围/63叶，唯一ell20关闭，补集仍开放 |
| [09-08 extremal V5](n59/20260908_extremal_v5.md) | B/N59_C1_EXTREMAL_ROOT_V5_PARTIAL_RAW_UNSAT_AND_THEORY_HANDOFF_20260908.md | 极值根与49→47，Nmax切分的成本 |
| [09-11 structural V6](n59/20260911_structural_v6.md) | R/docs/N59_C1_STRUCTURAL_SAT_V6_RESULTS_AND_THEORY_HANDOFF_20260911.md | 两种前沿口径，Q8整根与核心子叶的区别 |
| [09-22 manual12 r1](n59/20260922_manual12_r1.md) | B/formal_loop/N59_MANUAL12_ACTIVE_CODEX_TO_PRO_r1_20260922/RESULTS.md | 35代表/34入口，全部已尝试调用超时，14未尝试叶 |
| [09-29 manual12 r2](n59/20260929_manual12_r2.md) | B/formal_loop/N59_MANUAL12_ACTIVE_CODEX_TO_PRO_r2_20260929/RESULTS.md | 33代表、最新父交集RAW、真实约束和性能边界 |
| [r2实施](n59/r2_IMPLEMENTATION.md) | 上项dependencies/implementation/IMPLEMENTATION.md | 实际变量、guard与已用/未用条目 |
| [r2原运行说明](n59/r2_RUN_ON_CLUSTER.md) | 同目录RUN_ON_CLUSTER.md | 原计算问题及回收要求，仅作历史说明，不要求执行 |

主报告没有将这些不同版本的任务数量相加。其真实研究对象依次变化，且部分报告是中间快照。尤其“理论迁移”“代表资格变化”“完整根RAW”“cube RAW”分开记录。

## n58：第二重点

五份报告原件都在R顶层。

| 包内文件 | 原名 | 核心信息 |
|---|---|---|
| [V1](n58/20260829_v1.md) | N58_SAT_12H_EXPERT_REPORT_20260829.md | c3商分类与最初关闭，未运行c1主队列 |
| [V2](n58/20260902_v2.md) | N58_V2_THEORY_EXPERT_REPORT_20260902.md | 3A完整关闭；弱模型见证与完整图的区别 |
| [V3-3D](n58/20260904_v3_3d.md) | N58_V3_3D_12H_EXPERT_REPORT_20260904.md | 327505子RAW、0顶层关闭；phase→blocks接口 |
| [V4](n58/20260907_v4.md) | N58_V4_12H_THEORY_EXPERT_REPORT_20260907.md | 3B残余全闭、c1 4773宏根与首批47关闭 |
| [c1增量](n58/20260909_c1_incremental.md) | N58_C1_INCREMENTAL_12H_EXPERT_REPORT_20260909.md | 实际53闭合；四个新RAW可由旧禁型换根解释 |

配套完整理论在`../theory/n58/`。最新53/4720是09-09报告的实际账本；56/4717是纳入三条未写回推论后的条件更新，不并作一次新计算。

## n62：有效对照

- [旧状态与理论转折](n62/20260824_baseline_and_transition.md)：B/N62_CURRENT_STATUS_FOR_EXPERT_20260824.md，包含旧8/12及semantic子任务结果。
- [README_N62_AB.md](n62/README_N62_AB.md)、[README_N62_AB_RESUME.md](n62/README_N62_AB_RESUME.md)、[README_N62_PROGRAMS.md](n62/README_N62_PROGRAMS.md)：R中真实说明，分别解释A+B、最终补集覆盖、早期SMS/构造尝试。
- `../evidence/n62/`：旧SMS摘要、A+B中断快照、最终80/80摘要。旧pilot显示RUNNING是历史未更新状态，不据此猜测现在还有作业运行。

最后80任务活动墙钟473.684秒，不能当成n62整个研究的总耗时。

## n61、60：背景

| 包内文件 | 原来源 | 核心信息 |
|---|---|---|
| [n61 baseline](n61/vanilla_baseline.md) | B/N61_SAT_RESULTS_FOR_EXPERT.md | 60模板中21 RAW、39开放 |
| [n61初次理论迭代](n61/20260825_iteration1.md) | B/N61_EXPERT_PROOF_GUIDED_SAT_ITERATION1_HANDOFF.md | 39→36；三条新关闭与已启用约束 |
| [n61 CP02](n61/20260929_cp02_results.md) | formal_loop/N61_I12_CP02_CODEX_TO_PRO_manual-v1.2-feedback-loop_r1_12h_final/RESULTS.md | 55同公式seed全部超时；实际只新增W≤5 |
| [n60 P0](n60/20260831_p0.md) | B/N60_THEORY_GUIDED_SAT_P0_12H_RAW_RESULTS_AND_OPEN_FRONTIERS_2026-08-31.md | 216前沿轨道中42 RAW |
| [n60 quotient-first](n60/20260903_quotient_first.md) | R/N60_QUOTIENT_FIRST_SAT_18_OF_40_RAW_UNSAT_RESULTS_AND_OPEN_FRONTIER_20260903.md | 分类坐标从root转向quotient；此处40不等于后来的41分母 |
| [n60 Round11](n60/20260910_round11.md) | R/N60_ROUND11_12H_SAT_RESULTS_0_NEW_CLOSURES_AND_TWO_ROOTS_EXPERT_REPORT_20260910.md | 只剩两个大范围仍然无新关闭 |
| [n60 Round13](n60/20260929_round13_results.md) | formal_loop/N60_ROUND13_CODEX_TO_PRO_manual-v1.2-feedback-loop_r02_20260929/RESULTS.md | 80任务、130调用、0新关闭；完整启用/未启用条目 |

## 理论与原文链接的使用

`../theory/n59/manual12_r2_theory.md`保留完整整理稿，`manual12_r2_working_original.md`保留原稿。其引用的U、W38、MATCH，分别在本包重命名为`manual12_r1_working.md`、`continuation_38.md`、`matching_and_cycles.md`；P16小核较早正文在`20260915_round1.md`。原稿中的历史相对路径可能指向未搬入的完整旧包，请以本包的主报告、理论摘记和本导航为准。

这种选择性打包是为了让专家读方法和承重证明，不把千余个历史文件或生产CNF塞进附件。未取得的更早K3完整分类、K6全称Q界等仍明确缺失；不能声称本包已经完整认证全部旧理论和计算。

本包的CPU量只在原记录实际给出时标为实测或采样CPU；旧报告里solver墙钟之和、分配slot-hours等各保留原含义。主报告不把它们加成一个伪精确的项目总核时，也未估算LLM调用成本或推理总时间。
