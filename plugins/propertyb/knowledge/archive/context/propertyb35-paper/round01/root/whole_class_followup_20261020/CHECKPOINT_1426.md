# 36纸面研究当前检查点

更新：2026-10-20 14:26 UTC。Goal active；完整m(5)≥36未证明，已验收下界仍34，35完整纸面候选的Lean保持paused。不运行Lean、不触碰v2。

## 当前数学范围

主要仍八类：21δ7；22δ6/δ7；23δ6/δ7；24δ6及δ7剩余；25多六度。最新已把25多低类压至 **r=3…6，且每条原边的低迹至多二**，而非旧r3…7或r3…16。没有据此关闭整25或其他点数。

25新完整纸面链（均为25点、35互异五元边、点对覆盖）：
- `proofs/propertyb35/THREE_LOW_EDGE_BALANCED_EXTENSION.md`（M17）：三低同边，余两点D−5(λ−1)≤17可染；最坏184460/184756。
- `TWENTYFIVE_TEN_OR_MORE_SIX.md`（同目录）：六星共享Σt=r迫r≤11，再完整排r10/11。
- `TWENTYFIVE_NINE_OR_MORE_SIX.md`：r9共同高点图，两三叶星，W≤17。
- `TWENTYFIVE_EIGHT_OR_MORE_SIX.md`：r8三种星型，C8/C4和C0的b1/4/7全部排除，实际W/m连接。
- `TWENTYFIVE_SEVEN_OR_MORE_SIX.md`：r7三星型/五库存完整覆盖与实际排除；r≥8引用上一稿。
- `TWENTYFIVE_SMALL_LOW_TRACES.md`：r3…7非B⇒低迹≤2。四低边共同W≤26/m≤3；三低边λxy=1，两高行与纯高边共同扣除给W≤26/m≤5，精细式≤10016<10139。另由r7低迹纯二覆盖奇数七，给r7短替代证明。

root已全文核以上实际H连接，Sol独立核新r7/small，无新程序或大表。最新独核 `W/small_r_shared_gate/ROOT_TRIPLE_CHECK.md`、r7完整解析 `W/r7/REPORT.md`。

## 本轮明确正在做的义务

W=`context/propertyb35-paper/round01/root/whole_class_followup_20261020/`。

- two_six代理：`W/pure_pair_unit8/`，复用完整65族八单位目录，实际r个六度+(8−r)七度及无三低迹的完整小域。r4/5/6可由七度支撑图greedy保证所需4/3/2单位七度；r3需Brooks或额外K5处理。仅先判断真实原始ABC是否strict，不无端扩域。
- low_design代理：`W/r6_pure_pair/`，六低纯1/2迹对应K6低对＋19高的匹配结构；每高F1偶，至少七高对应完美匹配。目标实际共同W/补色门，未证。
- q4代理：`W/twentyfour_six_transfer/FOUR_LOW_REDUCTION.md`，24六度重复邻点形成内部matching，攻原边≥四低且含内部重复对，未证整类。
- root统筹剩余覆盖及实际接口，处理以下有效审阅。旧r3补色事件收费仍超34288，不继续逐条小修。

24新条件门在 `W/twentyfour_six_transfer/REPORT.md`：abc同G且三重复邻点都在G外，2min(du,dv)−5(λuv−1)≤14则B。单弱划分7542/92378；公共重复点原型四点可击中全部五块、根交零，故不能直接复制25正marked扣。当前不是普遍选点结论。

## 核验与审阅

- M17旧marked核：264交矩阵、17304正格四匹配支持；独立字面2239230个六红子集逐K一致，min(J−15Kmax)=324。root `ROOT_SCALAR_CHECK.json` 全264×46464可行调用PASS。旧J/W门为声明进口；无需重复计算。
- M17/TEN/NINE：Grok1275有效end_turn、Gemini1274有效SUCCESS，静态认可声明进口下成立，均未执行程序。Grok一处s3摘要错误已在1280确认纠正，原数学规范正确。
- r8：Grok1280有效end_turn，实际grok-4.7-build/xhigh，root读全回应；Gemini1279 stream idle timeout ERROR，无数学意见。原始 `W/GROK_R8_RESPONSE.json`、`GEMINI_R8_RESPONSE.json` 保留。
- 新r7/small Grok **functions cell1285**，同线程b2d0a223-e533-4c28-a37e-a1ef517fafaa；保存 `W/GROK_R7_SMALL_RESPONSE.json`。
- r8+r7/small Gemini授权fresh retry1 **functions cell1286**，请求gemini-4-argon-high/high；保存 `W/GEMINI_R8_R7_SMALL_RETRY1_RESPONSE.json`。未完整返回不计通过。共同新scope提示 `W/R7_SMALL_REVIEW_PROMPT.md`。
- 本批wiki已用helper追加partial experiment、条件工具集、gap_map/log/index/query_pack；未创建verified claim。记录 `W/WIKI_UPDATE.md`、`W/WIKI_R7_HELPER_RECEIPT.json`、`W/REVIEW_RECONCILIATION.md`。

上个14:07检查点归档 `W/CHECKPOINT_1407.md`。旧完整证据保持原位。最终尚须其他八类闭合、整篇proof-checker、跨家族最终审阅与全文HTML，不能把本批局部认可写成36完成。
