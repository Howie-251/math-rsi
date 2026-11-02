# P33与原50-spread在filled160050源上的接口

> 实际数据更新：producer已取得33点集合，本代理新集合／center-binding独验实际PASS。仅检查新528点对及1650个small-data邻域，0大边表／旧geometry／BFS／Lean重跑；实测0.071535943CPU。完整目标图仍未在本scope生成或验收，以下161700／169950仍是待生产端点。结果见[INTERFACE_RESULT.json](INTERFACE_RESULT.json)。

**任意实际W(3,7) partialovoid P33都适用，无需额外的特殊位置或与旧O22相容。** 这里继承的泛型定理已经给出结论：`OvoidSpreadCloneCapacity.adjacent_centers_unique`只用每条线至多一个所选点，以及每个点至多属于一条spreadline，没有把点集大小限制为22。本note不把这个已有定理重新算作成果；只明确filled source的bonus分配和本次33点数值预测。

本次源图必须是已接受的原160050点、5121600边、全64正则图。它包含160000个旧(p,l)点和50个既有fill点f_j。不得改用未填充的160000源，也不得取O22扩张后的161150或166650图的当前邻域。

## 旧结构与实际fullN64

固定旧标签为400p+l。旧图中(p,l)与(x,m)相邻，当且仅当p∈m、x∈l且二者不是同一顶点。原flag p∈l的旧度63，非flag旧度64。

原第j个fill点f_j（标签160000+j）只连以下64个旧flags：

    {(x,m):x∈L_j且x∈m}。

spread按原GF49 slope顺序保存，不能另按lineID排序。它把全部400points分到50条线，每点唯一owner。因此filled source中每个旧flag恰增加一条fill边，全部点均为64正则。

现在选center c_(i,j)=(p_i,L_j)，i=0..32，j=0..49。每个p_i在唯一spreadline上，所以1650个centers中恰33个是flags、1617个是非flags。其immutable sourcefullN分别是：

- flagcenter：63个旧邻居，加原来的一个fill邻居f_j，共64；
- nonflagcenter：64个旧邻居，没有fill邻居，共64。

这些fill点是原160050源的一部分，不是这次新添clone，也不是可重新分配的bonus。

## 为什么所有pins仍两两不交

对旧点w=(x,m)，若它邻接某个center(p_i,L_j)，则p_i∈m、x∈L_j。partialovoid保证m上至多一个p_i，spread保证x只对应一个j，所以w至多邻接一个center。若该唯一候选恰是w本身，旧selfpair被排除，不会产生第二个owner。

对原fill点f_k，邻接center(p_i,L_j)同时要求p_i∈L_j、p_i∈L_k。spread的唯一性首先强迫j=k；partialovoid再强迫L_k上至多一个p_i。因此f_k也至多属于一个center的fullN。

特别地，P33的33个点自动落在33条不同的spreadline上。这不是额外transversality条件，而是partialovoid性质对这些isotropic spreadlines的直接结果。恰33个fill点成为pins，其余17个不被使用。任何33点的普通cap或坐标列表都不能冒充此条件：必须是当前实际alternating form下任两点不共isotropicline的partialovoid。

于是1650个fullN64两两不交，pin总数为105600，精确分成

    old160000部分：33·63+1617·64=105567；
    originalfill50部分：33；
    合计：105600。

另一个数值解释是P33占据264条不同的GQ线，每条对应400个可能旧点owner，但33个flagselfpair排除，得到264·400−33=105567。整个160050源的基负载为1的点有105600个、负载0的有54450个。

centers本身不必独立。事实上该product中心诱导528K2加594个isolates；旧proof与本次fullN lemma都不要求centerindependence。实际生成不能改为复制“扩张后当前center全部邻域”，否则会引入其它clone及新的度数账；必须始终取immutable原160050源fullN64。

## 两个已指定端点的条件性数值

若只复制一次1650个centers，使用全部原5121600边并添105600条new-old边、0new-new边，则条件目标为：

    (65,3),n161700,m5227200；
    degree65:105600，degree64:56100。

若每个center复制六次，同一原fullN使用六次，共9900个新点、633600条new-old边，则条件目标为：

    (70,3),n169950,m5755200；
    degree70:105600，degree64:64350。

新标签可保持copy outer、point outer、spread inner，即160050+1650copy+50i+j。所有新点度64。每个原pin的总增加量分别为1或6，不会因原center中存在相邻对而额外收费。已有immutable-fullN路径引理继承sourceD3，并给每一步当前完整图的R2pin覆盖；路径内部只用原source点，不依赖未来clone。旧walk-collapse也保留nonD2。

与root更新后的公开保证161650／169900比较，两者条件差值都仅50。这些是待实现预测，不是已经生成的图或已认证全球纪录。

## 实际33数据到来后的限定核验

只检查新集合及新接口：33个distinct点标签属于原400point序；对新528点对用原已接受Gram form确认非零；从原小incidence/spread数据确定33个不同owners、1650orderedcenters及其fullN64，并核105567old＋33fill、load≤1。该核验不重建400点geometry，不重读5121600边表，不重跑旧field、BFS或Lean，也不搜索另一个33集合。

本次实际33集合现已通过独立新数据核验：33个标签与坐标匹配原400序、528对原Gram值均非零，264条线各含一个所选点、136条为空；33owners全异。1650个fullN64实际小数据绑定给出105567old＋33fill的105600distinctpins，全部数值预测支持，center诱导图也与528K2＋594isolates一致。

证据为INTERFACE_RESULT.json、INTERFACE_SELECTED_PAIR_VALUES.tsv、INTERFACE_ORDERED_CENTERS.csv和INTERFACE_PINS.tsv。旧O22与原图证据保持不变；该partialovoid为公开33点目标的复现，不计新纪录。任何后续完整图生产、独验、具体Lean及公开比较仍另行记账，不能把这份接口PASS冒称新完整图。
