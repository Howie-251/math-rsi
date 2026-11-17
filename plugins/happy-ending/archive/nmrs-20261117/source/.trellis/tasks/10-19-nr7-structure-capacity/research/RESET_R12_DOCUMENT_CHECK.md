# RESET-R12 文档转写与文件完整性检查

日期：2026-10-22。本检查仅核对主会话给定文本的转写、来源保存、字节保护和入口一致性；不补证、不独立审阅数学，不检查数学原创性。新增推导全部unreviewed/unaccepted，主会话自检和本检查均非独立审阅，不升级旧接受或assurance。不启动review、研究代码、SAT、枚举、求解或实验；不运行坐标或数学计算程序。

## 1. 来源与当前字节保护

[R12来源清单](RESET_R12_SOURCE_MANIFEST_20261022.json)是本轮新建的当前字节快照：R11清单原57项，加R11正文、R11文档检查及R11清单，共60项。清单本身30211字节，SHA256为CC6A880EF341B9586E283DE3A302AB01C70C9009F59EFA8C31B4380A055D3BB2。原57项与R11记录差异0；只记录当前版本，不按旧hash恢复。

[旧R11清单](RESET_R11_SOURCE_MANIFEST_20261022.json)自身SHA256仍为F9C13A96B5D0D3792125A9F389FD9D221E6AD43020EFA8A6D7CF7EF4C0B96887。R1—R11/旧检查/旧清单、INITIAL_BASELINE、全部归档和旧依赖均保护；旧归档MANIFEST中的27份snapshot原文另逐项核对字节/hash。

计划原件C:/Users/astro/Downloads/DOWNSET_INTEGRATED_RESEARCH_PLAN.md与[原字节副本](sources/2026-10-21/DOWNSET_INTEGRATED_RESEARCH_PLAN.md)均45715字节、SHA256为27CE02EB8797CCC2D89D814316B87C304FE6258FE3209C130819BAD330045C63。PDF原件D:/科研/math agent/ref/erdos_szekeres_upper_bounds_v1.pdf为199668字节，SHA256为F47C8CC16D4A1D8A5D483B79AA98F97C57919822DCD37DAC1B17A757E919F4C5；没有复制PDF或改动来源。

[当前cardinality](../../09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md)仍18010字节、SHA256为CFCAB4764AC1F40BF37FA7B8B761EE1CDBC3D004F3E64FB8074F001F7EE699D2。独立N756≤26沿C1—C7/C9/C10与C8/A[8,8] pending的原范围；[C9/C10接受](../../09-03-35-state-cardinality-charging/research/c9-c10-formal-acceptance-20261022.md)、旧C6/C7及same-family/provisional和精确model/backend/actual effort未知不可核实边界均保持，不重验、重放或升级。

## 2. 本轮文件与入口同步

新增3文件：R12来源清单、[R12完整正文](RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)、本检查。同步8入口：task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl、check.jsonl；本轮合计11文件，没有新增其他报告或研究程序。

同步前8入口hash及60保护文件字节/hash均与本轮起始快照相同。八次入口写入前各自重新核对全部8入口的预期hash：未写项用起始hash，已写项用本轮已记录的新hash，8次均通过，无并发差异。写后再按最终预期hash检查入口。

主会话最终措辞修正仅将task.meta.restart_scope中的“unbounded prime branch”改为“prime excess bound unresolved”；该次写入前也核对全部8入口预期hash并通过。此限定不表示prime规模无界，既有有限全局界仍适用。

implement只替换当前标题/导言、在末尾追加R12，原导言后的全部R1—R11历史文本逐字保留，前缀比较true。两个JSONL原24项文件引用逐一保留，新增R12正文和manifest后各26项；没有删改旧引用路径。

task.json只更新description、notes及meta下restart_scope、current_analysis_path、previous_analysis_path、current_analysis_status、current_round_date。去掉这些授权字段后，修改前后其余JSON字段序列化严格相同，未授权字段差异0。current R12/previous R11，日期2026-10-22；id、createdAt、in_progress、completedAt=null、原acceptance_status及其他未授权字段保持，不宣告长期完成。

## 3. 主会话材料的转写范围

