# 23、24度，直径3：有限公开公式补查

检索日：2026-11-01 UTC。仅延伸已有primary集合并作4批窄检索；未读边表、生成图、BFS、solver或Lean，未改专家包。下表是 **best-located public-source guarantees**，不是全球穷尽表，两格 `global_record_confirmed=false`。

| 最大度数 | 定位到的最强公开来源保证 | 依据与条件 | 拟议本地候选 | 比较 |
|---|---:|---|---:|---|
| 23 | **3549** | PolarStar：Brown/ER底图q=16，273点、度≤17；Paley(13)超节点13点、度6；273×13，度≤23，D≤3 | 4336，未生成 | 候选多787；尚未找到压过它的公开保证，不等于确认新纪录 |
| 24 | **6144** | Delorme opposite-GQ：现存GQ(3,5)，degree=(3+1)(5+1)=24，order=24×16²，D=3 | 4544，未生成 | **公开保证多1600，故4544不能改善该公开下界** |

## 24度的决定性反例

[Isham–Lakhotia–Monroe–Petrini，arXiv2608.27253v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)明确记述Delorme的opposite-product族：给定现存GQ(s,t)，度为(s+1)(t+1)、阶数为(s+1)(t+1)(1+st)²、直径3。该处同时列出所有primepower q均有GQ(q−1,q+1)。取q=4，所以s=3,t=5，得到6144/24/D3。原构造归于Delorme《Large bipartite graphs with given degree and diameter》JGT9(1985),325–334；本次未重新取该原文章PDF。

[Bamberg–Giudici作者原论文摘要](https://arxiv.org/abs/1005.2250v2)另明确构造由W(3,q)作Payne derivation得到的(q−1,q+1)广义四边形，支撑q=4的存在条件。这里使用公开公式推论，没有下载6144边表或本地认证该图。

这不是单个GQ的特殊极性商：opposite-product使用互换两坐标的极性，原GQ本身无需有极性。也不能把6144套到cap23：GQ(3,5)有64点、96线，故6144个点线对；384个incident flags删自环后度23，其余5760个顶点度24，实际最大度仍24。

## Brown、IQ、Paley适用条件

[PolarStar，SPAA2024](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)的Theorem3、Table2、Proposition2/Corollary1及§7.1给出：Brown/ER底图对任意primepower q有效；IQ的超节点度d只能满足d≡0或3 mod4，才可用2d+2点；Paley的2d+1必须是≡1 mod4的primepower。因此q16普通Brown合法，但不能使用不存在的IQ_6来代替Paley13，也不能在其他任意d套2d+2。

对这两种已发表超节点公式作全部可用小整数代入（不是图搜索），在cap23下IQ最大3294、Paley最大3549；cap24下IQ最大4368(q16,d7)、Paley最大3991(q17,d6)。表列BDF的2d公式分别最大3294/3822，也不改变上述比较。

Delorme《Grands Graphes》(EJC1985，已有本地primary)的**单GQ直径三特殊极性族**要求q=2^(2m+1)，q16不适用。其q8基图及已读2026 degree18/order2340产品的绝对点复制，分别到这两cap仅1495/1560与2990/3120，均未改善表中值。这里不把generic Brown与特殊GQ极性混用。既有Rajiv三份primary没有找到更强23/24专门实例，维护主表范围也不能给这两格的全球最强值。

结论仅为有据选题：**24度4544已被既有公式压过；23度4336可继续作为未认证新颖性的候选。** 没有把未找到更强值当作全球纪录认证，没有回看Mizuno88452或运行源BFS。机器摘要与检索范围见[DEGREE23_24_EXTENSION.json](DEGREE23_24_EXTENSION.json)。原审阅REPORT及旧证据全部未改。

## 2026-11-01 后续：拟议6160的既有性核查

后续另提出固定Δ24、使用GQ(3,5) spread补16点的6160候选。有限来源检查未定位公开6160或相同补强，但Delorme原JGT文章全文未取得，不能据此认定新颖性；6144是前次定位值，非全球最优认证。候选合法性未由本任务检验。详[dated supplement](DEGREE23_24_EXTENSION_SPREAD_SUPPLEMENT_20261101.md)。
