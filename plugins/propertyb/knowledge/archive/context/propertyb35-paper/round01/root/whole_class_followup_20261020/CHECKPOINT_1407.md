# 36纸面研究当前检查点

更新：2026-10-20 14:07 UTC。Goal active；完整m(5)≥36未证明，已验收下界仍34，35完整纸面候选的Lean保持paused。不运行Lean、不触碰v2。

## 最新实际范围

25点／35互异五元边／点对覆盖，至少八名六度点现有完整计算辅助纸面证明。新的优先链为：

1. `proofs/propertyb35/THREE_LOW_EDGE_BALANCED_EXTENSION.md`：三低同边，余两点D−5(λ−1)≤17可染。共同根A把三中心及实际原边的交叠绑定，最坏184460/184756，余296。
2. `proofs/propertyb35/TWENTYFIVE_TEN_OR_MORE_SIX.md`：同一个低点六星恰分全部高点超额，总额r。三低边成本≥4、四低边成本≥5，直接迫nonB的r≤11；r11、r10均由完整少数星型与四低边整除矛盾排除。
3. `proofs/propertyb35/TWENTYFIVE_NINE_OR_MORE_SIX.md`：r9有四低边时用共同高点三元覆盖排除；最后全A型的六条三低边构成真实六边高点图，重顶点迫两棵不交三叶星，最后W≤17接旧宏星门。
4. `proofs/propertyb35/TWENTYFIVE_EIGHT_OR_MORE_SIX.md`：r8三种星型完整分流。C8高度点矛盾、C4宏星精细界；C0的b1缺失二低重复覆盖、b7共同正超额覆盖、b4四边图及W≤17均接到原染色。无新计算。

主要仍八类：21δ7；22δ6/δ7；23δ6/δ7；24δ6及δ7剩余；25多六度。最后一类由r3…16缩为**r3…7**；另M17排除恰三低共边几何。其余点数没有因本次新门自动闭合。

这是新完整纸面子类，root和Sol已核全部实际连接；M17与r≥9已获Gemini有效静态认可，r8的Gemini及新Grok审阅仍在途，不是全36验收。不按r个数估计完成百分比。

## 证据与本轮记录

W=`context/propertyb35-paper/round01/root/whole_class_followup_20261020/`。

- `W/marked_partition/`：复用旧完整264交矩阵域及J，主实现对全部17304正格四匹配作容斥；独立另行生成所有支持、逐2239230个六红子集字面计数，逐项K及max一致，最小J−15Kmax=324。标记格内标签对称覆盖112089个具体四点选择。不是原H枚举。
- `W/ROOT_SCALAR_CHECK.json`：root精确接口核PASS，264矩阵／46464可行Dα调用，最坏184460；r9–25全部局部整数星型核对。
- `W/ROOT_ACCEPTANCE.md`：root实际读取代码、实际H连接及范围。r9最后重t=(4,5)保留，没有使用“无quad⇒t≤4”。
- `W/r13_after_m17/REPORT.md`：r9/10完整解析独审；`many_low/ROOT_COMMON_EXCESS_CHECK.md`：共同预算与r≥11短证。
- `W/WIKI_UPDATE.md`：规范helper新增1 idea、2 partial experiments，更新条件工具集、索引、日志、query_pack；未创建或升级verified claim。

旧r14–16、r≥17逐支稿保留，但后续直接复用新共同预算短证，避免再重复分支。旧完整域、J≥400及宏星W25的核验仍是有效进口，不需重新生成。

## 现在正在做什么

- 本轮三名Sol数学任务均已交付，root已核新M17及r≥8完整实际连接；wiki正在同步r8增量，不为凑并发派重复审阅。
- 下一数学范围是25点r3…7，须复用新M17共同预算；暂不自动扩新表或把r8证明套到r7。21–24八类地图仍保留，不能长期忘记其他点数。
- root处理当前两份在途审阅及范围记录，针对具体异议修改；旧范围审阅不重复。

24δ7的新共同根迁移诊断保存在 `W/twentyfour/AFTER_MARKED_GATE_GLOBAL_CHECK.md`：三子句阻塞核心与根坏事件可能交零，故不能直接套25统一正扣。真正剩余是实际度数预算下的共同核心总费用。没有启动新的19点交矩阵表或随机搜索。

## 审阅状态

- 旧r≥17 Grok cell1261已有效完成，线程b2d0a223-e533-4c28-a37e-a1ef517fafaa，grok-4.7-build/xhigh/end_turn。原始回应在 `root/global_reassessment_20261020/three_low_extension/GROK_R17_PLUS_RESPONSE.json`。静态认可旧实际连接，未重跑程序，不自动覆盖新M17/r≥9。
- 旧Gemini三轮r≥17审阅有效SUCCESS，见同目录 `GEMINI_RECONCILIATION.md`。
- 新M17最初Gemini续接cell1269资格检查EOF，`W/marked_partition/GEMINI_RESPONSE.json`为ERROR，无数学意见。
- 首次fresh重试cell1274已SUCCESS，线程097432f6-5374-4edc-9ad7-525e331ad215，实际CLI gemini-4-argon-high/high。完整静态认可M17/TEN/NINE，数值核和W25为声明进口，未执行程序；root核完整回应，见 `W/GEMINI_R9_RETRY1_RESPONSE.json`、`REVIEW_RECONCILIATION.md`。
- 同一新scope Grok cell1275已有效end_turn，grok-4.7-build/xhigh，认可M17/TEN/NINE声明进口下成立，未执行程序；`W/GROK_R9_RESPONSE.json`。其s3摘要“边t和至多3”错误已与正确原规范区分，正确是三点简单图不能各度3，见处置文件。
- Gemini r8新增单独续审 **functions cell1279**，同上fresh线程；提示 `W/R8_REVIEW_PROMPT.md`，返回后自动保存 `W/GEMINI_R8_RESPONSE.json`。
- Grok r8新增单独续审 **functions cell1280**，线程b2d0a223-e533-4c28-a37e-a1ef517fafaa，另请确认s3摘要修正；返回自动保存 `W/GROK_R8_RESPONSE.json`。未在同一线程并发，只有实际完整返回才登记意见。

上一13:21检查点归档在 `W/CHECKPOINT_BEFORE_MARKED.md`；更早停止路线、历史审阅及完整原始证据保持原位。不重复旧Goal或已停计算。
