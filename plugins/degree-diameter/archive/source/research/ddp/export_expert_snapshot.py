"""Export a self-contained expert HTML source and a portable local source bundle."""
from pathlib import Path
from datetime import datetime, timezone
from html import escape
import json
import shutil
import zipfile
import runpy

ROOT = Path(__file__).resolve().parents[2]
STAMP = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
EXPORT = ROOT/'research'/f'expert_export_{STAMP}'
EXPORT.mkdir()
DOWNLOAD = Path('/mnt/data')
DOWNLOAD.mkdir(exist_ok=True)
ledger = json.loads((ROOT/'research-wiki/DDP_METHOD_LEDGER.json').read_text())
rows = ledger['rows']
m = runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))

parts = [f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Degree/Diameter 专家审阅材料 {NOW}</title><style>
body{{font:16px/1.7 system-ui,sans-serif;max-width:1200px;margin:32px auto;padding:0 20px;color:#18232f}}h1,h2,h3{{line-height:1.35}}a{{color:#155bb2}}table{{border-collapse:collapse;width:100%;margin:16px 0}}th,td{{border:1px solid #cbd4dd;padding:10px;text-align:left;vertical-align:top}}.notice{{padding:18px;background:#edf4fb;border-left:4px solid #386db0}}.scroll{{overflow:auto}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#f5f7f9;padding:14px;font-size:13px}}details{{margin:12px 0;border:1px solid #dce2e7;padding:10px}}summary{{cursor:pointer;font-weight:600}}code{{overflow-wrap:anywhere}}small{{color:#56606c}}@media print{{details{{display:block}}summary{{font-weight:bold}}}}
</style></head><body><h1>Degree/Diameter 构造研究：专家审阅快照</h1>
<p>导出：{NOW}。本文件就是可编辑的完整HTML源码，浏览器可直接离线打开；正文、表格与已试方法记录均在文件内，无需本项目目录、网络或外部脚本。配套ZIP另含报告、构造代码、参数、保存边表和核验记录。</p>
<div class="notice"><strong>目前已验证新下界：0。</strong>目标仍是4≤Δ≤12、D∈{{3,4,5}}的完整简单无向图，超过相应最新公开下界。下文基线是2026-10-26保存快照，不是一般图上界。坏对减少、必要条件通过、来源恢复或有限族排除均不记作新下界。</div>
<h2>目前怎样选择构造，以及真正的不足</h2>
<p>先用完整顶点/边规则得到n和degree预算，再与目标基线和必要短路容量比较。已有正向路由定理时列出其覆盖范围；缺少全局保证时只做明确的有限试验。目前度数、阶数和若干容量障碍可严格检查，但很多候选的正向覆盖直觉仍偏弱。超过门槛、未被必要界排除、便于实现，都不足以证明它比其他构造更值得投入。</p>
<p>按用户要求扩大有实质区别的机制比较；同一失败模板不因坏对下降而追加seed、邻域或时间。逐方法结果、未闭范围与重启依据进入唯一Research Wiki，避免上下文压缩后重复。现有{len(rows)}条记录包括变体、控制器、工具与来源恢复，不等于{len(rows)}种独立方法。</p>
<h2>最新一轮的实际结果</h2><div class="scroll"><table><tr><th>入口</th><th>参数与正向依据</th><th>实际结果及边界</th></tr>
<tr><td>已知图删边降度</td><td>170点7度D3→6度；253点8度D3→7度。</td><td>唯一三步最短路分别强迫全部595/1012边保留；固定两源任意spanning删边均失败。没有展开删边搜索，不排除一般目标图。</td></tr>
<tr><td>线性码syndrome图</td><td>V=Fq^r，以H各projective列的非零倍数为生成步；n=q^r，degree=s(q−1)，diam为covering radius。</td><td>同方向重复步可合并，球界Σ C(s,j)(q−1)^j已使全部27格不过保存基线；495个算术参数比较，无矩阵/图搜索。与abelian Cayley相关，不虚增独立方法数。</td></tr>
<tr><td>72控制点×F2⁴逐边仿射线</td><td>n1152、degree8，目标D4、L1100。144边各自可逆线性映射+非零方向+offset；不同于已排除的四全局标签通用chart。</td><td>两固定起点各1000提案完成；独立全1152根确认D5、29152个&gt;4无序对。468个控制点有序槽恰有一条四步walk，必须逐条满秩；仍未全部满足。有限profile失败，不排除整个逐边模型。</td></tr>
<tr><td>W(3,5) incidence加两侧2-factor</td><td>156点+156线，n312、degree8，目标D3、L253。936条incidence全保留，所有异侧点对原本≤3；每侧添加156边2-factor。</td><td>两固定起点各1000合法交换完成；独立全312根确认D4、4090个&gt;3无序对。只剩同侧原远端覆盖未闭；一般2-factor组合未排除。</td></tr>
</table></div>
<h2>希望专家直接判断的数学问题</h2><ol>
<li>哪些生成机制能给出真正的全局覆盖保证，而不只满足阶数、degree与Moore/短路容量？当前选题依据中有哪些明显应停止的套路？</li>
<li>对72×F2⁴模型，468个唯一四路槽的rank4要求能否与144条边的逆一致性共同满足？是否有不依赖四全局标签的几何障碍，或合适的代数连接可同时满足这些约束？</li>
<li>对W(3,5)两侧2-factor模型，能否用一个设计/极性/自动同构规则保证全部同侧非共线点对三步可达？若不能，能否由精确覆盖矩阵给出统一障碍，指导更换结构而非增加交换？</li>
<li>已试结果中哪些失败原因可转成一个更强的构造规则？哪些只是局部最小，既不能证明无解，也没有继续加预算的正向理由？</li></ol>
<h2>怎样读目标距离</h2><p>实际D超过目标、普通无序坏对、NB有序缺项、代表状态缺项及理论容量不足分别保留；不合并成一个分数。控制图与条件性大图不跨层比较。37630点双新点方案只核两个新根，25是新旧点对缺项，不能写成全图全源坏对。UNKNOWN不等于不可行。旧D2/n61材料是暂停历史。</p>
<h2>逐方法记录</h2><p>以下为唯一Wiki的当前记录导出。每项保留目标、对象层级、实际/假设阶数、距离证据、停止范围、启发和从属变体。使用浏览器查找可按群、点数、参数或机制定位。</p>''']

families = sorted({r['method_family'] for r in rows})
for family in families:
    parts.append('<h3>'+escape(family)+'</h3>')
    for r in rows:
        if r['method_family']!=family:
            continue
        detail = {k:r[k] for k in ['goal','object_level','actual_order','hypothetical_order','actual_degree','actual_diameter','diameter_scope','bad_pair_count','bad_pair_count_type','other_metrics','status','exact_scope','positive_guarantees','remaining_gap','lesson','restart_condition','variants','evidence_paths']}
        parts.append('<details class="method" id="'+escape(r['id'])+'"><summary>'+escape(r['title'])+'</summary><p><strong>目标与对象：</strong>'+escape(m['goal_text'](r))+'</p><p><strong>距离：</strong>'+escape(m['gap_text'](r))+'</p><p><strong>范围与启发：</strong>'+escape(str(r['exact_scope'])+'；'+str(r['lesson']))+'</p><pre>'+escape(json.dumps(detail,ensure_ascii=False,indent=2))+'</pre></details>')

parts.append('<h2>最新构造源码与核验记录</h2><p>以下代码与结果也直接嵌入HTML，可离线查看；ZIP保留原路径便于复算。无需执行任何文件即可阅读。</p>')
wave10 = ROOT/'research/ddp/breadth_20261027_wave10'
for dirname in ['degree_reduction_scout','new_structure_scout','binary1152_edge_local','gq312_internal_cycles']:
    directory = wave10/dirname
    files = sorted(p for p in directory.iterdir() if p.suffix in {'.py','.cpp','.md'} or p.name in {'terminal.json','RESULT.json','best.independent_check.json'})
    for path in files:
        if path.stat().st_size<=300_000:
            parts.append('<details><summary>'+escape(str(path.relative_to(ROOT)))+'</summary><pre>'+escape(path.read_text())+'</pre></details>')
parts.append('<p><small>本文件是导出快照，不是第二个Wiki。唯一长期知识库仍是原项目research-wiki/。最新正式成果仍需公开基线刷新、独立验证、规定审阅与对应Lean；当前没有可登记的新下界。</small></p></body></html>')
html = '\n'.join(parts)
assert not m['capture'].screen(html)
(EXPORT/'EXPERT_REVIEW.html').write_text(html)
(EXPORT/'EXPERT_REVIEW.html.txt').write_text(html)
readme = f'''# 专家材料使用说明

导出时间：{NOW}。

1. 双击EXPERT_REVIEW.html可离线阅读完整说明、方法记录及最新构造代码。
2. EXPERT_REVIEW.html.txt与HTML逐字相同，供文本编辑器/其他模型复制源码。
3. research-wiki/DDP_METHOD_LEDGER.md与.json为当前账本导出；experiments/是逐项节点。
4. research/ddp/保留相关报告、可用构造源码、参数、边表和独立核验结果的原路径；context/含Goal与恢复状态。

已验证新下界仍为0。保存基线日期2026-10-26，未声明新纪录。普通坏对、控制器缺项、理论容量与两新根局部核验的口径分开。

本包用于专家讨论，不是完整环境镜像；不包含编译后的可执行文件、大型运行缓存和全部第三方原始附件。复算时以各报告中明确的输入范围和现有依赖为准。旧03:15专家包保持原样，本包是新的当前快照。
'''
(EXPORT/'README.txt').write_text(readme)

files = set()
def add(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT/path
    if not path.is_file() or path.stat().st_size>16*1024*1024:
        return
    if path.suffix not in {'.md','.json','.py','.cpp','.h','.txt','.edges','.html'}:
        return
    if any(s in path.name.lower() for s in ['sha256','checksum','manifest']):
        return
    if path.suffix in {'.py','.cpp','.h'} and any(s in path.read_text(errors='replace') for s in ['hashlib','SHA256SUMS']):
        return
    files.add(path)

for r in rows:
    add(r['wiki_path'])
    for raw in r['evidence_paths']:
        path = ROOT/raw
        add(path)
        directory = path if path.is_dir() else path.parent
        if directory.is_dir():
            for sibling in directory.iterdir():
                add(sibling)
for path in wave10.rglob('*'):
    add(path)
for raw in ['research-wiki/DDP_METHOD_LEDGER.md','research-wiki/DDP_METHOD_LEDGER.json','RESEARCH_BRIEF.md','research/progress.html','context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md','context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md','context/DD_PORTFOLIO_START_20261026/registry/cases.json']:
    add(raw)
for path in files:
    target = EXPORT/path.relative_to(ROOT)
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(path,target)

name = 'DD_EXPERT_CURRENT_'+STAMP
archive = ROOT/'research'/(name+'.zip')
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for path in sorted(EXPORT.rglob('*')):
        if path.is_file():
            z.write(path,path.relative_to(EXPORT))
for source, target in [(EXPORT/'EXPERT_REVIEW.html',DOWNLOAD/(name+'.html')),
                       (EXPORT/'EXPERT_REVIEW.html.txt',DOWNLOAD/(name+'.html.txt')),
                       (archive,DOWNLOAD/(name+'.zip'))]:
    shutil.copyfile(source,target)
project_copy = ROOT/'expert_review_current'
project_copy.mkdir(exist_ok=True)
for source, filename in [(EXPORT/'EXPERT_REVIEW.html','EXPERT_REVIEW.html'),
                         (EXPORT/'EXPERT_REVIEW.html.txt','EXPERT_REVIEW.html.txt'),
                         (archive,'EXPERT_REVIEW.zip'),
                         (EXPORT/'README.txt','README.txt')]:
    shutil.copyfile(source,project_copy/filename)
print(json.dumps(dict(snapshot_UTC=NOW,records=len(rows),html=str(DOWNLOAD/(name+'.html')),
    html_source=str(DOWNLOAD/(name+'.html.txt')),bundle=str(DOWNLOAD/(name+'.zip')),
    project_directory=str(project_copy),bundle_bytes=archive.stat().st_size,source_files=len(files)),ensure_ascii=False))
