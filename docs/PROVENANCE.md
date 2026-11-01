# 来源与复用

MathRSI 首版以用户维护的 [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) 和 Property B、ECC 两项实际研究为基础。用户明确授权复用 ARIS 内容，并要求保留其详细解释与可执行衔接，同时提高数学研究效率。

## ARIS

开发时读取的本机主仓库提交为 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`。用户指定参考 [auto-review-loop/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/c485faa59a68e51c6575dea67ca57abc7a6a2b9c/skills/auto-review-loop/SKILL.md)。借鉴其持续状态、原始审阅回应、实际修改后再评估和恢复方式；没有将实验评分阈值搬成数学定理的接受标准。

按具体任务继续复用 ARIS 的文献、wiki、推导、证明、审阅、Lean 与展示技能，见 [复用说明](ARIS_REUSE.md)。实际使用时读取当前安装的宿主版本；上述提交标记首版来源，不表示所有本地安装均与该提交完全相同。

ARIS 使用 MIT License，Copyright (c) 2026 wanshuiyin；本仓库保留其完整许可证 [LICENSE](../LICENSE)。MathRSI 的重组与领域适配由用户授权开展。

## 两个领域的研究经验

Property B 来源包括原题规格、实际证明连接、可复用引理、失败地图、六／八／九元方法与通用下界经验。ECC 来源包括旧题完整不存在性证明、新题未闭义务、实际计算成本及独立领域交接。可定位的原材料名由各插件 source map 保存；本仓库不复制大型扫描数据，不将源项目的研究状态冒作新系统能力。

首版架构此前经过 Gemini 4 讨论；本次实现阶段继续与 Gemini 4、Grok 讨论。实际请求、回复与采纳记录在本地开发记录中，最终范围见 [首版验证](../development/VALIDATION.md)。这些是工作流设计与使用检查，不是通用数学求解能力或 RSI 增益的实证。
