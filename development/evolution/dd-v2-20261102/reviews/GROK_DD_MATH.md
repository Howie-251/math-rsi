D4 同源覆盖还没有接到原简单图上；diagonal 有一句把非 D2 见证读反了。冻结完整邻域、GQ 计数、Mizuno dual 算术和 106→107 的 UNKNOWN 范围可以保留。本轮没有运行命令、Lean 或 BFS，也没有重算 dual。

## 要改的两处

**1. `construction-mathematics.md` §5 的 D4 段把 fiber 覆盖写成了图覆盖。**

代数本身与 `GLOBAL_COSET4_NOTE.md` 一致：`im(M_w−M_r)⊆H_w` 时，像是 reference 中心加固定 coset `(c_w−c_r)+H_w`，不要求每条满秩。原文接着限定了 reference、覆盖了哪些控制器对，以及怎样才成为 `SimpleGraph` 的 walk。这段都没写。

原文的界限是：reference 只能是从 a 到同一控制器 b、长度 ≤2 的实际 word，不能换成任意矩阵；97 组里 6 组首个 reference 失败且保持失败，91 组只盖住原先缺失的 3648 对，另外 33216 对各自沿用 rank-4 word。仿射路线给出长度 ≤4 的状态序列之后，只删除连续相同的完整 global label（virtual stay）。同一控制器、不同 local fiber，或同一 local state、不同控制器，仍是原图上的边。对所有 x 的 fiber 命中不给出点数、度数或非 D3，也不是后继 Lean 里那条 walk 定理。`lean-and-representation.md` 只说 coset 加保 port 对称后来闭合了源 walk，没有写下这条删除规则。

§5 该段改成：

> 只对源 15552 的有序控制器对 (a,b)。reference 必须是从 a 到 b、长度 ≤2 的实际 word。若每条参与路线满足 `im(M_w−M_r)⊆H_w`，像等于 reference 中心加 `(c_w−c_r)+H_w`，与 x 无关；不要求 H_w 满秩。本源常数 c 为 0，准则仍保留 offset。97 组中 6 组失败且保持失败；91 组只覆盖 3648 对，33216 对沿用 rank-4 word。状态序列只删除连续相同的完整 global label；同控制器不同 fiber、同 local state 不同控制器都保留为边。这里是 fiber 证书到原简单图的桥，不给阶、度或非 D3。

`dd-construction` 展开执行 B 已写 91 组成功、6 个 reference 失败，并说明只有空间计数不能交图证明。在“构造真实 walk”那句后加同一条删除规则即可。不要据此重开 91 组或新 Lean。

**2. `construction-mathematics.md` §7 把非 D2 见证写成了否定。**

现句是“p>0 时两者不交给非 D2 见证”。`DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md` 的结论相反：hub 的邻域在 fillers，clone 的邻域在 U，p>0 时二者不相邻且无公共邻点，距离恰为 3。

该句改为：p>0 时 hub 与任一 clone 不相邻、无公共邻点，距离恰为 3，这是非 D2 见证。s,t≥2 时另有一对源距恰为 3 的 U 点保持距离 3，因为 |U|>δ²+1，clone 和 hub 都不把它收成 2 步。前缀直径按插入时已经存在的路写，不从终图删点倒推。

阶、边、度分布、q8 的 G1=346516 与 pR+1=4226、hub 不能塌到旧 H 点、k>1 是在 G1 上克隆首块 pR 个 clone 加首个 hub，这些与原文一致，不动。

## 核对后保留

冻结完整邻域 §3 与 `FullNeighborhoodClones.lean` 一致：无孤立点、D≥3、新点只连开邻域、无 new-new、旧边保留。旧点度数加的是邻接对应中心的重数，新点度数等于中心度数。中心允许相邻或重复；q4 的 136 条 K2 加 17 个孤立点是中心诱导子图里的结构。旧距离由塌缩同态保持。“原图非 D2 则新图非 D2”是直径上界对 D=2 的情形。容量 `|I|≤floor(k|V|/δ)` 只属于正则 full-N、无 new-new。

§6 的 R、δ、H 的阶 `δR²+R`、q4 的 7242+289=7531，与 ovoid 证明一致。N_H 不交的结论成立：U 上的唯一性之外，每个 ovoid 点占用一条 spread line 的那个 filler，17 个 bonus 互不相同。名字 GQ 不代替 labels 和 projection，页内已经写了。§6 的阶是完整邻域克隆；diagonal 另加 hub，k=1 时是 7532。两节没有混。

`replay_mizuno_dual.py` 核对的是重建行与 `SIMPLIFIED_DUAL_CERTIFICATE.json` 的整数组合：364 行由 MODEL 的稀疏系数重建，行列和为 5，每行非零重数是 {1,1,1,2}，成本 203 个 5 与 161 个 6，右端 1092，Y 有 365 个、Z 有 364 个且非负，列组合等于证书分子，最小值 ≥10000，RHS=2061908<207×10000，因而整数 T≤206。保存的 `evidence/MIZUNO_DUAL_REPLAY.json` 就是这组字段。系数 2 是否落在 `M_mate`、行的几何必要性、5562 与 94014 都不由脚本计算；后两个是 206×27 和 88452+5562，由证明页在“每块 27 点”下解释。例子和 obstructions §8 已把算术、几何和一般 N(14,5) 分开。MODEL 把 P-load 与 affine normal/phase 标成放松；放松模型的上界仍排除更紧的可行集，页内也没有声称这两族约束被执行。不必加第二个验证器，也不要把缺失的 `LP_INPUT.json` 写回 archive。

obstructions §7 把 10 秒 HiGHS 无 incumbent 留在 UNKNOWN，并写明 C7-invariant 与 10976 个 one-departure 形状都不关闭一般 internal-S。这个范围没有收得过宽。

三名 Sol 继续。本轮不给数学真值分数，不改 `EVOLUTION.md`。
