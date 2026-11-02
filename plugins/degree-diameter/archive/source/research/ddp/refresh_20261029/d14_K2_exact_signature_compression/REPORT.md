# 精确签名表示门终态：无实质目标行压缩，停止

仅使用既有完整 R3/R4 缓存、FREE_ORDER 和 FREE_SPARES，完成全部端口和
目标的有序双位集精确相等分组。没有图读取、BFS、SAT、包含筛或原模型续时。

| 数据 | 原数 | 精确等价类数 | 合并数 |
|---|---:|---:|---:|
| 完整 (R3,R4) 端口签名 | 3685 | 3589 | 96（2.61%） |
| 完整 (R4support,R3support) 目标行对 | 94186 | 94069 | 117（0.124%） |
| 两 helper 的完整覆盖行 | 188372 | 188138 | 234 |

两种相等类的最大大小均为 2。端口组容量 `min(2,Σspare)` 为 1 的有
3480 组，为 2 的有 109 组；若使用组 selector，共需 7178 个 A/B selector。
每组的具体端口、spare、representative，以及容量 2 时的两次使用重建方案
均保存。压缩后完整目标系统仍有 188138 条覆盖行，不能把旧稀行模型
冒充完整系统；本次没有生成或启动任何新 CNF。

数学保全：同 helper 选择多个完全同覆盖组的 port 时，保留一个即可保持
所有 R3/R4 覆盖且不增占用和 pin 数。两 helper 需要该组两次时，要么同一个
spare≥2 的 port 分别连接两 helper，要么选两个不同 spare≥1 的 port。
各组端口不交，重建可逐组完成。目标行只在 R4 和 R3 两个支持集合同时相等
时合并；按组代表转置与完整原列的相等关系完全等价，因为被去掉的列只是
整个覆盖列的复制，没有丢弃任何不同的支持模式。

输出文件：

- `PORT_GROUPS.json`：所有端口组的完整成员、原标签、容量及具体重建方案。
- `port_to_group.u32le.bin`：原 3685 个缓存列位置到组编号的映射。
- `TARGET_CLASSES.json`：94069 个目标类的最小标签 representative 与大小。
- `target_to_class.u32le.bin`：全部 94186 个原目标标签到类编号的映射。
- `target_R4_group_support.u64le.bin` 与 `target_R3_group_support.u64le.bin`：
  行主序，94186 行，每行 57 个 little-endian uint64；位 g 表示端口组 g。
  类 representative 可直接定位对应完整覆盖支持行。
- `INPUT_ORDER_BINDING.json`：FREE_ORDER 与 FREE_SPARES 的 3685 个标签逐行一致。
- `RESULT.json` / `TERMINAL.json`：全部实际计数与计时。

编译与完整处理 **1.585135226 CPU 秒**，其中原生处理 **0.472294 秒**；
末尾文本顺序绑定的微小成本另记 RESULT，仍低于 10 CPU 秒预算。
这是既有 K2 模型的等价表示检查，不是新增构造方法，也不排除 K2 可行性。
由于目标行几乎没有压缩，按事前停止规则收束，不运行新 solver。
