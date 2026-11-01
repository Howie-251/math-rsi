# Property B 实务层：真实阅读范围与本地使用记录

2026-11-01。本次负责范围为`mathrsi-propertyb/references/practice/`、`examples/`以及新增`propertyb-certificate/SKILL.md`；不改主插件、数学reference、source-map或核心docs。源`aris4math`只读，archive由Root复制，本次所有数学程序在临时副本运行。未恢复m(5)≥35 Lean/≥36研究，未运行新Lean、付费模型或全图搜索，未碰ECC项目。

## 交付与设计依据

新增五份实务文档：索引、15组具体失败地图、计算与效率、Lean实务、检查器能力地图。新增五份完整案例：M65六元全链、十点signed真反例→实际共度受限门、21点component无增量停止证明、全部k≥12一般增长Lean、十二元M4663自适应覆盖。重写原空泛`local-branch.md`为实际案例导航。新增证书技能包含从原域/真实trace到算术、独核、审阅修正和原染色的实质操作，非仅路由。

所有新证据链接指向本仓`plugins/propertyb/knowledge/archive/`，没有要求作者Desktop目录。命令先建立工作副本，防旧脚本`write_text`覆盖archive。一般Lean案例保留固定环境及指定模块命令，但本次不执行。程序依赖JSON已告知Root，所选m6与k12复放现已实际成功。

## Inventory 与主题检索，不能误称穷读

执行`rg --files research-wiki context formal`得到12582条路径；另对四个目录按真实扩展名盘点，原始filesystem统计（包括formal下既有依赖）为：

|树|md|py|cpp|lean|所选四后缀合计|
|---|---:|---:|---:|---:|---:|
|research-wiki|199|0|0|0|199|
|proofs|175|0|0|0|175|
|context|1375|1353|56|235|3019|
|formal（含现有.lake依赖）|33|15|0|12146|12194|

这些是定位尺度，不是读取量。使用rg针对`截断/Nat.sub/fillEmpty_actual/actual caller/actual-input/自然数/kernel/Matched/lookup/rank/Gram/component/signed/反例/失败/定向/舍入/整数`在四树的md/py/cpp/lean检索，5400份文件命中；未逐一全文阅读这些命中，未读全部Mathlib或全部历史分支。大输出发生工具截断时另按行/小文件读取关键部分；下表明确材料层次，不把一次cat触及文件写成对全卷质量验收。

## 实质阅读范围

### 研究wiki与暂停总图

- `PROPERTY_B_FAILURE_ATLAS.md`：全部编号1…21分段核读，另追溯C4、signed门、A1换源、component、冻结八锁菜单原报告。新失败地图重组为15个有输入/数值/诊断/重试条件的主题，不机械复制条目数量。
- `PROPERTY_B_RESEARCH_LESSONS.md`：方法主体（结构预算、活跃项、避锁dual、共同实际坏对、完整分类、actual caller、Lean性能）逐段阅读；审阅历史尾部按当前实务问题使用，没有复核全部review原JSON。
- `PROPERTY_B_NEXT_BOUND_PLAYBOOK.md`：完整阅读T33→T34参数差分、21内部入口、迁移接口、暂停剩余与运行原则；没有按其早期“尚未形式化”覆盖后继成功日志。
- `PROPERTY_B_CONDITIONAL_TOOLKIT_36.md`：正文分段阅读六星W25、三划分共同计数、19-hit/相容门、整数W−t、紧二蓝面、M17及r9/r8/r7/r6/r11/r13后继。它包含自己更早的状态，本次文档以最新REMAINING_AUDIT/PAUSE为准。原始局部数值表与每份外模JSON未全读。
- m6≥66、m6≥67诊断及最终、m7≥131、m8/m9增一、k12≥4664等七篇wiki主体阅读，区分历史诊断与已完成后继，保留跨模型/独核/Lean各范围。
- `context/propertyb35-paper/REMAINING_AUDIT.md`与`PAUSE_HANDOFF_20261021.md`读取，21/22原始剩余审计回读。36保留八类主要缺口，25r5完整候选不等于全25闭合，r3/4新九锁选择不等于染色门。

