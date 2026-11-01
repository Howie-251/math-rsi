# 下界比较图的生成与证据

图的阅读来源是 `proofs/propertyb-general/RESULTS_FIGURE.md`。它由现有生成器内联进 `PROPERTY_B_GENERAL_BOUND.html`；四份核心证明源和已有 Lean 结果保持原状。

首图 delta 为全英文单图，共用真实线性k横轴：红色小参数读左线性纵轴（Δsmall=Lnew−Lprior），蓝色一般结果读右对数纵轴（保守保证增益Δ_cert=g_*≤Δ，相对B_RS+1），12…16留白。对每个k≥17，B_RS+1等于正文五项明确参考界的最大值，蓝线给出超过该包络的保证增益；主图及辅助图均不再设置k=32比较阈值，32仅保留为刻度与数值示例。全部图横轴标出Property B与超边大小k，主图右轴明确标出Δ_cert；图内颜色、轴标题和刻度明确对应；5…10补次刻度。small 保留原始整数标注与2^k归一化；overview 的绝对下界总量移入折叠区。三页PDF依次为delta、small、overview；原gain独立导出保留，但HTML不重复展示。小参数本次使用 m(5)≥35，保留纸面候选与完整 Lean 未闭合的状态。k=6…11保留合作者归属与验收范围。数据只比较指定文献及公式，不称当前世界纪录。

## 复现

在项目根目录依次运行：

```sh
python3 context/propertyb-general/bound-figure-20261021/general_data.py --verify
.tools/math-python/bin/python figures/propertyb_bounds/plot_bounds.py
export ARIS_REPO=/Users/rfy_naiveai/Desktop/aris_main
python3 context/rendering/render_propertyb_general.py --trace-dir .aris/traces/render-html/2026-10-21_general-bound-english-dual
```

小参数来源和两条新代入的精确分数见 `SMALL_K_SOURCES.md` / `small_k_sources.json`；一般段48点的有理见证与严格区间见 `GENERAL_DATA.md` / `general_data.json`。一般数据生成依赖原有 mpmath，重放仅用 Python 标准库；绘图使用项目 `.tools/math-python` 中的 Matplotlib 3.11.2。图按矢量 SVG 和 PDF 导出，PNG用于检查；三张 SVG 以内嵌图像形式驻留单个 HTML，阅读不依赖联网。

本次新增数值仅为已证明判据及定理的展示，不以有限采样替代统一证明，没有恢复旧35 Lean／36研究。
