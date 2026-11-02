"""Render the existing comparison data and the user's requested discussion page."""
import csv
import html
import json
from datetime import datetime, timezone
from pathlib import Path

STAGE = Path(__file__).resolve().parent
ROOT = STAGE.parents[2]
OUT = ROOT / 'research'
state = json.loads((STAGE / 'STAGE_STATE.json').read_text())
with (OUT / 'public_comparison_current.csv').open(encoding='utf-8-sig') as stream:
    rows = list(csv.DictReader(stream))


def esc(value):
    return html.escape(str(value), quote=True)


def number(value):
    return f'{int(value):,}' if value != '' else '—'


def sources(value):
    urls = [s.strip() for s in value.split(' ; ') if s.strip()]
    return ' · '.join(f'<a href="{esc(url)}">来源{index + 1}</a>'
                      for index, url in enumerate(urls)) or '待核'


body_rows = []
for row in rows:
    margin = row['margin']
    margin_text = f'{int(margin):+,}' if margin != '' else '—'
    body_rows.append(
        '<tr>'
        f'<td>({row["degree"]}, {row["diameter"]})</td>'
        f'<td class="num">{number(row["our_best_vertices"])}</td>'
        f'<td class="num">{number(row["checked_comparison_vertices"])}</td>'
        f'<td class="num">{margin_text}</td>'
        f'<td>{esc(row["evidence_kind"])}</td>'
        f'<td>{esc(row["note"])}<br>{sources(row["source_url"])}</td>'
        '</tr>')

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
target_rows = []
for row in rows:
    if row['diameter'] == '3' and 20 <= int(row['degree']) <= 26:
        target_rows.append(
            '<tr>'
            f'<td>({row["degree"]}, 3)</td>'
            f'<td class="num">{number(row["our_best_vertices"])}</td>'
            f'<td class="num">{number(row["checked_comparison_vertices"])}</td>'
            f'<td class="num">{int(row["margin"]):+,}</td>'
            '<td>未找到达到或超过本地图的公开构造</td></tr>')
page = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>公开比较、先进性与D3创新性说明</title>
<style>
:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;background:#f5f7fa;color:#213047;font:16px/1.8 system-ui,-apple-system,"Microsoft YaHei",sans-serif}main{max-width:1180px;margin:auto;padding:36px 24px 70px}h1{font-size:30px;line-height:1.4;margin:0 0 10px}h2{font-size:23px;margin-top:38px;scroll-margin-top:20px}h3{font-size:18px;margin-top:25px}a{color:#1559a0;text-underline-offset:3px}p{margin:12px 0}.meta{color:#627087;font-size:14px}.card{background:white;border:1px solid #dde4ed;border-radius:12px;padding:22px 26px;margin:20px 0}.important{background:#eaf2fc;border-left:4px solid #3678b8}.caution{background:#fff5e5;border-left:4px solid #c7892e}nav{display:flex;gap:10px 20px;flex-wrap:wrap;margin:22px 0}.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:15px}th,td{text-align:left;padding:12px 10px;border-bottom:1px solid #e1e6ee;vertical-align:top}th{background:#edf2f8}td.num{white-space:nowrap;font-variant-numeric:tabular-nums}code{background:#eef2f7;padding:2px 5px;border-radius:4px}li{margin:10px 0}input{font:inherit;padding:10px 13px;border:1px solid #b9c6d7;border-radius:7px;width:min(500px,100%)}small{color:#637189}.formula{white-space:nowrap}@media(max-width:600px){main{padding:24px 14px 45px}.card{padding:17px}h1{font-size:25px}th,td{padding:10px 8px}}
</style></head><body><main>
<h1>公开比较、先进性与D3创新性说明</h1>
<p class="meta">生成：__NOW__。整理本次对话中的公开来源、结果表和贡献判断；这是比较快照，研究动态见进展页。</p>
<nav><a href="#paper-claims">论文是否声称最大／后续引用</a><a href="#d3-20-26">20–26度专项检索</a><a href="#main-table">与Comellas表比较</a><a href="#public-files">公开图在哪里</a><a href="#d3-summary">D3比较依据</a><a href="#novelty">创新性判断</a><a href="#all-pairs">43组完整表</a><a href="public_comparison_current.csv">下载CSV</a><a href="public_comparison_current.html.txt">HTML源码</a></nav>
<div class="card important"><strong>当前判断：有些结果超过已核公开下界；D3整批的全球领先性与方法创新性尚未确认。</strong><p>此前未经完整比较使用的“全球SOTA”表述应撤回。合法图、超过某项公开下界、方法新颖和最早归属，是不同结论。</p><p>项目当前保存__GRAPHS__个合法命名图版本、__PAIRS__组参数，其中__LEAN__个具体实例完成Lean证明。多个degree或点数版本不等于同样多的独立创新；已认证全球优先权的新纪录仍为0。</p></div>

