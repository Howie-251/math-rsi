# 研究轨迹原料：从模板摸索到完整图、推广与受限失败

本页把原始记录中能够看清“先想什么、实际试什么、结果如何改变下一步”的关键轨迹串起来，供后续研究者提炼经验。它没有新增构造、复算图、重做公开检索或运行 Lean。原始方法账本及独立实体仍是逐条查重入口：[DDP_METHOD_LEDGER.md](../research-wiki/DDP_METHOD_LEDGER.md)、[机器账本](../research-wiki/DDP_METHOD_LEDGER.json)、[Wiki 入口](../research-wiki/index.md)。461 条 Wiki 记录是研究记录数，不是461种方法，也不是461张图。

这里的“当时结论”与“当前终态”有意分开。生产报告常写“待独验”“待 Lean”，随后这些工作已经完成；应继续读同目录独验、最终形式化及根处置，而不是以生产阶段快照覆盖后续结果。相反，一张图后来完成 Lean，也不能让历史失败的其他候选自动通过。当前完整图、参数和形式化清单以本包其他交付说明及 constructors 为准。

证据链接保持原 ar4math 根相对目录。大型边表、位集、缓存或历史可执行文件是否收录，以包根实际材料说明为准；本页不把导航路径存在等同于所有大型中间数据均已带入。每段列出的耗时仅是对应记录中的实际范围，不能相加冒充从提出问题到取得成果的总研究耗时。未保存的模型推理、人工讨论、排队、失败准备或墙钟记为缺项，不补成零。

## 1. 早期广度摸索：从“缺项少”转向解释缺项结构

早期同时考察 Cayley、双轨道/bi-Cayley、coset、仿射半直积、电压提升、已有图增广等机制。最有信息量的一条是666点的5度、目标D5的4+1图：它与目标只有666个无序坏点对的差距，容易让研究陷入继续调电压。

实际先恢复它的 C37 作用，得到18点、45边的商多重图，保留9个环及9对平行边。每个控制层目标有71–105个不同五步形式表达式，均多于37；形式容量没有排除它。把表达式代回实际电压并与原图独立 BFS 比对后，发现缺项由表达式碰撞造成。全部坏点对图恰为9个37圈，每个圈点各挂一片叶，全部失败点对距离6。

随后完整检查单电压邻域：1620次参数修改中27次不合法，1593次合法；0改进、9次只是同一无向图的环反向、1584次变差。最小真正变动也把无序坏点对从666增到1480。因此停止单坐标调参，保留“必须有耦合改动或不同生成规则”的结论，没有追加退火。这并不排除多个电压同时改变后出现D5图。

这一步产生了后来反复使用的区分：路线表达式数量、实际端点数量、不同目标能否共享同一组参数，是三个不同问题。其他早期容量门也没有被算成构造成功：例如220点双轨道指定反射规则的同层槽至多9<11，直接关闭该规则；816/930的符号存活模式需要继续做实际端点或结构分析，早期必要门通过不代表已经得到完整图。后续结论应沿 Wiki 的 superseding 节点读取。

耗时：C37形式诊断0.087054 CPU秒，完整单电压邻域0.196771 CPU秒，最小变差图独立全根核验约0.012秒。这里没有保存整个早期选题过程的端到端墙钟，不能以这三个小数描述研究总成本。

原料：[C37完整诊断与逐项移动记录入口](../research/ddp/m1_c37_diagnosis/DIAGNOSIS.md)、[220点指定族范围](../research/ddp/m2_coset_tower/bicayley220/STRUCTURE_SCOPE.md)、[816容量历史节点](../research-wiki/experiments/ddp-affine816-capacity-20261026.md)、[930容量历史节点](../research-wiki/experiments/ddp-affine930-capacity-20261026.md)。C37目录的 `diagnose.py`、`measurement.moves.jsonl`、`measurement.summary.json` 保存实际输入、每次修改和终态。

## 2. D5 保边扩张的第一轮失败：有余度不等于有可覆盖的邻域

对37628点、最大度11的公开源，保留全部旧边，再给一个新点挑至多11个有余度旧邻点。数学接口很明确：选中旧点的闭R4并集必须覆盖全部旧图；旧旧距离自动保留，新增点到旧目标由一条新边加最多四条旧边实现。

实际源有2504个度小于11的点，总度余量3316。研究先计算这些点的R4球，冻结8种起点 profile，每项贪心补到11邻居并做一轮完整坐标替换。最佳仍漏115个旧目标，独立多源R4核验与遗漏集合完全一致，没有展开37629点新图。

这里的“8”是8种起始方案，绝不是只允许8个邻居。该试验只关闭这8种起点加一轮局部改进，不排除其他11点覆盖集。继续提高同一局部分数没有给出新的结构理由，于是后续转向源图的有限几何覆盖结构，而不是把115个漏点反复少量削减。

