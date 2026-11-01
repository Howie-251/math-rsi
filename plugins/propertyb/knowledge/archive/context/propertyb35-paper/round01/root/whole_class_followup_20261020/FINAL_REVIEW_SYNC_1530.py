"""Reconcile the r6 Gemini response that arrived during the bounded sync."""
from pathlib import Path
import json,os,subprocess,sys

W=Path(__file__).resolve().parent
ROOT=W.parents[4]
ARIS=Path(os.environ["ARIS_REPO"])
helper=ARIS/"tools/research_wiki.py"
response=W/"GEMINI_TWENTYFIVE_R6_RESPONSE.json"
data=json.loads(response.read_text())["response"]["structuredContent"]
assert data["status"]=="SUCCESS" and data["model"]=="gemini-4-argon-high"
source="context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_TWENTYFIVE_R6_RESPONSE.json"

for name in ["AGENTS.md","NEXT_SESSION.md","context/propertyb35-paper/PROGRESS.md",
             "context/propertyb35-paper/BRANCH_COVERAGE.md"]:
    p=ROOT/name;text=p.read_text()
    text=text.replace("新完整24强链Grok1312及r6 Gemini1311仍在途，不能称新scope双模型通过。",
                      "r6 Gemini1311已有效SUCCESS静态认可声明进口下成立，未执行程序；新完整24强链Grok1312仍在途，不能称新scope双模型通过。")
    p.write_text(text)

cp=ROOT/"context/propertyb35-paper/round01/root/CHECKPOINT_CURRENT.md"
text=cp.read_text().replace(
"新24红组＋强三低＋r12整链Grok cell1312仍在途；完整r6 Gemini cell1311仍在途。没有有效返回前不写完成，不称新scope双模型通过。",
"新24红组＋强三低＋r12整链Grok cell1312仍在途。完整r6 Gemini cell1311已有效SUCCESS，CLI gemini-4-argon-high/high，静态认可声明进口下r6全链，未执行程序；原回应当时将独立raw重放记在途，现该核已另PASS，不能改写原JSON或把模型意见当执行证据。新scope不能称双模型通过。")
cp.write_text(text)

review=W/"REVIEW_RECONCILIATION.md"
text=review.read_text().replace(
"Gemini完整r6 cell1311仍在途，不能写新完整scope双模型通过。",
"Gemini完整r6 cell1311现已有效返回，准确范围见下节；不能写新完整scope双模型通过。")
text+="""\n## 收卷过程中返回：Gemini完整r6有效静态意见\n\nGEMINI_TWENTYFIVE_R6_RESPONSE.json 的response.structuredContent.status=SUCCESS，CLI gemini-4-argon-high/high，effort来源cli_selected_model_variant，线程06d7153b-a9ed-48d0-8a4c-9f86befb060a。本轮逐字读取完整有效正文：实际读TWENTYFIVE_EXACTLY_SIX_LOW.md全文、ZERO_SELECTION_LEMMA全文、源REPORT、FINAL_SCOPE_CHECK代码与JSON、域CHECK和FULL_REMAINING代码，以及失败签名的指定段和140证书前120行。\n\n它给SOUND_WITH_DECLARED_IMPORTS，具体核实际六低结构、七度s6行矛盾、含零独立三元组选点的四配置、共同14纯高边60>56、九锁实际迹签名可恢复性、标签运输和无quota普通ABC回原染色；未执行程序。声明进口为small低迹门、374目录完整性、128明确布局的有理数算术。其“独立raw另在途”反映调用时点，不能据此覆盖后来已完成的140独核，也不修改原响应；两项分别记录。\n\n该有效意见只覆盖25恰六度r6，不含r3/4/5、全25或完整36。新24强链Grok1312仍在途；不称新批双模型通过，不创建verified claim。\n"""
review.write_text(text)

