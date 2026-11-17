# RESET-R6 文档与文件保存检查

日期：2026-10-20。本记录只检查文档管理和一致性，不进行数学研究、独立证明验证或独立审阅，不构成正式验收。全部新增数学来自主会话Astra，保持unreviewed/unaccepted；主会话自检不是独立审阅。本轮没有研究代码、SAT、实验或reviewer调用，没有落持久化验证程序。

## 范围与数值口径

当前8入口为task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl和check.jsonl；新稿为[RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md](RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md)。任务身份、createdAt、in_progress、completedAt=null及原acceptance_status保留；current_analysis_path为R6、previous_analysis_path为R5。

固定历史任务基线45/58/103/206、gap19/28/72/174；R5与R6固定基线草稿44/58/101/201、gap18/28/70/169，普通O26/30/31/32，R6新增结构改善0/0/0/0。外部既有C7=28结合R5未审阅结构另表传播43/56/98/195、gap17/26/67/163，相对固定R5下降1/2/3/6归外部子界和传播，不计R6收益、不升级接受。这些不是精确极值或精确gap，检查只核对转写口径。

C7外部更新早于本轮起始快照；cardinality-layer-theorem在首批38项快照中已是16314字节、SHA256 7AE400CE801E769BF5165F44454DE042C878E1714244127F2C948AC3E088EC29，没有将其误报成本轮修改。C7接受记录随后补为第39保护项。其receipt SHA347bcf377f53102316c091ebdf9cd415acbaa33ffbe1f52f47061531f791ec96与文件自身SHA256分开；只沿用human accepted/SAME_FAMILY_PROVISIONAL原记录，精确审阅模型/后端/实际effort未知或不可核实，不重验或升级assurance，不改C6历史。

## 检查结果

检查完成：task.json及两个各12条JSONL解析通过，全部路径引用存在；46个本地Markdown相对链接均有效；直接读取10个本轮文件确认无尾随空白或冲突标记。git diff --check命令退出0、无输出，但任务被.gitignore第23行的.trellis/忽略，git status/diff为空，该命令不覆盖这些忽略文件，不能作为新增稿覆盖证据。实际空白/冲突、JSON/JSONL及链接检查均由PowerShell直接读取文件完成，哈希和字节数由直接文件检查完成；未改.gitignore、未git add。与起始task.json逐项比对，除授权更新的description、notes及4项当前分析meta外，其余字段全部保留，包括身份、createdAt、in_progress、completedAt=null和原acceptance_status；当前/前稿路径分别为R6/R5。固定基线表、外部传播及新增结构0的文字口径已核对；首次检查发现阶段仅列逐项公式而缺43/56/98/195汇总写法，已补齐后复核。39/39项保护文件SHA256与字节数均同起始记录，27/27份归档snapshot原件另与原MANIFEST一致。本轮没有研究代码、SAT、实验、独立审阅或持久化验证程序；这些检查不是数学验收。

主会话全文检查后，文档代理按完整指令落实五项明确性修订：第1.1节补齐自足模型、路径/weak7及D/U重算口径；第5.3节显式写出红横截的Y/Z及两外点存在理由；第5节结尾将Ω≤1反例限定为M≥2并保留单点边界；第4节负对照只限定共接点t可加入A而非任意覆盖交换；第5节补齐红侧两点兼容的显式操作与删点论据。结论与数值未变，修订后重新核对39项保护材料、27份归档原件、链接、JSON/JSONL、状态与diff，检查范围和通过数量同上；不构成独立数学审阅。

随后按主会话记录修订PRD成果口径为“全局数值收益只计已证明的无条件gap降低；结构定理、条件机制及适用范围另行记录”，一般n完整定理仍记录为结构成果。最后相关文件直接检查再次通过；Git命令结果及其不覆盖忽略文件的限制按上文保留。

## 起始保护记录

以下39项使用PowerShell Get-FileHash记录起始SHA256并读取字节数：R1—R5数学稿5项、R5_DOCUMENT_CHECK、INITIAL_BASELINE、archive全部29项（27份snapshot原件与README/MANIFEST）、三份旧证明/接受依赖。按授权更新的当前阶段不在保护范围，但归档阶段原件仍在保护范围。路径相对项目根目录。