耗时：R4准备约0.310 CPU秒，profile主体约1.019 CPU秒；包含编译和独立核对约2.667 CPU秒、墙钟约2.673秒。419352次评分属于一个固定有限批次，不是419352张新图。

原料：[失败报告](../research/ddp/breadth_20261027_wave4/record37628_single_extension/REPORT.md)、同目录 `result.json`、`independent_cover_check.json`、`source_profile.json`、`probe.cpp`、`terminal.json`。

## 3. D5 的成功转折：几何集合先负责旧核心，锚点负责剩余部分

后续恢复H(9)相关源的折叠、几何坐标与Q-line结构。与先挑大R4球相比，新规则给出一组几何 mandatory pins，先保证大块旧核心，再精确求少量锚点覆盖剩余点。真正验收的仍是折叠后的字面旧点、当前度数与当前完整图R4，而不是“它在几何上叫阻塞集”。

(11,5)线上，10个Q-line mandatory pins加1个锚点产生37629，再由剩余冻结池按序得到37630、37631。两个新增步骤各自在加入前的真实当前图上做完整R4覆盖；最强37631后来有独立全部37631根的普通BFS。剩余18项当时没有单锚点完成，不能据此断言它们在最终37631基图上仍失败，更没有证明37631最大。

(12,5)线上，先从42342起步，在已接受的42345图上冻结592项新的10-pin/cap2池。一个批次访问367项：32完整扩张、280次当时基图的精确至多两锚点失败、55次度数阻断；达到预先的32次成功复评节点便停，225项未试不是失败。逐步输出实际完整邻集、旧度数、source_n/m和补覆盖路径，得到42377；该代表图后来有独立全源BFS。此后其他有限规则继续推进，形成最终42343–42402共60个不同阶数的完整图序列。

关键纠错是增量缓存：旧R4球不能原封不动地拿来否定新基图。新增点会缩短一些旧距离，后续步骤需要更新当前覆盖，并包含所有先前新增点。37631后续报告给出精确缓存更新公式，同时每个正例另做当前图直接多源R4检查，避免正例仅依赖缓存实现。

耗时：37629之后的固定20项跟进为0.513024 CPU秒；42345→42377的32次扩张批总97.650981664 CPU秒，含312次mandatory多源R4、16079次缺项反向R4。首个新点在该批18.117 CPU秒出现。它不包括更早研究、后续代表图全源BFS或模型讨论的全部成本。

原料：[D11后续原报告与缓存公式](../research/ddp/more_graphs_20261027/h9_d11_followups/REPORT.md)、[D12固定批轨迹](../research/ddp/more_graphs_20261027/h9_d12_global_extensions/REPORT.md)、[D11当前证据节点](../research-wiki/experiments/ddp-h9-qline-d11-family-37631.md)、[D12当前证据节点](../research-wiki/experiments/ddp-h9-qline-d12-family-42377.md)。对应目录 `accepted_sequence.json` / `accepted_extensions.json` / 逐项结果保存完整邻集和先后次序。

## 4. Q-line 接近耗尽后的换规则：Baer、Rédei，以及不依赖几何名称的 prototype+guard

D12已用邻域逐渐消耗度数后，继续同一几何池会大量度数阻断或锚点失败。研究分别引入Baer子平面、Rédei阻塞集，而不是只把旧池再扫一遍。

Baer路线中，13个raw points经折叠变成11个mandatory pins；它们覆盖全部41356点旧核心，只漏9个extras。加锚点41666得到完整42398图。固定410项池终态为1成功、363次实际覆盖失败、46次度数阻断；364个实际mandatory检查都未漏核心。这里没有把364个F3-center平面的7560个Baer成员误写成所有可能平面已排除。

Rédei路线在固定85项 once-policy 下最终得到42399–42402四个完整图，其余23项当时度数阻断、58项当时覆盖失败。首步有新完整边表独立新根核验，后续由完整当前R4/度数归纳。后续又研究非Frobenius稳定平面的longside迁移，虽然首门64条线非空，完整5971968原参数所代表的degree池为空；关闭的是这个whole-class/nonstable-plane范围，不是所有阻塞集、所有PGL3 placement或所有增广。

D13则遇到另一个转折：完整几何邻域难以在实际满度位置落地，改用近完整旧点邻域。首例以51013为prototype，跳过满度11352，保留9个邻点并加入guard50577，得到51418。冻结91个single-fault prototype按既有范围处理，最终40成功、13当时度数阻断、38限定guard失败，得到51418–51457。原37次失败没有在后续新基图上偷偷重跑；剩余53项的正反馈只扩大已授权原池未访问部分。

