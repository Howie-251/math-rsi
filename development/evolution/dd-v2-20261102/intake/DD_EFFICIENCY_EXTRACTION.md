# DD 历史中的效率转折：给 MathRSI v2 的独立提取

2026-11-02。范围仅为只读提炼；未恢复数学 Goal、运行旧构造/solver/BFS/Lean、调用外审或修改源材料。只写本文件，未读 ECC 原工作区。这里的“候选”是维护建议，不表示 base 已修改或行为已验收。

已读 MathRSI `AGENTS.md`、`docs/EVOLUTION_WORKFLOW.md`、`docs/SKILL_ACCEPTANCE.md`，以及现行 `mathrsi-research`、`mathrsi-prove`、`mathrsi-route-loop`、`mathrsi-survey`、`mathrsi-verify` 相关正文、`mathrsi-research/references/efficiency.md` 和 Lean working-loop 的表示/性能段。历史入口为 `dd_research_full_handoff/guide/01_INITIAL_PROBLEMS_AND_TIMELINE.md`、`04_TIME_COSTS_AND_REPLAY.md`、`02_RESEARCH_TRAJECTORIES.md`，以下关键事实另核到原报告或 wiki/人工意见。

下文 **H** 指只读目录 `/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/`；**B** 指本仓 `base/skills/`。路径均可从这两个根直接定位。表中的 CPU 只属于写明的调用范围。

## 结论与已有能力的边界

现行 base 已有：实际 caller、共同对象、区分样本与全域、必要门足够即停、成本不明先真实探针、成熟结果立即消费、只重核受影响部分、停滞后重判、保持 NO/UNKNOWN 范围。DD 不支持把这些原则换个名字重加一遍。

有依据的新增候选主要是三个**父调用者动作**：

1. 增量文献返回更强基线时，立即重算活跃候选的比较门、取消已无竞争性的未启动工作并改派；合法性和既有证明保留。
2. 变更对象后，由具体保持定理划分“可继承命题 / 必须更新的缓存 / 新验证域”，再派 verifier；不能只问旧文件是否改过。
3. 一个真实代表输入测完后，实际消费为剩余批次成本与执行选择，保留已成功模块；不能探针交付后仍照旧全派。

固定规则障碍后的“哪些限制可释放”可作为 route-loop 的一个窄补充；余下经验更适合领域知识、失败实例或行为回归输入。

## 九个具体因果实例

### E1　停止坏对分数磨损，改问覆盖结构

**原因 → 改变。** 1152 机制通过局部边修改修好目标，却破坏同 fiber 的闭路线平面；后续若只按坏对少几百继续，不能说明生成规则接近完整覆盖。2026-10-27 08:38 人工要求“先提出可推翻预测”，09:27 明确停止这种局部磨损；尚未执行的 2520 枚举被取消，计为未执行。实际改读成功 H9 附件，从 non-star 邻域识别 Q-line，证明旧核心覆盖，再求少量 anchors。675 附件中恢复几何规则不算新图；最终 42343 的完整图和全根独验才计成功。

**证据与成本。** `H/research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md` 的 08:38、09:27、10:10、10:30、10:44 章节保存用户原话、失败预测及实际下一动作；`H/research/ddp/global_coverage_20261027/REPORT.md` 为原报告入口。更早 37628 的八 profile 贪心/一轮坐标替换最佳仍漏 115，419352 次评分的准备/编译/独核合计约 2.667 CPU 秒；它不代表整个探索成本。见 `H/research/ddp/breadth_20261027_wave4/record37628_single_extension/REPORT.md` 及 `terminal.json`。

**归属。** 停止分数磨损、提出区分性问题已在 B/efficiency 的“短探针”“最贵未闭连接”和 prove §5；**不新增同义 base 规则**。Q-line、折叠核心和锚点接口属 DD 插件。原 2520 未执行、旧 D2 暂停属任务状态。适合用来检验现行技能是否真的撤掉依赖失效预测的待派任务。

