**最大度数 8、直径 2：研究进展**

更新：2026-10-19 04:13:02 UTC。n61纸面推进：h6不同端口必为匹配，整个双C端口情形已排除；全阶仍开放。

**当前任务：n61端口进入六点集合后的共同配边**

**现在主力研究的是n61，连续数学推导优先，Lean后置。**&#x6CA1;有超过57点的目标图，数学区间仍为57≤N(8,2)≤61；这次有完整子情形排除，但不是整个61点问题已解决。

| **本次新增**                                                 | **实际剩余**                                             | **下一动作**                                         |
| -------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------ |
| h6的两个端口不同时，三组六点集合之间必须全部完美匹配；两个端口不能同时在集合之外。这是对原分支的一般配色证明。 | 至少一个端口在集合内的h6仍开放；共同端口、一般h5及没有双重缺陷的全图也未解决。旧RAW证据缺口保持。 | 沿真实父边继续推恰一端口在集合内、两端口都在集合内的情形，保留所有父点项，推到短矛盾或明确卡点。 |

这里h是两组五点父集之间的边数；“端口”是根的剩余缺陷所在点。W是三组六点集合的并，C是它们之外的剩余点。位置和配边均由原图强迫，没有另加反射或规整配色。

**新增证明的核心：**&#x82E5;三组之间有两份额外重复，特殊父类的交集先被迫有三个重复点，第四点却无论放在哪里都会违反实际父边的零缺陷要求。因此额外重复不可能，三组之间只剩完美匹配。再假设两个端口都在C，六个不同重复点中有三个最终都必须接向同一端口，而该端口最多只有两条C边，矛盾。这次连父集相交的可能也保留了，没有沿用只在前一情形成立的限制。

**这对下一步意味着什么：**&#x6B64;前整个h7可合法换根到h6，且至少一个新端口在C；结合本次排除，它只能进入恰一端口在W的剩余问题。h7仍是被归约，不是已经整体排除。K三点交集的旧换根循环已被本次证明覆盖，不再沿这条已关闭支线继续。

**执行方式：**&#x4E3B;线先连续推完一条证明链，中间检查不作为逐步等待关卡；结论落盘前只检查承重步骤。现有两个数学助手均在做n61，旧名称twofactor58不代表恢复58点支线。

**证据与运行：**&#x65B0;结论是本地纸面证明，未新增求解、外审或Lean。此前完整61点模型的唯一检验仍为UNKNOWN（88.006871 CPU秒／88.150863墙钟秒），无模型或排除证据，无solver或MCP在途。58/60已失败模板保持停止。

[不同端口必为完美匹配](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/H6_DISTINCT_PORTS_MATCHING_THEOREM.md) · [双C端口完整排除](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/H6_TWO_C_PORTS_ZERO_W_DEFECT_EXCLUSION.md) · [父行与中间短矛盾](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/H6_TWO_PORTS_PARENT_CAPACITY.md) · [总传播与其他范围](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/NONADJACENT_DOUBLE_DEFECT_PROPAGATION.md) · [进展与用户comments](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md)

历史阶段（展开查看已完成结果与旧实验记录）

以下均为历史阶段，按当时的结论与证据等级保留。旧计划、下一步和在途状态只说明该阶段的进程；实际剩余与下一动作以上方置顶说明为准。

**历史阶段 · 同端口短排除与h7到h6归约**

**主力已放在连续数学推导，Lean继续后置。**&#x8FD9;段没有新增求解、外审或形式化。此前完整61点共同模型的唯一检验仍是UNKNOWN。数学区间仍为57≤N(8,2)≤61，没有找到超过57点的目标图。

| **本次新增**                                                                                   | **实际剩余**                                                              | **下一动作**                                                                 |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| h5两根的两个特殊点完全相同时，只要一个在三组六点集合之外，就有短矛盾。h6两个特殊点不同且有一个在集合内时，三组之间必须全部完美匹配。另已证明完整h7可以合法换根到h6不同端口。 | h5/h6的完整共同配边仍开放，没有双重缺陷的图也仍开放。h7是被归约到待解问题，不是被排除。旧RAW认证缺口保持；不能给可信完成百分比。 | 集中研究h6不同端口都在集合外、且有两份额外重复时，两个额外点剩余的四条真实邻边如何同时覆盖两套父点。配色自由，先找短矛盾；其余h5/h6保留。 |

这里h是两组五点父集之间的真实边数；“端口”指根的剩余缺陷所在点。它们的位置、颜色和配边都来自原图，不是预选模板。

**新增短矛盾：**&#x68;5两根共享同一对端口时，若只有一个端口进入三组六点集合，保留父点项的交换公式一方面要求两端口之间缺陷为零，另一方面又强迫它们共用两个父点，直接冲突。结合此前两点都在集合外的四点缺陷分量矛盾，现在两个端口必须都在集合内；这个剩余仍未解决。

**h6的真实配边限制：**&#x82E5;两个不同端口有一个在集合内，还存在两份额外重复，交换公式会强迫它们共用同一父点。但某个额外点总共只有五条路线去覆盖五个父点，重复用掉一条后最多覆盖四个，矛盾。因此三组之间只能全为完美匹配。此前“共端口在集合外”的6≤5短排除也继续有效。

**换根减少重复研究：**&#x68;7的六份重复被迫落在两个各含三点的父色格里，由此能找出另一对真实双缺陷根。已逐项证明新根仍无三角、双缺陷两端仍孤立，且新h恰为6、两个端口不同。于是本分支后续可集中h5/h6，不用把h7两种形状另开研究；这一步本身没有证明图不存在。

**下一问具体在哪里：**&#x5728;h6双外部端口且有额外重复的情形，两端口不能共享父点。两个额外点各自剩余的两个邻点，都必须同时覆盖同一对U父色和同一对V父色。要检验的是这些真实无向边能否与其他匹配及内部边共同覆盖全部点对；不能只选一种二点排列后排除它。没有额外重复的情形及一般h5仍保留。

**尚未跨过的难点：**&#x68;6共端口只属于一个六点集合时，已得父边和三个邻点的双父色横截，但尚无矛盾或合法新根。h5两端都在集合内也有换根后回到原类型的情形，未当作排除。

**证据与实际运行：**&#x4E0A;述新推导为根和数学代理完成的本地纸面证据，未借旧回执声称外审或Lean。此前相邻双缺陷的一般35点分支已有独立证书关闭。最近完整模型504158变量、1816574子句，唯一发现88.006871 CPU秒／88.150863墙钟秒，正常UNKNOWN；没有solver或MCP在途，没有加时或重跑旧SAT。

[传播、短矛盾与下一配边问题](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/NONADJACENT_DOUBLE_DEFECT_PROPAGATION.md) · [h5同端口完整推导](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/NONADJACENT_DOUBLE_COINCIDENT_PORTS.md) · [h7到h6合法换根](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/NONADJACENT_DOUBLE_H7_MATCHING_STRUCTURE.md) · [单重端口的准确止点](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/NONADJACENT_DOUBLE_H6_SINGLE_PORT.md) · [进展与用户comments](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md)

**历史阶段 · ε=1证书排除与相邻双缺陷完整合并**

截至本次更新，ε=1完整输入102623变量、433048子句，全部1830真实点对共同覆盖；发现5.519699 CPU秒，另取证6.009175 CPU秒，独立检查0.162162 CPU秒，实际s VERIFIED。最终范围复核已结束，原发现RAW与独立认证分开保存。

合并ε=0，完整相邻双缺陷分支关闭。共享中心6>4矛盾另有纸面证明及直接复核；η=1的纸面必要结构作为方法止点保留，不再形成求解任务。其余61范围仍开放。

[全称合并证明及准确边界](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/EPSILON1_CHECKED_EXCLUSION.md) · [实际运行与证书](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/n61/epsilon1_single_packing_full61_run/RESULTS.md)

**历史阶段 · ε=0完整原分支的证书排除**

