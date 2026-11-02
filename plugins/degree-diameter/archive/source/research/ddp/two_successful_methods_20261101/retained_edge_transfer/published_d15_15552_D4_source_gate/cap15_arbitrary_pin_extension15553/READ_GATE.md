# cap15 / actual15552 任意余度 pin 单点扩张：继承旧 OPEN，非新求解入口

状态：**同一 unrestricted pin-cover scope 已实际尝试且仍 UNKNOWN；未发现严格全域 NO。此门只定位旧账与缓存，停止，不换 timer。**

## 实际源及两种不同障碍

源是已支撑 accepted16416 的同一 actual15552/116316：degree14 有648点、degree15 有14904点，D≤4继承 published/已闭 source proof。本次不读取 source 邻接或重验 source/field/kernel/BFS。

旧 `research/ddp/more_graphs_20261027/d15_D4_current15552/SOURCE_PROFILE.json` 给出 **minSatN=12**：每个旧中心的完整邻域至少含12个原degree15点。cap15 已无可用 slot，所以任意 frozen-old-N clone 都不合法。这是 full-neighborhood clone 的严格障碍。

但只添加一点 z、令其邻域为任意 `S⊆F14, |S|≤15`，不要求 S 等于某个旧邻域，则不存在上述 saturated-pin 问题。保持全部旧边时

`d_new(z,t)=1+d_G(S,t)`。

因此该单点规则全局 D≤4 当且仅当 `⋃_(s∈S)closedR3_G(s)=V(G)`。这已经是旧 actual-source 的完整同一问题，不能把 fullN-clone NO 外推成此 cover NO。

## 已有 free14 分布及完整缓存

旧 profile/报告直接保存：648 free 点，各1余度；24个连续81-label bins 各27 free，另168 bins无free。这里使用标签分布事实，不复用早期错误的 ordinary-equitable 假设。后续 completed-relation affine 恢复与当前 source proof 另有已接受记录，本次不重判。

`support_structure/RESULT.json` 与 `FREE_COMPONENTS.json` 还保存 free 诱导图恰为216个不交 C3。它只限制 free 内一步支配，**不能推出 R3 cover 至少216 pins**；R3路线可以穿过非free点。

同一旧目录 `research/ddp/more_graphs_20261027/d15_D4_current15552/single_vertex_R3_cover/` 已有：

- `PREPARATION_RESULT.json`：648/648 closedR3 全部完成，各球2310点；所有 free 球并集覆盖15552/15552，missing=0；每target支持67..185个pins，nnz=1496880。
- `R3_MASKS.bin`：little-endian uint32头 `[648,15552,243]`，随后每候选一个uint32旧label及243个uint64球mask。
- `COVER_CSC.bin`：uint32头 `[15552,648,1496880]`，649个int32列指针及nnz个int32 target-row IDs。
- `support_structure/RESULT.json`：全部15552 target support rows两两不同，无重复行可删；旧程序只查 equality，明确没有查 support containment。

本次没有读这些球/系数的二进制内容或重建任何球。全free union满只通过必要条件，不是15个球能cover的证据。

## 必须继承的实际终态

1. `single_vertex_R3_cover/RESULT.json`：648 binary、15552完整coverage行及sum≤15，唯一MILP到时无incumbent，`SINGLE_MILP_UNKNOWN_NO_INCUMBENT`。实际solver22.983918811 CPU、旧整批23.953803925；旧requested5CPU未守住且已明确记录，不能写成预算内成功。未导出15553图。
2. `research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/full_inversion_port_cover/RESULT.json`：inversion-invariant子域为raw UNSAT，未独立检查prooflog，只是该限制域的旧数值结果。
3. 相邻的 `full_independent_port_cover/RESULT.json` 与 `REPORT.md`：已有648个分别可选的pin selectors、15552完整不同support行、sum≤15、38132clauses。借源inversion作lex WLOG，另以旧invariant rawUNSAT为依赖跳过该已测子域；唯一60秒CaDiCaL返回 UNKNOWN/code0，solver59.902467 CPU、无pins。这里“independent selectors”不表示要求选出的pins在图中独立。

所以 unrestricted append 仍 OPEN/UNKNOWN，不能把旧raw子域UNSAT与asymmetricUNKNOWN合成全NO，也不能把它重新登记为从未尝试的新接口。旧canonical方向、affine-line充分证书等更小域的失败不改变这个边界。

## 唯一可推翻的后续数据问题（未授权、未执行）

若 root 选择先找真正缩模证据，而非续旧solver，最小的新问题是：

**是否存在实际最小支持行 u（|S_u|=67）及另一较大支持行 v，使 `S_u ⊊ S_v`？**

这里 `S_t={eligible pin indices covering old target t}`。这是具体的、可被完整保存系数反驳的预测，不是已经确认的事实。若支持，u的coverage clause蕴含v，v可无损删除；若没有，只关闭这个“67-support strict-containment”数据门，不排任意15-pin cover，也不自动换到下一支持大小或新timer。

最小数据只有旧 `COVER_CSC.bin` 及 `PREPARATION_RESULT.json` 的candidate mapping/target_support，或等价旧R3 masks；不需要 source、旧D4 BFS、field、affine全handoff、新球、solver或新图。已有 exact-equality 失败不能代替 containment 查询。本次没有执行该查询；它若只删很少行，也不构成新求解窗口的自动理由。

本门读取标准库进程CPU合计0.004796212秒；连路径定位/准备保守charge0.30/1.5秒。新增source parse、球/系数数值处理、solver、BFS、图、参数、Lean均为0。完成即停。
