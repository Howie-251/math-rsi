# RESET-R7 来源与文档完整性检查

日期：2026-10-21。文档子代理只检查来源、文件管理、转写口径与文档一致性，不补证明、不做数学推导、独立数学验证或审阅。全部新增数学来自主会话Astra并保持unreviewed/unaccepted；主会话来源核验、手证及自检不构成独立审阅，不升级接受状态。

## 1. 来源与保护范围

起始当前字节快照为[RESET_R7_SOURCE_MANIFEST_20261021.json](RESET_R7_SOURCE_MANIFEST_20261021.json)，其SHA256为`2F5BB3D96EE065E3B01CDE50829CB46F50C543685D0AEC75AD562E60634A9A53`。该文件保存41项保护材料的路径、起始字节数和SHA256：R1—R6数学6份，R5/R6文档检查2份，INITIAL_BASELINE1份，archive全部29项，三份旧证明/接受依赖。旧哈希未覆盖当前字节；当前8入口另有起始快照，按授权更新后不再要求其等于起始哈希。

| 来源 | 源路径 | 字节数 | SHA256 | 保存方式 |
|---|---|---:|---|---|
| 用户计划Markdown | C:/Users/astro/Downloads/DOWNSET_INTEGRATED_RESEARCH_PLAN.md | 45715 | 27CE02EB8797CCC2D89D814316B87C304FE6258FE3209C130819BAD330045C63 | [原字节副本](sources/2026-10-21/DOWNSET_INTEGRATED_RESEARCH_PLAN.md)，源与副本字节数/哈希一致 |
| 论文PDF | D:/科研/math agent/ref/erdos_szekeres_upper_bounds_v1.pdf | 199668 | F47C8CC16D4A1D8A5D483B79AA98F97C57919822DCD37DAC1B17A757E919F4C5 | 原处只记录，不复制或修改 |

论文版本、标题、日期、28页及文内DOI由主会话核对本地PDF记录；DOI网页工具未能访问，未宣称外部核实发布。主会话视觉核对PDF第5—6页，以及第24页的角点/逐色同前驱逆attainment/完整core双向递推公式，确认与提取文字一致；临时PNG不列为正式产物。文档子代理没有运行论文Lean/证书/源码、solver/checker、实验、archive下载或reviewer。附件中的SAT/有限搜索/重放建议只作为来源文字，不作执行授权。

## 2. 本轮文件与状态口径

本轮新建4个文件：来源manifest、计划原字节副本、[RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)及本检查记录；同步task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl和check.jsonl共8入口。implement保留全部旧轮历史后追加R7；R1—R6/基线/归档/三份依赖不改。

固定历史总界45/58/103/206、gap19/28/72/174；固定R5/R6草稿44/58/101/201、gap18/28/70/169；外部C7的R6传播43/56/98/195、gap17/26/67/163分别保留。固定旧子界R7草稿44/58/92/183、gap18/28/61/151；当前组合R7草稿43/56/89/177、gap17/26/58/145。相对两套对应基线，本轮迁移/传播改善0/0/9/18；相对固定R5总改善1/2/12/24分为外部1/2/3/6与本轮0/0/9/18。普通O26/30/31/32，转写按T−O核对，不把粗界写成精确值或正式接受值。

几何M_7比较41/49/79/80、gap15/19/48/48及组合40/49/79/80、gap14/19/48/48单列；25/49/30/ES81/ES319不直接进入抽象N。D_n^sig强制junction不丢弃，未迁移几何projective reduction或n8未迁移数值；未证联合source/τ收费、766严格扣减或Ω第二单位不计收益。

任务身份/createdAt/in_progress/completedAt=null及原acceptance_status须保留，current_analysis_path为R7、previous为R6。只更新授权的说明、notes与当前分析meta，不改变旧接受、assurance、证明绑定、运行或会话指针。

## 3. 主会话抽查修正的来源

以下修正均来自主会话抽查指令，文档代理只落实，不构成独立数学审阅：完成状态删除分批临时句；min{|N₀|,|N₂|}及集合基数显式化，ER例外⊂Z₁、蓝对偶⊂Z₂；p=5时恢复first5/first6；几何记M_7、抽象记N；代数下界名X_stab；极大角点由同一入对同时给二维标签，但红蓝逆前驱t_R/t_B可不同，逐色W中的pair/triple/rank只在该颜色内绑定同一个t；论文§5/restricted-25与§6—7的坐标顺序不同，未来需明确转置/decoder，不从变量编号猜颜色、不改原证书；六点负对照的T不是第一侧最小横截，仅否定返回条件本身自动低成本或私人见证自动独占，不反驳附加最小性/真实结构后的命题。

## 4. 最终直接文件检查

最终直接文件检查通过：41/41项保护文件SHA256与字节数同本轮起始记录，27/27份归档snapshot另与原MANIFEST一致；两份来源原件未变、计划副本与原件哈希/字节数一致，source manifest自身哈希未变且JSON回读通过。task.json和两个各15条JSONL解析及全部文件引用通过，当前编写文档60个本地链接有效。11份本轮编写文件直接读取无尾随空白或冲突标记，加上1份按字节核对的原始计划副本，本轮文件合计12份。计划内部原始链接不属于新写研究文档链接检查范围。

与更新前task.json逐项对比，除授权更新description、notes及当前分析meta（含本轮日期）外，其余字段保留，包括任务身份、createdAt、in_progress、completedAt=null及原acceptance_status；current为R7，previous为R6。正文0—9节顺序、PRD/阶段/正文数值表及固定/外部/本轮归因一致，主会话抽查要求的关键消歧均已转写。首次仅发现正文缺44/58/92/183汇总串（逐项推导及表格已有），已补齐后复核，无未解决文档错误。

git diff --check命令退出0、无输出；其不覆盖忽略文件的限制如下。以上检查只验证转写和文件一致性，不是独立数学审阅，不据此验收数学结果。

任务被.gitignore:23的.trellis/忽略，git diff --check即使退出0也不覆盖这些忽略文件，不作新增稿覆盖证据。实际检查以PowerShell直接读取文件、解析JSON/JSONL、检查引用和内容、直接Get-FileHash/字节数比对完成。用户计划副本不归一化，其内部源文链接不擅自修复，不当作新写研究文档的本地引用清单。不改.gitignore、不git add，不落研究程序或持久化验证脚本。