截至2026-10-18 16:25：两个特殊父点不相邻的完整原分支已关闭，η及全部合法配色、父类和核均自由，没有添加反射、统一排列或C5模板。完整归约与源码已核对，同一输入的LRAT经独立检查器验证；这不是整个61阶排除，也未接入Lean。

唯一发现用4.643433 CPU秒，另一次取证5.026064 CPU秒，独立检查0.136446 CPU秒；检查器实际输出s VERIFIED。该阶段计算及四轮复核均已结束。后续ε=1不借用本阶段回执，旧18点分解也不能直接套到交叠结构。

[完整分支排除及边界](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/EPSILON0_CHECKED_EXCLUSION.md) · [实际输入、取证与用时](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/n61/double_packing18_full61_run/RESULTS.md) · [18点必要归约](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/DOUBLE_PACKING18_KERNEL_REDUCTION.md) · [更早的C5两型续查](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/n61/cyclic5_joint_parent_run/RESULTS.md) · [一般配色的叶边条件](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/GENERAL_AP_LEAF_COMPLETION_DIAGNOSIS.md)

**历史阶段 · C5来源的完整续查**

**该阶段已完成的计算：**&#x65B0;续查正常完整结束，约0.009663 CPU秒／0.017840426墙钟秒，未触30／45秒预算。含继承旧图，共44个通过rho的参数表示、4800个六packing，双色中心条件合格0；后续P独立/AP判定没有在生产路径进入，不能另算一重排除。C5结果及一般叶图第1–3节已有直接复核；该阶段第4–5节仅完成本地核对。该阶段计算和MCP均已结束。

**历史阶段 · 具体规则与共同配边的诊断**

该阶段主工作是构造诊断。58点真正改动了上一证明固定的E–I关系；60点检查六正则单接口图与双接口匹配能否共同补成八度；61点把两套颜色的局部要求转成实际无向配边。三条线都先给明确规则，再检查是否真的覆盖。

**58：新规则修好新点覆盖，却至少留下7对旧点不通。**&#x65B0;的21个四元邻域把105对共享绝对点的E点改为经I相通，但同时破坏84对原有唯一I通路。即使其余指派自由，仍至少105对要靠新增匹配修复，匹配最多修98对。这是对真正改变EI的新规则的否定，一般EI重连仍开放。

**60：局部容量通过，还必须有同一组匹配。**&#x6240;选二重覆盖来源每行至少有15个亏缺目标，修复机制最多处理13个，故整个来源失败。随后给出的明确六正则图恰有13个亏缺，能通过弱筛选；但要求同一匹配全部修好时，三层之间的边数被迫为10/7，不可能为整数。该后续已完成独立核对及直接复核，没有运行搜索。

**61：得到精确的互反配边方法，但自动提供输入的规则失败。**&#x6307;定每个点的局部颜色排列后，可按互反颜色格独立匹配，保证边的两端都接受。但让同一颗星沿用同一排列的自然规则，需要10份颜色出现位置，而格容量只允许9份。放开排列仍是原共同问题，没有产生新候选。

上述推导均已获得本稿的直接范围复核。该阶段未因几条否定结论而宣布某阶更接近解决；上一轮88秒UNKNOWN保持原样，也没有据此补时或恢复旧试验。

**60点后续：完全抵消符号路线的整套机制也不行。**&#x7ECF;典根表示加本次推导，限制单接口图的每个连通块最多20点；而真实两步覆盖又要求每块至少17点。30个轨道既不能合成一块，也不能分成两块。它排除的是额外的“完全抵消”设计，一般允许少量不平衡的构造仍开放；新稿已单独直接复核。

[完整规则、证据与剩余范围](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/DD82_JOINT_INTERFACE_RULES_20261018.md) · [精确抵消证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/EXACT_SIGN_CANCELLATION60_OBSTRUCTION.md)

**历史阶段 · 一般共同模型返回 UNKNOWN；固定反射配色排除**

该阶段主工作是61点相邻孤立双缺陷分支的构造诊断，当时仍保留58点构造。上一张内部图放不下必需父类，这次让35点内部图、两套五色、六中心和独立五点补集共同选择。规范化没有固定第二重复色、补集第二色排列或接口类型。

**唯一一次共同求解正常返回UNKNOWN。**&#x5B9E;际88.01 CPU秒、88.14墙钟秒，没有返回候选，也没有排除证据。源码审阅与小赋值语义检查已通过；没有候选可继续接完整父类，不追加同输入时间或变换参数重试。

**新增的数学判断是：此前整个固定反射配色不能提升。**&#x516D;中心与五点补集的30对必须已经靠内部图或两组已知父点相通。每个补集点的四条叶边最多到达四个中心，所以它至少还要与两个不同中心同色。旧反射配色有补集点只能同色覆盖一个中心，无论怎样配叶边都不够。一般配色仍开放。

继续推导还把这30对的重复路线总量精确到2：20条内部两步路线加两组各6条同色路线，覆盖30对后恰剩2份重复。这迫使六颗星收到补集边的数量为5、3、3、3、3、3，或4、4、3、3、3、3。但这些条件已包含在刚才的模型中，尚无统一矛盾或新生成规则，不能用它们作为重复求解的理由。

58的并行不规则对合预算也只得到必要限制，尚未造出共同接口及符号。当时两方向的下一交付是实际共同对象或覆盖整个指定范围的矛盾；当时也不能根据已写结论数判断哪条更接近完成。结果及AP短证明的同线程第2轮复核已实际接受，本有界阶段两轮收束。一般共同对象与总体Goal仍开放。

[实际运行与用时](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/n61/joint_six_star_h35_run/RESULTS.md) · [规范化和父类覆盖](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/GENERAL_SIX_STAR_H35_NORMALIZATION.md) · [两份重复的完整推导](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/SIX_STAR_AP_DEFECT_BUDGET.md) · [58预算的准确止点](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/INVOLUTION58_IRREGULAR_BUDGET_STOP.md)

**历史阶段 · 58成果对齐与61共同父类问题的提出**

**58已完成旧有效结论的范围、前提和证据等级对齐。**&#x8FD9;不等于旧结论早就整体覆盖新模型。指定循环来源后来由新增证明关闭；28＋30的布局改变也不自动保证避开所有旧禁型。旧RAW保持原等级，不重新做历史审计。

**61从仍开放的“孤立双缺陷边也是原图边”分支提出一个具体问题：**&#x80FD;否同时造出35点四正则内部图、两套五色、六个互不相交的五点闭邻域，以及独立的五点补集，并满足重复路线预算？这六点及五点是完整图必须容纳的父点分组，不是任选装饰。

已经有一张真实H通过低重复检查，却接不上这个分组。该阶段接下来的工作因此是把图和分组一起生成，尤其让叶点剩余邻色由双方都接受的真实无向边补齐。成功后还要接完整X/Y和端口，检查全部61点对；若统一证明所有必要对象不存在，才能关闭这一整个分支。

| **方向** | **当时提出的下一步**              | **还缺什么**                                 |
| ------ | ------------------------- | ---------------------------------------- |
| 58构造   | 提出改变已失败跨边或外部边界的完整规则，再验实际图 | 仅换指定循环源、Brown边界或纯射影关联来源的内部配边已经无效；新规则尚未给出 |
| 61剩余分支 | 共同实现H、双五色、六星与独立五点补集       | 弱容量图不能补全；新的联合模型唯一一次返回UNKNOWN，仍无完整共同实例    |

比较依据是这些对象与缺口，不是已写定理数。61有明确问题不等于更容易或必须取代58主线。整体仍57≤N(8,2)≤61，构造与有全域价值的证明继续并行。

[完整范围对齐与下一动作比较](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/DD82_NEXT_ACTION_COMPARISON_20261018.md) · [当时下一问的精确规格](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/POST_ALIGNMENT_NEXT_QUESTION.md)

**历史阶段 · 共同构造边界的判断**

