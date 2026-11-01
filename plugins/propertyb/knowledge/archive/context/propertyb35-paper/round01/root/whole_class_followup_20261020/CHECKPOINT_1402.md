# 36纸面研究当前检查点

更新：2026-10-20 14:02 UTC。Goal active；完整m(5)≥36未证明，已验收下界仍34，35完整纸面候选的Lean保持paused。不运行Lean、不触碰v2。

## 最新实际范围

25点／35互异五元边／点对覆盖，至少九名六度点现有完整计算辅助纸面证明。新的优先链为：

1. `proofs/propertyb35/THREE_LOW_EDGE_BALANCED_EXTENSION.md`：三低同边，余两点D−5(λ−1)≤17可染。共同根A把三中心及实际原边的交叠绑定，最坏184460/184756，余296。
2. `proofs/propertyb35/TWENTYFIVE_TEN_OR_MORE_SIX.md`：同一个低点六星恰分全部高点超额，总额r。三低边成本≥4、四低边成本≥5，直接迫nonB的r≤11；r11、r10均由完整少数星型与四低边整除矛盾排除。
3. `proofs/propertyb35/TWENTYFIVE_NINE_OR_MORE_SIX.md`：r9有四低边时用共同高点三元覆盖排除；最后全A型的六条三低边构成真实六边高点图，重顶点迫两棵不交三叶星，最后W≤17接旧宏星门。

主要仍八类：21δ7；22δ6/δ7；23δ6/δ7；24δ6及δ7剩余；25多六度。最后一类由r3…16缩为**r3…8**；另M17排除恰三低共边几何。其余点数没有因本次新门自动闭合。

这是新完整纸面子类，root和Sol已核全部实际连接；新范围的Grok/Gemini审阅仍在途，不是全36验收。不按r个数估计完成百分比。

## 证据与本轮记录

W=`context/propertyb35-paper/round01/root/whole_class_followup_20261020/`。

- `W/marked_partition/`：复用旧完整264交矩阵域及J，主实现对全部17304正格四匹配作容斥；独立另行生成所有支持、逐2239230个六红子集字面计数，逐项K及max一致，最小J−15Kmax=324。标记格内标签对称覆盖112089个具体四点选择。不是原H枚举。
- `W/ROOT_SCALAR_CHECK.json`：root精确接口核PASS，264矩阵／46464可行Dα调用，最坏184460；r9–25全部局部整数星型核对。
- `W/ROOT_ACCEPTANCE.md`：root实际读取代码、实际H连接及范围。r9最后重t=(4,5)保留，没有使用“无quad⇒t≤4”。
- `W/r13_after_m17/REPORT.md`：r9/10完整解析独审；`many_low/ROOT_COMMON_EXCESS_CHECK.md`：共同预算与r≥11短证。
- `W/WIKI_UPDATE.md`：规范helper新增1 idea、2 partial experiments，更新条件工具集、索引、日志、query_pack；未创建或升级verified claim。

旧r14–16、r≥17逐支稿保留，但后续直接复用新共同预算短证，避免再重复分支。旧完整域、J≥400及宏星W25的核验仍是有效进口，不需重新生成。

## 现在正在做什么

- q4 Sol：r8有四低边的C8/C4子支短证已交付 `W/r8_quad/REPORT.md`。C8由唯一高度点实际剩余边数矛盾；C4用同一高点限制纯高且避它的(3,2)坏边数，接宏星精细界。待root核全文，不提前写整r8完成。
- two_six Sol：r8无四低边的b=1/4/7必要分流；b7/b4有root短论证待独审，最后b1也找到共同高点的剩余两低点重复覆盖矛盾，正在成稿。没有开大域或继续r7。
- lit Sol：新r≥9规范稿已交付，可空闲，不为凑并发派重复审核。
- root：核新稿/跨模型意见、维护完整分支范围；关注能消去整条实际分支的共同约束。

24δ7的新共同根迁移诊断保存在 `W/twentyfour/AFTER_MARKED_GATE_GLOBAL_CHECK.md`：三子句阻塞核心与根坏事件可能交零，故不能直接套25统一正扣。真正剩余是实际度数预算下的共同核心总费用。没有启动新的19点交矩阵表或随机搜索。

## 审阅状态

- 旧r≥17 Grok cell1261已有效完成，线程b2d0a223-e533-4c28-a37e-a1ef517fafaa，grok-4.7-build/xhigh/end_turn。原始回应在 `root/global_reassessment_20261020/three_low_extension/GROK_R17_PLUS_RESPONSE.json`。静态认可旧实际连接，未重跑程序，不自动覆盖新M17/r≥9。
- 旧Gemini三轮r≥17审阅有效SUCCESS，见同目录 `GEMINI_RECONCILIATION.md`。
- 新M17最初Gemini续接cell1269资格检查EOF，`W/marked_partition/GEMINI_RESPONSE.json`为ERROR，无数学意见。
- 按用户授权，首次fresh重试 **functions cell1274**，请求gemini-4-argon-high/high，新scope为M17/TEN/NINE；返回后自动保存 `W/GEMINI_R9_RETRY1_RESPONSE.json`。
- 同一新scope Grok续接 **functions cell1275**，自动保存 `W/GROK_R9_RESPONSE.json`。两者共用 `W/NEW_R9_REVIEW_PROMPT.md`。只有实际完整返回才登记意见；新稿终审在途。

上一13:21检查点归档在 `W/CHECKPOINT_BEFORE_MARKED.md`；更早停止路线、历史审阅及完整原始证据保持原位。不重复旧Goal或已停计算。
