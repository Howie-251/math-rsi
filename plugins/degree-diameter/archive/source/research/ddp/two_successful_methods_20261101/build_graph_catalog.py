"""Render the requested graph list from saved construction records; no graph tests."""
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import csv
import html
import json
import os
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
STAGE = ROOT / 'research/ddp/two_successful_methods_20261101'
OUT = ROOT / 'research'
state = json.loads((STAGE / 'STAGE_STATE.json').read_text())
clone_lean_path = STAGE / ('retained_edge_transfer/published_d15_15552_D4_source_gate/'
                          'degree16_plane837/ROOT_FULL_LEAN_DISPOSITION.json')
clone_lean = json.loads(clone_lean_path.read_text())
clone_kernel_complete = clone_lean['status'] == (
    'ROOT_ACCEPTED_COMPLETE_ORIGINAL_SOURCE_AND_CLONE_KERNEL_AUDITS_EXTERNAL_BINDING')
family_path = ROOT / 'research/ddp/more_graphs_20261027/delivery/families.json'
families = json.loads(family_path.read_text())['families']
ledger = json.loads((ROOT / 'research-wiki/DDP_METHOD_LEDGER.json').read_text())
d3_comparisons = json.loads((STAGE / 'public_baseline_audit/'
    'CATALOG_D3_COMPARISON_SOURCES_20261101.json').read_text())['entries']
dominated = {(r['Delta'], r['D'], r['n']) for r in ledger['known_publicly_dominated_instances']}
files = [ROOT / p for p in subprocess.run(
    ['rg', '--files', 'research/ddp/more_graphs_20261027',
     'research/ddp/two_successful_methods_20261101', 'research/ddp/refresh_20261029'],
    cwd=ROOT, text=True, capture_output=True, check=True).stdout.splitlines()]
edge_by_n = defaultdict(list)
for p in files:
    m = re.search(r'n(\d+)\.(?:edges|edgelist)$', p.name)
    if m:
        edge_by_n[int(m[1])].append(p)

def rel(p):
    return str(Path(p).relative_to(ROOT)) if Path(p).is_absolute() else str(p)

def pick_edge(n, degree, diameter):
    candidates = [p for p in edge_by_n[n]
                  if re.search(r'(?:^|_)d' + str(degree) + r'(?:_|\.)', p.name)]
    return rel(min(candidates, key=lambda p: (len(str(p)), str(p)))) if candidates else ''

def comparison(d, D, n):
    if (d, D) == (13, 5):
        return '作者仓库报告88,452点；Comellas主表仍51,417（外部图未在本机重验）'
    if (d, D, n) in dominated:
        return '已知有更大的公开图'
    if (d, D) == (16, 4) and n in (16389, 16416):
        return f'本次已查公开主表16384：+{n - 16384}；全球优先权未确认'
    return '全球优先权未确认；历史基线比较见原记录'

rows = []
for degree, family in families.items():
    degree = int(degree)
    for step in family['steps']:
        n = step['new_n']
        evidence = step.get('source_evidence', rel(family_path))
        # Historical records sometimes append a JSON member selector after ':'.
        if not (ROOT/evidence).is_file():
            evidence = evidence.split(':', 1)[0]
        if not (ROOT/evidence).is_file():
            evidence = rel(family_path)
        rows.append(dict(degree=degree, diameter=5, vertices=n, edges=step['new_m'],
                         phase='早期D5连续扩张', mechanism='保留旧边、逐点加入完整R4覆盖邻域',
                         Lean='未完成', acceptance='逐步当前图完整R4；独立BFS仅限原记录中的检查点',
                         public_status=comparison(degree, 5, n),
                         edge_file=pick_edge(n, degree, 5), parameters=rel(family_path),
                         generator='research/ddp/more_graphs_20261027/delivery/family_generator.py',
                         evidence=evidence))

# Named terminal instances only; source reproductions and calibration graphs are excluded.
orders = set(state['new_validated_orders']) | {2016, 16389}
stage_edges = []
for p in files:
    if not p.is_relative_to(STAGE):
        continue
    m = re.fullmatch(r'(?:graph_)?d(\d+)_D(\d+)_n(\d+)\.edges', p.name)
    if m and int(m[3]) in orders:
        stage_edges.append((p, *map(int, m.groups())))
assert len(stage_edges) == state['new_graphs'], (len(stage_edges), state['new_graphs'])
metadata = {(r['Delta'], r['D'], r['n']): r for r in state['current_phase_representatives']}
for key in ['new_degree54_graph', 'new_degree55_graph', 'new_degree56_graph']:
    r = state[key]
    metadata[(r['Delta'], r['D'], r['n'])] = r