这些结果解释了“换规则”的实际含义：Baer/Rédei改变了覆盖核心的方法，prototype+guard改为利用真实邻接的近完整复制。它们都是同一保边扩张接口中的不同邻域生成规则，不能把每个前缀或每种几何名称都统计成独立框架。

耗时：Baer生产16.311927 CPU秒；42398新根独立核验约0.2963 CPU秒。Rédei剩余83项续批2.979748 CPU秒，初始两项成本另存父生产记录，不补造合计。D13首生产9.644256492 CPU秒，原53项后续3.208995775 CPU秒，记录合计约12.85326 CPU秒；此为生产范围，不含整个研究/公开比较/形式化。

当前比较必须带更正：51457只超过当时保存的主表51417，后来找到作者公开88452点13度D5图，因此这40张仍是合法实例，但已知被公开更大图压过。不能把103个D5前缀叫103个全球新纪录。

原料：[Baer实际生产](../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/REPORT.md)、[Rédei后续](../research/ddp/more_graphs_20261027/h9_redei15/production/continuation/REPORT.md)、[非稳定longside终态](../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/REPORT.md)、[D13后续轨迹](../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/REPORT.md)、[当前D13范围与更正](../research-wiki/experiments/ddp-d13-singlefault-star-family-51457-20261027.md)、[公开比较更正](../expert_review_current/FOUR_GRAPH_RESULTS_20261031.md)。

## 5. F5 仿射构造：用两类路线共同覆盖全部点对

与增广源图并行，研究沿已有30点四端口控制器和仿射直线框架，选择F5上的具体矩阵、方向与真逆端口，产生3750=30×125点、20正则、37500边的完整图。控制器/通用框架继承Mizuno，不能把本地字面参数实例说成发明仿射提升。

正确思路不是要求一个路线类型单独承担全部点对：相同或非邻接控制层由满秩三步噪声映射覆盖F5³；相邻层由6个共一条直线的平面补全，大小5+6(25−5)=125。两种路线使用同一套矩阵、方向和逆配对，覆盖全部900个控制层有序对及任意起终坐标。

实际完整边表独立检查全部3750根，0坏点对、直径恰3。具体公式图后来在Lean中证明card、最大度≤20、真实Walk的D≤3及非D≤2；有限证书绑定到字面参数。Lean对象是公式图，不是磁盘ASCII文本parser形式化。

失败风险在这里已经明确：只把q换大，不能仅凭度数4q、点数30q³和若干局部满秩断言成功。下一条轨迹正是对这个直觉做可推翻检验。

耗时：完整边表生成0.106811736 CPU秒；全3750根独验1.824719026 CPU秒。最终形式化记录中的decoder批59.373935 CPU秒/墙钟59.081401秒、exact批2.779395 CPU秒/墙钟2.869179秒，是末次对应批次，不能当整个Lean开发总时间。

原料：[机制/来源交接](../context/dd-two-successful-methods-20261101/DD_TWO_METHODS_HANDOFF_20261101/TWO_SUCCESSFUL_CONSTRUCTION_METHODS.md)、[3750证明义务链](../research/ddp/refresh_20261029/f5_full_d20_D3/PROOF_SKELETON.md)、[结果摘要](../research/ddp/refresh_20261029/f5_full_d20_D3/RESULT_OVERVIEW.json)、同目录 `PARAMETERS.json`、`generate.py`、`INDEPENDENT_VALIDATION.json`、`FINAL_COMPILE_RESULT.json`。

## 6. 直接换域被反例推翻：F25保住了秩，却丢失相邻层覆盖

从F5成功提出的预测是：同矩阵嵌入更大域会保持逆关系和满秩，是否也保持D3？推导把中央三步turn和相邻层pencil投影到二维商的同一条射影直线。四方向frame下两组三个商方向的交数为k，pencil并集恰为 q+(6−k)(q²−q)。全部turn满秩要求k=0，而pencil覆盖要求6−k=q+1，两者共同给q=5。

这不是只说旧证明不好用。原C30存在不在三角形或四圈中的external边；沿这些边长度≤3的全部路线就是前/后回退pencil。q>5时最多6q²−5q<q³，连逐边逆相容矩阵或逆相容常量位移也不能修复这个固定控制器/直线关系障碍。

实际F25单点检验进一步给反例：F5嵌入F25保持全部36turn秩，(0,0)到控制层20目标坐标(0,1,α)仍不在任何六平面中。六平面只覆盖3625/15625，缺12000是解析覆盖数，不是生成468750点图后BFS所得。

因此下一步改变端口数/控制器短路线，而不是继续把C30原模板换q。q<5的partial-rank、逐边或多路线并集仍开放，没有因证书共同域q=5就排掉F4。