### E2　“复用验证”必须同时更新会变化的拒绝缓存

**原因 → 改变。** 保留旧边加新点可继承旧点对距离；但新点会缩短旧距离，所以旧 R4 球及“某项无 anchor”的旧负结果不能原封不动拒绝新基图。D11 跟进使用实际 current G 的精确增量更新，并对每个正例再做直接多源 R4 覆盖。18 个失败只属于各自被访问时的基图，不声称在终图仍失败。

**证据与成本。** [D11 原报告](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/more_graphs_20261027/h9_d11_followups/REPORT.md) 给出更新式：若加点 z 邻接 S，k=d_G(a,S)，旧目标新增部分在 k≤2 时为 R_(2−k)^G(S)，z 在 k≤3 时加入球；距离按真实 current G 计算。固定 20 项 0.513024 CPU 秒，产生两张完整增点图，正例当前覆盖检查两次，没有逐中间图全根 BFS。起点 37629 与已独验边表逐边比较、没有重跑其 BFS；最终 37631 的全根独验由 Root 另做。用户 11:50 的生产/验证取舍见人工主记录，不能扩成所有项目默认降低验证要求。

**归属与缺口。** B/mathrsi-verify §进入/恢复 已说“只重核受影响义务”，但没有让父 caller **消费一个对象变更的保持证明，划分继承结论、失效负缓存和新增域后再派 verifier**。这是小幅 base 候选；R4 公式和度数更新留领域。不是添加统一缓存平台，更不是默认“只验新根”。

### E3　F4 全局矩阵严格 NO 后，释放共享限制而保持真实逆关系

**原因 → 改变。** C60/F4 每 port 共用一个全局矩阵的完整 57600 域，6 个通过 forced-cell、0 个覆盖全部 3300 必要 rank3 对；共同零坐标的低秩像并集至多 61<64 证明必要性。这个 NO 没排逐边矩阵。下一模型保留控制器、方向和反向真逆，每条无向边分别选择 projectivity；一次 SAT 得到共同可行参数和 3840 点完整图。

**证据与成本。** [全局域原报告](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/f4_c60_global_projective/REPORT.md) 明确固定前提与未排范围。全域 0.084363529 CPU 秒；首项归一化准备失败的准确 CPU 未保存，不能把它算作全部成本。[逐边成功原报告](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/REPORT.md) 记录 150 选择、7200 selectors、14250 variables、24450 clauses，solver 0.233523 CPU 秒、准备+driver+solver 共 1.609514885 CPU 秒；全部约束重核后生产。独验全 3840 根约 0.087419 CPU 秒，Lean 成本另列 E4。

**归属。** 数学条件、必要性和有限模型属领域。B/efficiency“共同原对象”、route-loop Phase C/D 已要求修真正共享约束，**不重复增加“共同条件”规则**。可补的窄动作是：严格排除后先区分原规格要求与当前模型自加限制，若要释放共享限制，明确旧 NO 仍有效、保留哪些承重条件，再提出新真实 caller。不得由此擅自放开用户固定目标。

### E4　F4 的紧凑证书与成功模块复用，解决的是 kernel 表示成本

**原因 → 改变。** 图独验很快，具体 kernel 证书却受重复字面矩阵/decoder 展开影响。RouteData 51.92、首 row 52.79 CPU 秒后，将 3600 矩阵入口归入 402 个矩阵池、300 相邻 dart 归入 25 个 decoder 数组；`FastTables.matrix_eq_fast` 在 kernel 证明与原矩阵一致。已经成功的 MatrixCertificate 保留，消费者 API 修复没有重算该昂贵证书。

**证据与成本。** [BUILD_NOTES](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/BUILD_NOTES.md) 保存冷 `.olean` 读取首次 182.9 wall / 3.77 CPU 秒、缺 import 修复、数组表示调整和后续回执。压缩后 RouteData 12.18、同 Row00 29.27 CPU 秒；Rows01–59 三 worker 共 2020.311852 CPU / 698.85 wall 秒，Row00 不含在后 59 行内。矩阵桥 18.91 CPU 秒也有成本。前后尝试同时修过接口，不能声称一个变量造成固定倍数加速。

