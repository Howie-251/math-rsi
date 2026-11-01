# 最新数值程序的便携复算

从解压目录运行下面的入口；保留包内目录层级。它先将原始 Python 源码和 JSON 输入逐字复制到独立输出目录的 `work/`，再以该副本为工作目录运行程序。所有结果、日志及 `RUN_REPORT.json` 都写入该输出目录；收到的原证书不被覆盖。无需修改原机路径：本入口使用的程序以自身路径或副本工作目录定位依赖，没有改写数学、ROOT 或导入表达式。

```sh
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --list
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --case all
```

默认 `all` 运行 `m6,m7,m8,m9,m12` 五项独核。默认输出为解压根目录的 `reproduction-runs/<时间戳>/`。可只选部分，并指定一个尚不存在的输出目录：

```sh
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --case m7,m8,m9 --output /tmp/propertyb-check
```

程序逐条保留原断言；任一子程序非零退出即停止。请勿用 `python -O`。每次使用新的输出目录，以便保留上次结果。`RUN_REPORT.json` 记录实际命令、退出码、子进程CPU／墙钟及日志文件。输出目录会包含一份输入副本，完成后可自行删除整个输出目录。

| 模式 | 实际复核范围 | 依赖 |
|---|---|---|
|`m6`|M66全部实际使用算术分支：小点数与零锁、31–33、34全部最小度、35全部最小度、36–38、39、40–41、42–44尾83型。十条程序的具体次序在脚本中。结构论证仍须结合正文。|Python标准库|
|`m7`|全部424局部型、完整参数域及共同坏对整数向量；下降阶乘／Fraction实现。|Python标准库|
|`m8`|全部2094局部型、完整参数域；递归DP另核299组组件配额。|Python标准库|
|`m9`|全部3450局部型、完整参数域与决策树。|Python标准库|
|`m12`|692个点数的完整参数域、全部迹重数／度数／共度，20个紧型／端点Fraction重放。**不是664355型的第二概率实现全算。**|Python标准库|

运行环境为 Python≥3.10 的 macOS 或 Linux。原程序及本入口使用 Unix `resource`，六元部分使用 `signal.setitimer`；本次未在原生Windows验证。不需要原作者虚拟环境、`.tools/`、ARIS helper、Lean、浏览器或网络。最新五项独核不需要 NumPy、SciPy 或 mpmath。

作者最终生成器也可在副本中运行：

```sh
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --case m7-author,m8-author,m9-author
# 以下另需安装 NumPy；约70CPU秒是已有本机实测，非耗时保证。
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --case m12-author
```

前三项重生成最终证书，仍使用归档的先行输入／布局；不重新做布局搜索。十二元模式调用既有 `repro/conditional.py`、`tail.py`、`summarize.py`、`compare.py`，固定693／694切点，完整重算原实现的664355型并比较原数学行。它是作者原实现的重跑；即使与原证书完全相等，也不会扩大第二实现的20型概率范围。六元作者生成过程由多个历史生成器组成，本入口直接提供完整实际使用域的独核，不另发起探索生成器。

依赖分布为：七／八／九元作者生成器需 `propertyB_small_k/` 中的原概率核；六元独核需最新进展目录、此前66证明的注入核、诊断目录的尾83型程序及原六元概率核。十二元作者完整重跑需 `context/collaborator-small-k-20261019/m10-m11/` 内已解包的 `verified`、`certified`、`fast_exact_triple` 等模块，保持原层级即可。`portability_paths.json` 列出入口各模式所复制的实际源码／输入以及本次便携检查日志，可供打包者机械核对。

2026-10-30的实际便携检查见 `PORTABILITY_CHECKS.json` 和 `scripts/validation/`：全部22条子命令exit0；五项独核合计约87.9CPU秒，7／8／9作者生成器约18.9CPU秒，十二元作者全表及比较约81.8CPU秒，总计188.5CPU秒。十二元新全表重跑与归档数学行完全相等；这仍是原实现重跑。日志和运行报告随包，庞大的临时 `work/` 树不入包。这是同一Mac上在 `/private/tmp/` 独立工作副本执行，不能称为第二台机器复现；没有新数学验收、Lean构建或研究恢复。
