"""Render the current accepted families; keep earlier recovery snapshots as history."""
from pathlib import Path
from datetime import datetime,timezone
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
WORK=Path(__file__).resolve().parent
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
data=json.loads((WORK/'delivery/families.json').read_text())
assert data['distinct_explicit_examples']==103 and data['parameter_cells']==3
probe='research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/'
rows=[]
for key,f in sorted(data['families'].items(),key=lambda x:int(x[0])):
    ns=f['example_orders'];baseline=f['base']['n']
    rows.append(f'<tr><td>({key},5)</td><td>{baseline}</td><td><strong>{f["strongest_n"]}（+{f["strongest_n"]-baseline}）</strong></td><td>{min(ns)}–{max(ns)}，{len(ns)}例</td></tr>')
table=''.join(rows)
page=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第三参数：N(13,5)≥51457</title><style>body{{max-width:1040px;margin:32px auto;padding:0 22px;font:17px/1.8 system-ui;color:#182839}}h1{{font-size:29px}}h2{{font-size:23px}}.result{{background:#e9f5ed;border-left:4px solid #23834c;padding:18px}}.note{{background:#edf3fa;padding:16px}}table{{width:100%;border-collapse:collapse}}td,th{{text-align:left;padding:10px;border-bottom:1px solid #ccd6df}}a{{color:#145f9c}}pre{{white-space:pre-wrap;background:#f4f6f8;padding:15px}}</style></head><body>
<h1>第三参数已取得：N(13,5)≥51457</h1><p>更新：{NOW}。同一Goal ACTIVE；公开表所有未close格子均可选，原27格保留为起始池。旧N(8,2)/n61/SAT/谱继续暂停。</p>
<div class="result"><strong>本批新增40个（13，5）完整阶数例子。</strong>目前共103例、3个参数；最强51457点图有324863条边，最大度13、直径恰5。这里统计的是不同阶数图，不是103种独立方法。</div>
<table><tr><th>参数</th><th>公开下界快照</th><th>本轮最强</th><th>完整阶数例子</th></tr>{table}</table>
<h2>此前不知道什么，这次怎样预测和检验</h2>
<p>完整几何邻域在（13，5）都被满度点挡住，并不说明原图不能扩张。我们扫描已有顶点的完整邻域：源（13，5）有91个原型仅含1个满度邻居，而（14，5）最少有9个。这提示先保留一个几乎完整的旧邻域，删掉唯一接不了的点，再寻找能接替其私有路线的连接点。</p>
<p><strong>预测得到完整图支持：</strong>第38项原型51013，删去满度邻居11352，保留9个可接点；原来缺3535个核心点和79个先前扩张点。补入50577后，全部3614个遗漏被覆盖，得到51418点完整图，新顶点度10。此前37项只排除了其记录基图上至多两个补点的规则，较大连接预算仍未排除。</p>
<p>随后仅继续原53个未试项，每项一次，得到另外39图到51457；累计续算3.209CPU秒，生产总12.853CPU秒。全91项终态为40成功、13当时度数阻断、38限定补点范围失败，0未试。没有刷新之前失败项，也不声称最终51457已不可扩张。</p>
<h2>为何这次补点能替代缺失路线</h2>
<p>满度点11352与可接点50577共享全部10个核心邻居；前者另连3个外围点，后者另连51275，因此它们不是完整孪生点。3614个遗漏中，3608个有经共享邻居的50577最短路线；剩余6个核心点的最短补路走51275。新连接提供了原九点邻域没有的路线，而非重复增加已经覆盖的部分。</p>
<p>最小原基图对照还发现：下一张无补点例子的10点邻域，在原51417点图上就已全覆盖；其中保留的50638拥有被删6216的同一核心邻域。因此首次新增顶点对此例的旧目标覆盖并非必要。这里只对照了一例，不把其余39例都外推为原基图可行。<a href="../{probe}MECHANISM.md">机制、具体路线与对照</a>。</p>
<h2>数学验收与审阅</h2>
<p>首图51418已从完整边表独立重建，并直接比对原官方51417点raw邻接表：原324451条边全部保留，只加10条新边；所有度数≤13，新顶点到全图最远5步。后39步逐一检查实际当前图的完整R4覆盖和度数，保留旧边归纳得到全部点对≤5；各阶数超过D4 Moore界24506，故直径恰5。原公开基图D5事实继承，不重复旧全源BFS。</p>
<p>一次实际Gemini3.8Flash/high审阅接受首图数学结论和扩张论证；原文及处置均保留。审阅末尾建议后续逐图再独立BFS，这项重复检查按用户既定取舍未采用：首个新参数已独立检查，后续完整currentR4归纳足够，不冒称做过39次独立BFS。<a href="../reviews/ddp/d13_singlefault_star_20261027.DISPOSITION.md">审阅范围及意见处置</a>。完整实际图Lean实例仍0，Goal没有完成。</p>
<h2>结果、源码与专家包</h2>
<p><a href="../expert_review_current/MORE_GRAPHS_20261027.zip">完整ZIP</a> · <a href="../expert_review_current/MORE_GRAPHS_20261027.html.txt">本页HTML源码</a> · <a href="../research/ddp/more_graphs_20261027/delivery/families.json">103例全部字面参数</a> · <a href="../research/ddp/more_graphs_20261027/delivery/family_generator.py">统一生成器</a> · <a href="../research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md">数学说明与署名</a></p>
<pre>python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 13 --order 51457 --output graph51457.edges</pre>
<p><a href="../{probe}continuation/graphs/graph_d13_D5_n51457.edges">51457完整边表</a> · <a href="../{probe}accepted_family40.json">第三族40步</a> · <a href="../{probe}independent_newroot51418.json">首图独立验收</a> · <a href="../research/ddp/more_graphs_20261027/delivery/dry_run_d13_51457.json">生成器重建最强图：边表精确一致</a>。</p>
<p>主文件都保存在global_user/ar4math；下载区只镜像专家包。原51417、37628、42342公开源归Dharunish Yugeswardeenoo，partial-fold/duality基础归Rishabh Rajiv；本项目提供明确新增邻域、有限修复和完整图序列，不宣称首创孪生插入或单点扩张引理。公开主表17:38仍为51417；尚未公开提交或宣称最优。<a href="https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html">Comellas主表</a>。</p>
<h2>理解已怎样改变下一步</h2>
<p>我们已把代理规则迁到（14，5）、（15，5）：要求满点u和可接点w的邻域差分别≤3、≤1，替换旧原型中所有满点，使用完整缓存验覆盖。两个固定源分别虽有1088、205个满点能找到代理，但每个原型仍至少有8、9个满点没有代理，所以没有投影候选。阻碍在连接对象缺失，不是R4坏点减少；固定规则已停止，不靠改tie补不存在的代理。</p>
<p>此前（14，5）、（15，5）的64次完整连接选择也均未命中，任意14/15点覆盖仍未决。控制同一单余量类型后，平均R4占比分别17.39%、20.11%，密度提升属实，却没有自动实现共同覆盖，因而不再按漏3705/1848续轮。下一步应优先选择已有近完整可用原型或有明确路线代理的新源；原91池已完，不刷新失败。</p>
<p>固定AFY70普通两重覆盖在D6、三重覆盖在D7均被同纤维短闭路容量排除，未试电压；自然H3固定host的1..13个helper类已排，未逐阶研究14。精确范围、未决和重启条件均在唯一<a href="../research-wiki/DDP_METHOD_LEDGER.md">Research Wiki</a>，228条以上记录含来源、变体与工具，不等于独立方法数。</p>
<p><a href="../context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md">唯一恢复入口</a>；保留推导与历史，压缩后从最上方恢复。</p></body></html>'''
(ROOT/'research/progress.html').write_text(page)
summary=f'''# 第三参数40例已验收，Goal ACTIVE — {NOW}

当前数学结果103例/3参数：N(11,5)≥37631（3阶数），N(12,5)≥42402（60阶数），N(13,5)≥51457（40阶数51418..51457）。完整Lean实例0，Goal未完成。最新公开主表17:38仍51417，不宣称最优或已提交。

第三族首51418：original官方raw51417/324451直接对边，保全部原边，只加10边；fresh expanded adjacency新root全BFS eccentricity5，simple/max13/连通。后39步每步实际currentR4/degree归纳，未逐图root复验。最终51457/324863，generator全40prefix dry-run与最强边表精确一致，missing/extra/repeated0。原公开基图D5事实继承，无旧全源复算。

原91单满邻点prototype全部终态：40成功+13当时degreeblocked+38限定guard失败，0未试。首次38得1图；原53未试项一次得39图，续算3.209CPU、生产合12.853CPU，未刷新原37失败。停止这个固定池，不能据动态失败说final51457最大。

真正新直觉：11352与guard50577核心邻域相同（10点），差异全extras；guard代替私有路线，补3535core+79extras；具体距离/最短分支在singlefault_star_probe/MECHANISM.md。首noguard对照3962删6216的10pins在ORIGINAL51417就全覆，保留50638已是coreproxy；只测此例，不外推其它39。

一次Gemini真实SUCCESS/ACCEPT数学首图+通用归纳，reviews/ddp/d13_singlefault_star_20261027.DISPOSITION.md。原文要求后续逐图重复独立BFS的额外建议未按用户取舍采用，39次没有做，不伪称review免掉或做过。实际模型gemini-3.8-flash-high/high。

派生proxy向D14/D15固定源迁移也已终态：diff≤3/≤1固定投影，分别每原型至少8/9满pin无proxy，0候选/0R4检查；不要放宽tie后重复同一个不存在性障碍。D14/D15全free64构造、D14全局MIP UNKNOWN、AFY70 D6twofold/D7threefold容量、H3 helper1..13均已保存，不续失败最优值。D15密度20.11%对D14同单余量17.39%只支持局部覆盖提升，不等于完整构造。

交付：delivery/families.json、family_generator.py、FINAL_RESULTS_PROOF.md；expert_review_current/MORE_GRAPHS_20261027.zip及.html/.html.txt，下载镜像/mnt/data/AR4MATH_MORE_GRAPHS.zip。根报告research/progress.html。仅helper写唯一Wiki，不重导；方法账本228条以上是实验/来源/变体，不是方法数。

接下来优先：本批完成交付后，按‘低满邻点、已有free路线代理’选择新参数；对目前51457图可先只检查新生40顶点的完整邻域是否全部尚有余量（旧顶点全N至少1满度、degree单调已排，不重扫）。这是新生对象的完整false-twin路线规则，不是刷新37失败nearstars；≤1CPU可判是否有可扩张星，未执行，不能登记结果。若无直接候选，转原起始池其它D3/D4当前源；不要继续D14/D15原贪心或ordinary70cover尾部。最终仍需完整新构造及形式化，不能把直觉研究记为Goal完成。

最新用户允许公开表所有未close格子，不再以原27格作硬边界；旧D2/n61/SAT/谱暂停。当前原有Wiki已合并，不重复IMPORT。

---

下方历史快照不代表当前任务。

'''
entry=ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md'
entry.write_text(summary+entry.read_text())
brief=f'''# DD Portfolio research brief — {NOW}

## Problem Statement

继续同一ACTIVE Goal，在公开degree/diameter表所有未close格子构造超过最新公开下界的完整图；原4≤Δ≤12、D3/4/5是初始27格而非硬边界。旧D2/n61/SAT/谱暂停，唯一Wiki不重导。

## Constraints

优先有结构依据、较可能产完整图的其它参数，其次未深入源，再攻难点。先具体可推翻预测，再有限构造；保存推导/精确范围/重启条件。首次新机制或参数一次必要独立核验，后续完整实际currentR4/degree归纳，不逐图重复旧全源/BFS/外审。约每小时及重要变化更新progress.html，报告不等于暂停。完整图与Lean状态分列，不生成hash/manifest。

## What I'm Looking For

第三参数已成功：source13仅1满邻点的91原型，删1+≤2guards得到40图到51457。机制是free核心邻域代理，非raw映射假设。D14/D15同proxy投影都缺至少8/9个代理，固定规则已停。下一优先新生40顶点是否存在完整可用star（未检查），或其它D3/D4当前源中低满邻点且可提供互补路线的原型；原91及D14/D15贪心池不刷新。完整即时状态以NEXT_SESSION最上方为准。

## Background

唯一[方法账本](research-wiki/DDP_METHOD_LEDGER.md)按机制/参数/source查重，机器字段在同目录JSON。执行计划context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md；恢复入口NEXT_SESSION.md；人工原话research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md。先读相应条目，不全量重载旧历史。

## Non-Goals

不恢复D2，不重跑严格已闭范围，不以复现/同阶图/局部坏对下降/UNKNOWN/单个球比例提高代替完整新下界。不把动态各base失败登记为最后图最大，不把37次≤2guard失败扩大为更大guard预算不可行。

## Domain Knowledge

source13 prototype51013删11352后3535core+79extras私有路线由guard50577补齐：D/G同10core邻域，extras差异提供少数额外短路。首noguard原base单例已全cover，不能声称所有后39依赖seed。D14与D15单余量平均R4比例17.39%/20.11%，但各64构造都不全覆；下一规则要解决连接共同实现，不加greedy starts。D14全局MIP UNKNOWN，模型2被终止，未报精确总CPU或UNSAT。

## Existing Results (if any)

103不同阶数完整例子、3参数：37631/42402/51457。新13族40例，first51418独立新root+原raw对边，后39完整current归纳；最强生成器比对exactedge PASS。一次Gemini数学接受，额外逐步BFS建议按用户取舍未采纳且未声称执行。完整Lean实例0，Goal ACTIVE；ZIP/参数/源码在global_user/ar4math，下载区仅镜像。
'''
(ROOT/'RESEARCH_BRIEF.md').write_text(brief)
gap=ROOT/'research-wiki/gap_map.md'
gap.write_text(f'''# Gap Map — 最新 {NOW}

数学新下界3参数：N(11,5)≥37631、N(12,5)≥42402、N(13,5)≥51457，103阶数例子，完整Lean0，Goal ACTIVE。新13族原91池40accepted+13degreeblocked+38限定guardfail，全部终态。代理核心邻域补路是这次实质理解，完整R4实际验证不可省。

当前缺口：更多其它参数的完整图及最终实际图形式化。D14/D15固定proxy投影因每原型至少8/9无代理满点而0candidate；两源64贪心无命中不排任意14/15cover。D14全局MIP UNKNOWN，不冷启。新生40顶点的完整可用star仅列为下一项低成本预测，尚未执行；旧顶点fullstar monotone阻断不重扫。原91不刷新。原D2暂停，公开表所有未close格子可选。

唯一[恢复入口](../context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md)、[方法账本](DDP_METHOD_LEDGER.md)和交付delivery/为当前状态；旧快照不作任务队列。

---

以下历史保留范围，冲突以上方为准。

'''+gap.read_text())
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
common['helper'].rebuild_query_pack(str(ROOT/'research-wiki'))
status=dict(updated_UTC=NOW,goal_status='active',valid_examples=103,improved_parameter_pairs=3,
            mathematical_strongest={'11,5':37631,'12,5':42402,'13,5':51457},
            third_parameter_new_record=True,complete_Lean_instances=0,
            current_parameter=[13,5],active_research_processes=[],
            next_actual_action='Finish third-family expert archive; then test only40 newlyborn prototypes for legal fullstar, or choose a new currentD3/D4 source from structural evidence. No old91 refresh.',
            review_status='ACCEPTED_MATHEMATICS',review_disposition='reviews/ddp/d13_singlefault_star_20261027.DISPOSITION.md')
(WORK/'CURRENT_EXECUTION.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
agents=ROOT/'AGENTS.md';text=agents.read_text()
text=text.replace('当前数学最强至少37631/42402/51434，共至少80个超基线阶数例子、3参数，Lean0。','当前数学最强37631/42402/51457，共103个超基线阶数例子、3参数，Lean0。')
text=text.replace('当前构造资源转(15,5)100132实际源与覆盖profile；','当前第三参数40例已完成数学验收，后续优先低满邻点且有可用路线代理的新原型；')
agents.write_text(text)
goal=ROOT/'context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md';text=goal.read_text()
revision=f'''## {NOW} 第三参数实际成果与后续决策

本批已实际得到N(13,5)≥51457、40个不同阶数图，合计103例/3参数。机制从满度阻断完整邻域转为单满邻点删除与free核心邻域代理；第一图独立原raw对边+新root核验，后39逐步完整currentR4/degree归纳，一次Gemini数学审阅接受。原91候选已全部终态，不刷新失败。D14/D15的固定投影亦因缺代理明确收束。下一选择以当前source的低满邻点与可替代路线为依据，先具体预测后构造，继续其它未close参数，不按坏点数续微调。完整Lean实例0，Goal仍ACTIVE；详见NEXT_SESSION最上方，不据历史63/80例段落恢复旧队列。

'''
text=text.replace('## 0. 任务与权限边界',revision+'## 0. 任务与权限边界',1)
goal.write_text(text)
print('Rendered103/3 current HTML, brief, recovery, goal revision and query pack at '+NOW)