**归属。** B/lean-formalize/references/lean-working-loop.md 的 “Choose representations by real use”“Keep compilation and performance evidence useful” 已明确真实 consumer、桥引理、缓存和冷热条件；**不改原 ARIS 快照、不另造缓存框架**。紧凑池和保义绑定属领域/形式化实践实例，可作为 E5 消费规则的证据，不足以宣称系统 RSI 加速。

### E5　Q8 在花费 558 CPU 秒时测一条真实 row，再决定全批怎样完成

**原因 → 改变。** 初始完整形式化已付成本，不能通过只展示末端成功模块消失。暂停点 49 PASS、48 保持不变；改用 packed witness 的一条真实 full row 640 对耗 7.353664 CPU 秒，再用剩余 1047 行估算 7699.286208 CPU 秒、含桥预计全批约 8500，沿同一 12000 CPU 预算继续。47 条既有 row 继续原 NatTable，剩余同一 witness 分块紧凑保存，成功 row 不重编；末端 stack overflow 另作本地资源修复。

**证据与成本。** [COST_REASSESSMENT.json](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/formalization_full/COST_REASSESSMENT.json)、同目录 `README.md`、`FINAL.json`。最终累计 8413.702687 CPU 秒、1104 新模块 PASS、6 个失败尝试保留；完整 669905 projection pair，pilot 1225 与新 668680 分列。`estimate_is_guarantee=false`；FINAL 没有同范围总 wall，不能把累计 CPU 换成人工等待。

**归属与缺口。** “先真实探针”已存在，新增候选仅为 B/mathrsi-prove §2“领域数学/计算”及 §4 的**探针返回消费**：保留已用成本与已 PASS 范围，用实测代表规模估剩余及下游开销，决定继续、换表示或收卷；不得默认重建成功前缀。B/efficiency“短探针”可补一个完整 paused→测量→改批的例子。无需所有任务填统一预算表；只在批量资源已影响决策时执行。

### E6　基线更正应该撤掉无竞争路线，并可变成更强构造输入

**原因 → 改变。** 公开主表缺项不是公开不存在。13D5 的 51418–51457 仍合法且超过保存 51417，但作者包报告 88452；合法图不能继续写成全球纪录。更实质的路线变化在 q7：旧 22 点 partial ovoid 产 161150；深读原 Table5 的 W(7) 33 点对象后，公开方法组合保证已是 161650，旧比较失效，停止旧纪录目的续批，改复现公开 33 对象及其 fullN 接口，成为后续 P33 家族输入。

**证据与成本。** [P33 比较更正 wiki](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research-wiki/experiments/ddp-public-w3f7-partial-ovoid33-primary-table5-corrects-65-70-77-comparison-20261101.md) 的 Reasoning/重启依据，以及 `H/research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md`。一次 3 query 沿 primary 到 p140 §4.3 Table5；外部等待无完整计时。数值代入仅约 0.000007234 CPU 秒，不代表检索成本；33 坐标复现约 1.185447、接口约 0.071536 CPU 秒。161650 等是本项目组合已发表方法所得保证，未定位同数字作者边表，不是全球最大认证。`H/research-wiki/experiments/ddp-d13-singlefault-star-family-51457-20261027.md` 另区分 88452 作者包及作者保存 BFS 报告与本机未复验。F4 的 24 度 4544 在生产前即被公开 6144 挡住并取消；后转更强 GQ 来源，见 guide02 §8–9。

**归属与缺口。** B/mathrsi-survey §5 已要求准确基线，§7 已回原义务；缺的是**父 prove/route-loop 收到新基线后的调度消费**。建议在 B/mathrsi-prove §4 与 route-loop Phase D 的新文献返回处补：重算受影响候选的门槛和贡献、保留合法性/旧核验、撤掉已无竞争且尚未启动的任务、从更强来源重选任务；与用户允许的“纯合法实例”任务区分。不必为比较更正重跑旧图 BFS 或全篇审阅。

