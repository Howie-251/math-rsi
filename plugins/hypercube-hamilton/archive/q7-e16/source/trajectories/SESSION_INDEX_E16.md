# E16 研究轨迹增补

原 `Ruskey–Savage conjecture n=7.rar` 的 `trajectories/SESSION_INDEX.md` 延伸至 2026-11-12，已登记完整 E14 以及 E16 的 μ=2、4。这里沿用原档的事件与审计双索引，增补此后完整 μ=3、1、0 和 E16 的接受过程。旧档位置见[汇总 HTML](../START_HERE.html#baseline-title)。

| 日期 | 事件 | 实际范围与结果 |
| --- | --- | --- |
| 2026-11-13 | 从逐子族闭合改为核同一原输入的联合覆盖 | 暂停默认扩表，保留已证子族和构造。以原输入整域的可验证覆盖作为路线尺度。 |
| 2026-11-15 | 覆盖规则调整与见证核查 | 开始在同一实际匹配上核覆盖并集。此前两份见证经回代分别命中已有三桥整面接收和受控计数工具，已证原输入净增为零。 |
| 2026-11-15 | [μ=3 整族接受](../research/seven_directions/mu3_hard_first_2026_11_15/ROOT_ACCEPTANCE.md) | 已证构造、D=24 奇支撑全实现计划及两份冻结 RUP 证书覆盖所有 56 边且 μ=3 的短匹配。 |
| 2026-11-15 | [六维 A8 接受](../research/seven_directions/mu1_global_2026_11_15/q6_a8/ROOT_ACCEPTANCE.md) | 三少数、五多数孔时可避指定多数孔并保留规定匹配。七个剩余孔轨道各以奇覆盖点纤维核出可用双桥；26/26 项独审通过。 |
| 2026-11-15 | [μ=1 整族接受](../research/seven_directions/mu1_global_2026_11_15/ROOT_ACCEPTANCE.md) | 中央差一切直接构造，两个边缘型各有验真 RUP 证书。三孔小面分支的大面归约保留 23 个必要代表，小面孔位置保持符号化。 |
| 2026-11-15 | [μ=0 与完整 E16 接受](../research/seven_directions/mu0_global_2026_11_15/ROOT_ACCEPTANCE.md) | 唯一平衡轴余域的大面归约保留 19、98、72 个必要代表，联合 CNF 经独立重建和 RUP 验真。与 E14、相邻孔补全及 E16 五个 μ 整族合并，得到任意至少 56 边的七维短匹配的全短保边 Hamilton 延拓。 |
| 2026-11-15 | [参数化双桥登记](../research/seven_directions/mu0_global_2026_11_15/Q6_BALANCED_DELTA2_TRANSFER.md) | 指定独立孔内切时提供保边 64 点圈。E16 双平衡轴是已证回代。 |
| 源段未单列日期 | [分类准入纠偏](../guide/Q7_WORKFLOW_CHANGES.md) | 先对难余域做有界试证，通过关键检验且有可执行路线再采用分类。覆盖穷尽或严格降阶在整域验收时核对。 |

## 可核对记录

- [EVENT_INDEX_E16.jsonl](EVENT_INDEX_E16.jsonl) 记录路线账本事件、验收范围与本包证据入口。同日事件沿用账本的顺序。
- [AUDIT_INDEX_E16.jsonl](AUDIT_INDEX_E16.jsonl) 收录本增补范围内的五份独立审计回执，保留 PASS、`sound-modulo-imports`、`same-family` 和 `provisional` 的原记录。

`source.path` 和一基行号引用原工作区相应版本，`source_sha256` 是原文件的 SHA-256。事件条目的 `references` 可在本包直接定位已发布的证明、回执及流程说明。审计日期沿用回执的 `generated_at`，无该字段时 JSON 为 `null`。RUP 的验真范围见各冻结回执。可复用证明方法见 [MathRSI Wiki](../research-wiki/README.md)。
