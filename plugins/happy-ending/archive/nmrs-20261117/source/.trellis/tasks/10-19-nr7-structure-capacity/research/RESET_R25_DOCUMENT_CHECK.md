# RESET-R25 文档与转写一致性检查

日期：2026-10-24。全部新增 **unreviewed/unaccepted**；current R25 / previous R24。

## 检查范围、来源与接受边界

本文件只记录普通PowerShell文档读写、bytes/SHA256、JSON/JSONL解析、原字节保留、字段值/键序、文件引用、本地链接和确定文本锚点检查。不判断数学真伪，不自行补证明，不构成独立数学review，不升级旧acceptance、assurance或证明绑定。

数学由主会话直接研究与三名授权数学协作者确定，分三包及末后定点增强传入；Sol/high仅忠实转写。主会话已只读检查§0—2、§6—附录等指定内容并给出精度修正；这些主会话自检、协作者核对和本文档检查均不构成独立审阅或正式接受。

本轮直接采用用户工作基线b=N756=25；全部C_r用户报告UNSAT、证书验证进行中、旧正式checked/accepted记录三个来源层面分别保留。没有读取新证书、重放证明或干预现有运行。C8/A[8,8]pending、旧same-family/provisional及未核实backend/effort边界不变。

当前40/50/80/81及gap粗14/20/49/49沿用，四类新增全局界改善均0。新增引用Szekeres–Peters的已发表9点weak5计算基例单列：主会话已读原文§2/Theorem1，本轮没有复算或核验其程序，不称无外部基例自含证明，不改变b或全局基线。独立50未排，无新真实31/50/80；40..45只是在反设X80内必有的诱导母体归约，不是已找到对应构造。旧757十一点例复用，不认新构造。

只写R25正文、本检查、此前已固定的manifest及八入口。没有研究代码、SAT、枚举、求解、计算实验、证明重放、项目/临时研究脚本或独立review；不提交、不归档，不修改旧轮次/INITIAL_BASELINE/归档/旧接受/assurance/绑定/运行/会话指针。任务继续in_progress、completedAt=null。

## 不可变快照与100条保护路径

[固定源清单](RESET_R25_SOURCE_MANIFEST_20261024.json)在R25正文与入口前建立并固定后未改。[R25正文](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md)是本轮数学转写文件。

保护范围实际核对为R24原97条路径，加R24正文、R24检查、R24 manifest，共100个不同路径；99份现存文件按本轮起始当前bytes/SHA256保护，1个旧外部原件起始missing，不能称100份现存文件。与R24原97项当前hash/状态差异0；没有按旧hash恢复文件。

缺失路径C:/Users/astro/Downloads/DOWNSET_INTEGRATED_RESEARCH_PLAN.md保持exists=false、status=missing_at_round_start、current_hash_available=false，只保留historical_bytes/historical_sha256及历史来源，不冒称当前bytes/sha256，不恢复外部原件。仓库已有来源副本在保护范围内。

manifest保存八入口完整原bytes/base64/hash及完整original_task_value。创建后实际解码核对原bytes长度与SHA256，task原值与原bytes解析值一致；本次复查base64/hash亦全部一致。

| 文件 | 字节 | SHA256 |
| --- | ---: | --- |
| R25固定manifest | 367046 | 37DE7D5A0F45B646ABE84EA8DBEED1FC2CF5C955E5527F6B45B36119464E77DB |
| R25正文 | 39559 | 58DBDC41120DB3E587A0A7237E455E906775ACD88C3A7C6BA2D43ADFA414EFA9 |

本检查自身最终bytes/hash由完成回报提供，避免自引用hash。

正文每次创建、追加、指定修订、八入口每次写入、本检查创建前，均重读99份现存保护文件hash、1项missing状态、固定manifest、正文已存在后的预期hash及八入口当前预期hash。入口未写时用原hash，写后更新预期hash；没有覆盖或回退并发工作。

中断恢复后先实时复核：正文25236bytes、341行、SHA256 B16D216FCB3B2ABCB34A5EF36E5A8E9D55F939B527878A55E48AE31A0D748D35，check不存在、八入口仍R24原hash、100保护路径无差异，才按用户授权的一次原模型重试继续。manifest未重写。

## 八入口、原字节与task授权变更

五份Markdown仅prepend，原bytes为当前文件精确suffix；两份JSONL仅append，原bytes为当前文件精确prefix。task原bytes及全值在manifest固定；旧description/notes分别为当前字符串精确suffix。

| 入口 | 当前字节 | SHA256 |
| --- | ---: | --- |
| task.json | 27311 | DA36326FF0DFDE315B725E1771652654CEBEFFDEF95D112FCCE2A1ACA311D502 |
| prd.md | 29842 | D6DE01753AB7889A08CB140E74DDB2F471ADFD8B8F76CBB7D44D021CE814B993 |
| design.md | 27857 | 062C5C41C9F94B48CA47F63B6DA8CF6DC5E9DF9B0A4BEEEED24032E8F33C44D6 |
| implement.md | 56309 | CB2932B022A3425DF6FC50AFA46AC3EF4A1A91DC48699BB1A2AB544A40CB047A |
| STAGE_SUMMARY.md | 30143 | C95E9735DB61C3245EDD951EC59CFEA9ECCD454ACBC0E133743C71D6B895926E |
| research/README.md | 28779 | AEEFE120A16EDB4273E3385BC13BB5264850C87E0FF5A596C453ECE89E2AA7B4 |
| implement.jsonl | 23181 | FAFAD9ECFC875EF9A22203733ABF228E1E5DC9F9F38BE8A8E2A1D085605DEF88 |
| check.jsonl | 23166 | 4973676A6C2A2E602CDC41316B00D5B36D4FACF3FBE645D9983C01626A091CA5 |

