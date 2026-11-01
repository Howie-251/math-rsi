# 36纸面研究当前检查点

更新：2026-10-20 14:46 UTC。Goal active；完整m(5)≥36未证明，已验收下界仍34，35完整纸面候选的Lean保持paused。不运行Lean、不触碰v2。

## 当前数学范围

主要仍八类：21δ7；22δ6/δ7；23δ6/δ7；24δ6及δ7剩余；25多六度。最新已把25多低类压至 **r=3…6，且每条原边的低迹至多二**，而非旧r3…7或r3…16。24新全四低原边门已闭合，δ6只剩r1…12且每边低迹≤3。没有据此关闭整24/25。

25新完整纸面链（均为25点、35互异五元边、点对覆盖）：
- `proofs/propertyb35/THREE_LOW_EDGE_BALANCED_EXTENSION.md`（M17）：三低同边，余两点D−5(λ−1)≤17可染；最坏184460/184756。
- `TWENTYFIVE_TEN_OR_MORE_SIX.md`（同目录）：六星共享Σt=r迫r≤11，再完整排r10/11。
- `TWENTYFIVE_NINE_OR_MORE_SIX.md`：r9共同高点图，两三叶星，W≤17。
- `TWENTYFIVE_EIGHT_OR_MORE_SIX.md`：r8三种星型，C8/C4和C0的b1/4/7全部排除，实际W/m连接。
- `TWENTYFIVE_SEVEN_OR_MORE_SIX.md`：r7三星型/五库存完整覆盖与实际排除；r≥8引用上一稿。
- `TWENTYFIVE_SMALL_LOW_TRACES.md`：r3…7非B⇒低迹≤2。四低边共同W≤26/m≤3；三低边λxy=1，两高行与纯高边共同扣除给W≤26/m≤5，精细式≤10016<10139。另由r7低迹纯二覆盖奇数七，给r7短替代证明。

root已全文核以上实际H连接，Sol独立核新r7/small，无新程序或大表。最新独核 `W/small_r_shared_gate/ROOT_TRIPLE_CHECK.md`、r7完整解析 `W/r7/REPORT.md`。

## 本轮最新整体推进与停止点

W=`context/propertyb35-paper/round01/root/whole_class_followup_20261020/`。

**24全四低门**：`proofs/propertyb35/TWENTYFOUR_FOUR_LOW_EDGE.md`自含全部原G内部辐条／低低匹配，固定第五点蓝、选定低点红，19外点9蓝10红，再补三个自由低点。外重复中心7542、固定红／蓝针7722/8490、自由重复对16212。spoke的全部(p,s)≤89767；无spoke匹配0/1/2分别89693/87871/92002，均<N92378。第五点度数从固定费用消去。root已全文核实际边分类、无跨组共同边、所有费用和原染色。非B低迹≤3迫r≤13；r13的26条三低边仅52个高关联，11高点覆盖13低点却需55，故r≤12。Grok1301与Gemini1302均已有效完成本scope静态审阅，root全文核意见无实质问题；未执行程序，未称完整δ6闭合。

- `W/twentyfour_six_transfer/`保存原有三外重复门、两内部pair按度7/8的旧替代稿、固定高点消d全证明及新全四低纯整数回执。新单划分92378样本直接核确认5226/3120/3528/624/264，CPU0.098315；全门只核9个整数分支，无新交矩阵域。
- `W/paired_four_partition/REPORT.md`：两份任意4×4块划分上的联合补色通用失败≤15228，解析commonblock c0/1/2/4分流及924根交；比16212更强但24主规范不需要它，留作通用工具。没有新矩阵核。
- `W/pure_pair_unit8/`：完整4684可行键，r3复用旧DP证书剩33已处理nonstrict+6未处理；r4/5/6旧菜单剩1228/351/20。仅固定菜单不足，不是原H反例或全位置失败。已停止继续扩旧菜单，无整r收益。r3单位选点仅可能3K5+K4例外，尚未处理。
- `W/r6_pure_pair/REPORT.md`：真实低对匹配类三高满类至多2，若2类则其高超额至少2；全部私有点至多2。root全文核数目与row预算。准确共同W=150+D，尚未推出D≤5或精细门，未关闭r6。
- `W/three_low_triangle/AFTER_M17_COMMON_BUDGET.md`：旧补色界削18408，但仍超34288，未闭；不继续逐条小修。

