Same fixed F5 induced-subgraph mechanism. Please statically counterattack the new H65 lemma below; no numerical execution. The finite 25-point quotient enumeration is evidence for the stated lemma, not a Lean/DRAT certificate: all 2^25 subsets, largest subset avoiding the 100 three-slope noncollinear triangles is 12, each quotient vertex has 12 nonneighbors and any distinct pair has at most6 common nonneighbors. Verify normalization of three directions, support nesting, equality of supports when sizes>=65, the 13-line boundary, translation holonomy being nonzero, and the all30>=65 obstruction with maxdegree16. The 64/65 example is only a local relaxed-provider example. Do not extrapolate to general N(16,3) or all nonuniform induced graphs. Root independently checked paper and T1(1,1,1)=(1,2,3) outside E20; full-fiber propagation plus unique-word closure only reaches its external 5-cycle, not all30. Also examine these further route claims: all 22500 shared groups plus reverse exactly characterize D<=3 for all external adjacent fiber endpoints, since off-common-line difference belongs exactly one of the six planes. In the same fiber, there are exactly two triangle control words. Each has rank3 noise, hence exactly one lifted3path for each endpoint pair. There are 1000 same-fiber unordered pairs with5 two-step middle choices and6750 withnone, per fiber; the latter exact conditional formula is keepx&keepy => (keepa&keepb) OR (keepc&keepd), expressible as four endpoint-conditional clauses. A direct one-fiber all7750-pair check agrees, not a substitute for the general proof. Return SOUND AS STATED or concrete corrections, separately for H65, all-high exclusion, and complete external/same-fiber route classification. Main enhanced batch just ended UNKNOWN after59.879698CPU,0candidate; no graph claimed. Paper:

# Partial-fiber线占用：精确网格规则与sharp65阈值

固定原成功3750点F5源及其C30控制器。本文件只用external相邻控制fiber的双向shared-middle必要条件；不运行新SAT、原图BFS或生成候选图。通式推导为本地证明，唯一有限引理由本轮25点商的完整枚举支持，尚未外审/Lean。原源的six-plane pencil、反向关系以及任意三个ell方向独立为继承事实。

## 1 一张5×5网格的精确形式

固定external dart u→v、端口p及q≠p。令A=S_u，B=T_p^{-1}S_v，把目标坐标拉回u坐标。edge方向为ell_p。每个W=span(ell_p,ell_q)的陪集是一张5×5网格，q线为行、p线为列。令a_i是第i行A的列集合，J是B碰到的列集合，c_i表示该q行对应的N_q五点provider集合是否碰到相邻fiber保留集。

在格点w=(i,j)，shared-middle规则恰为：

    j∈J 且 a_i\{j}非空 ⇒ j∈a_i 且 c_i=1。

它与下列分类完全等价：

* a_i为空或J为空时无要求；
* 否则J⊆a_i；若|a_i|≥2，再要求c_i=1；若|a_i|=1则不要求c_i。

必要性：若j∈J但j不在a_i，则任取a_i中的点即触发矛盾；当行内至少两点时，每个已占列的中心都有另一个A点，因而provider必非空。充分性直接代回。

所以，对非空A、B的一张网格，B可占的列恰为所有非空A行的交集，并要求每个至少两点的A行有provider。特别地，若B占b≥2列且A占r行，则A包含对应r×b矩形、|A|≥rb、|B|≤5b、这些r行provider全非空。这是精确条件，不仅是计数下界。2048个单行真值状态全部与原格点公式一致。

注意：触发必须是q-line(w)去掉w后碰A。若只保留w，不能据此要求provider。

## 2 三个pre方向与三个post方向

商V/〈ell_p〉有25点，每点代表一条五点p线。A、B的非空p线支持分别记K、L。前回退的三个q≠p给三个不同的商方向；反向shared规则给另外三个post方向。six-plane pencil保证两组三方向恰分割商平面的全部六个方向。

若a∈K、b∈L且a≠b：

* 若差方向为pre，shared-middle的必选中心迫b∈K；
* 若差方向为post，反向规则迫a∈L。

因此K\L和L\K不能同时非空，K、L必嵌套。

若K严格包含于L，则固定b∈L\K，所有a∈K都必须在b的三个post方向线上。三条线去b共12点，所以|K|≤12。反向亦然。因此只要|K|、|L|均≥13，必K=L=U。

对于共同支持U中的pre方向边a—b，实际q方向平移把A在a线的保留子集恰好映到A在b线的保留子集：两边都有B点，分别应用两个端点顺序得到双向包含。post图对B同理。

## 3 小商有限引理及其作用

任意三个不同商方向经可逆线性变换可规范为(1,0)、(0,1)、(1,1)。令Gamma为25点图，同方向线上不同点相邻。

