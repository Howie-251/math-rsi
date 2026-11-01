# 一般下界图：可验的有限数值展示

`general_data.json` 含全部整数 `k=17,…,64` 的48个点。每点给出一个有理参数 `p` 和严格通过 RS 判据的整数预算 `M_plot`，因此 **`M_plot≤B_RS(k)`**。局部数值优化只用于提出候选；没有证明优化全局性，也没有断言这些整数等于 `B_RS(k)`。

差值主图的蓝色曲线、右侧对数纵轴直接使用 `gain_certified`，表示相对真正RS组合下界 `B_RS+1` 的保证增益下限；图上记为Δ_cert=g_*≤Δ，是保守下限，不是精确Δ。正文定理D证明，对每个k≥17，B_RS+1等于所列五项明确参考界的最大值，所以该曲线也给出超过这一参考包络的保证增益；这里比较的是指定五界，并非全部文献的最佳下界。折叠区绝对值参考图使用以下两条纵坐标：

* 参考基线：`baseline_lower=M_plot+1`。
* 本文定理推出的下界：`improved_lower=M_plot+1+gain_certified`。

其中 `gain_certified=floor(isqrt(M_plot)/(8(1+L_k)))`，`L_k` 为记录中的 `ln_k_upper`，严格包住 `ln(k)` 的上端点。由 `isqrt(M_plot)≤sqrt(M_plot)` 及增长函数的单调性，这一整数不超过定理在真实 `B_RS(k)` 处的增益。它是保守增益，不冒称等于定理中 floor 的精确值。另给 `gain_from_2_to_k`：同样方法只使用已证 `B_RS(k)≥2^k`，展示无需优化的更保守增益。后者使用紧的对数上界，可能优于旧示例用整数对数上界所得的数值。

数据来源是本文规范 `proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md` 的定义B.1、引理B.4及 `proofs/propertyb-general/CLIQUE_REFINEMENT.md` 的定理C；积分的有限多项式在前一文结尾明确给出。主定理及原始超图接口的 Lean 验收见 `context/propertyb-general-lean-growth/REPORT.md`。图点验算没有扩充主定理，也不以48个样点代替一般证明。

## 严格验算

令 `d=2^(k−1)`、`a=1−(1−p)^k`，精确计算

`J=sum((-1)^j*binom(k−1,j)*p^(2j+1)/(2j+1), j=0,…,k−1)`。

全部输入和 `J` 用 Python `Fraction` 有理算术；JSON保留 `p` 与 `J` 的精确分子、分母。接受条件为

`log(Q)−(M/d)log(a)<0`，其中 `Q=M(M−1)J/d²`。

验算器先把有理数以90位 `Decimal` 精度分别向下／向上转换。`Decimal.ln` 按 Python 标准库合同正确舍入到最近数；在其结果两侧各取一个相邻可表示数，包住准确对数。四则运算分别采用 `ROUND_FLOOR`／`ROUND_CEILING`。只有整个对数比值区间的上端点严格小于零才接受。每点存 `log_ratio_lower`、`log_ratio_upper` 和严格正的 `strict_log_margin_lower`。增益计算直接使用 `Fraction(ln_k_upper)` 及整数平方根，以精确有理除法取 floor。

候选求取借用旧 `round02/baseline-comparison/profile.py` 的对数比值及精确积分表达，以75位 mpmath 求一个驻点与阈值，再把 `p` 固定为分母不超过 `10^30` 的有理数；阈值整数只用于提出候选。验算器不依赖驻点是极小值、最优参数唯一、可行集合下闭或数值求根正确。

## 复现与实际结果

生成环境为 Python 3.14.6、已有 `mpmath 1.4.1`；未安装新依赖。实际生成并严格重放48点约0.4秒；系统 Python 的独立证书重放约0.1秒，全部通过。

```sh
.tools/math-python/bin/python context/propertyb-general/bound-figure-20261021/general_data.py
python3 context/propertyb-general/bound-figure-20261021/general_data.py --verify
```

第二条只需标准库，重新计算全部有理积分、区间及增益，并逐字段核对JSON。另用已有 `mpmath.iv` 的80位区间运算、直接从JSON读取有理 `p/J` 独立重算48个RS对数比值，全部区间上端点严格小于零；该交叉验算未参与候选选择。

| k | M_plot | 参考下界 M_plot+1 | 保守新增整数 | 本文推出下界 | 只用2^k的保守新增 |
|---:|---:|---:|---:|---:|---:|
| 17 | 168515 | 168516 | 13 | 168529 | 11 |
| 32 | 7030606389 | 7030606390 | 2346 | 7030608736 | 1834 |
| 64 | 39787796373588582529 | 39787796373588582530 | 152837269 | 39787796373741419799 | 104067276 |

上述三个点的严格对数裕度下界分别约为 `1.3676099660e−5`、`1.5693033056e−10`、`2.8201045649e−20`。全部48点通过，不存在以浮点近似误判为严格通过的点。

绘图提示：`M_plot` 等整数字段在 Python 中精确；后段超过 JavaScript 安全整数范围，浏览器精确提示须由 Python 转为十进制字符串，绘图坐标可单独转 Number。绝对下界宜使用对数纵轴；新增整数另画放大图，才能看清两条绝对曲线间的差距。不能把图中的参考曲线标为已证精确的 `B_RS+1`，推荐“可验 RS 参考下界”及“本文定理推出下界”。