下一轮从新24 r1…12／低迹≤3、25 r3…6／低迹≤2的实际对象出发，优先继续合并；不重跑已失败八单位旧菜单，不恢复21大谱或24旧P7矩表。21–23及24δ7的八类原地图仍有效，不得只汇报25单一路线。

## 核验与审阅

- M17旧marked核：264交矩阵、17304正格四匹配支持；独立字面2239230个六红子集逐K一致，min(J−15Kmax)=324。root `ROOT_SCALAR_CHECK.json` 全264×46464可行调用PASS。旧J/W门为声明进口；无需重复计算。
- M17/TEN/NINE：Grok1275有效end_turn、Gemini1274有效SUCCESS，静态认可声明进口下成立，均未执行程序。Grok一处s3摘要错误已在1280确认纠正，原数学规范正确。
- r8：Grok1280有效end_turn，实际grok-4.7-build/xhigh，root读全回应；Gemini1279 stream idle timeout ERROR，无数学意见。原始 `W/GROK_R8_RESPONSE.json`、`GEMINI_R8_RESPONSE.json` 保留。
- 新r7/small Grok cell1285已有效end_turn，grok-4.7-build/xhigh；`W/GROK_R7_SMALL_RESPONSE.json`。root全文核新scope认可，声明进口下成立，无程序重跑。
- r8+r7/small Gemini授权fresh retry1 cell1286已有效SUCCESS，CLI gemini-4-argon-high/high，线程06d7153b-a9ed-48d0-8a4c-9f86befb060a；`W/GEMINI_R8_R7_SMALL_RETRY1_RESPONSE.json`。root核全文解析意见，未运行程序，旧ERROR保持原记录。
- 本批wiki已用helper追加partial experiment、条件工具集、gap_map/log/index/query_pack；未创建verified claim。记录 `W/WIKI_UPDATE.md`、`W/WIKI_R7_HELPER_RECEIPT.json`、`W/REVIEW_RECONCILIATION.md`。

上个14:07检查点归档 `W/CHECKPOINT_1407.md`。旧完整证据保持原位。最终尚须其他八类闭合、整篇proof-checker、跨家族最终审阅与全文HTML，不能把本批局部认可写成36完成。

## 新24审阅已完成；新增局部门待核边界

- Grok cell1301有效end_turn，实际grok-4.7-build/xhigh，线程b2d0a223-e533-4c28-a37e-a1ef517fafaa；原始 `W/GROK_TWENTYFOUR_FOUR_LOW_RESPONSE.json`。
- Gemini cell1302有效SUCCESS，CLI gemini-4-argon-high/high，线程06d7153b-a9ed-48d0-8a4c-9f86befb060a；原始 `W/GEMINI_TWENTYFOUR_FOUR_LOW_RESPONSE.json`。
- root已全文核两份嵌套response.structuredContent.content，均确认新24全四低原边与r≥13推论，范围一致无实质问题；两者未执行程序、未重跑92378样本。不覆盖新12324锐门、23外重复门、24其余输入或全36。
- 23点指定原G的外重复条件门：四形主字面计数与独立双子集容斥全部一致，独立回执 `W/twentythree_low_transfer/independent/RESULT.json`；实际八蓝十红界47167−572d在d6亦strict（余23），固定二点重复另减2431α。指定三自由中心与G其余点共度一的选边条件仍需保留，不能写23整类闭合。
- `W/paired_four_partition/sharp_gate/REPORT.md`主实现报告12324锐门；独立核尚待完成。本检查点不预记新24三低结论。
- 上批wiki已完成，收卷只最小更新相关24节点、关系与导航；无新verified claim。审阅处置见 `W/REVIEW_RECONCILIATION.md`、`W/ROOT_ACCEPTANCE.md`。
