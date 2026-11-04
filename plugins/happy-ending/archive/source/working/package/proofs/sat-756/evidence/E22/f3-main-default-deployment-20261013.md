# F3 主变体 + bridges 默认方案部署记录

2026-10-13 15:59:17 +08:00，已完成本地源码更新及权威 Linux 服务器部署。新建 C_r 公式默认采用原 exact 编码 + bridges + 已测 F3 主变体，标识为 `legacy_exact_with_state_path_bridges_f3_main_v1`。

服务器工作区：`/data/ktqiu_hdd/math_agent`。运行环境：`forktqiu3`。本次没有启动新的 C_r 搜索或重跑 baseline。

## 接口及修改内容

```python
# 新默认：exact + bridges + F3 主变体
built = materialize_cell(environment, cell)

# 显式复现历史 bridges 方案
old_bridges = materialize_cell(environment, cell, f3_main=False)

# 显式复现历史 exact 方案
old_exact = materialize_cell(environment, cell, bridges=False)
```

`f3_main=None` 跟随 `bridges`；显式 `f3_main=True, bridges=False` 拒绝。所有选项严格检查布尔类型。F2、F2+F3 组合及 F3 vertex 变体没有进入默认生产编码。

- `state_charging/f3_main_rank.py` 提取已测 F3 主变体的通用前缀计数和位置秩约束，保留辅助变量分配顺序与子句顺序；生产模块不依赖 tmp/res 实验代码。
- `state_charging/cardinality_layers.py` 接入新默认、显式兼容开关、独立 F3 元数据以及 SAT 审计重建。原 exact 变量/子句保留，F3 使用新的连续辅助变量；bridge_clause_count 仅统计 bridges。
- `state_charging/cardinality_campaign.py` 独立验证 exact 层与 F3 层的变量边界、计数、规范元数据和哈希；声称新默认却缺少 F3 元数据的记录会被拒绝。重新计算外层哈希不能修复这些结构错误。
- 当前生成器的自动源码封存检查纳入新模块；增加对应测试，并更新当前 README、编码说明、AGENTS 默认编码段及 Trellis 规范。

## 语义依据与验证

F3 的位置秩约束来自原状态语义：若顶点 v 的状态为 h，已占用的真子集状态必须出现在 v 之前，已占用的真超集状态必须出现在 v 之后，因此数量分别不超过 v−1 与 N−v。前缀阈值辅助变量使用双向定义，每个原赋值均有唯一规范扩展。保留全部原子句，并只追加这些定义和蕴含约束，保持对原变量投影后的 SAT 等价性；此论证不依赖目标实例已为 UNSAT。

所有代码测试和公式生成均在 Linux 上执行：

| 验证 | 结果 |
|---|---|
| 既有 cardinality/bridges/campaign/remote tools 回归 | 40/40 通过 |
| 新 F3 前缀阈值、辅助变量唯一性、选项与元数据篡改测试 | 10/10 通过 |
| strict/relaxed × 原方案/F3 的非空小 SAT 控制 | 4/4 SAT，完整赋值检查、独立状态/路径重放及规范扩展通过 |
| 已测 F3 主变体 + bridges 的 CNF 字节身份 | A[1,1]、A[1,2]、A[1,10]、A[6,10] 全部匹配 |
| 原 exact / bridges 显式兼容选项 | 四个 case 共 8 个字节身份全部匹配 |
| 实际 campaign 记录和自动源码封存 | 通过，包含新模块和新增辅助变量元数据 |
| 部署后新进程导入与 A[6,10] 三种配置 | 新默认、历史 bridges、历史 exact 均匹配预期 |

四个新默认 CNF 的身份如下；这些是字节对照，未重新求解：