**58：一个完整射影关联来源已被纸面排除。**&#x4ECE;五阶射影平面任删两个点、两条线，固定剩下29点和29线的全部跨关联，即使两侧内部边全部自由，也不能完成目标。普通点只有很少重复路线余量，迫使内部边只能沿特定连线；删点连线与删线交点随后强迫出跨侧缺口或超额重复。这个结果说明必须改变真实跨边，不能只继续换内部因子。[完整证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/PG5_TWO_POINTS_TWO_LINES_PURE_INCIDENCE_OBSTRUCTION.md)

**61：局部匹配可行仍不等于真实补全。**&#x65B0;的反射六星规则明确给出44条边，五个补集点的两套邻色都可补齐。但某些叶点最后一条边只能单向要求对方，违反无向互反；一次由此指定的修正又迫使轴叶连接已经满度的颜色格。当时仅关闭这两套规则；随后上方30对覆盖证明已排除整个固定反射配色的提升。一般配色的共同模型仍开放。[明确规则与失败见证](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/SIX_STAR_H35_GENERAL_HALL_BOUNDARY.md)

另核59点“29对顶点加一个固定点”的对称构造：固定点虽改变覆盖预算，仍不能救活均匀双接口；不规则商与符号还没有共同生成规则，因此没有宣布该入口就绪。[准确范围](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/INVOLUTION59_ONE_FIXED_POINT_DIAGNOSIS.md)

以上三项均为新纸面推导，无新计算；根已核查，一次新的直接复核已分别接受准确范围。[实际回执](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/reviews/dd82/20261018_shared_construction_boundaries_review.json)。这不等于找到目标图或排除整个阶数，也不把某份反射星骨架当成全部剩余。

**历史阶段 · 61：容量通过后，失败落在什么结构上**

两个七元素置换决定35点H的70条边。首个通过对象的七轨道重复量为2、3、3、2、3、3、2，每个对应5点，总90；完整35行邻接矩阵核对通过，图也无三角。已有H及两父点的无序路线数直方图为0条150对、1条400对、2条45对。

当时原生成器在第116个相容组合处停止，未遍历完整族，第二类型尚未检查。之后只固定这张边表检查六点packing和独立五点补集，不要求新父类保持C5。后续已经接入必要父类条件，完整续查两种类型；该完整结果见历史区开头。本段70个packing的结论仍只针对当时这一张图。

**完整回溯得到70个六点packing。**&#x5341;个七点颜色类各删一点给70个互异集合，正好穷尽实际计数。它们的五点补集恰是被删顶点及其四邻点，含四条星边，不独立；也都不符合新普通类的双色计数。因此这张H不能补全，低重复容量本身不够。

这是经过源码审阅的小规模完备检查与纸面结构解释，最终第3轮实际SCOPED ACCEPT，阶段已关闭；非LRAT/Lean或全族排除。全部35个洞邻域二分检查均通过，这项条件没有否定对象。

随后的明确六星前端先保留24条星边并令另外五点独立。在补集点(0,0)处，第一色1、2、4三个必需邻位只能使用第二色2、4，发生短匹配矛盾。该固定前端也不能完成，但仅为本地根和代理纸面结果，未借前述回执接受，未修改参数继续试。

[必要父类与70集合的解释](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/n61/cyclic5_h35_run/FIXED_H_PACKING_OBLIGATION.md) · [实际边表](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/n61/cyclic5_h35_run/candidate.edges) · [后续六星短矛盾](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/n61/SIX_STAR_H35_FIXED_FRONT_HALL_OBSTRUCTION.md)

另两来源保持关闭：奇图O4的五色要求违反经典Fano大集非存在；K5的C7循环覆盖在全部七种接口下迫三角超额，新完整证明已直接接受。它们均不排除一般H。

**历史阶段 · 58：二点组构造不能使用均匀双接口**

若图有一个交换29对顶点的对称性，两组之间可以没有边、一对配对边，或全部四条边。把最后一种称为双接口。若每组接相同数量的双接口，已经得到完整矛盾；这项纸面证明获一次直接SCOPED ACCEPT。

最关键的度2情形中，重复路线预算全部用尽，迫使剩下的单接口图为29点四正则，且每条边恰属于一个三角形。它共有58条边，不能被三条一组分完，矛盾。逐点预算还限制非均匀双接口的分量形状。

这与旧29阶循环对称或29＋29均匀分块不同。完整自由对合族仍开放，截至该阶段，尚无满足单接口、内部边和符号覆盖的实际不规则商，不把形状清单当作可运行生成器。

[完整表示、覆盖条件与证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/SEMIREGULAR_INVOLUTION58_DIAGNOSIS.md) · [实际直接复核](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/reviews/dd82/20261018_involution58_double_interface_review.json)

另有一项已直接接受的新限制：支撑商若无四圈，每个单接口邻域就必须成团，迫使单接口度至多2、双接口度至少3，与路线预算矛盾。所以任意自由对合目标的支撑商都必须含四圈。这排除了整个无四圈极性来源，一般含四圈不规则商仍开放。[完整证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/INVOLUTION58_C4_FREE_QUOTIENT_OBSTRUCTION.md)

**历史阶段 · 58：为什么整体重连也必须改变外部邻接规则**

Brown的57点分成8个绝对点C、21个内部点I、28个外部点E。新点接全部C时，想让它两步到达I，至少要新增21条C–I边，并删去至少21条原C–E边。

考虑一个完整重连模板：每个E只保留原来两个C邻居之一，E–I关系不变，E内部保留旧边再加一条完美匹配；I内部及C–I允许共同任意改变。原来有168对E点仅靠共同C相通。把每个E看作八个C之间的一条边，选择保留端就是给K8定向；每三个C至多保住一对，所以最多保住56对，至少112对失去原通路。

新增匹配只有14条边。它能直接救回至多14对，每边与原E内三度邻接组合最多再救6对，总计最多98对。于是至少112−98＝14对仍不通。**仅调整I内部和C–I指派已经没有用。**&#x8FD9;没有排除改变E–I等其他真实邻接的Brown扩展，也没有证明某个改动就足够。

完整新证明已独立本地核对，已获一次直接外部SCOPED ACCEPT；没有生成或搜索已失败的图。另已纠正旧记录的范围：旧joint-boundary的21坏对源来自孪生点缩减，并非Brown＋hub。

[至少14坏对的完整证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/BROWN58_ONE_CE_MATCHING_OBSTRUCTION.md) · [旧实际范围、明确42边重连及失败见证](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/BROWN58_CONTINUATION_BOUNDARY.md)

[新的实际直接回执](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/reviews/dd82/20261018_brown58_one_ce_matching_review.json)

**历史阶段 · 自由两侧因子的实际短试验**

正式输入56,215变量、179,415子句，逐一要求同一张58点图的1,653个点对在两步内可达。准备耗时0.97 CPU秒；唯一无证明日志求解27.58 CPU／28.14墙钟秒正常返回UNKNOWN。这没有排除该族，也没有返回图。

纸面证明随后关闭整个指定来源：重复覆盖先排零交集，删除伙伴强迫的短段排两点交集；一点交集要求六行在两条旧列中各有三点且共享一对，实际来源几何却不允许所需的共邻总数。合并稿已全链本地核读，新的直接复核已接受。[实际实验](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/free_factors_cyclic58_run/EXPERIMENT_RESULT.md) · [完整证明与依赖](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/FREE_FACTOR_CYCLIC58_SOURCE_EXCLUSION.md)

**历史阶段 · 整类循环来源的排除**

左侧是28圈，旧28列由一个六元素集的全部平移组成；要求源关联覆盖所有左侧圈距大于2的点对。旧关联只许删除，另外增加两列，右侧允许任意圈分解再加六条不交弦。两条新列允许5或6度、允许支撑重叠，没有预先固定右圈顺序。

