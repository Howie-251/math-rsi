# 验证范围与执行分账

2026-11-06现时摘要：**通用full-Hall排除已被实际23点757模型反驳；该模型物理横截恰3，$\tau_{R_6}\le5$主目标及31点临界caller仍开放。** 后续固定24点插入域已checked UNSAT；physical31首片外部TERM，未报SAT/UNSAT。当前工作界40/49/75/76不变。报告涵盖2026-11-05至06执行；全部新增结果仍为 **unreviewed / unaccepted**，没有独立外审或生产验收。native Sol独立实现的颜色枚举与证书重放已实际在Linux通过；局部CNF成功checker的范围另见第3节。

## 1. 科学执行终态

早期sandbox SSH preflight为socket permission denial，exit255；其后一次显式提权只读preflight经auto-review允许，但实际remote connection closed，exit255。二者为不同事件。后来连接恢复，按既有授权新目录上传及受控执行成功；早期零调用记录仅描述其当时时段。完整时间顺序保留在[STATE.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-clique-source-hall-20261105/STATE.md>)，不公开私有连接身份。

Linux `py_compile` exit0。bounded validation exit0，实际状态为`PASS_BOUNDED_EXACT_PROJECTION`：512项n3完整projection、1个shared-role正例、6144项n5颜色/active-prefix、20项inactive mutation、40项primary mixed-color及nonprefix/独立bitset auditor控制。实际测试原件为[encoding_validation.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_clique_source_hall_20261105/stage_evidence/encoding_validation.json>)；它是有界实现测试，不是36点UNSAT或全称数学验收。

两份新CNF已实际生成，均覆盖active-prefix至多36点：

| Case | 变量 | 子句 | 字节 | CNF SHA256 |
| --- | ---: | ---: | ---: | --- |
| 757 | 345580 | 1753574 | 38038697 | `e6d8da26f582d5ab6f2fd108f07d0f4c10b07f1fd9d47daa7ac48b3be322657b` |
| 766 | 415733 | 2015928 | 43142651 | `fbf56330513e0c23ca75f972794d2933872f6493de456bf3202338846916a878` |

实际执行两个受控external Kissat首片，各600秒预算、8 GiB地址空间、2 GiB单文件限制；无自动续跑。两个进程组均已结束，未触及其他旧作业。

| Case | 实际终态 | 后继 |
| --- | --- | --- |
| 757 | exit10，SAT，57.804180秒 | `audit-model` exit0，7.008825秒，`AUDITED_ACTUAL_SAT_COUNTEREXAMPLE` |
| 766 | exit0，`s UNKNOWN`，600.029733秒；内建时限，非强制终止 | 无SAT审计触发，无UNSAT checker触发 |

两份最终原件分别为[757 RESULT.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_clique_source_hall_20261105/solve_slice01_evidence/solve_slice01_757/RESULT.json>)与[766 RESULT.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_clique_source_hall_20261105/solve_slice01_evidence/solve_slice01_766/RESULT.json>)。累计该首片范围有2次solve、1次成功实际颜色SAT audit、0次proof checker。两个partial DRAT均保留于Linux；SAT trace及UNKNOWN trace都不是UNSAT证明。本轮没有Windows科学执行。

## 2. 23点反例与独立物理横截核验

完整颜色原件[sat_audit.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_clique_source_hall_20261105/solve_slice01_evidence/solve_slice01_757/sat_audit.json>)的SHA256为`85c47e038e47e4537d71af97079c834860033a5926cf0f07c8190fba7473820d`。757审计检查完整赋值、公式重建和每条子句，再从1771个实际三元组颜色重算全部路径限制、完整源集与匹配。

另一个native Sol实现独立读取该固定颜色，枚举全部2至7点子集，核对连续三元组/全部三元组路径判据、8855个packet及全部同端点限制。全部实际红六恰92条；全源恰$F=\{0,1,2,4,8,15\}$且全红，六条饱和匹配路径在[enumeration.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/enumeration.json>)及现用正文第7节。无红七、无蓝五、无weak7。因此它是通用full-Hall排除的实际反例，同时属于766母类；不声称几何实现。