每点有12个非邻点，任意两个不同点的共同非邻点最多6个。因而|U|≥14时Gamma[U]连通：若有孤立点，则|U|≤13；若分成两侧均至少两点的无交边集合，则用每侧两点限制另一侧≤6，总数≤12。

本轮完整枚举Gamma的100个三方向非共线三角形的全部25-bit顶点子集，得到不含这种三角形的集合最大恰12。故|U|≥14必含这种三角形。确切算法见quotient.cpp：去掉集合的最小点，剩余集若已违规则当前违规；否则只检查包含该最小点的三角形。遍历全部2^25集合，未使用SAT或外部分类。

沿一个三方向非共线三角形提升，三个不同q方向的净平移落在〈ell_p〉中，并且非零：三个q向量线性独立，非零三段不可能净和为零。反复绕行产生F5中完整的五点平移群。因此该商点上的非空A子集必为整条p线；连通性再迫U上全部A线为整线。反向post三方向重复相同论证，使B也为整线。

## 4 H65：阈值及边界

若|S_u|、|S_v|均≥65，则|K|、|L|均≥ceil(65/5)=13，故K=L=U。

* 若|U|=13，两侧至多13×5=65点，故均正好占满所有线。
* 若|U|≥14，用上一节连通及非零holonomy三角形结论，仍迫两侧全部整线。

结论：双向shared-middle的keep-center部分本身就迫

    S_u是完整p线之并；S_v=T_p S_u；|S_u|=|S_v|。

这不使用provider条件，更不需要其它fiber大小下界。

65不能在这个局部必要系统中降为64。取actual p=1，edge为0→20，p线商坐标为(x0,x2)。令O为商原点的12个post邻点，U=O并{0}。A保留O上全部12条p线，并在原点线保留4点；B'=T_p^{-1}S_v保留U上全部13条线。于是|A|=64、|S_v|=65，一条A线未满。原点在pre图Gamma[U]中孤立，其余A线全满；反向B线全满，所以双向规则均成立。BOUNDARY_COUNTEREXAMPLE.json给出完整局部标签，两侧125个中心、各三个方向共750个条件实测零违反。provider flags取全true；这是局部阈值反例，不是满足全图16度或D3的候选。

## 5 与逐点16度的确定联系

假设所有30层均≥65。每条external边都是高高边，H65使每个S_a沿其两个external端口方向都闭合。两个方向独立，因此S_a必为其张成平面E_a的若干完整陪集之并：

    |S_a|=25m_a，m_a∈{3,4,5}。

高高external边的p-line关系使每个保留点在该端口恰有5个保留邻点。每层有两个external端口，共贡献10。

若b是triangle邻层，入端口方向不属于E_b：它是另外两个ell方向之一，任意三个ell独立。故对应五点邻线与S_b的每个平面陪集恰交一点，贡献m_b个邻点。若a的两个triangle邻层为b,c，则每个保留点的诱导度恰为

    10+m_b+m_c。

maxdegree16迫m_b=m_c=3。控制器每层都在三角形中，所以所有m_a=3、每层75点。

但actual external dart0→20、p=1有

    E0=span(ell1,ell3)，E20=span(ell0,ell1)，
    T1 ell3=(1,2,3)不在E20。

三平面陪集之并的平移稳定子恰为其二维方向E：F5商中的三点子集不可能对非零平移不变。H65的S20=T1 S0遂要求E20=T1 E0，与上式矛盾。

所以真正maxdegree16、D≤3、全部30层非空的保留图不可能每层均≥65；至少一层≤64。N≥1921又由平均值必有一层≥65，因此纪录候选必有高低混合。这未排除一般不均匀目标，也没有推出N≤1920。

## 6 高段及全fiber的准确边界

高高external相邻层等大小，故external 2factor中每个连通高段都传等大小。四连高a-b-c-d时，中间b、c沿各自两个external方向闭合，共同大小只能75、100或125。若中边的平面方向不运输，则75/100不可能；125全fiber不受这个方向论证排除。

若一层为完整125点，其任一external邻层只要非空，反向shared规则就沿三个独立q方向迫该邻层也完整。因此全fiber传遍整条external圈。但本文件没有证明一个整125圈与其它低圈不相容，不能声称每个C5都必含低层，也没有追加全局求解。

root另保存的FULL_FIBER_PROPAGATION_PROBE.json记录：只用external传播及258唯一控制词的full-endpoint规则，从任意单个fullfiber开始的30种闭包都恰停于其5点external圈。该probe约0.002503CPU，与本代理1.162269237CPU实验分账；文件保留paper独立核对pending标记。它说明这组规则没有传播到其它圈，不说明真实D3图一定允许完整125圈，也不排除其它路线约束进一步传播。

