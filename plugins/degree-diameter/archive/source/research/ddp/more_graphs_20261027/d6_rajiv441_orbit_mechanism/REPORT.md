# Rajiv441：实际旗机制已恢复，直推q4不在度数范围内

目标是理解原(6,4)441点PSU(3,3)三轨道源，先验证源模型再判断q4，而非沿已停504/650或split搜索。当前源邻接/旗坐标恢复完成，没有新图、源BFS、SAT或随机群搜索。结论：最初提出的双三角/3B+3C模型被反驳；真实规则的自然q4延续最大度达到15，不能据此声称2912点/degree9候选。

来源是 [原始441边表](../../second_mechanism/rajiv441.edges)、[已保存作者原文](../../second_mechanism/rajiv.txt) Appendix A，以及 [Comellas官方D4页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html)。作者Rishabh Rajiv，2026-09-24，组PSU(3,3)阶6048，轨道63/189/189、稳定子96/32/32。源1323边未重新BFS验算。

**事前预测与实际配额。** [PREDICTION.json](PREDICTION.json) 依据原文先预测正确配额，并明确检验所给替代模型；实际 [SOURCE_PROFILE.json](SOURCE_PROFILE.json) 为：

| 轨道/源编号 | A邻居 | B邻居 | C邻居 |
|---|---:|---:|---:|
| A：0–62，共63 | 0 | 6 | 0 |
| B：63–251，共189 | 2 | 0 | 4 |
| C：252–440，共189 | 0 | 4 | 2 |

C内部恰63个K3，B内部没有边。故A不是3B+3C，B/C也不是两个内部三角层。

**精确组合坐标。** 把每个B的两个A邻点投影成一条边，得到A上一个简单6正则图。189条边唯一分成63个三元组，每个A点恰在3个三元组中。称A点为point、三元组为line；目前这只是源中完全恢复的点–三元组几何，不把它未经识别就当作PG2(9)非各向同性点坐标。

B点对应flag(P,L)，其中L为其A邻点对所在的唯一line，P是该line中被漏掉的第三点。每个C的4个B邻居，其marked points恰为同一line M中的另外两个点、各出现两次；由此唯一恢复C的flag(Q,M)。所有189个C labels互异。

完整边规则为：

1. A_a与B(P,L)相连，当且仅当a∈L且a≠P。
2. B(P,L)与C(Q,M)相连，当且仅当P∈M、P≠Q且L≠M。
3. C(P,L)与C(P,M)相连，当且仅当L≠M，即固定point的旗形成clique。

第2条与全部756条B–C边完全一致，第3条与全部63个C三角形一致；连同378条A–B边，恢复全部1323边。源坐标及对应表在 [COORDINATES.json](COORDINATES.json)。我的第一版“C三角形固定line”猜测被实际反驳，随后冻结 [C_PANEL_PREDICTION.json](C_PANEL_PREDICTION.json) 并确认它固定的是point，结果在 [C_PANEL_ACTUAL.json](C_PANEL_ACTUAL.json)；没有把失败猜测默默保留到q4。

**真实路线含义。** 设A投影点图的一条三步测地线为a–P–R–b，所在lines依次L、M、N，取M中除P、R外的第三点Q。那么

```text
A_a — B(P,L) — C(Q,M) — B(R,N) — A_b
```

是四步路线，压缩了点图三次换点。这说明C旗层为何可以补足A–B–A–B–A只能覆盖的点图二步范围；它只是A–A类的解释，未宣称所有推广的旗类型点对都在四步内。源配额对应的非回退词预算亦已精确列于 [ROUTE_BUDGET.json](ROUTE_BUDGET.json)：A/B/C根各共937词，按目标A/B/C分别为(181,300,456)、(100,485,352)、(152,352,433)。词数仍不等于独立端点覆盖，此处不以预算冒充新D4验证。

**q4参数门槛。** 将同一旗操作写在任意均匀点–线几何上：每line有s+1个points，每point在t+1条lines中，points数v、flags数v(t+1)。则
\[
n=v+2v(t+1),\qquad d_A=d_B=s(t+1),\qquad d_C=t(s+1).
\]
A的邻居由经过它的line和line中其它marked point选择；B有s个A邻居与st个C邻居；C有st个B邻居及同point的t个C邻居。因此度数等式不依赖任何距离假设。

源是s=t=2、v63。若采用最初设想的自然Hermitian非各向同性point/orthotriad q4几何，则v=q²(q²−q+1)=208，正交邻点q(q−1)=12，每point在6个orthotriads中，flags1248。其dual亦列作条件对照；本轮没有做q3源与这两种坐标取向的同构识别，因为两种取向都已不能给当前度数范围内的原规则迁移：

| 条件模型 | A/B/C阶数 | 总阶 | A/B/C度数 |
|---|---|---:|---|
| 原源 | 63/189/189 | 441 | 6/6/6 |
| q4 points/triads | 208/1248/1248 | 2704 | 12/12/15 |
| q4 dual | 416/1248/1248 | 2912 | 15/15/12 |

核心错误是把C内部固定point的整个panel仍当作triangle：point/triad取向中，每point有6个flags，literal规则产生K6，C内部度5，加cross10共15。只把A分两份并matching它们不会降低B/C的度，因而不能推出degree9；point取向分A后阶数虽为2912，最大度仍至少15。详见 [Q4_PARAMETER_GATE.json](Q4_PARAMETER_GATE.json)。即使另改panel或cross连接，这已是需要重新证明全类覆盖的规则，不能从441源自动继承D4。

这里的q4算术是明确的条件模型，不声称源已被嵌入上述Hermitian坐标，也没有生成q4图。对原literal旗操作，度15超过当前Δ≤12，故不启动q4构造或求解；其它PSU轨道/稳定子或新连接方式并未排除。

恢复/配额CPU0.005609779秒，C-panel检查CPU0.002104584秒，参数/预算仅小型类型递推，无编译或源BFS。复现顺序为 [recover.py](recover.py)、[finish_flags.py](finish_flags.py)、[parameter_budget.py](parameter_budget.py)。原始预测、失败分支及坐标全部保留；此次有价值的结果是精确源规则与错误外推的止损，新下界0，当前源分析收束。
