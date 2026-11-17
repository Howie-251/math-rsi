# RESET-R8 文档与文件保存检查

日期：2026-10-22。本记录只检查来源、转写与文档一致性，不进行数学研究、证明补写、独立验证或审阅。全部数学由主会话Astra逐条提供，保持unreviewed/unaccepted；主会话自检、数学抽查及本文档检查均不构成独立审阅，不升级接受状态，不委派。

## 1. 起始清单与保护范围

沿用[RESET_R8_SOURCE_MANIFEST_20261022.json](RESET_R8_SOURCE_MANIFEST_20261022.json)的48项起始当前字节记录，不覆盖或重建。清单SHA256为`AC1E0F08FCFB025243D645151091D29C24E8AB8CB1103A144ECA4EC23540D25B`。48项包括R1—R7数学/旧文档检查/来源manifest与副本、INITIAL_BASELINE、归档、三份旧依赖及C9/C10接受记录、两来源原件，按清单逐项核对；不能拿R7旧哈希恢复外部当前更新。

本轮起始前cardinality-layer-theorem已由其他任务更新，当前18010字节、SHA256为CFCAB4764AC1F40BF37FA7B8B761EE1CDBC3D004F3E64FB8074F001F7EE699D2；相对R7旧保护快照仅此文件外部变化，当前字节受保护。C9/C10接受元数据限定独立N756≤26，accepted rows1—7/9/10、pending8/A[8,8]，不推25；same-family/provisional及精确model/backend/actual effort未知不可核实边界保留，不重验、重放或升级。

计划原件C:/Users/astro/Downloads/DOWNSET_INTEGRATED_RESEARCH_PLAN.md及既有副本均45715字节、SHA256为27CE02EB8797CCC2D89D814316B87C304FE6258FE3209C130819BAD330045C63。PDF原件D:/科研/math agent/ref/erdos_szekeres_upper_bounds_v1.pdf为199668字节、SHA256为F47C8CC16D4A1D8A5D483B79AA98F97C57919822DCD37DAC1B17A757E919F4C5。R8未复制或归一化来源，原件及原副本保持原字节，计划内部原始链接不擅自修复。

## 2. 本轮文件、入口与数字口径

本轮新建3文件：R8起始manifest、[RESET_R8_UNIFORM_DEFICIT_AND_JOINT_CAPACITY.md](RESET_R8_UNIFORM_DEFICIT_AND_JOINT_CAPACITY.md)、本检查记录；同步task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl、check.jsonl共8入口，合计11份本轮文件。授权同步前8入口与R8起始快照一致；implement保留全部历史并追加R8，旧稿不回写。

R7组合43/56/89/177、gap17/26/58/145保持历史原样。最新外部b26结合旧R5/R7草稿结构给41/52/83/165、gap15/22/52/133，普通O26/30/31/32；下降2/4/6/12全归外部28→26和旧结构传播，本轮新结构独立统一扣减0/0/0/0。就本轮新结构的独立贡献而言，本轮尚未进一步缩小全局 gap。若固定外部28，仍为R7组合；没有新766全局严格扣减或全局Ω第二单位。只核对转写的T−O，不把粗界写成精确极值或正式接受值。

单内部gate覆盖全部源的p5/n7子类可选h20/L2的5、B26给M≤51，统一766草稿表仍52；条件函数G_src/G_anch不因部分为正就作普遍正，也不能机械相加。几何40/49/79/80与论文41/49/79/80单列，本轮无新几何数值，未将PDF25/49/最终射影界或计算结果导入抽象N。

## 3. 主会话自检修正的转写记录

以下均由主会话提供，文档代理只同步，不作为独立数学审阅：

- 补齐完整signotope、四元包、weak/path/U(v)与容量标量的自足定义；SR/SB/ER/EB、Src(K)、N₀/N₂及J定义明确，几何h19/J16不移植。
- L2可与L1取min，但不保证有效粗界严格下降；蓝拼接长度显式写成p−1+1=p、p−2+2=p，仅w∈K时调用K内无蓝p。
- 精确入对逆attainment可服务多源，不要求红蓝前驱相同，不宣称整二维角点或孔证书；源共享真族的n≥p+3范围不作766反例。
- 单锚点星的m−j成本正确，但主会话发现并证明j≤1；m6必j1且收益0，j≥2已排除，不能再以H丰富性迫m6新增J。此为排除自然星多单位节省机制的新增推导，不给R7只用j1的证明制造缺口。
- 终端转色用(红,蓝,?,红)四点论证，第三项未预先给定；共享间隙只是未排除，未在n=p+2据此构造实例。
- 既有D(v)单射允许选择h=binom(2p−4,p−2)，有更小有效界时取min，不写任意h必小于另一粗界；51只列明确子类，不进入全局表。
- 原规范覆盖按p≥5/m≥2与p4/m1分开：前者交集M−2、766为7，后者交集S大小3；保留右块两点蓝路径真空边界。p≥5选定覆盖非规范，p4同类返回阻碍可出现在规范覆盖但已有3重叠，未研究/证明交集≤1等更窄候选；两者均不反驳全局Δ_aug/Ω正性或第二单位。

## 4. 最终直接文件核验

最终检查全部通过：48/48保护文件SHA256与字节数等于R8起始清单，无外部后续变化、未恢复任何旧版本；27/27归档snapshot原件另与原MANIFEST一致。两来源原件、原计划副本及R8manifest自身哈希一致，source manifest JSON解析通过。

直接读取11份本轮文件，无尾随空白或冲突标记。task.json与两个各18条JSONL解析通过，全部文件引用存在；7份当前编写Markdown的59个本地链接有效，来源副本内部原始链接不纳入新写文档链接检查。正文1—9节次序、PRD/阶段/正文数值表、全局与条件51的区分、独立贡献与外部传播口径、关键主会话量词修正及无待填标记已核对，无未解决文档错误。

与R8起始task.json逐项比较，除获授权description、notes及当前分析meta（含日期）外，其余字段保留，包括id、createdAt、in_progress、completedAt=null及原acceptance_status；current为R8、previous为R7、date2026-10-22。任务长期保持in_progress，不宣告整体完成。

任务被.gitignore的.trellis/忽略，git diff --check退出0且无输出也不覆盖这些忽略文件，不作新增稿覆盖证据；实际结果来自PowerShell直接读取/解析与Get-FileHash/字节数检查。不改.gitignore、不git add，不落持久化验证程序，不研究代码/SAT/有限枚举/求解/实验/独立审阅，不运行PDF代码，不委派，不改旧接受、assurance、证明绑定、运行或会话指针。
