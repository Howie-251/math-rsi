# T33 研究进度

2026-10-13 最终核验：**任意有限简单五元超图，边数至多 33 即具有 Property B；m(5)≥34 已完成端到端 Lean 证明。** 显式新 Main 的正式构建、构建后独立原题审计、Grok/Gemini 最终 C、正文检查和 HTML 保真检查均已完成。可读证明、转交包与 wiki 均已完成；T33 的全部验收要求已满足。

- 原始要求：[GOAL_PROPERTYB_33.md](../../GOAL_PROPERTYB_33.md)、[ACTIVE_GOAL.txt](ACTIVE_GOAL.txt)。正式规格：[T33](../propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md)。目标没有改变，也不扩展为证明 m(5)=34。
- 主声明：[Main.lean](../../formal/Aris4Math/ThirtyThree/Main.lean) 中 `Aris4Math.propertyB_of_at_most_thirty_three : Target33`。其前提仅为任意有限顶点集、简单五元边族及至多 33 边；点对覆盖、点数范围、局部类型表和概率界均在内部处理。
- 本机实际 `lake build Aris4Math.ThirtyThree.Main` 于北京时间 15:41 完成 1138 jobs、exit 0；15:42 的 `lake env lean ReviewAudit33.lean` 再次 exit 0。后者从裸 `[Finite V]` / `Finset` 原题得到合法 Bool 染色、每边两色均出现和至少 34 边下界。8 项传递公理仅 `propext`、`Classical.choice`、`Quot.sound`，无 `sorryAx`、新增公理或 `native_decide`。
- 构建保留了固定依赖缓存，是本机显式增量构建与独立导入，不是另一台机器上的重建。原始输出及命令见[最终装配](round02/final-assembly/REPORT.md)和[形式核验](FORMAL_VERIFICATION.md)。

## 全部分支与最终连接

| 范围 | 完成状态与证据 |
|---|---|
| 原始 T33 到 19–25 点 | `Target.lean`、`Reduction.lean` 已证明最小反例点对覆盖、≤18 点可染、≥26 点度数矛盾及补齐 33 边；[归约证据](round01/reduction/)。 |
| 19 点 | `ThirtyThree.Nineteen.nineteen_propertyB`；任意 H19、≤33 边；精确界 228354/230945；[证据](round01/nineteen/)。 |
| 20 点 | `ThirtyThree.twenty_propertyB`；12 个配置、实际加权删除与 88 分支闭合；[证据](round01/twenty-complete/)。 |
| 21 点 | `ThirtyThree.twenty_one_propertyB`；双锁/三锁的实际选点、类型及库存扣除闭合，总表最大界 3292/3315；[证据](round01/twentyone-math/)。 |
| 22 点 | `ThirtyThree.twenty_two_propertyB`；六种实际选点、高迹覆盖、真实重数和坏对扣除闭合；[证据](round01/twentytwo-selection/REPORT.md)。 |
| 23 点 | `ThirtyThree.twenty_three_propertyB`；以下六个完整分支全部闭合，在 `TwentyThreeComplete.lean` 内穷尽并调用；[装配证据](round02/final-assembly/)。 |
| 24 点 | `ThirtyThree.twenty_four_propertyB`；所有四低、匹配及混合分支闭合，包括 51 有标签匹配型到 18 代表及真实坏槽/dual；[证据](round02/twentyfour-complete/REPORT.md)。 |
| 25 点 | `ThirtyThree.twenty_five_propertyB`；实际六锁或八锁选择、14 型覆盖、实际类型与严格界闭合；[证据](round01/twentyfive-complete/)。 |
| 原主定理 | `ThirtyThree.finite_goal` 汇总全部七个点数，`propertyB_of_at_most_thirty_three` 返回原始任意有限输入的 Property B；[1138-job 正式构建](round02/final-assembly/main-build.log)。 |
| 独立原题与公理 | `ReviewAudit33.original_statement`、`both_colors_in_every_edge`、`original_lower_bound` 均通过；[构建后输出](round02/final-assembly/original-statement-post-build-audit.log)。 |

23 点令 r 为六度点数。完整分支入口如下；所有分类和数值条件均由实际 H 构造，没有作为外加假设留给调用者。

| 度数分支 | 完整入口 | 证据 |
|---|---|---|
| r≥4 | `TwentyThreeFourLowComplete.propertyB_of_four_sixes` | [四低完整报告](round02/four-low-unit/REPORT.md) |
| r=3 | `TwentyThreeThreeLowComplete.propertyB_of_three_sixes` | [三低报告](round02/twentythree-three-low/REPORT.md) |
| r=2 | `TwentyThreeTwoLowComplete.propertyB_of_two_sixes` | [两低报告](round02/twentythree-two-low/REPORT.md) |
| r=1，存在七度点与唯一低点共度≥2 | `TwentyThreeLowBadHighComplete.propertyB_of_low_bad_high` | [坏高邻居报告](round02/low-bad-high/REPORT.md) |
| r=1，与全部七度点共度1 | `TwentyThreeLowUnitComplete.propertyB_of_low_unit` | [全单位报告](round02/low-unit/REPORT.md) |
| r=0 | `TwentyThreeHighComplete.propertyB_of_no_sixes` | [完整高分支交接](round02/twentythree-selection/HIGH_BRANCH_HANDOFF.md) |

## 审阅与阅读稿

Grok 最终 C 与 Gemini 全新 C retry1 均已有效返回，在各自实际读取范围内未发现命题不对齐、隐藏前提或实质漏洞；二者是源码与已有日志的静态审阅，没有执行 Lean。Gemini 首次 C 的网络错误保持失败记录，不计作通过；有效重试也不改变该失败的性质。[原回应及主代理处置](round02/reviews/REVIEW_DISPOSITION.md)记录实际范围和 reviewer 笔误。

Fresh ARIS proof-checker 检查了完整正文及关键 Lean 接口，无未解决的实质缺口。两处正文说明已修正：21 点总表最大界为 3292/3315；23 点三低完整有标签域为 1796，844 是五种规范低预算下的数目。Lean 源码不受这两处修订影响。该审阅为 same-family/provisional；实际内核构建和公理审计另列为确定性证据。完整审计入口：[PROOF_AUDIT.md](round02/final-audit/PROOF_AUDIT.md)。

[规范证明正文](../../proofs/propertyb33/PROOF_PACKAGE.md)及[单卷离线 HTML](../../PROOF_PACKAGE_33.html)包含规格、概率引理、全部结构分支与精确界。HTML 全文、1049 个内嵌公式、9 张表及桌面/手机离线展示均通过保真审查；这一审查仅评价展示，不替代数学证明。

## 交付与恢复

[人工查验交接](../../HANDOFF_FOR_REVIEW_33.md)、`aris4math_t33_review_bundle.zip`、[复现说明](../../formal/README_T33.md)、[形式核验记录](FORMAL_VERIFICATION.md)及[round02 报告](round02/REPORT.md)为当前交付入口。包已生成且读取检查通过，wiki已新增 verified claim `propertyb-m5-ge34`；不再启动“剩余 23 点”研究，也不自动推进到 34 边新题。

旧 T32 保持完成，同一 research-wiki 继续积累。早期候选、失败路线和中途导航完整保留在[导航历史](round02/final-audit/NAVIGATION_HISTORY.md)、[候选地图](round01/large-math/COMPLETE_CANDIDATE_MAP.md)及各原始报告中。有限局部表的覆盖和实际输入绑定已在 Lean 证明；整图搜索与模型意见不承担全称证明义务。
