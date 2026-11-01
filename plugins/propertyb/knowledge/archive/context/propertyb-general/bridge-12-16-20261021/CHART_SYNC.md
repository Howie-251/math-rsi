# 12起统一曲线同步

2026-10-21，图表与 `proofs/propertyb-general/RESULTS_FIGURE.md` 已统一至全部整数 k≥12。主图继续采用用户指定标题“Property B m(k)｜差值主图：下界究竟提高了多少”，所有图内文字为英文；真实线性k横轴、红色左侧线性差值轴、蓝色右侧对数保证增益轴均保留。

同一统一公式的五个新增保证增益为2、3、4、6、9，旧基线为4633、9539、19602、40215、82377，新下界展示4635、9542、19606、40221、82386。它们从 `numeric_bridge.json` 的旧接受预算、向上对数端点和整数平方根派生；`build_bridge_plot_data.py` 重算保守公式并与 `INDEPENDENT_NUMERIC_CHECK.json` 核对，生成独立 `bridge_plot_data.json`。旧48点 `general_data.json` 和小参数来源JSON没有写入。完整曲线因此有53个真实整数样点（12至64）。可选更强C.2增益14、25、45、79、116另链接原 `NUMERIC_REPORT.md`，未混入统一曲线。

主执行者确认已实际核验新增Lean构建和独立原题审计日志后，全部k≥12改用同一实线，并将图例标为“Uniform theorem, k≥12 (Lean)”。图表同步执行者未自行运行Lean，不把数值程序或五项参考包络比较说成Lean结论。小k5–11的候选证明及局部证书状态保留，本轮Grok审阅状态未作完成声明。

## 实际生成与检查

执行：

```sh
.tools/math-python/bin/python context/propertyb-general/bridge-12-16-20261021/build_bridge_plot_data.py
.tools/math-python/bin/python figures/propertyb_bounds/plot_bounds.py
```

两个命令均exit0。生成delta、small、overview、gain四组SVG/PNG/PDF及三页 `propertyb_bounds.pdf`（delta、small、overview）。实际通过 `view_image` 检查delta、overview、gain：12起蓝线、红11标注与首点12无重叠，12与17刻度可读；主图小k次刻度保留5至11。全部实线最终版delta另实际查看，无截断或图例遮挡。

本分工仅读取render-html技能并修改图源，不运行HTML渲染；最终HTML整合与审阅由主执行者负责。