### 追到真实输入、反例与程序的来源

|材料|实际阅读/核对内容|用于本次哪项决策|
|---|---|---|
|`context/propertyb33/round01/large-math/candidate-audit/C4_SELECTION.md`|完整指定点C4推导、两条件不可合并、K4,7颜色反模型、真实H未实现边界|失败不等于原题反例，明确重试需新真实条件|
|`context/propertyb35-paper/.../two_triple_small_gate/REPORT.md`与`CHECK_COUNTEREXAMPLE.py`|全部正负集、1024红集程序、实际f七度超额5迫二残集≤3|真反例转受限门完整案例；受限门仅按原报告结论链接，未重新完整证明它|
|`context/propertyb35-paper/round01/middle/a1_global_potential_20261020/REPORT.md`|同一批16原边、10/10源、G2/G3/L1/L4精确差分、平坦换源|不能省略新增private或把源存在视作可修|
|`.../a1_rank_component_wedge_budget_20261020/REPORT.md`、`PILOT.cpp`、`VERIFY.py`|完整scalar域、threshold递归、e≥34恒等证明、literal graph、C++stdout与Python输入定位|确切可执行停算案例；不再猜C++输出路径|
|`context/propertyb35-paper/round01/root/whole_class_followup_20261020/REMAINING_AUDIT_21_22.md`|21低e99/余8/高e2668，22δ6的12骨架19向量、22δ7已闭q3以后缺后链|原始对象层的瓶颈，非表行进度|
|`context/propertyb-m6-66-20261029/PROOF_M6_GE66.md`及`independent/REPORT.md`|完整原题归约、32/min12特殊支、三四锁选点/迹、379域、原染色装配|完整成功案例|
|同目录`independent/check.py`|注入概率、共同删除/全坐标、读四JSON/写RESULTS、域循环、位置/度数断言|实测复放与检查器能力|
|`context/propertyb-m6-67-diagnosis-20261029/DERIVATION_PACKAGE.md`与`pilot/REPORT.md`|整数Q/Z门、42…44替换选点、选三锁后112余50的范围|结构选点成功不等于概率闭合；诊断后已被完整m6≥67替代|
|`context/propertyb-m7-131-20261029/independent/REPORT.md`及check.py读写入口|完整424型/2115296向量、tight分数、37…73与低度选点|能力与历史成本；本轮未重跑七元|
|m8≥267/m9≥543的`independent/REVIEW.md`与m8独核关键函数|完整新域、嵌套最低度池、299组件quota、73父型/完整决策树/3450叶|父型strict停止，避免全域统一扩锁；未逐字读其全部作者代码|
|k12≥4664的`independent/COVERAGE_REVIEW.md`、check.py、conditional.py、tail.py、REPRODUCIBILITY.json|全域/trace与20例Fraction、同一H条件三锁、固定693/694、S=2^52方向、读写输入|自适应覆盖案例；未把全域检查写成全表第二概率|

表内省略号只是长目录显示，正文所有实际链接使用完整路径；没有假称这张表覆盖全部source。

### Lean与实际工程

- `context/ARIS_LEAN_WORKFLOW.md`读取，重点原题命题对齐、实际输入、指定Main与审阅范围；不重做已完成ARIS技能贡献。
- `context/propertyb-unified-lessons-20261014/LEAN_AND_EFFICIENCY_INVENTORY.md`完整主体读取，含真实caller与通用接口、naturalsub、25缓存未完成及错误时间估计。
- `context/propertyb34/round01/middle-lean/PERFORMANCE_NOTES.md`完整读取，保留exit137、>15分钟/8GB、15552数组exit134、673查询/674域/70代表、87.75秒、925/3618证书与1–2秒wrapper。
- T34 `FINAL_30_MINUTES_REPORT.md`、`SEVEN_R234_INTERFACE_GAPS.md`读取，核r2/r3/r4欠完整分类和联合论证，未称只欠API。
- `formal/Aris4Math/ThirtyFour/PromotionReconstruction.lean`完整源码核读，读`fillEmpty_actual/extend_actual`实际前提与Nat减法证明来源。
- `formal/README.md`完整读取实际固定工具链/默认Main/RS/growth命令；`ReviewAuditGeneralGrowth12.lean`完整源码核读原积分最大元与裸Bool结论、传递公理列表；`Growth/Twelve.lean`前半关键种子/参数/最大元实现和后继报告阅读，不冒称本次重新逐行验了全旧依赖证明体。
- `context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md`与lean/REPORT、VERIFICATION读取，保留全部k≥12/Δ≥2、增量缓存成本、D/E未Lean。
- 未运行Lean/Mathlib构建，未重新核验旧35或36数学；所有历史秒数按原日志引用，区别本轮实测。

