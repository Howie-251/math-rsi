# DD 效率经验：供新 meta-evolve 技能独立执行的有界输入

2026-11-03。按最新指令停止扩大源阅读，先完成并整体集成 `mathrsi-meta-evolve`，再由该技能消费本文件及 DD context。本文只交历史事实、候选行为与小测试，不改 base/插件、不启动数学 Goal、旧 solver、Lean 或评审。下面七项来自实际已读原件；测试是新技能的决策测试，不要求复跑数学。

长证据复用：[阶段原件审计](early/SOURCE_AUDIT_EARLY.md) §17–24；[逐文件阅读账](early/READ_LEDGER.tsv)；[较早选择性提取](DD_EFFICIENCY_EXTRACTION.md) E3–E8。后者含本轮广读前已经核读的后期 DDP 成功链。源码根统一为 `/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/`；下列路径及行段均相对此根，链接打开起始行。历史 active/命令不构成当前授权。

## 1. 基线更正必须改变在排队的研究，而非只修改比较表

**旧行为。** 本地 q7 partial-ovoid22 图161150合法，被旧公开参数15给出的160750衬成改进；继续65/70/77目标会消耗研究资源。

**原件与改变。** [W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md:3) L3–36、40–50：直接读取印刷p140 §4.3 Table5，W(7)已有33点对象；相同公开方法组合保证变成161650/169900/181450。撤掉旧竞争目的续批，转向复现公开33点对象及其 full-N 接口；没有把旧图判非法，也没有为改比较重跑旧图BFS。

**结果与成本。** 原161150相对新161650为−500；条件77门槛也随之重算。一次三query及primary查阅，没有完整检索耗时；约0.000007234 CPU秒仅数值代入，不能当发现成本。161650是组合已发表方法所得保证，不是找到作者同数字边表或认证世界最优。详见旧提取E6。

**新技能可检验输入。**

```json
{"task_purpose":"improve_public_bound","accepted_local":{"degree":65,"D":3,"n":161150,"valid":true},"old_public_guarantee":160750,"new_primary":{"page":140,"section":"4.3 Table5","partial_ovoid_size":33,"derived_public_guarantee":161650},"queued_work":"continue old O22 record campaign","new_solver_authorized":false}
```

**预期。** 保留图合法性；撤销当前竞争主张及相应未启动续批；重算受影响门槛；把更强公开对象列为候选输入。若任务本来只要合法实例，不替用户改目标。不能把“表缺项”解释成不存在、把primary报告的穷尽最大值冒作本机复验。

**候选归属。** 通用的缺口是父 `prove/route-loop` 对survey新基线的调度消费；`mathrsi-survey` 已要求准确比较，不再原样新增一条“核查基线”。具体GQ/Delorme公式属DD，实际数值与队列属task state。建议新技能评估既有 `mathrsi-prove` §4 / route-loop Phase D 的消费者，而非先改插件。

## 2. 严格NO之后可释放工作模型的限制；用户固定规则仍须保留

**旧行为。** F4/C60每port共用全局projectivity，完整57600域失败。若把这一NO当成全部F4连接不可能，会错失逐边规则；若不写清规则变化，又会错误推翻旧NO。

**原件与改变。** [global REPORT](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/f4_c60_global_projective/REPORT.md:5) L5–21、70–83、107–112和 [edge REPORT](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/REPORT.md:12) L12–28：放开全局共享，150条无向controller边分别选projectivity，仍保控制器、方向与反向真逆。新共同SAT产生完整3840点20正则D3图；旧全局NO仍真。

另一个实际越界成功的例子是 [diagonal_fill_reallocation/PROOF_DRAFT.md](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/PROOF_DRAFT.md:3) L3–24：从346515删65条diagonal clone→own-filler边、加hub连65 fillers，保13862745条H旧边，得346516/14204970边。它明确改变旧mandatory full-N_H clone规则，不与旧fixed-adjacency障碍冲突。

**结果与成本。** F4全局穷尽0.084363529 CPU秒，首项准备失败CPU未留；逐边solver0.233523，准备/driver/solver合1.609514885。hub生产0.940117171 CPU秒；验证重查改变的65 diagonal根+hub共66根，4160未变off-diagonal根依赖路线留在U/H内部的证明继承，不能仅凭标签未改跳过。

