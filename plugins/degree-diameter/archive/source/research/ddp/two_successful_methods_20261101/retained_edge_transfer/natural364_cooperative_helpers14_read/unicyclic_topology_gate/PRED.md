# 自然364的14helper保边扩张：仅枚抽象单环拓扑的必要门

继承旧k1..13完整NO，不重跑3276/81900 masks、196371 Hall或sourceBFS。新纸面分析也关闭k14 tree：28spokes后2总空槽使每叶≥1port，helper tree diam≤4，中心4枝/第二层9叶必有3叶满枝；其parent/centre均无port，外国叶单元只能靠own≤3端口R4，旧good(T)=∅排除。

故k14若存在，只剩connected simple unicyclic H，14edge，每helper总degree4，oldspokes a_h=4-degH(h)，总28且每旧freeport用一次。

真实路线必要门G1：所有helper h到每个owner w(a_w>0)的H距离≤4。old-host跨两freeports需5旧步，加进出≥7，不能为≤5路线缩短H。

缓存给更强G2：若leaf ℓ的parent Hdegree≥3，则parent最多1个oldport，leaf自身3port T。若任何owner w在距ℓ=4处，其旧R2-cell interior除leaf R4(T)+parent R3(p)外无其它出口能供应；其它距≥2出口的R2/R1均困在各自不相交cell，w只供应旧port本身。旧good(T)=∅/good(T,p)=∅因此排除。故这种leaf到所有owner须≤3。parent度2(有2ports)不能偷套此门。

预测：G1加G2已排全部14-unicyclic maxdegree4拓扑。若有survivor，预测被推翻，保拓扑供具体28端口assign分析，不声称存在图。

完整有限域：每unicyclic图有唯一cycle c。挂树leaf距farcyclevertex为depth+floor(c/2)，故depth≤4-floor(c/2)。c≥10被G1排；c8/9不能挂树且不足14；只c3..7。每cycleroot最多2children、其它树点最多3children。按canonical rooted-tree children multiset枚所有深度合法挂树，cycle decorations按旋转/反射规范，强制总14。此为全无标号拓扑域，不是抽样树。

新数值只一次Python小枚举，CPU8秒硬限，wholecase10CPU，继承read.5、准备.25；返回各cycle raw14decorations/canonical拓扑/G1/G2拒绝及幸存adjacency，全部候选记录。无portassign、sourceBFS、ball、field、graph378、solver、Lean或ARIS。0survivor只闭fixedhost/k14/保全部oldedges/无新增oldold范围，不排更多helper或一般(4,5)。无自动k15梯。
