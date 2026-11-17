# RESET-R14 文档转写与文件完整性检查

日期：2026-10-22。本检查只核对主会话给定正文的转写、文件保存、字节保护和入口一致性；不推导、补证、独立审阅数学或检查数学原创性。全部新增unreviewed/unaccepted；主会话自检与本检查均非独立审阅，不升级接受或assurance。不启动review、研究代码、SAT、枚举、求解或实验，不运行数学、坐标或枚举程序。

## 1. 起始来源与保护方式

[R14来源清单](RESET_R14_SOURCE_MANIFEST_20261022.json)以[R13清单](RESET_R13_SOURCE_MANIFEST_20261022.json)现有64项保护文件为基础，加入R13正文、[R13文档检查](RESET_R13_DOCUMENT_CHECK.md)及R13清单，形成67项当前字节基线。原64项与R13记录相比当前bytes/hash差异0；创建前没有R14或更后轮次文件。清单另保存8入口原始字节的base64、bytes/hash和原task值，用于发现并行变化，不是依旧hash恢复历史版本的指令。

本轮仅新增3文件：R14正文、R14来源清单、本检查；按授权同步8入口：task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl、check.jsonl。合计11文件。曾为本轮新稿临时使用的文件名RESET_R14_TWO_ANCHOR_REPAIR_AND_JOINT_CARRYING.md，在确认指定目标不存在、原新稿hash未变且绝对路径位于本任务内后，仅移动为用户指定的RESET_R14_JOINT_REALIZABILITY_AND_GLOBAL_DEFICIT.md；旧临时名不再存在，未移动任何R1—R13文件。

R1—R13、[INITIAL_BASELINE](INITIAL_BASELINE.md)、[归档](../archive/2026-10-19-paused-route-rounds-1-4/README.md)、来源原件与副本、旧检查与manifest、旧接受、assurance、证明绑定、运行与会话指针保持。67保护项包含只读heptagons.tex接口，未新执行证书或迁移数值。归档MANIFEST列出的27份snapshot逐项核对bytes/hash；计划原件、原字节副本和PDF原件三项来源逐一核对，未复制PDF。

## 2. 正文转写与主会话限定

[完整R14正文](RESET_R14_JOINT_REALIZABILITY_AND_GLOBAL_DEFICIT.md)0—7节全部由主会话提供。路线A保留完整两锚点等价证明、单点侧与空eligible、2A2B退化分支、link总序、两置换图精确独立集模型、同一C的联合团容量、链分层及跨方向proper修复的完整兑现。允许空侧联合τ恰旧M−J、固定锚H20及22点完整signotope校准的范围均保留；未将其写成新的全局改善。

路线B保留全部实际完整/缩短尾、C(Q)/S(Q)、全部pair的h嵌套、实际红蓝秩、符号反射计数及整块carrier容量，完整转写≤6的全替代尾反共享见证、共同覆盖子类M≤51、双hub的非空核心条件、共同短尾逃逸和全替代中间供应者的≺_0关系、pB粗界。不同Q、共享/分散/嵌套、共后继和无最高阶fan等分支均未删去。

主会话最后给定的四项精确澄清已转写：§4.2链为原点序与link总序定义的二元偏序链，非原rank3单色路径；§6.3红秩在整个C(T)重算，后接T证明只用母红max p，不直接搬S秩；§6.1双hub只在K/E均非空时使用min/max，空核心由δ≥B处理；§5.2反射初段后的起点、终点及E/S步数完整列出。未自主补推导。

来源阅读记录归主会话：R13、R12§2—5.1、R11§6—7、R7§1、计划§4.5—5.4、current cardinality定义/Lemma2单射及既有C1—C7/C9/C10范围；清单保存路径、当前bytes/hash及主会话阅读归属。文档代理不将hash或文件存在检查当作来源数学的独立审阅。C8/A[8,8] pending、same-family/provisional和精确model/backend/actual effort未知不可核实等边界保持。

正文§7依赖链表、边界与共同实现自检、全分支兑现和停止处均为主会话给定。小δ全模型增强目标明确未完成；22点校准不称几何实现、全局repair最优或近饱和反例，短尾e8/m7的26点人口只称松弛尚未排除。

## 3. 八入口同步与原历史保护