跨度6的旧列没有删边，也不接弦。它通过自身跨边及一条左圈边能到达的左点集合记为W，至多18点；剩余左点只能靠它在右基础图中的两个邻列补上。每个其他旧列都至少与W重叠一个点，所以若W至多17点，两条旧邻列最多覆盖17＋5＋5＝27点。

只剩W恰有18点。此时源六元素之间不能有圈距1或2；除相对平移±2外，其他旧列至多补四个洞。两条±2列即使各能补五个洞，也因源必须覆盖圈距4而有一个重复补点，合起来最多补九个，仍填不满十个洞。

因此每个旧高列都要邻接新增列。全部30列中恰有18个高列，扣掉至多两条新高列，还剩至少16个；新两列却总共只有4个基础邻接位置，矛盾。这不依赖求解器、圈型枚举或小样本。

允许向旧列加入来源中不存在的关联时，上述整族排除不再直接适用。不过若这样修改的旧列数为m，仍有至少16−m个未改高列需要邻接“m条改列＋2条新列”，因此16−m≤2(m＋2)，即m至少4。这个必要条件不说明四列足够，也不启动逐个m加大的试验。

[完整证明与范围](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/cyclic28_completion58_run/CYCLIC28_COMPLETION_OBSTRUCTION.md) · [实际取消状态](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/cyclic28_completion58_run/IMPLEMENTATION_PAUSED.md)

**历史阶段 · 此前人工意见与当时的处理**

用户要求先说明58是否对齐旧有效结论，再从61合并后的真实剩余提出具体数学问题，比较接下来能做什么。

已完成旧58范围对齐，确认一般奇偶条件属于旧结果；后来用新证明关闭指定循环来源。61选择相邻孤立双缺陷的35点共同实现问题，已结束无效聚合探针，并实际构造和否定一份H。后续Brown与自由对合诊断均先核旧结果范围，再用明确规则或统一计数决定是否继续。

每小时只要求更新这一页，不要求新定理、构造或换假设。原新旧61对齐保持完成，旧RAW与I12条件范围不升级。

[用户原话与实际处置](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md)。

**历史阶段 · 旧61点成果对齐：确有范围重复，但证据不能升级**

**对应成立。**&#x82E5;一个点连着两条权重2的缺陷边，这两个2已经用完其缺陷预算4。它自动不在三角形里，可直接作为旧模型的根；两端各有三个父点，其他根外点只有一个父点，恰好就是旧[3,3]。两个三元父集交集大小只能是3、2、1、0，旧四类全部覆盖。

四类确实都有旧RAW UNSAT日志，没有额外加“全图无三角形”或I12条件。不过没有独立核验的证明，历史CNF原文件也已缺失。因此研究安排继承这份RAW覆盖，**不再重复探索它已覆盖的长双重缺陷路径**；严格证明记录仍保留认证缺口，不把“D必为匹配”说成已核验定理。

按旧RAW工作范围，按该阶段的分类，61点仍有“若干不共端的双重缺陷边”和“没有双重缺陷边”两大粗范围；这不是只剩两张图，也不是接近完成的比例。孤立双重缺陷边可以同时是原图边，也可以不是，不能混同于两条缺陷边共端。

旧I12的P/T/W分类、简单缺陷图及细中心结构依赖H与全图¬O，仍是条件结论；V3把缺陷连通性证明到任意61点目标，是实质的范围拓宽。V3的条目上界与h=0还增加了可核验的证明强度，但其部分SAT探索确与旧RAW范围重叠。

有界对齐已完成，实际跨模型范围复核已接受；没有重跑旧SAT、扩大Lean或重审全部历史。[完整对照、继承依据和准确缺口](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/DD82_OLD_NEW61_ALIGNMENT_20261018.md)。

**历史阶段 · 全域61点限制：30个低度诱导点放不进去**

**任何61点目标图中，任取一组点，若它们之间的实际诱导最大度不超过2，这组点至多29个。**&#x5141;许圈、路径和孤立点，不能先删掉多余边再套用。完整纸面证明和这次新应用均已被实际SCOPED ACCEPT直接复核，尚未做Lean。

关键不是旧61点缺陷分类。假设有30个这样的点S，补集有31点。跨边计数留下总共6份度数余量。补集中内部度恰为2的点，到S的路线数恰好30，任何重复都不允许；这迫使S没有路径端点或孤立点，并把补集分开。

沿圈求覆盖方程的最大值和最小值，又迫使各圈长度为5的倍数。补集因此必须分成25个圈上点和6个内部三度的点；每个S点恰好连接后面六点中的一个，称为它的“父点”，每个父点恰有五个S邻点。

已证明的二进制圈块规律使同一长圈上相隔3或4步的点只能共享父点，进而整圈都要同父，这超过五个位置。于是S只能是六个五圈。但一个五圈沿父点关系行走，又必须无折返地绕六点补图中的某个圈；它只能绕一个长度整除5的圈。六点二正则图只有六圈或两个三圈，均不允许，矛盾。

这条证明不调用I12的H或¬O、不使用旧RAW排除，也不调用旧十二五圈终点证明；只继承此前已经证明的一般二进制圈块引理。**它不排除整个61阶：**&#x5C1A;未证明每张目标图必有30点这样的诱导子图。

| **目标阶数** | **该阶段得到的诱导最大度≤2子图上界** | **依据**           |
| -------- | --------------------- | ---------------- |
| 58       | 28                    | 完整两块归约，保留旧LRAT依赖 |
| 59       | 29                    | 已有路线与跨边计数直接适用    |
| 60       | 29                    | 一般圈块刚性及旧五圈终点排除   |
| 61       | 29                    | 本次六单位余量与父点覆盖矛盾   |

[完整61点证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/INDUCED_DEGREE_TWO61_BOUND.md) · [长期结论与依赖](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/claims/dd82-induced-maxdegree-two61-bound.md) · [本次直接回执](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/reviews/dd82/20261018_induced61_bound_review.json)

**历史阶段 · 60点圈结构归约证明**

假如两侧各30点、各自内部是若干个圈，每点另有六条跨边，那么每个点到另一侧的一步和两步路线总共恰30条。要覆盖30个点，就不允许重叠：每个跨侧点对必须恰有一种路线。

先对一个对侧圈汇总路线，沿本侧圈得到 x(前邻)+3x(i)+x(后邻)=圈长。最大值和最小值比较迫使x恒定，所以每个圈长都被5整除。

把某两个圈之间的跨边写成0/1方格，精确覆盖要求每个格子的“自身、上、下、左、右”五格中恰有一个1。从任一个1出发，四个斜对角位置的覆盖会强迫四个新的1；它们继续强迫同一方向，最后只能形成 i−2j≡c 或 i＋2j≡c（模5） 的图案。方向和常数可以在不同圈对之间自由选择。

若有长度至少10的圈，取相隔三步的两个点：它们没有同侧两步路，而且在每个对侧圈中邻居属于不同模5类，也没有共同邻居。因此长圈不可能，只剩两侧各六个五边形；这个允许各接口任意方向的旧族已经有完整纸面排除。

进一步，若任意60点目标有至少30点的诱导最大度≤2集合，补集内部度0或1的点最多覆盖24或28点，均不够；跨边握手遂迫使两侧各30、内部全2度，回到刚排除的族。因此该集合**至多29点**。这是纸面证明及旧纸面结论的继承，没有新SAT或Lean。[完整证明、实数反例与适用范围](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/TWO_BLOCK60_CYCLE_RIGIDITY.md)。

**历史阶段 · 为什么4+4结构无需运行求解器**

在两组各29点、每点4条组内边和4条跨组边的结构中，同组一步与两步路线恰够覆盖其余28点，因此每一对同组点只能有一种路线。三角形必有两个同组点，会造成重复，所以不能出现。若一对异组点有三个共同邻居，其中两个必同组，而这两个点又共享原来的两个端点，也造成重复。

于是所有非邻点对只会有1或2个共同邻居。58点八正则目标每点有7次重复，因此恰有58×7÷2=203对“双共同邻居”点对。每一对确定唯一四圈，而每个四圈有两条这样的对角，203必须为偶数，矛盾。