task.json可解析。只前置description/notes，并更新既有五个meta字段restart_scope/current_analysis_path/previous_analysis_path/current_analysis_status/current_round_date。其他顶层及meta键集合、键序、每个值逐项对照original_task_value，差异0。status=in_progress、completedAt=null、原acceptance_status保持；current R25 / previous R24，旧正式接受记录保持。

两份JSONL原各50条有效JSON，当前各52条；原完整bytes精确prefix保持，各只按顺序追加R25正文与manifest两个引用，没有追加本检查或其他第三条。各52个file引用全部存在；原行未改、未重排。

## 正文结构、指定精度与文本检查

正文535行，主节§0—9共10节，另附录A。它完整转写已给定证明，不把长证明压成结果摘要；历史依赖只按实际使用范围引用，不重写旧正文。

§0—1记录模型/来源分层、全局数值及A—E的兑现链、覆盖/未强迫类、第一断点、尚未用信息、50存在时价值和下一投入。§2完整记录任意骨架/块方向的四包、固定实际双端精确路径式、必要充分帽/weak、边界cap9处理、经典重构/叶预算、已发表小基例、精确B+5实际达到、singleton边界；不外推一般进入或n6。

§3完整实际换点重算全部身份，准确引用R7§3.1的三链前提及R5canonical增广适用范围。全q排共同嵌入m/m'11..15，不排独立50。泛b式已按主会话纠正为ambient蓝端≥2b−10、j/t≥b−10。§4—5保留全供应身份及位于P×Q的实际全替代矩形，主式m+m'+q−w≥15、U/V非同、人口恒等式及不重复计损失全部明示。

§6记录W_B/W_E实际诱导归约，内部R5精确端集J→M_-、M_+→J_T与满25核L/L'、E/E'。W_E删M_+得E、删J_T得E'映射准确，内部蓝5身份不能继承。每z的特定内部红前供首点是J的非空子集，与该z全部H蓝后供第二点子集全交叉；对偶同理。只得位于J×Q/P×J_T的供应矩形，未称整个笛卡儿积都有边，未称所有原供端都被迫进入J/J_T。

§7扩大至任意q的j15。主会话指定的B4 joining已写明：入B4=(x_1,x_2,h,s)，B时将u后接得Y内B5，R时才把h前接出R6；不重复加入已经在B4中的h。canonical15/16分支、某f存在但不唯一选择、余量j−15与真实节省不双计均保留。

§8对全部ambient蓝前/后供只直接断言s∈S、t∈T，选择H'/H内部供才进一步为P/Q；反色桥证明仅需S/T。四支端点替换及代表性四包完整记录，准确停止于分别保证的内部供尚未在同一对外端闭合。旧R5真实757十一点例（因此亦在767）按主会话纠正模型标签并保留全染色/四包/路径/weak检查，不写766、不认新构造。附录只断言可达闭集全局限制，未保留未展开的奇闭游走转换。

§9明确四类新增全局界改善0、独立50和X80剩余分支、模块缺一般进入、全部共享P×Q供与两批正需求未联合兑现。52个指定确定文本锚点全部存在；锚点只是转写文本核对，不是数学真伪验证。

## 本地链接与创建前实际检查

创建本检查前已实际执行：100保护路径/固定manifest/正文/八入口hash及missing状态差异0；五MD旧bytes精确suffix、两JSONL旧bytes精确prefix差异0；task非授权值/键序、旧description/notes字符串suffix差异0；JSONL各52条/全部引用/新增顺序异常0；52确定文本锚点缺失0。

正文和五份Markdown入口共223个实际本地Markdown文件链接，其中6处指向待创建本检查，其余缺失0。扫描忽略代码中的公式，不执行被引用的依赖、证明或研究程序。本文链接的正文/manifest都已存在；创建后将再次扫描全部本地链接并实际复查保护/入口/状态，结果另附于下。

**就本轮新结构的独立贡献而言，本轮尚未进一步缩小全局 gap。**

全部新增unreviewed/unaccepted；任务继续in_progress、completedAt=null，长期目标未完成。本文件不赋予数学独立审阅或正式接受。


创建后终检已实际执行：重读100保护路径、固定manifest、正文、八入口及本检查；99现存保护文件hash/长度与1项missing状态差异0，manifest/正文/八入口/本检查预期hash差异0。五MD旧bytes精确suffix、两JSONL旧bytes精确prefix保持；task非授权值/键序、旧description/notes精确suffix差异0。JSONL各52条、只新增正文和manifest两条且引用全部存在。52指定文本锚点缺失0；含本检查的全部本地Markdown文件链接225处，pending0、缺失0。未发现R26或后续文件。current R25 / previous R24，status=in_progress、completedAt=null、旧acceptance_status保持。

本段记录已执行的普通文档/文件检查，不新增数学判断或接受。追加本段后再次复核保护/入口/状态/链接及本检查hash；最终bytes/hash由完成回报提供。
