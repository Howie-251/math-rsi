"""Use the canonical ARIS writer; no manual graph/Connections changes."""
from pathlib import Path
import json,os,re,subprocess,sys

W=Path(__file__).resolve().parent
ROOT=W.parents[4]
ARIS=Path(os.environ["ARIS_REPO"])
HELPER=ARIS/"tools/research_wiki.py"
FILTER=ARIS/"tools/capture_filter.py"
assert (ROOT/"research-wiki").is_dir()
PREFIX="context/propertyb35-paper/round01/root/whole_class_followup_20261020/"
idea="idea:propertyb36-common-marked-root-excess-20261020"
calls=[]

def experiment(slug,title,metrics,reasoning,provenance,tags,duration="paper proof and bounded exact arithmetic"):
    calls.append(["add_experiment","research-wiki/","--slug",slug,"--title",title,
                  "--idea",idea,"--verdict","partial","--confidence","medium",
                  "--date","2026-10-20","--hardware","local exact integer arithmetic and original-H paper derivation",
                  "--duration",duration,"--metrics",metrics,"--reasoning",reasoning,
                  "--provenance",provenance,"--tags",tags,"--update-on-exist"])

def existing_sections(slug):
    text=(ROOT/"research-wiki/experiments"/(slug+".md")).read_text()
    def section(name):
        return re.search(r"## "+name+r"\n(.*?)(?=\n## |\Z)",text,re.S).group(1).strip()
    return section("Metrics"),section("Reasoning")

paired="propertyb36-paired-four-partition-analytic-gate-20261020"
metrics,reason=existing_sections(paired)
metrics+="\n后继锐门另完整生成465行排序类/43轨，主字面计数与独立逐格10147全标号矩阵+完整行列群+块事件容斥全项一致。43根并/蓝core/红core/总数、43轨大小及465运输逐项一致，最大12324仅全1矩阵取等，分解10452+1296+576；独立CPU0.246136。该独立证据是新锐门全域核，不与较早解析15228四分混淆。"
reason=reason.replace("新12324锐门或23外重复门","当时尚未送审的12324锐门或23外重复门")
reason=reason.replace("原24最小度六的其余输入仍可有一至十二低点且全部低迹<=3",
                      "后继强三低与r12共同预算规范已使原24最小度六的其余输入压至一至十一个低点且全部低迹<=3")
reason+="\n15:30收口：12324已有独立全43容斥与10147标号域PASS；Grok新基础三低回应有效静态认可基础criterion及7/7、7/8，未执行程序。新红组+三低强门+r12整链Grok1312仍在途，不把基础意见外推。完整36未证，节点继续partial，不创建verified claim。"
experiment(paired,"19点配对补色工具：解析15228与完整锐门12324",metrics,reason,
           PREFIX+"paired_four_partition/REPORT.md; "+PREFIX+"paired_four_partition/sharp_gate/REPORT.md; "+
           PREFIX+"paired_four_partition/independent_sharp/REPORT.md; "+PREFIX+"paired_four_partition/independent_sharp/RESULT.json; "+
           "proofs/propertyb35/TWENTYFOUR_FOUR_LOW_EDGE.md; "+PREFIX+"REVIEW_RECONCILIATION.md",
           "property-b,m5-ge36,paired-partitions,exact-IE,actual-caller,provisional",
           "independent full labeled domain and IE CPU0.246136 seconds")