| Case | 变量数 | 子句数 | SHA256 |
|---|---:|---:|---|
| A[1,1] | 336790 | 1243528 | `008d05ace6a862097ac5268bdaef6b5e8b80096617fc376f9be67176a777f625` |
| A[1,2] | 392563 | 1445029 | `2dd663a9e87d346fe310f6da558b5308644e29353274d227074527fa6dc11193` |
| A[1,10] | 1134717 | 4114707 | `5e1e4efe3064eecb5b4528ddcac119fe51bb87cb562b880c2df0126a3e6f5ee9` |
| A[6,10] | 603443 | 2205456 | `55e3fd3c7f48373608fff0a29172c3f0dbce260aad5214411ba6fb20c0eaa8c1` |

A[6,10] 的新默认追加 9514 个 F3 辅助变量和 37140 条 F3 子句；原 bridges 为 4814 条。部署后历史 bridges 的哈希仍为 `43e266566b2ed80a9b5d8aa5ccce169d5aec54410baa1bf57a3dbf4a7a9a5073`。

本次没有运行证明检查器，没有新增 checked UNSAT 或定理接受记录。先前性能实验的 raw UNSAT 不因本次代码部署而升级。上述小 SAT 控制只验证实现和模型扩展，不是新的 C_r 性能实验。

## 部署与来源绑定

原生 `gpt-6.1-sol/high` 子代理完成实现、隔离测试和部署准备。其后连续两次模型容量错误，用户明确允许主线程仅完成剩余部署及部署后核验；未改变项目默认模型分工。独立 Claude 路线仍停用，本记录不声称完成独立 Claude 审阅。

部署前逐项核对原文件与已保存备份，部署 13 个明确文件；部署后核对 34 个运行源码的完整哈希。7 个修改/新增的 Python 文件本地与服务器完全一致。文档按各主机的原内容做窄修改，AGENTS、downset 规范和 parallel 规范未强行做整文件跨主机覆盖；内容或换行差异记录在 transfer_manifest.json。

核心已部署源码哈希：

| 文件 | SHA256 |
|---|---|
| cardinality_layers.py | `013cc48189a470cbed9035f77366da7fbf943df53f8cf344bd46e78827a0554f` |
| cardinality_campaign.py | `5226d6bba7375da44792cadc7151c972bdee0b14cf81df0a8f4fd909df52d410` |
| f3_main_rank.py | `d5ea34863e4f7c00b20665c56bff06929e16a86721438434d48d429791287004` |

部署回执状态为 `deployed_verified`（工程部署状态，不是 UNSAT 证明状态）。SHA256：`d27228df4aab5f75f72d30166c915cee0e66651274df05aae4e8b4f4a976f200`。

已核对 5 个既有封存入口及 C6/C7 的 4 个完整进程身份未变，未重启、终止或修改既有生产任务。所有旧 baseline、保留实验数据、封存运行时和证明保持原状。未执行 git commit/push。

服务器记录根：`/data/ktqiu_hdd/math_agent/tmp/f3_main_default_20261013`。原代码备份在其 `server_preimage/` 与 `server_preimage_manifest.json`；本地备份在对应 `local_preimage/`。

本地原始证据：`tmp/f3_main_default_20261013/collected_final/`，共下载 15 个小型文件、66403 字节，无 CNF 或证明下载。重要文件为：

- `deployment_receipt.json`：部署目标、源码哈希、部署后默认配置、封存与进程核对。
- `verify_active.stdout`：使用 `python -I -B` 从活动目录重新导入并核对三个 A[6,10] 配置。
- `validation/prepared_stage.json`：13 个目标和 34 个隔离运行源码的清单。
- `validation/tests.json` / `tests.stderr` 与 `f3_tests.json` / `f3_tests.stderr`：50 项测试原始结果。
- `validation/parity.json`：四个 F3 主变体和八个兼容选项的 CNF 身份。
- `validation/small_sat.json`：四个可满足控制及模型扩展/重放记录。
- `transfer_manifest.json`：传输哈希和本地/服务器源码对照。

验证脚本早期三次遇到调用约定/目录布局错误；原始 stderr 已保留。修正版按实际 campaign 写入契约通过，没有为通过验证而放宽生产校验。
