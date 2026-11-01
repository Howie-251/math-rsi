# 36纸面研究当前检查点

更新：2026-10-20 12:06 UTC。Goal active，完整 m(5)≥36 尚未证明；已验收下界34，35完整纸面候选的Lean保持暂停。不运行Lean，不碰v2。用户已收到同口径10→8→8的差分表，随后明确肯定条件引理的复用价值并要求沉淀；五项已写入 `research-wiki/PROPERTY_B_CONDITIONAL_TOOLKIT_36.md`，原引理总页、AGENTS和规范wiki实验节点已接入口。工具积累与整类闭合分别报告。

## 八个主要数学缺口

21δ7；22δ6/δ7；23δ6/δ7；24δ6/δ7余下结构；25至少三个六度点。**本轮没有整类减少**。不要把新引理、计算行数或已解决的控制例换算为全题进度。

## 已核的新工具及边界

1. `proofs/propertyb35/TWENTYFIVE_ZERO_PRIVATE_TIGHT_EXCLUSION.md`：同一最优唯一低坏边源、8≤b≤13、u=0、N2=15−b的整片紧边界不可能。root正文及精确小核PASS，独立Sol全文PASS。蓝13的Grok/Gemini有效静态认可；蓝12的Grok也已有效end_turn，Gemini两次ERROR未给数学意见；新8–11尚未跨家族审阅。不能扩成所有u0或所有25点。
2. `proofs/propertyb35/TWENTYFIVE_MACRO_STAR_COLORING.md`：六度z的六块内部重复权Wz≤25，直接给失败概率≤3059/3072<1。全λ≤2且六度数r≥8由共同计数满足门。root全文/代码及实际339840局部样本核PASS。无共度上限的“某低W≤25”仍是待证候选。
3. 三四块划分引理：`root/global_reassessment_20261020/three_partitions_lemma/PROOF.md`。任意N、三份块大小≤4划分、无共同双点单元，二重同块图满足2E≤3N−f3；N20的E≤30可达。root独立推导、Sol完整核稿、root回读。它只控制已选三星之间的重复，未控制其余原边新增共度，尚不能接W门。
4. 新十九命中判据：`root/global_reassessment_20261020/pairing_nineteen/PROOF.md`。匹配命中≥19条，剩16坏事件中有相容对即严格可染；相容是共享匹配分量的相对端点符号一致，不是原边实际交≤1。旧24点20-hit反例实际有19-hit匹配，配一对交概率1/64得到63/64；独立literal核PASS。root全文回读，尚无跨家族本范围审阅。普遍19-hit选择与等号相容仍未证。
5. 新整数图引理：同目录 `INTEGER_EXCESS_MATCHING.md`，24点整数非负权、总权≤74、行权≥5保证完美匹配权≥7；root已回读完整证明。实际十九命中要求W−t≥7，不能只用W≥7。冻结旧H全部182250个最大权匹配均命中≤18，而十九命中匹配W7/t0；精确DP和原边读回已存 `INTEGER_EXCESS_MATCHING_CHECK.py/.json`。最大权优先策略因此停止。`SELECTION_ATTEMPT.md` 的二/三匹配交换只把h18压成t≤5，三交换聚合无新加强；分数共享H只反驳连续预算，并非实际H反例。

以上root路径均在 `context/propertyb35-paper/round01/` 下。共同tight证据及审阅对账在`twentyfive/whole_class_attack_20261020/`。

## 全局路线的实际判断

- 22/23旧moment域不再扩扫：`root/global_reassessment_20261020/SOL_GLOBAL_MOMENT.md`表明已存23点键连更好的单独P界也无法处理，需要真实联合结构。Γ为**交数不等于一**图，不能误写成交一图。
- 单中心246型宏星占用松弛已有W40整数见证，15个固定蓝块对均不严格；停止扩该矩阵域，不是实际H反例。
- 共同W选点候选尚未反驳，也未证明。仿射30线加5边攻击的便宜上界只40/45<78，后续两MILP没有增加证据，已经停止。另一次固定交换立方体骨架：16低边baseW=(24,24,20)，候选26334→13408；唯一补全MILP约5.25CPU秒数值infeasible，无incumbent、无精确不可行证。独立模型核PASS，但不能推广。两次攻击均不继续变异或扩实例。
- 四点下降的跨22–25 L6候选尚未测试/证明；不可把它当现有修复定理。24低边共同修复仍开。
- `root/global_reassessment_20261020/degree_literature/REPORT.md`定位四篇原始来源；25点r>0必有Δ≥8，且全图必有50份重复点对，常见小最大度或全线性定理不直接适用。新文献报告尚待root核对细节。

## 在途与下一步

1. q4代理的二/三交换稿已完成，改攻十九命中等号时的16个坏事件划分；文件 `pairing_nineteen/EQUALITY_COMPATIBILITY.md` 正在写。已口头给Fourier二/四次系数平衡及变支持划分例，root尚未核稿，不假定等号必是固定五个分量。目标结合最优匹配证明存在相容剩余对，不扩原H搜索。
2. Grok线程 `f0335392-19cb-4010-bad2-abaca29dd7fc` 正在讨论宏星W门及共同选低中心义务，functions cell **1225**。提示与原回应自动写`root/global_reassessment_20261020/GROK_MACRO_PROMPT.md`、`GROK_MACRO_DISCUSSION.json`。先收实际返回再续接，不并发同线程，不把等待记成数学成果。
3. Gemini旧线程 `747b3cc4-03b7-4993-8980-3d43b183b227` 的B12首轮和retry1均ERROR，不计审阅。现为新的十九匹配选择义务启动 fresh Gemini4 Argon/high 调用，functions cell **1245**，提示 `pairing_nineteen/GEMINI_SELECTION_PROMPT.md`；返回自动保存 `GEMINI_SELECTION_RESPONSE.json`。与Grok的25点W义务不同，勿重复或重启仍在途调用。
4. two_six代理已完成条件工具文稿和δ8旧审阅状态说明修正，现在研究大量六度点的低点设计完整性／缺陷收费，写 `global_reassessment_20261020/many_low_design/REPORT.md`。不跑MILP或整图枚举、不重复全r的W猜想。
5. 主代理继续核真正能关闭整类的共同结构，不返回21局部谱或25下一张u/b表。先验证新路线的必要选择断言；充分引理本身不等于wholebranch。

旧检查点完整保存在同目录`global_reassessment_20261020/CHECKPOINT_BEFORE_TIGHT_UNIFICATION.md`；其中pending、主要路线为历史，不覆盖本页。不创建、暂停或结束Goal。
