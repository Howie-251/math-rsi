分类、阅读门槛、DD 的历史身份、ARIS 复用和 wiki 归属都站得住。只有一处会把模型共识重新变成前置：维护调用把 `research-review` 的 Step 4 说成了“问题清楚就返回”，被调技能的 Step 4 仍是双方同意才停。本轮 Gemini 在读、实现继续，这个执行没有被它挡住。本调用不认证证明或 v2 性能。

## 要改的一处

`base/skills/mathrsi-meta-evolve/SKILL.md` 第 4 节写：读取本仓 `research-review`，传 composed，Step 3 交回失效路径，Step 4 在问题判断清楚时返回协调者。同仓两份 `research-review` 的 Step 4 仍是：双方同意核心主张、定下实验计划、叙事结构稳定后才停。Step 5 还要收共识、claims matrix 和论文大纲。composed 只改这些内容写到哪里；没有字面参数 `— composed: <路径>` 时，它按自己的合同写独立审阅稿并走上述收束。第 4 节的可复制提示只写了“composed 维护适配”，没有这个参数。

最小修法只改这一节：写明协调者不执行 `research-review` 的 Step 4–5；提示里放上 `— composed: <本轮 EVOLUTION.md>`；一次返回失效路径、证据和最小修法即结束，由协调者决定。不要改两份 `research-review` 的通用论文审阅合同，也不要为此再开一轮。三个 Sol 的 B1、B2–B4、P1 不用停。

## 已核对且成立

分类可执行，也保住了原目标。技能第 2 节把同一证据分成 base 行为、领域知识、单题状态、暂缓。`EVOLUTION.md` 的 B1–B4、P1 都落到现有步骤：B1 在 `mathrsi-verify`、`mathrsi-research`、`mathrsi-assemble` 增加直接 Lean 分支，自然语言正式审计仍走 proof-checker；B2 在 `specify`、`prepare`、`survey`、`route-loop` 里只让竞争型基线改变队列，固定构造或证明目标继续；B3、B4 在 `route-loop` 和 `prove` 区分正证据继承、旧否证失效范围，以及路线像的并与必要门，不把局部 rank 或必要门通过写成原题已完成。P1 是返回原调用处的领域插件，不是第二条主流程。

阅读、验证和本轮执行没有无限前置。技能第 1、5 节和 `EVOLUTION.md` 写明：关键链足够就改，全库未读不阻塞；协调者自己使用，Sol 做作者和核对；不强制无历史代理重跑整题，也不重跑旧数学。当前 `docs/PLUGIN_CONTRACT.md` 第 61、71 行与此一致。`EVOLUTION.md` 把 Gemini 长读中断记为没有终稿、不计认可，实现继续。

DD 没有被写成 v1 实验。`references/evidence-and-transfer.md` 开头写明它是历史经验来源，成功、耗时和失败不归因于 v1，也不据此报告 v2 解题率。`EVOLUTION.md` 写了“不主张 MathRSI v1 已经跑出 DD”。base 里的 DD 段落是消费动作的例子，并链回该参考。

ARIS 复用是具体替换，不是空标签。`references/aris-adaptation.md` 指向四份原技能。对照原件：Claude 与 Codex 的 `meta-optimize` 都在不足五次 `skill_invoke` 时退出；Codex Step 6 是 `/meta-optimize apply` 并提醒下次再测，Claude 主线 Step 6 只暂存给 `meta-apply`；`meta-apply` 是单独人工调用，且 KILL 不能被人工翻案。数学适配明确不执行这组门槛，也不声称原版 meta-apply 已经跑过。

wiki 归属是对的。技能第 0、3 节：原任务 wiki 留在任务工作区；随插件携带的原 wiki 是只读历史库；新题写新题自己的 wiki；插件内容更新走外层维护。正在写的 `plugins/degree-diameter/skills/mathrsi-degree-diameter/SKILL.md` 让原 wiki 只负责定位，并写明不把归档原 wiki 改成新题 wiki。`PLUGIN_CONTRACT.md` 的“更新本题知识”指当前题目，且解题时不改 base。

## 实际阅读范围

全文读了 `mathrsi-meta-evolve/SKILL.md`、两份 references、`development/evolution/dd-v2-20261102/EVOLUTION.md`、`docs/PLUGIN_CONTRACT.md`。为核对五个问题，还读了两份仓内 `research-review` 的收束与 composed 段落，Claude `meta-optimize` 的只读生产者、五次门槛、模型减负和 Step 6，Codex `meta-optimize` 的对应门槛与 Step 6，以及 `meta-apply` 的人工落地门。B1–B4 只核了 `verify`、`research`、`assemble`、`specify`、`prepare`、`survey`、`route-loop`、`prove` 里已写入的对应段落；P1 只读了 degree-diameter 入口技能前 49 行和 README 的归档说明。未读 intake 长审计、461 条轨迹、archive 原文，也未执行命令、Lean 或搜索。审阅模型是本会话的 Grok。
