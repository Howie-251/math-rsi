**实质结论：在本次明确约定的复用输入下，C7 整行推理及证据绑定成立；未发现确认的阻断问题。** 本报告不构成人工正式验收。C7 应继续保持未发布状态，当前已接受的限定域上限仍为 29；28 是等待人工接受的候选上限。

审查对象为 [row_certificate.pending.json](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/row_certificate.pending.json>)，本次读取文件的 SHA-256 为：

`ea26adb07a4e17ca87bb6600a19c4fdb704911aacd773c8b38cca4a29dc78ee2`

**1. 数学推理与范围**

[数学定义及定理](</D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md:43>)明确量化于所有有限阶的完整有序 rank-3 signotope 着色，要求禁止蓝色 5 路径、红色 6 路径，且没有 weak 7-gon。颜色极性也明确：真 triple 为红色；历史 clause-group 名称不能替代 literal 语义。

端点单射论证成立。对 \(u<v\)，\(\sigma(u,v)\) 属于 \(D(v)\)。对每个 \(t<u\)，三元组 \((t,u,v)\) 必在一种颜色上延长终止于 \((t,u)\) 的路径，因此 \(\sigma(t,u)\) 至少有一坐标严格小于 \(\sigma(u,v)\)，不能支配后者。这使 \(\sigma(u,v)\notin D(u)\)，故 \(D(u)\ne D(v)\)。\(u=1\) 时前驱集合为空，论证同样成立。路径界把所有状态限制在 \(3\times4\) 盒中。35 个状态中，例外状态恰为 \(h_1=4,\ h_3\ge1\)，共有 10 个，其余 25 个普通状态。因此

\[
N=|\operatorname{Occ}(X)|=25+e(X)-m(X).
\]

该结论并不依赖某个固定阶数，也不把 SAT 辅助变量计数当作数学事实。证据位置：[端点单射与计数恒等式](</D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md:93>)。

C7 的反证归纳没有缺失分支：若 \(e\ge7,\ m\le6\)，已接受的 C6 给出 \(m\ge6\)，故 \(m=6\)。由计数恒等式，\(N=19+e\)。因为 \(7\le e\le10\)，反例只能且恰好落入四个精确 cell：

| Cell | \(r\) | \(e\) | \(m\) | 普通占据数 | \(N\) |
|---|---:|---:|---:|---:|---:|
| A[7,7] | 7 | 7 | 6 | 19 | 26 |
| A[7,8] | 7 | 8 | 6 | 19 | 27 |
| A[7,9] | 7 | 9 | 6 | 19 | 28 |
| A[7,10] | 7 | 10 | 6 | 19 | 29 |

复用四个已检查 UNSAT 输入即可排除全部反例，推出 \(C_7:e(X)\ge7\Rightarrow m(X)\ge7\)。这与[候选证书的 induction 字段](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/row_certificate.pending.json:8>)一致。

数值结论也正确：\(e=0\) 时 \(N\le25\)；\(1\le e\le6\) 时使用相应已接受层得到 \(m\ge e\)，故 \(N\le25\)；\(7\le e\le10\) 时 C7 给出 \(N\le25+10-7=28\)。这是上述模型域内的上界，不推出全局几何 Erdős–Szekeres 上界、完整充电不等式 \(m\ge e\)，也不推出 \(N\le25\)。

**2. 历史编码与语义映射**

本次证据对应历史 `legacy_exact_with_state_path_bridges_v1`，不是当前 F3-main 默认配置。历史 profile 的保留符合[编码契约](</D:/科研/math agent/erdos-szekeres-sat-main/.trellis/spec/backend/semantic-encoding-equivalence.md>)；不能把当前 builder 或新的 pruning 自动移植到旧证明。

我检查了封存源码中的关键映射：

- [严格基底选择](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261009_c7_bridges_v1/runtime/state_charging/cardinality_layers.py:573>)调用 `etv_signotope(7,5,6,order)`，metadata 明确 `strict_no_target`、`signotope=true`、`symmetry_breaking=false`。
- [精确终止路径递推](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261009_c7_bridges_v1/runtime/lib/downset_state_cnf.py:284>)使用完整双向 AND/OR 定义；[cell、state 和 occupancy](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261009_c7_bridges_v1/runtime/lib/downset_state_cnf.py:438>)保持精确定义，没有用单向外端点 witness 代替精确计数。
- [四个 at-most 组件](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261009_c7_bridges_v1/runtime/state_charging/cardinality_layers.py:712>)分别约束 \(e\le e_0,\ e\ge e_0,\ m\le6,\ m\ge6\)。e=10 的边界由明确的空约束与零界单元子句处理，未丢失等式的一侧。
- [bridges](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261009_c7_bridges_v1/runtime/state_charging/cardinality_layers.py:855>)由同一前驱 \(w<u\) 的 cell witness 导出：\((w,u,v)\) 的颜色必延长其中一条终止路径。达到蓝5或红6的项因路径界不可能而省略。这是语义蕴含，且不依赖某个 cell 已经 UNSAT。
- 基底的同外端点路径单调性需要 rank-3 signotope 的删除论证；该前提在[数学稿的 path-deletion 子引理](</D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md:183>)中明确。四点 packet 上同色首尾三元组强制中间两项同色，支持保持外端点的路径缩短；这里没有将该性质错误扩展到任意二着色。

因此，在继承已接受的严格基底／精确计数语义契约及历史重建记录的条件下，四个封存 CNF 对应所需数学反例类；本次没有发现额外而未声明的收缩假设。

**3. 四个 case 的身份与完成回执**

