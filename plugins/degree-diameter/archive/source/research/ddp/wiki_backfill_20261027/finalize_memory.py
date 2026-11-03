"""Finish the user-requested persistent research record; no graph work."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import json
import runpy
import shutil

WORK = Path(__file__).resolve().parent
ROOT = WORK.parents[2]
m = runpy.run_path(str(WORK/'sync_ledger.py'))
helper, capture = m['helper'], m['capture']
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def write(path, text):
    assert not capture.screen(text), path
    (ROOT/path).write_text(text)

def update_rollup(slug, old, new):
    path = ROOT/'research-wiki/experiments'/f'{slug}.md'
    text = path.read_text()
    meta = helper._load_paper_frontmatter(path)
    metrics = text.split('## Metrics\n',1)[1].split('\n## Reasoning',1)[0].strip()
    reasoning = text.split('## Reasoning\n',1)[1].split('\n## Connections',1)[0].strip()
    reasoning = reasoning.replace(old, new)
    reasoning += '\n\n本节点为整轮历史索引；逐构造的目标差距、证据和重启条件见 [统一方法账本](../DDP_METHOD_LEDGER.md)。'
    assert not capture.screen(reasoning)
    helper.add_experiment(str(ROOT/'research-wiki'), slug=slug, title=meta['title'],
        idea=meta['idea_id'], verdict=meta['verdict'], confidence=meta['confidence'],
        date=meta['date'], hardware=meta['hardware'], duration=meta['duration'],
        metrics=metrics, reasoning=reasoning, provenance=meta['provenance'],
        tags=json.loads(meta['tags']), update_on_exist=True)

with (WORK/'memory_finalize.log').open('w') as log, contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
    update_rollup('ddp-wave7-matching-signing-20261027',
        '新的171单点插入仅为待执行提案，不记成实际试验。',
        '在第七轮截点171单点插入尚为提案；后续第八轮已执行完全部34930665原始三边组、32846935合法matching，二步支配通过0。保存fallback独立全171根BFS为D4、79个>3无序坏对（11新旧、68旧旧）；不是一般171图排除。详见 [后续终态节点](ddp-wave8-insertion171.md)。')
    update_rollup('ddp-wave4-global-geometry-and-record-cover-20261027',
        'New three-step source supplies all18 localF3 patterns, but31controller/global certificate remain open.',
        'New three-step source supplies all18 localF3 patterns, but31controller/global certificate remain open. 后续澄清：旧增阶报告的8指8个固定起点，不是8pins；37628/42342单新点已经分别用满11/12pins。不能把此数当成尚未使用的度预算。')

nextpath = ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md'
old = nextpath.read_text()
historical = old[old.index('## Latest checkpoint: wave7'):].replace('## Latest checkpoint: wave7', '## Historical06:40 checkpoint: wave7',1)
current = f'''# DD Portfolio — current recovery state

Updated {NOW}. Goal ACTIVE, zero new lower bounds. Execute RESEARCH_GOAL.md. Old D2/N(8,2)/n61/SAT/spectral/Lean remain paused. At most two principal mechanisms and eight CPU workers. No hashes.

## Latest checkpoint: persistent method ledger completed

用户要求每个已试方法连同到目标的距离及时进入唯一Wiki，防止上下文压缩后重走旧路。已完成： [方法账本](../../research-wiki/DDP_METHOD_LEDGER.md) / [机器字段](../../research-wiki/DDP_METHOD_LEDGER.json)。共148条记录、35个机制家族标签；87个旧节点更新，61个逐项节点新增。包含变体、控制器、来源、工具，不称148种独立方法。第2–9轮62个实际试验主目录全部覆盖；1项已有节点复用。旧DD82留在同一Wiki作暂停历史。

恢复时先读账本说明及家族目录，再按机制、参数和固定范围检索相关条目。每批收束立即用canonical helper同步逐项节点和账本；记录target、baseline日期、实际/假设n、实际D、坏对计数类型、验证范围、停止原因、启发及重启条件。UNKNOWN、无图、控制器和最终图不得混为一谈。旧open/pending只是当时历史，不是自动重跑队列；若有superseding节点须先读后续。

## Latest math terminal results (wave8–9)

- insertion171：(7,3)，保存L170。枚举34930665原始三边组、32846935合法matching，二步支配通过0，最少新根漏11。fallback选最小新根漏而非全局bad最优；独立全171根BFS D4、79无序>3=11新旧+68旧旧。此固定插入族已排除，一般171图开放。
- Menon1296：(8,4)，保存L1100。保方向类子族有统一>=155520个B-C坏对障碍；未生成screen图。完整S36放宽2seed各1000incidence transpositions，最好图独立全1296根BFS D5、69737无序>4（AA91/AB2296/AC15253/BB7595/BC40661/CC3841）。有限profile停止，一般S36族开放。
- cooperative37630：(11,5)，保存L37628。保留旧205296边，新增互连两点各10pins，共21新边、max11。两固定初始化，各最多两完整坐标sweep；best新旧漏25=A10+B15。root独立核边表及两个新根BFS，ecc6/ecc6、25点号MATCH；没有全37630根BFS，actualD和全图普通bad字段留null，只报告已证D>=6及两根口径。旧源D5复用。最佳一坐标局部最小不排除一般双点模板；已停止，不加sweep/MILP/newnode/source。

旧增阶报告“8”是8个起点方案，旧37628/42342单点实际上已用满11/12pins，不是8pins。完整R3/R4缓存和上述边表/证据在wave9/cooperative37630/。所有有限数学批次已终态，没有后台搜索；不要将已派发或已结束描述成在途。

Current live page research/progress.html；expert03:15:51 HTML/MD/ZIP保持冻结，不覆盖。RESEARCH_BRIEF与gap_map已同步，query_pack由helper重建。最新实际Gemini接受范围仍是固定192点保旧边补度的NB5局部障碍；wave8/9无新Gemini回执，不称全审通过。新下界0、无新Lean验收。下次选机制须先说明已知覆盖保证和新瓶颈，不原样追加失败预算。

'''
write('context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md', current+historical)

comments = ROOT/'research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md'
text = comments.read_text()
text = text.replace('Goal **ACTIVE**，当前主力n61统一约束与真实共同实现。',
    'Goal **ACTIVE**，当前任务为Degree/Diameter Portfolio（4≤Δ≤12，D=3/4/5）；旧n61与D2任务已暂停。当前逐方法状态见 [方法账本](DDP_METHOD_LEDGER.md)。',1)
heading = '## 2026-10-27 人工意见：每种已试方法及目标差距及时更新Research Wiki'
if heading not in text:
    text += f'''\n\n{heading}

用户原话：“现在我们尝试过的方法，有没有及时update到research wiki里面，毕竟每次都会重新压缩上下文，我们要把尝试过的再并上与目标图的距离一并放到research wiki里面，既避免不走重复路，也可以拿一些新启发”。

落实于{NOW}：原来整轮汇总不足以代替逐构造记录，现补齐 [统一方法账本](DDP_METHOD_LEDGER.md) 和 [结构化字段](DDP_METHOD_LEDGER.json)，148条实验/变体/来源等记录（非独立方法数），35个家族标签，87旧节点更新、61新增。第2–9轮62个主目录全部覆盖；嵌套变体并入父项。记录目标与保存基线日期、实际/假设n、直径与坏对类型、验证范围、停止原因和重启依据。

已区分普通无序坏对、NB有序缺项、容量障碍和两新根的25个新旧点对；控制器不与最终图跨层算差距，UNKNOWN不记不可行。AGENTS/brief/gap map/query pack/NEXT_SESSION均建立账本优先检索入口；每批终态即同步，历史open不是自动续跑许可。数学新下界仍为0；本次回填未重跑图实验。当前171 D4/79、1296 D5/69737、37630只两根ecc6/新旧25，详见节点证据。
'''
write('research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md', text)

archive = ROOT/'research/progress_ddp_20261027_0640.html'
if not archive.exists():
    shutil.copyfile(ROOT/'research/progress.html', archive)
html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Degree/Diameter 研究进展</title><style>body{{font:17px/1.65 system-ui;max-width:1080px;margin:36px auto;padding:0 20px;color:#17212c}}h1,h2{{line-height:1.3}}a{{color:#155bb2}}table{{border-collapse:collapse;width:100%}}td,th{{padding:9px;border:1px solid #ccd4db;text-align:left;vertical-align:top}}.note{{background:#eef5fa;padding:16px}}.table-wrap{{overflow-x:auto}}code{{overflow-wrap:anywhere}}</style></head><body>
<h1>构造结果与Research Wiki已同步</h1><p>更新：{NOW}。Goal ACTIVE，4≤Δ≤12、D∈{{3,4,5}}。<strong>已验证新下界仍为0。</strong>基线是保存的2026-10-26快照。</p>
<div class="note">已补齐逐方法账本：148条记录、35个机制家族标签，87旧节点更新、61新增；第2–9轮62个试验主目录全部覆盖。记录含变体、控制器、来源与工具，不等于148种独立方法。<p><a href="../research-wiki/DDP_METHOD_LEDGER.md">方法、目标差距、失败启发与原始证据</a> · <a href="../research-wiki/DDP_METHOD_LEDGER.json">结构化完整字段</a></p></div>
<h2>最近的完整结果</h2><div class="table-wrap"><table><thead><tr><th>构造</th><th>目标</th><th>结果与距离</th><th>范围</th></tr></thead><tbody>
<tr><td>170→171单点插入</td><td>Δ≤7，D≤3；L170</td><td>保存fallback D4，79个无序坏对=11新旧+68旧旧</td><td>全部32846935合法三边matching均不满足新根必要二步支配。固定族停止，一般171图未排除。<a href="../research-wiki/experiments/ddp-wave8-insertion171.md">节点</a></td></tr>
<tr><td>Menon1296方向类筛选</td><td>Δ8，D≤4；L1100</td><td>保类族理论至少155520个B-C坏对；未生成候选图</td><td>先发现不变量再停止，完整S36放宽另列。<a href="../research-wiki/experiments/ddp-wave8-menon1296-screen.md">节点</a></td></tr>
<tr><td>Menon1296完整S36放宽</td><td>Δ8，D≤4；L1100</td><td>最好图独立全源D5，69737个无序坏对</td><td>两固定seed各1000交换完成；一般S36族开放，不原样续预算。<a href="../research-wiki/experiments/ddp-wave8-menon1296-unrestricted.md">节点</a></td></tr>
<tr><td>37628→37630双点互助</td><td>Δ≤11，D≤5；L37628</td><td>两新根ecc6，A漏10、B漏15，共25个新旧点对</td><td>保全部旧边；各10pins。只核两新根并复用旧源D5，未测全图普通坏对；有限坐标profile停止。<a href="../research-wiki/experiments/ddp-wave9-cooperative37630.md">节点</a></td></tr>
<tr><td>650加完美匹配</td><td>Δ6，D≤4；L441</td><td>独立全源D5，31918个无序坏对</td><td>10000合法交换结束，一般matching存在性仍开放。<a href="../research-wiki/experiments/ddp-wave7-shortcut650.md">节点</a></td></tr>
</tbody></table></div>
<h2>保留下来的启发</h2><p>应先筛唯一短路、端点容量和方向类不变量；它们失败时需要改变路由结构。局部满秩仍需所有控制点之间的全局覆盖。R4/R3双点互助有独立覆盖条件，但目前25项残缺只说明该有限profile未成功。旧报告“8”是8个起点，并非8pins；旧单点方案已经用满11/12邻居。</p>
<p>每批收束即更新逐项Wiki，压缩恢复先读账本说明与家族目录，再检索对应参数。所有当前有限试验已终态，没有后台数学搜索；本次记忆整理由三个subagent分工核旧记录、目录覆盖与指标口径，主代理统一写入。最近实际Gemini接受仅覆盖固定192点NB5保旧边补度障碍，wave8/9没有新互审回执。</p>
<p><a href="progress_ddp_20261027_0640.html">上一阶段进展页</a> · <a href="../context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md">恢复入口</a> · <a href="expert_review_20261027/STATUS.html">冻结的专家说明03:15:51</a></p><p>专家HTML/MD/ZIP保持原截点；旧D2/n61/SAT与Lean继续暂停。没有新的Lean验收。</p></body></html>'''
write('research/progress.html', html)
print('Updated rollup corrections, recovery state, primary user comment record, and progress HTML.')