def recorded_edge_count(record, n):
    # Saved construction metadata supplies counts without opening graph files.
    for entry in [record, *record.get('graphs', [])]:
        if entry.get('n') == n:
            return entry['m']
        if entry.get('target_n') == n:
            return entry['target_m']
    raise ValueError(f'No saved edge count for {n}')

for p, degree, diameter, n in stage_edges:
    r = metadata.get((degree, diameter, n), {})
    params = next((q for q in [p.parent/'PARAMETERS.json', p.parent/'RESULT.json',
                              p.parent.parent/'PARAMETERS.json', p.parent.parent/'RESULT.json']
                   if q.exists()), STAGE/'STAGE_STATE.json')
    edge_count = r.get('m')
    if edge_count is None:
        edge_count = recorded_edge_count(json.loads(params.read_text()), n)
    text = str(p)
    if 'f4_c60_edge_projective' in text or 'f7_c60_d35' in text or n == 56862:
        mechanism = '小控制器×有限域坐标层'
    elif 'diagonal_fill_reallocation' in text:
        mechanism = '保留源图、重分配复制点连接与余度'
    elif 'opposite_gq' in text or 'even_q8_gq_source80_81' in text:
        mechanism = '有限几何源图填补／完整旧邻域复制'
    else:
        mechanism = '仿射源图的完整旧邻域复制'
    evidence = next((q for q in [p.parent/'ROOT_GRAPH_RELEASE.json',
                                p.parent/'independent_acceptance/NOTE.md',
                                p.parent/'independent_acceptance/SUMMARY.json',
                                p.parent.parent/'independent_acceptance/SUMMARY.json',
                                p.parent/'RESULT.json', p.parent.parent/'RESULT.json']
                     if q.exists()), STAGE/'REPORT.md')
    lean = '未完成' if n in {3900, 4125, 20580} else '完整具体图已完成'
    if n == 16389:
        lean = '完整具体图已完成' if clone_kernel_complete else '完整目标未完成；代表路线pilot已通过'
        if clone_kernel_complete:
            evidence = clone_lean_path
    if n == 16416:
        complete = state.get('new_degree16_D4_plane864_batch', {}).get('Lean_complete', False)
        lean = '完整具体图已完成' if complete else '新具体目标进行中；不继承16389证明'
        if complete:
            evidence = p.parent/'ROOT_FULL_LEAN_DISPOSITION.json'
    rows.append(dict(degree=degree, diameter=diameter, vertices=n, edges=edge_count,
                     phase='本阶段新增终图', mechanism=mechanism, Lean=lean,
                     acceptance='已接受；独立检验与完整距离证明的范围见原证据',
                     public_status=comparison(degree, diameter, n), edge_file=rel(p),
                     parameters=rel(params), generator='', evidence=rel(evidence)))

f5 = ROOT / 'research/ddp/refresh_20261029/f5_full_d20_D3'
rows.append(dict(degree=20, diameter=3, vertices=3750, edges=37500, phase='继承F5成功实例',
                 mechanism='30点四正则控制器×F5³', Lean='完整具体图已完成',
                 acceptance='完整图及独立验证已接受，证据范围见原记录',
                 public_status=comparison(20, 3, 3750),
                 edge_file=rel(f5/'graph_d20_D3_n3750.edges'), parameters=rel(f5/'PARAMETERS.json'),
                 generator=rel(f5/'generate.py'), evidence=rel(f5/'PROOF_AUDIT.md')))
