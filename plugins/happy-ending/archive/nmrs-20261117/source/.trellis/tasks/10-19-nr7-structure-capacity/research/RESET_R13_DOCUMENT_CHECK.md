# RESET-R13 文档转写与文件完整性检查

日期：2026-10-22。本检查仅核对主会话给定文本的转写、来源保存、字节保护和入口一致性；不推导、补证或独立审阅数学，不检查数学原创性。全部新增unreviewed/unaccepted；主会话自检、本检查均非独立审阅，不升级接受或assurance。不启动review、研究代码、SAT、枚举、求解或实验，不运行数学或坐标计算程序。

## 1. 来源与保护基线

[R13来源清单](RESET_R13_SOURCE_MANIFEST_20261022.json)起始保护集为R12清单60项，加R12正文、文档检查、清单，共63项。与R12保护集相比，旧60项当前bytes/hash差异0；不把旧hash作为恢复目标。[R12清单](RESET_R12_SOURCE_MANIFEST_20261022.json)和[R12检查](RESET_R12_DOCUMENT_CHECK.md)本身保持。

经主会话授权，新R13清单另追加heptagons.tex只读接口依赖，保护集共64项。其绝对路径为D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/heptagons.tex，12887字节、SHA256为7B74BBF577036C1BB02E72F6B2422FB4F11893D836B11C98044D7774B5B8F706。标签为“主会话仅rg接口定位，无迁移/证书执行”；文档代理只定位和hash当前字节，未读数学推导，不改任何旧manifest。

计划原件、原字节副本与PDF原件三项来源保持；未复制PDF。归档MANIFEST列出的27份snapshot原文另逐项核对字节/hash。R1—R12、INITIAL_BASELINE、来源原件/副本、旧检查/清单及旧接受均保护。[当前cardinality](../../09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md)、[C6](../../09-03-35-state-cardinality-charging/research/c6-formal-acceptance-20261016.md)、[C7](../../09-03-35-state-cardinality-charging/research/c7-formal-acceptance-20261020.md)、[C9/C10](../../09-03-35-state-cardinality-charging/research/c9-c10-formal-acceptance-20261022.md)原范围不升级；独立N756≤26、C8/A[8,8] pending与same-family/provisional、精确model/backend/actual effort未知不可核实边界保持。

清单完整记录8入口起始原字节的base64、bytes/hash和原task值，用于发现并行变化；它们不是按历史版本回滚的指令。清单保存每次写入后的最终入口hash，旧入口快照仍保留。

## 2. 转写内容与主会话修正

[R13完整正文](RESET_R13_GLOBAL_STRUCTURE_AND_JOINT_CAPACITY.md)0—8节全部由主会话提供。保留完整路径族抗删除的量词及不交路径证明、两侧极值fan桥和二维包络、无fan诱导容量的目录计数、766全部阈值分支、一般混色边界删除修复上下界、极大匹配证明、任意预先指定方向序列的联合不交障碍证明，以及联合最优cut/方向/D、所有批次与一D/二D/三D完整投影、ambient/内部pair秩拼接的全证明与范围。

两次完整兑现、实质修复与未排除分支均保留，不以摘要取代正文。主会话阅读后指定的定义及措辞修正已经转写：首列757；weak长度和恰n+2及保端点缩短；h20/L1=15限766；C_b是选定有效上界；§4.4先限766 p5/a4；少于6−ε_K的横截量词；计划实际阅读粒度；高度共享只在足够小横截前提下排除；K端/E首镜像方向；额外红5末对蓝秩≤3仅为未排除支；ε_K/ε_E账本；766整个缺额范围及合格cut侧长条件。

主会话最后补充的两项数学亦完整转写：26点核心至少2个实际异常owner给出3阶fan attainment而不强制4阶；一般a=p−1强fan与尾点人数的遗传容量兑现整族恒0，全红p−1配置只校准子模型，不声称已嵌入近饱和母配置。这些均由主会话提供，本检查不独立判断证明。

全部方向序列结论保留总数限定：766 δ=0、1、2可预定4正3反，共7条不交真边，不把独立两次7相加成14，也不保证AAB/ABB子类型，不声称近饱和X已构造。线性横截下界不是缺额收益；另一方向的足够小实际修复上界未证，不能倒置不等式。

主会话来源阅读记录以正文为准：R12联合切分与J、R11核心、R7规范端点分解、R9§2、R10§1—2、当前cardinality定义/Lemma 2及既有接受范围；计划第4/6/7节原文及第5/8节条目。heptagons.tex仅接口定位，不新迁入19/25/49，不执行证书或重验收。计划中的计算建议不是运行授权，不声称新文献原创。

