# nonuniform58：唯一有界发现试验交付

2026-10-18 UTC。Run `dd82-hil-nonuniform58-20261018`。

**实际终态为 UNKNOWN。** 唯一正式准备成功，唯一无proof求解在设定的
28秒软时限正常结束，exit0；没有返回SAT模型，也没有得到UNSAT排除。
该构造族在数学上仍开放，58–61整体目标和已登记57≤N(8,2)≤61区间不变。

**复核状态：方向审阅已接受；fresh源码审阅PASS；同线程第2轮实际
交付复核已返回SUCCESS／ACCEPT。有限实验已交付，同一结构的纸面研究继续，未登记机制关闭。**

## 精确输入范围

左侧诱导为固定C28，右侧为固定C30加六条自由选择、两两不共端的非圈弦。
全部405个弦位和840个跨边位共同自由。左跨行和为6，右跨列和加弦度为6，
故完整图恰58点232边、每点度8；所有实际点对都必须有真实一跳或两跳路径。
没有预设弦端点或配对，也没有跨边周期性、额外排序或旧J＋P归一化。

它覆盖所有可按此固定圈加匹配弦规则表示的图，不覆盖任意非均匀58点图。
完整定义、代表重标与编码语义见 [PLAN.md](PLAN.md)、[SCOPE.md](SCOPE.md)
及 [encode.py](encode.py)。

实际保存的 [input.cnf](input.cnf) 首行为 `p cnf 73701 235491`，
与 [encoding.json](encoding.json)、独立源码计数及求解记录一致。
主变量1245个、计数辅助20616个、真实两自由边路径辅助51840个；
1537个非恒真覆盖OR与116个固定圈路径覆盖共同处理全部1653个无序点对。
通用实现保留了匹配条件下不会成立的9000个两弦路径AND，语义仍是同一族。

## 实际运行与终止原因

| 动作 | 实际结果 | CPU秒 | 墙钟秒 |
| --- | --- | ---: | ---: |
| 唯一正式准备 | exit0；生成完整输入并通过保存CNF赋值检查 | 1.093080 | 1.117314 |
| 唯一无proof CaDiCaL调用 | UNKNOWN；exit0，正常软时限停止 | 28.016724 | 28.150117 |

未经舍入的测量保存于 [preparation_process.json](preparation_process.json)
和 [result.json](result.json)。准备限20CPU／30墙钟秒；求解命令为
`cadical -t 28 input.cnf`，外层hard30CPU／45墙钟秒。两者均单核CPU1，
4GiB地址空间、每文件256MiB。具体配置见 [launch.json](launch.json)
及 [runner.py](runner.py)。

[solver.log](solver.log) L14明确记录 `-t 28` 的28秒real-time软时限，
L279记录 `c UNKNOWN`，L339记录 `c exit 0`；result中的
`wall_timeout=false`、`termination_signal=null`。没有触发外层墙钟终止，
也不是CPU硬杀或输出上限故障。日志没有SAT终态或模型行。

本次 `solver_calls=1`、`proof_logging=false`、`proof_checked=false`、
`target_graph_verified=false`。没有SAT模型，故没有执行模型解码或独立
BFS验收子进程，也没有生成候选边表或候选验收报告。

## 已完成的语义检查

[small_sanity.json](small_sanity.json) 保存8个AND真值和五份完整小图赋值：
合法十点四正则直径2正例；保持全部度数但有1个坏对的负例；删跨边；
删弦；违反匹配并具有真实两弦路径的负例。全部辅助定义、计数失败和
覆盖失败都与真实边及BFS一致；混合圈边＋弦、弦＋跨边、两条跨边均有
实际为真的路径。该次小检查CPU0.010175秒、墙钟0.010185秒。

正式准备另以纸面指定的完整八正则赋值检查实际规模。跨边规则为
`j−i mod30∈{0,2,4,6,8,10}`、0≤i<28；右侧弦为
`{(4,28),(5,29),(0,6),(1,7),(2,8),(3,9)}`，这里弦端点用右侧局部标签。
该图符合全部度数和匹配规则，但有**901个坏对、直径5**；完整73701位
赋值在235491条保存CNF子句中恰使901条覆盖子句为假，所有计数与辅助
定义正确。详见 [sanity.json](sanity.json) 的 `explicit_official_assignment`
及 `saved_DIMACS_explicit_assignment_check`。

这份八正则失败图是预先指定的编码检查输入，未固定到搜索CNF，也不是
solver发现的候选；901不能作为搜索质量、进度或接近目标程度。

## 复核与后续边界

第1轮 [Gemini方向回执](../../../../reviews/dd82/20261018_nonuniform58_direction.json)
实际返回SUCCESS／ACCEPT，返回模型字段为 `gemini-3.8-flash-high`、effort
`high`，线程 `07d186a1-44c0-44ed-90e8-d806c61f5032`。该轮接受方向与
既定小检查安排；没有预先认证后来求解结果。
[CODE_REVIEW.md](CODE_REVIEW.md) 为fresh-agent、same-family provisional
PASS，未发现需要修改的源码问题。第2轮[实际交付回执](../../../../reviews/dd82/20261018_nonuniform58_result_review.json)已接受实现、检查、真实UNKNOWN与范围；主代理处置保存在同一运行的002-root-disposition.md。

本次单次profile已完成，不自动加时、换seed、固定弦模板再试或改名重开。
UNKNOWN只说明这一有界调用未作出决定，不能归因为已找到数学矛盾，
也不能据此认定当前结构已无研究价值。可以继续有具体问题的纸面分析，
由新的数学内容和实际证据决定后续动作；预算结束本身不要求强制换路线。

本交付仅核对已保存记录并整理本文，没有启动新的计算，也没有修改共享
wiki、HTML或研究运行状态。

## Substantive paper round3

Same-thread actual SUCCESS/SCOPED ACCEPT in reviews/dd82/20261018_nonuniform58_structural_review.json directly covers ROW_DEFECT_PROPAGATION.md, ZERO_SURPLUS_PATH_OBSTRUCTION.md and RIGHT_SUPPORT_MATCHING_OBSTRUCTION.md. Root accepts the precise paper statements; arbitrary25+3 affine additions are excluded even with both2factors free. This does not exclude the complete free-C family. No new solver, graph, certificate or changed original result. Same construction research remains active at3/4 rounds; the next bounded paper action diagnoses an actual incidence trade, not a parameter ladder.
