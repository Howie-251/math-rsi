"""One bounded documentation update; leaves mathematical source files unchanged."""
from pathlib import Path
import json
import os

ROOT=Path(__file__).resolve().parents[5]
W=Path(__file__).resolve().parent
assert (ROOT/"AGENTS.md").is_file()
current="""**2026-10-20 15:30 UTC 当前恢复：主要八类仍开放，24／25低点范围进一步缩小。** 25恰六名六度点已成完整纸面候选，规范 proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md；独立31416→140完整域、140布局运输及3500行普通ABC全部PASS，128项严格、最大1429/1430，无quota／DP进口。25多低实际仅余r3…5且每边低迹≤2。24新强门 TWENTYFOUR_THREE_LOW_SEVEN.md 与完整 TWENTYFOUR_TWELVE_OR_MORE_SIX.md 已root全文核：δ6仅余r1…11且低迹≤3；三低边禁止七度点，含八度点时另一点至少十一度且须满足同一重复预算的强约束。配对锐门12324已独立10147标号矩阵／43轨全项核同，红／蓝组扣除1595／2035／616已成解析引理。Grok基础三低、Gemini23条件门有效静态意见已读，均未运行程序；Grok摘要S内／外笔误已处置，不扩大其范围。新完整24强链Grok1312及r6 Gemini1311仍在途，不能称新scope双模型通过。完整36未证、已验下界仍34，旧35 Lean暂停，不碰v2。详见当前CHECKPOINT_CURRENT及本轮REVIEW_RECONCILIATION。"""

navs=["AGENTS.md","NEXT_SESSION.md","context/propertyb35-paper/PROGRESS.md",
      "context/propertyb35-paper/BRANCH_COVERAGE.md"]
snapshots={}
for name in navs:
    p=ROOT/name
    text=p.read_text()
    first=text.index("\n\n")+2
    end=text.index("\n\n",first)
    old=text[first:end]
    assert "2026-10-20 14:46" in old,(name,old[:90])
    snapshots[name]=old
    historical=os.path.relpath(W/"CHECKPOINT_1446.md",p.parent)
    text=text[:first]+current+"\n\n[14:46历史检查点]("+historical+")保留上一范围；下方较早快照不覆盖本段。\n\n"+text[end+2:]
    p.write_text(text)
(W/"NAVIGATION_1446_SNAPSHOT.json").write_text(json.dumps(snapshots,ensure_ascii=False,indent=2)+"\n")
cp=ROOT/"context/propertyb35-paper/round01/root/CHECKPOINT_CURRENT.md"
assert not (W/"CHECKPOINT_1446.md").exists()
(W/"CHECKPOINT_1446.md").write_text(cp.read_text())

bc=ROOT/"context/propertyb35-paper/BRANCH_COVERAGE.md"
text=bc.read_text()
text=text.replace(
"|24|6,7|δ6任意四低原边、r≥13新纸面闭合；",
"|24|6,7|δ6任意四低原边、r≥12及三低加七度、8/8、8/9、8/10新纸面闭合；")
text=text.replace(
"|δ6剩r1…12且每边低迹≤3；δ7",
"|δ6剩r1…11且每边低迹≤3；三低边禁止七度，含八度时另一点至少十一且受强重复约束；δ7")
text=text.replace(
"|25|6,7|全七度、恰一／二六度、至少七六度均有完整纸面候选；",
"|25|6,7|全七度、恰一／二六度、至少六六度均有完整纸面候选；")
text=text.replace(
"|仅r=3…6且每边低迹≤2；","|仅r=3…5且每边低迹≤2；")
text=text.replace(
"已替代旧r3…16余域；准确剩余为r3…6且每边低迹≤2。",
"已替代旧r3…16余域；新[恰六低定理](../../proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md)又以实际九单位选点、完整140必要标记及128份普通ABC严格布局闭合r6，独立140运输／3500行复算PASS。准确剩余为r3…5且每边低迹≤2。")
bc.write_text(text)