<h2 id="d3-20-26">新增：20–26度、直径3专项公开检索</h2>
<div class="card important"><strong>截至2026年11月1日本轮已查公开来源，这七张本地图均大于已定位的外部构造保证，未找到达到本地图点数的公开构造。</strong><p>因此可标为“本轮公开检索中最大的已知实例／纪录候选”。这些参数已有研究；不是从表中缺少条目推断无人做。这个带日期和来源范围的结论不要求证明不存在任何未公开结果。</p></div>
<div class="scroll"><table><thead><tr><th>参数</th><th>我们当前图</th><th>已核公开方法保证</th><th>相对差额</th><th>本轮扩展检索结果</th></tr></thead><tbody>__TARGET_ROWS__</tbody></table></div>
<p>20度的2,791是19度2,783点公开图与通用复制定理的推论；用户查到的3,250点线索仍待核来源，若最终确认属于(20,3)，我们的3,840点仍多590点。21–23度的2,928／3,294／3,549来自PolarStar公式；24／25度来自广义四边形公式；26度的7,514是公开源和一般复制的组合推论。不能把这些推论说成作者逐一发布的数值边表。</p>
<p>确实有人研究这些范围：<a href="https://guillermo.com.au/pdfs/NewLargeGraphs(C).pdf">Loz与Pineda-Villavicencio的论文</a>给出17–20度的明确数值表；<a href="https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf">SPAA2024 PolarStar</a>研究直径3及高radix构造；<a href="https://doi.org/10.5281/zenodo.23052995">Rajiv的2026年公开结果</a>给19／20度2,783点；<a href="https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2">2026年的几何乘积论文</a>明确重述覆盖24／25度的旧构造公式。</p>
<p>检索覆盖相关维护表入口、近期论文及已识别作者结果索引。当前CombinatoricsWiki高degree页面未能取到，部分作者目录不可访问，Delorme JGT1985原文增强部分仍未读全。故“截至本轮所查资料最大”是可支持的表述；无日期和范围的“全球已认证最好／方法原创”仍不作结论。</p>
<p><a href="ddp/two_successful_methods_20261101/public_baseline_audit/D3_CAP20_23_USER_PRIMARY_SEARCH_20261101.json">20–23度检索记录</a> · <a href="ddp/two_successful_methods_20261101/public_baseline_audit/D3_CAP24_26_USER_PRIMARY_SEARCH_20261101.json">24–26度检索记录</a> · <a href="ddp/two_successful_methods_20261101/public_baseline_audit/D3_CAP20_26_USER_SEARCH_SUMMARY_20261101.json">七组汇总与来源范围</a></p>

