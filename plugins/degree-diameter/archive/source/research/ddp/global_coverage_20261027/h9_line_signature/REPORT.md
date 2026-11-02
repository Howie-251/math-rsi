# H9 line-image 预测：675 点整块被必要条件否定

`PREDICTION.json` 在筛选前冻结 P_line：当前首段675个 non-star extras（41502..42176）的核心附件 A_i 各包含一条完整 H(9) 几何 line 的 partial-fold 像，额外 pins 可以是 anchors。**675/675 均未通过必要条件，因此该整块解释被否定。** 没有重建 incidence、调用作者 verifier、运行 BFS 或生成新图。

## 折叠后 line 能否少于10点

须区分 φ=τ² 固定与非固定的 line，不能直接假设所有 line 像都有10点。依据已下载原文 Lemma4.1（正文第4–5页）及 Theorem5.1：

1. 若 line L 不被 φ 固定，则它不可能同时包含 p 和 φp：否则 L 与 φL 共享两个不同 points，由唯一线性质得到 L=φL。故其10个 points 在 partial fold K 中仍有10个不同像。令 L=σ(p)；p 不属于 H(3)，Lemma4.1 又证明 p、φp 均不在 τp 或 τ⁻¹p 上。因此整个 line 像落在 v=fold(p) 的**开**邻域 N_K(v) 内。
2. 若 L 被 φ 固定，则它是 H(3) 的一条线，含4个 H(3) points 与3个 generic φ-pairs。其中 s 个 pairs 被 split，像大小为7+s。H(3) 极性 σ 给唯一 h 使 L=σ(h)。非 absolute h 的 line 像恰是 N_K(h)；absolute h 的像是 N_K(h)∪{h}。两种均包含完整核心 star N_K(h)。此前810个 non-stars 的完整-star 包含筛已排除这一例外；颜色不改变 h 的这条邻接公式。

因此，对本次810个 non-stars，若 A_i 含任何完整 H(9) line 像，必有某 v 满足 |A_i∩N_K(v)|≥10。无需知道具体 incidence 表即可检验该必要条件。

## 一次实际筛选

| 对象 | 数量 | max open-star 交数分布 | 必要筛通过 |
|---|---:|---|---:|
| 原675点段41502..42176 | 675 | 654点为1，21点为2 | 0 |
| 最后165点中的non-star | 135 | 65点为1，11点为2，1点为5，2点为6，56点为10 | 56 |
| 全部non-star | 810 | 详见JSON | 56 |

56个通过者仅有必要交数，**尚未识别真实 line**，不能称为56条 line-image、pencils 或已证新—新覆盖。余754点已不可能满足这个具体 line-image+anchors 解释。

675点中647个的最大**闭**star交数也仅1。因此其任意两个 pins 既不相邻也无共同核心邻点，核心距离至少3。另28个最大闭交数为2；不能把 open-max=1 的654个全称两两距离≥3，因为某些 pins 可能相邻。

首个反例41502的10 pins 是

`{7,4212,8259,12377,12453,19260,19421,25736,26058,36805}`。

其 max-open=max-closed=1。`first41502_dispersion.json` 保存45个无序 pin-pairs 的直接邻接和共同邻点证据：全部为零，闭半径1邻域两两不交。41502也没有任何 extra 邻点；加入它使这45对 pins 都得到2步通路，而它们在 K 中原距离至少3。这与普通 twins 不能缩短核心距离的机制不同；没有求这45对的实际距离。

## 缓存与停止范围

现有目录有 τ、partial-fold witness、Q_data 与图边表，没有发现 point-line incidence 或逐 line folded-signature 缓存。τ 本身不是 incidence 表；K 的 merged 邻域或同色 split 的 K2,2 可合并多条关联信息，不能把任意10点邻域子集直接宣布为几何 line。这里只说明现成数据缺少直接、无歧义的 line witness，不声称证明了从整个 K 永远不可恢复几何。

原 `build_hexagon` 的完整版本自称需要几分钟，并枚举66430个 points 各728个局部组合，再生成全部 lines；本次没有运行。必要筛已否定675点块，故不为这一预测重建全 incidence。单次必要筛 CPU0.277466秒；首例45-pair证据的CPU另列于JSON。

## 下一项可证伪的互补覆盖建议（尚未执行）

P_irredundant：41502的10个 pin 的核心 R4 球各有非空 private region，即每个 pin a 都存在 x，使 d_K(a,x)≤4 而其余9个 pins 到 x 均>4。只需固定同一 A，不改 pins、不加 helper，用已有距离缓存或经 root 另行选择的一次10根 R4 计算检查覆盖重数和各 private region；任一 region 为空即推翻“10个 pin 都承担不可替代覆盖”的预测。

全体10球覆盖 K 已可从现有 P3 的41502成功行推得：此前146个 extras 均是完整邻域 clones，其相互边没有超出原型边的额外边，故 earlier graph 可回缩到 K；41502只连这10个核心 pins。这里新增的未知预测是各 pin 是否都必要，而非重复检查已知整图D5。无论结果如何，它只检验分散 pins 的覆盖互补，尚不给批量生成公式，也不代替新—新距离证明。本建议未执行；随后若有新的受控几何预测另行记录，不把它混为本次结果。

证据：本目录冻结预测、`necessary_filter.json`（全部810行）、`first41502_dispersion.json`；原文 `breadth_20261027_wave3/hexagon_partial_fold_scout/23056128_partial-folds-split-cayley-hexagon-H9-large-graphs-diameter-five.txt`；继承的 `h9_relation/star_containment.json`、`structural_classification.json` 与 root 的 `tail165_mechanism/RESULT.json`。新图0，新下界0。