这是完整纸面推导，实际Gemini第1轮已接受；尚非Lean结果。它还给出一般58点必要条件：必须有三角形，或某个非邻点对至少有三个共同邻居；并没有排除任意58点图。[完整奇偶证明、二块划分归约与合法归一化](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/EQUITABLE_TWO_BLOCK58_REDUCTION.md)。

**历史阶段 · 58点：为什么自由圈结构最终也走不通**

先前已证明，两块均匀划分只能是29+29、每点2条组内边和6条跨组边。跨组点对的路线数矩阵因此等于“每对至少一次，再每行每列各多一次”。多出来的位置构成一个置换。

任选右侧一个圈，设它有b点；x(i)是左点i连向这个圈的边数，p(i)表示该行多出来的一次路线是否落在这个圈中，取0或1。沿左侧圈逐点有 x(前邻)+3x(i)+x(后邻)=b+p(i)。

令所有x的最大、最小值为M、m。最大点给3M+2m≤b+1，最小点给3m+2M≥b，故M−m≤1。若确有两个整数值，方程迫使高低值沿每条圈边交替；所有圈都得是偶圈，与左侧总共29点矛盾。所以x和p只能恒定。右圈非空且置换每列一次，迫使p全为1、b=29。交换两侧得到两侧都只能是单个29圈。

这正落入已有独立LRAT证书排除的双29圈族，因此整个均匀两块划分族被排除。新步骤是纸面证明，最终排除继承旧计算证据；没有重跑旧证书。[完整分量证明与依赖](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/JOINT_TWOFACTOR58_COMPONENT_CONSTRAINTS.md)。

**历史阶段 · 58点推广：路径、圈与孤立点合起来仍最多28点**

任取顶点集S，要求其中每点至多有两个S内邻居；这是全部真实诱导边的条件。每个S点向补集至少发出六条边。若|S|≥29，补集内部度0只能覆盖S中的24点；先排除度0后，内部度1最多覆盖28点，所以补集每点内部度至少2、向S至多六条边。

于是 6|S|≤跨边数≤6(58−|S|)，只能|S|=29且全部取等号。取等号迫使两侧都内部2度、跨度6，属于已经排除的均匀两块族。因&#x6B64;**|S|≤28**。

此前直接接受的是诱导圈并；现在包含路径和孤立点的更宽表述也已由一次新实际回执直接接受，不借旧回执扩大范围。最终58排除链仍依赖旧独立LRAT证书，尚非Lean。这个界没有证明每个58点目标一定含29点的此类集合。[完整推广](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/INDUCED_DEGREE_TWO58_BOUND_EXTENSION.md) · [证据与依赖](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/claims/dd82-induced-maxdegree-two58-bound.md)。

**历史阶段 · 覆盖全部跨边选择的排除**

若58点目标图中某点度数至多7，它与两步内邻居合计最多1+7+7×7=57点，矛盾。因此每点度数必须是8。若两侧内部都恰为29圈，每点已有两条内部边，必须再有六条跨边。

分别沿两侧圈编号，以C(i,j)表示一条真实跨边。全部841个变量自由，行列各恰有6个1。每个异侧点对要么直接相连，要么先走一条左圈边，或最后走一条右圈边；这恰好是五种可能，模型全部包含。

同侧圈距离1或2的点对已被圈覆盖；其余每侧348个点对必须共享一个真实跨侧邻居。模型对29个可能共同邻居逐个使用双向AND，再要求至少一个存在。因此所有条件使用同一个C，不能虚报路径，也没有遗漏同侧距离。

任何具有这种划分的目标图，都可独立按两条圈顺序重标并给出满足赋值；反过来满足赋值直接给真实图。这份31581变量、102341子句的公式已获独立核验的UNSAT证明，所以整个明确子族被排除。[完整双向证明和范围](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/FREE_CROSS58_HAMILTON_BRIDGE.md) · [独立检查日志](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/free_cross58_run/certification/certificate_check.log)。

这里要求两侧的**诱导图恰为圈**。只有一个两圈二因子、但同侧还有其他边，不在排除范围；其他圈型和一般58点图也不在范围。独立证书已核验，最终跨模型结果复核已接受；不是Lean结论。

**历史阶段 · 58点不均匀内部度构造尝试**

左侧固定一个28圈，右侧固定一个30圈，再从右侧所有405条非圈点对中共同选择六条不共端弦。全部840条跨边也共同选择。左点各六条跨边，右弦端点各五条、其他右点各六条；完整图恰58点、232边、每点8度。弦的位置和配对均不预设。

右侧内部度有2和3两种，因此旧29＋29均匀划分证明不直接适用。基础两圈的五项跨覆盖即使总量恰够，仍可能有空洞；六条弦能新增60条跨侧路线，用它们修补空洞。因此也不能把60点“每格恰一次”的结论误套过来。

该阶段的一份度数合法赋值确实展示弦能修复一个空洞，但整体仍有坏点对，不是目标。该阶段的完整编码要求所有点对真实邻接或有真实共同邻点，用同一组边共同实现；这是受限构造族，不覆盖任意58点图。[规则与一次预算](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/nonuniform58_run/PLAN.md) · [为什么旧障碍不能直接取消本次输入](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/nonuniform58_run/MATH_DIAGNOSIS.md)。

唯一实验已返回UNKNOWN；正式规模的901坏对只是预先指定的编码检查图，不能当作求解器发现的候选或搜索进度。[实际交付与终态](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/nonuniform58_run/DELIVERY.md)

**历史阶段 · 匹配生成与完整图检查**

从58个空顶点开始，每轮在尚未使用的边中选一个完美匹配：29条边恰好让每点增加一个邻居。经过八轮，每点都恰有八个不同邻居。每轮可用图的最小度至少50，因此一定能找到完美匹配；但最终直径是否2，必须实际计算。

选择匹配时，先最大化各条边单独加入后能够修复的坏点对数之和，再优先保留更多几何边，最后以记录的seed打破同分。多条边可能修复同一对，所以这个收益之和只是选择规则；报告始终使用整张实际图的坏对数。保存每轮匹配与最终全部边，让失败结构可以直接检查。

八个匹配之并是初始生成的额外限制，不是任意目标图必备条件。八份不同标签边表不等于八个非同构图。实际前缀容量诊断已完成，见下节。[原规则与预算](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/global_matchings58_run/PLAN.md)。

**历史阶段 · 为什么第六轮已经不能补成目标**

设中间图每点已有r条边，还缺d=8−r条。某条可加边e单独修复的坏对数记为g(e)。所有最终修复只能来自一条新边（包括一旧一新路径），或以某点为中心的两条新边。因此修复总数至多为新增边的g之和，加58×d×(d−1)/2。

每点恰用d条新边，故各点最大的d个g之和，再除以2，是前一项的上界。它直接排除了六份第六轮图。对剩下两份，给每点选一个整数t(v)，还可用更紧的界：2×新增边g之和 ≤ d×所有t之和 + 所有可加边的 max(0,2g−t(u)−t(v)) 之和。这是逐边展开后删除负项，不依赖优化器最优性。

两份实际整数见证分别给出**645个坏对最多修复644个；639个坏对最多修复638个**。所以八份第六轮图全部不能完成，包括不按匹配分色的任意两度补边。主代理重新计算两份见证，数值一致；同线程Gemini第2轮已认可该结果及精确范围。

结论只针对八份保存的中间图，未排除其他生成轨迹或58阶；因此未执行第六轮补全SAT。随后唯一第五轮共同三度补全实际返回UNKNOWN。[完整推导与整数见证](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/global_matchings58_run/prefix_capacity/PREFIX_CAPACITY.md)。

**历史阶段 · 单调几何尝试与具体反例**