<h2 id="paper-claims">新增：这些论文是否声称最大，后来有没有被引用或更新？</h2>
<div class="card important"><strong>有些论文明确报告“当时最大已知”，也确实有后续论文引用并更新旧结果；声明必须连同日期和参数范围一起读。</strong><p>论文中的largest known表示作者依当时资料报告的纪录，optimal表示证明任何合法图都不能更大。我们的21–26度比较值有些只是已发表公式的代入，不能替作者补出逐项纪录声明。</p></div>
<div class="scroll"><table><thead><tr><th>原始论文／报告</th><th>是否声称当时最大</th><th>涉及的实际数值与范围</th><th>对20–26度比较意味着什么</th></tr></thead><tbody>
<tr><td><a href="https://doi.org/10.5281/zenodo.21180071">Rajiv，2026年7月</a></td><td>摘要明确报告新的最大已知图。</td><td>所列特定参数包括20度、D3、2,202点。</td><td>是带时间的具体纪录报告，后来被同作者后续结果提高。</td></tr>
<tr><td><a href="https://doi.org/10.5281/zenodo.22073603">Rajiv，2026年8月</a></td><td>明确报告提高已发表下界，并保留作者当时所知的范围。</td><td>20度、D3、2,750点。</td><td>引用7月报告并提高20度结果，不是最终或今天的最大值。</td></tr>
<tr><td><a href="https://doi.org/10.5281/zenodo.23052995">Rajiv，2026年9月</a></td><td>以截至2026年9月的最大已发表下界作比较，报告新下界；表中“最大已发表”短语定义的是previous-bound列。</td><td>19度2,783点，因此也适用最大度上限20；20格前值2,750，新下界2,783。</td><td>支持20度的具体改进报告；2,791是我们再套一般复制定理所得，原文没有单独报告2,791点图。</td></tr>
<tr><td><a href="https://spcl.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf">PolarStar，SPAA2024</a></td><td>有“几乎所有radix的最大已知直径3网络”的广泛声明；接近最优的讨论还有限定的star-product设计空间。</td><td>正文明确比较18–20度及更高radix；不能把almost all读成每个degree都已逐格证明领先。</td><td>2,928／3,294／3,549是我们对21／22／23度合法代入得到，尚未定位原文逐一将这三个数字声明为全图纪录的表格。</td></tr>
<tr><td><a href="https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf">Delorme，EJC1985</a></td><td>引言与Table2给截至1983年末的已知最佳数值表。</td><td>该表列3–15度；另给一般构造与复制方法。</td><td>支持方法来源；不把6,144／7,225／7,514当成原文三个“已知最大”表项。</td></tr>
<tr><td><a href="https://doi.org/10.1002/jgt.3190090304">Delorme，JGT1985</a></td><td>原文未取全，具体纪录措辞未知。</td><td>后续论文明确把opposite-GQ构造归给这篇。</td><td>24–26度及同cap填补的精确归属仍需原文；不凭题名推断有或没有最大声明。</td></tr>
<tr><td><a href="https://guillermo.com.au/pdfs/NewLargeGraphs(C).pdf">Loz与Pineda-Villavicencio，2010</a></td><td>摘要与正文明确报告17–20度、D2–10的当时最大已知网络。</td><td>Table2列旧D3结果17／1,610、18／1,620、19／1,638、20／1,958。</td><td>证明20度早有具体研究；旧表值不替代今天已核的更强来源。</td></tr>
<tr><td><a href="https://arxiv.org/html/2608.27253v2#S7.SS8.SSS1">Isham等，2026年10月v2</a></td><td>§7.8.1明确称18度2,340点为截至2026年10月最大已知；§7.7对19／20度仅称接近最大已知。</td><td>Table3给19／2,470、20／2,600；它是极性图设计空间表，止于20度。</td><td>不能把较新的2,600说成20度全球最好；24／25的6,144／7,225来自它重述的公式，26度7,514还用到一般复制。</td></tr>
</tbody></table></div>

