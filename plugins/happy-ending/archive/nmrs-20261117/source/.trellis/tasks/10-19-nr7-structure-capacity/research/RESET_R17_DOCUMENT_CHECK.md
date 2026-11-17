# RESET-R17 文档与转写一致性检查

日期：2026-10-23。全部新增unreviewed/unaccepted。

## 检查范围

本文件只记录文件、字节、JSON/JSONL、引用、任务元数据及主会话提供数学文本的转写一致性检查。正文§0—8（含§4.5）由主会话及授权数学协作者确定，主会话报告已通读并完成自身数学核验；这不是独立审阅。Sol/high文档代理仅转写、落实指定文字修正及公式排版，不补证、不判断数学真伪、不启动review。没有运行研究代码、SAT、枚举、计算实验、证明重放或独立review。

## 当前字节基线与保护

R17源清单保持初始字节不变。其76项protected_files已全部重新读取当前字节与SHA256比较，字节数/hash差异均0；完整路径和各项hash以本轮基线清单为准，不在此重复长表。保护集为R16原73项及R16正文、检查、manifest，包含R1—R16、INITIAL_BASELINE、归档、来源、旧接受和只读依赖。不按旧hash恢复，不改旧assurance、证明绑定、运行或会话指针，不提交或归档。

| 文件 | 字节 | SHA256 |
| --- | ---: | --- |
| R17正文 | 28315 | 98E2FA67DD145327ECBDA48E3FF96FAB0478D733A5E369E29A23D70287A8AB52 |
| R17源清单 | 229132 | F72E26EED1FF0303FDAD56BA6EDE3552EF937030EECAD961E9DE29929659299F |

## 八入口写入与历史字节

共8次入口写入；每次写前均核对全部8入口、main和manifest的预期SHA256，未写入口对照基线，已写入口对照本轮刚记录的hash。无并发差异。写入本检查前再次核对上述全部预期hash，通过。

| 入口 | 字节 | SHA256 | 原始历史字节保留 |
| --- | ---: | --- | --- |
| task.json | 11859 | DC70E3BE99313AB5CB44C59A8C5CCDEA926C68A431779DCD0A19B632323B2525 | original bytes stored in baseline：通过 |
| prd.md | 16690 | 8FE05ED364962732D7B1D08E04E8B88CC4DCC120A24F7F081AF328B87BAA7839 | exact suffix：通过 |
| design.md | 14900 | 503129CA16369903D95BE9FAEBA4D096E9F9E949B72BBF04AD9B9FF35D7C3EB0 | exact suffix：通过 |
| implement.md | 41941 | 6830B13FE6368AEA156D112E8EC5AE90841ED91A7DD87CB05B9130F80DF946C4 | exact suffix：通过 |
| STAGE_SUMMARY.md | 16416 | 7D82C557908AEB374800A7A13E55E8C16574F1B3B2C4977E62699DB3379BC665 | exact suffix：通过 |
| research/README.md | 15479 | 2E570E66EEC39413B580BC6F749A5ABA981A60E0FE0E723AB6DFCD82D6D42686 | exact suffix：通过 |
| implement.jsonl | 13777 | D31B3ECF2240477D5D0C389F880D4F9AA637B6B9DD5BDCF6B90AFCB647B977FB | exact prefix：通过 |
| check.jsonl | 13762 | E34FBC2C7615C76A68C681FF4310EFDAA883987D2522B5336298CDEC11F2FA6F | exact prefix：通过 |

五个Markdown入口仅prepend各自相关简短条目，原始字节均为精确后缀；两份JSONL原始字节均为精确前缀。task.json原始字节保存在manifest的base64中；其旧notes字符串为当前notes精确后缀。需求边界、结构接口、转写执行、阶段结果、研究导航各自简记，未复制相同长摘要。

## 任务JSON与JSONL

两份JSONL各36条有效JSON，原34条旧字节保留，末尾只追加R17正文与R17manifest两条。全部36条file引用都存在，缺失0，追加顺序核对通过。

task.json可解析。只改description、notes和既有五个meta字段restart_scope/current_analysis_path/previous_analysis_path/current_analysis_status/current_round_date。其他全部顶层及meta键集合、顺序和值逐项比较不变；旧acceptance_status及assurance保持。current R17 / previous R16，status=in_progress、completedAt=null，不完成长期任务。

## 正文结构与指定内容转写

正文§0—8共9主节、18子节，包括新增§4.5；主要显示公式10组，独立LaTeX开闭标记各10。21项指定公式、参数表及范围措辞检查通过。公式检查仅保证从主会话确定文本到Markdown的忠实转写，不作独立数学验证。

共同取等两条精确账本保留，不称正缺额定理；父状态实际锚/单色纤维及同owner双向互补保留q−实际人口缺额，767/777偏移9/18保留。中央BBRR及整体分离双侧几乎完全接口限制同一W，仍未推出额外缺失。E侧真实红4供应、K26/e8及E对偶中阶fan限定、R7逐段读取文字按主会话指定修正。

全路径串联κ精确式、完整canonical母配置νlive=ν=m/κ1及p≥4、n≥2p−1范围保持；不是766近饱和例，不证明所有目标Y可归约。saving与Δ_0不可双计，条件实际|D|≤1的76651只作真实D证书的条件代入，不称新的全局或已证更广目标子类。普遍正收益未得。

全局T41/52/83/165、O26/30/31/32、gap15/22/52/133不变；直接全局、递推新增、既有工具新全局数值迁移、外部新增四类收益均0。几何历史与INITIAL_BASELINE数字保留历史范围。

就本轮新结构的独立贡献而言，本轮尚未进一步缩小全局 gap。

## 本轮文件清单

新增research/RESET_R17_GLOBAL_CO_SATURATION_AND_CAPACITY_TRADEOFFS.md、research/RESET_R17_SOURCE_MANIFEST_20261023.json、research/RESET_R17_DOCUMENT_CHECK.md；同步task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl、check.jsonl。未写其他文件，R1—R16及旧基线不改。全部新增unreviewed/unaccepted；协作、自检与文件检查均不构成独立审阅或接受升级。

本检查自身最终字节/hash由完成回报给出，避免自引用hash。