**该阶段完成有限检验的完整模型：**&#x4B;(x)表示背景点是否保留，X(x,y)表示一条原来没有的新边。保留数恰为58，新边必须连接两个保留点；旧边只要两端保留就存在。对于保留点x，旧邻居中的保留点数加新增边数恰为8。删除点不受这个辅助计数限制，因为其旧邻居可以保留而它自己不在图中。

背景非相邻点x、y原本有唯一共同邻点m。两个端点都保留时，完整模型要求：m也保留，或新增x–y，或存在一旧一新边的真实路径，或存在两条新边构成的真实路径。所有条件使用同一组K和X，所以可满足赋值直接对应完整图。没有固定删除方案或任意邻居选择。小图语义检查特意覆盖删除顶点的计数守卫、混合路径及两新边路径。

设 H 是删点后保留的旧图，δ(x)=8−deg_H(x) 是点 x 还能增加的边数。δ(s)=0 的点 s 已饱和，它的邻居不能再变化。若 x 与 s 在 H 中距离超过 2，而 δ(x)=1，那么 x 的唯一新邻居 y 必须属于 N_H(s)，并且 y 自己还允许增加边。

因此，x 必须从其所有饱和坏伙伴的旧邻域交集中选择 y；交集为空或其中所有点都已饱和时，该删除方案不可能补全。旧 58 点方案中，x=8 的两个饱和坏伙伴为 16 和 40，它们的邻域不相交。旧 59 点方案中，x=20 所需交集只有 43，但 43 已饱和。这解释了为什么原来的 SAT 没有给出图，以及新的筛选实际修复什么。

精化筛选仍没有要求每对点最终都被覆盖，也没有完整约束高缺口点接收的边数。该阶段原计划是：若返回 SAT，再释放全部可选新边，精确满足每点新增度数，并逐一要求原题的真实邻接或真实两跳路径。不能固定一份筛选模型随意选出的边后，把该分支失败说成整个删除集失败。

**新增具体反例：**&#x35;8点新方案中，0、1、2的旧度数均为7，5和61的旧度数为8。0到5及61都没有两跳路径，而 N_H(5)∩N_H(61)={2}，故必须补边0–2。补完后 N(0)={2,65,66,67,68,70,71,72}，N(2)={0,5,13,29,37,45,53,61}，交集为空。1到这两点仍没有两跳路径，且只能补一条边，矛盾。这个论证保留所有其他补边自由，详见[短证明与实际数据](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/POLARITY73_REFINED58_FORCED_EDGE.md)。

这一单调几何构造族的 60/61 点情形已有排除，58/59 点必须删至少 8 个外层点；这些结论不排除任意 58–61 点图。完整推导见 [polarity73 研究稿](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/proofs/dd82/construction/POLARITY73_REDUCTION_CANDIDATE.md)。

**历史阶段 · 已执行实验与当时预算**

该阶段：一般六星共同模型80074变量、357211子句。小语义1.695936 CPU／1.719001墙钟秒；正式准备0.906760／0.917317秒；唯一发现求解88.012765／88.135652秒，正常软时限UNKNOWN，未返回模型。完整配置与终态见上方运行报告。

| **实验**                 | **状态 / 返回对象**                                               | **实际用时或预算**                                                            |
| ---------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------- |
| 10 月 13 日：58 点原筛选      | SAT 删除方案；随后证明不能补全，330 个旧坏点对                                 | 求解 CPU 0.013380 秒，墙钟 0.115486 秒                                        |
| 10 月 13 日：59 点原筛选      | SAT 删除方案；随后证明不能补全，415 个旧坏点对                                 | 求解 CPU 0.060981 秒，墙钟 0.187628 秒                                        |
| 该阶段：58点精化筛选            | SAT；九组语义检查、完整CNF赋值检查通过。449个旧坏点对、需补40条边；随后由强迫边矛盾排除该删除集       | 求解CPU0.963712秒／墙钟1.134302秒；解码CPU0.158462秒                              |
| 该阶段：59点精化筛选            | UNKNOWN，exit0；达到soft28秒后正常结束，无目标或排除                         | 求解CPU27.996050秒／墙钟28.192344秒                                           |
| 该阶段：完整变量58点模型          | 173093变量／558930子句；八组完整邻接赋值检查通过；单次求解已结束：UNKNOWN，exit0，无目标或排除 | 准备CPU2.829600秒／墙钟2.870178秒；实际求解CPU28.043004秒／墙钟28.198339秒，无证明日志        |
| 该阶段：空图八轮匹配，seed0–7     | 8张完整58点232边八正则图，独立BFS全部通过数据一致性检查；全部直径3、177–201坏对，无目标        | 整批CPU5.450637秒／墙钟5.625482秒，含全部BFS；预算60／90秒，正常结束                        |
| 该阶段：实际seed3第五轮的共同三度补全  | 56004变量／173002子句；8组完整邻接语义检查通过；唯一一次求解UNKNOWN，exit0，无图或排除     | 准备CPU0.845590／墙钟0.917591秒；求解CPU27.827669／墙钟28.150040秒，soft28正常结束，无证明日志 |
| 该阶段：两侧C29、841跨边全自由共同构造 | 31581变量／102341子句；发现运行exit20、原结果无proof；随后独立取证成功              | 准备CPU0.415676／墙钟0.466776秒；求解CPU24.360557／墙钟24.810792秒，无proof           |
| 同一自由跨边输入的独立取证          | exit20，完整LRAT 67727049字节；原输入未改                              | CPU26.549147／墙钟27.212125秒；预算50／70秒                                     |
| 独立lrat-trim证书检查        | exit20且输出s VERIFIED；精确保存CNF已认证UNSAT                         | CPU0.834874／墙钟0.886483秒；预算30／45秒                                       |
| 58点全部均匀两块联合模型          | UNKNOWN；无图、无证书；两侧圈结构与全部跨边自由；单次无proof预算60/90秒，未加时            | 57.906149 CPU / 58.206894 墙钟秒                                          |
| 该阶段：58点28＋30、六自由弦与全部跨边 | UNKNOWN，exit0；soft28正常结束，无模型、无proof、无BFS验收调用                | 准备1.093080 CPU／1.117314墙钟秒；求解28.016724 CPU／28.150117墙钟秒                |
| 该阶段：循环28列源的58点补全       | 正式计算取消：完整纸面容量矛盾；encode.py仅写入，未执行，无CNF、模型或solver调用           | 没有正式求解用时；原30CPU／45墙钟秒计划未执行                                             |
| 61实际C5 H35             | 首个前端通过，type0第116对停止，maxrho3/总90，非全族穷举                       | 子进程0.004081 CPU／0.010942墙钟秒，预算30／45；编译小语义另0.964903／0.991224秒           |
| 固定H六点父类                | 完整1049节点、70个六packing、普通双色合格0；纸面解释补集不独立                      | 0.036680 CPU／0.066160墙钟秒，预算10／15，正常exit0                               |

找候选模式若返回 UNSAT，仅记为未经认证的输入结果，另行判断是否值得取证。UNKNOWN、资源上限和执行错误均不当作数学排除。CPU 秒与研究墙钟时间分别记录。

**历史阶段 · 此前完整自由跨边路线仍未解决的问题**

左28圈里有322对点不能靠圈内两步相通，必须共享右侧邻居。右侧度数给出390次共同邻居计数，但同一对可能被反复计入，不能把390当作已经覆盖390对。

新的本地手算例说明：保持所有左点对的共同邻居数完全不变，只调整跨边在右圈上的位置，就能让基础跨覆盖空洞从12个变为282个。两个例子都只覆盖65对左侧远点对，都不是目标；它们说明这些总数缺少对位置的控制。

而12个空洞的例子也无法完成：空洞全在两条左行，这两行的跨邻居都不是右弦端点，因此六条弦无论怎样配对都不能给它们补路。“有60条补路资源”并不意味着能把资源任意搬到空洞。

