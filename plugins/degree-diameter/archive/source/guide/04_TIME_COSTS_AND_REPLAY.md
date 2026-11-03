# 逐批耗时、增量复用与复现边界

**本交付保留461项研究记录的时间原文和可定位的结构化计时。已经能够回答“某批搜索、构图、独验或Lean实际用了多少资源、后来怎样避免重复工作”；现有记录不足以给出没有缺项的全研究总耗时。** 代表实例中，3750点F5图的确定性生成为0.106812 CPU秒、独立全源验图为1.824719 CPU秒；16416点D4图的增量构图为0.223061计费CPU秒、独验套件为11.413770 CPU秒、该新实例Lean为14.020611 CPU秒。另一方面，Q8两个大源图的完整有限Lean闭合确实用了8413.702687 CPU秒，成本没有被忽略。

以上数字分属不同工作范围，不能拼成“几秒完成全部研究”。下面把原字段、实际作用域、共享成本和可复现入口逐项列清。

## 1. 先读两张索引，再沿原始记录看时间

- [逐实验计时：timings_by_experiment.csv](timings_by_experiment.csv)保存461行记录，保留原`source_record.duration_raw`、结构化CPU／wall字段JSON及其源路径；空值保留为空。
- [研究轨迹：trajectory_index.csv](trajectory_index.csv)同为461行，连到输入、实际范围、结果、经验与重启条件。时间必须与这张表的工作范围合读。
- [原始唯一研究账本](../research-wiki/DDP_METHOD_LEDGER.json)保留原记录。当前461行中，`source_record.duration_raw`只在92行出现，89行非空；后续很多有效时间存在实际RESULT／TERMINAL／FINAL中，而不在这个早期文字字段里。**字段空缺不代表没有耗时。**

`duration_raw`不能机械抽一个数字当秒数。例如原账本实际含有：

| 原记录 | duration_raw原文示例 | 应怎样读 |
| --- | --- | --- |
| `ddp-affine-cayley258-20261026` | `4.095573 production/prep +0.004713864 independent CPU s` | 生产／准备与独验的两个CPU范围；继续沿各自证据看是否已被累计字段包含 |
| `ddp-affine816-full-closure-20261027` | `966.507956720CPU` | 某次闭合记录的CPU，范围由原报告确定，不按标题猜成全部该方法历史成本 |
| `ddp-m1-first-profile-20261026` | `60 wall seconds per process` | wall且按process计；不能直接当总CPU |
| `ddp-m1-d7-first-profile-20261026` | `120s each` | 单位／实测还是预算尚需原记录澄清，不能默认每项都实际跑满 |
| `ddp-m1-d5-prunings-20261026` | `8 explicit candidates` | 这是候选数，不是8秒 |

不需要重新抄写461项；本篇提供读原始时间和发现复用机会所需的代表实例。

## 2. CPU、wall、预算和等待分别是什么

| 名称 | 本项目记录中的含义 | 常见误读 |
| --- | --- | --- |
| CPU秒 | 进程实际消耗的处理器时间；部分driver通过子进程回执／`wait4`累计，具体看原脚本 | 多worker的总CPU可能明显大于用户等待的wall |
| wall秒 | 从某个明确调用开始到返回的现实经过时间 | I/O、调度或冷缓存可使wall远大于CPU；也可能不包含调用前的排队和讨论 |
| CPU预算／硬限制 | 允许消耗的上限或终止门 | 预算120秒不是实际耗时120秒 |
| cumulative／accounted CPU | driver当前作用域的累计值，可能含准备、编译、失败和先前子批次 | 不能再把它的组成项逐个相加一次 |
| preparation charge | 对未精确观测到的准备成本作出的明确保守记账 | 与`actual_process_CPU_seconds`不同，不能伪称全部是实测process CPU |
| LLM／外审等待 | 模型请求、服务排队、生成与返回消费期间的经过时间 | 本地脚本CPU不能代表远程模型耗时；SUCCESS或threadId本身不提供时长 |
| 人工等待 | 等待研究策略反馈、专家、登录或交付确认等 | 当前没有统一完整的计时日志，不把它按0计入“端到端总时间” |

目前缺少贯穿所有会话的完整LLM wall、token／金额、人工等待和统一硬件占用记录。文件日期、研究起止日期、某次终态时间，也不能直接补出这些缺项。能够可靠报告的是有原件支持的批次成本和完整范围。

