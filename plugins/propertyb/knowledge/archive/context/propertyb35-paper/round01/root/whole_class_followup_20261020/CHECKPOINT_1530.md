# 36纸面研究当前检查点

更新：2026-10-20 15:30 UTC。Goal active；完整m(5)≥36未证明，已验收下界仍34，旧35 Lean保持paused。不运行Lean、不触碰v2。

## 当前准确剩余

主要仍八类：21δ7；22δ6／δ7；23δ6／δ7；24δ6／δ7剩余；25多六度。

- 25多六度仅余r=3…5，且每条原边低迹≤2。新恰六低已具完整实际纸面证明及全140独立普通ABC核。
- 24δ6仅余r=1…11，且所有原边低迹≤3。三低边不能含七度点；若含八度点，另一点至少十一度，且alpha=0、p=0、s8=0、s_big∈{2,3}、d_big≥9+s_big。
- 23新门仍保留三自由六度中心与G其余点共度全一的选择条件，不关闭23整类。
- 24δ7原全七边一般初态、七高一／二内部其余范围保持原表；没有由本批δ6进展关闭它。

完整表以context/propertyb35-paper/BRANCH_COVERAGE.md为准。旧14:46检查点归档在whole_class_followup_20261020/CHECKPOINT_1446.md；更早snapshot均保留作历史，不覆盖本页。

## 最新规范与真实连接

W=context/propertyb35-paper/round01/root/whole_class_followup_20261020。

25：
- proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md：6一低、15二低、14纯高原边；s=0/2/4/6真实私有分组与共同row预算；选含s0且避024/common-pure的七度独立三元组，配六低成九单位锁。
- 374无色目录×84六低标记完整31416→140；81无色／105彩色轨道，完整重标号运输。128普通ABC严格、最大1429/1430；12失败中含零仅024/common-pure与006，由实际选点和s6行矛盾排除。不用quota／DP最优性。
- W/r6_nine_unit/independent：31416独立过滤、140完整counts、140运输与3500行普通ABC全部PASS，0.613576CPU；374目录及概率引理仍为声明进口。
- r≥7与r3…7低迹≤2的旧规范继续有效，故25现在只余r3…5低迹≤2。

24：
- TWENTYFOUR_FOUR_LOW_EDGE.md：全四低原边可染及r≥13。
- TWENTYFOUR_THREE_LOW_EDGE.md：任意实际p/su/sv/alpha的完整自由组件和固定原边分类；全部7/7、7/8闭合。
- MONOCHROMATIC_FOUR_SET_OVERLAP.md：固定红六／七扣1595／2035，固定蓝七及以上扣616；解析树界／Bonferroni，不枚举原H。
- TWENTYFOUR_THREE_LOW_SEVEN.md：任三低加七度点全部闭合，以及上面八度必要条件。root全文核，actual分组互不重复。
- TWENTYFOUR_TWELVE_OR_MORE_SIX.md：r12每低最多一二低给q0/3/6；共同K/a/b预算和度数盈余排完三个面，末端唯一big11却被三个重复低点迫≥12。与r≥13进口合为r≥12闭合。

规范均位于proofs/propertyb35。root全文核上述新actual连接，完整分支未按局部型数量估完成度。

## 完成的精确局部证据

- 配对锐门W/paired_four_partition/sharp_gate：465行排序终态／43轨主字面计数。
- W/paired_four_partition/independent_sharp：另逐格10147全标号矩阵、完整行列群43轨；精确块事件容斥重算根并、两core、总数，43全项及轨大小、465运输全部一致，最大12324唯一全1；CPU0.246136。不是只核极值。
- W/twentyfour_three_low/UNION_RESULT.json：caller小参数及r12关联算术PASS0.001631；结构覆盖和原染色连接由规范正文证明。
- 23 W/twentythree_low_transfer：四形literal与独立180项容斥8值一致；最紧d6/alpha0为43735<43758，余23。固定二点内部重复可减2431alpha，但未去掉三个自由中心的内部共度一条件。
- 旧marked264矩阵、17304支持和J−15Kmax≥324证据保持冻结，不重算。

## 审阅：严格区分实际范围

- 既有24全四低／r≥13：Grok1301有效end_turn、Gemini1302有效SUCCESS，静态核全文且未执行程序。
- 新GROK_TWENTYFOUR_THREE_LOW_RESPONSE.json有效end_turn，grok-4.7-build/xhigh，仅确认基础三低criterion、7/7、7/8、旧必要条件(6)，12324作局部进口；未执行程序。其“其余重复邻点在S外”摘要反向，正确在S内，规范原本正确。
- GEMINI_TWENTYTHREE_FOUR_LOW_RESPONSE.json有效SUCCESS，CLI gemini-4-argon-high/high；静态确认指定23条件门，未执行程序。后半去internal是未证建议，不记任意23四低闭合。
- 新24完整链Gemini cell1313已有效SUCCESS，CLI gemini-4-argon-high/high，全文静态读取红蓝重叠、基础三低、强三低、r≥12四规范，声明进口下认可；未执行程序，旧四低门与独立12324数值为进口。root已全文读回应，无实质异议。Grok cell1312仍在途。完整r6 Gemini cell1311已有效SUCCESS，CLI gemini-4-argon-high/high，静态认可声明进口下r6全链，未执行程序；原回应当时将独立raw重放记在途，现该核已另PASS，不能改写原JSON或把模型意见当执行证据。新scope不能称双模型通过。
- r≥7/small的Grok1285、Gemini1286旧有效范围保持，失败旧调用原记录不改。

全部原response及处置见W/REVIEW_RECONCILIATION.md，root实际核对见W/ROOT_ACCEPTANCE.md。本次wiki只增／更partial节点，不创建verified claim或改写已验下界。

## 下一轮边界

不继续重跑已失败八单位旧菜单、21大谱、24旧P7库存，不以条件工具当整类闭合。后续从25 r3…5、24 r1…11及其他六个主要开放类的完整实际对象出发，由root统一选线；本次收卷不开始r11新推导。