原始 source seal、四份 `formula_replay.json`、parallel4 seal、四份最终 `status.json`、`checker.exit.json`、前后 proof-binding 和候选证书之间的 cell、CNF、proof 标识逐项一致；每个 \(e=7,8,9,10\) 都恰有一个 intended case。四份历史 replay 均记录 `matched=true`，完整 metadata 也与两份 seal 一致。

| \(e\) | CNF SHA-256 前缀 | Proof SHA-256 前缀 | 完成回执 |
|---:|---|---|---|
| 7 | `0085db8421a6` | `5c5b623a2be9` | VERIFIED_UNSAT |
| 8 | `bfac274a30cb` | `25263633feff` | VERIFIED_UNSAT |
| 9 | `882bd7f01ec9` | `52cfc574cede4` | VERIFIED_UNSAT |
| 10 | `b3c6182183b6` | `37b15b9dcc25` | VERIFIED_UNSAT |

完整身份保存在候选证书 `inputs.cases[]`。四份 status 都记录同一个 checker digest：

`ed07375252b2ef179a10dd4c632593c5e588b87e4ae99cdbf0b87be8cd9eea14`

四个退出码均为 0、`timed_out=false`。我还核对了四份完整 checker 日志的文件大小与 SHA-256 均匹配原始回执，并读取其尾部；四者均以 `s VERIFIED` 结束，补充的 8192-byte 摘录与原始日志尾部字节相同。这里仅检查记录及日志，没有执行 checker。

早期 [source execution_terminal](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261009_c7_bridges_v1/execution_terminal.json:32>)保留 `CANCELLED`／`CANCELLED_WITHOUT_RECEIPT`；这些是早期控制流程的终止记录，不能作为完成检查结果。后续 [parallel4 execution_terminal](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261014_c7_parallel4_checker_v1/execution_terminal.json:3>)明确绑定四份成功 status。候选使用后者，没有把原始停止状态篡改成成功，也没有只凭 solver 的退出码授予证明资格。

**4. C1–C6 依赖与发布状态**

C1–C5 原始验收回执分别接受 10、9、8、7、6 个 cell，限定域上限依次为 34、33、32、31、30。其依赖引用与候选 `inputs.accepted_predecessors` 的路径、digest 和大小一致。C5 通过已接受 C4 传递包含 C3，缺少单独顶层 `c3_acceptance` 字段不是依赖缺口。各旧 `resolved_final` 保留 pending flags，而独立 acceptance receipt 负责授予结论；两者角色没有冲突。

C6 的 [acceptance receipt](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261016_c6_acceptance_v1/campaign_acceptance_audit.json:2>)与[明确人工授权](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/res/state_charging/20261016_c6_acceptance_v1/human_acceptance_20261016_v1/human_authorization.json:4>)接受的是同一模型域内的 C6 和上限 29，保留 provisional，fresh checker replay 为 0、复用五个 case。其 bridges e6 与 compact e7–10 的 source seal 身份对应历史 C7 `pending_c6` 指向的来源。因此候选 `inputs.c6_pending_sources_resolved=true` 有依据；无需改写历史 seal 内的 pending 字段。

候选目前诚实保留：

- `c7_proved=false`、`theorem_credit=false`、`certified_upper_bound=null`；
- `candidate_scoped_upper_bound=28`、`previous_accepted_scoped_upper_bound=29`；
- fresh checker／formula replay 均为 0，复用 case 数为 4；
- `review_route.assurance="same-family/provisional"`，且明确要求独立 row review 后另行人工接受。

这些字段位于[候选状态及范围](</D:/科研/math agent/erdos-szekeres-sat-main/tmp/c7_row_primary_20261020/row_certificate.pending.json:508>)。正面的实质审查不能自动将它们改成正式接受。

**5. 限制、修复要求与 reviewer provenance**

确认的阻断问题：**无**。为支持本次限定结论所必需的修复：**无**。正式发布仍需要单独的明确人工接受事件，这是既定发布条件，不是要求重新检查各 case。

本次实际边界与非阻断限制如下：

- 我仅作本地只读数学、源码及证据记录检查。对候选列出的 small artifacts 与历史 runtime 共 60 个绑定条目核对了本地大小、SHA-256 和 manifest 映射，全部吻合；另核对了四份完整 checker 日志的文件绑定。
- 未运行 solver、checker、项目测试或 formula replay；未读取、复制、hash 任何 CNF／DRAT 证明正文；未检查 C8、C9、C10 工作。四个 C7 case 的成功检查和已接受 C1–C6 是按用户要求复用的前提。
- source seal 记录了 164 个 Linux 外部 runtime dependency 的哈希；这些外部依赖文件未在本地 manifest 中导出。本次没有独立重验 Python、PySAT/native binary 或 checker 可执行文件，也没有重建整个 Linux 执行环境。依赖其历史封存与 replay 记录，不能把此次工作描述为新的端到端可重现性验收。
- 我读取了 C6 acceptance receipt 中的 provenance／限制字段，但未读取此前 C6 reviewer 的报告、response 或辩护文本，也未使用其他作者进度总结作结论依据。
- 本次是用户明确覆盖 Claude 路由后启动的 fresh GPT reviewer。未调用 Claude、未委派其他 reviewer。保障等级为 **same-family/provisional**；确切运行模型、提供方 backend 与实际 effort 没有可独立验证的 attestation，记为 **unknown／unverifiable**，不能宣称跨模型家族独立性。

**最终实质判定：SUPPORTED_UNDER_STATED_REUSE_ASSUMPTIONS。保障判定：SAME_FAMILY_PROVISIONAL。人工正式验收状态：仍待明确接受。**