## 3. 早期F5／3750：生成很快，发现与形式化是另外的工作

源目录：`research/ddp/refresh_20261029/f5_full_d20_D3/`。

| 实际阶段 | 原字段／数值 | 已做的具体工作 | 精确原记录 |
| --- | --- | --- | --- |
| 互补矩阵／局部接口实验 | `cpu_seconds=0.059301383` | 四端口局部互补输入得到支持；不是完整图验收或全项目搜索时间 | [f5_complementary_triples/RESULT.json](../research/ddp/refresh_20261029/f5_complementary_triples/RESULT.json) |
| 确定性构图 | `CPU_seconds=0.10681173599999999` | 写出3750点、37500边的完整字面图并检查生产定义与度数；本阶段不跑BFS | [GENERATION_RESULT.json](../research/ddp/refresh_20261029/f5_full_d20_D3/GENERATION_RESULT.json) |
| 独立全源验图 | `CPU_seconds=1.8247190260000001`，预算30 CPU秒 | 由字面边表重新建立邻接，全部3750根D3通过；没有重验旧103个图 | [INDEPENDENT_VALIDATION.json](../research/ddp/refresh_20261029/f5_full_d20_D3/INDEPENDENT_VALIDATION.json) |
| 早期controller decoder编译失败 | `CPU_seconds=123.903922`，`wall_seconds=86.27546058222651`，预算120 | 真实失败成本，结果`COMPILE_FAILURE`；不能用后续成功覆盖掉这次费用 | [FORMAL_CONTROLLER_DECODERS_RESULT.json](../research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_CONTROLLER_DECODERS_RESULT.json) |
| 早期split decoder编译失败 | `CPU_seconds=110.762498`，`wall_seconds=96.92005342245102`，预算110 | 同样是保留的失败尝试 | [FORMAL_SPLIT_DECODERS_RESULT.json](../research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_SPLIT_DECODERS_RESULT.json) |
| 最终decoder成功批 | `final_decoder_batch.CPU_seconds=59.373934999999996`；`wall_seconds=59.081401117146015` | 900个控制器单元、4500个NB decoder及500个相邻decoder所需的最终核验证据 | [FINAL_COMPILE_RESULT.json](../research/ddp/refresh_20261029/f5_full_d20_D3/FINAL_COMPILE_RESULT.json)及[实际decoder回执](../research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_KERNEL_DECODERS_RESULT.json) |
| 最终exact成功批 | `final_exact_batch.CPU_seconds=2.7793949999999996`；`wall_seconds=2.869178894907236` | 收束真实Walk上界与非D2的具体原目标 | [FINAL_COMPILE_RESULT.json](../research/ddp/refresh_20261029/f5_full_d20_D3/FINAL_COMPILE_RESULT.json) |

这里0.106812秒回答的是“参数已经确定后写出这张图需要多久”，没有包含此前寻找和放弃其他构造的研究时间。最终两个成功批也不是整个Lean开发成本：早期失败、基础模块、接口准备等另有日志。不能只摘最后成功编译的几秒，称整个发现过程完成于几秒。

这个实例留下的实际转折是：**保持原图定义和原证明目标，通过Array表示与证明项归约方式的调整，完成了之前因资源限制失败的核验证据。** 已有[最终证明核对](../research/ddp/refresh_20261029/f5_full_d20_D3/PROOF_AUDIT.md)明确记录这一过程。它值得下一版继承，但原记录没有给出一个排除其他同时修复因素的整系统效率A/B。

## 4. F4／C60／3840：解的搜索、快速图检验和昂贵kernel核验是三类成本

### 4.1 已保存的实际时间

