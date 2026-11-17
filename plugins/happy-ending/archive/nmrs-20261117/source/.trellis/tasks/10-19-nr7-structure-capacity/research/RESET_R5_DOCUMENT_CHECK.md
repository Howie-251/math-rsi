# RESET-R5 文档与文件保存检查

日期：2026-10-20。本记录仅检查文档管理与一致性，不独立验证数学，不构成独立审阅或正式验收。全部新增数学来自主会话Astra并保持unreviewed/unaccepted；本轮没有运行研究代码、SAT或实验，没有调用reviewer。

## 检查范围

当前入口为task.json、prd.md、design.md、implement.md、STAGE_SUMMARY.md、research/README.md、implement.jsonl和check.jsonl；新稿为[RESET_R5_COVER_AUGMENTATION_CAPACITY.md](RESET_R5_COVER_AUGMENTATION_CAPACITY.md)。身份、createdAt、in_progress、completedAt=null及原acceptance_status保留；current_analysis_path指向R5，previous_analysis_path指向R4。

R5草稿推导总界44/58/101/201、普通O26/30/31/32、gap18/28/70/169，直接改善1/0/1/1、额外递推0/0/1/4、总改善1/0/2/5；这些只是主会话草稿，新接受未发生，旧接受基线45/58/103/206及gap19/28/72/174按原证据保留。此处只核对入口转写口径。

## 检查结果

文档检查已完成：task.json解析通过；两个JSONL各10条均解析通过，全部引用存在；50个本地Markdown链接均存在；10个本轮文件无尾随空白或冲突标记，git diff --check通过。任务身份、createdAt、in_progress、completedAt=null、原acceptance_status及R5/R4当前/前稿路径均核对通过。36项保护文件SHA256及字节数全部与起始记录一致；27/27份归档snapshot原件另与原MANIFEST的SHA256和字节数一致。只按授权更新当前STAGE_SUMMARY，归档阶段原件原字节保留。没有运行研究代码、SAT或实验，没有启动独立审阅。

## 起始保护记录

以下36项均在本轮写入R5及更新入口前，用PowerShell Get-FileHash记录SHA256并读取字节数。包括R1—R4、INITIAL_BASELINE、归档全部29项（27份snapshot原件及README/MANIFEST）以及两份旧证明依赖；不含按授权更新的当前STAGE_SUMMARY，其归档原件仍包含在保护范围。

路径相对项目根目录。

| 文件 | 字节数 | 起始 SHA256 |
|---|---:|---|
| .trellis/tasks/09-03-35-state-cardinality-charging/research/c6-formal-acceptance-20261016.md | 5688 | B1933D27A9AC23EAF23C58AC3EE91318ECB4B1E97C6A8087D18F4957AF502F9D |
| .trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md | 15700 | 68BE10BA7D8118C6A9ABD4E85D138DBFF095045B09AB4968E4D8BB2441093661 |
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
| .trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md | 22728 | 3966740FB7D366A8037466D07E195C48F1F48897708D1512CD16CF2C4EB69DD3 |

这些检查不改变旧接受状态、证明绑定、运行或会话指针；长期任务保持in_progress、completedAt=null。

