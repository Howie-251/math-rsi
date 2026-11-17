# RESET-R9 文档转写与文件完整性检查

日期：2026-10-22。本记录只检查主会话给定材料的转写、文件及入口一致性，不是数学推导、独立证明验证或独立审阅。全部新增数学unreviewed/unaccepted；不启动reviewer、子代理、研究代码、SAT、枚举、求解或实验，不改旧接受、assurance、证明绑定、运行或会话指针。

## 1. 起始保护与来源

[R9_SOURCE_MANIFEST_20261022.json](RESET_R9_SOURCE_MANIFEST_20261022.json)保存51项当前字节及8入口起始hash。清单自身SHA256为18264FDFBA634C266AF125200EE953FA67AD703482159B93A597B5C8F676C977，保持不变。保护范围是R8清单48项，加R8正文、R8文档检查、R8清单；包括R1—R8、INITIAL_BASELINE、所有归档、原来源/计划副本及当前旧依赖。逐项hash与bytes复核；不拿旧轮hash恢复外部当前版本。

27份归档snapshot另与原MANIFEST逐项核对。计划原件C:/Users/astro/Downloads/DOWNSET_INTEGRATED_RESEARCH_PLAN.md和既有副本均45715字节、SHA256为27CE02EB8797CCC2D89D814316B87C304FE6258FE3209C130819BAD330045C63；PDF原件D:/科研/math agent/ref/erdos_szekeres_upper_bounds_v1.pdf为199668字节、SHA256为F47C8CC16D4A1D8A5D483B79AA98F97C57919822DCD37DAC1B17A757E919F4C5。来源原件及计划副本均未改写，PDF未复制；计划内原始链接不擅自修复。

外部cardinality-layer-theorem当前18010字节、SHA256为CFCAB4764AC1F40BF37FA7B8B761EE1CDBC3D004F3E64FB8074F001F7EE699D2；C9/C10既有记录限定独立N756≤26，rows1—7/9/10 accepted、C8/A[8,8] pending，不推25。same-family/provisional、精确model/backend/actual effort未知不可核实保持；仅沿用元数据，不检查证明体、重放或升级。

## 2. 本轮文件与转写修订

新增R9清单、[R9正文](RESET_R9_RESOURCE_STABILITY_AND_TRANSVERSAL_COST.md)、本检查记录共3项，更新task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl、check.jsonl共8入口，总计11份本轮文件。同步前8入口hash均与起始快照一致，无并发差异；implement保留R1—R8全部执行历史并追加R9，JSONL原18项引用保留，各新增R9正文/清单后为20条。

以下均是主会话补充或自检后指定的转写，不是文档代理的数学审阅：D⊂非源核心、显式(L1+1)h一次计数；易读联合式M≤B_*+min{C_*,ρB_*+|G|}+κ_end；P_-顶点一次区间分层、G单列一次；非负系数及外层max的条件缺额公式；766粗源300弱于平凡26，不能包装数值改善；新增4.3的不对称N(n,5,p+1)、n≥p+2构造族Ω≥p−2，756特定族Ω≥3不改独立26、不搬到766等阈值。原4.2正确p4对称例保留。

正文完整0—9节，无暂存占位。H区间引理n≥6不需右根；端点匹配Base及κ≤n−2须右根末点分支，D7自动、一般n8不自动；一般t_*接口不预设n8成本。同一λ、同一分拆和固定最小横截的不同预算项才相加，不叠加G_anch/另一个T核心/G_src。端点横截不等于A/B交换或Ω增量；条件51/47未声称类非空或近饱和；尚未排除分支不冒充真实反例。

## 3. 数值与任务状态

当前R8/R9均41/52/83/165，普通26/30/31/32，gap15/22/52/133；逐项T−O和R9变化0与正文、PRD、阶段表一致。直接全局、递推传播、旧工具额外迁移、外部新增四类收益均0。就本轮新结构的独立贡献而言，本轮尚未进一步缩小全局 gap。外部26仅沿用，不重复计入R8相对R7的2/4/6/12；历史45/58/103/206、固定R5/R6 44/58/101/201、C7入R6 43/56/98/195、R7 43/56/89/177不回写。几何25/49及射影最终界未迁入抽象N；无新几何数值，粗界不作精确极值或正式接受值。

task current_analysis_path指向R9，previous指R8，日期2026-10-22；id、createdAt、in_progress、completedAt=null、原acceptance_status及其他未授权字段保持。全部新增unreviewed/unaccepted，长期任务未完成。

## 4. 直接文件核验口径

PowerShell一次性直接读取11份本轮文件，检查JSON/JSONL解析、原引用保留及路径存在、7份当前编写Markdown的本地链接、空白、冲突标记、占位、章节、入口/状态和给定数值表。51保护项与27归档另逐项Get-FileHash及bytes核对，来源2原件和计划副本另核对；没有持久化检查脚本或研究程序。

git diff --check退出0；全仓库命令对其他既有改动文件输出LF将转CRLF的提示，未将这些文件视为本轮改动或处理。仓库.gitignore:23忽略.trellis/，所以git diff不覆盖本轮新增/修改文件。实际证据来自上述直接文件读取与hash，不改.gitignore、不git add。首次raw evidence输出因PowerShell将Git stderr保留为ErrorRecord，JSON深度序列化出现大量技术信息；这不影响直接核验结果，最终输出先转成字符串消除此记录问题。

最终直接文件结果：51/51保护hash与bytes相同；27/27归档记录相同；2原件和1计划副本共3项来源检查相同；R9清单自身hash未变。task JSON和两份20条JSONL均解析，40/40引用存在；7份当前编写Markdown共77个本地链接存在；11份本轮文件无行尾空白和冲突标记，正文0—9章节齐全、无暂存占位。正文/PRD/阶段的4行数值表一致。未授权task字段差异0；当前R9、previous R8，in_progress、completedAt=null、原acceptance_status保持。直接检查失败项0，未发现阻断。

[当前阶段](../STAGE_SUMMARY.md) · [PRD](../prd.md) · [研究入口](README.md)