| 实际阶段 | 原字段／数值 | 作用域与包含关系 | 精确原记录 |
| --- | --- | --- | --- |
| 本次兼容参数搜索＋生产 | `whole_CPU_seconds=1.609514885` | 该次完整准备、一次求解、生产的driver作用域；预算60 | [TERMINAL.json](../research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/TERMINAL.json) |
| 上行中的SAT子项 | `solver_CPU_seconds=0.23352299999999998`；`prepare_CPU_seconds=0.848586814`；`driver_CPU_seconds=0.527405071` | 这些已经属于whole，不能再加到1.609514885之后 | 同一TERMINAL |
| 全3840根独验 | `CPU_seconds=0.087418572`；`wall_seconds=0.09082318842411041` | 字面简单性、度数与全部3840根R3；是具体独验实现的实测，不与F5的Python验图实现直接比较倍数 | [independent_acceptance/SUMMARY.json](../research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/independent_acceptance/SUMMARY.json) |
| 当前Row00成功试跑 | `29.266997` CPU秒 | 已核的第一行证书，后续59行批次明确不含此项 | [NEXT_FORMAL_OBLIGATION.md](../research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/NEXT_FORMAL_OBLIGATION.md) |
| 后续Rows01–59有限证书批 | `finite_batch.completed_CPU=2020.3118519999998`；`wall_seconds=698.8453323058784`；`completed=59`，`workers=3` | 三worker累计CPU与现实wall分列；不要将59行各自CPU再加一次 | [formalization/FINAL_COMPILE_RESULT.json](../research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/FINAL_COMPILE_RESULT.json) |
| 最终装配模块 | Certificates `5.049542000000001`；Diameter `2.03543`；Exact `2.141916`；Audit `2.1321079999999997` CPU秒 | 原`final_modules[]`的四个独立末端模块；不是再证明所有有限行，也不是全项目总额 | 同一FINAL的`final_modules[]` |

上述1.609515秒只包含找到当前共同可行参数的那次生产范围。此前全局同port选项的失败、路线表示调整、理论推导和外审均另有记录。图的快速全源检验，也不能代替kernel内将任意源坐标、控制器点对及具体定义接成原定理的工作。

### 4.2 已有实测支持的表示改进

[BUILD_NOTES.md](../research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/BUILD_NOTES.md)与[CHECKPOINT_B.md](../research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/CHECKPOINT_B.md)给出了足够具体的原料：

- 首次Field尝试约182.9秒wall、3.77秒CPU，主要是冷`.olean`读取，同时还发现缺少导入等接口问题。这说明wall与CPU不能互换。
- 保存参数中的长平坦数组改写为按控制器嵌套、字面元素相同的表示。旧失败稿34.59 CPU秒与后续成功10.47 CPU秒并非只有一个变量变化；它们可说明开发转折，不能据此孤立声称某改动带来固定倍数。
- RouteData在旧表示下成功编译约51.92 CPU秒，首次有限行约52.79 CPU秒；将重复矩阵和decoder无损放入紧凑池后，记录为RouteData约12.18 CPU秒、同一Row00义务约29.27 CPU秒。
- 紧凑表仍有数学绑定：3600个NB逆矩阵入口选自402个不同矩阵，300个相邻dart选自25个不同64目标decoder数组；`FastTables.matrix_eq_fast`在kernel中证明紧凑查表与全部原矩阵相等。图语义和有限检查没有通过压缩而被删除。
- 已成功的昂贵有限模块被保留；修复消费者接口或拆分后续行时不重新编译未变化的已通过模块。59行在3个worker下完成，解释了累计CPU约2020秒而wall约699秒。

这些是可以直接提炼成工程经验的局部前后记录。它们支持“减少重复字面展开、把共享证明与有限输入分开、保留成功模块”；尚不能推出MathRSI整体研究速度提高了多少。

## 5. D16／16416：先前源图成本与新实例增量成本分开

源目录：`research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/`。

