# Many-low 覆盖设计：有界原始文献定位

2026-10-20。范围：25点、35条互异五边、覆盖所有点对，低点度6；只定位可用结构定理，不运行H搜索、不涉及Lean或v2。

**结论：本次6个定向检索式未找到可直接推出 `r≤19`、或由许多度6点强迫30边仿射骨架的覆盖设计定理。** 找到的精确完成定理要求先抽取线性部分平面，仍缺从原35边覆盖到该输入的证明。不能将这个有限检索结论写成文献中不存在此类定理。

## 当前对象与文献输入之间的缺口

度6的点x满足 `Σ(y≠x) λxy=4·6=24`，故每个λxy=1；这只控制至少一端为低点的点对。所有重复点对位于h个高点中，并不表示任意两个原块至多交一点。即使h≤5、至多一条高点内部五边，**两个含低点的块仍可共享两个或更多高点**。因此“高内部边至多一条”不是部分仿射平面的线性性假设。

原输入也不是全体点度6的BIBD：35·5=175而25·6=150。不能把最小重复度点的局部等号升级为整个覆盖的精确设计。

已知r=18无30边骨架实例作为任务输入保留；本次没有重新验证或推广该实例。

## 精确定理与可用条件接口

### 1. 部分仿射平面的完成：条件工具，尚非当前覆盖结论

Cassie Grace, Klaus Metsch, Geertrui Van de Voorde, *A Completion Result for Partial Affine and Inversive Spaces*, arXiv:2505.23995 **v2**, 24 Nov 2025，预印本。[v2原始PDF](https://arxiv.org/pdf/2505.23995v2)

版本注意：搜索命中及`/html/...v1`显示旧作者信息；本次实际PDF首页是上述三作者/v2，以下页码均指v2印刷页码。

- p.2定义：order n的PAP有n²点、每线n点、任意两线交至多一点。
- p.3 Theorem 2（定位Dow 1986, Theorem 2.1）：PAP、平行关系为等价关系、b>n² ⇒ 可补成仿射平面。
- p.8 **Theorem 7**，结合p.2的`g(5)=g1(5)=24`：order5 PAP若平行为等价关系且b>max(23,25−√5)=23，则可补成仿射平面。

**可供后续使用的准确接口：** 从原H抽取至少24条互异五边A，证明任意两条交≤1并且“相等或不交”在A上具有传递性，即得一个30线仿射平面的完成；完成所添的线不必已经是H的边。因此即使该条件工具触发，仍须另证“完成的30条线全在H中”，才能声称H含30边骨架。本次未证明任一抽取或包含步骤。

### 2. 无平行等价假设的近满部分平面完成

Stephen Dow, *A completion problem for finite affine planes*, **Combinatorica 6 (1986), 321–325**, DOI 10.1007/BF02579258。[原出版社摘要](https://link.springer.com/article/10.1007/BF02579258)

出版社原始摘要明确：任意order n≠3、具有n²+n−2条线的PAP都可补成仿射平面。因此n=5时，**28条线性原块**足以应用完成结论。该摘要未给正文定理号；本次没有取得1986正文全文，不臆造具体定理页码。该结果仍要求PAP；35条覆盖边不能据边数直接代入。

### 3. 覆盖设计的仿射极值刚性：全体重复度条件不满足

Joanne Hall, Daniel Horsley, Douglas R. Stinson, *Bounds on data limits for all-to-all comparison from combinatorial designs*, **Designs, Codes and Cryptography 92 (2024), 2863–2879**, DOI 10.1007/s10623-024-01418-6。[原文§4, Lemma 4.8](https://link.springer.com/article/10.1007/s10623-024-01418-6)

其条件为：覆盖设计D没有重复点（相同块关联列），**每个点**均在至多c+1块中，并且加权块负载极小值L(D)=1/c。结论为almost projective plane，或删点得到order c仿射平面。取c=5需要全部点度≤6，当前175次总关联已排除该前提；低点很多不足以替代全体上界。此文也不是按原块删到30边骨架的定理。

## 已有本地来源

已检查`research-wiki/papers/`及`ref/`中设计相关索引。命中Sarvate–Mishra–Namyalo的Clatworthy参数页：`research-wiki/papers/sarvate2016_group_divisible_designs.md`、`ref/literature-20261019/sarvate_mishra_namyalo_clatworthy.pdf`。其R155是全体点度7的(25,35,5)两指标设计构造；重复一个平行类的构造不简单，也不是当前many-low覆盖的分类或完成定理。没有从该来源新增进口。

## 搜索收据与停止范围

只用了以下6个查询，之后仅打开原始来源、定位定理和核对PDF页面：

1. `covering design v k squared minimal replication affine plane excess embedding theorem`
2. `pair covering designs affine plane excess minimum replication points completion`
3. `"covering designs" "minimum replication" affine`
4. `"partial affine plane" "completion" "points" 1986`
5. `"covering designs" "excess" "affine" plane`
6. `"covering" "25,5,2" replication`

未采用搜索中的百科、AI生成定理站、彩票站、非原始摘要聚合站作为数学依据。没有发现并核验many-low专用定理，未据有限未命中排除其存在。当前最具体的文献方向是**先证明可抽取24条平行等价的线性块，或28条任意线性块**；两者都只是条件接口，不能记作r≥20分支已排除。
