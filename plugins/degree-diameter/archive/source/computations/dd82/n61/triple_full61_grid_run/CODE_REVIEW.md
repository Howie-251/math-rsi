# Full61 U-by-Ta grid wrapper：增量源码审查

日期：2026-10-13。审查身份：**reused-agent，同一 Codex 审查代理的增量复核**；
沿用此前 `../triple_full61_run/CODE_REVIEW.md` 的基础审查，不冒充 fresh-agent
或 Gemini。依据项目 `experiment-bridge` 的源码审查步骤，范围仅为本次 wrapper。

**结论：未发现阻断问题，可进入根代理安排的有界准备与执行。**

本次读取新目录的 `encode.py`、`runner.py`、`SCOPE.md` 与
`proofs/dd82/n61/CONNECTED_TRIPLE_GRID_NORMALIZATION.md`，并定点检查基础模块的
路径与接口。新归约的数学接受状态由根代理提供；本次不重复审查其证明或完整基础编码。

- 新编码仅替换基础模块的 `fixed_adjacencies`，先取得全部旧固定项，再追加坐标项。
  原来的 1830 边变量、61 个全度数约束、两种 port case、全部实际二步路径和覆盖条件
  仍由原函数生成。四个旧匹配没有改动，也未固定 C、sigma 或 V-Z 的排列。
- 完整 U-Z 块为 96 项：F 的索引 0..3 与 U 对应；其余顶点严格使用
  `Z[4+4*i+j]`，覆盖索引 4..23，即实际顶点 41..60。完整 Ta-Z 块为 120 项：
  Ta[i] 仅连第 i 行的四个非 F 点，并对 F 取零。两块合计新增 **216 项：44 个 1、
  172 个 0**。其中 196 项来自三族新编号公式，另 20 项为旧 exact-degree-0
  已蕴含的 Ta-F 零值；两种计数口径一致。
- 两个 wrapper 在动作前修改导入模块的 `HERE`；导入函数的全局名称查找因此读取
  新目录。基础 `ROOT`、通用 helper、求解器、checker 和 BFS 的项目级路径仍正确。
  runner 的 prepare/decode 子进程调用新目录 `encode.py`；编码、模型、边表、日志、
  proof、BFS verification 和 checker 结果均使用新目录。编码器 decode 的默认 log
  参数也由新 wrapper 给出。旧模块受 `__main__` 保护，导入时不启动动作；导入前
  禁用 bytecode 写入，不修改旧证据目录。
- SAT 的完整模型检查与独立 BFS、RAW_UNSAT 到单独 LRAT 检查的处理，以及所有
  CPU/wall/memory/output 上限均沿用已审基础 runner。两种 case、gamma-delta 边
  的两种可能及全部 96 项 V-Z 均保留。

实际轻量检查：两份新源码 AST 解析通过；仅加载定义并调用新旧 fixed-adjacency
函数，用实际顶点编号独立构造期望坐标块，确认完整新增字典恰为上述 216 项、
旧项值全部不变、没有冲突、V-Z 与 gamma-delta 未固定；同时确认 prepare/decode
及 runner 三个动作的全局 `HERE` 全部指向新目录，项目根目录一致。

未调用 prepare、decode、solver、checker 或 BFS，未生成 CNF；未改动作者源码或
旧运行证据。此结论是源码增量接受，不是运行结果、性能提升或数学排除证据。