rows.sort(key=lambda r: (r['degree'], r['diameter'], r['vertices']))
for r in rows:
    is13 = (r['degree'], r['diameter']) == (13, 5)
    r['public_source_order'] = 88452 if is13 else ''
    r['public_source_url'] = ('https://github.com/rmizuno42/ddp/blob/main/'
        'results/degree13-diameter5/README.md') if is13 else ''
    r['public_source_raw_url'] = ('https://raw.githubusercontent.com/rmizuno42/ddp/main/'
        'results/degree13-diameter5/README.md') if is13 else ''
    r['public_verification_scope'] = (
        '作者公开构造包与验证报告；本项目仅核读来源，未重新运行外部图验证') if is13 else ''
    r['comparison_lower_bound'] = ''
    r['margin_against_this_bound'] = ''
    r['comparison_formula'] = ''
    r['comparison_evidence_kind'] = ''
    r['comparison_secondary_URLs'] = ''
    r['comparison_audit_file'] = ''
    r['comparison_priority_note'] = ''
    c = d3_comparisons.get(f'{r["degree"]},{r["diameter"]}')
    if c:
        bound = c['comparison_lower_bound']
        margin = r['vertices']-bound
        comparison_text = (f'低于已核公式下界{bound:,}（差{-margin:,}）' if margin < 0 else
                           f'高于此公式下界{bound:,}，差额+{margin:,}' if margin > 0 else
                           f'达到公式下界{bound:,}')
        r.update(public_status=comparison_text+'；全球最高与优先权未确认',
                 public_source_order=bound, public_source_url=c['primary_urls'][0],
                 public_verification_scope=c['evidence_kind'], comparison_lower_bound=bound,
                 margin_against_this_bound=margin, comparison_formula=c['formula'],
                 comparison_evidence_kind=c['evidence_kind'],
                 comparison_secondary_URLs=' | '.join(c['primary_urls'][1:]),
                 comparison_audit_file=c['audit_file'], comparison_priority_note=c['priority_note'])
keys = {(r['degree'], r['diameter'], r['vertices']) for r in rows}
groups = defaultdict(list)
for r in rows:
    groups[(r['degree'], r['diameter'])].append(r)
assert len(rows) == len(keys) == state['accepted_total_named_legal_instances']
assert len(groups) == state['accepted_total_parameter_pairs']
assert sum(r['Lean'] == '完整具体图已完成' for r in rows) == state['complete_concrete_formula_Lean_instances']
for r in rows:
    for key in ['edge_file', 'parameters', 'generator', 'evidence']:
        if r[key]:
            assert (ROOT/r[key]).is_file(), (key, r[key])

with (OUT/'graph_catalog.csv').open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

def esc(value):
    return html.escape(str(value))

def link(path, label):
    return f'<a href="{esc(os.path.relpath(ROOT/path, OUT))}">{esc(label)}</a>' if path else ''

def links(r):
    return ' · '.join(x for x in [link(r['edge_file'], '边表'), link(r['parameters'], '参数'),
                                  link(r['generator'], '生成器'), link(r['evidence'], '证据')] if x)

def comparison_html(r):
    value = esc(r['public_status'])
    if r['public_source_url']:
        label = '原始论文' if r['comparison_formula'] else '作者原始说明'
        value += f'<br><a href="{esc(r["public_source_url"])}">{label}</a>'
        if r['public_source_raw_url']:
            value += f' · <a href="{esc(r["public_source_raw_url"])}">说明纯文本</a>'
    if r['comparison_formula']:
        value += f'<br><small>{esc(r["comparison_formula"])}</small>'
        value += ' · '+link(r['comparison_audit_file'], '适用条件与推导')
    return value

best = [max(v, key=lambda r: r['vertices']) for k, v in sorted(groups.items())]
summary = dict(graphs=len(rows), parameter_pairs=len(groups),
               complete_Lean=sum(r['Lean'] == '完整具体图已完成' for r in rows),
               early_D5=sum(r['phase'] == '早期D5连续扩张' for r in rows),
               inherited_F5=sum(r['phase'] == '继承F5成功实例' for r in rows),
               stage_new=len(stage_edges),
               literal_edge_files=sum(bool(r['edge_file']) for r in rows),
               prefix_generator_only=sum(not r['edge_file'] for r in rows))
clone_lean_summary = ('完整原目标、独立import审计与外部绑定已接受' if clone_kernel_complete
                      else '完整形式化仍在进行')
latest16 = state.get('new_degree16_D4_plane864_batch', {})
latest16_summary = ('新(16,4)16416图对本次已查主表16384多32点；' +
                    ('新具体Lean已完成' if latest16.get('Lean_complete') else '新具体Lean仍在进行')) if latest16 else (
                    '新(16,4)16389图对本次已查主表16384多5点，' + clone_lean_summary)
head = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>度直径图完整清单</title>
<style>body{max-width:1280px;margin:30px auto;padding:0 20px;font:16px/1.65 system-ui;color:#192b3c}table{border-collapse:collapse;width:100%}td,th{padding:9px;border-bottom:1px solid #dce3eb;text-align:left;vertical-align:top}th{background:#f0f5fa;position:sticky;top:0}a{color:#135fa6}input{padding:10px;width:min(560px,90%);font:inherit}.note{padding:15px;background:#edf4fb}.scroll{overflow-x:auto}small{color:#59697b}</style>
<h1>Degree/Diameter：已接受图的完整清单</h1>'''
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
parts = [head, f'<p>快照：{now}。本页由已接受的参数、图文件及验收记录生成；具体校验范围见各行证据。</p>',
         f'<div class="note"><strong>{summary["graphs"]}个具体图 · {summary["parameter_pairs"]}组参数 · '
         f'{summary["complete_Lean"]}个完整具体Lean实例</strong>'
         f'<p>{summary["early_D5"]}个早期D=5连续扩张版本＋原3750点F5实例＋本阶段{summary["stage_new"]}个终图。'
         '同一参数的不同点数版本分别列出；这些数字不代表独立方法数或已认证全球纪录数。'
         f'当前已认证全球优先权的新纪录为0；{latest16_summary}。</p></div>',
         f'<p><a href="graph_catalog.csv">下载全部{summary["graphs"]}行CSV</a> · <a href="graph_catalog.html.txt">完整HTML源码</a> · <a href="progress.html">研究进展</a> · <a href="public_comparison_current.html">公开比较与创新性说明（含43组表）</a></p>',
         f'<h2>每组参数当前点数最多的图（{summary["parameter_pairs"]}组）</h2><p>这是项目内部代表表；“点数最多”只比较本项目已接受实例。</p>',
         '<p>公开比较区分主表条目与作者仓库发布的构造报告。例如(13,5)主表仍为51,417，'
         '作者仓库另报告88,452；相应行已给原始链接。外部报告不等于本项目重新验证。</p>',
         '<p><strong>D3高degree各行的“公式下界”是本项目代入已发表方法所得，'
         '不是官方逐项纪录或全球最大值；没有逐个定位到相应数值边表。</strong>'
         '每行提供论文、代入公式和完整适用条件。65–79度的+50还受填补规则公开归属未决的限制；'
         '86/90/94/98度的+70/+74/+78/+82只相对4225Δ，若更强的填补源已公开，'
         '相对优势会缩至5/9/13/17。详见相应推导中的归属边界。</p>',
         '<div class="scroll"><table><thead><tr><th>(Δ,D)</th><th>点数</th><th>已存版本数</th><th>完整Lean</th><th>公开比较状态</th><th>原始材料</th></tr></thead><tbody>']
for r in best:
    parts.append(f'<tr><td>({r["degree"]},{r["diameter"]})</td><td>{r["vertices"]:,}</td>'
                 f'<td>{len(groups[(r["degree"],r["diameter"])])}</td><td>{esc(r["Lean"])}</td>'
                 f'<td>{comparison_html(r)}</td><td>{links(r)}</td></tr>')
parts += [f'</tbody></table></div><h2>全部具体图（{summary["graphs"]}个）</h2>',
          '<p>早期图逐步检查当前图完整R4覆盖，独立全根BFS仅限保存的检查点；后续图结合独立检验和完整证明。'
          '请点开“证据”查看实际范围。未保存单独边表的早期前缀，可用链接的生成器和字面参数复现。</p>',
          f'<label for="filter">筛选参数、点数、方法或状态：</label><br><input id="filter" type="search" placeholder="例如：16,4、2016、未完成、旧邻域"><p id="count">显示{summary["graphs"]}个图</p>',
          '<div class="scroll"><table id="all"><thead><tr><th>#</th><th>(Δ,D)</th><th>点数</th><th>边数</th><th>方法</th><th>Lean</th><th>原始材料</th></tr></thead><tbody>']
for i, r in enumerate(rows, 1):
    parts.append(f'<tr><td>{i}</td><td>({r["degree"]},{r["diameter"]})</td><td>{r["vertices"]:,}</td>'
                 f'<td>{r["edges"]:,}</td><td>{esc(r["mechanism"])}</td><td>{esc(r["Lean"])}</td><td>{links(r)}</td></tr>')
parts += ['</tbody></table></div>', '<script>const q=document.getElementById("filter");q.addEventListener("input",()=>{let n=0;const s=q.value.toLowerCase().replaceAll(",","");for(const r of document.querySelectorAll("#all tbody tr")){r.hidden=!r.textContent.toLowerCase().replaceAll(",","").includes(s);if(!r.hidden)n++}document.getElementById("count").textContent="显示"+n+"个图"})</script></html>']
page = '\n'.join(parts)
(OUT/'graph_catalog.html').write_text(page)
(OUT/'graph_catalog.html.txt').write_text(page)
print(json.dumps(summary, ensure_ascii=False))
print('Representatives:', [(r['degree'], r['diameter'], r['vertices']) for r in best])
