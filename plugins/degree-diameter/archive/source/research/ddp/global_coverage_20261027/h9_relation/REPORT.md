# 41699与42342的共同部分折叠核心：精确关系和仍缺的pencil规则

两图确实共享一个**41356点、234318边的同编号诱导核心**，不是仅有同样的H(9)来源。它是旧witness的 `33397+7959` 部分折叠，不含其后280个H(3) copies和63个普通twins；故该共同核心可直接继承旧Theorem5.1的全局D≤5保证。当前42342图由这一共同核心加986点组成。

但旧41699成品不能在未核对的情况下当作当前图原样保留的核心。两图附加区的编号和邻接明显不同；当前作者没有提供逐点copy/pencil分解。以下区分了精确图比较、结构匹配和作者来源陈述，没有把编号差异冒充实际删边历史。

## 原始来源与旧构造的可复现关系

仅使用已有文件，未重试链接或下载：

* Rajiv [23056128](https://zenodo.org/records/23056128)：本地完整论文§5、Theorems5.1/5.2、Table2；旧witness、`graph_d12k5_n41699.edges.xz`及生成函数`partial_fold`。后者只读，未执行默认verifier。
* Dhar [23653049](https://zenodo.org/records/23653049)：本地metadata的三段H9描述、README、CURRENT_GRAPHS及42342原始邻接。已有`SOURCE_NOTES.md`、`raw_structure_initial.json`、appendchecks同时复用。

旧生成器明确先按几何point labels建立G(S,c)，再把H(3)额外copies编号追加，最后追加普通twins。旧witness的三阶段是：

| 旧阶段 | 顶点标签范围 | 点数 | 边数 |
|---|---|---:|---:|
| G(S,c)，|S|=7959 | 0..41355 | 41356 | 234318 |
| 加280个H(3) copies | 0..41635 | 41636 | 237006 |
| 再加63个普通twins | 0..41698 | 41699 | 237699 |

旧H3 copies和twins的具体数量、颜色、邻接负载已由wave3结构记录核对。旧的全局D5充分性来自点到线奇路径投影及复制定理，而不是本次重复BFS。

## 一次明确的只读边集比较

显式测试旧编号0..41698到当前相同编号的映射；没有先假定该映射是正确几何对应。

| 比较范围 | 旧边 | 当前同范围边 | 共同边 | 旧边缺失 | 当前新增 |
|---|---:|---:|---:|---:|---:|
| 前41356点诱导图 | 234318 | 234318 | 234318 | 0 | 0 |
| 前41636点诱导图 | 237006 | 237007 | 234330 | 2676 | 2677 |
| 前41699点诱导图 | 237699 | 237732 | 234330 | 3369 | 3402 |

因此共同41356核心的identity对应已由全部边证明；超过此范围，旧标签不能直接继续沿用。比如旧边(0,41521)在当前同编号图中不存在，当前则有旧图没有的(0,41442)。这些附加点可能重新编号、重新配置或增加了anchors；原文不足以判定哪个操作实际发生。

若硬按上述identity编辑旧41699图，需要删3369条旧边、加10887条当前边，净增7518边；其中新增包括前41699内3402边、与后643点之间7464边、后643内部21边。这是**数值标签下的精确差集**，不是作者确实执行了这些删边/重接操作的证明。没有搜索任意重标号embedding或图同构。

以真正已证的共同核心为base，当前分解则没有任何歧义：

`42342 = 41356 + 986`，

`245217 = 234318 + 10517(core–extra) + 382(extra–extra)`。

old-old核心点对的D≤5因此继续成立；附加986点的old-new、new-new覆盖仍需各自生成规则或证书。

## current986的结构等邻接分类

按root补充授权，只做一次无距离的结构分类。对每个current extra v取N_core(v)，检查是否**等于**共同核心某个原型h在核心内的完整邻集N_core(h)。所有匹配都保留原型编号；没有据此强行判定几何类型。

| 数值范围 | extra数 | N_core完整相等者 | 不满足相等者 |
|---|---:|---:|---:|
| 41356..42176 | 821 | 146 | 675 |
| 42177..42341 | 165 | 30 | 135 |
| 合计 | 986 | 176 | 810 |

176个相等者的core原型全部唯一。这只是copy-like结构，不证明是作者H3 copies、ordinary twins或pencils。810个未相等者不能直接叫810 pencils。随后按root单独授权做了更宽的完整star包含测试，结果这810个点也完全不包含任何core原型的完整邻集；见下节。几何类型仍未据此命名。

一个可直接使用的**正向全局覆盖**结论是：共同核心加上述176个copy-like点的41532点诱导子图D≤5。把这176点之间的所有边先删掉，每个点即为核心原型的普通twin，Lemma2.2给完整D5保证；当前多余边只会缩距。因此不需要猜它们的几何类型，也不需要它们组成完整H3-blowup。41532只是当前已知图内的一块覆盖证书，不是新下界，也不主张是能由这类证书识别的最大子图。

## P_star：完整core star的宽包含分类

在执行前以 `P_STAR_PREDICTION.json` 冻结预测：986个current extras中至少643个不含任何完整core star（star-containing至多343）；343为root提供的bare-core clone-packing上界，本代理没有重求该优化。

对每个A_i=N_current(i)∩K，实际检验的是 **存在v∈K使N_K(v)⊆A_i**，不是A_i⊆N_K(v)。因为core无孤点，任何合格v都属于∪_(a∈A_i)N_K(a)，先取这批候选再逐个subset检查即可；最大候选集合实际131点，理论最多144。所有986点、所有候选原型均保留，不只取首个。

结果为：**star-containing176，恰好等邻接176，严格超集0，non-star810**。多原型点数0；176点各有唯一原型，810点没有任何原型。P_star被实际分类确认，强于至少643的预测。即使允许额外core anchors，这810点仍不具备由任何单个完整core star直接继承的普通twin证书；但不据此识别其pencil几何或断言它们没有其他D5机制。

代表：extra41356的A_i={8214,8645,9055,10197,10854,11511,40951}=N_K(0)。字典序首个non-star为41502，A_i={7,4212,8259,12377,12453,19260,19421,25736,26058,36805}，103个候选原型全部subset失败。严格超集类别为空，没有虚构代表。

若每个star-containing点各选一个完整star，把额外anchors和new-new边都忽略，便得到bareK普通clone模型的可行子结构；core上的degree负载不会增加。因此extra anchors/new-new边不会绕过root的343 packing上界。本次只检查结构包含，不做新packing、距离或候选优化。`star_containment.json`保存全部986记录和分类，CPU0.190848秒。

## 旧280copies哪些能结构对应，为什么不能只看N_core

旧280 H3 copies及旧63普通twins的N_core均等于某个core原型邻集。当前有158个点的signature匹配旧280某一signature，按signature的供应数量最多配对158个旧copy，122个旧copy没有**完整相等signature**候选；旧63普通twins的signature在当前extras中均未再出现。这排除了固定共同核心identity下原样诱导保留整个旧附加区的说法，不能排除允许更多core边的非诱导embedding或重新配置copies。

即使配对这158个旧copies，也必须检查实际tail-tail邻接。按各signature内旧、新编号排序给出一个明确对应后，158点之间仍有6个邻接不匹配，故不能宣称158个旧copy图已原样保留。具体缺边与映射全部在`structural_classification.json`。在当前所有176个copy-like点之间，完整clone-blowup预期223边、实际214边，缺9边而无额外边；这同样不能只从N_core等同推出完整blowup身份。

只从这份已计算的6条mismatch清单排除后号点42276、42277、42279、42280，即得一个**154个旧copies的明确诱导对应**：共同核心固定，旧selected copies的全部core与tail-tail邻接都与当前对应点一致，合计41510点。它不是最大embedding搜索结果，只是可检查的保留子结构。更大的普通twin覆盖证书41532已在上一节直接成立；两者回答的问题不同。

tail-tail缺边不构成这些176点的D5失败，因为普通twins本来不要求new-new边。它们只阻止“完整copy-blowup/旧附加区原样保留”的过强结构声明。

## 42177与最后165：来源事实和编号假说分开

作者metadata对42342的原话结构是：先有closed split set、H3 copies和pencil vertices的partial-fold来源，再“further165 vertices”以旧空余度邻居的R4球覆盖加点。**这165个不能直接称为165 pencils。** README没有补充当前S、copy数、pencil数、逐点类型或邻接规则。

对current数值末165点作切分，实际得到前42177点243411边、跨切分1805边、末165内1边(42280,42314)。这个数值切分与作者追加数量相符，但没有作者ID-stage映射，故不能仅凭“末165”将其逐点类型认证。前42177比共同核心多821点，这821点也不能认定为“旧343原样+478pencils”。

## 原pencil规则仍缺什么

1. 每个pencil的几何对象、参数、中心，以及对split/merged/H3点的邻接公式和额外anchor规则。
2. closed split set的作者精确定义。旧partial-fold的degree负载闭包不能自动替代这一定义。
3. current986的类型/原型/anchor witness及与旧280/63的重标号或替换关系；当前附加区的几何身份不能由数值label继承。
4. pencil对共同核心及任意两pencils/其他extras的D≤5证明。旧Theorem5.1/5.2和普通twin lemma没有为不满足其邻接前提的点自动担保。
5. 若最后165采用逐步R4覆盖，需实际添加次序及针对每个earlier graph的覆盖证书；作者一段概述不是已完成的本地核验。

本次没有重取原文、全源/多源BFS、R4 domination、greedy、packing或局部修补。一次边比较CPU1.048746秒；新增结构signature与明确对应核对CPU0.684849秒；后续154子结构只复用已保存mismatch元数据推得。报告不能被解释为固定41636核心的63额外点上限限制任意H3-copy重新配置。root据共同D5核心和已完成P_star分类选择后续整体覆盖规则，本任务到此结束，不自动优化。

## 文件

`adjacency_comparison.json`保存全部边集/分段计数；`current_extra_signatures.json`保存986个点的N_core、唯一或缺失原型、旧signature对应和extra邻居；`structural_classification.json`保存实际tail-tail核对及154点显式映射。`compare_existing.py`和`classify_existing.py`仅为本次只读结构处理。`RESULT.json`汇总严格结论及未闭范围；`P_STAR_PREDICTION.json`和`star_containment.json`保存新增冻结预测与宽包含分类。