耗时：C30全部900控制对/2550端口词绑定0.039213342 CPU秒，F25反例点积0.000116998 CPU秒；没有大图生成、域梯子扫描或BFS。

原料：[完整推导与反例](../research/ddp/two_successful_methods_20261101/affine_field_conditions/DERIVATION_PACKAGE.md)、同目录 `ALL_CONTROLLER_ROUTE_CLASSES.json`、`F25_COUNTEREXAMPLE.json`、`PREDICTION.md`、`check_once.py`、`check_F25_counterexample.py`。

## 7. 改为五端口C60：F7成功；F4共享矩阵失败后释放逐边自由度成功

F7路线继承已保存Bhakar/F4t4nt作者的60点五端口控制器，只继承控制器，不冒用其F3图为本地新图。五个conic方向在每条中央边给前后两组四个商方向，恰组成PG(1,7)全部8点，覆盖7+8(49−7)=343。六张chart按真逆绑定，包括自逆matching端口两端分别使用T和T⁻¹。全部3300非邻/同层对有NB3，300相邻对由pencil覆盖，得到20580点、35正则、360150边、恰D3。它后来被公开比较35875压过，保留合法实例，停止纪录目的微调。

F4上最初沿用“每个port一张全局矩阵”。完整60×60×16=57600个逆相容projectivity组合中，6个过forced cell门，0个能给全部3300对提供rank3路线。低秩路线在共同零坐标的并集最多61<64，使rank3条件在该固定纯线性域中是必要条件，因此这不是随手选的充分证书失败。

下一次真正改变生成规则：每条无向控制边分别选projectivity，共150个选择，反向赋实际真逆。一次有限SAT找到共同可行字面参数；重新核全部约束、300个pencil和3300个rank3路线后生成3840点、20正则、38400边图。独立全部3840根PASS，后来具体公式Lean及最终审阅完成。它没有推翻旧57600全局域排除，成功来自放开了旧域中的共享限制。

耗时：F7局部门/控制对0.040972556 CPU秒，生成0.348461891 CPU秒；独立全20580根位集R3核验1.707838828 CPU秒、墙钟1.723733秒。F4全局完整枚举0.084363529 CPU秒；此前首次准备因“首项”误作“首个非零项”在0组合处失败，其准确CPU未保存，不能说完整成本只有该小数。3840全根独验0.087418572 CPU秒；SAT及生产的具体分项沿该目录原结果读取，本页不猜总耗时。

原料：[F7全部点对证明](../research/ddp/two_successful_methods_20261101/f7_c60_d35/PROOF.md)、[F7独验摘要](../research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/SUMMARY.json)、[F4全局负域报告](../research/ddp/two_successful_methods_20261101/f4_c60_global_projective/REPORT.md)、[F4逐边成功证明](../research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/PROOF.md)、同目录 `PARAMETERS.json`、`ROUTE_CERTIFICATE.json`、`PAIR_COVERAGE.json`、`independent_acceptance/SUMMARY.json`。

## 8. D3 保边克隆：把巨大旧邻域冲突缩成小控制器负载

已有D3源给出可复用的完整原邻域克隆：新点连接旧中心c的全部原始simple邻域。新旧点对用源路径替换首端；新新点对用源路径替换两端。中心相邻时用clone(c)–d–c–clone(d)三步，中心相同的不同副本经共同旧邻居两步，因此不必假定中心独立。难点改为所有旧点承受的新增负载不能超余度。

F5源先选与四方向横截的25点平面，一块邻线分割每个目标125点层，把负载缩到30个控制器重数。6块和15块分别产生150/375克隆，得到3900和4125。后者达到该固定源完整原邻域克隆总槽界，但不是一般N(22,3)最优。

F4新源改用normal=(1,1,w)的16点横截平面，五方向点积全非零，300条弧的4800条邻线与字面源绑定。60控制器负载模型实际找到9/22块，得到3984、4192，比旧源同参数结果多84/67。12/24是计数上界，求解器报告optimal没有被擅自升级为独立最优性证明。把两份实际负载逐项相加得到31块、496克隆、4336点的23度图；重复中心必须按重数保留为不同新点。

完整独验对3900/4125分别检查全部150/375新增根，加“37500旧边全保+3750源全根D3”覆盖全部点对；不是本轮重复旧根BFS。F4克隆同样保全部源边并验全部新根；3984/4192/4336后来完成具体公式Lean，3900/4125仍没有。已试但被公开6144压过的24度4544方案在生成前取消，不是失败图或成果。

耗时：F5两个终图生产总0.399614746 CPU秒，独验总0.342881714 CPU秒/墙钟0.345150秒；F4平面块生产/求解有限批总1.589214495 CPU秒。各模型选择/形式化成本分别在原结果中，不与这些生产小数混作总时间。