**新技能可检验输入。**

```json
{"old_no_scope":"same projectivity shared by every edge of each port","fixed_by_user":["controller","reverse maps are actual inverses"],"model_choice":"global sharing","proposal":"one projectivity per undirected edge","old_no_exhausted":true,"execute":false}
```

**预期。** 输出旧NO精确域、允许改变的模型限制、仍需保留的承重条件及新真实caller；不自动求解。第二测试把 `fixed_by_user` 加上 `every clone must retain full N_H`：hub删边方案应判当前合同外/待新授权，不能悄悄释放。只在用户目标允许规则变化时提候选。

**候选归属。** 通用消费者缺口是在NO之后辨别限制来自原规格还是当前工作模型，已有“共同对象/改假设可重启”不重复增加。具体projectivity、删边/路径和受影响根分类属DD；旧NO和新图状态属task state。

## 3. 新探针被证明自动成立，应收卷；后半章会覆盖前半章的“下一问”

**旧行为。** 新旧61对齐后，提出6×6二阶矩阵Q的非负性与边际，准备据此探索更强约束。

**原件与改变。** [POST_ALIGNMENT_NEXT_QUESTION.md](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/proofs/dd82/n61/POST_ALIGNMENT_NEXT_QUESTION.md:90) §4 L90–174是提问；§6 L280–401逐个普通/特殊行、ε/η完整证明Q≥0和边际均由原接口自动成立。后续§8–9 L439以后转向实际H与必要父类共同生成，不继续把Q当新筛。

**结果。** 探针没有新排除、没有证明严格加强、没有新SAT；其价值是以具体证明取消无增量路线。整段成本没有完整量化，不能用后续solver秒数估填。长审计§17。

**新技能可检验输入。**

```json
{"proposed_next":"encode Q>=0 and its marginals as new pruning","source_sections":["POST_ALIGNMENT_NEXT_QUESTION.md:90-174","POST_ALIGNMENT_NEXT_QUESTION.md:280-401"],"later_result":"all proposed conditions follow from existing interface in every case","old_terminal":"no solver launched","execute":false}
```

**预期。** 以完成证明覆盖旧计划，标记“自动后果、无新增筛域”；拒把它命名成新机制/新性能收益，不推荐补小条件重跑；保存推导作为解释工具。不能把停止此探针扩大成原题或整个数学来源耗尽。

**候选归属。** 通用是消费后续结论并撤掉陈旧next-action，已有停滞/失败地图不再加同义口号。Q公式与case proof属DD；失效next-action属task state。

## 4. 同域历史RAW足以研究避重，仍不足升级严格结论

**旧行为。** 新V3 internal-double得到结构与h1认证后，r1/r2四次UNKNOWN，曾把长double路径继续列为新开放构造范围。

**原件与改变。** [OLD_NEW61_ALIGNMENT_MATH.md](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/proofs/dd82/n61/OLD_NEW61_ALIGNMENT_MATH.md:33) L33–127证明“实际B2两边共端”与旧t0[3,3]完整四父集轨等价，不需I12/no-O、B连通或全图无triangle；[原对齐处置](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research-wiki/DD82_OLD_NEW61_ALIGNMENT_20261018.md:38) L38–49、69–77区分两层。按用户纠正停止重叠internal研究，保其结构工具和新h0独立认证价值。

**结果与成本。** 四旧RAW墙钟822.694/4212.021/5631.030/192.947秒，均exit20/proof:null、certified=0；八历史CNF已缺。新UNKNOWN不推翻旧RAW，也不能被旧RAW改写为新checked。严格层D-path/全共端排除仍有认证缺口；不能把I12 H∧¬O条件性结论移到全域。长审计§17、19。

**新技能可检验输入。**

```json
{"new_route":"continue r1/r2 internal-double construction","new_results":["UNKNOWN","UNKNOWN"],"mapping":"any two B2 edges sharing an endpoint iff one old complete [3,3] orbit; four orbits cover","old_evidence":{"terminal":"UNSAT","proof":null,"certified":0,"historical_cnfs_missing":8},"new_certification_authorized":false}
```

**预期。** 继承RAW等级作避重、停止把同域当新构造入口；保留严格认证缺口与已证独立工具；不重跑补证、不宣称D已认证matching、不把新旧调用时间相加作不重叠收益。报告用户纠正导致的实际路线更换，而非只附免责声明。

