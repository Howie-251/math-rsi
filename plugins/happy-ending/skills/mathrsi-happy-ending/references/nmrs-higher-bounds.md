# N(m,r,s) 高阶受限容量、共享标签核与原生迹对偶

本参考整理 [2026-11-17 综合交接包](../../../archive/nmrs-20261117/HANDOFF.md) 从 $m=7$ 扩展到 $m=8,9$ 及一般受限容量族 $N(m,r,s)$ 的可执行方法、证据状态与调用边界。

## 1. 统一记号与三步装配

在完整有序 rank-3 signotope 中，$N(m,r,s)$ 为同时避免蓝 $r$ 点路径、红 $s$ 点路径与同端 weak $m$-gon 的最大点数。记：

$$C_m = N(m,m-1,m-1),\qquad Q_m = N(m,m-1,m),\qquad F_m = N(m,m,m),$$

并以 $D_m$ 表示 R7 不交 H–R 分拆中**带额外交接排斥（junction exclusion）**的双侧残余容量：残余自身避免 weak $m$ 与蓝 $(m-2)$ 路径，且不存在同一点既结束红 $(m-2)$ 路径又开始蓝 $(m-3)$ 路径（因此 $D_m$ 不能直接替换无限制的 $N(m,m-2,m)$）。

对 $m \ge 6$：
1. **R7 分拆：** $Q_m \le C_m + D_m$；
2. **R20 最左 pivot 合法 chart：** $F_m = Q_m + 1$；
3. **几何包含与强迫阈值：** $\mathrm{ES}(m) \le F_m + 1 \le C_m + D_m + 2$。

注意反向推导不成立：不能由公开平面上界 $\mathrm{ES}(8) \le 319$ 直接推出全体抽象 signotope 的 $F_8 \le 318$。

## 2. 七参数新增解析与条件结构（m = 7）

- **Owner 区间解析界 $N(7,5,7) \le 39$：** 基于代表红团、第一端点与五行求和，纯解析排除 40 点层（不依赖 CNF；[owner §7.7](../../../archive/nmrs-20261117/source/reports/n7-owner-intervals-20261116/PROOF.md)）。
- **一般平衡严格容量 $N(2p-3,p,p) \le 2b - 1$（$p \ge 4$）与 $N(7,6,6) \le 49$：** 经实际替末、安全增广与双色端点交替环排除证明（[严格容量证明](../../../archive/nmrs-20261117/source/reports/n766-strict-capacity-20261105/PROOF.md)）。
- **为何单独降 $A,C$ 不自动降 $Q_7 \le 75$：** 现有全局接口只给 $Q_7 \le \min\{3b, C+b+5, A+C-1, \lfloor 9A/4\rfloor, \lfloor 9C/5\rfloor\} = 75$，推进 $Q_7 \le 74$ 必须转向同一母体上的总物理横截费用 $\tau_{R_6}(X)$。
- **共同锁块上限与真中性流（2026-11-17）：** 五份有序五点红锁块的精确必要 CNF 经 DRAT 核验 UNSAT（`lock-blocks/q5`），故规范正反非 through 锁或 R7 同一共同匹配中的块型边合并至多 **4 块**（另有 20 点四块合法染色说明纯投影上限恰为 4）；74 点反设被迫含至少 5 个 clean 根并进入同一全局端口最大流。无条件 $N(7,6,7) \le 74$ 仍开放。

## 3. 八参数：九洞共享标签证书与八边形迁移（m = 8）

- **可重放九洞封包 $N(8,6,6) \le 61$（`milestone9`）：** 在 $4 \times 4$ 盒 $\binom{8}{4} = 70$ 个状态上，63 条六阶单调盒链 + 30 条共享最紧 `[1,4]` pivot 行给出 93 条基线行（迫 $\ge 8$ 洞，$\le 62$）；再对共享末对标签与局部 signotope packet 运行 CEGAR，抽出 **11 个不可满足核**（连同转置共增 22 行，总计 **115 条必要行**），顺序计数器 budget-8 CNF+DRAT 核验 UNSAT，迫至少 **9 洞**，即 $N(8,6,6) \le 61$。配套 9 洞向量 `[4, 27, 29, 32, 37, 40, 42, 61, 65]` 击中全部 115 行，证明该 115 行矩阵精确最小值为 9（**它是矩阵 hitting 见证，不是 61 点 signotope 构造**）。
- **解析传递子界：** 结合 $N(8,4,8) = 22$（Baek）与坐标擦除切片计数，工作稿给出 $N(8,5,7) \le 51$、$N(8,5,8) \le 66$、$N(8,6,7) \le 109$、$N(8,6,8) \le 165$。
- **八边形 signotope 迁移与平面边界：** 重放 Schroeder 公开 15 文件有限遗漏树算术（`check_octagon_omission.py`，`PASS`）结合本项目抽象循环符号 packet 桥（[EIGHT-CYCLE-TRANSFER.md](../../../archive/nmrs-20261117/source/reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)，待独立审阅），得到抽象 signotope 工作界 $C_8 \le 193, D_8 \le 124 \implies Q_8 \le 317, F_8 = N(8,8,8) \le 318$。**平面 $\mathrm{ES}(8) \le 319$ 本身已是 Schroeder 公开预印本定理，不认领为新平面降界**；不调用公开遗漏树的自主九洞 + 解析备用链为 $195 / 126 / 321 / 322 \implies \mathrm{ES}(8) \le 323$。