主会话明确授权同步后，共进行8次入口写入。每次写入前均核对全部8入口的预期hash：未写项用起始值，已写项用本轮记录值。8次全部通过，没有覆盖外部变化；清单保存8项最终bytes/hash和逐次核对标记。

prd/design/implement/stage/README五份Markdown均仅前置R14当前段，原R13及其全部历史内容作为完整原字节后缀保留，逐一base64字节比较均为true。两个JSONL保留原28行的完整原字节前缀、全部原路径及历史reason，各追加R14正文和清单两项，变为各30条；新增reason明确只作转写与文件检查、unreviewed/unaccepted，不作review。未把旧行的历史reason冒充本轮审阅。

task.json只修改description、notes及meta下restart_scope、current_analysis_path、previous_analysis_path、current_analysis_status、current_round_date。删除这些授权字段后，修改前后其余JSON序列化严格相同；原R13 notes也完整作为新notes后缀保留。current R14、previous R13；id、createdAt、status=in_progress、completedAt=null、原acceptance_status及其他字段保持，长期任务未完成。

## 4. 数值转写与直接文件证据

数字仅按主会话给定值作跨文件转写比较，不运行数学计算程序。全模型41/52/83/165、普通O26/30/31/32、gap粗界15/22/52/133、J27/31/53/84保持；几何历史40/49/79/80及gap14/19/48/48分列，历史45/58/103/206不回写。M=O+e_occ−m_missing不登记为精确极值。

新结构直接全局、递推传播、既有工具新全局数值迁移、外部新增四类收益均0。766“一个实际完整红四点尾覆盖全K，或对偶完整蓝前缀覆盖全E”子类M≤51单列，不传播为全局。carrier≤25依赖旧C1—C5，不是独立N756≤25；原独立26及R8传播只沿用，无fan25/窗口25/条件82不用作新全局界。未证repair≤20、K/E普遍共享覆盖及未知统计量均不登记收益。正文及入口保留原句：就本轮新结构的独立贡献而言，本轮尚未进一步缩小全局 gap。

初检直接raw evidence：67/67保护bytes/hash相同，27/27归档相同，3/3来源相同，8/8最终入口hash一致；8次写前全部8入口核对均通过。task非授权字段相同、原notes后缀保留true；五Markdown原历史后缀与两JSONL原前缀共7项字节比较全部true。两个JSONL各30条，原28路径各保留，60/60引用存在。

正文0—7共8节，60对显示公式定界成对；初检6份当前Markdown共43行表格列数一致，122项本地链接中仅6项指向随后创建的本检查，其余均存在；无行尾空白或冲突标记。本检查创建后，再对7份当前Markdown、全部11文件和完整保护链终检，实际结果记录下文。

直接证据来自PowerShell文件读取、JSON/JSONL解析、Get-FileHash及字节比较。.trellis被gitignore忽略，空git diff不作为文档证据；未改.gitignore或git add。本检查不构成独立数学审阅或正式接受。

[当前阶段](../STAGE_SUMMARY.md) · [PRD](../prd.md) · [设计](../design.md) · [执行记录](../implement.md) · [研究入口](README.md)

最终正文31896字节，SHA256为5C670BCCA68CB5C4AB7EFE2D225F04836B91F61511BD2B01590B747F22F85838；最终R14来源清单160949字节，SHA256为DF72A92F57BF38548F21E61BAA87B8DE75FFE9C423CEF6AC4F2278AB84808E0F。

直接终检raw evidence：67/67保护bytes/hash相同，27/27归档相同，3/3来源相同，8/8最终入口bytes/hash相同；8次入口写入前全部8入口预期hash核对通过。五Markdown原历史完整后缀及两JSONL原完整前缀共7项字节比较全部true；task非授权字段差异0、原notes完整后缀保留true。两个JSONL各30条，原28路径及历史reason保持，60/60引用存在。7份当前Markdown的133/133本地链接存在，43行表格列数一致，全部11份本轮文件无行尾空白或冲突标记。正文0—7共8节，60对显示公式定界成对，阶段性待转写提示已清理；失败项0，无文档阻断。

主会话报告已复读最终正文0—7及当前task/README，四项澄清已落实，无新增数学转写修订；这不作为独立数学审阅或接受。current R14/previous R13、in_progress、completedAt=null及原acceptance_status保持，全部新增unreviewed/unaccepted，长期目标未完成。本报告及上述终检仅为文件与转写一致性证据。
