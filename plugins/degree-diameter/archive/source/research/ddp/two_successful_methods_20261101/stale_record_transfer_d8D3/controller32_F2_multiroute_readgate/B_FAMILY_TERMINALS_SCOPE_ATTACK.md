# B线C32/C33两族终态：有限只读scope收束

本文件只读两族代码、既有PRED/PAPER及actual结果；不重跑data reduction、controller/参数、ordinarywalk DP、matrix/field、图/BFS或solver。C33 postprocess只读已保存报告，不再次统计100行。没有发现下述两个明确范围的否定缺口；两者强度不能混同。

## C32：完整插边族的任意≤2choice／8fiber规则NO

原两chart检查的参数域已绑定：378450 raw，284310 simple、94140非法。随后 `base_capacity.cpp`只读已存tail行，对root30以`cur30=total30=1`开始；每步逐四port累加`2*cur`，共三步，并加到total。这精确实现普通controllerwalk的容量`sum_(l=0..3)2^l W_l`，包含0步/立即回退，无matrix或pointimage。每typedstep至多两个实际输出使真实target数≤此容量；碰撞只会使上界宽松。

actual BASE_CAPACITY_RESULT：284310全数，root30最小容量0有283388个、4有907个、8有15个。因此前284295已拒；15只是root30必要门幸存，不能提前称全族NO。

CAPACITY_SURVIVOR_RESULT随后逐条保这15个tails，仅各追加root31一次，root30不重复；每条minimum均0，firstbad有些先遇容量4，不与minimum0矛盾。全局survivor为空。结合完整域和同一必要不等式，足以严格关闭本C30→C32插边族的**所有uniform8fiber、每typedcontrollerstep至多两个输出、路径只投影到该controller邻接的lift规则**，包括edge-local/nonlinear，非仅ARC/R。

不能把这统一结论改称“每个C32的base都D>3”：907个root30 min4来自正容量但数量不足，当前未给它们全root的base-projection否定。C32整体支持的是≤2choices负结论；更大每arc分支、非uniform fibres、其它C32或其它拓扑不在结论内。两stage累计5.174706358/30是原receipt，本文不新增数值，也不为closed controllers再搜chart。

## C33：三type/C11规范域与三roots

实际controller由 `(tau,j), j∈C11` 给出，A:0j→1j→2j→0(j+p)；B:0j→2j、1j→0(j+q)、2j→1(j+r)，其余ports取真实inverse。每port改变type所以无loop；四邻不同恰要求p,q,r都非0。当前simple族不包含zero参数导致的重复port邻点模型。

共同平移`(tau,j)->(tau,j+c)`保持全部typed边，故三个type根0、11、22代表所有33个source vertices；不能未经证明把types也合成一根。单位缩放`j->lambda*j`把(p,q,r)变成(lambda*p,lambda*q,lambda*r)，保portlabels；取lambda=p^-1可规范p=1，q,r非0的100项覆盖整个非零三参数simple族，不要求100项彼此非同构。

`run_once.py`为每参数实际构造这些ports并检查simple；words保全部长度0..3，不删basebacktracks。对三个root都完成controller endpoints的reachable set，并各保存root_summaries；即便第一fiber坏cell已找到，后两root的summaries仍照常计算。故这份saved数据确可用于新的base-projection判定，无需另跑controller BFS/word。

原RESULT固定ARC100全NO、self fibres全8通过；`first_bad_is_projection_count=43`只说43项的**第一个fiber坏cell**恰无base route，不代表只有43个controller D>3。新的 `PROJECTION_POSTPROCESS.json`明确saved_rows100、controllerD3survivors0、max(minimum of three type reaches)=32。也就是每参数至少一type root的≤3 base可达数<33；不是说所有三roots每一项都<33（部分分量可为33）。这与原firstbad43不矛盾。

因此这100个规范controller及其全部非零p/q/r原像的base本身都D>3。若一个非空lift的每个controller fibre均有点、每条边投影为该controller边（或在同fibre内停留），投影路径不长于实际路径，故base的远对不可能被lift在3步连接。这严格排该**固定三type/C11拓扑族上的任意surjective projected lift**，不受ARC/R、线性/非线性、fiber大小或choices数限制；但不排另一个C33拓扑、允许跨非邻controller的新边、删掉base fibre的子图或一般8D3图。

本强结论来自已保存controller reachable数据，不能反过来写成原100项在当时就证明了所有charts。原self/fullrank三角局部成功照实保留，不是完整264图；actualgraph/BFS0。postprocess所报case5.653785158包含root整理，本文未重算。

## 当前处置边界

可以分别接受C32任意二choice/8fiber完整NO，以及C33该三型C11 controller的projection完整NO。不能把C33的更强“anylift”无条件套到C32，也不能因任一局部修好就开第二chart/拓扑窗口。所有数值已terminal，0新图/参数/Lean，153/43/47不变；root将另存ROOT/FINAL和下达Wiki任务，本文件不写这些根文件或Wiki。
