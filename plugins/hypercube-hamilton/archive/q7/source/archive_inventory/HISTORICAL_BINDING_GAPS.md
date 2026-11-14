# 冻结版本恢复与剩余历史缺项

已定位 47,033 条 JSON 冻结引用中的 47,025 条。另 8 条要求的历史字节未找到。保留原清单和现存同名版本，未解析记录列出具体引用、来源清单和要求的 SHA-256。两项关键离线重放使用的 178 条去重引用全部定位。 [未解析清单](unresolved_bindings.jsonl) · [两项重放输入](key_check_inputs.json)

| 所在清单 | 未取得的历史版本 | 影响范围 |
| --- | --- | --- |
| E14 低差与小跨数提交 | `R7_JOINT_COVERAGE_SCOPE.md` | 提交当时的联合覆盖台账。现存新版列出各已审命题。低差证明正文在结尾以台账提示其余覆盖路线，逐项论证和所引证明保留。该历史清单尚不能逐字节完全复验。 |
| Q6 T15 D3 独立检查结果 | `Q6_T15_D3_BATCH_REVIEW_check.cpp` | 一份旧 C++ 检查器版本。归档保留现存同名源码、Python 驱动和机器输出。旧回执要求的 C++ 字节尚无法重放。 |
| R7 P2 残余引理输出 | `r7_p2_residual_test2.cpp` | 一份旧残余探针源码。归档保留现存同名源码及固定探针输出。要求旧源码字节的原运行尚无法重放。 |
| Q6 A6 后果与状态审计 | `PROOF_PACKAGE.md`、`NEXT_OBLIGATIONS.md`、`PROOF_CHECK_STATE.json`、`RUN_STATE.json` | 四项历史包导航、义务或运行状态版本。数学证明、计数证据与审计回执可阅读。该历史状态审计尚不能逐字节完全复验。 |
| ARIS 介绍文档的审阅回执 | `docs/ARIS_INTRO.md` | 上游介绍文档旧版。现存介绍和回执保留。 |

从六维 RAR 及现有工作区筛查同名候选时，历史版本必须满足冻结 SHA-256。七维旧运行状态和错题集的精确版本经当前文件前缀重建，原七维项目 `AGENTS.md` 则从 E 盘源路径取得。三个恢复结果均逐字节符合其冻结 SHA-256。

六维 T15 core8 历史背景集的三份二进制和一份台账也已恢复。以冻结的 `eight_after_balanced_bridge_candidates.json` 为基，从原行序筛去 `core_choices` 与 `{0, 5, 15, 18, 21, 23, 25}` 相交的行。按目标 1、7、31 连接各行的 `bytes(Z + W)`，分别得到 1,495、2,162、2,270 条，共 5,927 条。依据旧 core4/core24 台账的字段顺序与 `refresh_eight_core_ledger.py` 的口径重算历史台账，使用 UTF-8、两空格缩进、CRLF 和终止换行。四个输出均与 core8 审计的 `context_snapshot_hashes` 相符。该审计把这组文件列作历史工作集背景，另列定理证明、证书、导入、检查器和结果的冻结散列。 [core8 审计](../research/six_directions/T15_CORE8_FULL_REVIEW.md) · [恢复位置](../history/source_versions/q6_core8_context/research/six_directions/)