### E7　固定完整邻域到顶后，改变承重连接可以越过旧障碍

**原因 → 改变。** 346515 的 full-N_H 固定复制规则已受限制；成功并非偷偷无视上界。新规则删 65 条 diagonal clone→own filler 边，加一个 hub 连全部 65 fillers，保留 H 的 13862745 条旧边，得到 346516，边数保持 14204970。这改变旧 mandatory full-N_H 邻接，旧 fixed-adjacency 否定结论仍真。

**证据与成本。** [重分配原证明](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/PROOF_DRAFT.md) 给出真实 owner、全部字面 delta 和路径分类。生产 0.940117171 CPU 秒；独验重查 65 个改变 diagonal 根加 hub 共 66 根，不是全 346516 根。4160 个未变 off-diagonal 根继承依据是其路线留在 U/H 内部，而非只因根标签未改。新的具体 Lean 与外部 scope 分别存在，不借旧 PASS。

**归属。** “改假设可重启”已在 B/Lean working-loop 和效率参考；可与 E3 合并为一个 route-loop **可释放模型限制**的例子。具体删补规则、路径论证与受影响根分类属 DD 插件。E2 的 base 验证消费应能承接它；绝不能泛化为删旧边后仍默认旧点对自动保持。

### E8　D16 找到够用的 32 块后冻结，不把 feasibility 当最大 packing

**原因 → 改变。** 旧 FOUND31 是首次找到 31 即停，非最大值。新问题只加 ≥32 行，保留原 192 变量、192 目标负载模型，零目标一次 HiGHS 找到 32 块、160 不同目标标签；这提供足够接口但不单独提供完整图或最优性。后生产 864 个 fullN 克隆并做新终图验收/具体 Lean，未借 16389 的图 PASS。

**证据与成本。** [32块原门](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/controller_pack32_gate/NOTE.md)；其 RESULT 的记账累计与 NOTE 四舍五入/driver范围略不同，见 guide04 §5。solver 1.951147927 CPU / 1.955020 wall 秒；RESULT 累计 charge 10.13869782，其中旧 7.714861215、新实际进程 2.223836605、准备 charge 0.2，不再另加 solver。新图生产 0.223061134 charged CPU（其中实际 0.123061134+准备0.1）；全终图独验套件 11.413770046 CPU。`degree16_plane864/formalization/FINAL.json` 记新 Lean 14.020610885 CPU、5次尝试含1失败、旧 PASS 重编0；旧源/16389 首次形式化共675.777657109 CPU，是共享前提成本。

**归属。** “见证够用即停”“只重核受影响”已在 B/prove §1/§2；**无新增 base 行为**。具体 controller 横截块属领域；FOUND31/32、输入标签与外部优先权 UNKNOWN 属任务状态。可用于测试消费者是否停止不必要最大化、先完成原图连接，而非根据 solver 的 `Optimal` 字样宣称最大基数。

### E9　修好一个门不等于整体改善；NO 与 UNKNOWN 选择不同后继

**原因 → 改变。** N2 六个已保存基例上 3048 个合法 repair 参数中，426 真修好旧失败 pair，却全部损坏新根覆盖；本轮没有一个进入全旧根检查。保存“局部修复确实有效”和“联合目标失败”两事实，不按 repaired pair 数续算。另 public106 的一次 10 秒 MILP 无 incumbent 返回 UNKNOWN；后来纸面排除保持 C7 且只改 G[S] 的 S10/S11 子族，不把旧 MILP 追改成全族 NO。

