# (8,9)4601361 source迁移：source审查与有限BFS执行设计

本分析不执行producer、不下载大边表、不枚53,804,809个NB词，也不重跑旧source BFS。唯一目标族已由Root冻结：nextprime49663、同93phase及normals0/1/4800/4208，全部60个primitive93 actions；预算120 aggregate native CPU，compile另记。以下用于这个实际批，不新增参数队列。

## 1. 实际source、gauge与连通

AUTHOR采用LEFT law
(n,I)(m,J)=(n+a^I m,I+J)，
source N49477/M93/a19070，三数及四正元完整绑定见 [ANALYSIS_GAUGE.json](ANALYSIS_GAUGE.json)、[GAUGE_ARITHMETIC.json](GAUGE_ARITHMETIC.json)、[AUTHOR_construction.json](AUTHOR_construction.json)。source正phase/normal为25/24458、85/25770、21/7723、79/40638。

LEFT translation共轭使b→b+(1-a^j)c。引用source owner已算c32880，shift=[0,41140,9293,46574]，第二项非零；共同scale46118得到normals[0,1,4800,4208]。phase j'=67j（25·67=1 mod93），旧j=25j'，新β=a^25=37269，phases[1,22,12,85]。本分析不重新计算这些constants。

目标只按这条source-normalized整数控制定义，p49663，n4618659、m18474636。真逆为(-β^-j b,-j)，必须按目标β重算。LEFT中的准确连通关系是g2*g1^-22=(normal1,phase0)；反序虽然也给非零normal，却不是literal1。g1给全部C93，normal1给全Fp，故每个目标model连通。

八个有向phase1/22/12/85/92/71/81/8互异且非零，所以每项simple八正则。Cayley左平移给单identity的完整距离证据等同全图直径，不依赖旧source的Aut报告。

## 2. 现成helper与必须修改的边界

可复用：
- [field6959 implicit radius9队列骨架](../d6_D9_current331387_source/field6959_all_embeddings/probe.cpp)：只借visited/queue/hist/case结果结构；它是RIGHT且p小，不能照搬step或int模乘。
- [field641 LEFT Cayley内核](../d7_D8_current264440_source/field641_all_embeddings/probe.cpp)：借LEFT坐标和每action真实inverse思路，目标需换成单prime normal与93phase。

目标(p−1)²=2466314244已超signed32。所有pow、inverse及shift预表的模乘都用int64_t/uint64_t中间值；vertex ID、queue uint32足够。不能复制旧helper里的int a*a或normal*factor表达式。

推荐phase-major编码ID=phase*p+normal。每action预表：
powers[phase]=β^phase；
shift[phase][dart]=powers[phase]*b_d modp；
nextBase[phase][dart]=((phase+j_d)mod93)*p。

每次queue pop只分解一次phase/normal；八邻步是normal+shift、一条件减p、nextBase+normal，无热循环模乘或反复除法。这严格等于LEFT right-step，不换group convention。

visited distance用int8_t(-1)，queue用uint32_t，合约5N bytes≈23MB；重用两个buffer，无显式adj或大型word缓存。只展开depth0..8，depth9节点计入覆盖和hist但不再扫其边。全N已达到时，hist的最大非零层给exactD≤9；若未全达，只记录R9失败，globalD仍null。

## 3. 规模、首例profile与hard aggregate

每个完整case的上界约8N=36,949,272邻边步，60项总上界2,216,956,320。没有再除以93：单identity免去了全源根，但这一个BFS仍有约462万个group states。radius9截止常少于该上界，优于逐词处理53.8m prefixes。

第一项primitive root就作为正式case0完成，CPU/time同时作吞吐profile；不得丢弃后再重跑“正式首项”。按该时间反馈剩余规模即可，120CPU是已授权hard aggregate，不因缺点相近或profile快自动扩到更多参数。只看是否完整覆盖，不按R9 missing排序后续roots或修改normals。

一个进程用RLIMIT_CPU=120；compile另报。循环内应有软截止（例如留出数秒写结果），至少在每case开始/结束和固定queue块处检查累计CPU。每完成case写并flush index/β/CPU/R9reached/hist/首missing和next_cursor；在途case开始前也先写cursor。若软截止或hardkill时尚未完成某case，标UNKNOWN/partial，不把已访问数量当完整R9遗漏，更不能写全60排尽。此前完成case保持终态，不自动重跑。

每root一个实际case；首真正fullhit立刻保存β、全正逆gens、编码、source引用及完整hist，余root明确UNTESTED并停止。失败没有必要展开depth10求exactD，也不导出全部失败边表。正图的大edge导出/独立验收由Root在首hit后安排，不混入普通负case预算。

## 4. root等价与不遗漏

Fp为素域，不能把不同primitive roots当作fieldautomorphism而略去。exact93用β^93=1、β^31≠1、β^3≠1判定，全部φ93=60个不同roots排序后各一次。

即使β与β^-1，也不能简单靠inverse-closed连接集省一半。常规phase取负的群同构若保持这组normalizedS，g1=(0,1)迫normal conjugacy shift为0；g2 normal1要求scale=-β^22，而g3 normal4800≠0又要求scale=-β^12，primitive93下两者不等。这里不声称任意Cayley图同构已被分类，只说明此常见快捷等价没有成立。没有额外已证明的参数变换就不设skip。60项内如有未知图同构重复，保留它比引入遗漏更直接。

## 5. 首hit的适量独立验收

若producer给fullhit，可由不同实现从参数生成全邻接/CSR，重算target powers和inverse，检查各点八个邻点、无loop/repeat、双向一致及完整边定义，再做一次identity完整BFS。显式directedarcs约8N，CSR约36N bytes，规模可控。

只要参数定义与全部边一致，Cayley群左平移的纸面证明使这一identity结果覆盖全图；严禁对约460万个source roots逐一BFS。旧4601361 source也不重验。若正图BFS未通过或模型不一致，不能用rawquotient/fullphase支持替代D9证据。本分析未执行任何这些正图步骤。

本批只关闭/命中固定p49663、四normals、93phases及全部60actions；不包括其它prime、其它normal向量或所有degree8 Cayley构造。
