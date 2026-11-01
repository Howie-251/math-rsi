# 2026-10-06 文献更新与替代路线

**本轮没有核实到已经证明 `m(5)≥33` 的原始文献。** 目前能直接核对的起点仍是 Grill–Linzmayer 2024 的 `m(5)≥32`。这是一轮有针对性的检索结论，不是穷尽查新或新颖性证明；2026 年综述全文仍未取得。

本轮按 ARIS `research-lit` 和 `novelty-check` 的检索原则，结合本地知识库、arXiv API、作者机构页、出版社及公开软件原文。未启动独立新颖性裁决，也不输出评分或模型验收。

## 1. 对当前任务最有用的新增信息

| 材料 | 已检查范围 | 能提供什么 | 对 `m(5)≥33` 的边界 |
|---|---|---|---|
| Ferber–Shapira, *A quantitative Lovász criterion for Property B* (2019), arXiv:1903.04968 | 4 页全文 | 有序单交边对下界、等号刚性、分离事件重叠与 Bollobás 集对论证 | 可加必要条件；原定理本身不排除 32 边 |
| Szeider, *SAT Modulo Symmetries: A Survey* (2025), SC-Square / CEUR Vol.4116 | 11 页全文；重点 §3.2、§3.3、§4.4 | 合法染色驱动的 co-certificate learning、动态同构剪枝、独立证书 | 可实施的计算替代路线；没有声称本项目规模已可解 |
| Cherkashin, *On small non-uniform hypergraphs without property B* (2023), arXiv:2303.03803 | 5 页正文；未重新枚举其图中构造 | 不同边长的权重模型；低阶构造与渐近背景 | 非均匀问题不能直接替代五元目标；无可直接套用的 32 边排除式 |
| Grill–Linzmayer, *An Overview of Property B* (2026) | 出版社元数据、摘要、参考文献 | 确认 2024 下界论文及另一项启发式上界研究被引用 | 未读到正文，不能据此判断最新数值 |
| Linzmayer 2018 硕士论文 | 机构元数据、摘要、检索可见首页 | 模拟退火与 Property B / covering codes 的实现背景 | 官方 PDF 下载返回 HTTP 500；未将其记为已下载或全文已读 |

新增有效本地 PDF 共 **3 份、20 页**，原文链接、文件名、阅读深度及下载状态见 [机器可读记录](literature_new_sources.json)。本分支未修改共享 wiki 或原 reference manifest，供主分支统一吸收。

## 2. 单交边对：一个严格但暂时偏弱的附加条件

令 \(\gamma(H)\) 为满足 \(|A\cap B|=1\) 的**有序**不同边对数。Ferber–Shapira 的 Proposition 1.1（PDF p.1，证明 p.2）给出

\[
H\text{ 不可二染色}\quad\Longrightarrow\quad
\gamma(H)\ge n\binom{2n-1}{n}.
\]

Theorem 1（PDF p.2，证明 pp.3–4）进一步说明：等号成立的不可二染色超图必须包含 \(K_{2n-1}^{n}\)。取 \(n=5\)，阈值为 630；32 条边不可能包含有 126 条边的 \(K_9^5\)，而 \(\gamma\) 是偶数，因此 **任何本项目的反例都必须满足 \(\gamma\ge632\)**。这是文献定理的直接推论，不是目标定理的证明。[原文](https://arxiv.org/pdf/1903.04968)

较有启发的是其证明组织：每个单交边对对应一个排列分离事件，概率恰为 \(4!4!/9!=1/630\)。等号要求这些事件不能重叠，随后导出极强的局部刚性。可探索的改进是：在 32 边、低度标记点条件下，能否强迫若干分离事件发生正量重叠，从而改进并集界。需要对重叠事件另行精确计数，不能直接把文献的等号刻画当成接近等号的稳定性定理。

**可计算的事件交叠改进（本轮推导建议）。** 固定实际顶点 \(x\) 与右边 \(B\ni x\)，把全部满足 \(A\cap B=\{x\}\) 的左见证分成一组。记 \(E_A\) 为 \(A\setminus\{x\}\) 全在 \(x\) 前、\(B\setminus\{x\}\) 全在后的事件。对该组索引的任意树 \(T\)，

\[
\Pr\Bigl(\bigcup_A E_A\Bigr)
\le\sum_A\Pr(E_A)-\sum_{AA'\in T}\Pr(E_A\cap E_{A'}).
\]

