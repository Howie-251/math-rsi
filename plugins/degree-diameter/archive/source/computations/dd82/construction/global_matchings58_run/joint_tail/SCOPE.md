# 唯一输入：实际 seed3 的五轮前缀 F5

`encode.py prepare` 与 `encode.py decode` 是唯一入口，不接阶数、seed 或前缀长度
参数；默认输入输出均为本目录，解码默认读 `solver.log`。本源码不启动 solver，
不准备任何已经被排除的F6输入，不自动递减前缀、换seed或增加预算。

固定图取自 `../pilot/seed3/rounds.json` 的前五组实际匹配，直接检查58点、145边、
各点度数5及930坏对。全部1508非边共享实际无向新边变量，每点新增度数恰3；
全部旧坏点对须由真实新增直边、一旧一新路径或两新边路径覆盖。原有边和旧
两步路径在单调补全中始终存在。故SAT与包含这个F5的目标图双向等价，但不代表
任意58点图。87条新边可以构成任意简单三正则图，不必分成三个完美匹配。

原M6/M7/M8只作为一份完整邻接赋值做语义核对，不固定其中任何边；不增加匹配
颜色、旧几何、群作用或其他未证明限制。主编码直接复用
`polarity73_reduction_run/refined/completion.py` 的通用 `build`、
`check_explicit_assignment`、`semantic_sanity` 和 `graph_check`；不调用其绑定
几何删除集的 `prepare`、`decode` 或 `surviving_graph`。

准备时输出 `input.cnf`、`encoding.json`、`variable_map.json`、`sanity.json`。
指定计数器表示应为56004变量、173002子句，源码核对这一计数。完整邻接语义
检查包含无补边、全部补边、原实际八轮图（度数正确但177坏对），以及已有小图
正反例；另外加入三棱柱正例：固定三条竖匹配，新边是两个奇三角形，最终三正则
直径2，确认新增奇圈没有被颜色条件排除。每份显式赋值都逐条比较CNF与实际BFS。

解码要求完整DIMACS赋值并检查每条子句，再重建实际边表、度数和全部BFS距离。
成功输出的 `candidate.json` 含 `n`、`edges`、`ambient_labels`，并写连续标签的
`candidate.edges`；非目标不得成功退出，图检查失败时保存完整坏点对。
根代理随后另调现有独立 `verify_hs_candidate.py`。

这里只有一个计划内固定前缀输入。SAT须通过完整图检查；无证明日志UNSAT只记
未认证结果；UNKNOWN仅表示未决定，均不能升级为整个58阶或全部匹配生成族结论。
