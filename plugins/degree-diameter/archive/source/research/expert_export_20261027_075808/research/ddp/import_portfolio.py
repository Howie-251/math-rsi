from pathlib import Path
import sys, shutil, re, json
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[2]
manifest=root/'.aris/installed-skills-codex.txt'
repo=Path(next(l.split('\t')[1] for l in manifest.read_text().splitlines() if l.startswith('repo_root\t')))
sys.path.insert(0,str(repo/'tools'))
import research_wiki as w
from capture_filter import screen
wiki=root/'research-wiki'; pkg=root/'context/DD_PORTFOLIO_START_20261026'
archive=root/'context/dd82/archive/portfolio_transition_20261026'; archive.mkdir(parents=True,exist_ok=True)
for rel in ['AGENTS.md','RESEARCH_BRIEF.md','research-wiki/query_pack.md','research-wiki/gap_map.md','context/dd82/NEXT_SESSION.md','research/progress.html']:
    src=root/rel; dst=archive/rel; dst.parent.mkdir(parents=True,exist_ok=True)
    if not dst.exists(): shutil.copy2(src,dst)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
goal='context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md'
current='''## 当前唯一执行入口 — DD Portfolio 2026-10-26

执行 context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md。范围4≤Δ≤12、D∈{3,4,5}，目标是超过最新公开下界的完整合法图；默认最多两条主机制。启动材料按实际原路径保留，不另复制第二套包或wiki。
以下所有DD82“当前/继续/唯一执行”均为历史记录，任务安排已暂停；n61谱、h5/h6、旧SAT及D=2不自动恢复。旧57≤N(8,2)≤61、已关闭范围、RAW缺口和Lean未完成状态保留。
唯一知识库research-wiki/；人工意见仍写入research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md。约每小时及重要发现更新research/progress.html；报告不是换题或暂停。新恢复入口context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md。

'''
p=root/'AGENTS.md'; s=p.read_text()
if '## 当前唯一执行入口 — DD Portfolio 2026-10-26' not in s: p.write_text(current+s)
brief='''# DD Portfolio research brief

## Problem Statement
范围4≤Δ≤12，D∈{3,4,5}。在27格选题池内按机制找超过最新公开下界的完整简单无向图。不要求全部27格或精确最优值。唯一执行入口context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md。

## Constraints
旧N(8,2)暂停，保留57≤N≤61及全部证据等级。默认最多两条主机制；无哈希。完整边表、独立全源距离检查；新成果Lean后置。每小时更新原research/progress.html，只报告真实进展，不按时钟换题。

## What I'm Looking For
M1小商图电压覆盖，比较M2非等长轨道或M3仿射中的一条；先有顶点、边、度数和完整覆盖条件，再选能跨越基线的参数。

## Existing Results (if any)
包内5张已知图是继承的准备期核验，零新纪录；非本次启动重跑。最新旧成果h7关闭、T≤34与λ_min(B)<−2及§7.19局部谱限制保留，旧原文和comments不撤回。来源、项目旧成果、本轮核验、提案分别记录。

## Background
启动包context/DD_PORTFOLIO_START_20261026/；原旧brief已保存在context/dd82/archive/portfolio_transition_20261026/RESEARCH_BRIEF.md。历史任务不成为并行队列。
'''
(root/'RESEARCH_BRIEF.md').write_text(brief)
p=wiki/'gap_map.md'; old=(archive/'research-wiki/gap_map.md').read_text()
p.write_text('''# Gap Map

Current phase: dd-portfolio-20261026. Only D=3/4/5 and 4≤Delta≤12 are active. Old DD82 tasks are paused, not solved.

- DDP1: No new lower bound yet. Find a complete graph above the current public record via small-base voltage coverage or one affine/nonuniform-orbit mechanism. Twelve initial entries and all27 baselines: ../context/DD_PORTFOLIO_START_20261026/SCOPE_AND_CASES.md.
- DDP2: Every proposed covering guarantee must hold jointly for all base endpoints and fiber targets. Degree/partial rank alone is insufficient. New objects need independent checks and then corresponding Lean.
- DDP3: Public baseline dates and local verification are distinct. Imported5 known graphs are preparation evidence, not discoveries or reexecutions in this session.

## Paused DD82 gaps and historical stage (not a task queue)

'''+old.replace('# Gap Map\n\n','',1))
for p in (wiki/'ideas').glob('dd82-*.md'):
    s=p.read_text()
    if '\nstage: active\n' in s:
        s=s.replace('\nstage: active\n','\nstage: archived\n',1).replace('**stage:** `active`','**stage:** `archived`',1)
        pos=s.find('\n# ')
        if pos>=0:
            end=s.find('\n',pos+1)
            s=s[:end]+ '\n\n执行状态：2026-10-26 PAUSED_BY_NEW_GOAL；保留原数学结果及未完义务。下方“当前/下一步”为历史，不派发任务。\n'+s[end:]
        p.write_text(s)
        w.append_log(str(wiki),f'Pause old execution without changing mathematical outcome: {p.name}')
