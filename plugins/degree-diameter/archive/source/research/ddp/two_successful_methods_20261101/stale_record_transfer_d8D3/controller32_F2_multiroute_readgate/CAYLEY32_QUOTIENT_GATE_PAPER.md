# 32点controller：两个global inverse-pairs的商过滤

状态：纯paper生成规则过滤，0controller选择、word枚举、群列表、source/field/BFS、solver、Lean或网页。当前32点controller尚未实际绑定，不能从“32点/4端口”臆定其为下述Cayley模型。

## 1. 条件命题与所需假设

设controller真为Cay(G,{a,a^−1,b,b^−1})，|G|=32，a,b是两个固定global generators。假定有surjection

    φ:G→C2²，φ(a)=(1,0)，φ(b)=(0,1)。

从identity走≤3步，落kernel的word必须使a类与b类出现次数都为偶数（逆元在C2²中有同像）。所以奇长1/3不可能；长度2中混用a/b也不可能。全部可达kernel元素只可能是

    {e, a², a^−2, b², b^−2}，至多5点。

但kernel有32/4=8点，故至少3个kernel点距identity>3，controller不能D≤3。回退只产生已计的e，generator involution或square重复只会进一步减少点数；没有通过抽样或枚完4³words推结论。

## 2. 非循环二生成有限2群自动有该商：自含证明

先证任意finite2group的maximal proper subgroup M都normal且index2。让M左作用于G/M的left cosets；所有orbit大小为2的幂，故fixed cosets数与偶数[G:M]同parity。至少有identity coset固定，于是fixed cosets至少2。fixed cosets恰为N_G(M)/M，故normalizer严格大于M；由maximality即N_G(M)=G，M normal。商G/M若order≥4，取任一nonidentity元素的适当2幂得到order2元素，其子群proper/nontrivial，与M maximal矛盾；故index2。

令Φ0为所有squares与commutators生成的normal subgroup。每个index2 maximal quotient都会杀掉它们，所以Φ0包含于每个maximal M。商V=G/Φ0是F2-vector space；a,b生成G使dimV≤2。

若dimV=0，则G=Φ0⊆某proper maximal M，矛盾。若dimV=1，选a或b中有非零像者g，则G=⟨g⟩Φ0；若⟨g⟩proper，可放入某maximal M，同时Φ0⊆M，又迫G⊆M，矛盾。因此G=⟨g⟩cyclic。

所以**非循环、由a,b生成的finite2group必有dimV=2**；a,b在V中的像自动为basis。对order32正是第1节所需C2²商。不需要查32阶群数据库或引用未证明的Frattini/basis库定理。若a,b根本不生成G，controller已不连通，也不能D3。

## 3. 循环例外也不构成继续group32梯的入口

循环G中a,b交换，任何≤3word都可整理为a^m b^n且|m|+|n|≤3。此整数菱形仅有1+4+8+12=25个指数对，实际images可能更少，故不能覆盖32点。这是符号计数，不是新增word/群枚举。

因此固定32点、两个global inverse-paired generators这一接口，在循环和非循环finite2group两种情形都不能给controllerD3。无需再逐群32换参数验证同一规则。

## 4. 精确未排范围及multiroute关系

此门不排未满足C2²商/指定生成接口的其它order、非Cayley32图、状态依赖reverse标签、或不同的全局端口结构；尤其不能将结论误称为“所有4regular Cayley32图都不行”。degree4的其它inverse-closed生成集未必只是两个global inverse-pairs，本paper没有将它们WLOG归入a±/b±。

若后续affineF2³ lift的每条边真投影到该controller边（允许holding也只使投影更短），一个缺失的≤3 controller endpoint不能靠多条fibre路线的并覆盖补回。multiroute point-union可修补的是已有controller路线的低rank互补，不是不存在的controller短路。

当前只把下一生成器约束为须离开上述Cayley两inverse-pair接口，例如非Cayley或实质改变port结构；不在本paper列模板、选controller、做新field或展开其它参数。旧“所有约化三词分别rank3”的已排域保持原scope，不冒多路线F2³并覆盖也已排。0图/参数/Lean/新独立方法计数，完成即停。