**候选归属。** 通用缺口是“范围映射+等级”被调度消费者共同使用；图论等价证明属DD，映射表/缺件属task state。无须另建通用RAW证明定理。

## 5. 把同一原对象与全部caller接入，才把前端成功转成有效结论

**旧行为。** 固定H35通过双五色与rho容量，或单packing/局部配边能写，并未提供完整61图。初相邻double七型profile全UNKNOWN，不能说数学已经用尽。

**原件与改变。** [GENERAL_SIX_STAR_H35_NORMALIZATION.md](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/proofs/dd82/n61/GENERAL_SIX_STAR_H35_NORMALIZATION.md:1) §3–6指出二次定标限制与真实AP30对/同一父类义务；[EPSILON0_CHECKED_EXCLUSION.md](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/proofs/dd82/n61/EPSILON0_CHECKED_EXCLUSION.md:13) L13–23把真实第二packing/R18、自由双色、完整S/T、端口及全部1830原pair接到同一输入。不是择一个便利核，亦未把之后新精确预算加进冻结CNF。

**结果与成本。** ε0发现96329变量/433762子句，4.643433 CPU秒RAW；另同input取证5.026064，checker0.136446，最终只关ε0/η自由。ε1独立重证port=c+b−1，保P∩Q自身port1，另同输入认证后合得任意原图边Δ≤1；非相邻double/无double及整61仍开。实际CNF/LRAT未随包携带，只保原接受日志，当前未复放。长审计§18、20–21。

**新技能可检验输入。**

```json
{"goal":"original61 degree8 diameter2","current_candidate":"H35 passes local colors and rho","missing_callers":["same S/T partition","actual port equations","all 1830 original pairs"],"proposed_shortcut":"certify only H35 local model","target_artifact":"complete original graph or complete branch exclusion","execute":false}
```

**预期。** 指出尚未闭的具体caller，不把局部实例判成功；优先共同表示真实剩余边/父类/原点对。若输入改为完整ε0原图归约及saved checker receipt，认可该分支成果及准确imports，不再要求与其无关的新预算稿/整阶Lean来接受此范围。

**候选归属。** 数学表示与归约属DD；通用已有“共同对象/actual caller”应保留不动。本案可检验新技能是否定位实际缺失consumer、复用旧成功检查，而非机械生成另一份共同对象清单。

## 6. 明确UNKNOWN之后冻结输入；新结构可成为新机制，弱后果不自动续授预算

**旧行为。** 完整46点原图输入一次504158变量/1816574子句、88.006871 CPU/88.150863 wall秒UNKNOWN；没有model/proof或可续CDCL状态。

**原件与改变。** [nonadjacent46 RESULTS](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/computations/dd82/n61/nonadjacent_double46_full61_run/RESULTS.md:3) L3–11按用户意见冻结、回连续纸面、Lean后置；不按h/交数/seed拆或加小条件重跑，也不为明确UNKNOWN再开结果外审。后来实际H6不同ports→全W/三matching/UV2P3+2K2是新完整结构，才成为共同输入；[H6 RESULTS](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/computations/dd82/n61/h6_joint_w_completion_run/RESULTS.md:3)保全部第三匹配720、端口父色，一次87.867778 CPU秒又UNKNOWN后同样收卷；新repeat-support定理未临时塞入重跑。

**结果。** 局部纸面可排真实子域、保工具，整体仍未解；不把短UNKNOWN当来源穷尽或“接近成功”。H6的244边八正则fixture直径3/651未盖仅验证前端，不是数学进展或目标正例。长审计§22–24。

**新技能可检验输入。**

```json
{"frozen_input":"nonadjacent46","terminal":"UNKNOWN","cpu":88.006871,"saved_solver_state":false,"user_instruction":"continuous paper reasoning; no h/seed/small-cut retries","new_result":"an identity already implied by the frozen model","proposed_action":"add it and relaunch for 90 seconds"}
```

**预期。** 拒绝该重试，保持原目标、用户边界与UNKNOWN原状；把新弱式收为解释工具或拒绝项，选真实未闭共同义务。第二输入换成“完整证明的新H6结构、覆盖映射与独立输入计划”：允许提出实质新机制供既有授权判断，但不能由本测试直接执行或推断必有速度收益。