# Four portable drafts, transformed through installed canonical writers; no claim birth.
def body(rel):
    s=(pkg/'wiki_import'/rel).read_text(); s=s.split('---',2)[2].strip(); s=s.split('\n',1)[1].strip()
    return s.replace('context/dd-portfolio-20261026/','context/DD_PORTFOLIO_START_20261026/')
def checked(s):
    hits=screen(s)
    if hits: raise RuntimeError(hits)
    return s
source_slug='ddp-record-sources-20261026'
sourcepath=wiki/'papers'/f'{source_slug}.md'
if not sourcepath.exists():
    p=w.ingest_paper(str(wiki),title='Table of Large Degree/Diameter Graphs',authors=['Francesc Comellas'],year=2026,venue='UPC maintained public table',thesis='Public record source map, snapshot2026-10-26; reports largest known graphs, not optimality. Reading depths retained.',tags=['ddp','degree-diameter','records'])
    s=p.read_text(); old_id=re.search(r'node_id: (.+)',s).group(1)
    s=s.replace(old_id,'paper:'+source_slug)
    sourcepath.write_text(s); p.unlink()
    w.append_log(str(wiki),'Converted canonical Comellas paper node to stable imported ddp-prefixed slug before linking.')
    with sourcepath.open('a') as f: f.write('\n## Imported source map and read depth\n\n'+body('papers/ddp-record-sources-20261026.md')+'\n\nSource URLs and read scope: [SOURCES_AND_METHODS](../../context/DD_PORTFOLIO_START_20261026/SOURCES_AND_METHODS.md). These reading claims belong to package preparation, not a new full-text review.\n')
items=[('ddp-open-parameter-construction-20261026','多参数度数—直径构造：让机制选择适合的参数','active','ideas/ddp-open-parameter-construction-20261026.md'),('ddp-counterexample-gates-20261026','在多参数构造中检验承重覆盖保证','active','ideas/ddp-counterexample-gates-20261026.md')]
for slug,title,stage,rel in items:
    exists=(wiki/'ideas'/f'{slug}.md').exists()
    p=w.upsert_idea(str(wiki),slug,title,stage=stage,outcome='pending',thesis=checked(body(rel)),risks='No complete new graph yet; partial coverage and finite subclass failure do not settle the original problem.',tags=['ddp'],based_on=['paper:'+source_slug,'paper:mizuno2026_new_lower_bounds','paper:przybocki2026_doubly_saturated_ramsey'],target_gaps=['DDP1' if slug==items[0][0] else 'DDP2'])
    if not exists:
        with p.open('a') as f: f.write('\n## Local provenance and inherited scope\n\n[PRIOR_WORK_LEDGER](../../context/DD_PORTFOLIO_START_20261026/PRIOR_WORK_LEDGER.md); [latest human comments](../DD82_PROGRESS_AND_COMMENTS_20261018.md).\n')
