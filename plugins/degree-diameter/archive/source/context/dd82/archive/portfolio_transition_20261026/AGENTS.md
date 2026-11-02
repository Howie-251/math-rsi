<!-- ARIS-CODEX:BEGIN -->
## ARIS Codex Skill Scope
ARIS Codex packages installed in this project: skills-codex
Managed entries: 85
Manifest: `.aris/installed-skills-codex.txt`
ARIS repo root: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/aris_repo`
Project skill path: `.agents/skills/<skill-name>`
For ARIS Codex workflows, prefer the project-local skills under `.agents/skills/`.
When a skill needs ARIS helper scripts, resolve the repo root from the manifest or set it explicitly:
`ARIS_REPO=$(awk -F'\t' '$1=="repo_root"{print $2; exit}' "/inspire/hdd/global_user/mahaitong-240108120090/ar4math/.aris/installed-skills-codex.txt")`
Do not edit or delete symlinked skills in place; update upstream or rerun:
`bash /inspire/hdd/global_user/mahaitong-240108120090/ar4math/aris_repo/tools/install_aris_codex.sh "/inspire/hdd/global_user/mahaitong-240108120090/ar4math" --reconcile`
For copied Codex installs, use:
`bash /inspire/hdd/global_user/mahaitong-240108120090/ar4math/aris_repo/tools/smart_update_codex.sh --project "/inspire/hdd/global_user/mahaitong-240108120090/ar4math"`
<!-- ARIS-CODEX:END -->

## ar4math 使用约定

- 数学工作使用项目内 ARIS Codex 技能；源码位于 `aris_repo/`，由 2026-10-08 的上游 main 源码包安装（不是 Git checkout）。
- 外部 Gemini 协作使用本项目的 `antigravity` MCP（`antigravity-exec`），不安装或引入 Gemini CLI。
- Antigravity 原生程序为 `bin/agy`；实际交互、模型查询和 MCP 使用 `bin/agy-via-proxy`。包装器复用现有 Mihomo 配置中的 `US-Dedicated-P1-1`，在临时本地端口启动专用代理并在结束后清理，不修改主 VPN。
- Gemini Pro 模型使用 `gemini-3.1-pro-high`、effort `high`，已设为 MCP 默认值。2026-10-08 同账号实测：TW-IPv6-P2-1 返回地区错误；US-Dedicated-P1-1 上 Pro 成功回复。后续不可将请求模型冒充实际返回模型。
- `antigravity` / `antigravity-reply` 是独立工具，不会自动替换 ARIS 技能原有的 reviewer 路由。
- 不主动生成产物哈希、校验和或哈希清单。

## DD82 active research

- Sole current execution plan: `context/dd82/N61_GLOBAL_CLOSURE_SPECTRAL_GOAL_20261019.md`. The human-in-loop plan remains applicable only where it does not conflict with this phase. The V3 plan is the inherited workflow/mechanism history, not a concurrent queue. V1 `N8/DEGREE_DIAMETER_8_2_ARIS_GOAL.md` and V2 `context/dd82/DD82_CONSTRUCTION_FIRST_GOAL_20261011.md` are historical, not concurrent task queues. Project root remains this ar4math directory. Do not access unrelated Property B or coding-theory projects.
- User explicitly authorized sending all N8 research materials needed for discussion (goal, specifications, private proofs, code, results) to Google/Gemini through Antigravity MCP on 2026-10-11. Use requested `gemini-3.8-flash-high` / `high` for these research discussions, preserving actual returned metadata. This does not require changing the global MCP default.
- Preserve original inputs under `N8/`; read-only extracted archive is `context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/`. Historical RUNNING/RAW fields are historical evidence, not current jobs or certified theorems.
- Single wiki: `research-wiki/`, updated through ARIS helpers. Current formal project: `formal/`, Lean 4.24.0, namespace DegreeDiameter. Do not introduce sorry, new axioms, native_decide, hashes or checksums.
- Full exact-value goal remains open unless both an explicit optimal graph and arbitrary-graph upper bound are connected in Lean and reviewed.

## Latest user research priority — 2026-10-11

- User explicitly directs that known order63,64,65 exclusions need not be reproved or further formalized. Stop dedicated N63 table/restriction/characteristic-polynomial work; preserve completed files and compiled evidence. Treat classical upper62 as cited mathematical baseline, not a new Lean axiom.
- Continue public foundations only when they directly serve new order58–62 results (Moore counting, regularity, actual defect identities). Focus new proof, construction and computation on unresolved58–62 ranges. This instruction overrides the older goal file insofar as it asks for dedicated formal reconstruction of known63–65 exclusions.

## Current construction-first execution — 2026-10-11

- Main work is actual58–61 constructions, exact expanded-graph checks, failure analysis and useful mathematical obstructions.
- n62's one bounded existing proof+SAT completeness review is COMPLETE in context/dd82/N62_EXISTING_PROOF_CHECK.md, with Gemini final review saved. Mathematical range is57≤N(8,2)≤61, full Lean unfinished. No new n62 solver search, proof optimization, Lean or repeated review absent a concrete new error.
- Freeze dedicated57 and63–65 formalization and unfinished old n62 Lean modules. Lean remains final acceptance after decisive new mathematical results.
- Do not repeat unchanged Brown/A5/old local-switch searches. Apply useful new58–61 constraints to computations promptly. Preserve the existing wiki and project.

## Current V3 execution — 2026-10-13

- Follow V3's ARIS DD82 mathematical adaptation: research-pipeline, explicit mechanism, Gemini direction review, actual implementation/proof and CPU verification, bounded auto-review-loop with the same mechanism/thread and reviewer memory, then evidence-based continuation or pivot.
- External reviewer only existing Antigravity/Gemini, requested gemini-3.8-flash-high/high; no automatic fallback, new Gemini CLI, shared skill edits, paper scoring, rendering, hashes, schedulers or old Lean work. Preserve actual returned model metadata without claiming independent backend attestation.
- Goal resumed active. Initial run dd82-v3-f9-c7-20261013-0749 tests the actual10080 normalized f9C7 parameters; this is a bounded construction-family decision, not a new definition of the goal. General58–61 remain open unless actual full-scope evidence changes that.

## Current human-in-loop execution — 2026-10-18

- Follow `context/dd82/DD82_HUMAN_IN_LOOP_GOAL.md`, which supersedes conflicting historical V3 execution arrangements. Construction-first58–61; preserve useful global proofs, inherited62–65 and postponed Lean.
- Maintain `research/progress.html` as a simple local Chinese research view, updating at meaningful changes and roughly hourly during active work; updating is not a pause. Human feedback stays in the existing comments section of `research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md` (one primary record).
- Discovery runs default to no proof logging; any unproved UNSAT stays unverified until a distinct justified certification task. Do not enlarge old budgets or reset closed mechanisms by renaming. Existing Antigravity authorization/model route remains effective.

## 2026-10-18 用户对报告节奏的澄清

每小时只要求更新 research/progress.html，不要求每小时新构造、新定理或切换 hypothesis；有数学依据的路线可以连续研究数小时，如实报告进展、未决问题、失败原因与继续理由。当前n58推导后完成一次旧baseline/20260825 iteration1/I12CP02与V3的有界n61对齐，核清[3,3]与双重缺陷共端边对应、前提及RAW证据等级；不重跑旧SAT、不扩Lean、不全历史重审。对齐后继续原58–61构造及全域证明，方向不按时钟强制切换。

## 2026-10-18 最新人工收束：n61一般共同结构

- 主力集中相邻孤立双缺陷分支的一般H35；六星、独立P5、双五色、实际AP30对覆盖及两份重复是原分支必要条件。反射、同星统一排列等特殊配色不得默认为一般范围。
- 58/60失败特殊模板不自动续修；已完成结论保留。
- 用户明确允许并要求有依据续查原C5生成来源：首H的70个packing失败仅排此H，第二类型未查。选择把必要父类条件接入实际生成后继续；旧“p/q不恢复/不重跑”不能阻止此次已授权的实质验收改进。C5仍是额外构造限制，A/P不强加C5作用，结果不外推一般H。
- 一般证明研究AP30对仅两份重复如何限制共同无向配边；若只是现模型已满足弱条件，明确未跨难点。
- HTML置顶只保留一项“当前任务”，按新增/剩余/下一动作组织；旧阶段标题和在途状态必须归历史，不与当前并列。每小时仍仅更新HTML。

## 2026-10-19 最新人工优先级：纸面推导优先

用户认为本题证明路径不长，要求更多精力放在数学推导；主力研究原图强迫结构、真实配边和短矛盾。Lean继续后置，不恢复形式化。必要复核集中在承重结论和实际计算入口，中间推导先连续推进，不逐条另开外审或流程。当前已准备的非相邻双缺陷完整模型仍只作原定一次有界检验；不据弱条件重跑、加预算或恢复失败模板。每小时仅更新HTML的要求不变。


## 2026-10-19 最新人工指导：统一约束优先，分类服务于原始n61存在性

用户认可并要求保留h6完美匹配定理、双C端口排除及h7合法换根，不要求停止证明路线。下一阶段优先用真实缺陷矩阵、父边、重复路线预算、共同匹配及换根关系，寻找同时作用于多个h5/h6剩余范围的定理；不在每次排除位置后自动继续交集、颜色或排列的小分类，不预加反射或统一排列。

每次必要分类明确是否完整覆盖原范围、哪些真正关闭、哪些只归到另一开放分支，以及是否减少核心困难。仅增加端口子类型不能当作进展；若连续推导只增加描述，应检查是否进入长尾，考虑更整体表示、合并范围、有明确完整范围的有限计算，或无双重缺陷分支。不是到点强行换方向，也不因短期未闭就放弃。

用户优先h6恰一W端口，因为承接h7。实际时间差：该完整范围已在H6_ONE_W_PORT_PARENT_THEOREM.md纸面关闭；结合既有合法换根，h7已在其稿§9合并排除。保留这些更新，不能因指令中提到较早剩余而重开已闭证明。

始终保留一般非相邻双缺陷、无双缺陷及旧RAW认证缺口，不能据局部结果称整个n61接近完成。构造与不存在性方向均保留，Lean后置，严格证据要求不变。小时要求仅报告，无每小时换hypothesis或新定理要求。

下一次HTML重点回答：真正关闭的完整范围；是否有同时作用多个分支的新定理；分类在收缩还是仅细化；关闭整个非相邻双缺陷还缺哪项共同数学条件；继续当前路线的明确数学理由。将指导接入实际任务后继续研究。


## 2026-10-19 最新人工安排：n61整体收尾与完整谱算术

按 context/dd82/N61_GLOBAL_CLOSURE_SPECTRAL_GOAL_20261019.md 替代冲突的旧执行优先级。本阶段只研究n61；n58–60暂停，n62–65不重启，Lean仍为最终验收。暂停自动h5/h6细分、新构造模板和随机B/谱族筛选。先在现有wiki对照旧谱成果、输入测试包、三种文献收尾及真实未完义务，随后立即研究不可约因子提升、整数重数、非主迹44与真实矩阵实现。n61平方行列式分母45；旧n59分母53不适用。谱恒等式、旧测试和包内材料不登记为本轮新成果。

当前优先选择全图同一迹的算术收尾；保持含/无双重缺陷的全部原图。允许有完整范围与实测依据的有限判定，不自动恢复旧巨大公式加弱条件长跑。新的有依据输入不再机械受旧28/88秒单次限制。保留最新h6恰一W及h7已闭事实，计划里较早的h7状态以原稿§9为准；一般h5/h6及旧RAW认证缺口仍开放。HTML只一项当前任务，说明整体量、谱障碍、新增与旧条件差别、缺口和继续理由；每小时仅报告。
