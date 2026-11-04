请作一次有边界的MathRSI workflow维护讨论，不审全项目、不写文件。用户查看README的五阶段表与图：prepare/handoff提wiki，route-loop/prove/verify似乎没有，问实际何时读取、写入、怎么维护。请直接读 /Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md、mathrsi-route-loop/SKILL.md、mathrsi-prove/SKILL.md、mathrsi-verify/SKILL.md，以及docs/WORKSPACE.md、docs/ARIS_REUSE.md、base/skills/mathrsi-route-loop/references/aris-review-adaptation.md、base/skills/skills-codex/research-wiki/SKILL.md。上述mathrsi-*均在同一base/skills目录。

已定位事实：route入口读wiki、终轮有实体写回和helper；prove只在交接前明确沉淀，入口不显式检索实体；verify引用proof-checker的wiki hook，但直接Lean/确定性检查分支少普通知识回写。WORKSPACE已要求贯穿更新，query_pack不覆盖实体全文。ARIS claim节点只能由proof-checker真实audit建立，不可为普通wiki更新强行跑proof-checker。upsert_idea默认skip既有页，update-on-exist会重写丰富正文；add_experiment默认no，不能把unknown误判失败。源码副本保持不变。

我拟修：在现有WORKSPACE增加共用读写操作段和五阶段读/写/消费表，不增新skill或Python平台。总控明确<W>/research-wiki，启动读index/query_pack定位，再按义务读完整实体及原证据，插件archive只读查方法。先加载当前宿主research-wiki技能，用本clone的绝对helper路径。由一个当前wiki writer串行操作，worker交局部事实/路径；重大实质结果、反例、范围修正/验证后及时写，不等整篇结束，不重复无变化导航。paper/idea/experiment/canonical claim保持既有schema；直接Lean和局部确定性证明记录到普通方法/idea正文+VERIFICATION链接，不假造claim或额外审计。正文安全增量编辑不覆盖旧证据，图关系由add_edge，刷新导航、log、读回实体；父caller读取变化和未闭义务行动。helper失败保留实际事实及待同步路径即可。README五行新增Wiki read/write列，图下写清横条含义，不必重画历史图。

请判断这是否修真正缺口，指出必要修正，并给一段简短可用于README的双语解释及五阶段读写表。HERO：不造数据库/锁服务/评分/强制定时器，不重做未变数学，不要求新无历史agent全流程。单次讨论足够。