| 实际阶段 | 原字段／数值 | 读数要点 | 精确原记录 |
| --- | --- | --- | --- |
| 32个controller块的可行性搜索 | `solver_CPU_seconds=1.951147927`；`solver_wall_seconds=1.9550197087228298` | 一次零目标可行性求解，返回足够的32块；不是最大packing大小的证明 | [controller_pack32_gate/RESULT.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/controller_pack32_gate/RESULT.json) |
| 该搜索门的记账总额 | `cumulative_charged_CPU_seconds=10.13869782`，其中`prior_sourcepacking_CPU_seconds=7.714861215`；`actual_new_process_CPU_seconds=2.223836605`，准备charge `0.2` | 原记录已说明包含旧source-packing成本，不能再加一次7.714861215或solver子项 | 同一RESULT |
| 冻结选点后的构图 | `CPU_seconds=0.223061134`，其中`actual_process_CPU_seconds=0.123061134`、准备charge `0.1` | 只读15552旧源一次，生成16416完整图；没有重验旧源、旧field/rank或跑solver | [degree16_plane864/RESULT.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/RESULT.json) |
| 新终图独立验收套件 | `total_suite_CPU_seconds=11.413770046` | 包含本套件准备／编译／独验；预算120 | [degree16_plane864/independent_acceptance/RESULT.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/independent_acceptance/RESULT.json) |
| 上行中的validator与BFS | `validator_CPU_seconds=8.83664`；`all_final16416_BFS_CPU_seconds=8.76858` | 全部16416根真实终图BFS；两个字段是套件的内部工作范围，不能与11.413770046累加 | 同一独验RESULT |
| 本新实例Lean | `CPU_seconds=14.020610885000002`；5次尝试，1次失败，4个PASS模块 | 新Fin16416目标、输入绑定、Exact与Audit；`old_PASS_Lean_recompiles=0` | [degree16_plane864/formalization/FINAL.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/formalization/FINAL.json) |
| 先前15552源及16389的完整形式化批 | `CPU_seconds=675.7776571089998`，其中`base_pilot_CPU_seconds=112.39300934000002`、`new_compilation_CPU_seconds=562.8593889999999`等 | 这次已有源图的完整闭合为16416增量提供前提；不能隐去，也不能当作每个新图都重复支付的成本 | [degree16_plane837/formalization_full/FINAL.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane837/formalization_full/FINAL.json) |

下一版可以继承的具体做法是：固定字面旧图的完整邻域和已经闭合的真实Walk定理，对新实例只证明新选择的160条controller-owner方程、864个新角色及其12924个pin绑定，再调用同一个通用克隆证明。旧16389的“图PASS”没有被挪用为16416的“图PASS”；后者有自己的实际终图独验和新具体目标。

这能说明成本怎样分摊，以及为什么一个新实例的Lean只需14.02 CPU秒。675.78与14.02覆盖的数学义务不同，不能直接相除宣称“系统加速48倍”。

## 6. Q8：8413.702687 CPU秒的首次完整闭合被如实保留

### 6.1 图生产和数学验图

| 实际工作 | 原字段／数值 | 实际范围与包含关系 | 精确原记录 |
| --- | --- | --- | --- |
| 80／81度两个filled源的生产 | `accounted_CPU_seconds=2.6451570069999994`；`wall_seconds=2.7170787528157234` | 编译、两个生产子过程与wrapper的记账范围；单看cases中的0.820927／0.85992会漏掉编译等 | [even_q8_gq_source80_81/RESULT.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/RESULT.json) |
| 这两个源的独立验收套件 | `total_CPU_seconds_including_geometry_data_binding_compile_four_files_129helper_BFS_and_aggregation=10.520798412`；`wall_seconds=10.679506301879883` | 四份实际文件绑定、编译、129个helper新根BFS及汇总；旧点对由完整GQ路线证明覆盖 | [independent_acceptance/TERMINAL.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/TERMINAL.json) |
| 上行的validator子项 | `validator_CPU_seconds=8.91291` | 已包含在独验套件，不再额外累加；64／65个helper根分开保存 | [independent_acceptance/RESULT.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/RESULT.json) |

129个新根、完整字面绑定和旧点对路线证明共同支持这两个完整图。实际并未从327744或342290个旧／新根全部重跑BFS；记录中的这种节省有确定的覆盖理由，不等于省略尚未证明的点对。

### 6.2 首次完整有限Lean批

[formalization_full/FINAL.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/formalization_full/FINAL.json)明确记录：

- `CPU_seconds=8413.702687096991`，总预算12000 CPU秒。
- `pilot_separate_CPU_seconds=40.105386447`：先前两模块pilot单列，不藏在“无需成本”的前提里。
- 1104个新模块PASS，完整669905个projection pair；其中pilot已闭合1225个，其余668680个由1095条新projection row覆盖。
- hline完整10385个位置、howner完整1097个位置；最终两个具体原目标无用户证书前提，独立Audit通过。
- `failed_module_attempts=6`，包括assembly stack overflow、tactic import问题、受控成本重评及graph alias instance错误；失败分类和每次原日志均保留。
- `old_modules_modified_or_recompiled=false`、`large_graph_files_read_in_formal_batch=0`、`BFS_in_formal_batch=0`。

这个累计CPU来自原driver的作用域，不是两个源图的每图CPU，也不是整个项目总CPU。原FINAL没有给与这8413.702687完全同范围的总wall字段，不能把它直接说成用户等待了2.34小时。多worker CPU、远程模型等待和现实经过时间应继续分开。