该阶段仍未证明全部自由跨矩阵能否同时覆盖322对并修好跨侧缺口。新的零余量障碍已经关闭一整类几何来源，但允许所有行都有少量弦路线的情形仍开放；不能从一次UNKNOWN判断空间已耗尽。

固定跨矩阵后的补洞归约在该阶段第3轮已被直接复核：12个弦端点必须在同一个兼容图里配完，弦的双方要互相修补对方所有缺口。这个精确归约仍没有给出满足全部同侧覆盖的实际跨矩阵。

还有一个新的共同约束：把右侧“圈内距离超过2、又没有跨侧共同邻居”的高低点对连起来，这些缺口边经同一弦伙伴换位后，必须落到真实右圈的高低边界上。因此它们只能构成若干路径，不能成环。某个低点若有两个高点缺口，伙伴甚至被唯一确定。条件已直接复核，但两低点之间的缺口和左侧覆盖仍要共同满足。[右侧支撑与共同匹配的证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/nonuniform58_run/RIGHT_SUPPORT_MATCHING_OBSTRUCTION.md)。

**历史阶段 · 几何填法的统一障碍：并非只否决一个补边选择**

在该阶段的28＋30分组中，12个右点是弦端点。左点若一个弦端点都不连，它的30条基础跨路线就必须恰好覆盖右侧30点，不能有重复。它自己和两个左邻点各自的六个跨邻居因此必须两两分开。

若连续三个左点都处于这种零余量状态，它们的三组六邻域恰好分割18个非弦端点。中间点的覆盖又要求每个弦端点在右基础圈中恰有一个邻居属于中间组；它只剩一个基础邻居供两端组使用。对两端行分别计数，迫使外侧两点各自连接六个弦端点，而且两组六点恰好互补。

左圈为28圈时，这两个外侧点圈距离为4，必须有跨侧共同邻居；互补结论却说一个都没有，所以连续三个零余量点不可能。不能据此禁止任意三个分散零点，也不能假定目标一定含零点。

推广到任意两侧圈型：若另外25行两两有共同邻居，每个零余量点的两个左邻点就不能都来自这25行。因此三个特殊点只能诱导三点路径或三角形。路径迫外侧普通点没有共同邻居，矛盾；三角形迫每个弦端点在右基础图中有三个不同邻居，也矛盾。

任意25×30、行度6列度5且行支撑两两相交的关联矩阵，添加任意三条互不相交的六列新行，正好落入这个范围。它覆盖全部阶5仿射平面三行扩充，包含先前特定PP5方案。**完整纸面证明与范围已被实际第3轮SCOPED ACCEPT直接复核**；没有新增计算或Lean，也未排除任意自由跨矩阵。[完整新证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/nonuniform58_run/ZERO_SURPLUS_PATH_OBSTRUCTION.md) · [长期结论与证据](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/claims/dd82-nonuniform58-affine-front-exclusion.md)。

**历史阶段 · 改变关联关系的实例**

在明确的F5坐标中做三次独立的2×2交换：每次删去两条跨边、补上交叉的两条，保持所有点度数。三个特殊点各自从没有弦路线变成有一条；普通点(0,1)与(1,3)还失去了原来的唯一共同线。因此这次确实破坏了旧证明的两个前提。

问题是，每个特殊点仍保留一个完整平行类，所有普通点仍与每个特殊点有共同邻居。一个特殊点只有一份重复路线余量；若它在左侧接普通点，无论另一邻点是普通还是特殊，都会产生至少两次重复。因此三个特殊点又被迫组成三角形。

即使允许这个三角形，仍有一个高列不属于任何特殊点的跨邻域，又不是弦端点。要覆盖三个特殊点到它的距离，它必须在右基础二因子中各接三个互不相交邻域中的一个点，度数至少3，矛盾。

这份具体交换诊断及更广的“每个特殊行一次独立交换”族，已在实际第4轮被直接接受。后者按删除平行类列或额外列分成两支：前者让至少五个左点支撑不交，超过左圈四个近邻位置；后者回到上述重复路线矛盾。完整自由跨矩阵仍开放。 [完整独立交换族证明](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/computations/dd82/construction/nonuniform58_run/PARALLEL_CLASS_TRADE_CAPACITY.md)

**历史阶段 · 当时的后续研究安排（已由置顶任务更新）**

该阶段曾诊断一种局部换边：在三个颜色横截面之间交换三角形，检查是否能保持双五色和六中心星边，并消掉五点补集内部的边。这项纸面诊断已存入历史并停止，没有留下在途计算。它没有给出完整对象；局部排列等价式和亏缺数量等弱条件，也不能单独当作新搜索入口。

该阶段留下的共同实现问题由置顶任务承接：同一实际35点内部图、两套五色、六点零端口父类和独立五点补集必须同时成立。只给补集一侧的匹配、叶度序列或另一张低重复内部图仍不够。

当时还保留58点构造方向；其后用户已要求主力集中一般n61，58／60已失败特殊模板不自动续修。该阶段“不恢复原p/q”的安排已被用户明确允许的有依据续查更新：后续完整检查了C5来源两种类型，结果见历史区开头。旧SAT及参数阶梯没有自动恢复。

该阶段一般六星模型已完成源码、语义和唯一实际求解，UNKNOWN原样保留；该模型的求解与两轮实际复核均已结束。该阶段结束时只剩局部换边的纸面核对，solver与MCP均已终态；此处不代表现在的在途任务。后续AP预算均属现模型隐含结构，不作为新剪枝加时重跑。整体Goal仍ACTIVE；小时要求仅更新HTML，不要求每小时新定理或换假设。

**历史阶段 · 仍有效的历史成果与开放范围**

2026-10-18对齐纠正：若下列历史记录把长路径、非空匹配、空D并列开放，那是未合并旧RAW前的表述。对齐后的工作范围与严格证明缺口已在该阶段的对齐记录中分别说明。

61 点缺陷矩阵 B=A²+A−7I−J 的正支撑连通、每行和为 4、非对角项至多 2；值为 2 的点对构成路径森林 D。内部三点 u-v-w 上已得 N_A(u)∩N_A(w)⊆N_A(v)，这是有继承依赖和已检查 CNF 的计算辅助结论，尚非 Lean 定理。它不排除 D 含较长路径、D 为非空匹配或 D 为空三大剩余范围。

