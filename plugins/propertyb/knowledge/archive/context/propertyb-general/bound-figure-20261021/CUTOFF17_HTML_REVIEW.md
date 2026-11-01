# cutoff17 与增益轴标的限定 HTML 保真审阅

- 日期：2026-10-21
- review_independence: same-family
- acceptance_status: provisional
- 结论：PASS（仅限本次显示与源文保真修订），无发现。

本次只核查五项参考包络起点从32收紧到17，以及随后用户指定的 Property B 横轴与 Δ 增益右轴标识。未重新审查数学正确性、未复算48数值点、未运行Lean，未修改页面或生成器。

实际读取 `proofs/propertyb-general/BASELINE_COMPARISON.md` 的定理D、引理D.2及邻接比较文字，`RESULTS_FIGURE.md` 的差值主图说明，`LITERATURE_COMPARISON_TABLE.md` 的五项参考比较；核对 `PROPERTY_B_GENERAL_BOUND.html` 的文字与 `data-tex` 公式。定理D与D.2、表格、图解范围均为 k≥17；B3/B4、D.2的q/v定义及起点17计算保留。HTML公式属性未发现遗留 k≥32 阈值，32作为数值样点予以保留。

实际用 view_image 查看 `figures/propertyb_bounds/delta.png`，以及 `.aris/traces/render-html/2026-10-21_general-bound-cutoff17/desktop-figure-delta.png`；收到追加轴标要求后，又查看最新 `delta.png` 与 `.aris/traces/render-html/2026-10-21_general-bound-delta-labels/desktop-figure-delta.png`。最终图共用真实线性k横轴，标题为“Property B: hyperedge size k”；红色读左侧线性轴，蓝色读右侧对数轴，右轴明确“Guaranteed lower-bound improvement Δ_cert(k)”。图注给出 Δ_cert(k)=g_*(k)≤Δ(k)，与正文公式一致。17处开始蓝色曲线，图内五界包络注记为k≥17；没有将32标为新阈值，32刻度与≥2,346样点仍在。图内全英文；12…16保持留白；两份最终图片轴标及图注可见，未见裁切。

读取两版 `browser-check.json`；最终依据为 `2026-10-21_general-bound-delta-labels/browser-check.json` 与同目录 `canonical-math-check.json`。主执行者的桌面/手机记录均为1004公式及1004公式SVG，mathInputsMatch与mathInputOrderMatches为true，无缺失公式、数学错误、页面横向溢出、断锚或外部资源；规范公式检查966条，missingSnippets为空。本审阅读取这些实际浏览器记录，并未重新启动浏览器执行相同检查。

## 追加：图前标题的一处文案修改

同日仅追加检查最终标题 `Property B $m(k)$｜差值主图：下界究竟提高了多少`。读取最终HTML标题与 `.aris/traces/render-html/2026-10-21_general-bound-propertyb-title/browser-check.json`、`canonical-math-check.json`，并用 view_image 查看该目录 `desktop-figure-delta.png`：标题实际完整显示，m(k)渲染为数学公式，无裁切。桌面/手机记录均1005公式及1005公式SVG，公式内容与次序匹配、缺失列表为空；规范公式967条全部保留。此增量无发现，保持 same-family/provisional；未重审图或数学。