### 6.3 成本重评怎样实际改变运行

[COST_REASSESSMENT.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/formalization_full/COST_REASSESSMENT.json)记录暂停点已花`558.405518791` CPU秒；当时有49个PASS模块，48个保持不变。实际测得一条packed row为`7.353664` CPU秒，再据剩余1047行估计后续成本`7699.286208`、含bridge的全批约8500 CPU秒。原字段明确`estimate_is_guarantee=false`，最后实际累计为8413.702687。

[原README](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/formalization_full/README.md)解释了可复用的细节：先前47条成功row保留原NatTable；其余采用同一witness按base4194304、每32项分块的紧凑表示；两个Inputs用纯core `Fin.cases`装配。完成的row不重新编译。末端Exact/Audit遇到native stack overflow后，用Lean `-s65536`调整线程栈；这不改变原数学目标，也不提高每模块60 CPU秒的硬限制。

因此，这里已有“实测小行→重估余量→改变表示／装配→保留成功结果→完成原目标”的完整转折。它没有让第一次完整有限证明变成零成本，也不是整套agent的效率A/B。

### 6.4 继承Q8源以后，后续图只支付对应增量

| 后续具体目标 | 已记录的Lean CPU | 新增范围 | 原记录 |
| --- | ---: | --- | --- |
| 82度346515 | `53.90320076900001` | 四个新模块；已闭合的Q8源模块不改、不重编 | [balanced_full_ovoid_copy82/formalization/FINAL.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/formalization/FINAL.json) |
| 7532与346516两项共同新批 | `108.23453976900001` | 共13个新模块、16次尝试含3次失败；旧projection／geometry／field重跑0 | [diagonal_fill_reallocation_formalization/FINAL.json](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/diagonal_fill_reallocation_formalization/FINAL.json) |
| 上行的两个case模块子项 | Q4 `14.510148`；Q8 `77.88688200000001` | 两项已经属于108.234539769共享批，不能各再加一个shared batch | 同一FINAL的`claims[].case_module_CPU_seconds`与`shared_batch_CPU_seconds` |

这种记录能让后续系统看到真正值得继承的东西：昂贵的完整源图证明先闭合一次；新增图保留原源，证明明确的新角色与局部delta，复用原Walk、度数负载和finite输入接口。省去的工作由已有证明保证，不靠减少目标或把未验证数据当假设。

## 7. 外审和模型等待：保留真实结果，时间缺项明确留空

本项目有实际跨模型外审记录，但本地进程CPU无法代表远端模型消耗。此次核读的F4、Q8及16416最终raw回应保留`status`、thread、请求模型／实际标签、effort与完整正文，未提供统一的elapsed／wall字段。

可定位的代表包括：

- [F4最终C raw](../research/ddp/two_successful_methods_20261101/reviews/F4_FINAL_C_GEMINI_RAW.json)与[处置](../research/ddp/two_successful_methods_20261101/reviews/F4_FINAL_C_DISPOSITION.md)：早期A、B因输出限制ERROR且没有实质意见，最终C读取实际最终源码与已有回执返回SUCCESS；失败没有被改写成PASS。
- [Q8三目标最终C raw](../research/ddp/two_successful_methods_20261101/reviews/Q8_THREE_TARGETS_FINAL_C_GEMINI_RAW.json)与[处置](../research/ddp/two_successful_methods_20261101/reviews/Q8_THREE_TARGETS_FINAL_C_DISPOSITION.md)：一次shared调用检查三目标，不应计成三次独立服务等待。
- [16416最终C raw](../research/ddp/two_successful_methods_20261101/reviews/D16_D4_16416_FINAL_C_GEMINI_RAW.json)与[处置JSON](../research/ddp/two_successful_methods_20261101/reviews/D16_D4_16416_FINAL_C_DISPOSITION.json)：`paid_calls=1`、`retry=false`、实际distinct fresh thread；这个“1”是调用次数，不是1秒或1美元。

这些外审是静态读取源码和已执行回执，没有再次跑构图、BFS或Lean。若以后从宿主日志补出某次请求的开始／结束时间，应保留原范围和服务故障；目前不以文件修改时间推算统一等待时长，也不按0补齐。

## 8. 哪些耗时能够复现，哪些边界必须一同继承

### 8.1 完整图的确定性重建

