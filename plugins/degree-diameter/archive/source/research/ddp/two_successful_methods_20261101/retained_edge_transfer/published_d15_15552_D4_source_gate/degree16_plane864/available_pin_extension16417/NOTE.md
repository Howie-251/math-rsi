# 当前16416可用pin单点扩张：一次有限覆盖门，UNKNOWN

本批未找到≤16个pin的完整覆盖，也没有证明不存在。实际可行上界仍为29个pin；其度数会使新增点超过cap16，所以没有生成16417图。此case按授权终态停止，不续seed、solver或旧D4验证。

## 先提出并实际检验的问题

[PRED](PRED.md) 的正预测是：当前accepted16416图中，存在≤16个当前degree<16的不同pins，使它们的**当前图闭R3**覆盖所有16416点。该规则可保全部129240旧边，只加新点16416及pin边；不同于已暂停的原15552 full-N克隆packing，也不要求pin是旧864个clone之一。

预测本轮仍UNKNOWN。一次greedy与一次冗余删除给出29点完整覆盖；唯一暖start HiGHS窗口30秒没有改善到≤16。不能把“未找到”写成反驳，也不能把29称最优。

## 完整当前输入与覆盖数据

接受图literal只解析一次，作为新cover问题输入：
`../graph_d16_D4_n16416.edges`，16416点／129240边。

当前可用pins为 **4050**：126个degree14、3924个degree15；其中3186个原15552旧点，864个当前clone。全部允许，目标域也包括全部864个当前clone，没有缩成原15552子图。

每个pin计算一次精确depth3闭球，共4050个局部根。这些是新覆盖问题的支持计算，不是旧sourceD4／全根有效性复验。每球覆盖大小2425…2641，全部可用球的并为16416。

- [ALL_AVAILABLE_PINS.json](ALL_AVAILABLE_PINS.json)：实际pin labels、当前degree/role及完整域。
- [ALL4050_CLOSED_R3_SUPPORTS.bits](ALL4050_CLOSED_R3_SUPPORTS.bits)：4050个实测闭球，每行2052 bytes、little-endian，bit0…16415为真实当前target label。
- [SUPPORT_SCHEMA.json](SUPPORT_SCHEMA.json) 与 [ALL4050_PIN_SUPPORT_PROFILE.tsv](ALL4050_PIN_SUPPORT_PROFILE.tsv)：行映射、大小、byte offset和完整频率。
- [COVER_COLUMN_MAPPING.json](COVER_COLUMN_MAPPING.json)：4050列仅按完全相同coverage压成3798列，保每组全部actualpins，以最小actual label代表；单位cost下重复相同列不会改善覆盖。

## 一次greedy与一次求解

greedy每步取最大未覆盖增益、actualpin字典序tie；先后29点覆盖全图，逆序做一次冗余删除后仍29。首点11502覆盖2641目标；末三步增益11、8、4。该返回是一个具体可行上界，不是对共享覆盖最优值的估计。[GREEDY_RESULT.json](GREEDY_RESULT.json) 保存全部步骤与labels。

随后预先写 [SOLVER_PRED.md](SOLVER_PRED.md)，仅启动一次既有HiGHS minΣpin二元cover模型：3798个等价列、完整16416行、9,779,328个非零、每行coverage≥1、threads1，warm29的每个约束均先核为可行。未固定greedy集合，未排当前clone pins或targets。

实际 `passModel`、`setSolution` 均kOk；配置time_limit30秒。返回 `HighsModelStatus.kTimeLimit`，solver实际CPU30.285677327秒，保留可行29点、node0、dualbound0。没有可用的≤16证据，也没有独立不可行或最优性证明。[RAW_SOLUTION.json](RAW_SOLUTION.json)、[MODEL.json](MODEL.json)、[WARM_START_RETURN.json](WARM_START_RETURN.json) 保留原返回。

返回best的binary及全16416 bitset union实际核对通过。[BEST_COVER_PIN_SET.json](BEST_COVER_PIN_SET.json) 保存29个真实pins，但明确它不是合法cap16单点扩张；没有`PIN_SET.json`、新完整边表或新根全路由产物。

## 成本、数学接口与停止边界

唯一driver838889／child838897，session71061已exit0，HANDLE/TERMINAL均无活跃进程。实际所有child CPU **34.473098**，driver **0.018066489**，准备预留1.0；本新case合计 **35.491164489 / 60 CPU秒**。child hard50，solver配置30，数值单线程；无重启或第二solve。[RESULT](RESULT.json)、[TERMINAL](TERMINAL.json)、[HANDLE](HANDLE.json)、[CHECKPOINT](CHECKPOINT.json) 与stdout/stderr保存实际过程。

本批0新图、参数或Lean计数。current graph parse1、new-question depth3 support roots4050；旧D4/allroot有效性BFS、field、Lean、ARIS均0。没有≤16命中，因此新根route/multisource BFS阶段也为0。现有16416图、旧kernel及专家包未修改。

[AVAILABLE_PIN_EXTENSION_PAPER.md](AVAILABLE_PIN_EXTENSION_PAPER.md) 给出的条件接口仍有效：available且≤16的current closedR3 cover可用SingleExtension真Walk定理得到D≤4，新增点度≤16，旧边全保留；exactD4下界可由16417>Moore16D3=3857给出。不能直接假定任意新pins保留旧nonD3 witness，完整新kernel也尚未形成。本轮没有命中，故没有将这个条件接口记成新构造。

停止本批，不继续同solver/timer或只改善几个末端目标。所有精确支持与完整actual映射已保存，未来新问题可直接复用；未知仍是“同一≤16 pin选择是否能同时完成所有当前覆盖”，不是某个pin单球没计算或遗漏clone。任何续算或改变规则由root按已存数据另作有限决策。