原料：[通用克隆与F5证明](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/PROOF.md)、[F5两终图独验](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/independent_acceptance/ACCEPTANCE.md)、[F4横截块证明](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_plane_blocks/PROOF.md)、[两负载相加的4336独验](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_load_sums_23_24/independent_acceptance/SUMMARY.md)、[阶段八图及失败规则回顾](../expert_review_current/TWO_METHOD_RESULTS_20261101.md)。

## 9. 换源而不只是加度：opposite-GQ的flag余度与spread补点

F4升24度4544被公开6144挡住后，研究转向那个更强的几何来源。经典opposite-GQ源的顶点是点线对(p,l)，交叉incidence给邻接；删自环后，incident flags恰有一格余度。spread能否把它们分成完整R2覆盖的pin组，是新预测。

GQ(3,5)的6144点源有384个度23 flags。16条vertical spread线把它们分成16组24pins；每组覆盖全部旧点，组间有相邻flag给新新点对三步路线。实际保留73536旧边、加16点384边，得到6160/73920全24正则；16次完整当前R2检查及独立全部6160根都通过。来源6144重现不计新成果。

随后迁到balanced GQ(4,4)：7225点源有425个度24 flags，17条Desarguesian spread给17组25pins，产生7242/90525全25正则；迁到GF7的GQ(7,7)，160000源加50个64-pin点，得到160050/5121600全64正则。后者独验并非全160050根BFS：独立重建400点/400线几何、全部160000个projection前提，并逐条绑定全部5121600字面边，使一般真实Walk证明覆盖所有点对，另对全部50个新根做普通BFS。

这条推广成功依赖真实点线incidence、唯一投影、spread和字面标签全部可对齐，不是只把q换大。也不能把通用Delorme框架或经典GQ构造据为本项目新发明；具体filled源是否早已公开，仍影响公开优势是否真实。

耗时：6160生产0.195456125 CPU秒，独验约1.080653 CPU秒；7242生产0.252167557 CPU秒，独验0.243566 CPU秒。160050生产3.871704688 CPU秒，独验含编译/预检4.717618 CPU秒；其新400行/415模块具体Lean的全部尝试约6240.27858 CPU秒，说明验图很快不等于形式化成本小。

原料：[6160几何与路线证明](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq35_spread24/PROOF.md)、[7242证明](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/PROOF.md)、[160050生产报告](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/REPORT.md)、[160050独立完整数学连接](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/independent_acceptance/PLAIN_PROOF.md)。

## 10. Ovoid×spread：完整原邻域必须冻结，中心不独立也能克隆

在7242源上，显式二次型Q的17个零点构成ovoid，每条线恰交一次；与原17条spread相乘得到289个中心。raw邻域恰分割7225点，17个flag的self-entry删除并由对应bonus替换，实际289个25邻域仍不交、最大负载1。中心之间却有136条匹配边和17个孤点，说明“中心必须独立”是多余限制，但也说明不能一边加克隆一边读取演化的current N(c)，否则会把新点错误带入后续邻集。

实际先冻结原source的完整simple邻域，再加289个独立克隆，得到7531/97750，最大度26。289克隆达到该固定25正则源、cap26、完整原邻域规则的容量界floor(7242/25)，不代表N(26,3)最大。公开比较也更正为已发表通用方法保证7514，而不是只拿7225当基线；7531相对该保证仅+17。

GF7线上先有一个更小partial-ovoid方案被公开比较挡住；后改用三组立方coset：p_t^k=(1,t,t³+k,−t²)，k=0,2,4，加无穷点，共22点。B值为(t−s)³+(l−k)，由GF7立方剩余与coset差保证不共线，×50 spread得到1100个64邻域不交中心，实际产出161150。后续深读公开文献Table5发现33点partial ovoid，旧“超过公开15点方案”的比较失效；161150本身仍合法但已低于33点推论161650。

研究随即使用公开33点对象而不是继续包装22点为纪录：33×50=1650个中心，以同一冻结160050源、每个中心k重复制，k=1..15给degree65..79的15个实际终图，n=160050+1650k。相对未fill源组合公开公式各多50，但若filled源同规则已有公开，这50优势仍可能归零。它们是一套机制的15个参数实例，不是15种方法。

耗时：q4 ovoid预检0.161736872 CPU秒；7531生产0.787637899 CPU秒、独验约0.064811 CPU秒。q7三coset预检0.838462388 CPU秒、生产含准备2.032453389 CPU秒、独验最终6.753769767 CPU秒；具体Lean98.887887 CPU秒、含binding/prep108.816773203 CPU秒。P33十五图不是十五次全源BFS：两批最大图k8/k15共实际37950新增根BFS，逐图完整字面绑定与源内点路径证明覆盖其余终图/前缀。

