# 62 顶点、最大度 8、直径 2：SAT 结果与新理论的联合状态

日期：2026-08-24

## 0. 一句话结论

目前尚未证明或否定 62 顶点候选图的存在性。旧 SAT 计算在 12 个穷尽的
无三角形根模板中关闭了 8 个，剩余 4 个；新理论把全局问题重新压缩为 7 个
有证明覆盖性的 `A+B` 模板，其中 5 个双重边模板与旧 SAT 已关闭的
`02--04` 模板完全对应，真正需要继续攻击的是两个 simple-`B` 模板
`S_TOUCH` 和 `S_DISJOINT`。

必须区分：

- `PROVED`：有书面数学推导，相关有限分类脚本已复现；尚未经过外部专家或
  proof assistant 认证。
- `RAW_UNSAT`：SAT solver 返回退出码 20 和 `s UNSATISFIABLE`，但未生成
  DRAT/LRAT/FRAT 证明轨迹。
- `OPEN`：既无通过验证的 SAT 图，也无完整 UNSAT 结论。

因此，下面 8 个分支可以称为“solver-level closed”，但除 `01` 现在还被
新三重边定理独立排除外，不能称为已经独立认证的计算机证明。

## 1. 问题与旧 SAT 的穷尽根化

目标是判定是否存在简单图 `G` 满足

\[
|V(G)|=62,\qquad \Delta(G)\le 8,\qquad \operatorname{diam}(G)\le2.
\]

任一候选图必为 8-正则图。每个顶点至多位于一个三角形中，而 62 不能被 3
整除，因此至少存在一个不在三角形中的根 `r`。固定

\[
N(r)=X=\{1,\ldots,8\},\qquad
Y=V(G)\setminus(\{r\}\cup X),\quad |Y|=53.
\]

因为 `r` 不在三角形中，`X` 是独立集。对 \(y\in Y\) 定义
\(P(y)=N(y)\cap X\)，则

\[
\sum_{y\in Y}(|P(y)|-1)=3.
\]

把三个单位的 excess 按 `S_8` 重标号分类，恰好得到 12 个根模板：一个
四父点模板、三个“一个三父点加一个二父点”模板，以及八个“三个二父点”
模板。这是旧 SAT 计算宣称的全局覆盖基础。

旧 CNF 只把 `Y` 内的 1,378 条潜在边作为图边主变量，并加入：

1. 每个 `Y` 顶点的精确剩余度；
2. 每个未被根层覆盖的 `X--Y` 或 `Y--Y` 点对必须相邻或拥有公共邻居；
3. 根层 defect 推出的 fiber-cap 和 saturated-fiber cuts；
4. 同一单父类内按异常点邻接签名排序的安全重标号消对称。

辅助变量包括度数二进制计数器、carry 和公共邻居 witness。编码版本为
`n62_root_v1_saturated_signature_20260815`。

## 2. 8 个已经返回 RAW_UNSAT 的根模板

表中父集使用根邻点的 1-based 标号。`Singleton sizes` 是八个单父类
`C_1,...,C_8` 的大小。时间为首先返回 UNSAT 的 solver 的实际墙钟时间。

| ID | 异常父集 / 结构 | Singleton sizes | Vars | Clauses | 首个 UNSAT solver | Wall time | 状态 |
|---|---|---:|---:|---:|---|---:|---|
| `01_four_parent` | 一个四父点 `1234` | `(6,6,6,6,7,7,7,7)` | 93,404 | 237,012 | 837 leaves: AE-Kissat; 1 leaf: CaDiCaL | final queue 71.871 s | 838/838 RAW_UNSAT |
| `02_triple_pair_i0` | `123` 与不交 pair `45` | `(6,6,6,6,6,7,7,7)` | 93,404 | 233,005 | AE-Kissat 2025 MAB | 1,852.332 s (30m52s) | RAW_UNSAT |
| `03_triple_pair_i1` | `123` 与交 1 点 pair `34` | `(6,6,5,6,7,7,7,7)` | 93,404 | 233,971 | AE-Kissat 2025 MAB | 3,741.837 s (1h02m22s) | RAW_UNSAT |
| `04_triple_pair_i2` | `123` 与交 2 点 pair `12` | `(5,5,6,7,7,7,7,7)` | 93,455 | 235,040 | AE-Kissat 2025 MAB | 2,560.216 s (42m40s) | RAW_UNSAT |
| `05_three_parallel_pairs` | `12,12,12` | `(4,4,7,7,7,7,7,7)` | 93,557 | 236,353 | CaDiCaL SC2025, seed 104729 | 44,067.272 s (12h14m27s) | RAW_UNSAT |
| `06_double_pair_pendant` | `12,12,13` | `(4,5,6,7,7,7,7,7)` | 93,455 | 235,181 | CaDiCaL SC2025, seed 104729 | 147,270.942 s (40h54m31s) | RAW_UNSAT |
| `07_double_pair_disjoint` | `12,12,34` | `(5,5,6,6,7,7,7,7)` | 93,455 | 234,215 | AE-Kissat 2025 MAB | 119,327.817 s (33h08m48s) | RAW_UNSAT |
| `12_three_disjoint_pairs` | `12,34,56` | `(6,6,6,6,6,6,7,7)` | 93,404 | 234,490 | CaDiCaL SC2025, seed 104729 | 114,132.180 s (31h42m12s) | RAW_UNSAT |

