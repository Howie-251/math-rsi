# Loz1100的具体D4迁移：四逆对p61整族与四个固定CRT lift均失败

来源为已验(8,4)1100，群乘法(i,x)(j,y)=(i+j,x·2^j+y)，i mod20、x mod55。原四生成元(4,27)/(12,11)/(9,9)/(19,11)，逆元重排、共同共轭(0,22)及x乘3后，精确归为

(phase,x)=(1,0),(12,33),(11,1),(16,19)。

因33=2^10−1、19=1+2+2^4，冻结同一源规则A0、B=r10−1、C1、D=1+r+r4，保持四个inversephasepairs。未重新验证源边表或BFS。来源EyalLoz及Comellas当前D4描述；基线日期2026-10-27，L=1100。

关键区别：源2 mod55整体order20，但CRT分量orders4/10，Phi20(2)=205≠0 mod55；不能把primitive20 field的关系误施于源或CRT。

## 实际检验

1. primitive p61（假设n1220）：全部≤4 reducedwords按20phase计，原始自由B/C/D的Phi20形式容量最薄phase10为72，仍容61，所以实际检查冻结整数规则的8个order20根。全部失败，代表根遗漏依次289/127/110/201/98/82/298/86；没有导图或全图距离测量。
2. 保持真实整数r2：因m|2^20−1、55<m≤160，全部合法模数恰75/93/123/155，n1500/1860/2460/3100。完整≤4路对每m求值，代表根分别漏229/380/601/974；全失败。m93的action实际order10但仍合法C20作用。没有把field的Phi20判据外推给CRT。
3. 针对phase10薄层，事前预测至少一个自由平移可全覆盖。穷尽p61的8个actions、每action3783个共轭/标量规范case，总30264项（其中8项复用前轮已知失败）。**0个phase10 survivor；每action单层最大仅53/61。预测被推翻，固定p61四逆对phasepattern的全部自由translation关闭。** 其它19层未查且无须查。

这区分了固定多项式的求值碰撞与更强的自由pattern阻碍：前者只排12个具体lift；后者精确排Fp61的该phasepattern，不排其它phase或一般D4新图。完整图的degree/diameter/badpair字段均未填写；所有计数仅为代表根端点覆盖。

首轮CPU0.066323808秒，自由参数输入准备0.11474803秒、native枚举0.006424秒（编译另计）；0新图、0新下界、0旧source重验、0BFS、0MIP/外审/Lean。达到明确终态，不扩自由参数、prime或offset队列。

证据：[SOURCE.json](SOURCE.json)、[事前预测](PREDICTION.json)、[首轮完整结果](RESULT.json)、[计算程序](check.py)、[自由phasepattern报告](free_prime61_phase_pattern/REPORT.md)。源参数来自本地generator_specs及已验d8_D4_known.edges，公开页面为 https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html 。仅写输入[wiki_row_suggestion.json](wiki_row_suggestion.json)，没有改共享Wiki/HTML/交付文件。
