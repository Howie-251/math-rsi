分层可以成立：`mathrsi-route-loop` 做唯一外层控制者，`research-review` 用 `— composed:` 承担每一审阅回合的取证和同会话对话。`composed` 只决定报告归谁写，不切断 `research-review` 自己的第3–4步。现在的调用写着“读取并执行”整份技能，那一轮会按“双方同意、实验计划、叙事定稿”继续对话，并索要实验、分数和 claims；外层同时又拥有 Phase C 的实作和 Phase D 的复核。这就是内外一起推动下一步。约束写在本次调用里，不改上游 `research-review` / `auto-review-loop` 字节，也不另做 Python 调度器。

必须真实留下的是这些动作，不是只留 route 和 trace：

- 首轮用已解析路由的宿主首呼工具，reviewer 自己读原题、候选、失败原件和原始结果。续接只用该会话的 reply，沿用原来的 model、effort 和 cwd；reviewer 读真实 diff 与结果文件。
- 先保存完整原文、session、实际身份和读过的范围，再提取意见。未完成、截断、未读关键原件保持失败，不能改成主代理自审。
- 每位 reviewer 单独带上自己的 memory，原文追加 `Memory update`。作者不能代写“已解决”。结论逆转时先对两份原文，不重开一次付费请求来换答案。
- 高影响分歧走同会话裁定：作者给证据，reviewer 标明接受、部分接受或仍驳回。分歧可以保留。
- 先完成数学实作并读回产物，再送复核。承诺、计划或 worker 的完成状态都不是修复。探针还在跑就不发复核，也不把失联当成未发出而自动重试。
- 恢复到精确 phase。C 未做完继续 C；reply 在途就收回后再进 D。已保存的 route 和 session 优先于后来改过的项目默认。换 model 或 cwd 才新开首轮，并带上原 memory。
- 只有本次明确要求独立攻击时才另开 fresh session，并重贴 scope limits。提示词保留原 scope limits，换掉的是 ML 问题。

避免双驱动的操作界线：一次 `research-review` 调用只做一轮。Phase A 是首轮审阅，做到收集上下文、真实调用、必要的证据追问后返回。Phase D 是实作完成后的另一次调用，用同一 `threadId` 请 reviewer 裁定原关切是否解决，然后返回。澄清证据、指出反例或写出最低补证，属于这轮对话。推导、`proof-writer`、领域探针、改证明和决定下一轮，只由 route-loop 做。`research-review` 不执行它原来的第4步停止条件，不启动修复，不调度下一轮。memory 和 `ROUTE_REPORT.md` 只由 route-loop 写；`research-review` 返回独有内容和 trace 路径。

这些 ML 条件改成路线判断，不调用 `review_gate.py`，也不编造 6 分或 ready：

- “ready / almost / 双方同意”改为：原输入到下游的连接已经写明，本轮关键异议已由读回的证明、严格反例或探针处理，剩余条件足够交给 prove；或者预算用尽、候选被否定、所需审阅未完成。这只结束本次路线范围，不表示定理成立。
- “最低修复是实验、GPU 或改叙事”改为一条区分性数学动作。ECC 旧题是补上独核没有覆盖的属性，做一次不借用旧接受集的扫描，再决定是否扩完；必要 pair 为空就停掉它所覆盖的扩张。Property B 是先证明同一对象上的松弛没有增益，再改共同约束；界已经严格就不再追更紧常数。
- 训练检查、`result-to-claim`、模拟会议分数、论文大纲不进入本阶段。终轮只把新增且可复用的路线事实写入现有 wiki。证明验收仍留给 `mathrsi-verify`。
- 24 小时清空状态不用于长期数学任务。恢复靠报告里的断点。

MCP 这一层不缺第二套调度器。`reviewer_route.py` 继续只解析配置；真正调用是宿主里的 `grok` / `grok-reply`、`antigravity` / `antigravity-reply`，以及按路由需要的 Codex、Claude 桥。续接只传 `threadId` 和 `prompt`。Claude 的 `review_reply` 例外，必须重传 cwd、tools 和 model，省略 tools 就只剩提示正文；`jobId` 不是 `threadId`。离线测试只证明桥的协议，不能写成这条路线已经审过。

最小修法只改 route-loop 的调用段和 `aris-review-adaptation.md` 里同一句：写明本次不跑 `research-review` 第4步；Phase A 与 Phase D 各是一次调用；提示词替换分数和实验要求，保留 scope limits；续接参数按 `REVIEWER_MCP.md` 里该后端的 schema，不套 Codex 的 `spawn_agent`。本次只读了这三份技能、route-loop 的适配页、`output-composition.md` 的 composed 合同和 `REVIEWER_MCP.md`，没有运行命令，也没有改文件。