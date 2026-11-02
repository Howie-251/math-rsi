# 从实际图到 Lean 声明：caller、表示与复用

Lean只按当前任务需要调用。固定公式图已完成的kernel、保存的literalBFS和模型静态review是不同证据。本页给实际数学与程序入口；不在archive编译、不假定新机器已有原Linuxcache。

## 1. 固定F4公式图的完整caller链

真实顶点标签`64*a+x0+4*x1+16*x2`，60controllers×F4³；F4按多项式编码0,1,w,w+1，w²=w+1。源码用`F.ofCode`解释数据，ring numeral2本身为0，不能将保存的code2误作该numeral。

[Field](../archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840Field.lean)给四元运算、Vec／Mat、basis decomposition和additive_ext；它要求additive和F4scalarlinear两者，才能从三个basis扩到任意vector。

图定义 `graph` 是实际forward关系的looplesssymmetrization。每dartmatrix按实际源控制器/port选择，而reverse在targetcontroller/inverseport；不是只有一个globalmatrixperport。MatrixCertificate对实际basis与direction核inverse；[Routes](../archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840Routes.lean)据此证明forward_reverse、adj_iff_forward，故每点邻域是Fin5×F4的像，degree≤20。

同文件`bounded_walk_of_route`把三个forwardedge装成真实`SimpleGraph.Walk`，只要求controller终点和fiber终点两式。`route_affine`拆成源中心与zero-source噪声。

[DecoderInterface](../archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840DecoderInterface.lean)用basis有效性＋noise linearity给任意displacement。相邻decoder的before／afterbacktrack因真正的逆有共同directcenter，覆盖300darts×64residual。非邻／同层controllerWord给3300pairs各三basis证书。

[DiameterInterface](../archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840DiameterInterface.lean)处理任意u,v：先按实际控制器adjacency分支，adjacent令d=target−directcenter，nonadj令d=target−chosenroutecenter，分别喂decoder并供给上述两终点式。它的发展premises由已闭Certificates真正供给；[Diameter](../archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840Diameter.lean)调用`diameter_of_local_decoders controller_valid nb_noise_valid adjacent_valid`，没有把certificate留给用户。

[Lower](../archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840Lower.lean)对0与6核所有一步和400两步forwardwords，借adj_iff_forward与Walk分解排任意Walk≤2。[Exact](../archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840Exact.lean)真正导出：

```text
concrete_order_degree_and_D3 :
 card(Fin3840)=3840 ∧ (∀u,degree(u)≤20) ∧ DiameterAtMost graph 3

diameter_exact_three_in_project_definition :
 DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
```

它们没有输入certificate前提。保存Audit打印实际定义／type／transitiveaxioms，只有propext、Classical.choice、Quot.sound。此结论不包含LeanASCIIparser、精确20regular、38400edgecount或mathlibediam等式；外部literalchecker另承担实际文件属性。

## 2. 表示压缩怎样保持原对象

原graph的300dartmatrices不改定义；FastTables先证明每个原matrix等于compactpoollookup。25distinctdartmatrices、402distinctdecoderinverses、25distinct64targetadjacentdecoder用于减少重复展开。有限检查继续对原routeVec做，而不是只证明压缩后的另一个图。

60控制器行s分模块，已通过部分保留。历史59rows2020.311852CPU加Row0029.266997，单module预算115、三workers是当时环境实测，不是本插件默认。需要重现时先确认固定Lean4.24及依赖／内存；不要将历史CPU加总伪称本次新测。

q8较大projection表用base4194304 packed32、分块与Fin.cases改善kernel表示；共1104模块的历史过程含失败与恢复。压缩要有lossless语义桥、表到原输入绑定及真caller，不能因更快就省掉coverage。D4源192controller的24symmetries／8orbits只作用source，不自动作用固定837／864clone集合，clone另有owner负载证明。

## 3. Clone与新原目标如何接上

[FullNeighborhoodClones](../archive/source/formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean)是generalgraphconstruction；新具体instance须提供真实source、center函数、sourceD、noisolates、degree／load界、carrierlabel等价和nonD2。不能只导出genericallk就称八个具体端点均已编译。

P33 source载体为Fin160000⊕Fin50，family为Source⊕(Fink×Fin1650)，明确等价Fin(160050+1650k)。q8diagonal higherk则sourceG1／first4226roles，别把原GQcenter或仅4225clones送入caller。外部orderedrecipebinding核实际graph文件／parameters与该定义同序，不冒作Leanparser定理。

D4源15552非正则，单满秩word不足；实际coset应用对(a,b)只选从a到同一b、长度≤2的reference word。97组尝试保留6次首reference失败；91组成功证书覆盖3648个原缺失对，其余33216对沿用rank-4证书。这里的实际reference选择不收窄一般仿射coset引理。

系数证书给出的长度≤4状态序列到真正SimpleGraph.Walk之间还有原邻接桥：只删除连续相同完整global label的virtual stay。同控制器但不同fiber状态、同fiber状态但不同控制器均不得删除，其余步骤绑定为真实源边。coset、保持port的对称transport及该桥接合起来供给源的真实Walk；fiber覆盖单独不提供阶、度、非D3或最终kernel出口。

plane owner恢复另证load≤1，选定I31/I32的完整正等式供具体clone目标；源PASS不替代新label、owner和degree的caller。

## 4. 当前任务的执行方法

1. 读当前正式目标与实际导出声明，反译carrier、Adj和DiameterAtMost定义；确认目标是固定图还是任意图族。
2. 找本次未闭的actualcaller，不从整个archive统一重编。缺数学假设回prove；纯API／数据展开留形式化内修。
3. 若任务要求新build，在任务副本配置固定toolchain／manifest／imports。先直接调用一个非平凡实际输入，测表示／成本，再扩有限rowdomain。原sourcecache可复用时别复制整个引擎。
4. 指定真实newmainmodule；默认旧Main成功不算。构建后独立import展开原命题、type和transitiveaxioms。打印standardaxioms仍须核actual目标，不足以排P→P式削弱。
5. 返回实际命令、exit、new／reused模块、完整域、输入绑定和未闭连接。静态阅读旧receipt就明确未build；模型review未执行Lean也照实写。

归档compile.py读取原LinuxROOT和旧FORMAL_ENV_COMMAND，且generate_lean.py缺原ROUTE_CERTIFICATE输入；这些原件便于审计，不保证unmodifiedportablebuild。原包没有工具链／oleancache。新环境需要的依赖明确准备；用户只要求阅读／复用证据时无需安装／重编。