review=W/"REVIEW_RECONCILIATION.md"
text=review.read_text().replace(
"本次仅记录其独立核仍待完成，不把主实现报告或上述24审阅当作独立验收，也不预记任何新24三低结论。",
"其独立核现已完成：independent_sharp逐格生成10147标号矩阵、465行排序类、完整行列群43轨，以精确块事件容斥逐项复算根并／两core／总数；43行、轨道大小与465运输映射全部相同，最大12324，CPU0.246136。该确定性核不代替实际三低调用证明或更强后续范围的跨审。")
text+="""\n## 15:30 UTC：基础三低与23条件门的两份有效意见\n\nGROK_TWENTYFOUR_THREE_LOW_RESPONSE.json 的嵌套 response.structuredContent.stopReason=end_turn，实际 grok-4.7-build/xhigh，线程 b2d0a223-e533-4c28-a37e-a1ef517fafaa。它静态核 TWENTYFOUR_THREE_LOW_EDGE.md 全文、sharp_gate/REPORT.md 全文和独立稿的对象／失败分解／容斥接口，认可基础criterion、全部7/7与7/8原边、旧必要条件(6)；手核全1矩阵10452+1296+576和同划分10986，未执行程序。\n\n原回应一句“其余重复邻点在S外”把方向写反。这里S=V\\\\G，未指向G固定点或自由匹配点的重复邻点必须在S内。root及本轮逐字核对确认规范正文原本正确；保留原JSON，只纠正这处摘要，不拿错误句作证明。该意见不覆盖新红组扣除、三低加七度的全部d范围、八度强必要条件或r12整支。\n\nGEMINI_TWENTYTHREE_FOUR_LOW_RESPONSE.json 为有效SUCCESS，CLI gemini-4-argon-high/high，effort来源cli_selected_model_variant，线程06d7153b-a9ed-48d0-8a4c-9f86befb060a。它实际静态读取23条件REPORT及独立REPORT，核四形完整、180项容斥公式及3186手算、原边分组与补色连接、47167−572d−2431alpha及130m−52d−221alpha≤470，确认指定三自由中心与G其余点共度一的范围成立；未执行程序。后半“去掉内部共度一”只属建议及瓶颈讨论，未形成完整证明，不能记任意23四低原边已闭或全23可染。\n\n## 新完整范围的当前状态\n\nroot已全文核24红组解析扣除1595／2035／616、TWENTYFOUR_THREE_LOW_SEVEN.md及TWENTYFOUR_TWELVE_OR_MORE_SIX.md。原三低基础审阅不自动覆盖这条新链；Grok新24强链cell1312在途，无有效完成意见前保持在途。\n\nroot已全文核TWENTYFIVE_EXACTLY_SIX_LOW.md及其实际选择接口。r6_nine_unit/independent现有真实PASS：在374目录进口下独立31416→140过滤、全部非零counts逐项相等；140双射／布局运输及3500行35桩普通ABC全项重放，128strict最大1429/1430；含零失败仅024/common-pure与006，CPU0.613576，无DP或quota。该核不重生成374目录，不替代actual选点lemma。Gemini完整r6 cell1311仍在途，不能写新完整scope双模型通过。\n\n准确纸面剩余为25 r3…5低迹≤2、24δ6 r1…11低迹≤3及三低高点强限制；八个主要类仍开，不创建verified claim或宣称完整36。\n"""
review.write_text(text)

accept=W/"ROOT_ACCEPTANCE.md"
text=accept.read_text()
head_end=text.index("\n\n")
text="# 本轮共同结构与实际原H连接：Root核对"+text[head_end:]
first=text.index("\n\n")+2
end=text.index("\n\n",first)
text=text[:first]+"""2026-10-20 15:30 UTC。完整36未证明。root现已全文核25恰六低及24强三低／完整r12实际证明；25余r3…5低迹≤2，24δ6余r1…11低迹≤3。新12324配对门与r6全140普通ABC已完成独立确定性复算；新完整24强链Grok1312、r6 Gemini1311在途。以下各旧节保留原范围和进口，末节给本轮新接受接口。"""+text[end:]
text=text.replace(
"12324锐门主报告已完成但独立核待完成。没有由此接受新24三低结论、全24或完整36。",
"12324锐门已完成独立43轨精确容斥全项核，详见independent_sharp。新24强门与r12另由下节明确核对；没有据局部门接受全24或完整36。")
text+="""\n## 15:30 UTC：新24强链与25恰六低的实际接受范围\n\n24基础三低的15−p自由边、四类固定边数和两方向min已逐项核正。原边索引分别放入红固定、蓝固定、自由组件及纯外四组，各固定色组内部先取并，合法扣红六1595、红七2035、蓝七616，再与其他组取并；没有跨组重复扣交。由此任何三低原边含七度点即染色；含八度点且不可染必须alpha0、p0、s8=0、s_big为2/3、d_big≥9+s_big。\n\nTWENTYFOUR_TWELVE_OR_MORE_SIX.md的r12链保持共同原H：逐低行给q0/3/6与n1=0；高点行3a+2b=12+K及共享N8≤K≥11≤12−2q；q3/q6由度预算排除；q0的A/B/C与inactive行预算迫唯一big。最后A2/B3面迫big度11、a3=8、K=12，任一含八度的big三低边三中心都重复big，强门迫big至少12，矛盾。与四低≥13推论一起，实际至少十二低点全闭。root已全文核，未将新scope预记为跨模型完成。\n\n25 TWENTYFIVE_EXACTLY_SIX_LOW.md使用实际六低纯一／二迹结构，七度点s不得6，冲突图选含s0且避024/common-pure的真实独立三元组。其九锁原迹必在完整140必要标记中；128份明确布局以普通ABC严格，余12中含零仅024/common-pure与006，分别由选点和行预算排除。raw最大1429/1430，证明不需要quota／DP最优性。\n\n新独核r6_nine_unit/independent/REPORT.md、RESULT.json、ROWS.json、TRANSPORT.json已实际PASS，root全文读REPORT和CHECK.py：31416→140覆盖相等，140实际双射和布局、3500普通行及140总分全部一致，CPU0.613576。声明进口为374目录覆盖及一般概率引理；没有重新枚举H，也没有把模型意见替代实际执行。新r6 Gemini1311及24强链Grok1312仍在途。\n"""
accept.write_text(text)

checkpoint="""# 36纸面研究当前检查点

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
- 新24红组＋强三低＋r12整链Grok cell1312仍在途；完整r6 Gemini cell1311仍在途。没有有效返回前不写完成，不称新scope双模型通过。
- r≥7/small的Grok1285、Gemini1286旧有效范围保持，失败旧调用原记录不改。

全部原response及处置见W/REVIEW_RECONCILIATION.md，root实际核对见W/ROOT_ACCEPTANCE.md。本次wiki只增／更partial节点，不创建verified claim或改写已验下界。

## 下一轮边界

不继续重跑已失败八单位旧菜单、21大谱、24旧P7库存，不以条件工具当整类闭合。后续从25 r3…5、24 r1…11及其他六个主要开放类的完整实际对象出发，由root统一选线；本次收卷不开始r11新推导。
"""
cp.write_text(checkpoint)
print("Current navigation, review records, root acceptance and checkpoint updated.")