<h3>实际读到参考文献的后续引用链</h3>
<p>下面的箭头表示“后来的论文引用较早论文”，均核过原文参考文献或明确正文引用。列举确认的关系，不冒作完整被引清单或被引次数。</p>
<div class="scroll"><table><thead><tr><th>后续论文 → 被引论文</th><th>原文定位</th><th>后续结果是否改变相关比较</th></tr></thead><tbody>
<tr><td>Rajiv 2026年8月 → Rajiv 2026年7月</td><td>8月报告参考文献[11]</td><td>20度结果从2,202提高到2,750。</td></tr>
<tr><td>Rajiv 2026年9月 → 7月及8月报告</td><td>9月报告参考文献[19]、[20]</td><td>20度上限的下界提高到2,783；这是一条同作者后续报告／自引链。</td></tr>
<tr><td>Rajiv 2026年9月 → Isham等2026年8月v1</td><td>9月报告参考文献[13]与Table1；当时10月v2尚未发布</td><td>19度从2,470提高到2,783；这个最大度19图也适用于20度上限。</td></tr>
<tr><td>Isham等2026 → PolarStar 2024</td><td>参考文献[31]；§7.8.1</td><td>明确把18度旧值1,830提高到2,340；这一更新不属于我们20–26的七格。</td></tr>
<tr><td>Loz与Pineda-Villavicencio 2010 → Delorme两篇1985论文</td><td>参考文献[16]为EJC、[17]为JGT；相关构造章节</td><td>确认几何源、极性与复制方法的继承关系；不提供新的24–26度对手点数。</td></tr>
<tr><td>Isham等2026 → Delorme两篇1985论文</td><td>参考文献[19]为EJC、[20]为JGT；§3.4.2、§7.7</td><td>明确重述opposite-GQ公式与复制。是24–26比较方法的可核出处，不是七格最新总纪录表。</td></tr>
<tr><td>Isham等2026 → Loz与Pineda-Villavicencio 2010</td><td>参考文献[35]；§4.2、§7.3与Theorem2.7</td><td>引用并扩展距离论证，没有给出达到本地6,160／7,242／7,532的24–26度结果。</td></tr>
<tr><td>V3R1T4S作者公开包 → Rajiv 2026年9月报告</td><td><a href="https://raw.githubusercontent.com/elder-plinius/V3R1T4S/main/known-knowns/biggest-graphs/README.md">README的References／credit条目</a></td><td>这是后续公开包引用，非期刊论文；所读七项结果范围未给20–26度D3更新。</td></tr>
</tbody></table></div>
<p><small>8月报告的Table1仍把20度旧基线写为1,958，但正文Remark2已承认7月的2,202并说明得到更大图；本页2,202→2,750的更新线依据正文与真实日期，不把旧基线列误当完整同期最强证明。</small></p>
<div class="card"><strong>20度这条可核的更新线：</strong><p>2026年7月2,202 → 8月2,750 → 9月2,783 → 已发表方法的复制推论至少2,791 → 本地当前3,840。</p><p>用户提供的3,250点仍为待核线索；若确认属于(20,3)，应加入这条比较线，本地仍多590点。后续引用本身不代表认可所有纪录声明；较新的论文也可能只研究特定图族。</p></div>
<p><strong>对我们七张图的当前影响：</strong>这次沿已确认的引用链，尚未定位到达到本地七个点数的后续公开构造。因此仍保留“截至本轮已查公开资料中最大实例／纪录候选”的结论。对较新报告，未找到后续引用不表示无人引用或没有更新；本页没有给未经核定的引用总数。</p>
<p><a href="ddp/two_successful_methods_20261101/public_baseline_audit/D3_PAPER_CLAIMS_FORWARD_CITATIONS_20_23_20261101.json">20–23度：原文声明与后续引用证据</a> · <a href="ddp/two_successful_methods_20261101/public_baseline_audit/D3_PAPER_CLAIMS_FORWARD_CITATIONS_24_26_20261101.json">24–26度：原文声明与引用证据</a></p>

<h2 id="main-table">一、与当前Comellas主表比较</h2>
<p><a href="https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html">Comellas原始表</a>目前覆盖degree 3–16、diameter 2–10。它列的是“最大已知图”；只有加粗项表示已证明最优。页面提示新结果收录可能有延迟。高degree未列入这个数值表，不能据此推断没有更好的已知构造。</p>
<div class="scroll"><table><thead><tr><th>参数(Δ,D)</th><th>我们当前点数</th><th>当前Comellas表</th><th>准确判断</th></tr></thead><tbody>
<tr><td>(11,5)</td><td class="num">37,631</td><td class="num">37,628</td><td>超当前表3点；全球最新比较待补</td></tr>
<tr><td>(12,5)</td><td class="num">42,402</td><td class="num">42,342</td><td>超当前表60点；全球最新比较待补</td></tr>
<tr><td>(13,5)</td><td class="num">51,457</td><td class="num">51,417</td><td>超表40点，但低于作者另行公开的88,452点图36,995点</td></tr>
<tr><td>(16,4)</td><td class="num">16,389</td><td class="num">16,384</td><td>超当前表5点；全球最新比较待补</td></tr>
</tbody></table></div>
<p>比较必须采用相同限制：最大度不超过Δ、直径不超过D。只查旧详情页、只比较某一种图族，或只比较正则图，都可能漏掉适用的更大图。</p>

<h2 id="public-files">二、之前说的“更大公开图”在哪里</h2>
<div class="card"><h3>13度、直径5、88,452点：有完整公开图包</h3>
<p><a href="https://github.com/rmizuno42/ddp/blob/main/results/degree13-diameter5/README.md">Mizuno作者构造说明</a> · <a href="https://github.com/rmizuno42/ddp/blob/main/results/degree13-diameter5/certificate/graph.edges.gz">完整压缩边表</a> · <a href="https://raw.githubusercontent.com/rmizuno42/ddp/main/results/degree13-diameter5/README.md">原始README文本</a></p>
<p>作者报告它是13正则、574,938边、直径恰5的完整简单图，2026年10月13日加入仓库。作者同时注明该结果尚未反映在Comellas表中。本项目核读作者报告，未重新验证这张外部图；也未证明它达到数学最大值。</p></div>
<div class="card caution"><strong>D3的35,875、161,650、169,900，证据类别不同。</strong><p>这三个具体数字是本项目代入、组合已发表方法得到的下界。未定位到作者分别发布这些具体点数的完整边表，也未确认它们是全球最高。因此直接搜索点数未必能找到独立图包。</p></div>