experiment("propertyb36-twentyfour-strong-three-low-r12-20261020",
           "24点强三低补色与至少十二六度点的共同预算闭合",
           "24点至多35简单五边pair-cover。固定颜色组内部union解析扣红六1595、红七2035、蓝七及以上616，原边索引分组互不重复。任三six+7+d原边可染，最坏92328/92378余50；三six+8+8/9/10全strict。非B含8的F3须alpha0,p0,s8=0,sbig2/3,d_big>=9+s。r12逐低行迫qLL0/3/6、n1=0；共同高点行3a+2b=12+K，N8<=K>=11<=12-2q。q3/q6度预算矛盾；q0 A/B/C与inactive共同row预算迫唯一big，末端big11/a3=8/K12使F3的3low全重复big，强门迫big>=12，矛盾。结合四低>=13门，实际>=12six可染，非B仅r1..11/低迹<=3。",
           "root已全文核完整实际H、固定组扣交、q0/3/6穷尽及最后重复预算连接；数值配对进口12324已两方法全43核。UNION小核仅参数/关联算术，不枚举H。Grok基础三低有效静态意见只覆盖旧criterion、7/7、7/8与旧必要条件(6)，不覆盖本新红组/完整r12链；新Grok1312在途。四低>=13先前Grok/Gemini静态意见保持原范围。partial相对完整36，不把新paper theorem升级verified claim或声称全24δ6闭合。",
           "proofs/propertyb35/TWENTYFOUR_THREE_LOW_SEVEN.md; proofs/propertyb35/TWENTYFOUR_TWELVE_OR_MORE_SIX.md; "+
           "proofs/propertyb35/MONOCHROMATIC_FOUR_SET_OVERLAP.md; "+PREFIX+"twentyfour_three_low/UNION_REFINEMENT.md; "+
           PREFIX+"twentyfour_three_low/UNION_RESULT.json; "+PREFIX+"paired_four_partition/independent_sharp/RESULT.json; "+
           PREFIX+"GROK_TWENTYFOUR_THREE_LOW_RESPONSE.json; "+PREFIX+"REVIEW_RECONCILIATION.md",
           "property-b,m5-ge36,twentyfour,shared-budget,r12,strong-three-low,provisional")

experiment("propertyb36-twentyfive-exactly-six-low-20261020",
           "25点恰六名六度：九单位真实选点与完整140普通ABC",
           "实际25/35/pair-cover且恰六six，small低迹门给6一低/15二低/14纯高。高点私有s0/2/4/6，七度点s不得6。实际冲突图选含s0且避024/common-pure的独立三元组，配六low得九单位锁。374目录x84标记31416，低交排29485、负重数排1791，余140/81无色/105彩色轨。128明确普通ABC布局strict max1429/1430；12失败中含零仅024/common-pure及006，由选点及行预算排除。新独立31416→140完整域/全部counts相等，140双射及实际布局运输、3500位置普通ABC和140总分全同，CPU0.613576，无quota/DP。",
           "root已全文核canonical和独立REPORT/CHECK.py，实际选点、原H→全域、具体布局与Bool染色连接成立。独核只进口已有374目录与独立注入计数概率实现，不重生成目录、不代替actual选点证明。Gemini完整r6 cell1311仍在途，未预记静态PASS或双模型通过。后继25多低当前仅r3..5且低迹<=2，主要八类仍开；partial相对完整36，不创建verified claim。",
           "proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md; "+PREFIX+"r6_nine_unit/ALL140_CERTIFICATES.json; "+
           PREFIX+"r6_nine_unit/FINAL_SCOPE_CHECK.json; "+PREFIX+"r6_nine_unit/independent/REPORT.md; "+
           PREFIX+"r6_nine_unit/independent/RESULT.json; "+PREFIX+"r6_nine_unit/independent/ROWS.json; "+
           PREFIX+"r6_nine_unit/independent/TRANSPORT.json; "+PREFIX+"ROOT_ACCEPTANCE.md",
           "property-b,m5-ge36,twentyfive,r6,unit-locks,raw-ABC,independent-replay,provisional",
           "independent 140 labels/3500 ordinary ABC rows CPU0.613576 seconds")

experiment("propertyb36-twentythree-four-low-conditional-20261020",
           "23点指定三自由六度中心：四形完整补色条件门",
           "H23<=35 pair-cover，G含三自由six a,b,c，均与G其余点共度1；剩固定u六度、h度d>=6，可有alpha=lambda_uh-1=0/1/2。单星20关联/18点仅一三重点、两二重点同/相邻/不交块pair共四形。8蓝10红冲突2557/3186/2967/2940，9/9为3186/3996/3708/3672，主字面与独立180项IE全8值同。实际8/10总界47167-572d-2431alpha，最紧d6alpha0为43735<43758余23；一般门130m-52d-221alpha<=470。",
           "Gemini回应GEMINI_TWENTYTHREE_FOUR_LOW_RESPONSE.json有效SUCCESS，CLI gemini-4-argon-high/high，实际静态读主REPORT与独立REPORT，手核最坏3186及实际边分组、补色连接；未执行程序。其后半去掉内部共度1的讨论是建议，未证明任意23四低原边可染，不记全23闭合。partial只记录真实条件门与独立精确计数，保持选边条件。",
           PREFIX+"twentythree_low_transfer/REPORT.md; "+PREFIX+"twentythree_low_transfer/RESULT.json; "+
           PREFIX+"twentythree_low_transfer/independent/RESULT.json; "+PREFIX+"twentythree_low_transfer/COMPARISON.json; "+
           PREFIX+"GEMINI_TWENTYTHREE_FOUR_LOW_RESPONSE.json; "+PREFIX+"REVIEW_RECONCILIATION.md",
           "property-b,m5-ge36,twentythree,conditional,actual-caller,provisional")

