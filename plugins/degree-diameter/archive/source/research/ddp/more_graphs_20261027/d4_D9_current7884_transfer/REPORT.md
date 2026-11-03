# (4,9)7884配方恢复及p109固定阶十八phase族完整结论

已取得当前Bhakar数学仓库的实际recipe，没有下载7884整张边表，也未重验旧D9或生成新图。它是三点底图的群电压提升，不是把7884直接当群阶的Cayley图。唯一Wiki未见这个当前源的精确迁移范围。

## 实际源及乘法约定

原始 [README](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg4/dia9)、construction.json与作者ddgraph.py已分别保存为 [README.author.md](README.author.md)、[construction.author.json](construction.author.json)、[ddgraph.author.py](ddgraph.author.py)，URL和大小见 [SOURCE.json](SOURCE.json)。

~~~
G=<x,y | x^73=y^36=1, yxy^-1=x^18>, |G|=2628.
(i,j)(a,b)=(i+18^j*a mod73, j+b mod36).
~~~

这是源码Metacyclic类明确使用的rightlaw。底图三点0,1,2；0→1有三条平行link，电压为e、x49 y10、x40 y14；0→2为e；1→2为x y6；2处loop为y3并取逆向dart。提升点(v,g)沿每个dart右乘其电压，左乘G在每个纤维上传递，故有三个完整根轨道。

三类点各四邻，recipe给n=3×73×36=7884，m=15768。标签为2628v+i+73j。旧source的D9沿用作者既有验证，没有再作sourceBFS或将recipe声明冒充新的验收。

## 承重算术及可选参数理由

实际action18在模73下阶十八，核为C36中的阶二子群。四类非恒等电压的阶依次为18、18、6、12；尤其x y6的六步闭路与y3的十二步圈是可明确保持的关系，而非只保总阶数。

最近奇数模数81虽有精确阶十八action，例如8，但(x y6)^6的平移为6 mod81，电压阶变成162。它不保持源的六步闭路；因此不把“action同阶”当作足够的迁移理由。

109是73之后第一个允许精确阶十八action的prime。它的最小此类action为4；保留M36和底图phases时，四类电压阶仍为18、18、6、12。小算结果在 [SMALL_SOURCE_PROFILE.json](SMALL_SOURCE_PROFILE.json)；这些是群元素关系计算，不是候选图直径验证。

原49/40不是随意直接复制整数。将它们写成源action18的低系数多项式：在degree≤5、系数属于{-1,0,1}中，按L1、degree、系数tuple字典序选取，得到

~~~
A(r)=-r²-r³, B(r)=-1-r².
~~~

对源模73，它们恰为49、40。差为A−B=1−r³；对primitive18root，Φ18(r)=r6−r3+1=0，故差也为−r6。这条关系在prime109仍成立。选r=4便得A=29、B=92。

据此保存一个受控建议 [TRANSFER_PROPOSAL.json](TRANSFER_PROPOSAL.json)：N109、M36、r4，底图与所有phase不变，仅按上述固定多项式迁移，目标n=11772>7884。参数选取不使用失败分数，不扫六个actions或其它N。

## 必要容量与实际单候选

源只有三种底图根轨道；同一base-target/phase槽中的非回退≤9路由必须实际覆盖正常子群的每个残基。保留action与电压精确阶的理由是保存短闭路造成的路线互补；它不能保证求值后没有碰撞，raw word数量也不是充分条件。

互补代理完成的 [phase必要容量](phase_analysis/RESULT.json) 在全部324个rootbase/targetbase/phase槽中最少有323条≤9非回退词；[Φ18整数端点去重](phase_analysis/endpoint_polynomials/RESULT.json) 后最少仍有248个形式端点。两项都不足以排除109，但形式数量充足不是求值后覆盖的证明。

[CANDIDATE_PREDICTION.json](CANDIDATE_PREDICTION.json) 在新参数生成前冻结“唯一109/r4的三个轨道根都能九步覆盖”的预测。低系数表达是本轮从源残基拟合并规范选定的controlled lift，不是原作者已证明的通用公式。

只执行N109、M36、r4、A29、B92这一项。程序在内存中构建11772点、23544边的完整邻接，实际检查全四正则、simple、无向；随后从base0 identity根作一次完整BFS。全部11772点连通，但该根偏心率十一，九步遗漏347个点。因此按冻结顺序立即停止，没有跑base1/2，更没有全11772源BFS或导出失败图边表。

| 检查 | 实际结果 |
| --- | --- |
| 新图阶数/边数/度数 | 11772 / 23544 / 全4正则 |
| simple、无向、连通 | 是 |
| 已查根轨道 | 仅base0 identity |
| 该根偏心率 | 11 |
| 该根R9遗漏 | 347 |
| native CPU秒 | 0.001110 |
| 编译CPU秒 | 0.760192 |
| 本候选整批CPU秒 | 0.763268 |

结果见 [CANDIDATE_RESULT.json](CANDIDATE_RESULT.json)、[root0_check.json](root0_check.json)。偏心率十一是这一个根的数据，不能写成已求得全图直径；实际global D及全图普通无序坏对总数保持null。347是有方向的固定root0→target缺项，不是全图坏对。

[root0_missing_by_slot.json](root0_missing_by_slot.json) 保存全部缺项的endbase/phase分解。其中endbase0/phase5遗漏七个域元素

~~~
9,10,33,75,83,88,97.
~~~

首个按编码标签的缺项是target174=(base0,phase1,field65)，精确距离十。[FIRST_FAILED_ROOT_WITNESS.json](FIRST_FAILED_ROOT_WITNESS.json) 保存同次BFS的parent路径：

~~~
0—3924—2499—7416—8136—288—5330—3771—11619—8022—174.
~~~

这已推翻唯一r4候选的D9预测：保持group action阶、电压阶与一个cyclotomic差关系，仍未保持全部路线求值互补。没有依据坏对下降追加r、offset或prime。互补代理后续按root授权作六个Galois embedding有限数值对照，六项均在root0失败，未生成更多图。

任何候选若三个identity-fibre根都通过，左G作用才把这三根证据提升为全图D≤9。当前只查首根且已失败，不满足这个验收前提；也不能用n11772低于D8 Moore界13121来推断恰D9。原7884source不重新验证，本轮完整新下界仍为零。

## 后续固定自由A/B族已终态

由新碰撞反馈，root另授权同一p109/M36/phases/C1的全部自由A/B与六actions，共71286项，现已完整无解。0新图/BFS/UNKNOWN；三必要层联合覆盖已不相容。准确计数和范围见 [generic_ab109_search/REPORT.md](generic_ab109_search/REPORT.md)。这不排其它prime/phase/C0；固定族按约停止。

## 固定阶十八phase族现已完整关闭

在旧(10,14)自由A/B族失败后，root授权保持电压阶而改变quotientphase落点。E={2,10,14,22,26,34}的15个无序pair按相位自同构分五轨道；一个继承，其余四个的新285144设置完整无解。实际新图/BFS/UNKNOWN均零。详见 [phase_order18_family/REPORT.md](phase_order18_family/REPORT.md)。这仅闭p109/M36/C1/loop3和该phaseorder族，不扩prime、M、C0或其它phaseorder。