## 实际本地使用：四组既有程序

2026-11-01，从本仓archive复制到临时目录

`/var/folders/qz/3h_f66zn67zbty04w0mjyysm0000gn/T/mathrsi-propertyb-practice-57e_dkra/`

每组保存`PRACTICE_REPLAY.stdout`、`.stderr`与脚本本次实际JSON；总记录`SUMMARY.json`。该目录是本轮开发验证证据，不是技能使用时要求作者机器路径；五案例中的命令用mktemp可在其它位置重建。Root可按交付要求收录本次原始输出，不将临时路径伪装为长期portable artifact。

|本次真实运行|退出/实际结果|本次墙钟/CPU|
|---|---|---|
|m6独核check.py|exit0，379型、621579完整整数向量，所有strict，最大682298/682341|墙1.4492秒；程序输出保存在副本RESULTS|
|signed CHECK_COUNTEREXAMPLE.py|exit0，PASS_COUNTEREXAMPLE、1024红子集、243 hitting、修复0|墙0.0230秒，脚本CPU0.000258秒|
|component重新clang++、pilot stdout写副本PILOT.json，再VERIFY.py|两次exit0；33,867小图、U35_76=13074、literal连通无孤立|Python墙0.1980秒、CPU0.164898秒；C++实际输出另保留PILOT.json|
|k12独核check.py|exit0，全域664355/692v，20次Fraction，PASS_MODULO_IMPORTS，complete_second_probability_replay=false|墙3.0212秒、脚本CPU2.896259秒|

这些是本轮真实旧小程序复放，不是新下界/新独立数学证明/跨模型认证。程序输入来自archive但所有改写仅在临时工作副本，源与archive均未改。m6/m7依赖各自JSON必须随目录，k12独核仅需COMPLETE、CONDITIONAL、TAIL三JSON，component VERIFY读PILOT.json；signed自造全部输入。

## 技能与链接验证

按本机`skill-creator/SKILL.md`编写新增技能。宿主Python与既有goal-pulse venv均缺PyYAML，首次quick_validate未运行成功；随后仅在临时venv安装PyYAML并执行上游quick_validate，真实输出`Skill is valid!`/exit0，未给本仓新增依赖或平台代码。临时环境`mathrsi-skill-validate-o8z85V/venv`只供本次检查。

新Markdown相对链接按本次文件范围检查：12份Markdown、88个本地链接目标，缺失0。全仓`tools/check_links.py`不支持--help，试探该选项实际触发全扫描，archive历史正文中大量HTML/JSON/旧绝对导航未作为全部资产复制，因而报告1467缺目标，另含公式的正则误识别；这不是本次新实践文档的检查通过证据，也不通过改写历史正文伪造全仓零断链。

## 未读/未做与合理边界

未全文阅读所有5400命中、所有formal依赖、所有研究树或所有审阅JSON；未完整新审m6≥67最后每分支作者程序、m8/m9每行作者实现、k12全664355概率；未读每篇文献PDF来重认证所有进口。文中相关状态依原规范、独核与最新审计记录，明确不升级。

未新建通用验证器/调度平台，只有复用既有checker与文档链接检查；未写数学新结论、未运行大构建、未恢复Goal、未清理旧资产、未推Git。成熟文档与实测结果已逐项通知Root，不等整批才交接。