slug="propertyb36-seven-and-small-low-traces-20261020"
metrics,reason=existing_sections(slug)
reason=reason.replace("25多六度余r3..6","25多六度在本节点形成时余r3..6")
reason+="\n15:30后继：TWENTYFIVE_EXACTLY_SIX_LOW.md已给r6实际完整纸面证明，140标签独立普通ABC PASS，故当前25仅r3..5/低迹<=2。该新scope Gemini1311仍在途，不能借本节点旧r7/small认可外推。新24强门与r12另设partial节点。"
experiment(slug,"七六度点完整纸面分支与r3至7低迹统一约化",metrics,reason,
           "proofs/propertyb35/TWENTYFIVE_SEVEN_OR_MORE_SIX.md; proofs/propertyb35/TWENTYFIVE_SMALL_LOW_TRACES.md; "+
           "proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md; "+PREFIX+"REVIEW_RECONCILIATION.md",
           "property-b,m5-ge36,r7,small-low-traces,actual-caller,provisional")

for slug in ("propertyb36-twentyfour-strong-three-low-r12-20261020",
             "propertyb36-twentyfive-exactly-six-low-20261020",
             "propertyb36-twentythree-four-low-conditional-20261020"):
    calls.append(["add_edge","research-wiki/","--from","exp:"+slug,"--to",idea,
                  "--type","supports","--evidence",
                  "Partial original-H subbranch/conditional progress with stated imports and explicit independent evidence; new complete cross-family scopes remain pending, not a global Property B claim."])
calls.append(["upsert_idea","research-wiki/","--slug",idea.split(":",1)[1],
              "--title","共同标记根扣交与六星共享高超额预算",
              "--description","25实际已压r3..5/低迹<=2；24共享重复预算闭r>=12，仍余r1..11；完整36八类仍开。",
              "--stage","piloted","--outcome","pending",
              "--thesis",
              "共同marked M17及同一高超额预算接r>=7，small门迫r3..7低迹<=2；r6真实九单位选点和140必要标记普通ABC闭合。24采用19点固定红蓝与三低补色组件；完整配对锐门12324、红蓝组1595/2035/616扣交闭所有F3+7及8/8..10，共同低点重复matching预算进一步闭r12。23仅有指定三自由六度中心共度1条件门。所有方法坚持原H实际对应，不以不同视图独立最坏值代替共同预算。",
              "--risks",
              "已验全局下界34，完整36未证，主要八类仍开。25r6独立140raw PASS而Gemini1311在途；新24强链root全文核而Grok1312在途。旧Grok基础三低意见与Gemini23条件意见不扩大为新整类意见；后者去internal仅建议。既有r>=7跨族有效范围保留。所有新实验partial，不创建verified claim。",
              "--tags","property-b,m5-ge36,common-root,shared-excess,shared-repeat,actual-caller",
              "--target-gaps","G7","--update-on-exist"])

payload=W/"WIKI_1530_PAYLOAD.json"
payload.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+"\n")
screen=subprocess.run([sys.executable,str(FILTER),str(payload)],cwd=ROOT,text=True,capture_output=True)
(W/"WIKI_1530_CAPTURE.json").write_text(json.dumps(
    dict(returncode=screen.returncode,stdout=screen.stdout,stderr=screen.stderr),ensure_ascii=False,indent=2)+"\n")
if screen.returncode:
    raise RuntimeError("Capture filter flagged payload; inspect WIKI_1530_CAPTURE.json before writing")

