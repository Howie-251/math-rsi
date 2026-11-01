# 22 点及 23 点双锁分支的实际类型表

2026-10-06；源码 `formal/Aris4Math/DoubleTripleLockProfiles.lean`，命名空间 `Aris4Math.DoubleLockProfiles`。文件仅负责双锁；三锁 6,7,7 分支由单独的 `TripleLockProfiles.lean` 负责。

核心接口：

- `realizes_v22_66`、`realizes_v22_67`、`realizes_v22_77`
- `realizes_v23_66`
- `exists_realized_profile22`

前四项都接受真实超图 `H`、32 条边、不同顶点 `x,y`、实际共度 `codegree x y = 1` 和相应两点度数，结论为已有具体 Numeric 剖面的 `RealizesProfile`。两点以 `Fin 2` 标记，0 对应 x、1 对应 y；锁定位置固定为从 0 开始的 10、11，即 Numeric 的 11、12。

`exists_realized_profile22` 只要求实际点对覆盖和 32 条边，通过 `LowDegree.exists_two_locks_of_twenty_two` 导出其中一份实际表，不把低度选点或类型计数作为未证前提。

## 类型计数的来源

`four_partition` 对任意有限集和两个谓词证明四个布尔成员区域的基数和等于全集基数。将两个谓词取为“x 在该边内”“y 在该边内”，即可得到实际边集的四类分区。

`two_counts` 使用实际 degree/codegree 定义，推出精确计数：

| 锁定位置类型 | 实际边数 |
|---|---:|
| 空 | `33 − degree(x) − degree(y)` |
| `{11}` | `degree(x) − 1` |
| `{12}` | `degree(y) − 1` |
| `{11,12}` | `1` |

`two_type` 证明实际 `positionType` 恰对应这四个区域；`realizes_two_profile` 同时证明表覆盖所有实际边、类型列表不重复、每一行重数正确，再与 Numeric 中的四份已核验数据逐一对应。

这里的四类讨论是对单条任意边的成员谓词作逻辑分区，未枚举超图或用搜索未命中作为依据。

## 核验和边界

全部 11 个定理已真实编译并逐项导入后审计：重编译 5.255 秒、导入审计 3.160 秒，退出码均为 0；只依赖标准 `propext`、`Classical.choice`、`Quot.sound`。无 `sorry`、新增公理或 `native_decide`。

构建日志、实际命令、退出码及完整公理审计保存在 `.aris/traces/proof-checker/2026-10-06_run07/`，文件前缀 `lean-doublelock-profiles-`。

本模块给出实际结构到类型数据的证明；22 的 6/7、7/7 以及 23 的 6/6 所需 link 扣除，由 LinkDeletion/ProfileDeletion 和最终 ProfileApplication 连接。本模块未自行宣告整体 Property B 目标完成。
