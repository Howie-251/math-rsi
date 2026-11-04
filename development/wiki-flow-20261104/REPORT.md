# Wiki 读写衔接：本次维护

用户从 README 五阶段表和历史图发现 wiki 只在首尾被明显提及，要求检查 base 是否实际复用 ARIS 的结构化读写，以及怎样反复取用经验以避免重复失败。本次是 v3 主线的调用衔接修补，固定版本标签保持不变。

## 原来已有与本次补齐

已有：survey 的文献实体写入；route-loop 入口读取、终轮写回及完整 helper 例；prove 交接前沉淀；verify 消费 proof-checker 的 claim hook；handoff 最终整理。WORKSPACE 已要求贯穿更新，也保留“query pack 未收录完整实体”的实际试用结论。

本次补齐：

1. research 明确任务 wiki 路径、首次读当前宿主 skill、派发前检索、回收后写回及父调用者消费。
2. prove 入口主动检索旧实体；route-loop 实质轮次、prove 成熟产物不等终轮或整证结束才沉淀。
3. verify 的直接 Lean、确定性检查和修复分支也写准确普通实体，返回实际路径；保持原 canonical claim 合同。
4. WORKSPACE §7 提供五阶段读／写／消费表、原 helper 用法、既有正文保留、单写者、读回和下一动作。prepare、handoff、ARIS_REUSE 与 route reference 接同一段。
5. README 双语五阶段表都显式列出 wiki 操作，历史图下解释横条的实际含义。

没有更改任何原 ARIS helper、上游技能副本或 schema；没有新增 Python 平台、模型评分门、锁服务、定时器、数学研究 Goal。程序检查与原数学状态不受本次 Markdown 修改影响。

## Gemini 讨论与事实核对

一次原生续接，thread `64c8b1e2-f85c-440a-9922-dfe8ce70728a`；返回 `gemini-4-argon-high/high`、`status=SUCCESS`。请求、完整回应、原始工具返回分别为[request](gemini.request.md)、[response](gemini.response.md)、[raw](gemini.raw.json)。Gemini 静态核读维护文件，确认三处不对称及集中规程方案；未执行本次 helper 或数学程序。

采用其五阶段持续读写说明，保留原技能的 paper/idea/experiment/claim 分工。Root 直接核对 `base/tools/research_wiki.py`：upsert_idea 默认 skip；update-on-exist 重写 idea/paper 模板；add_experiment 默认 no；add_edge 不检查节点存在。操作说明据此要求读旧页后增量编辑、显式判据及先建节点后连边。

纠正 Gemini 的一项过强映射：不能一概把“全域排除”判为 no，也不能一概把条件引理当 partial；verdict 必须相对于该实验准确命题。成功完成不存在性排除可为 yes。没有明确运行判据的结果只写方法页与原证据，不强造 experiment。Canonical claim 的登记要求也不改变独立 Lean 证明的数学效力。

## 验证范围

本次核对旧实现与新调用点，并检查维护文档链接、表格列及diff；没有重跑全部未变软件或数学。原 wiki helper 的真实建页、关系、重建和实体读回已有[领域实际试用](../propertyb-rebuild/forward-use/REPORT.md)及同目录 WIKI_COMMANDS.json 记录，原结果直接复用，未称本次重跑。该试用已经暴露 query_pack 省略某些正结果正文，现规程因此坚持按实体路径读全文。

本轮文件以 docs/WORKSPACE.md §7 为共用操作入口，主入口和五阶段消费它；实际代码版本及合并记录见 Git 历史。
