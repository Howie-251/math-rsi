# 第4页上界与来源核对

核对日期：2026-11-17。对象为本目录 `progress.tex` 第4页。本说明核对数值、对象域、文献进口和现存计算证据的归属，不是完整项目证明的独立验收。没有在本轮启动 solver、重跑 Linux checker、构建 Lean 或调用独立 proof-checker。第1、2、3、5页不在本次修改范围。

## 阅读口径

`N(m,r,s)` 是有序 rank-3 signotope 的最大避免人口，禁止蓝 r 点链、红 s 点链与 weak m-gon。`ES(m)` 是实际平面一般位置点集的强迫阈值。不能把两者混写，也不能从公开的平面 `ES(8)≤319` 反推所有 signotope 的容量。

左列为选定的已公开文献定理及其明确组合推论，不是“所有行的最佳已知值”认证。星号表示本说明从公开结果组合得到的数值，**不表示原论文印出了这个数值**。右列是项目现用工作上界：`d` 为直接文献进口，`t` 为公开有限数据加项目抽象迁移，`c` 为已有精确有限 checker 日志支持的证书及项目装配。无字母的右列数值是项目解析工作稿。绿色只表示相对本表左列更小，不表示原创性、最优性或已独立接受。

## 文献原件和采用范围

1. [Baek, *On the Erdős–Tuza–Valtr Conjecture*, v2](https://arxiv.org/html/2206.04260v2)。Theorem 2.6 的有序配置 cups–caps 容量是 `binom(r+s−4,r−2)`。Theorem 2.7 给四帽受限上界 `binom(m−1,2)+1`，在 m=8、9 为22、29；Theorem 1.6是对应的平面陈述。22与29是直接文献进口，不归为本项目新证明。
2. [Dobbins–Holmsen–Hubard, arXiv:1305.2266v2, §3](https://arxiv.org/pdf/1305.2266)。采用 Observation 3.2 的杯帽延长规则、Lemma 3.4 以及其后重取根论证。广义配置/伪直线的模型解释也见其§1.2。此处按项目使用的 rank-3 signotope/wiring 对应解释链与 convex/weak 出口；**不推广到任意三元组二染色**。Lemma 3.4 单独给 `N(8,7,8)≤461`、`N(9,8,9)≤1715`，下述递推组合更强。
3. [Schroeder, *Erdős–Szekeres: Upper Bounds for Convex Heptagons and Octagons*, Version 1, 2026预印本与附件](https://michaelschroeder.ai/research/ErdosSzekeres/companion)。公开结论包括平面 `ES(8)≤319`。本地原件 [geometry.tex](../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/geometry.tex) 的 `thm:transfer` 是平面 `Q_n≤C_n+D_n` 和 `ES(n)≤C_n+D_n+2`；[octagons.tex](../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/octagons.tex) 给平面193与124及有限证书。其平面证明不自动成为项目抽象 signotope 证明。
4. [Nassajian Mojarrad–Vlachos, arXiv:1510.06255v2 (2016), Theorem 1.1](https://arxiv.org/abs/1510.06255)。在 n=9，`binom(13,7)−binom(10,6)+2=1716−210+2=1508`。
5. 近期交叉来源 [Aichholzer et al., *Garment numbers of bi-colored point sets in the plane* (2026), Appendix B, Lemma 10证明，第13页](https://arxiv.org/pdf/2603.05339#page=13) 也明确写出 `ES(9)≤1508` 并归于 Mojarrad–Vlachos。这是公开使用1508的佐证，不是检索完整性或2026年绝对最佳值认证。

22与29可以作精确判断，而非仅有上界。Baek Definition 1.4定义取等命题 `P(n,a,b)`，Theorem 1.6证明 `P(n,4,n)`，故平面避免最大值在n=8、9分别恰为22、29。平面下界构造同时是本表的合法signotope；Theorem 2.7又给抽象上界。因此本表同一避免域内也有 **`N(8,4,8)=22`、`N(9,4,9)=29`**。这两行的确切最优性来自文献，不是项目原创，也不能外推为其他行最优。

## 左列组合推论的完整算术

记 `T_m(r,s)=N(m,r,s)`。按 DHH Observation 3.2 的同一点杯帽延长规则，把点分为“结束一条红(s−1)链”的集合 A 与其补集 B。B 无红(s−1)链；A若含蓝(r−1)链，其起点已有所选红(s−1)入链，延长规则迫使红s链或蓝r链。因此

`T_m(r,s) ≤ T_m(r−1,s)+T_m(r,s−1)`。

两部分都是原配置的实际子配置，继承 weak m-gon 禁形。此递推给的是文献规则的组合推论，没有导入右列51、63、109等项目加强。

| 推论 | 只使用文献输入的算术 |
| --- | --- |
| `N(8,5,8)≤78*` | `22+56=78` |
| `N(8,6,8)≤204*` | `78+126=204` |
| `N(8,7,8)≤456*` | `204+252=456` |
| `N(9,5,9)≤113*` | `29+84=113` |
| 辅助 `N(9,6,9)≤323*` | `113+210=323` |
| 辅助 `N(9,7,9)≤785*` | `323+462=785` |
| `N(9,8,9)≤1709*` | `785+924=1709` |

DHH §3 的重取根保持广义配置的凸位置关系：删去极端根后，相应方向不能含(m−1)链。故全对角避免人口满足 `F_m≤Q_m+1`，给 `N(8,8,8)≤457*`、`N(9,9,9)≤1710*`。原有462、1716是较弱的文献对角避免人口界，不再用它们伪装最强的可立即组合基线。

对真实残余 D_m，把点按是否结束红(m−2)链二分。未结束者无两色(m−2)链；结束者因禁止同一点的 junction 而不能开始蓝(m−3)链，所以整个第二类无蓝(m−3)链。两类都继承 weak m-gon 禁形，进而无单色m链。于是

`D_m ≤ N(m,m−2,m−2)+N(m,m−3,m)`。

这给 `D_8≤70+78=148*`、`D_9≤252+323=575*`。原154、582来自第二类只用普通 cups–caps 容量，确为有效但较弱的基线。它们也是现有证书的状态宇宙大小，不能因新比较基线而改写证书宇宙。

还有一个必须披露的平面组合：Schroeder的公开平面 residual transfer 定理配合 `C_9≤924`、`D_9≤575`，给

`ES(9)≤924+575+2=1501*`。

因此幻灯片左格同时保留 **1508 [1501*]**。1508是上述论文已明确写出的数值，1501是本次组合公开定理的推论，不署名为 Mojarrad–Vlachos 的数值，不称已有外部先例、已审阅新纪录或全局最优。**项目抽象 signotope 的 `Q≤C+D` 不计入左列文献推导**；此处1501只使用公开平面定理。

## 八边形逐行登记

| 对象 | 左列文献基线 | 右列工作值及原件 | 层级 |
| --- | ---: | --- | --- |
| `N(8,4,8)` | 22 | 22，Baek2.7；项目调用见 [CASCADE-63 §2](../n79-overlap-20261116/CASCADE-63.md) | d，直接进口 |
| `N(8,5,7)` | 56，`binom(8,3)` | 51，[THREE-COLUMN-STRICT §§1、6](../n79-overlap-20261116/THREE-COLUMN-STRICT.md) | 解析工作稿 |
| `N(8,6,6)` | 70，`binom(8,4)` | 63，[FIVE-ACTIVE866 §6](../n79-overlap-20261116/FIVE-ACTIVE866.md) | 解析工作稿 |
| `N(8,5,8)` | 78* | 66，[坐标删除原稿 §8](../n78-row-compression-20261115/PROOF.md)，22的真实含坐标切片双计数 | 解析推论，仍依赖Baek |
| `N(8,6,7)` | 126，`binom(9,4)` | 109，[PROOF §§2–7](../n79-overlap-20261116/PROOF.md)，126态至少17洞 | 解析工作稿 |
| `N(8,6,8)` | 204* | 165，[坐标删除原稿 §8](../n78-row-compression-20261115/PROOF.md)，由66双计数 | 解析推论，不用残余124替代普通容量 |
| `C_8=N(8,7,7)` | 252，`binom(10,5)` | 193，[EIGHT-CYCLE-TRANSFER §§1–8](../n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md) | t，Schroeder公开数据加项目抽象桥 |
| `D_8` | 148* | 124，同一迁移稿 | t，同上，真实残余 |
| `N(8,7,8)` | 456* | 317=`193+124`，同一迁移稿§8及 [R7 §3.2](../../.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) | t，项目抽象装配 |
| `N(8,8,8)` | 457* | 318=`317+1`，同一迁移稿及 [R20](../../.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) | t，合法chart加一 |
| `ES(8)` | 319，Schroeder公开预印本 | 319，既有平面数值；项目迁移线也给318+1 | d，不是新的平面数值下降 |

193、124不是本项目原创的平面数值。项目新增主张是公开有限行与树对完整 signotope 输入的抽象迁移。有限 checker已在Linux重放，但新packet桥未独立审阅。原始证据为 [OCTAGON-SOURCE-RECEIPT](../n79-overlap-20261116/OCTAGON-SOURCE-RECEIPT.md)、[replay-receipt.json](../n79-overlap-20261116/octagon-source-replay/replay-receipt.json) 与 [finite-result.json](../n79-overlap-20261116/octagon-source-replay/finite-result.json)。这些记录不能当成全链Lean重建或抽象桥的独立验收。

## 九边形逐行登记

| 对象 | 左列文献基线 | 右列工作值及原件 | 层级 |
| --- | ---: | --- | --- |
| `N(9,4,9)` | 29 | 29，Baek2.7；项目调用见 [平移行原稿 §9.3](../n78-shifted-rows-20261116/PROOF.md) | d，直接进口 |
| `N(9,5,8)` | 84，`binom(9,3)` | 78，[THREE-COLUMN-STRICT §§1、6](../n79-overlap-20261116/THREE-COLUMN-STRICT.md) | 解析工作稿 |
| `N(9,5,9)` | 113* | 96，[平移行原稿 §9.3](../n78-shifted-rows-20261116/PROOF.md)，`floor(10·29/3)` | 解析推论，依赖Baek |
| `N(9,6,7)` | 126，`binom(9,4)` | 117，[GRAPH §§2–5](../n79-overlap-20261116/GRAPH.md) | 解析工作稿 |
| `N(9,6,8)` | 210，`binom(10,4)` | 185，[TRANSFER-NEXT §§5–10](../n79-overlap-20261116/TRANSFER-NEXT.md) | 解析工作稿 |
| `N(9,7,7)` | 252，`binom(10,5)` | 222，[NINE29](../n79-overlap-20261116/NINE29.md) | 解析工作稿 |
| `N(9,7,8)` | 462，`binom(11,5)` | 380，[PROOF §9.3](../n79-overlap-20261116/PROOF.md)，462态至少82洞 | 解析工作稿 |
| `C_9=N(9,8,8)` | 924，`binom(12,6)` | 688=`924−236`，[direct-cycle-lp/RESULTS](../n79-overlap-20261116/direct-cycle-lp/RESULTS.md) | c，有限证书及原输入接口 |
| `D_9` | 575* | 458=`582−124`，同上 | c，582态是真残余证书宇宙，不是本表最强组合基线 |
| `N(9,8,9)` | 1709* | 1146=`688+458`，同上、R7 | c，项目装配 |
| `N(9,9,9)` | 1710* | 1147=`1146+1`，同上、R20 | c，合法chart加一 |
| `ES(9)` | 1508，另列1501* | 1148=`1147+1`，同上 | c，几何子类及避免到强迫加一 |

原始成功日志 [run-988-d2/standalone-check.log](../n79-overlap-20261116/direct-cycle-lp/run-988-d2/standalone-check.log) 与 [run-d9-d3/standalone-check.log](../n79-overlap-20261116/direct-cycle-lp/run-d9-d3/standalone-check.log) 均记录 `status=PASS`。本轮静态读到：

| case | states | 缺失态下界 | 上界 | 正权行数 | 精确分子 | λ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 988 | 924 | 236 | 688 | 883 | 235971673 | 1000000 |
| d9 | 582 | 124 | 458 | 532 | 123539361 | 1000000 |

分子分别严格大于235λ与123λ，故整数缺失态至少236与124。checker为 [compact_certificate_final.py](../n79-overlap-20261116/direct-cycle-lp/compact_certificate_final.py)。紧凑证书为 [988 JSON](../n79-overlap-20261116/direct-cycle-lp/run-988-d2/compact-certificate.json) 与 [D9 JSON](../n79-overlap-20261116/direct-cycle-lp/run-d9-d3/compact-certificate.json)。本轮另核了两份文件SHA256，与日志的 `compact_sha256` 一致：

- 988：`5872dda9c68e83696f42d5e45edb41294647fd0546ab1752a17b25e0ab17bec8`
- d9：`ccee0f65beba7f72709ee4e9cc77a5d71faddc9fb3c270f365544b91d40a5638`

本轮读取历史成功日志及核文件绑定不等于本轮重跑。有限支持、整数算术与实际配置到certificate rows的数学接口是不同义务，后者仍依赖工作稿，完整九边形证明没有因这些PASS而升级为独立审阅通过。

## 本轮交付与限制

第4页已替换历史项目左列为以上文献基线与标星组合；右列数字未改，明确分出直接进口、迁移与证书。来源检索覆盖本说明列出的原论文、Schroeder已绑定源包、近期1508交叉来源和项目原始工作文件，未宣称穷尽所有公开论文、最新预印本或所有可递推加强。没有宣称全部右列原创、最佳或已独立接受。

现有完整登记入口仍为 [LARGER-PARAMETER-BOUNDS.md](../n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)。本说明保留原始工作文件中的历史阶段与认证边界。