原料：[q4 ovoid、冻结邻域及容量证明](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/PROOF.md)、[q7三coset原报告](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/partial_ovoid65_gate/cubic_coset22/REPORT.md)、[P33当前15图证据](../research-wiki/experiments/ddp-gq77-published-p33-immutable-fulln64-clone-eight-degree65-72-family-20261101.md)、[公开33点比较更正](../research-wiki/experiments/ddp-public-w3f7-partial-ovoid33-primary-table5-corrects-65-70-77-comparison-20261101.md)。

## 11. q8先做小几何预测，再产大图；重分配对角边越过固定邻接障碍

进入q8前没有直接开大图阶梯。唯一小几何pilot核了585点/585线、336960个非incident唯一投影，O65与spread65；再核Payne派生512点/640线、322560唯一投影、O64和spread64。全部通过，但此阶段只给条件规模，没有完整图，不能提前计成果。

实际选两个有竞争力的源：degree80用Payne源327680，加64个80-pin filler得327744；degree81改用balanced源342225，加65个81-pin filler得342290。这样避免继续把较弱Payne源升度到81，却被balanced公开来源压过。随后O65×spread65给4225个冻结原N81克隆，得到346515/14204970、最大度82。

固定完整N_H规则到达一类饱和障碍后，改动承重连接：删去65条对角clone到自有filler边，加一个hub连全部65 fillers，全部H旧边不动，得到346516，边数仍14204970。这与q4的7531→7532相同；它改变了旧克隆mandatory邻域，不与“固定旧邻接不能再补”的否定结论冲突。q8新图独验只重查65个改变的对角根加hub的66根，4160个不变off-diagonal根与旧根用完整字面绑定和源内点路径证明覆盖；不是宣称本轮全4226新根或全346516根BFS。

进一步把G1=346516中的4225克隆+hub视为4226个独立first roles，其完整邻域不交且都在旧H。复制的是冻结G1角色，不是原GQ中心，也不是不断增长图的current N。这样复用已有full-neighborhood引理构造83及分散选择的86/90/94/98度终点；每个命名实例各有实际边表和独立scope，不把条件参数窗口全部登记成已生成图。

耗时：小几何pilot含编译2.285789276 CPU秒；两filled源生产2.645157007 CPU秒/墙钟2.717079秒，独验10.520798412 CPU秒；346515生产2.146262777 CPU秒、独验12.395600852 CPU秒。346516对角重分配生产0.940117171 CPU秒。q8两源具体形式化全批8413.702687 CPU秒、82克隆具体形式化53.903200769 CPU秒；这些包含失败/接口修复的真实范围，不能删掉后只报最后成功模块几秒。后续角色复制的各批成本保存在各自 `replication*_batch`、独验及formalization结果中，未在本页拼成端到端加速倍数。

原料：[小几何pilot](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_geometry_pilot/SUMMARY.md)、[q8完整路线](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/PROOF.md)、[346516对角重分配](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/PROOF_DRAFT.md)、[冻结G1角色复制证明](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/multiplicity9_degree90/PROOF.md)、[q8当前终态汇总节点](../research-wiki/experiments/ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101.md)。

## 12. D4迁移：从15552字面关系恢复27点横截块，31块并非最大，32块得到16416

迁往D4时，15552源不能仅因15552=192×81就猜一个商。既有恢复材料先把648个度14点的virtual self-entry补回，得到每行五个目标控制器、每目标三点的loop-completed关系；全部960弧/77760 rowsets与字面源精确匹配，恢复真实192×F3⁴仿射接口。实际源degree14:648、degree15:14904，不是15正则。

五条输入kernel方向的第二坐标均非零，所以W={x1=0}的27点平面横截全部kernel。同一controller块的完整原邻域互不相交；若所选controller的五目标集合不交，则跨块也不交。此时每块27个fullN克隆可把cap升到16。达到已定位16384比较值至少要31块，条件规模16389；第一次找到31便停止，不等于证明最多31。

后来明确询问32块可行性，保留同一192变量/192目标负载模型，加≥32基数行，一次HiGHS找到32块，160目标labels互异。按冻结I32×W产864个克隆，保116316旧边，实际得到16416/129240、最大度16、恰D4。独立全部16416根普通BFS检查269485056个有序点对≤4，每根离心率4；新具体Fin16416 Lean/Audit与新scope审阅完成，不借16389旧PASS。

另一条同源研究显示推广边界：把字面GF4/C30限制到F2³不是合法240源，e2实际被映到(α,0,α+1)；旧signed binary/局部rank反例只关闭其真实前提，不能据此否定已经恢复的F3⁴ fullN接口。后续16417等必要模型若超时或放松可行，只保留其自身UNKNOWN/受限结论，不能将32块当已证最优。