**证据与成本。** [N2 repair 原报告](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/NOTE.md)、同目录 `SIX_SAVED_BASES.json`、`RESULT.json`、`ALL_ACTUAL_VARIANTS.tsv`。原 pair 0→1 由4修到1，新根41→1变4；全部终图度数仍合法，失败不是度数。0.099139578 实际 CPU+0.15 准备 charge=0.249139578；严格关闭仅指定六基例/第三cut/一次repair/pin替换域。public106 见 `H/research-wiki/experiments/ddp-d2-public106-internal-pin-old-edge-repair-scoped-gates-20261101.md`；唯一 6253变量/23161行模型累计10.514675635 CPU，后对称传播同 case 10.585169327，不相加为两个独立总额。

**归属。** 共同条件、样本/全域、UNKNOWN保持开放已在 B/prove、route-loop 和 efficiency；**不新增状态 taxonomy 或“失败就换线”硬规则**。此处应保存为领域失败/重试边界和消费者回归输入。不能用放松可行或 32 个未命中样本宣称全族 NO，也不能恢复旧 N(8,2)/n61 队列。

## 候选改动落点与不应做的改动

| 候选 | 现有规则已做什么 | 真正还需观察的消费行为 | 精确建议位置 |
|---|---|---|---|
| C1 基线更正驱动重派 | survey 已区分原文纪录/公式推论/本次来源范围并回原义务 | 父读取新门槛，修 active 比较，取消过时的未派批次，选择更强公开输入或转别的参数 | `B/mathrsi-prove/SKILL.md` §4“每轮按实际结果推进证明”；`B/mathrsi-route-loop/SKILL.md` Phase D 的文献回流段；survey §7只补返回需明确影响的候选，不重写整轮survey |
| C2 有保持理由的增量验证 | verify 恢复段已要求只重核受影响义务 | 从真实 delta 与保持定理导出继承域/变化域；负缓存可能需更新；父据此给 verifier 准确任务并消费覆盖 | `B/mathrsi-verify/SKILL.md` §1（对象域/检查器/输出使用之间），及 `B/mathrsi-prove/SKILL.md` §4 参数改变后的重核段；公式放插件 |
| C3 代表成本回执变成实际批次决定 | efficiency/Lean 已有真实探针、缓存、同目标比较 | 暂停点成果不丢，实测后估剩余与桥接开销，在原预算内明确保留/更换表示/继续域；随后实际执行选定动作 | `B/mathrsi-prove/SKILL.md` §2“领域数学、构造搜索或确定性计算”探针返回处；`B/mathrsi-research/references/efficiency.md`“短探针应回答一个决策问题”补Q8消费例 |
| C4 固定族障碍的可释放限制（次优先） | 已有反例限范围、改假设可重启 | 旧 NO 后辨认限制来自原规格还是工作模型，放开一个有数学理由的共享/邻接限制，保留旧NO并生成新caller | `B/mathrsi-route-loop/SKILL.md` Phase C/D；E3/E7放领域材料，由base只问边界与下一动作 |

**建议先试 C1/C2/C3，C4 可作为 route-loop 具体例而非又加一套流程。** E1/E4/E8/E9 已有原则主要欠真实回归验证，不能因 DD 案例新就重复扩 base。领域 math、源对象和具体 parser/binding 应进未来 DD 插件或任务记录；本轮不创建插件。source首次昂贵核验与后续增量同列成本，不为每个实例重新全扫。拒绝把所有成功产图当纪录、把实例数当机制数、把必要门通过当原图、把重放当发现，也拒绝增加强制双扫/逐图Lean/双模型检查栈。

## 成本解释的硬边界

`H/guide/04_TIME_COSTS_AND_REPLAY.md` 的461行索引中，`duration_raw`仅92行出现、89行非空；很多其它时间在真实 RESULT/FINAL，空字段不能按0。缺贯穿全程的 LLM wall/token/金额、人工等待、统一硬件占用，不能得出完整总研究成本或系统A/B倍数。

生成3750的0.106812 CPU秒是在参数已确定后写图；不含发现、失败路线、独验或形式化。F5最后 decoder/exact 成功批也不覆盖早期123.903922与110.762498 CPU秒编译失败。CPU、wall、硬预算和 preparation charge分别报告；cumulative含子项时不再相加。F4三worker累计CPU与wall不是同单位；Q8 shared三目标外审一次调用不能算三次等待。旧14秒增量Lean用了既有编译源，不承诺冷环境从零14秒。当前有局部表示/组织前后证据，无排除其它因素的系统效率A/B。