<h2 id="d3-summary">三、D3高degree此前使用的比较</h2>
<p>以下下界是已核方法保证，不能当作逐项全球纪录表。全部具体参数、差额与来源在后面的43组表中。</p>
<div class="scroll"><table><thead><tr><th>D3参数</th><th>我们当前结果</th><th>已核方法下界</th><th>差额</th></tr></thead><tbody>
<tr><td>35度</td><td class="num">20,580</td><td class="num">35,875</td><td>已落后15,295点</td></tr>
<tr><td>54度</td><td class="num">56,862</td><td class="num">55,512</td><td>+1,350</td></tr>
<tr><td>55–59度</td><td>57,672至60,912</td><td class="formula">1028Δ</td><td>+1,132逐降至+260</td></tr>
<tr><td>64–79度</td><td class="formula">160050+1650(Δ−64)</td><td class="formula">160000+1650(Δ−64)</td><td>每组+50</td></tr>
<tr><td>80度</td><td class="num">327,744</td><td class="num">327,680</td><td>+64</td></tr>
<tr><td>81度</td><td class="num">342,290</td><td class="num">342,225</td><td>+65</td></tr>
<tr><td>82、83、86、90、94、98度</td><td class="formula">4226Δ−16</td><td class="formula">4225Δ</td><td>分别+66、67、70、74、78、82</td></tr>
</tbody></table></div>
<p>例如，65度目前最好为161,700点，比较保证161,650；70度目前最好为169,950点，比较保证169,900。旧65度161,150和旧70度166,650另行保留，它们已被该公开方法下界超过。</p>
<p>20–26度也列入完整表：已有较弱来源保证不等于最新全球阈值。用户提供的3,250点线索仍保留为来源和参数待核，不能凭未搜索到就否认它；17度的当前公开比较尚未核定。</p>
<h3>具体原始依据</h3>
<ul>
<li><a href="https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf">Delorme，1985，Grands Graphes de Degré et Diamètre Donnés</a>：§2给极性商，§7给一般复制，§8给具体几何集合。35度下界为33,825+2×1,025=35,875。</li>
<li><a href="https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf#page=12">Cimráková–Fack，2007，印刷p140 Table 5</a>：W(7)中实际找到33点partial ovoid；43是该表的上界。结合50条spread和公开源构造，得到每升一度增加1,650点的比较保证。</li>
<li><a href="https://arxiv.org/html/2608.27253v2">Isham等，2026</a>：§3.4.2给opposite-GQ公式，§7.4给极性乘积，§7.7讨论复制。q=r=8时，源为342,225点、degree81，可复制中心4,225个。</li>
<li><a href="https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf">PolarStar原始论文</a>：用于部分20–23度比较，具体代入见完整表和保存报告。</li>
</ul>
<p><a href="ddp/two_successful_methods_20261101/public_baseline_audit/CATALOG_D3_COMPARISON_SOURCES_20261101.json">31组D3公式与来源索引</a> · <a href="ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md">35度与旧65／70度的逐步推导</a></p>