耗时：32块求解新进程1.951147927 CPU秒、墙钟1.955020秒；含继承准备的同case累计约10.13905 CPU秒。16416新全根独验11.414157660 CPU秒；新具体Lean批14.020610885 CPU秒，含首Defs失败。它们复用了未受影响的源证明/编译，不包含从零恢复源关系的全部成本。公开比较主表/URSA描述为16384，本地+32；URSA报告全文缺口与方法优先权仍UNKNOWN。

原料：[15552源与27点接口恢复](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/NOTE.md)、[32块有限门](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/controller_pack32_gate/NOTE.md)、[16416真实Walk与离心率预测](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/PROOF.md)、[16416当前终态](../research-wiki/experiments/ddp-d16d4-whole27-fulln-clone864-graph16416-20261101.md)、[GF4误限制反例](../research-wiki/experiments/ddp-stale-d8d4-c30-gf4-binary-restriction-fivecover-input-20261101.md)。

## 13. D2迁移失败的实质：两步路线迫使共同owner、预算和奇偶同时成立

把D5/D3补点迁到D2，不能沿用较长路径的自由度。固定Brown91旧诱导图、cap11时，helper i的旧目标覆盖必须满足 V(G)=N_G[S_i]∪⋃_{j∈N_H(i)}S_j，且所有旧pin合计B≤101。粗总容量先得到h≤16，107点似乎尚有空间。

实际进一步区分36内部点、45外部点、10绝对点，追踪每个旧点的唯一owner/可重复容量；从175个line/pin profiles和小整数DP发现逐组证书。把每组覆盖缺口与helper邻居的excess预算相加，h=16必须B=101且全部helper满度，度数和16×11−101=75为奇数，矛盾。因此固定Brown91、旧诱导边不改、任意helper图的扩张至多106，不能超过已读公开106。它没有证明106扩张存在，更不是一般N(11,2)上界。

随后按用户意思改为公开106源允许删补旧边。最小4matching/no-old-repair由critical pin forcing直接排除，指定oneRepair的252 anchors全有实际旧pair反例；更一般只在10–11 pins内部重连的MILP唯一10秒运行返回UNKNOWN、无incumbent，不能记整族NO。其后找到真实order7源自同构，再纸面排除“保持该C7且只改G[S]”的S10/S11限定规则；这不能追改旧MILP为已解，也不排打破C7、非invariant pins或cross-S改边。

耗时：Brown91几何profiles/两次DP/编译已记合计2.016578981 CPU秒，短证不依赖把DP witness当图。公开106内部重连MILP相关case累计10.514675635 CPU秒，后续sector/匹配传播累计10.585169327 CPU秒；分别的纸面改进没有伪造solver终态。旧N(8,2)/n61历史队列未因此恢复。

原料：[Brown91完整解析证书](../research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/PROOF.md)、[公开106当前scope与UNKNOWN](../research-wiki/experiments/ddp-d2-public106-internal-pin-old-edge-repair-scoped-gates-20261101.md)、原目录 `MINIMAL4_PROOF.md`、`internal_pin_rewiring/MODEL_SCOPE.json`、`SOLVER_RETURN.json`、`paper_S11_domination/NOTE.md`。

## 14. 小图改边对照：修好一个旧pair，可能正好毁掉新根

在41点4正则D3的Messières N1源上，两条不交旧边删除、四端点接新星是最小42点规则。全部3075配置中3072新根失败；3个新根通过，却全部损坏old-old距离。首见证旧点1→33的三步路1–17–22–33因删17–22变四步1–17–41–22–33，两个端点甚至都不是pin。这说明只查新根或只查pin附近不足以保径。

换N2/N3只作真实不同源对照，各3075全访，N2有6个新根通过但旧旧失败，N3无新根通过。再围绕那6个N2基例试指定第三cut、一次old-old repair和一次star端口替换：3048个参数中426修好了保存的旧pair，但426全部失去新根R3。首例把0→1修到1步，却使新41→1变4步。有限域完整结果证伪的是“这次局部补偿能同时保两边”的预测，而不是声称坏pair完全没改善。

另一例Exoo132→134只有10000个不同样本：9997败首helper，余3败另一helper，old-old阶段没有进入。它只能记样本失败、该机制UNKNOWN，不能套N1/N2全域NO，更不能把失败归因old-old损伤。

耗时：N1全域含接口0.350856972 CPU秒；N2/N3原批1.503331119 CPU秒；指定3048 repair批0.249139578 CPU秒。Exoo132样本1.872316415 CPU秒，旧sourceD6全根BFS没有重跑。这些完整有限域或样本停止后没有自动换seed/增repair/扩大cut。