### 2.1 `01_four_parent` 的细分情况

基础 CNF 为 93,404 变量、237,012 子句。旧运行把最终 manifest 设计为
838 个互斥且穷尽的叶：

- 793 个顶层 `M` cubes；
- 困难的 cube 737 被依次按 `e`、`q`、skeleton 和 `x1` 继续细分；
- 最终形成另外 45 个 materialized CNF leaves；
- 838 个叶全部返回退出码 20；SAT=0、TIMEOUT=0、ERROR=0；
- 837 个叶由 AE-Kissat 2025 MAB 关闭，最慢的一个叶由 CaDiCaL 关闭；
- 所有叶 solver wall time 合计 673.362 秒，最慢叶 71.863 秒；52-worker 最终
  queue wall time 为 71.871 秒。

这组数字仅表示最后一次完整叶队列验证，不包含此前发现和生成细分结构的总人工
及计算时间。当前目录保存了 794 个顶层 `M` 记录和最终 838 叶 manifest；本次
审计用独立临时枚举确认：这 794 个矩阵恰好是满足行列和均为 6、对角元至多
为 1 的非负整数 `4 x 4` 矩阵在同步 `S_4` 行列置换下的全部轨道。但项目内
没有保留从头生成这 794 个 `M` 记录的源脚本，后续 45 个深层 CNF 的生成和
覆盖审计脚本也未找到。因此专家复核时仍应把完整分区的可重建性列为补件项目。

新理论给了一个不依赖这 838 个 SAT 结果的排除：四父点 `y` 满足
`B_{ry}=3`，而新的三重边引理证明所有 `B_ij<=2`。因此 `01` 目前同时具有
理论排除和旧 RAW_UNSAT 两条证据链。

### 2.2 其余 7 个单体 CNF 的运行方式

统一 72 小时运行从 2026-08-15 17:04:31 UTC 到 2026-08-18
17:04:31 UTC。11 个模板各运行一个五配置 portfolio：AE-Kissat 以及四个
CaDiCaL 配置。某配置首先返回退出码 20 后，同模板其他配置被停止。上表时间是
winner 时间，而不是五配置 CPU 时间之和。

结果文件记录了 solver 路径、配置、退出码和时间；winner 日志只保留了
`s UNSATISFIABLE` 或普通 solver 输出，没有 proof trace。

检查点进展为：24 小时时关闭 `01--05` 共 5/12；48 小时时再关闭
`06,07,12`，达到 8/12；72 小时时仍为 8/12。整个统一运行记录的 solver
CPU 采样约为 2,034.34 core-hours；这只是资源账，不代表搜索空间完成比例。
同样，模板数 8/12 也不能解释为已经搜索了组合空间的三分之二。

## 3. 旧 SAT 尚未关闭的部分

以下 4 个模板在统一 72 小时预算到达时仍为 TIMEOUT：

| ID | 三个二父集形成的图 | Vars | Clauses | 旧 monolithic 状态 |
|---|---|---:|---:|---|
| `08_triangle_pairs` | `K_3` | 93,404 | 233,923 | TIMEOUT |
| `09_star_pairs` | `K_{1,3}` | 93,404 | 235,267 | TIMEOUT |
| `10_path4_pairs` | `P_4` | 93,404 | 234,112 | TIMEOUT |
| `11_path3_plus_pair` | `P_3 \sqcup K_2` | 93,404 | 234,301 | TIMEOUT |

后续 12 小时 semantic-cubing 实验共运行 4,029 个子任务：

| Template | Tasks | RAW_UNSAT tasks | UNKNOWN tasks | 完整 source leaves 关闭数 |
|---|---:|---:|---:|---:|
| `08_triangle_pairs` | 732 | 0 | 732 | 0/12 |
| `09_star_pairs` | 64 | 40 | 24 | 0/1 |
| `10_path4_pairs` | 2,440 | 90 | 2,350 | 0/40 |
| `11_path3_plus_pair` | 793 | 26 | 767 | 0/13 |
| **Total** | **4,029** | **156** | **3,873** | **0/66** |

因此 156 个 UNSAT 子任务是真实的局部排除，但没有关闭任何完整 source leaf，
不能把它们计为额外关闭一个根模板，也不能宣称旧四类已部分完成某个可定义百分比。

