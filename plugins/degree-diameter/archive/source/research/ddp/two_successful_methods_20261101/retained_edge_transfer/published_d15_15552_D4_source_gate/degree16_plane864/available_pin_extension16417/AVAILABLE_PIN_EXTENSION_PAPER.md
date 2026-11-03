# accepted16416 可用pin单点扩张：真Walk与exactD4接口

状态：条件纸面接口确认，数值owner另做唯一覆盖case。本文件不计算球、不读取完整图、不枚pin或运行solver，不编译旧/新Lean、field或BFS，不把尚未返回的cover当命中。

## 1. 真正可复用的旧source声明

实际source是已经接受并完整kernel闭合的16416图，不是重新证明15552源，也不是将未完成fullpacking当新source。缓存模块

    DegreeDiameter.Portfolio.F3Graph15552Clone16416Exact

namespace `DegreeDiameter.Portfolio.F3Graph15552.Clone16416` 实际给出：

    card_vertex : Fintype.card Vertex = 16416
    degree_le : ∀v, graph.degree v ≤16
    diameterAtMost_four : DiameterAtMost graph 4
    not_diameterAtMost_three : ¬DiameterAtMost graph 3
    final_claim : FinalClaim
    original_concrete_goal : card=16416 ∧ degree≤16 ∧
      (∀u v,∃w : graph.Walk u v,w.length≤4) ∧ ¬DiameterAtMost graph 3

其中 `Vertex=Fin15552⊕Fin864`，`label : Vertex≃Fin16416` 来自已闭Definitions。它不是盲假定carrier本来就Fin16416。原FullNeighborhoodClones/source/field/coset等既有 `.olean` 只import，不重编。actualgraph/role与原simpleN绑定入口是本case既有 `formalization/FINAL.json`、`EXTERNAL_BINDING_RESULT.json` 与root接受回执。

## 2. 命中所需数学条件及degree账

令 G 为该accepted graph，S⊆Vertex是**当前图**中不同可用pin组成的集合：

    |S|≤16，且每个s∈S满足deg_G(s)<16；
    ∀v，存在s∈S及真实G.Walk s v，长度≤3。

第二条是闭R3覆盖，pin本身允许0步。当前可用点不限原15552source中的旧点，也可包括864个clone；它们都必须用accepted16416当前degree和当前邻接，不能套原source余度。既有actualfinaldegree14:126/15:3924/16:12366，故all-available集合4050；该统计继承，不重算。

新增一点Z，只连S，保留G全部旧边、无其他修改。新Z度恰|S|≤16；每个pin度加1后≤16，其余度不变。点数16417。若pinset为空不可能覆盖非空source，因此实际覆盖条件也保证新点与source相连。newdegree及olddegree等式是简单neighbor-set分拆，不需要旧field/geometry输入。

## 3. 现成SingleExtension的精确签名

`formal/DegreeDiameter/Portfolio/SingleExtension.lean` 已有通用定义/定理（文件开头历史注释提D5，但以下general theorem并不限D5）：

    singleVertexExtension (G : SimpleGraph V) (pins : Set V)
      : SimpleGraph (Option V)

其 `none` 是新点，`some v` 是旧点；旧旧边恰G，none只邻pins。还定义

    PinsCoverRadius G pins r :=
      ∀v,∃u∈pins,∃p : G.Walk u v,p.length≤r

以及

    singleVertexExtension_diameter (G) (pins)
      (hdiam : DiameterAtMost G D)
      (hcover : PinsCoverRadius G pins r) :
      DiameterAtMost (singleVertexExtension G pins) (max D (r+1))。

直接取D=4、r=3、hdiam=`Clone16416.diameterAtMost_four`，得到真实全点对Walk≤4。新旧对由一条star边加旧≤3 Walk，旧旧对沿G旧Walk不变，逆向用Walk.reverse；不需要再跑旧D4验证。

如果数值命中返回一次multi-source parent/depth证据，可复用同文件：

    ParentDepthCertificate G pins 3
    parentDepthCertificate_sound cert : PinsCoverRadius G pins 3。

四个字段义务是 `depth≤3`、`depth=0⇒pin`、非根parent与本点有真实G边且depth减1。它给genuineWalk，不能拿外部布尔cover或JSON值当Lean theorem。命中后的新有限证据只需绑定到当前graph和label，不重旧source/field/kernel。

新carrier可用 `Option Clone16416.Vertex`，显式label给 `some v↦Clone16416.label(v)`、`none↦16416`，由旧label双射与Option分类证明到Fin16417的等价。无需猜未读取的库equivalence名称，也不能误把newnone编号0而与实际新点16416冲突。

## 4. exactD4不能无条件沿用旧nonD3 witness

本单点扩张是任意available pins，不是fullN clone。一般没有从扩张图到G或原15552图的collapseHom；新的Z可缩短旧旧距离。旧0/81或其他nonD3 witness可能因pins新增≤3路线，不能直接借旧 `old_walk_bound_iff`/nonD3结论。

但当前order与degree给独立且充分的数学lower bound：最大度16、直径≤3的简单图满足Moore上界

    N≤1+16+16·15+16·15²=3857。

16417>3857，故任何满足上述degree账的扩张图都不可能D≤3；与真Walk≤4合起来即exactD4，不依赖旧witness避pin。甚至宽松ordinary-walk计数界1+16+16²+16³=4369也足够，但本次未为其新增或编译定理。

当前project的 `DegreeDiameter/Moore.lean` 是旧degree8/D2专用接口，不能未经核对直接当generic16/D3 theorem使用。因此cover若命中，完整具体Lean还需一个新的小通用层数计数lower lemma，或给新图真实不经短路的nonD3证据并kernel化；不能宣称该lower部分此刻已闭。它不需要重旧field、coset或fullsource。最终仍须原无前提FinalClaim与独立Audit/std3，不能把cover条件保留给用户。

## 5. 当前边界

纸面确认：available且≤16的全current-R3 pin cover命中，足以构造16417/max16/exactD4候选。它是此前成功单点R_(D−1)覆盖机制在accepted16416上的新实际输入，不把通用引理另记原创定理。当前只准备接口，不启动任何求解或新Lean；若sole数值owner命中，优先实际候选/新proof，不另开负定理或API探测。没有命中回执之前，图/参数/Lean增量均0。
