# 全部精确组与全部目标的 K2 模型

`model.cnf` 已完整生成，**100492 个变量、385396 条子句、129971928 个 literal
occurrences、631293647 字节**。当前仅准备，**未调用 solver**。

本模型恢复全部 **3589 个合法精确覆盖组**，不限制为分数解的 391 个正组；同时
直接加入全部 **94186 个目标的双侧共同覆盖**。原全端口模型只取部分目标行，
391 模型虽含全目标却额外限制了列。本目录是完整组、完整目标模型，未续任何旧
timer，也不将旧 UNKNOWN 当作不存在证据。

## 字面输入和映射

`INPUT.json` 指向现成 `d14_K2_exact_signature_compression/` 的两份转置支持缓存：
每个目标连续 57 个 little-endian uint64，bit g 是原精确 group g。3589 个有效位
后的 padding 必须为零；生成器同时核 R3 支持包含于 R4 支持。没有源边表读取、
新球计算、BFS 或 LP 列筛。

`SELECTOR_MAP.json` 完整保存原组成员的 column、旧顶点标签及 spare。组 g 的
A selector 为 `g+1`（1..3589），B selector 为 `3590+g`（3590..7178）。
原组顺序不变。3480 组容量 1，109 组容量 2。

同 helper 在同一个完整 `(R3,R4)` 等价组多选端口不增加覆盖，删掉多余选择不增
度数和容量使用，所以每侧每组至多一次是无损约简。两侧同时选容量2组时，有
spare2 成员可供两侧共用，或可用两个不同 spare1 成员；同旧点连接两个不同新点
不构成重边。不同组成员不重叠，重建可逐组独立完成。

## 计数、容量与完整覆盖

每侧采用与391准备器相同的 forward 顺序阈值计数，阈值1..13。达到阈值必须向后
传播；新选择把上一阈值推进一级；上一前缀达到13时禁止再选。任意超过13的
selector 赋值触发冲突，任意≤13的赋值可用真实前缀阈值扩展，故辅助变量无需
反向定义也精确表达投影后的 at-most13。

- 7178 个 selector。
- 93314 个计数辅助变量，193778 条计数子句。
- 3480 条容量1互斥 `¬A_g∨¬B_g`；容量2组无互斥。
- 两个 helper 间固定一条新边，各侧≤13个 pin 给新度≤14；这条新边不占旧端口。

目标 t 的两条原始覆盖子句为

```
OR_{g:t∈R4_g} A_g  OR  OR_{g:t∈R3_g} B_g
OR_{g:t∈R3_g} A_g  OR  OR_{g:t∈R4_g} B_g。
```

完整系统原有188372条覆盖行。程序以完整 `A的57words || B的57words` 为 key，
只作精确相等合并；side0 key=(R4,R3)，side1 key=(R3,R4)。输出中 side A/B 对应
的变量支持与这个 key 相同，不把未编码目标推断为已覆盖。
仅合并 **234 条**完全重复行，保留 **188138 条**，各条486..888个 literal。
因此总子句数为 `193778+3480+188138=385396`。

全部原目标保留在 `target_side_to_coverage_row.u32le.bin`：先 side A 的94186项，
再 side B，值为零起始唯一覆盖行编号。`coverage_row_representatives.tsv` 保存每行
代表 `(side,target)` 与重数；另有 `coverage_row_multiplicities.u32le.bin`。
唯一覆盖行紧跟 CNF 前197258条计数/容量子句，顺序与行编号一致。

没有 LP 支撑限制、行支配、稀行选择或 A/B 对称规范。

## 实际执行与记录恢复

准备入口为 `python prepare.py --prepare-only`，没有 solve 入口。编译/native
串行，各为单进程；观察超时只轮询同 PID，不 kill/restart。

| 进程 | PID | 返回码 | 已记录 CPU 秒 |
|---|---:|---:|---:|
| 初始 Python driver | 2495003 | 1 | self CPU 未保留 |
| 唯一编译 | 2495004 | 0 | 0.947397 |
| 唯一 CNF native 生成 | 2495009 | 0 | 1.460136 |
| 记录恢复，只读一次 CNF | 2524344 | 0 | 1.008549350 |

原生程序已经完整写出 CNF 并返回0，但初始 driver 用 `NATIVE_RESULT.json` 保存
子进程记录，覆盖了同名原生统计，随后读取 `variables` 时 KeyError，故 driver
返回1。已将源码中的原生统计文件改名为 `CNF_BUILD_RESULT.json`，**没有再次编译
或执行生成器**。

`recover_metadata_once.py` 仅读已经完整保存的 CNF 一次，恢复 header/条数/literal
数/行宽，核全部原目标映射的重数一致；结合原生完成日志及子进程成功返回，写出
`MODEL.json`、`PREPARE_TERMINAL.json`。CNF 没有被修改。原生记录与初始异常日志
保留在 `NATIVE_RESULT.json`、`native.log`、`prepare.log`。
已测编译、native和恢复合 **3.416082350 CPU 秒**；初始 driver 的少量 self CPU
未记录，故不伪称这个数是精确总 CPU。该次准备未因异常重启，也未耗尽90秒预算。

对子句 key、两侧输出极性、selector 位号、行映射、组容量及 forward≤13 的独立
只读源码检查通过；没有另跑数学候选或图校验。

## 交 root 审阅后的边界

尚无 solver 调用、整数候选或新图。拟后续最多一次 solver≤300 / whole≤420 CPU，
UNKNOWN 即停；此处没有自动启动。真 SAT 后须用原完整57word支持核全部双侧目标，
再按组成员重建实际 A、B，root 另验新根；不得把 SAT 文本直接当合法新图。

本模型只针对固定94186源、既有全部合法freeport、加入相邻两个helper且每侧≤13
的 K2 操作。它没有删除原边、改变原图或处理一般 degree14/diameter5 构造。
