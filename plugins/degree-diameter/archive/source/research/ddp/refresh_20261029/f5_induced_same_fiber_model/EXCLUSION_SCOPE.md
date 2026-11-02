# 固定3750图的诱导16度目标已计算排除

## 精确命题

令G为../f5_full_d20_D3/PARAMETERS.json定义并以graph_d20_D3_n3750.edges保存的既有成功图。不存在顶点子集S，使诱导图G[S]同时满足

    |S|≥1921，maxdegree≤16，diameter≤3。

此处不固定|S|恰1921，不要求整fiber，不要求每层同大小或对称。只排这张固定图的诱导顶点保留；不是一般N(16,3)上界，也不排改边、换参数或换源。负结论尚未Lean形式化。

## 从合法诱导图到CNF的保全链

1. 每个源顶点有独立keep变量，合法诱导图按S赋值。原20个邻点中至少4个删除的条件与最大度≤16等价；精确二进制求和给阶数≥1921。原编码见../f5_induced_retention_closure/prepare.py。
2. 控制距离3唯一词的端点若保留，则原唯一真实路径的内部点必须保留。left OR5/right OR25及32250压缩条件为必要关系，正反词均存在。
3. 真正D3支持对129条Horn规则闭合。完整24575闭支持中，三16支持控制距离失败、三19支持用四条不交external坏边的125密度界得阶数≤1875。故目标全部30层非空；该条件未强迫whole fibers。
4. 全部external共享中间点关系是精确局部距离条件，keeper与provider分别用两条OR子句编码。与前项共同继承原315221/1290903模型；该旧模型自己的UNKNOWN不用于本次排除。
5. 同层全部232500个无序端点对的所有二/三步路线已明确枚举，完整距离条件由930000子句表达，未选择性截掉替代路线。二步存在时复用旧exact OR5，三步两个AND按分配律无损展开。
6. h_a与每层保留点数≥65精确双向绑定。H65证明高高external边迫整线及T_p运输；全30层高会与度≤16和字面矩阵方向冲突，故至少一层低。总点数≥1921又迫至少一层高。相应95792新增子句只增加已证必要条件。
7. 所有辅助变量都按exact gate可扩展赋值，因此任一目标S将导出最终333551变量/2316695子句model.cnf的满足赋值。root读过各生成器及逻辑对应；H65与支持几何有实际静态跨模型审阅。数学推导和枚举实现的证据分别保存，没有把审阅意见当作求解证明。

源邻接缓存与已验完整边表的全部75000有向邻接项已直接比较一致，见SOURCE_CACHE_BINDING.json。这是新负结论的对象绑定，没有重做原3750根BFS。

## 不可满足证据

发现调用返回rawUNSAT后，只做一次带LRAT的原样CNF再现。CaDiCaL以同一个model.cnf输出证书，独立lrat-trim读取该CNF和证书返回20并输出s VERIFIED。准确命令、PID、CPU、输出均在lrat_certificate/RESULT.json及checker.stdout；证书在certificate.lrat。

因此最终CNF不可满足。与上述必要性链合用，排除精确命题中的S。发现阶段54.406117 solver CPU，认证含独立检查62.004200 CPU，组合whole119.899129 CPU；未修改旧终态，未做第二次重试。

## 依据与停止决策

支持/密度/shared原理见../f5_induced_shared_routes_model/DERIVATION_PACKAGE.md；H65与高低范围见../f5_partial_line_occupancy/PROOF.md；同层完备性与编码见ROUTE_CLASS_PROOF.md。两份实际审阅在reviews/ddp/f5_induced_support_shared_20261030及f5_H65_route_classes_20261030的response/disposition；后一回复的正反组数量措辞已在disposition纠正，实际22500组已经含两向，编码始终未重复加组。

停止在该固定G上继续删顶点、调整各层点数、换保留seed或增加同类求解时间。保留可迁移的共享路线/H65认识。若继续研究16度，必须实际改变源图或边规则；仅把uniform75的external charts改成保平面运输也被两条短词最多50点的局部障碍阻断，准确范围见PROOF第7节。其他参数的研究不受这个固定源排除限制。