## 4. 2026-08-24 新理论进展

以下是交接文档中标为 `PROVED`、并已重新运行配套有限检查脚本的主要结论。

### 4.1 重复矩阵

对候选邻接矩阵 `A` 定义

\[
B=A^2+A-7I-J.
\]

则 `B` 是对称、非负整数、零对角矩阵，并满足

\[
B\mathbf1=3\mathbf1,\qquad AB=BA,
\]

以及对不同顶点

\[
|N(i)\cap N(j)|+A_{ij}=1+B_{ij}.
\]

### 4.2 三角形与三重边

若 `t(v)` 是经过 `v` 的三角形数，则

\[
\sum_{u\sim_Gv}B_{vu}=2t(v).
\]

由 `B` 行和 3 得到每个顶点至多属于一个三角形。进一步的理论推导及有限
整数矩阵/GF(2) 检查排除了 `B` 的三重边：

\[
\boxed{B_{ij}\le2}.
\]

所以每行只有 `2+1` 或 `1+1+1` 两种类型。

### 4.3 四边形奇偶性

令 `d` 为 `B` 的双重边数，`T` 为 `G` 的三角形数，则

\[
\boxed{d-T\equiv1\pmod2}.
\]

若 `B` 没有双重边，则 `B` 是简单三次图并且

\[
\boxed{T\text{ 为奇数}}.
\]

这保证 simple-`B` 情形可以选择一个位于三角形上的根。

### 4.4 从 12 个旧模板压缩为 7 个新模板

新理论按 `B` 是否含双重边分为两类：

1. 若含双重边，选择双重边端点为根，根型必为 `[3,2]`；交集大小为
   0、1、2，交 0 的情形再分成 3 个局部轨道，共 5 个 `D*` 实例。
2. 若不含双重边，`B` 简单且 `T` 为奇数；选择三角形顶点为根，只剩
   `S_TOUCH` 与 `S_DISJOINT` 两个轨道。

七个模板为：

| 新 ID | 根结构 | 与旧模板的关系 |
|---|---|---|
| `D0_MATCH` | `P(9)=123,P(10)=45`, `9-10` 非边 | 与下面两个一起穷尽旧 `02` |
| `D0_EDGE_BIN` | 同上，`9-10` 为边且重复点在 `P(10)` 内 | 与另两个一起穷尽旧 `02` |
| `D0_EDGE_BOUT` | 同上，`9-10` 为边且重复点在 `P(10)` 外 | 与另两个一起穷尽旧 `02` |
| `D1_MATCH` | `P(9)=123,P(10)=14` | 对应旧 `03` |
| `D2_MATCH` | `P(9)=123,P(10)=12` | 对应旧 `04` |
| `S_TOUCH` | 根三角形 `0-1-2`，`P(9)=13` | simple-`B` 的一个全局轨道 |
| `S_DISJOINT` | 根三角形 `0-1-2`，`P(9)=34` | simple-`B` 的另一个全局轨道 |

七模板 JSON 已由生成脚本重新生成并逐字段比对；交集轨道和稳定子群轨道计数
均与 handoff 输出一致。

## 5. 旧 SAT 与新理论合并后能说什么

### 5.1 可以说的最强条件结论

在接受旧 CNF 等价性、分支覆盖以及 solver 退出码 20 的前提下，若 62 点候选图
仍然存在，则：

1. `B` 不含双重边；否则选择双重边端点为根，必落入旧 `02--04`，而这三类
   已 RAW_UNSAT。
2. 因而 `B` 必须是 62 顶点的简单三次图。
3. `G` 的三角形总数 `T` 必须为奇数。
4. 对任何用于旧分类的无三角形根，三个二父集不能形成三平行边、双边加邻边、
   双边加不交边或三条不交边，因为旧 `05,06,07,12` 已 RAW_UNSAT。
5. 所以尚存的无三角形根形状只有

   \[
   \boxed{K_3,\quad K_{1,3},\quad P_4,\quad P_3\sqcup K_2}.
   \]

6. 换用新理论保证存在的三角形根，候选图必须落入

   \[
   \boxed{S_TOUCH\quad\text{或}\quad S_DISJOINT}.
   \]

这是当前最清楚的搜索空间描述，但其中第 1、4 步仍依赖未带证明轨迹的 SAT
输出，故应称为“基于当前计算证据的条件结构定理”。

### 5.2 理论没有替代掉哪些 SAT 结果

- 三重边引理直接替代了旧 `01_four_parent` 的 SAT 排除。
- 新理论没有单独证明旧 `02--07,12` 不可能；这些分支的不可能性目前仍来自
  RAW_UNSAT。