## 3. 八入口同步与状态保护

本轮新增3文件：R13正文、R13来源清单、本检查；同步8入口：task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl、check.jsonl。合计11文件，没有新增研究程序或其他报告。

初次8次入口写入及主会话补充整族零收益校准后的8次同步，共16次写入前，每次均核对全部8入口的预期hash：未写项使用起始值，已写项使用本轮记录的新值，16次均通过，无并行差异。最终8入口hash与清单最终预期值一致。校准限定已同步全部8入口：停止单极值fan加尾点数量这一遗传容量粗化的局部常数优化，不否定更强ambient联合条件，也不把全红p−1子配置称为近饱和母配置。

PRD、design、阶段与研究入口在当前R13内容之后完整保留原R12文本，逐字后缀比较均为true；不回写旧历史。implement仅更当前标题/导言并追加R13，原导言之后的R1—R12及归档执行历史逐字前缀比较为true。

两个JSONL原26项引用路径全部保留，各追加R13正文与manifest后为28项。仅将前两项当前入口reason同步R13，原其余引用保留，56项文件引用均存在。

task.json只修改description、notes和meta下restart_scope、current_analysis_path、previous_analysis_path、current_analysis_status、current_round_date。删除这些授权字段后，修改前后其余JSON字段序列化严格相同，未授权字段差异0。current R13/previous R12；id、createdAt、status=in_progress、completedAt=null、原acceptance_status及其他字段保持，长期任务未完成。

## 4. 数字、链接与直接文件证据

数字仅按主会话给定值作跨文件转写比较，不运行数学计算程序。全模型41/52/83/165，普通O26/30/31/32，gap粗界15/22/52/133；几何分列40/49/79/80与gap14/19/48/48，历史口径保持。R12的J27/31/53/84不重复登记为R13改善；指定方向序列δ_T=0时数量5/7/10/27是必要条件，不是新全界。

四类全局收益均0：新结构直接、递推传播、旧工具新全局数值迁移、外部新增。C3≤25只限无指定fan类，不等于独立N756≤25；原独立26及R8传播仅沿用，窗口25/条件82不用，未证β/a/b不登记。正文及8入口保留原句：就本轮新结构的独立贡献而言，本轮尚未进一步缩小全局 gap。

初检直接raw evidence：64/64保护bytes/hash相同，27/27归档原文相同，3/3来源相同，8/8最终入口hash一致；task非授权字段相同；4份入口完整R12历史及implement历史保留true。两JSONL各28条、56/56引用存在、原26路径各保留。6份当前Markdown的111项本地链接中，6项指向随后创建的本检查，其余全部存在。32行表格列数一致；10份已存在本轮文件无行尾空白或冲突标记。正文0—8节齐全，共31对显示公式；该检查不构成数学审阅。

本检查建立后，对全部11文件、7份当前Markdown以及保护、归档、来源、JSON/JSONL、入口和历史再终检，实际结果记录在下文。直接证据来自文件读取、JSON解析、Get-FileHash及字节/文本比较；.trellis被gitignore忽略，空git diff不作为文档证据，未修改.gitignore或git add。

旧接受、assurance、证明绑定、运行与会话指针保持；本检查不构成正式接受。

[当前阶段](../STAGE_SUMMARY.md) · [PRD](../prd.md) · [研究入口](README.md) · [旧R12检查](RESET_R12_DOCUMENT_CHECK.md)

直接终检raw evidence：64/64保护bytes/hash相同（63旧项及1只读tex接口），27/27归档原文相同，3/3来源相同，8/8最终入口hash一致；16次入口写入前全部8入口预期hash核对均通过。task非授权字段差异0；PRD/design/stage/README原R12全文与implement历史保留全部true。两JSONL各28条、原26路径各保留，56/56文件引用存在。7份当前Markdown的123/123本地链接存在，32行表格列数一致，全部11份本轮文件无行尾空白或冲突标记。正文0—8节共9节，31对显示公式定界成对；失败项0，无文档阻断。

最终正文27664字节、SHA256为21809EF9B68A3A997A662DA119490158C80B8EA1E9C0E40076454AF6823F3B45；最终R13来源清单133511字节、SHA256为DD31A485F7239D047A17BED9ED0D8C54AD6CF57676D6079CF66F04A3B9ADE0F2。正文§4.4最后仅将易误读的“p−1/2”转写为“最大红、蓝路径长度分别为p−1和2”，不改数学或其他入口。current R13/previous R12、in_progress、completedAt=null及原acceptance_status保持。该直接文件/转写终检不构成独立数学审阅或正式接受。
