# v3 README 与发布处置

用户要求在 README 说明 v0、v1、v2、v3 分别改了什么，与 Gemini 讨论后将完整 v3 一并 PR 合入。Root 提供实际标签、变更记录、维护审阅与有界使用结果；Gemini 主写双语草案，Root 核实采用。固定入口：[v3](https://github.com/lisresearchgroup/math-rsi/tree/v3)；旧 v1/v2 标签不移动。

## 实际讨论

- 会话：`64c8b1e2-f85c-440a-9922-dfe8ce70728a`，沿原 Gemini 会话一次续接。
- 返回 `gemini-4-argon-high`、effort `high`、`effortSource=cli_selected_model_variant`、`status=SUCCESS`。
- [请求](gemini.request.md)、[完整原回复](gemini.response.md)、[原始工具返回](gemini.raw.json)均保存。
- 本次是 README 组织与事实表达，不是新增数学审阅；此前 Gemini/Opus 各两轮维护审阅及实质修法见[原处置](../reviews/DISPOSITION.md)。

## 采用与事实核对

采用“版本—经验来源—具体工作流变化—领域能力”演进表及“四类问题—实际动作—所属流程—来源工具”表；两张旧图移入明确的 v2 历史折叠区。保留 Gemini 的正文结构与主要表达，版本表压缩为读者可以扫描的实际区别；领域详细证据继续链接原报告。

Root 按实际实现纠正草案：

- 不能写“四代始终十技能”：v1 是九项解题技能，v2 增加独立 meta-evolve 后为十项，v3 保持十项。
- v0 已有数学量词与核验实践，只是尚无共享 MathRSI 总控；没有把旧技能写成完全不跟踪量词。
- PR #7 晚于固定 v2 标签，是其后主线日常修补并进入 v3，不写成固定 v2 已含该提交。
- Erdős 86 研究 C4-free 超立方体子图；未采用草案的 induced-four-cycle 表述。
- 领域源码和真实方法来源保留历史归属。新技能维护实用检查不改写成 v3 重解原题或等预算效率实验。
- 公开基线改变的是竞争研究队列，不废除用户固定目标或旧定理的数学有效性。

用户随后明确要求把“强化base workflow”和“扩大、深化plugins”分成两条演进线；README导语、版本表列名和v3两组章节已据此组织。技能数保持十项不代表base未增强，实际强化以原技能新增的研究动作及使用记录为依据。

README、快速开始、V3_CHANGES、演进说明和当前维护入口同步发布态。代码与数学证书在前次集成中已完成适用检查；本次只改变文档，核链接、版本事实与 diff，不重复未改动的数学重算。

## 发布范围

完整 v3 已有实现、六领域十四技能与科学资料随同发布。PR #7 原作者提交保留，提交与合并使用用户指定的 wanshuiyin 身份；仓库可见性保持私有。沿既有固定版本约定在合入后的完整快照创建 v3 标签，README 提供 v1/v2/v3 浏览及 ZIP 入口。GitHub main、v3 refs 与合并 PR 是最终提交记录。