## 建议的小型行为试用（尚未执行）

试用应由未写补丁者从原输入执行，保留实际下一任务/命令和父消费；下面“验收观察”供评估者使用，不放进受试agent的输入里。用历史已知答案只能检验调用行为，不是盲解题率评测。不运行旧Goal，不默认重放大图/Lean。

| 试用 | 给使用者的原始输入与任务 | 评估者检查什么 |
|---|---|---|
| T1 基线更正 | `H/research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/partial_ovoid65_gate/cubic_coset22/REPORT.md`、当时待继续批次范围，以及 E6 的 `W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md` 中原Table5摘录/公式和来源定位；要求父prove消费这份增量survey并交下一项工作包。不给后续P33成功总结 | 是否保留161150合法性、纠正比较、停止旧纪录目的续批，转33点接口复现或其它有理由任务；是否避免重验旧图/重做整个survey。此包未带原报告所指 `w3_f7_threshold25_sources/` PDF/截图，因而这只验既有survey证据的消费；不能称本轮独立读primary或完成联网查新。仅读后写建议而未实际派发不能称调度行为通过 |
| T2 增量验证与负缓存 | 给D11原REPORT、加入前/后参数及缓存版本说明；另在独立小工作副本给合成C5边集 `{01,12,23,34,40}`、已有D2接受事实，加新点5邻接`{0,2}`，再给“另删旧边12”的分支。任务是制定并实际执行小图验证 | 纯增边分支可用旧点对保持+新根覆盖；删12分支不能继承原旧点对，虽新根仍D2，旧pair1→3距离变3。检查者应发现真实失败；父不能把“只验新根”作所有delta规则。合成图只是行为夹具，不冒作历史DD成果 |
| T3 真实成本消费 | E5目录的 `PAUSE_BARRIER.json`、`attempts/EvenQ8SourceFullDerivedRow040/attempt0003.json`、原 `PRED.md`/`MODULE_PLAN.json`，从 `COST_REASSESSMENT.json` 仅提供当时已用558.4055、49PASS/48未变、剩余1047行这些原始状态，不提供后来预测/FINAL。要求产生并执行一个有界新模块/小row任务，父按回执更新后续安排 | 是否保留旧PASS，区分已用/预测余量/预算，给出有依据的剩余估计而非保证，实际消费回执；只改报告、不改变后续安排则该关键行为未过。`CHECKPOINT_B/C`已是闭合终态，不能冒作当时暂停断点；环境无匹配Lean/编译依赖时明确仅消费静态审查，不用旧FINAL代替试跑 |
| T4 固定规则NO与UNKNOWN | F4全局REPORT和逐边真实接口定义，或public106 `MODEL_SCOPE.json`/`SOLVER_RETURN.json`与后来C7纸面NOTE；要求路线caller决定下一精确义务 | 是否保留原NO/UNKNOWN的准确域；能否指出可释放的是模型自加共享限制、必须保留的是真逆/原规格。不得把后来子族NO覆盖旧UNKNOWN、不得自动重启solver或换seed |
| T5 联合门失败 | N2 `SIX_SAVED_BASES.json`、指定第三cut/repair/pin替换规则和一份原始RESULT/短路径；在独占小副本重算这一个已保存见证，父消费 | 是否同时报告旧pair修好与新根失败，按真实反例停止该指定预测的依赖；不把426修复数当成果，不从一例推整域NO，完整3048域结论另依原覆盖记录 |

建议 C1 用 T1、C2 用 T2、C3 用 T3 各先做一次，遇具体失效再修实际caller。T4/T5用于有改动覆盖该路径时的窄回归，不为凑完整评测矩阵全部执行。没有同输入成本对照时只报告消费行为改善，不写“提速N倍”或“已证持续RSI”。
