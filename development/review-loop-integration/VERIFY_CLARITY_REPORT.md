# verify、assemble、handoff的实际执行衔接

本次只修改三份MathRSI技能：`mathrsi-verify/SKILL.md`、`mathrsi-assemble/SKILL.md`、`mathrsi-handoff/SKILL.md`。没有改ARIS双端源码或proof-checker输入适配reference，没有启动原数学、Lean、全域复算、Goal或付费模型调用。Root另行组织的Gemini/Grok审阅不在本报告的执行范围内。

## 原来的不清楚处与本次修改

verify原稿已有详尽的正确性边界，但主要按检查类别说明，读者仍需自行还原先做什么、哪一类输入从哪里进，以及检查结果怎样接下一步。现在开头给出短执行图和四类入口表：完整现稿直接读、分散候选先assemble、局部义务隔离所需依赖、旧audit按具体断点恢复。后文仍保留详细散文，图不是必须逐节点执行的状态机。

verify明确调用formula-derivation澄清同一对象与推导、proof-writer补写已有论证、survey/research-lit定点查进口，读回结果后返回同一审计义务；研究wiki记录来源和实际用途。独立计算写清实际任务包与回收：输入、谓词、需要排除的错误、输出用途、真实覆盖和差异。完整生成、拒绝重放和原输入连接仍是不同义务。

正式proof-checker增加可直接发出的自然语言执行请求，并要求verify读取其真实产物和源改动。保留TeX/source-unit输入适配、ledger、反例pass、修复、复审与closure；Markdown转写后修复仍回写canonical正文，不以转换稿通过认证未同步旧稿。research-review只承担有明确疑问的数学咨询slot，不代替完整checker。

reviewer选择明确向research-review、checker、Lean以及handoff内部的渲染/引文审阅传递已经给出的覆盖项。解析route之后仍需按本仓REVIEWER_MCP实际调用工具，保持fresh/blind要求和宿主差异；不把选择解析器当模型执行，不重标失败或同家族provisional。checker渲染自己的audit阅读页，verify消费其真实结果；完整正文阅读页和包由handoff承担。

按Root转达的Grok具体意见，局部research-review进一步明确保留原件阅读、必要同会话证据澄清/反驳及未证项回交，数学适配不继续原Step3/4的论文共识、实验计划或叙事改写；`— composed:`只改写者，不承载该流程边界。修法归verify或prove，不由review slot另派。未修改上游research-review字节。

assemble原稿已有真实writer请求，但缺少入口到消费的短地图。新增四类输入的立即动作与返回，并强调读writer实际文件、逐处核前提供给；补文献或推导返回同一连接。高风险验证交回caller安排，避免assemble与verify重复启动完整审计。

handoff新增从正文/真实验证到阅读版本、包、读回/复现、wiki/恢复页的具体接棒表；补完整render调用说明、独占副本重放任务及可消费的返回例。已有正确正文和证据复用，展示中断只续展示；未完成研究可准确交接。仅主dispatcher启动同级后继，三者均保留该规则。

## 实际案例的依据与消费

依据为仓内`development/workflow-redesign/REAL_PROJECT_TRANSITIONS.md`，并核对其链接的T33实际caller/装配报告及ECC独立交接，不读取或更改原ECC工作区。

| 真实转折 | 本次落入的执行行为 |
|---|---|
| ECC旧43/10早期仅验保存F成员，随后第二实现重新遍历完整域 | 局部verify必须解决生成无遗漏的具体缺口；交完整集合及绑定回原pair caller |
| ECC全部必要pair无边，已足够排除三行延拓 | 消费便宜必要门回原题，停止更强且无必要的三行计算；完整生成与拒绝见证不混称 |
| T33先有24点实际caller，再闭整个24点，原题仍余23点 | 局部通过返回prove与准确remaining，不提前handoff；assemble组织实际条件供给 |
| T33六个23点分支接新Main，裸原题复述与传递公理审计 | 全局verify指名新模块，不用旧T32默认build；实际消去RemainingGoal再收束 |
| T33最终只改3292/3315及1796/844两处说明 | 按真实已核覆盖定向修正文，正确Lean不变，不重开路线或整轮计算 |
| 一般k纸面结果先完成，主定理C后来Lean，D/E继续纸面 | 按各自真实范围交付，不为统一最高验证等级重做已解题 |

这些是历史执行的流程提炼，不是本轮重新执行数学的证据。五元35的完整Lean、36研究及ECC45/11状态未升级，旧题未恢复。

## 检查范围

完成后执行三文件frontmatter/围栏检查、`git diff --check`和仓内`tools/check_links.py`一次。结果附在下方。文档与链接检查不证明流程的长期效率或新的数学结论；本轮没有声称三个技能已完成真实新题端到端行为试跑。

- `python3 tools/check_links.py`：exit 0，53份文档、942个本地链接目标，0 missing。
- 三份SKILL的frontmatter与代码围栏检查：exit 0，均通过。
- 三份SKILL及本报告的`git diff --check`：exit 0，无空白错误。
- 随后按Grok具体意见补充的research-review段落不增加链接、frontmatter或围栏；该补充已核读与既有单caller约定相容。