**候选归属。** 通用是已授权边界内的行动选择与停止条件消费；精确H6证明属DD，冻结input/资源/用户指令属task state。拒绝固定轮数停机、任意弱条件都可重试以及用报告代执行。

## 7. 验证按真实依赖与变化复用；证书检查CPU不能冒作发现成本

**旧行为。** 把“所选triple有h0”当作全局h0，会错误允许给新triple加cut；反方向若得到全局h0却重跑其h1证书、全旧模型sanity，则浪费已有效证据。

**原件与改变。** [INTERNAL_DOUBLE_FINAL_PORT_CONSEQUENCES.md](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/proofs/dd82/n61/INTERNAL_DOUBLE_FINAL_PORT_CONSEQUENCES.md:5) L5–13、24–30：checked r0产生**任意连续D-triple**的h0，新v-u-z重根才可得66负second-threshold units；不是当前triple局部h0自动合法。r2保121选择中的51合法/70禁pair。原body/变量不变，检查delta真值和body保全，继承h1，不重算它；两新profile仍UNKNOWN。

编译侧同样有真实瓶颈与复用：[F4 BUILD_NOTES](/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/BUILD_NOTES.md:5) L5–16：冷olean首182.9 wall/3.77 CPU；literal intern后原graph不变，RouteData51.92→12.18 CPU、同Row00 52.79→29.27；kernel矩阵桥18.91另记。保已过row模块、三workers完成Rows01–59为2020.311852 CPU/698.85 wall，Row00另29.266997。不把变表示等同数学改变，也不把前后接口修复算单变量受控倍速。

**结果与成本边界。** ε0/ε1分别“发现→取证→checker”的CPU为4.643433→5.026064→0.136446和5.519699→6.009175→0.162162，不能只报末项。CPU/wall、准备收费/实际进程、共享前提/新增检查分开；同父累计与子项不得重复相加。缺原CNF/LRAT只说明当前包无法复放，不抹历史acceptance，也不称已本机重验。

**新技能可检验输入。**

```json
{"accepted":{"theorem":"h0 for every consecutive D triple","origin":"checked r0","artifact_present":false,"original_receipt_present":true},"new_use":"triple v,u,z if B_uz=2","delta":{"existing_variable_bits":true,"new_units":66,"old_body_preserved":true},"request":"plan minimal validation; do not execute"}
```

**预期。** 先验新use是否在全称域；只继承实际满足依赖的旧结果，核cut/bit语义及body delta，无授权不重跑旧h1。把theorem改成“selected u,v,w only”时，应阻断66cut的数学前提，不能靠checker将错误归约补成真。测试额外要求解释182.9wall/3.77CPU只能说明该次冷I/O，不能推定所有Lean成本均I/O；给出缺总成本/重叠口径，不造总加速比。

**候选归属。** 通用缺口是验证调用者消费依赖、变更和已存在收据的决策；已有等级记录/缓存要求不原样复制。各数学定理与桥属DD，具体依赖/cut/build模块及预算属task state。

## 未读范围与执行边界

这不是“全库已读”。early账本对分配目录的收束状态为：264份全文正文、105份全文代码、239份结构数据/日志解析、9份完整差异阅读并继承重复段、4份完全重复继承、1份部分代码；**2560项UNREAD，另59个文中引用路径在交接包缺失**。清点和引用命中不计阅读。早期审计§1现已补当前数字；各后续节保留分批历史。

未读主要包括：大量construction/计算域及输出；H5余下完整证明、GLOBAL_SPECTRAL_FACTOR_ARITHMETIC与其余n61材料；两portfolio全部原始卡/registry/刷新细节；context/dd82余文及archive总REPORT；多数对应wiki。`joint_six_star_h35_run/encode.py`仅L1–190（导入CNF原语完整）已读，后半未读。某些n62较强中间工具已补、某些仍未读，以逐行ledger为准，不据导航推全。

较早选择性提取中的后期DDP原报告只覆盖所列实际成功/失败链，不代表其整个父目录已审。原数学Goal仍不在本任务授权内；本文件不请求补跑、外部审阅、发布或改旧源。按新顺序，下一步是**已集成的新技能独立消费这七项，产出提案/测试/验收，而非继续把几千原件阅读设为前置，也不是直接将上述候选写入base**。
