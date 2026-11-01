# 来源与复用

MathRSI 首版以用户维护的 [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) 和 Property B、ECC 两项实际研究为基础。用户明确授权复用 ARIS 内容，并要求保留其详细解释与可执行衔接，同时提高数学研究效率。

## ARIS

开发时读取的本机主仓库提交为 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`。用户指定参考 [auto-review-loop/SKILL.md](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/c485faa59a68e51c6575dea67ca57abc7a6a2b9c/skills/auto-review-loop/SKILL.md)。借鉴其持续状态、原始审阅回应、实际修改后再评估和恢复方式；没有将实验评分阈值搬成数学定理的接受标准。

按具体任务继续复用 ARIS 的文献、wiki、推导、证明、审阅、Lean 与展示技能，见 [复用说明](ARIS_REUSE.md)。实际使用时读取本仓固定快照对应的宿主版本；上述提交标记首版来源，不表示所有本地安装均与该提交完全相同。

ARIS 使用 MIT License，Copyright (c) 2026 wanshuiyin；本仓库保留其完整许可证 [LICENSE](../LICENSE)。MathRSI 的重组与领域适配由用户授权开展。

## 两个领域的研究经验

Property B 来源包括原题规格、实际证明连接、可复用引理、失败地图、六／八／九元方法与通用下界经验。ECC 来源包括旧题完整不存在性证明、新题未闭义务、实际计算成本及独立领域交接。可定位的原材料名由各插件 source map 保存；Property B完整知识与源码已本地归档；精确选择和缺失大数据范围见plugins/propertyb/knowledge/README.md。研究状态不冒作新系统能力。ECC当前仅保留旧草案，等待另一位领域agent维护。

首版架构此前经过 Gemini 4 讨论；本次实现阶段继续与 Gemini 4、Grok 讨论。实际请求、回复与采纳记录在本地开发记录中，最终范围见 [首版验证](../development/VALIDATION.md)。这些是工作流设计与使用检查，不是通用数学求解能力或 RSI 增益的实证。

## 自包含修订

上游30技能双端完整目录、两套shared-references、53 helpers、leaf与许可证已复制进base。逐文件来源在[ARIS_SNAPSHOT.json](../base/ARIS_SNAPSHOT.json)，实际副本核验见[验证记录](../development/VALIDATION.md)。不依赖原aris_main或全局skills。新增Property B四入口与详细数学/实务库是MathRSI适配；原文和已复用源码不伪称本次新作。论文PDF与第三方历史原件的版权仍归原作者，MIT不重新许可这些档案。

同一上游提交的Grok、Antigravity、Codex和Claude-review四份Python桥接现位于[mcp-servers](../mcp-servers/README.md)，实际服务源码保持原字节，测试定位和本仓安装说明的改动列在[SOURCE](../mcp-servers/SOURCE.md)。该附加包独立记录来源，不更改原207文件base快照。模型CLI和登录是运行环境依赖，另一份ARIS checkout不是依赖。

当前route-loop是原auto-review-loop的明确数学适配，执行其改进链并按数学任务替换原ML对象/停止判断；其余MathRSI流程实际调用固定的ARIS能力。原始设计意见、修复和复核见[本轮处置](../development/review-loop-integration/REVIEW_DISPOSITION.md)。跨模型讨论、静态消费审计和实际协议/模型调用分别记范围，不宣称全部数学研究能力已获新题长程验证。