[完整近期进展、comments 与证据](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md) · [V2 成果与耗时](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/context/dd82/WORK_SUMMARY_V2_20261013.md) · [执行约定文件](https://nat2-notebook-inspire.sii.edu.cn/ws-6e6ba362-e98e-45b2-9c5a-311998e93d65/project-4493c9f7-2fbf-459a-ad90-749a5a420b91/user-08e7437e-ff7e-4a35-818a-7fc61c96111c/jupyter/04d759be-b732-44ce-a6be-382a59398c45/9b721da5-5a9d-4f3d-a341-0a21f5158f10/files/global_user/ar4math/context/dd82/DD82_HUMAN_IN_LOOP_GOAL.md)

**历史阶段 · 变更记录**

2026-10-18 16:38:29 UTC：置顶只保留一般n61共同构造一项任务；此前ε=0完成阶段也转入历史，共30个历史阶段。顶部明确本次新增、实际剩余和下一动作，并区分已通过的源码复核与尚待直接复核的新纸面结果。

2026-10-18 15:08:42 UTC：接口规则六稿获各自直接复核，最后一稿统一排除精确符号抵消机制。58/61比较仍按真实下一动作；报告后继续局部换边诊断，无新求解。

2026-10-18 14:38:35 UTC：共同模型唯一求解UNKNOWN；新增30对覆盖关闭整个旧反射固定配色的提升，AP预算落实为两个重复单位但未得一般矛盾。58不规则预算未给生成规则；不加时、不按定理数选主线。

2026-10-18 14:15:11 UTC：三篇新稿获直接SCOPED ACCEPT并完成根处置；一般61下一问保留全部接口，不自动穷举反射匹配或改59固定点数。该阶段全部任务终态，整体Goal继续ACTIVE。

2026-10-18 14:12:05 UTC：将58对齐边界、61实际下一对象及行动比较置顶。新增纯射影关联58完整纸面排除、反射六星两规则失败和59单固定点必要障碍；无新计算，当时直接复核在途。

2026-10-18 13:57:27 UTC：固定H的70个packing揭示补全失败，最终第3轮实际接受，原枚举不恢复；继续固定六星前端，局部Hall矛盾已本地完成。下一问转到六星、独立补集和双色缺色共同生成。

2026-10-18 13:49:16 UTC：实际C5 H通过rho3/90并独立核验，停止原枚举，续接同一H的六点零端口父类义务；C4支撑和C7来源两新证明直接接受。

2026-10-18 13:38 UTC：登记C5双五色实际H生成计划，当时方向/源码检查中、正式运行未开始；补得58支撑商必含四圈与61逐点重复分解。本轮数学范围不变。

2026-10-18 13:24:00 UTC：报告更新后继续完成奇图O4父点五分区诊断，继承经典STS7大集非存在；将61下一问题具体化为实际H/双五分区与逐点、总体重复容量共同实现。该阶段所有任务终态，整体Goal仍继续。

2026-10-18 13:19:54 UTC：Brown新统一计数获实际直接SCOPED ACCEPT，cell380终态；更新后继续35点奇图的父点着色诊断，无新求解。

2026-10-18 13:16:46 UTC：继续实际构造诊断；自由对合正则双接口排除直接接受；Brown整体外部模板至少14坏对的纸面证明已完成、当时外审在途；61明确H35由单行缺陷6大于4否掉。无新目标、完整阶数排除或SAT。

2026-10-18 12:55 UTC：新终结定理直接ACCEPT已登记；报告更新后继续完成非共线三删点射影前端的统一低列容量障碍，后者本地证据单独记账。所有计算与外部调用均终态，Goal继续ACTIVE。

2026-10-18 12:49 UTC：r1/r2末两分支本地完整PASS，合并为整个固定循环来源排除；当时新稿的直接复核在途。按用户要求重写下一动作比较；唯一实验仍UNKNOWN，开始不同几何前端的纸面诊断。

2026-10-18 12:32 UTC：5＋6获独立本地PASS和实际第3轮直接ACCEPT；剩余两新列必须6度。加入两项已证必要计数，当时代码改动复核在途；6＋6与自由左因子结构继续纸面研究，无新正式求解。

2026-10-18 12:16:59 UTC：按用户要求补清旧58覆盖；纠正奇偶结论重复。具体比较58删除几何与61真实父点共同实现；61二阶聚合非负探针已证自动，停止此切入。正式求解未启动。

2026-10-18 10:49:38 UTC：新增61点诱导最大度2子图≤29的全域必要结构，获新的直接复核；全部远对覆盖循环源的单调补两列排除也已接受。更新后继续完成左因子改序诊断，没有新solver。

2026-10-18 10:39:19 UTC：旧第4轮实际复核收尾；新增全部远对覆盖循环源的单调补两列纸面排除，取消正式计算，新证明另行复核。非单调修改至少四旧列是必要条件，非可行构造。

2026-10-18 10:13:40 UTC：HTML更新后完成具体F5关联交换诊断；旧前提确实改变，但低余量相交结构仍迫矛盾。本地完整证明，未归入第3轮回执，未运行新计算。

2026-10-18 10:10:33 UTC：第3轮直接接受固定C配对归约、三零行刚性、全部25＋3仿射前端排除与右侧缺口森林约束。完整自由C族仍开放；继续一个度数保持关联交换的纸面诊断，无新求解。

2026-10-18 09:56:50 UTC：同一路线继续得到固定C的兼容配对条件，并排除一个具体PP5关联前端（本地纸面结果）；任意自由C族仍开放，无新增求解。

2026-10-18 09:55:09 UTC：非均匀58第2轮实际回执ACCEPT，计算终态仍UNKNOWN；继续纸面分析，新增固定跨矩阵后的12端点兼容匹配归约（本地证明，未另做外部审阅）。

2026-10-18 09:46:48 UTC：非均匀58唯一求解UNKNOWN，当时实际结果第2轮复核在途；继续同一结构的纸面问题，未追加预算。

2026-10-18 09:40:58 UTC：60点一般圈块归约、完整两侧圈族排除及58/60诱导最大度2上界均获一次新ACCEPT；58点非均匀构造源码PASS，当时计划下一步准备一次完整输入并限定求解。

2026-10-18 09:32:15 UTC：继续原Goal；补充58点诱导最大度≤2的本地推广，检查60点完整两侧圈族，准备58点28＋30非均匀构造。当时无新求解、目标图或已接受新阶数结论。

2026-10-18 09:24:39 UTC：新旧61有界对齐完成并接受；n58分量刚性和诱导二正则子图≤28完成并接受；联合实验UNKNOWN原样保留，无新计算。

2026-10-18 09:17:05 UTC：旧[3,3]覆盖共端双边已核清，纠正61研究剩余；n58新增分量刚性纸面证明，当时两项范围复核在途。

2026-10-18 09:10:06 UTC：澄清每小时仅报告；n58纸面归约获接受，当时唯一联合试验运行中；开始用户指定新旧61有界对齐。

2026-10-18 08:57:50 UTC：4+4候选被短奇偶矛盾否决，无新增solver。登记完整自由二因子联合构造，当时源码/小语义与方向复核在途；未生成正式输入。

2026-10-18 08:42:36 UTC：最终Gemini第2轮接受已核验证书及完整子族归约，有限机制CLOSED2/4；wiki和恢复入口同步。该阶段计算与外部复核均结束，下一结构仅在核对范围，无新批次。

2026-10-18 08:37:39 UTC：独立LRAT检查成功，精确CNF已认证UNSAT；新增完整双诱导29圈子族排除，57–61不变。当时最终范围复核准备中。

2026-10-18 08:34:56 UTC：自由跨边完整模型真实返回UNSAT，尚未认证。为同一精确输入设立独立有界取证，未改原始结果或输入。

2026-10-18 08:32:44 UTC：自由跨边模型正式准备与必要检查完成；新线程方向接受；当时唯一有界求解已启动，尚无终态。

2026-10-18 08:26:43 UTC：匹配机制最终第3轮复核接受并关闭。登记新的双Hamilton圈自由跨边共同模型；代码与数学检查开始，未运行正式输入。

2026-10-18 08:18:21 UTC：完整F5共同模型实际UNKNOWN；所有计算终态，当时最终第3轮复核在途。不追加F4、seed或时间；开始核对更宽的非循环双侧结构是否值得作为新机制。

2026-10-18 08:06:32 UTC：整数势进一步排除两份剩余F6，首批全部第六轮前缀已不能完成；取消F6补全，准备一次F5共同三度补全；无新求解。

2026-10-18 07:58:41 UTC：首批八张完整58点图及独立BFS完成，均非目标；方向复核返回认可。开始分析实际中间图的容量损失。

2026-10-18 07:51:43 UTC：单调路线最终复核4/4返回并收尾；转向从空图生成完整58点八正则图，当时方向在审、源码在写，尚无新批次结果。

2026-10-18 07:40:52 UTC：完整58点共同模型返回UNKNOWN；本日三次求解合计57.002766 CPU秒，不含推导、准备和复审。短profile未命中不等于全族排除或空间耗尽。

2026-10-18 07:35:11 UTC：第三轮复审返回；纠正审阅建议中对删除顶点的度数约束及无依据的运行时间预测。选择一次完整58点共同模型作最终有限检验。

2026-10-18 07:25:31 UTC：新增两次实际精化筛选；新增58点强迫边反例。该删除集被排除，完整58/59单调构造族仍开放。

2026-10-18 07:20:32 UTC：恢复持续研究；建立本地 HTML；同步当时的计划和人工意见；选择上次已提出、尚未执行的精化筛选。没有新增图或阶数排除。