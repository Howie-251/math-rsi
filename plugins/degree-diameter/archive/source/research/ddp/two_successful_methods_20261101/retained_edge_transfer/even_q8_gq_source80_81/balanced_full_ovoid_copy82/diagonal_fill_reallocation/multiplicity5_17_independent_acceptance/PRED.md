# 独立预测：仅degree86与98，统一实际G1 source

2026-11-01。先登记预测再执行。两图唯一source都是actual accepted G1 graph_d82_D3_n346516.edges，不用degree83/86链式source。总预算60 CPU秒含小准备、一次编译、parent单读及两完整图验收，单worker。

实际source role J为parent标签342290+h，h0..4225，最后h4225是first hub。独立从G1 literal读取每role的全部实际邻接，绝不导入producer的邻域逻辑/cache；要求J独立且其完整N都落原H标签<342290，4226个N两两不交，空邻域没有。按source actual N size分类65diag／4160off／1hub，并在读candidate/BFS前保存first两个actual off和所有65diag role indices。

每candidate各单读一次，逐条保留parent全部14204970边；newlabel=346516+4226*copy+h，newrole恰复制source role342290+h的完整N。每条新边独立验证属于该literal N，同时每newrole实际度数完整且simple，故全邻域相等；保存每newrole的j/copy/h/sourcecenter/newlabel/Nsize及actual count，以共同parent4226真实N表为模板。parent仅全suite流读一次，其边表缓存在内存对照两candidate，原H文件不读。

degree86：r4新blocks、total k5，n363420/m15573870，degree86:342225/81:20865/80:325/65:5。degree98：r16新blocks、total k17，n414132/m19680570，degree98:342225/81:70785/80:1105/65:17。

每图仅测**最后新block**的65diag＋first两个actual off＋hub，共68普通radius3 BFS，旧根0、其他新增根0。预测86 diag(1,80,5254,358085)、off(1,81,5333,358005)、hub(1,65,5269,358085)；98 diag(1,80,5266,408785)、off(1,81,5345,408705)、hub(1,65,5281,408785)。逐类完整hist与预测对照，差异不能静默修正。

新root的source同role及其他copy的同role距离应为2；新vertices中distance2恰r−1，其他r*4225个新role vertices在distance3。只在原定68 BFS中核这些项，不增加根。保存last hub到parent clone342290的真实distance3 witness。

全pairs/prefix依actual parent G1 D3＋无isolated的full-neighborhood-clone端点替换证明，全部内点在parent。任意同role重复有共享parent邻点，任何future copy不当路线内点。degree/load由source literal role N不交与每role至多r copies得出。未测范围明确为86的16836／98的67548个新增根，不把68测量当全根实验。

0原H／field／geometry／oldroot BFS／Lean／solver／付费审阅重跑，0rootstate/Wiki/旧冻结包修改，0hash，0其他候选。root收到actual独验后自行计图/参数。
