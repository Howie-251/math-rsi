# (25,3)：7225公开公式与7242候选的有限比较

检索日：2026-11-01 UTC。只核这一格，沿用已有primary集合并完成3批窄web检索。没有读边表、构图、BFS、solver、Lean、安装或改专家包。任务下达时7242尚未生成；本报告不把候选计入成果，后续实际构造状态由producer另记。

**best-located公开来源保证为7225；本次未定位明确公开的≥7242实例或同一spread补17公式。** 这不是全球穷尽，也不证明首创，`global_record_confirmed=false`。

## W(3,4)和17线spread的一手依据

[Delorme，Grands Graphes，EJC6(1985),291–302](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)§1(pp291–292)使用PG(3,q)的点与非退化交替形式下的完全迷向直线构成阶q的广义四边形，即symplectic W(3,q)。§8(a)(pp298–299)对任意primepower q，以不可约二次多项式给出的矩阵A构造直线〈X,AX〉，明确得到q²+1条互不交直线，partition全部点；这是所需line spread，而非仅引述其名称。

取q=4：点数为q³+q²+q+1=85，线数同为85；每线5点，每点5线。spread为q²+1=17线，17×5=85点。这项存在性不受特殊单GQ极性商的q=2^(odd)条件限制。本次没有新生成85点几何或搜索spread。

## 7225的公开公式与其它已读族

[arXiv2608.27253v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)给Delorme opposite-GQ族：

`N=(s+1)(t+1)(1+st)^2，Δ=(s+1)(t+1)，D=3`。

该处明确包含所有primepower q的GQ(q,q)，故s=t=4给`N=25×17²=7225，Δ=25`。原GQ无需有极性；不能与不允许q4的特殊单GQ直径三极性商混淆。原构造归属Delorme《Large bipartite graphs with given degree and diameter》JGT9(1985),325–334。

同一已读[PolarStar primary](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)的有效小整数代入，cap25下IQ最大4914（q16,d8,273×18）、Paley最大4641（q16,d8,273×17），均低于7225。这里遵守IQ的d≡0或3 mod4、Paley的2d+1为≡1 mod4的primepower条件。Delorme一般升一度复制套公开24度6144图仅直接保证6155，也不改变比较；这只是公开公式推论，不是另找到一份6155边表。

## 7242补强的归属边界

由阶(4,4)计数可推出opposite基图有425个incident flags度24、6800个非flags度25；原边数90100。父级提出沿17线spread，把425余度flags分成17组各25个pins，加17点425边，预期7242点90525边。这些是**候选规则与整数代入**，本任务未检验数据或合法性。

已读arXiv§7.7及Delorme EJC§7/8的复制陈述是`N+k|S|、Δ+k`，并未明确给出本次保持25度的flag-star补点公式。三批精准检索也未定位7242或≥7242一手保证；数字检索相关召回较弱，不能当作无既有结果的证明。

重要缺口仍继承[前次spread既有性核查](DEGREE23_24_EXTENSION_SPREAD_SUPPLEMENT_20261101.md)：Delorme原JGT1985正文未取得，当时出版社入口仅回摘要，本次没有重复取文。因此不能声称原文没有该补强。经典GQ、spread和opposite-product归属必须保留；具体增点规则的公开优先权与全球纪录均待核。

当前没有找到需要因公开≥7242而取消候选的依据。若producer的实际构造通过，只可先称“超过本次定位的7225公开公式构造17点”，不能称已认证全球SOTA。八图专家快照及旧Four均未更动；完整检索词和公式范围在[JSON](DEGREE25_EXTENSION_20261101.json)。