- 七模板定理是完整的重新参数化，不是七个模板的 UNSAT 证明。
- `S_TOUCH/S_DISJOINT` 会在不同根坐标下覆盖旧模板中仍可能属于 simple-`B`
  的搜索空间，不能把
  旧 156 个 semantic UNSAT cubes 直接翻译成新模板的 clauses；需要显式的
  re-rooting/isomorphism 映射才能安全复用。

## 6. 已实现的新 `A+B` SAT 前端

新前端没有从裸 62 点图开始。它读取七模板 JSON，只保留 1,378 个 `Y--Y`
图边主变量，并显式编码：

\[
f_{uv}+q_{uv}+A_{uv}=1+b1_{uv}+2b2_{uv},
\]

`B` 行和 3、`B<=2`、精确度数、三角形成员变量、simple-`B` 奇偶性和双重边
局部计数。七个基础实例的实际规模为：

| ID | Vars | Clauses |
|---|---:|---:|
| `D0_MATCH` | 428,657 | 1,568,402 |
| `D0_EDGE_BIN` | 428,652 | 1,568,384 |
| `D0_EDGE_BOUT` | 428,652 | 1,568,383 |
| `D1_MATCH` | 428,657 | 1,568,399 |
| `D2_MATCH` | 428,657 | 1,568,393 |
| `S_TOUCH` | 399,108 | 1,448,815 |
| `S_DISJOINT` | 399,110 | 1,448,824 |

生成器把每个基础实例做 3 层二叉分裂，形成 `7 x 8=56` 个语法上穷尽的叶。
DIMACS header/实际子句数、变量映射、计数器原语和独立 SAT 模型验证器均已做
本地检查。当前只做过秒级 pipeline smoke test，尚无新的完整模板 UNSAT。

## 7. 当前尚缺的关键环节

1. `S_TOUCH` 与 `S_DISJOINT` 尚未得到 SAT 或 UNSAT 结果；这是当前核心开放项。
2. 旧 7 个单体 RAW_UNSAT 没有 proof trace，需要 proof-producing solver 重跑并
   由 checker 验证，才能成为证书级计算结果。
3. 旧 `01` 的 838 叶虽全部 UNSAT，且顶层 794 个 `M` 轨道已被临时独立枚举
   复核，但生成脚本和后续 45 个深层分支的覆盖审计脚本仍需补齐；不过新三重边
   定理若经专家接受，已使这条旧计算链不再必要。
4. 新理论的三重边排除是最重要的新数学环节，专家应优先检查五胞腔划分、
   8 点块三类型归约以及最终 GF(2) 矛盾是否存在隐藏假设。
5. 新 `A+B` 编码目前没有显式加入 `B`-分量商矩阵分类；`AB=BA` 则由完整
   `B=A^2+A-7I-J` 等式和正则性自动推出，不需要作为额外正确性条件。

## 8. 主要本地证据位置

- 旧 12 模板生成器：`degree_diameter_sat/n62_all_templates_cnf.py`
- 旧四父模板生成器：`degree_diameter_sat/n62_four_parent_cnf.py`
- 旧 72 小时总结果：`degree_diameter_sat/results/n62_all_templates/summary.json`
- 旧各模板结果：`degree_diameter_sat/results/n62_all_templates/remaining_portfolio/`
- 四父 838 叶结果：`degree_diameter_sat/results/n62_four_parent/n62_all_four_parent_55cpu/`
- 四父最终 manifest：`degree_diameter_sat/run55/four_parent_final_leaves.jsonl`
- 后续 12 小时 semantic 结果：`degree_diameter_sat/results/n62_semantic/12h_20260823T163729Z/solve/summary.json`
- 新理论 handoff：`n62_theory_handoff_20260824/N62_SAT_HANDOFF_FOR_CODEX.md`
- 新七模板及审计：`n62_theory_handoff_20260824/n62_root_templates.py` 和 `.json`
- 新 `A+B` 生成器：`degree_diameter_sat/n62_ab_cnf.py`
- 新独立验证器：`degree_diameter_sat/n62_ab_verify.py`

## 9. 建议专家优先回答的问题

1. 三重边排除证明是否完全成立？若成立，旧 `01` 可正式从 SAT 依赖中删除。
2. `d-T` 奇偶恒等式及 simple-`B` 必有奇数个三角形的推导是否成立？
3. 双重边局部分类是否真的使旧 `02` 精确分成三个 `D0*` 轨道，并使交 1、2
   各只剩 `D1_MATCH/D2_MATCH`？
4. `S_TOUCH/S_DISJOINT` 是否无遗漏地覆盖所有 simple-`B` 图？
5. 旧 CNF 的 signature lex order、fiber caps 和 saturated cuts 是否均严格保持
   可满足性？
6. 在确认数学归约后，应优先直接证明两个 `S*` 模板不可能，还是为它们生成
   proof-producing SAT 分解？
