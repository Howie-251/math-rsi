# 只读结论：新规则未定位旧排除，但完整R8缺集没有缓存

实际源和 implicit recipe 齐：Rodriguez–Canale331387/994161，全6regular/D9，使用已继承 RIGHT group `(j,n)*(a,c)=(j+a,n*41^a+c)` over C49/F6763。原作者小 C 发 left-Cayley 边，既有 working code 已通过 inversion 解释为 right 模型；不能混用左右坐标。没有本地完整 raw adjacency，也不需要在读门下载它。

在实际source目录、当前6D9 stage与对应少量canonical Wiki节点的有限检索中，未定位这个同源“删3条顶点不交旧边＋一个6star”的旧 strict NO。旧三类 single-subdivision全部NO，及F6959/primitive49/fixedphase/allnormal全部NO是不同范围，完整继承但不重跑；不能把它们当本规则已排。

旧 single-subdivision 的 actual run.cpp 是关键数据边界：三次查询只保存 missing counts14088/13875/14028、first labels20/6/20及层直方图。完整 missing sets/bitsets和距离数组没有写盘，d/q仅在 query 内存；因此现在没有可直接拿来求交的三份完整缺集，也未定位旧all-source距离/unique-geodesic数据。firstmissing或缺量不能替代真正路线补集。

这次纸面接口比“再对每个三cut host做R8”更精确：设六pin集合P、H=G−3cuts。因为所有删边两端都在P，`d_H(P,v)=d_G(P,v)`。最近P→v路径若穿任何删边，穿后的端点仍是P成员，从它起步更短，矛盾。故新根R9等价于三个 translated endpoint-pair R8 缺集的交为空；即便旧单删边缺集取自删边host也相同。这是**充要**的新根接口，不会因另外两条cut破坏最近P路径而失效。

下一数据动作应由root另授权解决这个明确缺口：为新多pin互补问题取得三代表完整 endpoint-R8 缺集，利用实际Cayley左平移后做集合交，避免每triple重复球查询。此处不运行该动作。old-old仍须独立关注：任何已存在避开cuts的旧≤9路保留；经新星路线的最短长度为 `d_G(u,P)+2+d_G(v,P)`，其与 `d_H(u,v)` 的较小值才是新旧点对距离。没有旧geodesic缓存，就不能凭新根已cover宣布完整D9。

另外按root要求只读核对 shortest-word multiplicity：未定位 actualF6763源的 shortest endpoint counts。附近 `controller_capacity/RESULT.json` 只有49phase、按length/lastdart计的 raw NB prefixes，不含 normal endpoint，也不是最短路计数；F6959 image/form 数据同样不能当作F6763源的 geodesic counts。root提出的 cut-critical9geodesic factorization 门属于下一数据问题，当前未构造该 DP、未枚任何 u-v。

本轮0triples、0新图、0BFS、0field/D9复验，保守计0.8/5CPU；所有工作停止，原源和旧terminal未改。PRED仅提出新根缺集互补的可推翻正假设，不把331388当成果。