## 4. 九参数：原生边界迹稀疏整数对偶与平面推论（m = 9）

- **参数化原生边界迹行：** 在 $a \times b$ 子盒（固定包含集 `inc` 与排除集 `exc`，深度 $|\text{inc}|+|\text{exc}| \le d$）中，由递减 $(q_1,\dots,q_{a-1})$ 与 $p_i \in \{q_i, q_i+1\}$ 确定起点 $S$ 与终点 $E$。列链与高链给出 $a+b$ 个状态；在禁 8 点单色路与同端 weak 9 下，任意被占子集产生顶点数为 $|\text{occ}|+2$ 的同端蓝红路对，故至多占 8 态，每条迹在允许状态集上至少缺 $a + b - 8 - \text{forbidden}$ 个洞。
- **自包含整数对偶证书（零浮点消费）：** 对整数行权 $w_r > 0$ 与尺度 $\Lambda = 10^6$，记总需求 $D = \sum w_r d_r$、状态负载 $\ell_W = \sum_{W \in r} w_r$ 及 $\{0,1\}$ 过载惩罚 $P = \sum_W \max(0, \ell_W - \Lambda)$，由 $h_W \in \{0,1\}$ 直接得 $\sum h_W \ge \lceil (D - P)/\Lambda \rceil$：
  1. `run-988-d2/compact-certificate.json`：924 状态、883 条正权行，$D - P = 235{,}971{,}673 > 235 \times 10^6 \implies \ge 236$ 洞，即 **$C_9 = N(9,8,8) \le 688$**（不调用任何 $977 \le 222$ 或八参数公开环进口）。
  2. `run-d9-d3/compact-certificate.json`：582 允许状态、532 条正权行，$D - P = 123{,}539{,}361 > 123 \times 10^6 \implies \ge 124$ 洞，即带交接排斥的 **$D_9 \le 458$**。同时 `fractional-grid.json` 在全部 **47,635** 条深度 $\le 3$ 生成行上给出最小行余量 3、总和 $123{,}539{,}833 / 10^6 \le 124$ 的精确有理可行解，证明该深度 $\le 3$ 原生迹 LP 的整数上限恰好封顶于 124。
- **工作推论装配：** 经 R7 与 R20 装配（整条纸面桥仍待独立审阅），得到 **$Q_9 = N(9,8,9) \le 1146$**、**$F_9 = N(9,9,9) \le 1147$** 及平面强迫工作推论 **$\mathrm{ES}(9) \le 1148$**（对比 Mojarrad–Vlachos 2016 文献值 $1508$，以及按公开平面方法折算的组合参考值 $924 + 575 + 2 = 1501^*$）。解析子表另给 $N(9,5,8)\le 78, N(9,5,9)\le 96, N(9,6,7)\le 117, N(9,6,8)\le 185, N(9,6,9)\le 264, N(9,7,7)\le 222, N(9,7,8)\le 380, N(9,7,9)\le 633$（基座 $N(9,4,9)=29$ Baek）。

## 5. 一般 m 受限容量族

坐标擦除阈值 chart 保持诱导三元颜色与禁止路径，支持在同一母体上对一阶/二阶包含-排除切片做双计数：
- **严格平衡容量：** $N(2p-3,p,p) \le 2 N(2p-3,p-1,p) - 1$（$p \ge 4$）；
- **三列二次缺额：** $N(m,5,m-1)$ 相对二项式目录具有 $\sim n^2 / 12$ 量级的二次缺洞下界（[THREE-COLUMN-STRICT.md](../../../archive/nmrs-20261117/source/reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)）；
- **四列三次缺额：** $N(m,6,m-2)$ 具有 $\sim n^3 / 80$ 量级的三次缺洞下界（[STRICT-FAMILY4.md](../../../archive/nmrs-20261117/source/reports/n79-overlap-20261116/STRICT-FAMILY4.md)、[LARGER-PARAMETER-BOUNDS.md](../../../archive/nmrs-20261117/source/reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)）。

以上一般 $m$ 结论均为待独立审阅的工作证明，不认领 $m \ge 10$ 的统一显式 $\mathrm{ES}(m)$ 闭合上界。
