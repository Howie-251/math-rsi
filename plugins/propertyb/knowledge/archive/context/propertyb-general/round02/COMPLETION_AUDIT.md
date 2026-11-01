# 一般 Property B 下界：最终交付验收

2026-10-21。主代理对照 `GOAL_PROPERTYB_GENERAL_BOUND.md` 全文及第十一节的五项交付要求完成验收。结论：**本一般下界 Goal 的数学与交付要求已经满足，可标记完成。** 本记录不恢复旧 35 Lean 或 36 研究。

## 定理、范围与严格改进

正式规格为项目根 `FORMAL_SPEC_PROPERTYB_GENERAL.md`。对每个整数 k≥17，任意有限简单 k 元超图在边数至多 B_RS(k)+Δ(k) 时可二染，其中

\[
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
\]

B_RS 为规范源明确定义的 RS–FKG–精确积分判据的最大整数预算。证明包括该最大值非空有限、2^k≤B_RS<k2^k、严格参数见证及全范围 Δ≥1。因此 m(k)≥B_RS+Δ+1；顶点数、点对覆盖、度数、共度和线性均不是最终前提。

完整比较尾范围取 K={k≥256}。其中更强的五项明确参考包络比较对全部 k≥32 已成立：L_ref=B_RS+1，新整数下界严格增加 Δ。k≥256 的补充结论还证明指定零锁必要数据松弛不能接受任何 M>B_RS。后者的对象是正文列出的数据测试方案，不宣称松弛见证是实际超图，也不宣称穷尽所有潜在 Grill 方法。精确比较、整数端点及每个更大 M 的覆盖均已写出。

`round02/final-literature/REPORT.md` 与 `round02/baseline-comparison/SOURCES_FINAL.md` 保存原始文献核对和访问范围。没有发现具体遗漏的更强适用公式；未将有界检索误写为世界最优性证明。该增益不提高领先渐近常数。

## 完整证明及实际对象连接

规范源为 `proofs/propertyb-general/` 下 CORE_THEOREM、UNIFORM_INTEGER_GAIN、CLIQUE_REFINEMENT、BASELINE_COMPARISON 四份 MD。数学链完整：任意假定反例 → 最小顶点商与点对覆盖 → 同一实际边族的单交图 → Gram／公共点团界 → 实际有向坏对数 → 同一个重染参数的严格失败概率界 → 原超图两色染色。

核心正式审计 `formal-audit/PROOF_AUDIT.json` 覆盖 18 个源单位、78 项微义务；`BASELINE_ADDENDUM.json` 和 `COMBINED_AUDIT.md/json` 纳入比较源全部十节与最终拼接。结论均 PASS，无未核销数学义务。此处的 proof-checker 是 same-family/provisional 数学审阅，不是 Lean 内核验证。

## 独立复核与指定跨家族终审

辅助程序实际核对 93 个小超图、618304 个重染结果、123 个参数压力例，以及另一实现的 54 个精确离散例和 20 个整数数据例。程序与原输出均保留；这些测试服务于查错，统一定理由解析证明承担。展示增益例子用精确整数／有理数验证，没有声称计算出 B_RS 的实际最优值。复算命令已写入 `HANDOFF_PROPERTYB_GENERAL.md`。

Grok 4.7/xhigh 与 Gemini 4 Argon/high 均完成核心和新旧界比较／最终拼接的有效静态审阅。原回应、范围与主代理处置见 `reviews/CORE_DISPOSITION.md`、`reviews/BASELINE_DISPOSITION.md`。Grok 比较终稿从同次原生 completed 事件回收，原 MCP 回包缺失事实保留；没有将失败或未返回调用计为通过。两家的表述笔误已按原式核查，不写入证明。无待修复数学意见；模型认可不作为证明前提。

## HTML、交接与知识库

`PROPERTY_B_GENERAL_BOUND.html` 内联四份规范证明及全部比较，不需跳出正文读 MD 才能完成论证。532 条公式顺序及非空白 TeX 与阅读源一致；所有公式内嵌 SVG，桌面／手机实际离线检查通过。fresh 展示审阅的唯一公式遗漏已修复并获定向 PASS，最终状态文字更新后的源与 DOM 再次核对通过。证据为 `.aris/traces/render-html/2026-10-21_propertyb-general/REPORT.md` 和 `final-status-check.json`。主代理已查看代表页面，并用 Microsoft Edge 打开最终文件供用户阅读。

`HANDOFF_PROPERTYB_GENERAL.md` 已同步最终状态、四源阅读顺序、精确比较范围、审计入口和可选复算命令。现有 research-wiki 沿用；主 claim `propertyb-general-growing-integer-gain` 已按 proof-checker 证据登记 verified，方法综合、G8、idea、log、index、query_pack 及项目导航均已同步。Goal 工具标记完成后，仅补记最终调度状态。

本轮没有新 Lean 形式化或外部合作者独立复现；它们不是本 Goal 的完成前提。原 m(5)≥33、≥34 成果与旧 35 Lean、36 研究记录保持原状态；没有读写 aris4math_v2。全部五项交付已落实，无额外打包要求或尚在等待的模型调用。
