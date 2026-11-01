# 工作流设计与成稿审阅处置

2026-11-01。本轮对象是MathRSI技能的实际编排和经验提炼，不是重新认证历史数学结果。Gemini参与设计和正文结构讨论；Grok提供独立架构与成稿批评。两个模型均静态读材料，没有运行本轮数学程序或Lean，不能以其意见替代行为测试。

## 调用与实际范围

- Gemini原会话`1ad5d3b8-d2e7-4d79-8c3a-b2dd65ff5ec9`：初步workflow设计、五组子流程修订、具体成稿阅读。三轮实际返回`gemini-4-argon-high/high/SUCCESS`，effort来源为CLI selected variant。完整原件见`GEMINI_WORKFLOW.raw.json`、`GEMINI_NESTED_REVISION.raw.json`、`GEMINI_IMPLEMENTATION_REVIEW.raw.json`及对应请求。它的“全读”范围是其回复声明，Root没有据此宣称它执行了程序。
- Grok原会话`dee1cc32-f026-4dcc-b037-533ddb816b1a`：嵌套架构讨论、具体成稿审阅，实际返回`grok-4.7-build/xhigh/end_turn`。原件见`GROK_NESTED_WORKFLOW.raw.json`、`GROK_IMPLEMENTATION_REVIEW.raw.json`。成稿轮明确未读ARIS上游全部正文或两题archive源，只根据当前技能和实证报告核对执行衔接；原项目事实另由Root/Sol阅读原件支撑。
- Sol三组作者完成上游阅读、独占技能实现和互相衔接核查；属于同家族。实际行为试用另见[REPORT](behavioral-trial/REPORT.md)，其fresh局部审阅也如实provisional。

## 采纳、修正和保留的判断

| 具体意见 | 处置与实际改动 |
|---|---|
| 主入口原先是规则而非编排 | 改成五子工作流，包含实际调用内容、产物消费、后继和正常回流；每个子流程有可独立完成的任务 |
| 设计初稿把路线审阅与完整证明审计混在一起 | route-loop单独持有路线迭代；verify消费proof-checker自己的完整修复回路；单数学review slot明确是适配，不冒称整个原ML循环执行 |
| Grok初步建议只新增一个路线技能 | 未将目录数量当约束。用户确认五组子工作流；specify/survey/assemble等分别有数学规格、进口核读和实际caller装配职责，已以具体内容交成稿审阅 |
| Gemini初步建议中的统一字段/flag或模型最终否决 | 未照搬不存在接口或评分门。原模型意见可据证据反驳，原始回应保留；局部预算不自动暂停Goal |
| Gemini与Sol发现主入口四处链接多一级 | 已改成仓内三层相对路径，本地链接检查通过 |
| Gemini发现ECC原交接已入库但报告仍说未入库 | 报告改为准确前后阅读范围，优先引用两份原交接；实际收录文件显式纳入版本管理 |
| Sol发现审计TeX修复未回写原Markdown | 新增实质修复反向同步、对应核对和唯一正文owner，最终交付正文须对应最后实际audit |
| Gemini建议避免机械双份正文 | 新正式审计稿可直接以TeX为唯一源；已有MD需要保留才做适配；短稿对应可写入原audit说明，不强制新文件 |
| Grok发现specify和prepare都可能执行survey | specify初步只返回调查委托；prepare执行一次survey，再显式final |
| Grok发现survey回流可能误送specify | survey入口及结尾按caller返回：route/prove回原义务，prepare回prepare，不自行改目标 |
| Grok发现父子都启动下一阶段 | 主入口及所有相关子技能统一：子流程返回产物/剩余/建议next，直接父调用者调度一次；内部探针、survey、局部verify照常实际执行后返回 |
| Grok发现Property B文献入口只有主流程指示 | survey增加实际propertyb-literature调用、archive种子/误读核对及共享单次research-lit，唯一LITERATURE writer合入领域提取 |
| Grok建议二元码自动读取旧ECC插件 | 未采纳自动加载。ECC草案尚待用户指定领域agent完善；本轮复用已授权原交接的经验，成熟插件由用户/任务明确启用 |

## 验证边界

[本地记录](VALIDATION.json)保存九项技能格式和维护链接检查，以及相对别名搬迁检查。[行为试用](behavioral-trial/REPORT.md)实际验证已有方法入口、领域L7/ARIS writer、精确算例、局部verify及返回prove；它没有执行完整新题广搜、路线多轮MCP、正规proof-checker或Lean。

本轮没有通用效率/解题率实测，也没有把模型同意当作性能或数学证明。修正后的父子控制权另做Grok定向复核，请求保存在`GROK_FIX_REVIEW_REQUEST.md`。

## 修订后的定向复核

Grok同会话有效返回`grok-4.7-build/xhigh/end_turn`，完整原文为`GROK_FIX_REVIEW.raw.json`。它重新静态读取九个MathRSI入口、verify输入适配及领域literature输出约定，确认前轮四项控制冲突已消除：初步规格不重跑survey；survey按原caller返回；父子不重复启动同级阶段；Property B文献能力进入实际共享调查。它也确认TeX单源及修复回写约定已写入，没有执行程序。

Root核对修订文件与本地检查，接受这些控制问题已在当前正文中解决。Gemini成稿意见的两项旧路径/来源陈述问题已修并由本地检查覆盖，TeX单源建议已落地；没有额外声称Gemini又审过最终修订。行为试用仍只支撑其明确执行路径，完整新题调查或长期求解的实测留待真实任务。
