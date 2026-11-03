# actual3645 单 cut + 最大可用 star：纸面接口

**支持指定规则，尚不判历史是否已关闭。** 沿用源max11、7个degree10 free点F、其余点degree11、D≤4及旧 `closedR3(F)` 覆盖2902/缺743的实际事实。本文件不parse源、不枚cut、不计算球/BFS/solver；同scope历史由唯一readgate owner核对，若已有完整NO须继承停止。

## 度数与重叠没有漏洞

删除一条实际源边e={u,v}，令 `P=F∪{u,v}`，添新点z连全部P，其它旧边不动。设 `k=|{u,v}∩F|∈{0,1,2}`，则 `|P|=9−k≤9<11`。

- 原degree11的cut端点变10再加一条star边，恢复11。
- 原free的cut端点变9再加一条star边，最终10。
- 其余free从10变11；其余旧点不变。

所以端点重叠时依然simple/max11，不应重复添加已在F内的pin。新order3646，边数是 `m_source−1+|P|`；没有声称新图正则。

## 新根的精确门

记T=G−e。被删边的两端都在P，故 `d_T(P,t)=d_G(P,t)`：最短多源路径若经过cut，可从下游P端重启，去掉其更长前缀。因而

`d_(new)(z,t)=1+d_T(P,t)=1+d_G(P,t)`。

新根R4当且仅当源 `closedR3(P)` 覆盖全部3645。用旧缓存的缺集 `D=V(G)\closedR3(F)`（743点），此门恰为

`D ⊆ closedR3_G(u) ∪ closedR3_G(v)`。

若u、v都在F，P=F，旧缺743直接排此edge；若只有一端在F，只多一个球。这里无需把任意子star的距离也错误替成源距离，重启结论仅针对含全部cut端点的最大P。

## 为什么最大P支配整个单cut子规则

固定e，只允许删e并加一个z及z-old边、保持max11。删边后唯一可接受新spoke的旧点恰为F与cut端点，所以任何合法邻集S必为P的子集。由于全部P仅7..9点，最大star本身也合法。所有这些S图都是最大P图的同顶点子图；添边不会增大距离。因此若最大P图在新根或旧旧处失败，此edge的所有子star都失败。这个支配不包含其它旧旧repair、其它删边、额外helper或换源。

## 旧旧必须独立检查

源G的D4不能直接当成删边host T的D4。精确地，令 `r(a)=d_T(a,P)=d_G(a,P)`，则对旧点a,b有

`d_(new)(a,b)=min(d_T(a,b), r(a)+2+r(b))`。

最短路或完全在T内，或恰访问z一次。旧G中distance≤3的pair删一边后经star替代至多加1，仍≤4；潜在损伤在distance4且依赖cut的旧pair。新根满覆盖不证明这些pair安全，必须由实际候选旧旧检查或等价完整证书处理。此处不借FullN retraction、旧保边SingleExtension theorem或degree2 subdivision的NO。

旧保全部旧边、仅用F的扩张NO，依据free球缺743；本规则通过删e释放原满度端点，已改变该关键前提，不能套旧NO。反过来，若历史实际已完成同一单cut最大star域，本paper也不授权重跑。后续所有数值须root另行决定；本次新增图/参数/Lean/数值批均0。
