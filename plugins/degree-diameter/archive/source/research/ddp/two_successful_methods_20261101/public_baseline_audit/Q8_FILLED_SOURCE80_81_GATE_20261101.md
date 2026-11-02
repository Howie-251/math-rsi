# q8两个filled-source候选：80度＋64、81度＋65的有界公开门

2026-11-01 UTC。**已核PolarStar／Delorme／GQ公式在80、81度的最大保证分别仍为327680、342225；两个filled-source候选327744、342290分别多64、65点。** 本次只做参数选择标量门，不生成或验收图，不认证world SOTA／优先权。

| 参数 | 本次选择的源 | 已核公开源保证 | 条件fill数 | 条件候选 | 差值 |
| --- | --- | ---: | ---: | ---: | ---: |
| 80,3 | Payne GQ(7,9) opposite源 | 327680 | 64 | 327744 | +64 |
| 81,3 | balanced GQ(8,8) opposite源 | 342225 | 65 | 342290 | +65 |

来源几何的真实F8/F64、fullO/spread和全部projection已经由独立小实验PASS；本报告直接继承，不重验域或几何。这不等于完整opposite/fill图已经生产或验收。当前仅准备两个生成器，未增validated_graph_instances。

## 实际代入的公开门

已核[opposite-GQ一手公式及参数域](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)给degree=(s+1)(t+1)、order=(s+1)(t+1)(1+st)²。q8的两次代入分别为80×64²=327680、81×65²=342225。

PolarStar按[作者原文](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)IQ／Paley全部合法小整数代入；folded、standard12 duality、一般复制按[Delorme原文](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)及已核接口。极性产品沿用已核适用参数，不假定任意q都有相应极性。

| cap | PolarStar IQ | PolarStar Paley | GQ直接 | ovoid/spread复制比较 | folded复制 | standard12 duality复制 | 极性组合复制 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 80 | 148962 | 151739 | **327680** | 327680 | 82000 | 82240 | 164000 |
| 81 | 160328 | 151739 | **342225** | 342225 | 83025 | 83268 | **342225** |

81度q8×q8极性产品也给342225，并未超过balanced直接源。IQ最大参数80为q47/d′32，81为q53/d′27；Paley两cap均由q53/d′26给151739。每个最佳参数与合法计数在同名JSON。

本地filled源始终没有当作公开来源。此处327680／342225是已发表公式的保证，不声称另定位到两个数值的独立公开边表或全球维护表。

## 81度必须换源，不能自动延续80度Payne复制

即使80度Payne filled候选327744成立，再给其fullO64×spread64的4096个basecenters各复制一次，81度也只有

```text
327744+4096=331840 < 342225，少10385点。
```

因此这个81度延续已被真实公开balanced源阻断；新81度候选应使用balanced GQ(8,8)源的65点fill，不能将source80链入source81。阻断的是该复制方向的竞争性，不是81度图存在性。先前停止的P33 k16／degree80候选186450同样保持停止；当前327744是另一明确源选择。

## 优先权边界与执行回执

[exact spread-fill优先权审查](SPREAD_FILL_SOURCE_PRIORITY_20261101.md)仍为 **UNKNOWN**：已读一般lemma/spread并未定位相同opposite-source fill pins及覆盖规则，关键JGT1985正文仍未取得。若同一filled-source构造已公开，当前源候选的64／65优势可能归零；本门没有据未命中认证新纪录。当前public数字未改。

实际标量CPU **0.044623607秒**，小于5秒。[源代码](Q8_FILLED_SOURCE80_81_GATE_20261101_scalar_check.py)和[JSON](Q8_FILLED_SOURCE80_81_GATE_20261101.json)已保存。0新query、旧P33窗口重验、q8field/geometry检查、完整图、BFS、Lean、solver、外审或Wiki helper。rootcounts、专家DRAFT和所有冻结包不改；未派82及以上degree梯子或长期Lean。
