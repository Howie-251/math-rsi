# Natural364固定四corepins：nested Hall门与全两cut域终态

状态：只读 `JOINT_PORT_INTERFACE_READ.md/json` 后作paper推导；没有新source/距离/球、匹配数值、BFS或solver。root随后给出的fixed/global actual摘要在下节单独标为有限数据，不冒作本paper重新计算或新的抽象几何定理。

## 1. 沿用精确mate接口

源为自然H3 polarity364/714：28个degree3ports、336个degree4core，ports互距5，28个闭R2类恰partition364。固定P为两条不交core-cut的四端点，T=G−两cuts。加newz邻P，ports添任意perfectmatching M。

记α(b)=d_G(P,b)，holes为d_G(P,t)>4的targets。每hole有唯一R2 owner b，β_b(t)=d_G(b,t)≤2。已有exact接口给

    hole t可达newrootR5 iff α(M(b))+β_b(t)≤3。

令D为有hole的owner ports，β_b=max_(该类hole)β_b(t)，τ_b=3−β_b∈{1,2,3}；F为无hole的ports，其mate无约束。互相允许的边为 `α(a)≤τ_b且α(b)≤τ_a`；对F一端把其τ视为∞。这仅certifies newroot全覆盖，旧旧D5另有义务。

## 2. 有hole的owners彼此不能作为mate

取实现β_b的hole t。三角不等式给5≤d_G(P,t)≤α(b)+β_b，因此

    α(b)≥5−β_b=τ_b+2。

若两个demand owners b,c允许互配，则α(c)≤τ_b且α(b)≤τ_c，结合上式会同时要求τ_c+2≤τ_b和τ_b+2≤τ_c，矛盾。因此D在允许图中是independent；所有需求必须由无hole的F提供mate。

这也避免了把一般非bipartite matching错误套Hall的风险：本实例确实先变成D→F的二分需求覆盖，配完D后剩余F没有约束、形成clique，可任意补完。无需枚举完整28port匹配。

## 3. 三个nested Hall计数其实是newroot matching的充要门

令N_k={a port:α(a)≤k}，k=1,2,3。D中τ为1/2/3的可选mate集分别是F∩N1、F∩N2、F∩N3，三者nested。故Hall全部子集条件化为

    |{b∈D:τ_b=1}|    ≤ |F∩N1|，
    |{b∈D:τ_b≤2}|    ≤ |F∩N2|，
    |D|               ≤ |F∩N3|。

必要性由每个集合的mate必须互异；充分性按τ从1到3依次分配尚未使用的nested resources。剩余F数=28−2|D|是非负偶数，且任意两F互允/原ports无旧边，所以能补成perfectmatching。

α(a)≤2时，其整个R2类距P≤4，故N1、N2自动属于F；前两右侧可直接写|N1|、|N2|。N3未必全在F，第三行不能盲用全部N3冒充分性。最先一行就是root需要的简单必要门：每个**β2-hole owner**须匹配一个不同的nearport N1。

## 4. 两corecuts使nearports天然至多2

每个corepoint至多邻一个port，否则两ports距离≤2，违反距5。对一条core边u–v，若其两端邻接不同ports a,b，就有a–u–v–b三步，也违反距5。因此一条core边的两端合起来最多贡献一个nearport；两条corecuts的四端点P于是满足

    |N1|≤2。

这个上界只用ports距5与core-edge关系，不需要新球或计数。本推导没有进一步推出β2-hole owners至少21或uniform>4；当前停止依据采用source实际R4完整数据，不强求另立几何下界。不能将一个fixedP的24个hardowners外推成所有P的几何定理。

## 5. root实际fixed/global数据怎样给严格停止

root报告 [joint_fixed_first_P/RESULT.json](joint_fixed_first_P/RESULT.json)：P={43,58,151,314}的四R4各148，union留下72 holes；24个owner类有β2-hole，而N1只有port126。Hall24>1排此固定P的全部portmatching，非随机样本失败而已；没有旧旧阶段。

随后root一次完整 [all_two_corecut_Hall_gate/RESULT.json](all_two_corecut_Hall_gate/RESULT.json) 处理全部**196371个disjoint corecutpairs**：β2-hole owner数量范围21..27，near数量0..2，实际joint最小差h−n为20，0幸存。21..27与差20在此明确是完整有限数据，不是本paper新推的普遍几何下界。新332个coreR4加复用原4个构成完整support，不重sourceD5、28portballs或旧root验收；matching枚举无需执行。

每个cutpair都违反第一行Hall必要条件，故严格排**固定自然364源，删任意两条顶点不交core-core旧边，newz连全部四端点，28ports任意perfectmatching，其余不变**的整个规则。它会有365/730全4度，但newroot不可能R5全覆盖，因此不用追加旧旧BFS才能拒绝。旧10000个独立随机matching样本的UNKNOWN历史保留；新的完整Hall域是随后更强的实际停止依据，不改旧样本成“当时已穷尽”。

global case累计3.763081991/20CPU（含原fixed/read/prep），本paper不重算或新增数值。这个No不排shared-endpoint cuts、portcuts、第三cut、额外oldoldrepair、多helpers、另一个公开4regular364源或一般365/(4,5)。root已要求停止，不以剩余预算扩第三cut/其它source。