源码入口在`constructors/`，原大边表由保存参数与生成器按需恢复：

```sh
python3 constructors/late_graphs/rebuild.py --list
python3 constructors/late_graphs/rebuild.py --case d20_D3_n3750 --output /new/output/graph_d20_D3_n3750.edges
python3 constructors/late_graphs/rebuild.py --case d16_D4_n16416 --output /new/output/graph_d16_D4_n16416.edges
```

早期103个D5前缀使用`constructors/early_d5/`的保存基图、families与重放入口；后期50图使用`constructors/late_graphs/`逐项映射，47个既有具体Lean图均在后者。部分P33/Q8原生产器按批生成多个端点或同时生成classical源，中间工作目录可能产生大边表；这些输出在新目录中生成，不要求它们全部装入本ZIP。

这重放的是已经保存的确定性构造，通常不用重跑发现时的SAT、选点搜索和失败路线。**重放用时可以衡量生成器和参数包是否好用，不能冒充发现该构造所花的研究时间。** 新机器的CPU、编译器、I/O和缓存不同，也不保证重放等于历史原秒数。

### 8.2 字面图核验与数学覆盖

确定性生成、字面绑定、全源BFS、只验全部新根并继承旧点对，以及Lean证明是不同工作。本篇表格说明每次实际做了哪一种。需要重新验收时按原作用域使用对应源图和证据，不能把“保留旧图”未经证明扩成“任意改边后旧点对都不用检查”。

`--compare`比较已保存字面图与新生成文件的整数行流，不生成哈希。只比较边表不能单独证明直径；原独验器和原数学覆盖证明均有各自作用。已复用的完整源／kernel结果若未受改动影响，可以继承；输入或规则改变时再检查受影响的部分。

### 8.3 Lean重放

原工程使用已有Lean4.24.0及匹配Mathlib依赖。源码与原命令／日志可交付，工具链、第三方缓存与历史`.olean`不因此变成包内自带。历史14秒增量Lean使用已经编译成功的源模块；从完全干净环境重建整个依赖闭包，会支付以前的源图有限证明成本，不能照搬14秒作为从零重建承诺。

原`driver.py --resume`、历史live handle或旧Goal入口是恢复材料，不是当前要求重新启动的任务。已存在FINAL且所有过程终态时，应先读FINAL／CHECKPOINT，再由新任务明确选择要复现什么；不能机械恢复原已闭合队列。

### 8.4 本轮打包检查单列

根代理本轮重新从打包原基图检查103步当前完整R4覆盖和度数，记录约`2.851 CPU秒／27.7 wall秒`；这是本次源码交付的检查，不是2026年早期发现103个前缀的原研究时间。具体终点边表比较和本轮代表重放范围以交付根说明为准。

压缩ZIP、复制材料、生成HTML或编译验证器的本轮包装开销也只属于本轮。原研究的构图、独验、Lean、外审等待各保留自己的时间，不因重新交付而重复归入新发现。

## 9. 怎样从这些原料提炼有用的加速经验

下一套系统可以从以下已有转折抽出实际规则：

1. **先把同一义务换成较小、可检查的表示。** F5的Array调整，F4的matrix／decoder紧凑池，以及Q8的packed witness块，都有原源码、失败和成功回执；保存到原定义的证明绑定，避免用“压缩”删掉真正要验的情况。
2. **先测一个真实非平凡输入，再决定怎样扩大。** F4当前Row00、Q8一条packed row、D16的一个足够可行选点集，实际改变了后续批次。试跑结束后直接消费其成本与结果，不要求所有问题都追求更大的搜索最优值。
3. **将一次性的源证明与后续实例增量分开。** 完整源图、field／geometry、通用Walk定理通过后，后续只补新选择、新角色和新的有限绑定；复用的前提、实际新成本与首次共享成本同时记录。
4. **保留失败与累计边界。** 早期编译失败、后续修复和预算重评都有真实费用；相同累计字段在多个摘要出现时只计一次。把超时／UNKNOWN和严格排除范围放回轨迹索引，才知道下一次是否值得重启。

目前这些材料支持局部表示改进、有限证书组织和增量复用的具体判断，尚未执行“冻结策略与持续学习策略”的系统效率A/B。本交付提供的是继续检验和提炼所需的完整可定位原料，不把局部成本差异包装成已经证明的全系统RSI速率增长。