正文0—10节完整合并主会话三批材料和后续明确补充，不以摘要替代证明：A两个供应次序的逐包末点搬运、实际完整前缀保留、i0空类和未获得拥塞收费；B精确path公式、全部端点weak等价、Φ两闭式及推导、目录无重叠联合不等式、递归类精确解析/几何构造、实际切分树及望远镜恒等式均保留。

A重复供应下的多对一严格限定为条件分支：未证明或构造目标近饱和区间的大规模实现。只有第7节p≥4/n≥2p−1的δ0四群/两核心族是完整构造的共同高复用例；n7p5明确违法，不作766反例。五点几何prime例按主会话给定坐标、十个三元色、五个四元包及四种切分失败逐项转写；最小prime5、M5/δ47仅证分支存在，远离近饱和且自身无正gap，不反驳近饱和prime容量候选。

r_K/b_K的本节顶点数定义与downset各减1区别已补；无weak n排单色n、故a,b≤n−1的主会话说明已补。主会话指定的10组核心公式采用标准LaTeX显示公式，开闭定界成对；不改数学或数字。结构为本轮新提炼而不声称文献原创，经典cups–caps递归思路和自足证明的归因保留。

主会话实际阅读记录保留R5§2—8、R7§1—3、R8§9.1—9.3、R9§2、R10§1及§5—8、R11全文、计划与当前cardinality Lemma2/26范围；旧paper-05页图只视觉核对三链桥接，不新迁入25/49/19/16，不重放、不重新验收。计划中的计算建议不是运行授权。

## 4. 数字、状态与直接核验

数字只按主会话给定值作跨文件转写比较，没有运行数学计算程序：全体N为41/52/83/165、普通O26/30/31/32、gap15/22/52/133；根切分J27/31/53/84、已证明条件收益14/21/30/81；递归全可分类精确O单列。766δ<21/M>31的结构排斥、prime未量化分支及条件收益不能传播到全局的范围保持。

五类审计保持：新结构直接全局0、递推0、旧工具新全局迁移0、外部新增0；prime无新上界，不登记β/a/b，14/21/30/81是已证条件子类收益。历史和几何口径不回写，窗口25和R10条件82不用。正文、PRD、阶段与入口保留原句：就本轮新结构的独立贡献而言，本轮尚未进一步缩小全局 gap。

直接文件初检raw evidence：60/60保护hash及bytes相同，27/27归档原文相同，2原件和1副本共3项来源相同；R12清单自身hash不变。task/manifest JSON与两个各26条JSONL解析有效，52/52文件引用存在，原24项引用各保留。初检6份当前Markdown的84项本地链接中，6项指向随后新建的本检查，其余均存在；本检查建立后将全部链接一起终检。正文0—10节共11节齐全，无待填占位；10组显示公式定界成对。初检41行表格列数一致，数字表逐项与给定文本一致，10份已存在本轮文件无行尾空白或冲突标记。

终检包括本检查、全部11份本轮文件及7份当前Markdown，检查本地链接存在、表格列数、空白/冲突、JSON/JSONL、入口hash、60保护/27归档/3来源和未授权task字段；最终计数见本节末尾的直接终检记录。所有检查仅针对文件及转写一致性，不称数学审阅。

.trellis受gitignore忽略，空git diff不覆盖这些文件，未以其作为新稿证据；没有改.gitignore或git add。实际证据为直接读取、JSON解析与Get-FileHash。旧接受、assurance、证明绑定、运行和会话指针不变。

直接终检raw evidence：60/60保护hash及bytes相同、27/27归档原文相同、3/3来源项相同；R12清单SHA256仍CC6A880EF341B9586E283DE3A302AB01C70C9009F59EFA8C31B4380A055D3BB2。task/manifest JSON与两份各26条JSONL有效，52/52文件引用存在、原24项引用各保留。7份当前Markdown的94/94本地链接存在，无缺失检查链接；41行表格列数一致；11份本轮文件无行尾空白或冲突标记。正文0—10节齐全、无待填占位，10组显示公式定界成对，给定数字表逐项匹配。未授权task字段差异0，全部8入口最终预期hash一致；implement原历史保留true。current R12/previous R11、in_progress、completedAt=null及原acceptance_status保持。文件/转写检查失败项0，无文档阻断；该结论不构成数学审阅或正式接受。

[当前阶段](../STAGE_SUMMARY.md) · [PRD](../prd.md) · [研究入口](README.md) · [旧R11检查](RESET_R11_DOCUMENT_CHECK.md)