原料：[N1原报告](../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/NOTE.md)、[N2/N3源对照](../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/NOTE.md)、[426修好旧pair却毁新根](../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/NOTE.md)、[Exoo132样本边界](../research-wiki/experiments/ddp-stale-d3d6-exoo132-adjacent-helpers-repair134-sample-20261101.md)。

## 15. 老题攻关中的三类障碍：端口根本到不了、路线被破坏、共享参数不能兼容

老题清单按保存主表年代与Moore空间选择15格，但年代久、上界差大都没有被当作可实现保证。这里保留三种代表失败，使后续能知道应换什么，而不是只看到“都没成功”。

第一类是保边接口先天无覆盖：3645源全部7个free ports的R3漏743旧core，关闭任意保边helper扩张；585源的实际3-(65,9,1)设计把所有finite helpers的core可达数压到462<520，甚至允许额外old-old边也无解。必须删改旧边或换源，继续同源换helper数量不能改变结论。

第二类是删边路线补偿受联合预算限制。CM253→254四cut八星每类27必要义务、余三cut最多18，排纯星。五cut加一repair独立容量一度35≥27，原容量否定预测被反驳；把repair和实际两halfcut邻端绑定后完整7640544合法半选择联合上界24<27，才关闭该指定一repair规则。独立最大值相加不能代表可同时实现的候选。

第三类是路线容量够、单槽也都可满，但共享选择冲突。固定C8作用Z32的256点规则有457个≤3逆码非回退词，各phase不同形式46–63≥32；57344个连通规范参数全访，单phase都存在满32参数，phase0和2共同满却为0。此处应该改变连接参数共享结构，不是继续改善总缺项。最小冲突的真实proper-subset witness、每槽覆盖和全域表均已保存。

相邻的一条新D5机制更能防止过度排除：fixed binary240普通C23的四global系数12720案严格NO；改逐实际边电压后66路线变成66不同flow、差rank65，22个独立差方程构造出一个packet满23，确实去掉旧局部障碍。全packet容量门也过，但32个固定条件全局样本仍无完整D5。该逐边家族和22方程仿射空间都保持UNKNOWN；下一问题是多packet兼容，不能把32个样本升级为全C23-cover不可能。

耗时：3645最近singlecut最大star全20044旧边新根门失败及后处理累计2.943111119 CPU秒；CM253纯星/联合repair累计3.686201072 CPU秒；global256完整主批2.080238239 CPU秒、一次旧表兼容后处理后累计2.274279767 CPU秒；binary240/C23从旧global门到逐边局部构造、全flow门和32样本累计5.704705500 CPU秒。它们没有新合法图，不能以packet满数或必要义务少了多少冒充普通坏点对改善成果。

原料：[3645纯保边障碍](../research-wiki/experiments/ddp-d11-d4-free7-monotone-barrier-20261027.md)、[585完整定理](../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/THEOREM.md)、[CM253联合repair完整证明](../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/FINAL_PROOF.md)、[global256最小冲突](../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/NOTE.md)、[C23局部成功与全局UNKNOWN](../research-wiki/experiments/ddp-d5-fixed-binary240-four-global-coefficient-c23-cover5520-complete-no-20261102.md)、[15个老题当前清单](../research/stale_record_candidates.html)。

## 16. 这些轨迹尚不能自动证明什么

完整图、一个参数族、一个构造机制、一次独验、一次形式化、一次公开比较是不同记账对象。103个D5前缀来自三个参数序列，不能叫103种方法；P33的15个k终点是一套复制规则，不能因有15份具体Lean就说学会了15种新构造。公开源的重现、条件参数公式和已取消候选都不计完整新图。

同样，验图/检查器的CPU小数不等于发现这张图的总耗时。q7/q8的有限前提、Lean实例化和接口修复成本远大于边表生成；保存失败准备、timeout/UNKNOWN、重复调度纠正和未返回审阅，是理解实际研究过程的原料。原始记录中哪些调用是静态阅读、哪些实际运行，不能因模型写了PASS就互换。

对于公开先进性，现有轨迹已经出现两次实质纠正：13D5的88452作者包，以及W(7)公开33点partial ovoid。它们不撤销本地图合法性，却改变“新纪录”的说法，也直接改变下一次选源和中心集合。对比一个主表缺项或“本轮未搜到更大”不足以认证全球最大。当前公开来源缺口、同规则优先权、已有公式代入保证，都应随结果保留。

后续提炼可以从这些已经发生的变化开始：几何结构怎样代替局部评分；共享参数怎样释放；冻结原邻域怎样避免错接新点；公开比较怎样导致取消或换源；严格NO怎样阻止重复路，UNKNOWN怎样保留真正开放接口。这里提供的是可核查轨迹和材料入口，尚未把这些内容改写成新skills，也没有宣称已实证持续自我改进或提速倍数。
