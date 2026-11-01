# 新增文献比较表有界审阅

日期：2026-10-21。`review_independence: same-family`；`acceptance_status: provisional`。

## 范围与结论

本次只审阅 `proofs/propertyb-general/LITERATURE_COMPARISON_TABLE.md` 的两张新增总结表及其在 `PROPERTY_B_GENERAL_BOUND.html` 中的展示；不重新审计已验数学证明、Lean或旧paper，不发起其他模型调用。本次是已有结果的总结，不构成新数学证明。

**PASS：内容与最终展示核查通过。** 未发现文献归属、常数、范围、取整或参考包络扩大问题。修前手机两表第一列过窄，已由主代理仅对这两表增加1000px最小宽度和首列150px最小宽度；本审阅者对最终HTML重新执行浏览器检查并目读左右截图，作者名、关系列均正常换行，内部横滚可达，未产生整页横溢。

## 数学与来源核对

实际读取规范新增表、`SOURCE_CHECK.md`、既有 `BASELINE_COMPARISON.md` 的D/D.1/D.2/D.3及比较范围说明，并定点读取本地四篇原PDF：RS作者稿p.7；CK刊页408–410；Pluhár作者稿pp.2–3；GL v3 p.7。另渲染并目读Pluhár p.3以确认符号系数。

- RS全域常数0.1适用于k≥2；RS证明允许任意固定c<1/√2及相应充分大起点，表未错误归功于CK。CK原2^(k−1)归一化下常数c′<√2，换为2^k后c=c′/2正确；未给虚构统一有限起点。
- Pluhár符号系数确为exp(−1/(12k))/(√2·π^(1/4))；未误抄为正的二分之一次幂。准确有向单交对概率β=((k−1)!)²/(2k−1)!与最大严格预算表达一致。
- GL Theorem 1的五项最终数值为32、64、128、263、538，范围k=5,…,9；没有把中途数或固定v=2k+1结果混作一般k全域定理，也没有声称C在不重叠的小k范围逐项更优。
- B_RS明确为本文组合RS Claim A.1与Claim 2.4证明中积分，再定义的最大整数可染预算；没有冒充RS原文同名定理。有限判据严格小于1；可染预算B到m(k)下界B+1、实严格界m>X到floor(X)+1正确。
- B_lin≤B_RS、B_pair≤B_cont≤B_RS的k≥17范围，以及L_GR≤2^k<B_RS+1的k≥32范围均与D.2/D.3一致。L_ref只取明列五项，D/E保留纸面证明状态；没有扩大为所有GL锁点方法或所有已知下界。

## 实际展示与保留核查

独立离线Playwright，桌面1440×1000、手机390×844。两表各为表头加5行，列数分别恒为4和3；每表21公式均有对应SVG。桌面两表均1116px宽、全部列同屏；手机两表均1000px宽，354px容器内部可横滚。表格文字15px，首列与说明列均正常换行。页面总964公式/964SVG，无MathJax错误，无整页横溢。旧902公式用旧浏览器记录的TeX多重集逐项比对，全部保留。四份规范源与新增前source-snapshots逐字相同。

机器记录：`TABLE_AUDIT.json`；可复验脚本：`audit_tables.py`。截图位于 `.aris/traces/render-html/2026-10-21_general-literature-comparison/fresh-{desktop,phone}-literature-table-{1,2}-{left,right}.png`（desktop仅left）。
