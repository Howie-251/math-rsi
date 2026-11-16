# 新 main 与本地 DD 反馈修订整合

2026-11-14。用户要求后续使用的版本同时包含下载包的新主循环，以及此前在本地落实的研究反馈。按 `mathrsi-meta-evolve` 在现有框架上整合；本轮仅本地维护，不恢复数学 Goal、不改验收、不重建 Wiki、不推送或发布版本。

## 来源与实际范围

- 基线：用户提供的 `math-rsi-main (2).zip`，已解压的 2026-11-11 main 快照。包含固定 v4 及其后全局进展重评、六领域路由与 ECC 节点维护。它是下载时快照，不声称等于 2026-11-14 远端 main。
- 本地反馈：旧 `math-rsi-publish` 的 `fix/dd-search-feedback` 未提交修改。原工作树及全部修改保留；移植其三个 DD 工具、真实小输入、测试、必要的技能调用及说明。
- 工作树：`math-rsi-integrated`；本地分支 `integrate/main-dd-feedback-20261114`。新快照为主线，旧文件不能整体覆盖新技能。复制的历史研究、版本标签与来源说明保持原意。

## 合并取舍

| 已有内容 | 本次处理 |
|---|---|
| 新 main 的五阶段、唯一调度者、独立全局重评、一次有界展期、完整有限计算保护 | 保留新版实现，不用旧版较弱续批说明替换 |
| 旧版母机制累计投入、细分/换种子不清零、局部成果与路线价值分开 | 由新版 `global-reassessment.md` 统一执行；DD 返回领域依据，不另开主循环 |
| DD 固定选择后剩余端口不足 | 移植 `residual_cover.py` 和 `candidate_selection.py`，让结果实际选择继续固定分支或修改前部 |
| 关键操作未执行或变量未变化 | 移植 `search_operations.py`，保留提案、执行、合法、接受和关键变化的区别 |
| 迁移前检查成功条件、原题条件与人为限制分开 | 增量接入新版 DD 技能，保留 v4 的饱和图改边/补点方法与验收 |
| 旧研究恢复文本仍指定 v2 克隆 | 验证后统一指向本整合目录；原目标、成果、研究数据和暂停状态不变 |

恢复中发现 ZIP 内技能别名以文本文件展开；将整合目录中的这些项按原 ZIP 的符号链接类型恢复，保留原相对目标。网页预览副本不变。

## 校验与边界

已完成以下有限核查：

- 导入基线的 49,600 个文件与原 ZIP 文件集合完全对应；115 个技能别名均恢复为可解析的仓内相对符号链接。
- 新版 10 个 `mathrsi-*` 主技能与 `global-reassessment.md` 的内容保持原样。DD 的 v4 饱和改边新增段保留，`saturated-insertion-and-replay.md` 与 obstruction 技能整文件未改。
- DD 的三个工具、三份测试和真实 fixture 与旧本地修订逐字一致；`python3 -B -m unittest discover -s plugins/degree-diameter/tests -v` 实际 23/23 通过（DD 作者执行，0.034 秒）。
- Root 从 `/tmp` 调用本整合目录继承的 `forward_use.py`，实际导入整合目录的模块；输出见 [本次结果](forward_use_result.json)。真实 77 组输入触发 `REVISE_FIXED_CHOICES`，`continue_fixed` 调用 0 次，`revise_fixed` 调用 1 次，固定 B-only 待办从 1 项变成 0。小覆盖例与操作派发例也通过脚本自身断言，均不代表新图。
- 三个变动 DD 技能通过 `skill-creator` 格式检查；`tools/check_links.py` 检查 135 份维护文档、1,984 个本地链接，缺失 0；`git diff --check` 通过。
- `docs/DOMAIN_ROUTING.md` 在新版调用点接 DD 反馈；DD 的 `CONTINUE_UNRESOLVED` 只表示局部候选尚未被排除，不是整条研究路线获得新额度。旧版主线停滞说明统一引用新版全局重评，不另建重叠规则。

尝试一次现有 Antigravity 路由的有界设计审阅，服务因既有 `gemini-3.1-pro-high` 与 effort 配置不兼容返回 ERROR，未开始原件审阅，threadId 为空；[请求](review_request.txt)与[原回应](review_response.json)保留。未修改服务配置、未重复请求、无跨模型 PASS。Root 与 DD 作者的检查属于本地/同家族核查。

全局重评仍是 agent 执行协议，不是宿主的自动额度监控器。本次不新建调度平台，不声称已验证长程研究不会空转，也不把旧数学成果计作本版本的新结果。跨模型审阅若不可用如实保存；同家族检查不冒充异构模型审阅。

## 采用与恢复

采用为本地整合版：新 main 主循环＋已有 DD 搜索反馈修订；不创建或移动 v1–v4 标签。旧修改工作树、原 ZIP 和网页预览副本保持。本次没有更新远端 main，也未发布网页或恢复图搜索。

当前任务工作区的 `math_rsi_local_code.txt`、`math_rsi_resume_latest_table_goal.txt` 与原 Goal/恢复入口只更新所选框架位置；原数学暂停断点、已有结果、公开数据快照、预算与 Wiki 沿用。项目本地 `.agents/skills/` 的 MathRSI＋DD 别名指向本目录，原 ARIS 别名及全局安装不变。再次明确恢复研究时，从本目录读取主技能和 DD 入口；不能因源码已更新而假定旧二进制/搜索驱动已经接入反馈，应在真正启用该驱动时核对它的调用。