[transversal.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/transversal.json>)枚举横截大小0、1、2、3层，得唯一最小$K=\{0,14,18\}$、$\tau=3$。独立[replay_receipt.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/replay_receipt.json>)直接以全部三元组重建92条红六，重放最优横截及完整低层反证书，状态`PASS_INDEPENDENT_REPLAY`。475行证书由277行覆盖全部大小至多2的点集，另有198行合法三点层漏点见证；不能把475行说成全部必需的下界证书。三条不交红六也给简单下界3，见[original_packing.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/original_packing.json>)。

两项主要独立程序的受控运行及重放均exit0，无超时，见[run_receipt.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/run_receipt.json>)。private路径统计也实际通过，见[private_paths_result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/private_paths_result.json>)：按$F$顺序为$[12,2,2,0,2,5]$，源4无private，所以$F$不是inclusion-minimal横截。该统计不把物理$\tau$改成6。

## 3. 后续两个独立探针的实际终态

### 3.1 固定24点单点插入：checked UNSAT

[覆盖原件](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_private_hall_extension_20261106/COVERAGE.md>)固定旧23点全部1771色，只插入$z=15$，并固定新源集$F=[0,1,2,4,8,16]$、映射后的原满匹配、全源private及指定private红六$(4,5,9,10,14,z)$。新点相关253个三元组可以变化。此完整固定域的solve exit20、0.254508秒；checker exit0、0.755343秒，`check.stdout`有唯一`s VERIFIED`。

实际[EXTENSION.cnf](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_private_hall_extension_20261106/fixed_evidence/EXTENSION.cnf>)已完整取回本地，9364183字节，SHA256为`761eeca28afd9870b7e3191124c24e16461ccb276adf123fbf2ed327c9198e04`；[solve.drat](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_private_hall_extension_20261106/fixed_evidence/solve.drat>)为1280957字节，SHA256为`a8eae93c6c1d6b8b321194a45847a186d9fdb420b244cfe31bcf5fa3e6501dc7`。文档worker以LiteralPath存在及哈希检查确认二者。完整绑定与终态见[RESULT.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_private_hall_extension_20261106/fixed_evidence/RESULT.json>)、[check.receipt.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_private_hall_extension_20261106/fixed_evidence/check.receipt.json>)及[check.stdout](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_private_hall_extension_20261106/fixed_evidence/check.stdout>)。此项已不只是raw UNSAT，但`production_accepted=false`；它不排其他插入位置、扩张、31点域或一般minimal-$F$ Hall对象。

另一个明确的lex候选只是构造失败：packet、no$R_7$、全源、private与匹配均通过，却有19条蓝五和6对weak端点。蓝五$(13,14,15,16,17)$与同端$(1,15)$的红六$(1,3,5,10,14,15)$、蓝三$(1,6,15)$已显式保存，见[lex_candidate_result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_private_hall_extension_20261106/lex_candidate_result.json>)，不能把它当作母类反例。

### 3.2 fixed31必要域：外部时限终止，没有solver状态

[COVERAGE.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_physical_cover31_20261106/COVERAGE.md>)与[STATE.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_physical_cover31_20261106/STATE.md>)明确all31 active、动态$F$、每源private、满匹配及有限cut列表；初始cuts为`[]`。这是真实$\tau\ge6$的必要域，未以旧$q^2$核替代物理覆盖。新的bounded validation为`PASS_PHYSICAL_PRIVATE_AND_CUT_EXACT_PROJECTION`，包含655360项private状态及327680项cut状态比较、活动性与格式控制；[encoding_validation.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_physical_cover31_20261106/stage_evidence/encoding_validation.json>)记录实际PASS。新exact-hit auditor也经Linux独立小域验证通过，属于实现证据。