| 文件 | 字节数 | 起始 SHA256 |
|---|---:|---|
| .trellis/tasks/09-03-35-state-cardinality-charging/research/c6-formal-acceptance-20261016.md | 5688 | B1933D27A9AC23EAF23C58AC3EE91318ECB4B1E97C6A8087D18F4957AF502F9D |
| .trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md | 16314 | 7AE400CE801E769BF5165F44454DE042C878E1714244127F2C948AC3E088EC29 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/MANIFEST.json | 11297 | 6D97F0D4E9C0EF4573E28E6C9AFE86F617341F9921BED1B71A9E5DB95258A5C6 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/README.md | 7055 | E226FCF087B0F6EFC44E6455F052A717907D0E1970D371252451FE6D42B81F46 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/check.jsonl | 485 | FC28671FB19016CE6FF2B2F04447CCD5489F3784A97BC019FBBB785C72F0EC39 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/design.md | 897 | 5A313386883018E08F015EA1D6B6A62327DB90ACCA9F70DF50B01E9E3AF75E3D |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/implement.jsonl | 501 | 31CEE52993928B65BBFF96770BB7DC47E1F02869C785EDBC64E9FFFE51CD8016 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/implement.md | 3076 | 64907AFA62B6275553E4B3B4762A22F64EAEC12591D08839C8C018CC635D9E45 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/prd.md | 2137 | 36ADCFCC5AF34C4402CB2F588DFE0C1ECF0BB6EC21CA89EF84CB3C60AA930FFA |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/00-foundations.md | 5165 | 973889D121CDF434CD25FAB83329E5DBCCF3A46393B211BB9A65E89E64A0D655 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/01-general-lemmas.md | 6302 | 5C3B543A645725C5C25042CDBB0436F936AD8DD23FF62A6E09CC9DD5DCBB451E |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/02-cross-group-structure.md | 7367 | 2288C23D51A3FB7F6F71B3D5C163210C786AED27D55F299A4D83E44A98EEA577 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/03-migration-and-obstacles.md | 7741 | 44F435352DFDF51A121BE118D61E7AC0020B87E3F0C2565DB4C5DF4AC8423C1B |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/04-round-log.md | 5153 | 4C2D567C0C9315E3731E7F79F7E1B44DF51125454615E9351387F7B4E8AAC73A |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/05-core-overlap-and-extreme-structure.md | 6298 | 02ECE624140B8D2DD72EB5A859A0B725B83A4632E11897705B68E95E082DB83E |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/06-hole-transport-and-sharp-budgets.md | 5631 | CE832DC53B2F065AC0955EC8C1437D9B54C65340ABFBFFFC9B5C7959673D1207 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/07-two-colour-balance-766.md | 5922 | 6CAD0F4DD6FF94365ECD05CA3A2BB9559E5F910F4E027E639056C8C6F06A625E |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/08-interval-descent-and-cover-obstacles.md | 6647 | 62BE788614ED6D45F71DF6AF6E324199BDD3CE215A8468E480454BE6EE3D1033 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/09-general-capacity-function-and-stability.md | 5804 | 0377645325E6D8DF66A9E0C75E4D17FD513A12A1F495174B8BFA2E7F5682BC71 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/10-saturated-edge-endpoint-cutoffs.md | 5020 | 22441981F560517A70469EDD2A8FBB478F9D022C961FDA81E94E1D3DECA937FA |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/11-saturated-cross-witnesses.md | 5644 | 20DF4D423FB4F27133E16D58C686B0777F7DF200CA65074A21110AAB1CC246DE |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/12-e41-interface-and-remaining-cases.md | 6803 | 6A7C3D233969F6A4525AE57DBA49A7AF0F18819A88AA36C435910DC70A9E7FFD |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/13-common-tail-capacity-and-deletion.md | 6972 | 1DD299919E1E04B5AA1BB6083ABA0CFEB8A00B4BFBCCD1FE06B33B6BCA8790FE |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/14-second-saturated-family-and-endpoint-branches.md | 5675 | 693EC8139065BD5D99B69FF80EB09C27F2AC2AAAD06DB9BFD09B4C5FA5510D09 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/15-blue-tail-support-and-anchor-deficit.md | 4703 | E95FA491C46502F0E754A61C15D6935B9B63611BE5D5A27A65625E57AC6A9A3A |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/research/16-forward-backward-capacity-and-remaining-extremes.md | 9175 | 85552B8BEDE054443977682D98845844FAF934E4A809BE2CD7B4751FB64CE9C1 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/ROUND1_SUMMARY.md | 5309 | 58E0945DF1A0CE94B9FC1C9505D609197C61BAA2E04314F2A5FD430372101148 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/ROUND2_SUMMARY.md | 8609 | 43CD91ECA5B2A3B7ECAC2C68D65E598539D1063A2758EC48DAAB1FA054969823 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/ROUND3_SUMMARY.md | 7719 | 2293740648060784F9426DD9948D897F0A2A7BC408568AB3BA1A97A174B861DB |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/STAGE_SUMMARY.md | 5966 | 81FCAA0BF3D2D89E3D3A20881DAC7D217BA05BC712117D3512F8579036A858C2 |
| .trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/task.json | 1184 | AFE0C40997C586069DABA9281F6597F912764FE2FE7AF450179FC8D7245CEDE3 |
| .trellis/tasks/10-19-nr7-structure-capacity/research/INITIAL_BASELINE.md | 3591 | 7D72B057D08E88EFC6D566CA75C04754FC30E56414942C16702187B41C3F06F6 |
| .trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R2_COMMON_START_CAPACITY.md | 26941 | F9FF6774E52DA1BBE1658404EF4EB714DEBB2BFD5459F535FEB4DCDF9B13044E |
| .trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R3_BIDIRECTIONAL_IDEAL_INTERVALS.md | 25747 | 1CC19E827B7F40DE147A8D694A55B14A7C6B04486BC29126A586871069BEDDD3 |
| .trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R4_BIDIRECTIONAL_COVER_DEFICIT.md | 31914 | ADCE35BD9448936EA83DD92F3B91A8852B11D1FBFB7AC86370FDA66E577394CA |
| .trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md | 21509 | A96D9F5B62C63BCEBAA2EE1139F3F66509B312D2AFB366A3CC9F986B0E0DD472 |
| .trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_DOCUMENT_CHECK.md | 9333 | 38F54822334157DA7BED46EDD477C0D9EEB7158020A5EE6119006C907D322881 |
| .trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md | 22728 | 3966740FB7D366A8037466D07E195C48F1F48897708D1512CD16CF2C4EB69DD3 |
| .trellis/tasks/09-03-35-state-cardinality-charging/research/c7-formal-acceptance-20261020.md | 6189 | FF02302949483E273A4124609C708ECBE0675D522463C4BCFC4430DD1651B4CD |

不改旧接受状态、证明绑定、运行或会话指针，长期任务保持in_progress、completedAt=null；不宣告整体完成。

