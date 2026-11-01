# 36纸面研究当前检查点

更新：2026-10-20 16:10 UTC。Goal active；完整m(5)≥36未证明，已验收下界仍34，旧35 Lean暂停。不运行Lean、不触碰v2。

## 当前准确剩余

主要仍八类：21δ7；22δ6／δ7；23δ6／δ7；24δ6／δ7；25多六度。

- 25多六度仅余r3…5，且每条原边低迹≤2；r6完整实际论证及140独立普通ABC核已完成，Grok1318／Gemini1311有效静态认可声明进口下成立。
- 24δ6新r11完整论证已root全文逐节核，准确仅余r1…10，低迹≤3。任意F3禁止七度点；含八度时另一点至少十一度，且alpha0/p0/s8=0/s_big2或3/d_big≥9+s_big。新r11跨审待，不能借r12意见升级。
- 23任意四低原边完整条件论证已root核，独立1293292颜色／732库存／10209键／558144选项全同；尚不保证存在四低边，不关闭23整类。Grok1322／Gemini1323新scope有效正文仍待root处置，不预记认可。
- 24δ7一般actual共同修复仍开。新极小蓝源提供至少三个m≤3的七度中心，不是染色结论。
- 25r5均匀三K5子情形的解析证明、Y内λ5两三锁strict待root核；非均匀Y仍开，二低λ4小门另行执行，不冒充整个r5闭合。

完整表以context/propertyb35-paper/BRANCH_COVERAGE.md为准。15:30／14:46历史检查点分别保留在whole_class_followup_20261020/CHECKPOINT_1530.md、CHECKPOINT_1446.md。

## 本轮数学与证据入口

W=context/propertyb35-paper/round01/root/whole_class_followup_20261020。

24新r11：
- W/twentyfour_r11/REPORT.md：全部十四(q,a)面。通用十一度owned/unowned容量N8(w)≤min(Kw,11−Kw)，十三面由不活跃行共同共度与matched-low补盖排除。
- 唯一(q,a)=(0,1)面：9/9任spoke由实际固定两组扣交严格；A4时十double各恰2seven，迫其他high b≤2；A≤3由3N8≥11(A+B)−64及高盈余迫degree7^3/8^4/9^5/11、N8=5，唯一11全部F3搭8，九度拥有只能落double，最终20>15。
- W/twentyfour_r11/FINAL_CHECK.py、FINAL_RESULT.json实际PASS0.003683CPU；十四面、两个凸性等号、96个9/9参数、最后十一度和九度行均核。没有生成H或新增概率划分表。root已全文核，尚无该新scope跨族意见。

已建立24链：
- proofs/propertyb35/TWENTYFOUR_FOUR_LOW_EDGE.md：所有四低原边与r≥13。
- MONOCHROMATIC_FOUR_SET_OVERLAP.md：红六1595、红七2035、蓝七616解析组内扣交。
- TWENTYFOUR_THREE_LOW_EDGE.md／TWENTYFOUR_THREE_LOW_SEVEN.md：实际组件、固定边分组、锐配对12324、F3+7全域及8强必要条件。
- TWENTYFOUR_TWELVE_OR_MORE_SIX.md：r12 q0/3/6共同重复预算与唯一big末端矛盾。
- paired_four_partition/independent_sharp：独立10147标号矩阵／43轨容斥全项相同，最大12324，CPU0.246136。

25r6：
- proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md：6一低／15二低／14纯高，真实选含s0且避024/commonpure的独立七度三元组，六低配三七成九单位。
- W/r6_nine_unit/independent：31416→140完整过滤与counts、140双射／布局及3500普通ABC全项相同，128strict max1429/1430，CPU0.613576；374目录和P1–P5仍声明进口，不用quota/DP。

23新条件定理：
- W/twentythree_internal_map/ALL_INTERNAL_CANDIDATE.md及independent/REPORT.md；全部14带色单星形、内部重数732必要库存、10209度数键、558144布局选项和末8键原染色连接已root核。最紧43755/43758，余3。
- 老twentythree_low_transfer外重复条件门仍保留原scope，Gemini旧意见不能自动扩大到新任意内部重复入口。

24δ7新源态：proofs/propertyb35/CRITICAL_LOW_EDGE_MINIMAL_BLUE_SOURCE.md，M34/35删低总度边G，同一最小蓝源至少三名七度中心m≤3。旧Gemini讨论两处错误由root规范纠正，新回应核对另记；尚欠同源多中心修复。

25r5条件研究：W/r5_nine_unit/common_weight_lp/UNIFORM_Y_THEOREM.md及LOW_EIGHT_PAIR_RESULT.json；均匀Y与λY5仅分开条件范围，不排非均匀Y。二低小门在two_low_gate/，由root按最终实际覆盖验收。

## 审阅与验收边界

- 24全四低旧Grok1301／Gemini1302有效静态；基础三低旧Grok摘要“S外”已明确应“S内”，规范原文正确。
- 新24完整红组／强三低／r≥12：Grok1312有效end_turn、grok-4.7-build/xhigh；Gemini1313有效SUCCESS、CLI gemini-4-argon-high/high。两份全文静态SOUND_WITH_DECLARED_IMPORTS，均未执行程序，root已全文读；不含新r11或全24。
- 新25恰六低：Grok1318有效end_turn／Gemini1311有效SUCCESS，实际范围及进口同r6；均未运行程序，140独核是另一独立确定性执行证据。root已全文读两份意见，无实质异议。
- 新r11、23任意四低、critical修复源及r5条件支均按各自新scope处理，不借上述旧审阅扩范围。

完整原回应与处置见W/REVIEW_RECONCILIATION.md；root实际核读见W/ROOT_ACCEPTANCE.md。wiki只增／更partial实体，不创建verified claim或更改已验下界。

## 后续边界

由root统一选择完整实际对象入口。当前不扩旧21大谱、24P7逐库存、已有失败布局，不把条件工具当整类完成。八个主要类保持开放；新24 r11仅减少δ6内部的一个完整r面。