gap=ROOT/"research-wiki/gap_map.md"
text=gap.read_text()
first=text.index("\n\n")+2
end=text.index("\n\n",first)
text=text[:first]+"""**2026-10-20 15:30 UTC 当前共享预算范围。** 八主要类仍开；25仅余r3…5且低迹≤2，新r6九单位选点及140标记普通ABC已完整纸面连接，独立140运输／3500行PASS。24δ6仅余r1…11、低迹≤3：新红蓝组1595／2035／616扣交闭所有三低加七度及8/8…10，再以共同重复预算闭r12；12324配对门已独立10147标号／43轨全项核同。root全文核新actual链；完整r6 Gemini1311、新24强链Grok1312在途，不预记完成。Grok基础三低与Gemini23条件门已有有效静态意见，未运行程序；后者去internal仍未证。完整36未证，不创建verified claim。详见条件工具集和当前CHECKPOINT_CURRENT；下方较早r范围仅为历史。"""+text[end:]
gap.write_text(text)

toolkit=ROOT/"research-wiki/PROPERTY_B_CONDITIONAL_TOOLKIT_36.md"
text=toolkit.read_text()+"""

### 2026-10-20 15:30：24强三低／r≥12与25恰六低

[24三低强门](../proofs/propertyb35/TWENTYFOUR_THREE_LOW_SEVEN.md)
在同一原边、同一19点9蓝10红空间，将实际固定红／蓝四集边组分别取并：
六红扣1595，七红扣2035，七蓝及更多扣616；这些是组内扣交，不重扣自由组件。
故任三six+7+d原边可染。若非B三低边含8，必须alpha0、p0、s8=0、
s_big为2或3且d_big≥9+s_big，故8/8、8/9、8/10也全闭。
[同色四集重叠规范](../proofs/propertyb35/MONOCHROMATIC_FOUR_SET_OVERLAP.md)
给完整解析树界／Bonferroni证明。

[24至少十二低点规范](../proofs/propertyb35/TWENTYFOUR_TWELVE_OR_MORE_SIX.md)
以同一低点重复matching给r12三面q0/3/6，高点行3a+2b=12+K及共享N8≤K≥11≤12−2q；
q0末端唯一big11却有全部12low重复它，强门迫big≥12，矛盾。
结合旧四低≥13门，24δ6现仅余r1…11、每边低迹≤3。
配对锐门另有[独立10147标号／43轨精确容斥全项核](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/paired_four_partition/independent_sharp/REPORT.md)，
最大12324、CPU0.246136，非只核极值。

[25恰六低规范](../proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md)
用真实含s0七度独立三元组配六低成九单位锁；完整31416→140必要标记，
128份普通ABC严格、最大1429/1430，含零失败仅024/common-pure及006，由实际选择与行预算排除。
[独立核](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r6_nine_unit/independent/REPORT.md)
完成140布局运输及3500普通ABC行，CPU0.613576，无quota／DP；374目录仍为声明进口。
所以25现仅余r3…5且低迹≤2，旧r6必要结构和旧菜单失败保留为历史。

上述新完整actual链已root全文核，新24强链Grok1312与r6 Gemini1311仍在途；
旧基础三低Grok、23条件门Gemini有效意见不外推。
23去掉三个自由中心内部共度一只是建议，未关闭23四低或整类。
本批仍为完整36目标下的partial记录，不创建verified claim，主要八类未消失。
"""
toolkit.write_text(text)

receipt=[]
for args in calls:
    run=subprocess.run([sys.executable,str(HELPER),*args],cwd=ROOT,text=True,capture_output=True)
    receipt.append(dict(command=args,returncode=run.returncode,stdout=run.stdout,stderr=run.stderr))
    (W/"WIKI_1530_HELPER_RECEIPT.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
    if run.returncode:
        raise RuntimeError(run.stderr)
for args in (["log","research-wiki/","15:30 recovery sync: 25 r6 complete paper caller and independent140 raw PASS; 24 strong F3 and r12 complete paper chain, paired43 independent IE PASS; new cross-family1311/1312 pending. Partial nodes only, no claim promotion."],
             ["rebuild_index","research-wiki/"],["rebuild_query_pack","research-wiki/"]):
    run=subprocess.run([sys.executable,str(HELPER),*args],cwd=ROOT,text=True,capture_output=True)
    receipt.append(dict(command=args,returncode=run.returncode,stdout=run.stdout,stderr=run.stderr))
    (W/"WIKI_1530_HELPER_RECEIPT.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
    assert run.returncode==0,run.stderr
print("Canonical helper wiki sync PASS:",len(receipt),"calls; partial experiments only.")