<h2 id="novelty">四、如何确定先进性与创新性</h2>
<ol>
<li><strong>图是否正确：</strong>完整生成、最大度与全点对距离证明、独立验证及Lean支持合法性。</li>
<li><strong>是否提高最新已知下界：</strong>比较当前主表、作者公开包及适用论文构造推论，采用其中最强的已核保证。超过其中一个公式尚不足以认定全球领先。缺少来源的阈值应标待核。</li>
<li><strong>方法新增了什么：</strong>明确新连接规则、新兼容条件或新覆盖论证；判断是否已经被旧定理直接包含。换参数、增加复制次数和得到更多实例，通常不增加独立方法数。</li>
</ol>
<p>增加几个点可以构成有价值的新纪录，前提是比较可靠、完整图合法。点数很大、验证很完整、实例很多，都不能单独证明新颖性或最早归属。</p>
<div class="scroll"><table><thead><tr><th>目前的三项候选贡献</th><th>已有部分</th><th>值得专家判断的具体增量</th></tr></thead><tbody>
<tr><td><strong>54度56,862点仿射源</strong></td><td>Schreier控制器、仿射提升思想；一般完整邻域复制</td><td>六端口、八张真逆映射、相邻层十平面互补与C78词的同时兼容。它不是已核Delorme比较公式的直接代入；是否构成新构造族及其优先权仍待核。</td></tr>
<tr><td><strong>保持原degree上限的spread填补</strong></td><td>opposite-GQ源、spread存在性及一般扩张思想</td><td>incident-flag接针、余度分配和完整D3覆盖。关键原始JGT论文正文仍有缺口；目前既不能认定只是直接旧推论，也不能认证原创。</td></tr>
<tr><td><strong>diagonal连接重分配</strong></td><td>首个G1成立后，更高复制次数可用已有full-N复制规则</td><td>首个G1省去diagonal clone–filler连接、加入hub，并证明遗漏路线得到补齐。需要判断这条具体规则及一般证明的归属，后续degree端点不另计独立方法。</td></tr>
</tbody></table></div>
<div class="card caution"><strong>公开比较缺口会怎样影响“优势”：</strong><p>65–79度十五组共同的+50来自同一源填补；若同样填补及接口已发表，十五组优势会一起归零。86／90／94／98度的+70／74／78／82若扣除已经公开的同源填补，则只余+5／9／13／17；若相同新规则也已公开，则相应优势归零。未检索到相同规则，不能当作原创证明。</p></div>
<p>当前最值得专家审的是54度图的共同兼容机制、首个diagonal重分配规则，以及spread-fill在原始文献中的归属。D3新degree／复制倍数梯子已停止，避免以实例数量代替独立贡献。</p>
<p><a href="ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/PROOF.md">F9／C78完整证明</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md">diagonal一般规则与后续复制关系</a> · <a href="ddp/two_successful_methods_20261101/public_baseline_audit/SPREAD_FILL_SOURCE_PRIORITY_20261101.md">spread-fill精确归属缺口</a></p>

<h2 id="all-pairs">五、43组参数完整比较表</h2>
<p>“比较下界”表示本项目已核到的适用来源；整列不是全球最佳纪录。差额只相对该列。优先权与方法新颖性均未认证。</p>
<p><input id="filter" type="search" aria-label="筛选参数或来源" placeholder="筛选，如：54、主表、作者、待核"><span id="count">　43组</span></p>
<div class="scroll"><table id="all"><thead><tr><th>(Δ,D)</th><th>我们当前点数</th><th>已核比较下界</th><th>差额</th><th>证据类别</th><th>边界与来源</th></tr></thead><tbody>
__ROWS__
</tbody></table></div>
<p><a href="public_comparison_current.csv">下载43组CSV</a> · <a href="graph_catalog.html">全部152个合法图版本及原始材料</a> · <a href="progress.html">当前研究进展</a> · <a href="public_comparison_current.html.txt">本页完整HTML源码</a></p>
<p class="meta">本页整理已有结果和来源，没有重新生成图、执行BFS、编译Lean或重新认证全球纪录。数据与研究状态入口：<a href="ddp/two_successful_methods_20261101/STAGE_STATE.json">STAGE_STATE</a>。</p>
</main><script>
const filter=document.getElementById('filter');filter.addEventListener('input',()=>{const needle=filter.value.trim().toLowerCase().replaceAll(',','');let count=0;for(const row of document.querySelectorAll('#all tbody tr')){row.hidden=!row.textContent.toLowerCase().replaceAll(',','').includes(needle);if(!row.hidden)count++;}document.getElementById('count').textContent='　'+count+'组';});
</script></body></html>
'''
page = (page.replace('__NOW__', esc(now))
        .replace('__GRAPHS__', str(state['accepted_total_named_legal_instances']))
        .replace('__PAIRS__', str(state['accepted_total_parameter_pairs']))
        .replace('__LEAN__', str(state['complete_concrete_formula_Lean_instances']))
        .replace('__TARGET_ROWS__', '\n'.join(target_rows))
        .replace('__ROWS__', '\n'.join(body_rows)))
(OUT / 'public_comparison_current.html').write_text(page)
(OUT / 'public_comparison_current.html.txt').write_text(page)
print(json.dumps({'html': 'research/public_comparison_current.html',
                  'source': 'research/public_comparison_current.html.txt',
                  'comparison_rows': len(rows), 'bytes': len(page.encode())},
                 ensure_ascii=False))