# No installed prior counterexample node exists: source draft remains linked, not invented.
p=wiki/'ideas/ddp-counterexample-gates-20261026.md'
with p.open('a') as f: f.write('\nLocal lookup found no pre-existing dd82-counterexample-guided-research wiki node. The historical U5 is preserved at [user snapshot](../../context/DD_PORTFOLIO_START_20261026/references/user_snapshots/dd82-counterexample-guided-research.md); its general method is imported here, its n61 queue stays paused.\n')
w.add_experiment(str(wiki),'ddp-known-baselines-20261026',title='继承准备期五张已知图的有限检查；零新纪录',idea=items[0][0],verdict='partial',confidence='high',date='2026-10-26',metrics='Known n=120,253,1100,2485,5334; imported reports say all roots checked by C++ BFS and independent Python bitsets. This session did not rerun them.',reasoning=checked(body('experiments/ddp-known-baselines-20261026.md')),provenance='context/DD_PORTFOLIO_START_20261026/validation/baseline_verification.json',tags=['ddp','inherited-known-baseline'])
for a,b,t,e in [('idea:'+items[0][0],'idea:'+items[1][0],'uses','Counterexamples test complete generating and covering promises.'),('idea:'+items[0][0],'idea:dd82-n61-global-closure-spectral','uses','Historical scope and failure memory only; old execution paused.'),('idea:'+items[1][0],'idea:dd82-polarity73-monotone-reduction','uses','Inherited lesson: relaxed screening is not joint completion; D2 exclusions are not D3-5 exclusions.'),('paper:'+source_slug,'paper:mizuno2026_new_lower_bounds','uses','Same existing paper reused; June lower bound is superseded numerically by current public table, not a new discovery.')]: w.add_edge(str(wiki),a,b,t,e)
comment=f'''\n\n## {now}：新 Goal 启动，旧 DD82 暂停\n\n用户明确要求导入后立即研究4≤Δ≤12、D∈{{3,4,5}}，不用再确认；每小时只报告、不强制换线。停止旧n61谱、h5/h6及SAT任务安排；本机进程检查未发现旧计算在运行。保留全部旧成果、失败和comments。改做M1小商图电压覆盖，并比较M2/M3选一条互补机制。\n\n实际合并4份草稿，使用安装manifest指向的ARIS helper、唯一research-wiki；未创建claim。补充启动包滞后项：h6恰一W及h7已闭；n61全域T≤34与λ_min(B)<−2、§7.19因子限制均按项目最新记录保留，57≤N≤61仍开放。§7.19不借用§7.15–7.18的Gemini回执。五图核验为准备期继承，非本会话发现。\n\n新入口：{goal}。旧brief、query、gap和HTML原样归档于context/dd82/archive/portfolio_transition_20261026/。来源代理只读原始公式；尚未运行新搜索、无新下界或Lean。\n'''
with (wiki/'DD82_PROGRESS_AND_COMMENTS_20261018.md').open('a') as f:f.write(comment)
next_text=f'''# DD Portfolio recovery\n\nUpdated {now}. ACTIVE goal: [RESEARCH_GOAL](RESEARCH_GOAL.md). Single wiki: ../../research-wiki/; read query_pack and latest primary comments. Import is complete; do not redo it or activate old n61 work.\n\nCurrent: M1 voltage sources for(6,3)/(7,4), plus comparison of M2/M3 for one second mechanism. Source notes research/ddp/m1_sources/ and research/ddp/second_mechanism/. Root is deriving joint voltage coverage and preparing bounded experiments. No new lower bound yet.\n\nBaseline snapshot is registry/cases.json, not a global latest guarantee. Five included known graphs have inherited preparation checks, not this run's results. Latest old h7/T34/spectral results remain preserved.\n\nApproximate hourly update to research/progress.html, and on significant evidence/comment. First update {now}; next active-work report due around one hour later. No timer promised. CPU first batch at most8 local workers total, memory comfortably below available; inspect actual live handles before resuming runs.\n'''
(pkg/'NEXT_SESSION.md').write_text(next_text)
p=root/'context/dd82/NEXT_SESSION.md'; old=(archive/'context/dd82/NEXT_SESSION.md').read_text(); p.write_text('# PAUSED — DD82 historical recovery\n\n2026-10-26: do not execute the historical next actions below. Current entry: [DD Portfolio](../DD_PORTFOLIO_START_20261026/NEXT_SESSION.md). Mathematical open states are preserved.\n\n'+old)
html=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Degree/Diameter 开放参数研究</title><style>body{{font:17px/1.65 system-ui;max-width:1050px;margin:35px auto;padding:0 20px;color:#17212c}}h1,h2{{line-height:1.3}}a{{color:#155bb2}}table{{border-collapse:collapse}}td,th{{padding:7px 14px;border:1px solid #ccd4db}}.note{{background:#eef5fa;padding:15px}}</style><h1>当前任务：按构造机制寻找新的度数—直径下界</h1><p>更新：{now}。范围 4≤Δ≤12，D∈{{3,4,5}}。Goal 持续进行；旧 N(8,2) 暂停。</p><div class="note"><strong>当前状态：尚无已验证新下界。</strong>已完成必要 Wiki 合并及任务入口切换，正在读取原始生成公式并推导覆盖条件。首次重点比较 (6,3)/(7,4) 的小商图电压覆盖，以及一条仿射或非等长轨道机制。</div><h2>当前数学问题</h2><p>小商图中的每条边携带纤维变换。度数由每个底点发出的真实边决定；直径还要求每种起终底点之间、长度不超过 D 的路线同时覆盖所有纤维位移。局部覆盖或单个满秩路线不能直接替代这个共同条件。</p><h2>基线和证据</h2><p>启动快照读取日期2026-10-26，Comellas表标注更新2026-10-25；活跃条目正在重新读取。12个优先入口及27格见<a href="../context/DD_PORTFOLIO_START_20261026/SCOPE_AND_CASES.md">范围表</a>。</p><table><tr><th>类别</th><th>实际状态</th></tr><tr><td>已知基线复现</td><td>继承准备期120、253、1100、2485、5334点五图核验；非本次新成果</td></tr><tr><td>新候选</td><td>尚未生成</td></tr><tr><td>已验证新下界</td><td>0</td></tr><tr><td>只关子族 / UNKNOWN</td><td>本轮尚无；旧记录按原范围保存</td></tr><tr><td>Lean</td><td>新数学发现之后开展，尚未开始</td></tr></table><h2>最近人工意见与实际改变</h2><p>按用户新Goal停止旧n61谱、分类和SAT安排；保留历史失败及最新h7、T≤34等成果。已把新范围写入AGENTS、研究brief、query_pack和恢复入口。每小时只汇报真实进展，不强制换题；报告后继续研究。</p><p><a href="../research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md">唯一人工意见记录</a> · <a href="../research-wiki/query_pack.md">Wiki当前入口</a> · <a href="../context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md">恢复入口</a> · <a href="../context/dd82/archive/portfolio_transition_20261026/research/progress.html">旧研究页面原样归档</a></p></html>'''
(root/'research/progress.html').write_text(html)
w.append_log(str(wiki),'Merged four DD portfolio drafts through installed helpers; new execution activated, DD82 paused with outcomes preserved. Source map stable slug conversion; package baseline evidence not rerun. Updated comments/navigation/HTML with original archives.')
w.rebuild_index(str(wiki)); w.rebuild_query_pack(str(wiki))
(root/'research/ddp/IMPORT_REPORT.md').write_text(f'''# Import completed {now}\n\n4 portable drafts merged into the existing wiki via installed ARIS helper. Source-map paper now paper:ddp-record-sources-20261026, two ddp idea nodes and one ddp known-baseline experiment. Existing Mizuno/Ramsey nodes reused. Historical counterexample note was only present as package U5; its general method linked in the ddp node. No claim status minted.\n\nNewest local old results take precedence over earlier package snapshots: h7 fully closed; T≤34 and λ_min(B)<−2, §7.19 local factor restrictions preserved. Original evidence/RAW gaps unchanged. No old job found in process inspection.\n\nOriginal UI/brief/gaps/recovery saved at context/dd82/archive/portfolio_transition_20261026/. New goal and comments are linked by research/progress.html and generated query_pack. Resource inspection:128 visible CPUs, about1.4TiB available memory,391GiB free disk; this is shared hardware, initial budget≤8 CPU workers, no large search yet.\n''')
print('IMPORT_COMPLETE',now)