新CNF有307617变量、1370733子句、28264702字节，SHA256为`775ab17715b811f8854d26eb494fb1e9097b9eff52f628a9c16d2c4d16b20e03`。唯一solve片在600.017416秒达到外部时限，exit−15、`termination_reason=SLICE_WALL_DEADLINE`、`reported_statuses=[]`。这是外部TERM中断，**没有solver-reported UNKNOWN，也没有SAT或UNSAT**，见[RESULT.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_physical_cover31_20261106/solve_slice01_evidence/solve_slice01_cuts000/RESULT.json>)。partial proof为333447168字节，留在Linux，SHA256为`76a2517472bef253b8f829f54f2af98901e94dc5ff2a6322a6da0930c4712136`，不是完成的UNSAT证明。

实际SAT-model audit=0，actual checker=0，没有物理$\tau$、26点接口或固定31排除结果。所有自有运行已退出，无自动续跑。本报告四个solve片合计：757 SAT、766内建UNKNOWN、fixed24 checked UNSAT、physical31外部TERM；真实SAT颜色audit一次，proof checker一次。独立枚举/重放、lex分析和auditor bounded validation分别按其原收据保留，不能混作实际模型审计。

## 4. 解析结论及准确范围

| 项目 | 实际依据 | 不推出 |
| --- | --- | --- |
| $q^2$有限核覆盖 | 主会话解析限制到$q$条实际匹配路径的点并；正文命题1 | Hall排除为真；归约本身替代实际求解或模型审计 |
| 共同邻居红高度 | 主会话手核；正文命题2 | 共同交集小即Hall邻居并集亏缺 |
| $q\ge5$右侧共同末点禁形 | 主会话手核；正文定理3，调用旧三链锁$n=q+1$ | 任意满$q$匹配不可能 |
| 外端uncrossing反例 | 旧完整表及主会话参数核对 | full-$q$源目标反例；实际新23点模型另有证据 |
| 附录A直接两边swap | 完整色表、packet、路径及weak解析 | 完整$q$匹配正规化被反驳；普适$\tau\le2$ |
| 附录B蓝连接短红尾源强迫 | 一般$q\ge3,k\ge1$解析证明 | 任意匹配可抽出所需蓝连接红块 |
| 附录C两条分离红尾负对照 | 完整色表及逐型解析 | 可以删去B的全部跨块蓝前提；本构造未Linux验证 |

现用正文为[PROOF.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-clique-source-hall-20261105/PROOF.md>)，解析止损见[APPENDIX.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-clique-source-hall-20261105/APPENDIX.md>)。附录新增构造均没有借用23点模型的Linux核验。原三链、caller及旧反例的来源仍在正文明确链接；旧$b25$、acceptance、sealed运行及task metadata不升级。

## 5. 剩余义务与交接边界

物理$\tau_{R_6}\le5$仍开放；31点、$\tau\ge6$的757临界caller并未被23点、$\tau=3$的例子反驳。附加每源private条件下的满匹配排除仍未证。一般净收益允许同一个$K\subseteq Y\cup I$命中$Y\cup I$全部实际红六且$|K|<|I|$，从而留下$b+|I|-|K|>b$点短帽；不能只命中选出的private见证。取$I'=I\setminus K$、$K'=K\cap Y$，剩余路径避开$I\cap K$，所以$K'$命中$Y\cup I'$全部红六且$|K'|<|I'|$，这与$Y$内横截版本等价，亦允许最后三源的两点hit选入末源$v$。fixed24成功checker和physical31中断均没有提供这一共同横截。

本轮未调用外审。文档身份与链接检查见DOCUMENT_CHECK.json；该检查仅为本地PowerShell/.NET控制操作，不是独立数学核验。后续科学工作继续只在Linux执行，准确新输入与运行绑定分别建立；无盲重试或自动续跑，保留既有授权和全部旧证据。
