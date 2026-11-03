"""Refresh the single recovery entry and live report from terminal evidence."""
from pathlib import Path
from datetime import datetime, timezone
import runpy

ROOT=Path(__file__).resolve().parents[3]
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
status=f'''# 当前Goal ACTIVE — {NOW}

最新人工授权：公开degree/diameter表中所有尚未close的格子均可选；原27格只是起始池。优先产出其它参数完整构造，先有可检验的结构直觉，再构造和适量核验，及时保存推导。旧N(8,2)/n61/SAT/谱暂停；不新建Goal、不重导Wiki。

已接受结果：N(11,5)≥37631、N(12,5)≥42402，共63个不同阶数例子、2参数，完整Lean实例0。没有第三参数新纪录。统一参数/生成器：research/ddp/more_graphs_20261027/delivery/。新Rédei15四例42399..42402已有一次集中Gemini数学接受（85项计数订正4+23+58），首步fresh edge-file新root独立核验，后续每步degree+完整currentR4归纳。最后全源checkpoint仍42377，不重跑旧基图。

当前数学入口与本批终态：
- 正在(15,5)当前100132 source取数与覆盖profile。选它是因为Δ15的理论R4容量44326/100132高于Δ14的33321/94186，且来自不同F5^5/32controller机制；先检验首20个实际free点的平均R4比例是否高于D14 rare类约16%，不能以理论容量代替完整cover。source一次流式下载；literal后actualdegree+首20球≤5CPU，未自动启动全free/64starts。见d15_D5_mizuno_extension/PREDICTION与DOWNLOAD_PROGRESS。
- (14,5)：94186/m657452 source已到，free3685/slots3700。rare15类全部14-subsets失败后改全free，一次补3670R4球；allfree union全盖，每target支持455..824，但64个固定14pin构造全失败，漏3705..4479，总4.412CPU。操作预测被反驳，任意≤14pin存在性仍UNRESOLVED。已停止该有限生成规则，43MB完整球缓存保留，不按3705继续微调。
- (13,5)：stable3640 fullQlines全degreeblocked。nonstable87360occurrences按共轭合为43680实际closuretests，也全含满度pin；12096项card≤13仍不合法。仅1满pin的12项全部fullsize19，删后18>13，故singlefault池也无合法项。诊断恢复0.172CPU不计新line实验；不扩其它plane或删多点。
- (13,3)：公开主表972，旧描述页仍952；具体52470byte source已索引但literal尚未取得。已提出奇数27fiber若外度12且内部matching则至少36spares的预测，未作actualdegree/覆盖检验。不是当前计算队列；不继续网页重复下载。
- 一名代理负责D15实际source/profile，其余已完成有限任务；63例ZIP和H3受限类证明已保存。root维护共同状态、推导与有限实验取舍。当前唯一Wiki账本220条记录，不等于220独立方法；回填脚本是历史批次，不用旧输入重建覆盖当前账本。

刚完成且不得原样重跑：
- (13,5)51417源已绑定50554核心+863extras。702稳定Rédei×1120planes共786240项degree池0。核心不是旧core的pair-flip gauge：1345个K2,2→matching及1345个反向变化，类内翻转不能改边数。不得虚构非stable raw映射。
- 同源whole-class Baer13：7560×1120=8467200项，1740次closure全部pins degree合法，但card21/22/26=814/158/768，全部>13，pool0。只关这两个固定池；非F3 planes/其它阻塞集仍未排。
- (4,5)自然H3源364/714，28个degree3 ports两两距离5，任何保边且不加old-old边的D5增广helper连通，4k≥28+2(k−1)→k≥13。k13所有diam≤4 tree归约后，3276triples与81900(triple,parentport)都不能完整覆盖所需外部R2分区，因此1..13全关，必要helpers≥14；k14未查，不逐阶续长尾。
- PSL：p23/C3的4661项；q25/C4两个78规则；q25/C5的60项均完整无命中。既无第三参数图，也不外推一般图不存在。
- 新Rédei15 N12固定85项once-policy全部终态，4成功/23degree阻断/58coverage失败，0UNKNOWN。按用户其它参数优先，不changed-base刷新这个池。

原441 uniform旗规则、2485 C25有限范围、Exoo72有限范围、5334固定基图>2-sheet、1152局部坏对修补均保持已收束状态。精确证据见唯一research-wiki/DDP_METHOD_LEDGER.md及同名实验目录。记录数包含变体、来源与工具，不是独立方法数。

---

以下是历史快照；冲突时只执行本页最上方状态。

'''
entry=ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md'
entry.write_text(status+entry.read_text())
brief=ROOT/'RESEARCH_BRIEF.md'
old=brief.read_text()
history=ROOT/'research/ddp/more_graphs_20261027/BRIEF_HISTORY_BEFORE_TRANSFER.md'
if not history.exists(): history.write_text(old)
brief.write_text(f'''# DD Portfolio research brief — {NOW}

## Problem Statement

在公开degree/diameter表尚未close的格子里，构造超过最新公开下界的完整简单无向图。用户已明确允许超出最初4≤Δ≤12、D∈{{3,4,5}}的27格。继续同一ACTIVE Goal、同一个Research Wiki，旧N(8,2)/n61/SAT/谱暂停。

## Constraints

优先有结构依据、较可能成功的其它参数，其次尚未深入入口，再攻难点。先写可被推翻的覆盖预测，再推导/小实验/构造；结果必须改变下一规则或参数选择。不要按小幅坏对下降无限续算，也不机械中断有依据的有限工作。复用已验证基图与代码，新机制首次命中做必要独立核验，后续完整degree+currentR4归纳，不重复旧全源或逐图外审。最终图仍须全部点对达标；数学发现与Lean完成分列。推导和精确失败范围即时保存；约每小时及重要变化更新research/progress.html。

## What I'm Looking For

当前转(15,5)100132实际source与首20free点R4比例检验，比较Δ15/F5^5结构与已测Δ14/F3^5覆盖密度，检验后再决定构造规则。D14全3685free球已保存，64固定14pin构造均失败，≤14任意cover仍未决；D13 stable/nonstable Qline、Rédei、Baer固定池已终态，不复跑。(13,3)972 literal待取得，奇数fiber余量预测未验。自然H3固定host的1..13helpers已排，不从14起逐阶续。详细状态见唯一[NEXT_SESSION](context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md)。

## Background

唯一知识库[方法账本](research-wiki/DDP_METHOD_LEDGER.md)，按机制、参数、source、已排范围检索；不反复重载整本。当前执行计划[RESEARCH_GOAL](context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md)。人工原话仍在research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md。旧brief原文保存在research/ddp/more_graphs_20261027/BRIEF_HISTORY_BEFORE_TRANSFER.md，不是当前队列。

## Non-Goals

不恢复旧D2，不重跑严格已闭有限范围，不以UNKNOWN/局部条件/复现/同阶例子作新下界，不将文件整理记为数学成果。不生成hash/checksum/manifest。

## Domain Knowledge

当前13核心具有complete/matching类块，F路径可lift，所以whole-class阻塞邻域可保证核心R4；旧raw非stable集合不自动适用。任何新邻域还需通过当前degree与全部extras覆盖。自然H3固定host的1..13helpers已排；任意377图/其它host不受此结论。失败必须限定当前source、生成规则和完整实际范围。

## Existing Results (if any)

N(11,5)≥37631、N(12,5)≥42402；3+60=63个不同阶数完整例子，仅2参数，无第三参数新纪录。完整Lean实例0，Goal未完成。delivery/families.json和family_generator.py可恢复全部图。最后四图源于新Rédei15覆盖，已获一次Gemini审阅接受（85项计数纠正），没有重复旧图全源检查。(12,5)固定池停止，新资源转其它参数。
''')
gap=ROOT/'research-wiki/gap_map.md'
gap.write_text(f'''# Gap Map — 当前修订 {NOW}

当前目标：公开表所有未close格子，优先取得其它参数的完整新图；原27格不是硬边界。同一Goal ACTIVE、唯一Wiki，旧D2暂停。N(11,5)≥37631、N(12,5)≥42402，共63例/2参数，Lean0，第三参数仍未取得。

当前入口：(15,5)100132 source与首20free点R4比例预测。D14全free64构造已无命中，43MB球缓存保存，任意≤14cover仍未决；D13 stable/nonstable Qline、702Rédei、7560Baer固定池均degree空，不重跑。(13,3)972 literal待取得、奇数fiber余量预测未验。自然H3固定host的1..13helpers已排，不从14起逐阶续。(12,5)85项池已终态。

恢复先读[NEXT_SESSION](../context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md)，按[账本](DDP_METHOD_LEDGER.md)对应机制检索，推导/失败范围及时入库。最终成果缺口仍是更多参数的完整新图及最终形式化，不把直觉研究或整理计作Goal完成。

---

以下保留历史范围与旧阶段，非当前派发计划。

'''+gap.read_text())
goal=ROOT/'context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md'
txt=goal.read_text()
txt=txt.replace('主力转(4,5)自然H3极性364图的一点/双点协作扩张，并检查已成功阻塞集技巧向(13,5)公开51417源的合法迁移。','该轮(4,5)与(13,5)有限迁移已终态；当前按NEXT_SESSION转(13,3)972与(14,5)94186 source，继续先直觉、后构造。')
goal.write_text(txt)
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>构造进展：其它参数优先</title><style>body{{max-width:1040px;margin:32px auto;padding:0 22px;font:17px/1.8 system-ui;color:#182839}}h1{{font-size:28px}}h2{{font-size:23px}}.note{{padding:16px;background:#edf3fa}}.result{{padding:16px;background:#e9f5ed}}table{{width:100%;border-collapse:collapse}}td,th{{padding:9px;border-bottom:1px solid #ccd6df;text-align:left}}code,pre{{white-space:pre-wrap}}a{{color:#145f9c}}</style></head><body>
<h1>当前任务：把构造经验迁移到其它未关闭参数</h1><p>更新：{NOW}。同一Goal ACTIVE；范围已按最新人工授权扩大到公开表尚未close的格子。原27格保留为起始池，旧N(8,2)归档工作继续暂停。</p>
<div class="note"><strong>当前尚无第三参数的新纪录图。</strong>本批(13,5)、(14,5)有限检验均已收束；正在转(15,5)100132实际源，先比较20个可接点的真实覆盖比例，再决定连接规则。已有63例ZIP已交付，(12,5)不再续同一池。</div>
<h2>本次预测、检验与下一步</h2><table><tr><th>问题</th><th>预测与实际检验</th><th>实际决策</th></tr>
<tr><td>(13,5)，51417源</td><td>稳定Rédei15应有可接邻域：702×1120项全检查，degree合法0，预测被反驳。旧raw映射也不能只翻转标签恢复：1345个边块4→2、1345个2→4。改whole-class Baer13后，8467200项中1740次全部pins可接，但需要21/22/26pins，全部超过13。</td><td>停止这两个固定池；不称整个(13,5)无望。<a href="../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/REPORT.md">源与覆盖证明</a> · <a href="../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/baer13_transfer/RESULT.json">Baer结果</a></td></tr>
<tr><td>(4,5)，自然364源</td><td>28个端口两两距离5，度预算先给k≥13。k13必须是diam≤4的tree；所有拓扑归约后，3276个三元组和81900个加父端口组合均无足够外部分区覆盖，故固定host的1..13 helpers全排。</td><td>必要helpers现≥14，未从14起逐阶继续。任意377图和其它host未排。<a href="../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/REPORT.md">具体推导与范围</a></td></tr>
<tr><td>(13,3)，主表972</td><td>主表972、旧描述页952；已定位36×F3³具体source，但literal尚未取得。若外度12且内部是matching，奇数27点块必有未匹配点，预测至少36个spares，仍待实际检验。</td><td>保存精确来源与预测，未猜实际度数；暂不重复网络队列。</td></tr>
<tr><td>(14,5)，94186源</td><td>已绑定3685可接点/3700槽。rare15类14子集最少漏9754；改全free后64固定14pin构造全失败，漏3705–4479。所有候选合并能盖全图，每target支持455–824，故不是根本到不了，而是14个连接的共同覆盖未实现。</td><td>总4.412CPU，保存43MB完整球缓存后停止；任意≤14cover仍未决，不按漏3705继续。<a href="../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/REPORT.md">第二次预测与真实范围</a></td></tr>
<tr><td>(15,5)，100132源</td><td>Δ15理论R4容量相对阶数更高，且原机制为32controller×F5⁵；预测首20个实际free点的平均覆盖比例高于D14约16%，尚待literal检验。</td><td>一次流式取当前源，随后degree与20球profile≤5CPU；不把外部degree报告或旧fiber标签冒作当前绑定。</td></tr></table>
<p>(13,5)nonstable新规则也已终态：87360line occurrences按共轭合为43680个实际closuretests，全部含满度pin。12个仅单满pin的诊断全部需19pins，删后18仍超过13；无R4/anchors生产，不重跑stable3640line或续删多点。</p>
<h2>已经取得的完整图</h2><div class="result"><table><tr><th>参数</th><th>公开基线</th><th>本轮最强</th><th>不同阶数完整例子</th></tr><tr><td>(11,5)</td><td>37628</td><td>37631（+3）</td><td>37629–37631，3例</td></tr><tr><td>(12,5)</td><td>42342</td><td>42402（+60）</td><td>42343–42402，60例</td></tr></table></div>
<p>合计63例、2参数；不是63种独立方法。全部数学验收通过，完整Lean实例仍0，Goal没有完成。最强42402图有245937条边，最大度12，直径恰5。</p>
<h2>最新成功机制：Rédei15阻塞邻域</h2><p>f(x)=x⁵的9个图点加6个方向点碰到PG2(F9)每一条直线；5个固定点与5对共轭点折成10+s个连接点，给extras留下anchors。新邻域不包含旧完整Q-line或Baer13。有限85项依次测试得到42399–42402四个新图，4成功+23当时度阻断+58当时覆盖失败，0UNKNOWN。失败仅针对各自当时基图，不声称最终42402已不可扩张。</p>
<p>每一步检查实际degree与全旧图完整R4覆盖，保留全部旧边，归纳得D≤5；阶数超过D4 Moore界给D恰5。新机制第一图从边表重建独立验新根，其后不重复旧全源BFS。一次集中Gemini审阅已接受覆盖论证与四图，记录中漏计第一失败项的算术已处置；完整实际图的Lean仍未完成。<a href="../research/ddp/more_graphs_20261027/h9_redei15/theory/PROOF.md">覆盖证明</a> · <a href="../reviews/ddp/redei15_20261027.DISPOSITION.md">审阅处置</a></p>
<h2>文件和可恢复源码</h2><p><a href="../expert_review_current/MORE_GRAPHS_20261027.zip">完整ZIP</a> · <a href="../expert_review_current/MORE_GRAPHS_20261027.html.txt">HTML源码</a> · <a href="../research/ddp/more_graphs_20261027/delivery/families.json">全部字面参数</a> · <a href="../research/ddp/more_graphs_20261027/delivery/family_generator.py">统一生成器</a> · <a href="../research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md">数学说明</a></p>
<pre>python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42402 --output graph42402.edges</pre>
<p><a href="../research/ddp/more_graphs_20261027/h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges">42402完整边表</a> · <a href="../research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges">37631完整边表</a>。以上文件均在实际global_user/ar4math目录，ZIP含原作者基图、生成参数与代码。基础partial-fold/duality归Rishabh Rajiv，原公开扩张基图归Dharunish Yugeswardeenoo；本项目新增明确邻域与构造。</p>
<p>公开数值以<a href="https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html">Comellas主表</a>为准（本次已核对），不能以滞后描述页作当前纪录。</p>
<p>推导、失败范围与重启依据存入唯一<a href="../research-wiki/DDP_METHOD_LEDGER.md">Research Wiki</a>；当前任务只看<a href="../context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md">恢复入口最上方</a>。PSL固定陪集、441旗规则等已完成负结果留在对应节点，不按失败最优值继续微调。</p></body></html>'''
(ROOT/'research/progress.html').write_text(html)
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
common['helper'].rebuild_query_pack(str(ROOT/'research-wiki'))
print('Updated recovery, brief, gap map, query pack, plan and live HTML at '+NOW)