accept=W/"ROOT_ACCEPTANCE.md"
text=accept.read_text().replace(
"新完整24强链Grok1312、r6 Gemini1311在途。",
"r6 Gemini1311已有效静态认可声明进口下成立，新完整24强链Grok1312在途。")
text=text.replace(
"新r6 Gemini1311及24强链Grok1312仍在途。",
"新r6 Gemini1311已有效SUCCESS静态认可声明进口下成立，未执行程序；本轮已读完整意见，准确读取及进口见REVIEW_RECONCILIATION。24强链Grok1312仍在途。")
accept.write_text(text)

gap=ROOT/"research-wiki/gap_map.md"
text=gap.read_text().replace(
"完整r6 Gemini1311、新24强链Grok1312在途，不预记完成。",
"完整r6 Gemini1311已有效静态SUCCESS，声明进口下成立且未执行程序；新24强链Grok1312仍在途，不预记完成。")
gap.write_text(text)
toolkit=ROOT/"research-wiki/PROPERTY_B_CONDITIONAL_TOOLKIT_36.md"
text=toolkit.read_text().replace(
"上述新完整actual链已root全文核，新24强链Grok1312与r6 Gemini1311仍在途；",
"上述新完整actual链已root全文核；r6 Gemini1311现已有效SUCCESS静态认可声明进口下成立、未执行程序，新24强链Grok1312仍在途；")
toolkit.write_text(text)

payload=json.loads((W/"WIKI_1530_PAYLOAD.json").read_text())
calls=[]
for args in payload:
    if args[0]=="add_experiment" and args[args.index("--slug")+1] in (
        "propertyb36-twentyfive-exactly-six-low-20261020",
        "propertyb36-seven-and-small-low-traces-20261020"):
        args=args.copy()
        i=args.index("--reasoning")+1
        args[i]=args[i].replace(
            "Gemini完整r6 cell1311仍在途，未预记静态PASS或双模型通过。",
            "Gemini完整r6 cell1311现已有效SUCCESS，CLI gemini-4-argon-high/high，静态全文核r6及选点证明，SOUND_WITH_DECLARED_IMPORTS；未执行程序，374目录及128布局算术作进口。其独立raw在途字样是原调用时点，后来140独核完成另有确定性证据。不称双模型通过。")
        args[i]=args[i].replace(
            "该新scope Gemini1311仍在途，不能借本节点旧r7/small认可外推。",
            "该新r6 scope现获Gemini1311有效静态SUCCESS、声明进口下成立、未执行程序，准确范围另记，不能借本节点旧r7/small认可外推。")
        j=args.index("--provenance")+1
        args[j]+="; "+source
        calls.append(args)
    elif args[0]=="upsert_idea":
        args=args.copy()
        i=args.index("--risks")+1
        args[i]=args[i].replace(
            "25r6独立140raw PASS而Gemini1311在途；",
            "25r6独立140raw PASS且Gemini1311有效SUCCESS静态认可声明进口下成立，未执行程序；")
        calls.append(args)
(W/"WIKI_1530_REVIEW_FINAL_PAYLOAD.json").write_text(json.dumps(calls,ensure_ascii=False,indent=2)+"\n")
screen=subprocess.run([sys.executable,str(ARIS/"tools/capture_filter.py"),"-"],
                      input=json.dumps(calls,ensure_ascii=False),cwd=ROOT,text=True,capture_output=True)
assert screen.returncode==0,screen.stdout
receipt=[]
calls += [["log","research-wiki/","During15:30 sync r6 Gemini1311 returned valid SUCCESS: static SOUND_WITH_DECLARED_IMPORTS, no execution; independent140 raw PASS remains separate evidence. New24 strong Grok1312 pending; no claim promotion."],
          ["rebuild_index","research-wiki/"],["rebuild_query_pack","research-wiki/"]]
for args in calls:
    run=subprocess.run([sys.executable,str(helper),*args],cwd=ROOT,text=True,capture_output=True)
    receipt.append(dict(command=args,returncode=run.returncode,stdout=run.stdout,stderr=run.stderr))
    assert run.returncode==0,run.stderr
(W/"WIKI_1530_REVIEW_FINAL_RECEIPT.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
print("Final r6 review status reconciled, helper calls:",len(receipt))