证明是逐样本的：若恰有 \(r>0\) 个事件发生，它们在树中诱导的边数至多 \(r-1\)；若没有事件发生，两边都为零。这使扣除不会出现无控制的多次重计。

交事件只要求 \((A\cup A')\setminus\{x\}\) 在前、\(B\setminus\{x\}\) 在后；这两个集合不交。无锁条件下，令 \(q=|(A\cup A')\setminus\{x\}|\le8\)，其概率为

\[
\frac{q!4!}{(q+5)!}\ge\frac{8!4!}{13!}=\frac1{6435}.
\]

锁定条件下应按自由/锁定位置重新计数，不能搬用这个无锁常数。可先按相同锁定类型分组，以已知同型见证数构造树并得到统一交叠下界；外层再对 \((x,B)\) 求并集界。它扣除的是**真实临界对事件之间的重叠**，与 link 修正删除根本不可能成为临界对的多交边对是不同操作。两者如要合用，须清楚标明事件集合，并在更新 \(C'_k\) 后重取逐位置 min；目前没有计算其能否补上困难分支的全部差额。

## 3. 一个可以省掉的方向：裸覆盖 LP 与全体不均衡染色

以下是本轮的独立初等推导，尚未走项目的独立 proof-checker 验收；给出完整论证供复核。

把 `FORMAL_SPEC.md` 的 COVER 模型放松为 \(0\le z_A\le1\)，最小化 \(\sum_A z_A\)，保留所有 \(R\subseteq[v]\) 的覆盖不等式。记其最优值为 \(L_v\)。对任何可行解按全部顶点置换平均，可行性和目标值不变，且得到常数解 \(z_A=t\)。大小为 \(r\) 的红集约束成为

\[
t\left[\binom r5+\binom{v-r}5\right]\ge1.
\]

记括号内为 \(g(r)\)。当 \(r<v/2\) 时，

\[
g(r+1)-g(r)=\binom r4-\binom{v-r-1}4\le0,
\]

并且 \(g(r)=g(v-r)\)，所以最小值在均衡分割取得。于是对本项目的 \(v\ge19\)，常数解满足上界 \(t\le1\)，且

\[
L_v=\frac{\binom v5}{\binom{\lfloor v/2\rfloor}5+
\binom{\lceil v/2\rceil}5}.
\]

| 顶点数 | 全部染色的裸 COVER LP 最优值 |
|---|---:|
|19、20|646/21|
|21、22|57/2|
|23、24|161/6|
|25|230/9|

所以单纯从均衡染色扩展到所有不均衡染色，**不会增强这个 LP 的最优值**。整数模型仍需要所有染色，不能删去非均衡约束后声称等价。

更具体地，取 \(z_A=32/\binom v5\)。它在七个顶点数上都满足全部染色约束、\(\sum z_A=32\)、点对覆盖

\[
\sum_{A\supseteq\{u,w\}}z_A
=\frac{640}{v(v-1)}\ge1,
\]

以及最低度约束

\[
\sum_{A\ni u}z_A=160/v
\ge\left\lceil\frac{v-1}{4}\right\rceil.
\]

因此“裸 COVER LP + 点对覆盖 + 最低度”仍有显式分数可行解；求解这一放松不会排除 32 边。有效改进必须利用整性、已选局部结构或更强的高阶有效不等式。这里没有否定条件化 LP 或 SAT/ILP 路线。

## 4. 可直接实施的计算路线：结构生成 + 染色反证约束

Szeider 的综述 §3.2（PDF pp.4–5）介绍两个求解器配合：第一个生成结构，第二个寻找合法染色；找到染色后向第一个返回排除所有被该染色满足的结构的约束。§4.4（p.7）明确已有超图二分关联图应用。§3.3（p.5）区分对称性置换证书与 SAT 的 DRAT 证书。[原文](https://ceur-ws.org/Vol-4116/invited1.pdf)

对本项目的适配方案（这是建议，不是已经完成的计算）是：

1. 在剩余的具体 \(v\) 与局部轮廓分支中，生成 32 条五元边；加已证明的点对覆盖、度数和共度条件。
2. 使用 E1 寻找该超图的合法二染色。若找到红集 \(R\)，加入
   \[
   \bigvee_{A\subseteq R\ \mathrm{or}\ A\subseteq V\setminus R}z_A.
   \]
   这正是 COVER 约束，排除的不只是当前一个候选。
3. 用顶点及边重标号的同构剪枝压缩生成；关联二分图的两侧需保留类型，不能把原顶点与超边交换。
4. 若生成器最后给出 UNSAT，要保存可独立检查的证明及所有剪枝的数学根据。若染色器给出 UNSAT，则先验证其候选超图与不可染证书，它才可能成为反例。

[官方软件](https://github.com/markirch/sat-modulo-symmetries)和[文档](https://sat-modulo-symmetries.readthedocs.io/en/latest/)已核对入口，本轮没有安装或运行。适合在概率路线留下有限的困难局部型后使用；不预先承诺对所有 19–25 顶点类型直接蛮力即可完成。

## 5. 原作者代码与 2026 文献的实际检查结果

已取得 [arXiv:2403.05674v3 源文件包](https://arxiv.org/src/2403.05674v3)。该下载实际上是 gzip 压缩的**单个 `PropB.tex`**，解压大小 24,778 字节，保存在 `ref/source_packages/grill_linzmayer_2403_05674/`。其 lines 247–252 说明作者使用 C 与 GNU libgmp 做精确计算，但这个版本的源包没有附这些程序。不能扩大为“作者从未公开代码”。

[2026 年综述出版社页](https://link.springer.com/chapter/10.1007/978-3-032-18810-6_9)只开放摘要与参考文献；正文没有获得。参考文献 16 列出 Linzmayer–Grill, *Some upper bounds for property B for small values of n by heuristic search* (2024)，但无可取的全文链接。另查到 [Summit280 官方会议摘要](https://conferences.renyi.hu/uploads/Abstract_Booklet_Summit280.pdf) p.22，只说明采用启发式求上界，不给新的具体数值，故不据此改写本项目文献基准。

## 6. 检索覆盖和下一步

关键检索角度包括：精确标题与作者；`m(5)` 配合 32/33、2-colorable、2025/2026；有限单交边对、link；SAT、整数规划与覆盖；原作者机构页、源包与引用追踪。另用 ARIS arXiv helper 实际执行两组查询：

- `ti:"Property B" OR (au:Linzmayer AND all:hypergraph)`，返回 11 条。无关的拓扑/强迫论 Property B 另行排除。
- `(all:"hypergraph" AND (all:"2-coloring" OR all:"property B" OR all:"two-coloring")) AND submittedDate:[202604060000 TO 202610062359]`，返回 7 条；摘要涉及星染色、随机阈值、几何或其他极值问题，未发现直接排除本项目 32 边的陈述。

原始 API 返回分别保存在 `literature_arxiv_search_20261006.json` 与 `literature_arxiv_recent_20261006.json`。检索结果中的非正式研究日志只作为定位线索，没有用作定理来源。API 题名、作者或日期字段也不能替代原文；例如 2024 基准条目仍错误地把 TU Wien 当作作者。

优先继续当前多锁定与 link 证明。若具体局部型仍无法闭合，再从两处引入增量：临界分离事件的交叠扣除；按困难局部型运行有证书的 CCL/SAT。暂不把纯均衡计数换成无条件全染色 LP 当作新的改进。
