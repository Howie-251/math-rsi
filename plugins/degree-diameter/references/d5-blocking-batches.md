# D12 有界续批与已验前缀收件

本接口服务于原 D12 部分折叠源族：最大度 12、核心标签 `<41356`、原 754 张平面的 91 条核心行。它由真实成功程序整理而来，不是任意 D5 图生成器。构造原理与 D11 的不同核验方式见[联合补全](d5-joint-completion.md)。原始程序、证书和数据完整保留在[2026-11-16 原包](../archive/dd-latest-two-parameters-20261116/README.txt)，可调用修正版位于 `../tools/`；原包不因维护而改写。

## 调用前先接实际源

父调度已经接受源图的简单性、度数与直径上界，再将实际源路径、点边数和证据写入**现有** STATE 的 `current_context.families["12,5"]`。`generator_domain` 必须为 `d12_754_planes_core41356`。`latest_graph` 需有 `n`、`m`、`edge_file`、`evidence`，且对应非空 `accepted_orders` 中最大已验阶数。批次驱动是已验前缀的续接器，不初始化研究、源认证或另一份状态库。

只有输入域、核心覆盖引理和实际折叠都与原族相符时，才能使用原平面表。表在包内
`originals/ar4math/research/ddp/expert15_20261114/d5_resume_20261115/d12_blocking_family_continuation/RAW_PLANES_ACTUAL_IDS.txt`。
换源族时先重新证明其接口；修改几个常数不能完成迁移。

```sh
DD_PLUGIN="/path/to/MathRSI/plugins/degree-diameter"
python3 "$DD_PLUGIN/tools/d5_blocking_batch.py" \
  --state /task/STATE.json --planes /task/RAW_PLANES_ACTUAL_IDS.txt \
  --output /task/new-batch --max-new 8 --cpu-limit 20 --wall-limit 480 --plan-only
```

`--plan-only` 只读计划，不编译、不搜索。去掉它才执行，并要求现用状态为 ACTIVE，实际授权及总预算仍由父调度与宿主维护。执行前重新读取暂停状态、已登记的返回终态、最新源路径/点边数/生成域；旧计划失效时在创建输出目录和启动进程前退出。相对源图路径以 STATE 所在目录为基准，输出目录必须不存在。

工具依赖 Python 标准库、POSIX `resource/preexec_fn` 和 C++17 `g++`。预算统计包括编译、控制检查与 native 子进程；CPU 限额是单进程机制加整批实际计费，不宣称分布式总预算硬隔离。实例数、CPU 与墙钟参数由当前任务决定，示例不构成新研究授权。

## 回收：已返回、待独验、已接受分别记

作者的 `accepted_new_graphs` 是历史字段名，只表示作者检查命中。批次输出保持 `independent_validation: PENDING`。由原独验程序检查每个实际前缀的全点度数、旧边保留、新根完整距离与终图边集，父调度读原件后决定接受范围，再使用收据适配器写回。

```sh
python3 "$DD_PLUGIN/tools/extension_receipts.py" \
  --state /task/STATE.json --family 12,5 \
  --author /task/batch/RESULT.json --independent /task/batch/independent/RESULT.json \
  --acceptance-basis '已读原件并接受这些前缀；源D5沿用指定证据，具体Lean仍开'
```

适配器仅支持原逐点保边 JSON 格式，**不运行 BFS，也不替代父调度的数学接受**。它检查源、连续前缀、终图与独验收据一致。源必须对应 `latest_graph` 或 `accepted_checkpoints[源阶数]` 中已有的 `n/m/edge_file/evidence`，并与独验原件的 `construction_inputs.source_raw_edge_file` 绑定；同阶但另一张图不能混用。源与终图的已接受身份保存在原家族记录里，无额外数据库或哈希。

`accepted_orders` 只列已接受的新增阶数。旧收据复读保留其源 checkpoint，不重复计数、不用早期成功覆盖后来同图的零新增 UNKNOWN 或限定域 No。作者与独验原件每批独占不覆写路径，`consumed_receipts` 保存已消费的路径对。真正新批次可更新停止状态，不人为给 UNKNOWN/No 排先后级别。旧材料搬迁后，父调度保留原收据逻辑路径对应的 checkpoint，另给当前可运行源路径；不能仅凭 basename 相同冒充同一来源。

只有需要原 DD 汇总时才设置 `phase_start_counts`；可选计数由 DD 适配器产生，Base 不依赖图家族或 Lean 数量。完整字段和真实 batch01 兼容性检查见[软件接口记录](../../../development/evolution/v5-dd-20261116/checks/WORKFLOW_HELPERS_REPORT.md)。

## 决定下一步，而不是自动续跑

| 返回 | 父调度消费为 |
|---|---|
| `BATCH_LIMIT_REACHED` | 本批数量达到上限；依边际成本与剩余总预算决定一个有限后继，不称机制耗尽。 |
| `UNKNOWN_*` | 本次预算内未决。保存已生成前缀并独验；不能当成 No，也不能自动续费。 |
| `COMPLETE_NO_IN_CURRENT754_SUFFICIENT_PLANE_DOMAIN` | 只排当前图的这 754 张平面充分证书域，不排所有图或其它构造机制。 |
| 进程/准备错误 | 按实际 compile/control/native 阶段处理；准备完成不等于搜索已开始。 |

原 D12 后三批分别新增 8、8、14 图；最后一批在继续找 42,434 点图时遇预算停止，已验 42,433 点前缀保持有效。每轮都应消费已得成果，而非把整批 UNKNOWN 当作零成果。源图 Lean 缺口与原最终审阅要求仍保留为共享义务，不为每个 `+1` 重开相同条件 wrapper。

派发前可在原在途记录登记只在终态落盘的 `terminal_result`，由[当前事实交接](../../../base/skills/mathrsi-research/references/current-context.md)检查漏收。已有结果先由父调度消费，再生成下游输入；终态存在不等于接受。所有状态更新均不自动恢复 Goal、不启动下一批。
