"""Archive Q6 scientific evidence without mutating its originals."""
from pathlib import Path
import argparse, ast, collections, datetime, hashlib, html, json, os, re, shutil, subprocess, sys, time, urllib.request, zipfile

SRC=Path('E:/新问题')
DEST=Path('D:/Ruskey–Savage 猜想n=6')
ARIS=Path('F:/c4free-hypercube-main/ARIS')
ROOT_ID='01a1927c-031a-7331-bec9-341615c84a96'
OMIT={'__pycache__','.git','.venv','node_modules','edge-profile-cdp','edge-profile-seminar','edge-profile','edge-profile-mobile'}
def excluded(p):return any(x in OMIT or x.startswith('edge-profile') for x in p.parts)
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def write(n,s):
 p=DEST/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def js(n,d):write(n,json.dumps(d,ensure_ascii=False,indent=2))
def copytree(a,b):
 for p in a.rglob('*'):
  rel=p.relative_to(a)
  if excluded(rel) or not p.is_file() or p.is_symlink():continue
  q=b/rel;q.parent.mkdir(parents=True,exist_ok=True)
  if q.exists() and q.stat().st_size==p.stat().st_size and q.stat().st_mtime_ns==p.stat().st_mtime_ns:continue
  shutil.copy2(p,q)
def download(url,p):
 try:
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=25) as r:p.write_bytes(r.read())
  if p.suffix=='.pdf' and not p.read_bytes().startswith(b'%PDF'):raise ValueError('not PDF')
  return {'url':url,'file':p.relative_to(DEST).as_posix(),'status':'saved','sha256':digest(p)}
 except Exception as e:
  if p.exists():p.unlink()
  return {'url':url,'status':'unavailable','error':str(e)}

def build():
 DEST.mkdir(parents=True,exist_ok=True)
 print('Copy scientific evidence',flush=True)
 copytree(SRC/'research',DEST/'research')
 for p in SRC.iterdir():
  if p.is_file() and p.suffix in {'.md','.html','.pdf'}:shutil.copy2(p,DEST/p.name)
 print('Copy ARIS framework snapshot',flush=True)
 copytree(ARIS,DEST/'ARIS_framework')
 plan='''# Q6 self-contained research archive plan

**Goal:** Preserve the complete Q6 proof/evidence/search/ARIS history and an offline presentation portal.

**Architecture:** Keep scientific files at original relative paths; add searchable metadata and visible execution traces; preserve originals and perform verification only in a disposable working copy.

**Scope:** Known published theorems remain explicit mathematical imports. Offline readability and certificate binding checks are distinguished from rebuilding every search and from formal proof verification.

- [x] Snapshot scientific files and the ARIS framework.
- [x] Export relevant visible messages, tool calls and tool outputs, excluding hidden reasoning and global account configuration.
- [x] Include local papers where obtainable and record missing sources.
- [x] Add portable verifier, inventories, replay guidance and offline HTML portal.
- [ ] Hash every packaged file; compare copied scientific files against source.
- [ ] Rerun the final P6 checker in an isolated copy rooted in this package.
- [ ] Render and check the offline portal and proof pages.
'''
 write('PACKAGING_PLAN.md',plan)
 # Export only the research thread and its explicit descendants.
 candidates=json.loads((SRC/'research/six_directions/report_tools/session_candidates.json').read_text(encoding='utf-8'))
 ids={ROOT_ID};selected=[]
 for _ in range(len(candidates)+1):
  old=len(ids)
  for d in candidates:
   src=d.get('source') or {};sub=src.get('subagent',{}) if isinstance(src,dict) else {}
   parent=sub.get('thread_spawn',{}).get('parent_thread_id')
   if parent in ids:ids.add(d['id'])
  if old==len(ids):break
 # Current continuation explicitly named in the current workspace history.
 ids.add('01a19edb-db42-7843-8586-408e78cc49a9')
 turns=[];tools=[];sessions=[]
 for d in candidates:
  if d['id'] not in ids:continue
  p=Path(d['file']);sid=d['id'];out=[];meta={k:d.get(k) for k in ('id','cwd','source','bytes')}
  with p.open(encoding='utf-8') as f:
   for line in f:
    try:e=json.loads(line)
    except ValueError:continue
    kind=e.get('type');v=e.get('payload',{});typ=v.get('type');record=None
    if kind=='session_meta':meta['timestamp']=v.get('timestamp');continue
    if kind=='response_item':
     if typ=='message' and v.get('role') in ('user','assistant') and v.get('channel') not in ('analysis','summary'):
      text='\n'.join(c.get('text','') for c in v.get('content',[]) if c.get('type') in ('input_text','output_text','text'))
      if not text:continue
      record={'kind':'message','role':v.get('role'),'channel':v.get('channel'),'text':text}
     elif typ in ('function_call','function_call_output','custom_tool_call','custom_tool_call_output'):
      record={'kind':typ,**{k:v[k] for k in ('name','call_id','arguments','input','output') if k in v}}
    if record:
     record={'timestamp':e.get('timestamp'),'session_id':sid,**record};out.append(record)
     if record['kind']=='message':turns.append(record)
     else:tools.append(record)
  if not out:continue
  write(f'trajectories/sessions/{sid}.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in out))
  transcript=[f'# Visible trajectory {sid}',f'Parent/source: `{json.dumps(meta.get("source"),ensure_ascii=False)}`']
  for e in out:
   if e['kind']=='message':transcript += [f'\n## {e["timestamp"]} · {e["role"]}',e['text']]
  write(f'trajectories/transcripts/{sid}.md','\n\n'.join(transcript))
  meta['records']=len(out);meta['file']=f'trajectories/sessions/{sid}.jsonl';sessions.append(meta)
 js('trajectories/SESSION_INDEX.json',sessions)
 turns.sort(key=lambda x:x.get('timestamp') or '')
 tools.sort(key=lambda x:x.get('timestamp') or '')
 write('trajectories/VISIBLE_DIALOGUE.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in turns))
 write('trajectories/TOOL_EXECUTION.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in tools))
 print(f'Exported {len(sessions)} research sessions, {len(turns)} messages, {len(tools)} tool records',flush=True)
 # Local reference material and exact acquisition provenance.
 (DEST/'literature').mkdir(exist_ok=True)
 refs=[('Fink_2007.pdf','https://kam.mff.cuni.cz/~fink/publications/kreweras1.pdf'),
 ('Fink_Hotmar_2501.19029v1.pdf','https://arxiv.org/pdf/2501.19029v1'),
 ('Havel_Krivanek_1982.pdf','https://dml.cz/bitstream/handle/10338.dmlcz/106137/CommentatMathUnivCarol_023-1982-1_10.pdf'),
 ('Fink_2factor.pdf','https://ktiml.mff.cuni.cz/~fink/publication/west.pdf'),
 ('Cygan_Kratsch_Nederlof.pdf','https://arxiv.org/pdf/1211.1506'),
 ('Wang_Zhang_1301.2931.pdf','https://arxiv.org/pdf/1301.2931'),
 ('Ali_Ba_Yang_2506.21432.pdf','https://arxiv.org/pdf/2506.21432'),
 ('Fink_Mutze_2401.01769.pdf','https://arxiv.org/pdf/2401.01769')]
 provenance=[]
 for name,url in refs:
  print('Reference '+name,flush=True);provenance.append(download(url,DEST/'literature'/name))
 local=Path('D:/浏览器下载/symmetry-17-00995.pdf')
 if local.is_file():shutil.copy2(local,DEST/'literature'/local.name)
 js('literature/ACQUISITION.json',provenance)
 # An embeddable Python runs the stdlib-only package verifier and P6 checker offline.
 (DEST/'runtime').mkdir(exist_ok=True)
 runtime=download('https://www.python.org/ftp/python/3.12.10/python-3.12.10-embed-amd64.zip',DEST/'runtime/python-3.12.10-embed-amd64.zip')
 if runtime['status']=='saved':
  with zipfile.ZipFile(DEST/runtime['file']) as z:z.extractall(DEST/'runtime/python')
 js('runtime/ACQUISITION.json',runtime)
 # Preserve this builder for future iterations, without making it a required reader dependency.
 shutil.copy2(Path(__file__),DEST/'archive_builder.py')
 js('trajectories/EXPORT_SCOPE.json',{'root_thread':ROOT_ID,'sessions':len(sessions),'visible_messages':len(turns),'tool_records':len(tools),'hidden_reasoning_exported':False,'global_account_config_copied':False,'history_kind':'existing session-visible records and tools, not reconstructed reasoning','cutoff':'2026-11-03 Asia/Shanghai; live final turn is a bounded snapshot'})

def index():
 files=[];reviews=[];paths=[]
 R=DEST/'research/six_directions'
 for p in sorted(DEST.rglob('*')):
  if not p.is_file() or p.name in {'FILE_CATALOG.json','index.html','PACKAGE_MANIFEST.json','PACKAGE_VALIDATION.json'}:continue
  rel=p.relative_to(DEST).as_posix();suffix=p.suffix.lower()
  group='other'
  if rel.startswith('trajectories/'):group='轨迹'
  elif rel.startswith('ARIS_framework/'):group='ARIS框架'
  elif rel.startswith('literature/') or suffix=='.pdf':group='文献'
  elif suffix in ('.bin','.cnf'):group='证书与搜索数据'
  elif suffix in ('.py','.cpp','.mjs','.rs','.zig','.exe'):group='程序'
  elif 'REVIEW' in p.name or 'AUDIT' in p.name:group='审计'
  elif suffix in ('.log','.jsonl','.tsv','.csv'):group='运行记录'
  elif suffix=='.md':group='证明与说明'
  elif suffix=='.json':group='状态与有限结果'
  files.append({'path':rel,'bytes':p.stat().st_size,'group':group})
  if p.parent==R and p.suffix=='.json' and 'REVIEW' in p.name:
   try:
    d=json.loads(p.read_text(encoding='utf-8-sig'))
    if isinstance(d,dict):reviews.append({'file':rel,'verdict':d.get('verdict'),'summary':d.get('summary',d.get('reason_code','')),'dependencies':list(d.get('imported_dependency_hashes',{})),'model':d.get('reviewer_model'),'assurance':d.get('acceptance_status')})
   except Exception:pass
  if suffix in ('.py','.cpp','.md','.json') and p.stat().st_size<2_000_000 and rel.startswith('research/six_directions/'):
   try:
    txt=p.read_text(encoding='utf-8-sig',errors='replace')
    hits=sorted(set(re.findall(r'[EF]:[/\\][^\n\r\"\'<>]{0,160}',txt)))
    if hits:paths.append({'file':rel,'examples':hits[:5]})
   except Exception:pass
 js('FILE_CATALOG.json',files);js('trajectories/REVIEW_DEPENDENCIES.json',reviews);js('RELOCATION_NOTES.json',paths)
 stages=[('基础与端点归约','GENERAL_NEAR_PERFECT.md'),('完整四孔','FOUR_HOLE_FULL.md'),('完整六孔','SIX_HOLE_CLOSED.md'),('五维A8','Q5_A8_FULL_CLOSURE.md'),('五维A10','Q5_A10_FULL_CLOSURE.md'),('完整八孔','EIGHT_HOLE_FULL_CLOSURE.md'),('完整十孔','TEN_HOLE_FULL_CLOSURE.md'),('完整十二孔','TWELVE_HOLE_FULL_CLOSURE.md'),('十四孔末25几何','FOURTEEN_FINAL25_PROOF.md'),('完整十四孔','FOURTEEN_HOLE_FULL_CLOSURE.md'),('十六孔双源','SIXTEEN_SMALLCUT_PROOF.md'),('完整十六/十八孔','SIXTEEN_EIGHTEEN_FULL_CLOSURE.md'),('完整P6总装','P6_FULL_CLOSURE.md'),('六方向推论','SIX_DIRECTION_CYCLE_COROLLARIES.md')]
 lines=['# ARIS 迭代与RSI复用指南','本指南由归档时的现存证据整理；阶段顺序表示证明依赖，不假装重建不可见的内部思考。','## 研究流程','提出精确量词 → 构造/搜索 → 保存正证书或不可能性见证 → 独立验证 → 记录接受范围 → 总装检查。未接受与失败尝试均在原目录保留。','## 证明阶段']
 for title,name in stages:lines.append(f'- [{title}](research/six_directions/{name})')
 lines+=['## RSI 后续迭代协议','1. 为新目标新建目录，固定输入、原命题、源代码版本、随机种子和资源预算。','2. 区分生成器与验证器；负搜索结果、缺秩矩阵和抽样不能作为全称不可能性结论。','3. 记录每轮候选、失败原因、反例/障碍、修订和子代理接受范围；以本包原件作为冻结基线。','4. 先验明父层已接受、实际压缩匹配满足避障，再接入总装；不要仅检查原匹配。','5. 对新证书重算合法性、完备域及矩阵位；模型审读不替代确定性检查。','## 轨迹入口','- [会话索引](trajectories/SESSION_INDEX.json)','- [可见对话](trajectories/VISIBLE_DIALOGUE.jsonl)','- [工具执行记录](trajectories/TOOL_EXECUTION.jsonl)','- [审计依赖列表](trajectories/REVIEW_DEPENDENCIES.json)','- [历史进展账本](PROOF_PACKAGE.md)','- [ARIS框架说明](ARIS_framework/README_CN.md)','## 自包含边界','已有文献定理仍作为显式数学输入；完整引用与取得的PDF保存在literature目录。框架是当前文件快照，不声称等于每次历史执行时的字节版本。可见轨迹不包含隐藏推理，也没有账户密钥或全局配置。最初搜索的墙钟时间和硬件如无记录，不能补造。']
 write('ARIS_RSI_GUIDE.md','\n\n'.join(lines))
 catalog=json.dumps(files,ensure_ascii=False).replace('</','<\\/')
 counts=collections.Counter(x['group'] for x in files)
 cards=''.join(f'<span>{html.escape(k)}：{v}</span>' for k,v in counts.items())
 stagehtml=''.join(f'<li><a href="research/six_directions/{name}">{title}</a></li>' for title,name in stages)
 guide=(DEST/'ARIS_RSI_GUIDE.md').read_text(encoding='utf-8')
 page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ruskey–Savage 猜想 n=6 · 完整研究包</title><style>
body{font:17px/1.85 "Microsoft YaHei",sans-serif;background:#f3f5f6;color:#24343c;margin:0}main{max-width:1200px;margin:30px auto;padding:38px;background:white}h1{font-size:30px}h2{font-size:23px;border-bottom:1px solid #ddd;padding-top:25px}a{color:#12616c}nav{display:flex;gap:14px;flex-wrap:wrap}.cards{display:flex;gap:10px;flex-wrap:wrap}.cards span{background:#eef5f5;padding:8px 14px}input,select{font:inherit;padding:9px;border:1px solid #bbb;max-width:100%}input{width:65%}table{border-collapse:collapse;width:100%;font-size:14px}td,th{text-align:left;border-bottom:1px solid #ddd;padding:8px;overflow-wrap:anywhere}td:first-child{width:72%}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f7f7;padding:20px}.notice{border-left:4px solid #4b858b;padding:15px;background:#f0f6f6}iframe{width:100%;height:760px;border:1px solid #ddd}.scroll{overflow:auto}button{font:inherit;padding:7px 16px}@media(max-width:700px){main{margin:8px;padding:18px}h1{font-size:25px}iframe{height:650px}}
</style><main><h1>Ruskey–Savage 猜想 n=6 · 完整研究包</h1>
<p>离线成果展示、详细证明、全部现存有限证书与搜索产物、ARIS迭代和可见工具轨迹。归档日期：2026-11-03。</p>
<nav><a href="#results">成果</a><a href="#proof">详细证明</a><a href="#aris">ARIS / RSI</a><a href="#catalog">全部文件</a><a href="README.md">使用说明</a><a href="VERIFY.ps1">验证入口</a></nav>
<h2 id="results">成果与范围</h2><p>主命题 P₆：对 Q₆ 的任意立方体边匹配 M、任意自由根 u 和任意异奇偶目标 v（可以已覆盖），存在包含 M 的 Hamilton u–v 路。结合 Fink 完美匹配定理得到完整六维 Ruskey–Savage 圈结论；结合 Fink–Hotmar 提升框架得到任意维数至多六方向的圈延拓。</p>
<p class="notice">项目内审计保证等级为 same-family/provisional，依赖明确列出的文献定理与确定性有限证书；未经外部同行评议或证明助手形式化验证。包装校验、最终总装检查与重跑全部大型有限计算是不同层次。</p>
<p><a href="Ruskey-Savage_Q6_研究报告.html">打开组会报告</a> · <a href="Ruskey-Savage_Q6_证明资料汇编.html">打开详细证明汇编（含原始证明与审计）</a> · <a href="research/six_directions/P6_FULL_REVIEW.json">最终审计</a></p>
<iframe title="组会报告" src="Ruskey-Savage_Q6_研究报告.html" loading="lazy"></iframe>
<h2 id="proof">详细证明及证书依赖</h2><ol>STAGES</ol>
<p>原件完整保留在 research/six_directions，历史待审状态按原样保留，以最终绑定的接受范围为准。二进制证书下载与生成代码、失败尝试、审计日志均可在下表检索。</p>
<h2 id="aris">ARIS 迭代、轨迹与 RSI 复用</h2><p><a href="ARIS_RSI_GUIDE.md">完整迭代指南</a> · <a href="trajectories/SESSION_INDEX.json">会话索引</a> · <a href="trajectories/REVIEW_DEPENDENCIES.json">审计依赖图数据</a> · <a href="ARIS_framework/README_CN.md">ARIS框架</a> · <a href="REPRODUCE.md">复现指南</a></p><pre>GUIDE</pre>
<h2 id="catalog">全部文件检索</h2><div class="cards">CARDS</div><p><input id="q" placeholder="搜索文件名：FINAL25 / A8 / REVIEW / jsonl"><select id="group"><option value="">全部类型</option></select></p><p id="stats"></p><div class="scroll"><table><thead><tr><th>文件（相对路径）</th><th>分类</th><th>大小</th></tr></thead><tbody id="rows"></tbody></table></div><button id="more">显示更多</button>
<h2>复现与可迁移性</h2><p>全部页面与证书链接使用包内相对路径。执行 VERIFY.ps1 可离线验证清单；执行 REPLAY_FINAL.ps1 在新工作目录中运行最终 P6 总装检查。某些历史搜索脚本保留原始盘符，具体文件见 RELOCATION_NOTES.json，重跑前按 REPRODUCE.md 配置。原件不为迁移而篡改。</p>
<p><a href="PACKAGE_VALIDATION.json">本次包装检查</a> · <a href="PACKAGE_MANIFEST.json">SHA-256全文件清单</a> · <a href="literature/ACQUISITION.json">文献取得情况</a> · <a href="SELF_CONTAINED.md">自包含范围</a></p></main>
<script>const files=CATALOG;const q=document.querySelector('#q'),g=document.querySelector('#group'),rows=document.querySelector('#rows');for(const x of [...new Set(files.map(x=>x.group))])g.add(new Option(x,x));let limit=150;function render(){const term=q.value.toLowerCase(),xs=files.filter(x=>(!g.value||x.group===g.value)&&x.path.toLowerCase().includes(term));rows.replaceChildren();for(const x of xs.slice(0,limit)){const tr=document.createElement('tr'),td=document.createElement('td'),a=document.createElement('a');a.href=x.path.split('/').map(encodeURIComponent).join('/');a.textContent=x.path;td.append(a);tr.append(td);for(const s of [x.group,(x.bytes/1024).toFixed(1)+' KB']){const d=document.createElement('td');d.textContent=s;tr.append(d)}rows.append(tr)}document.querySelector('#stats').textContent=`共 ${xs.length} 个匹配，显示 ${Math.min(limit,xs.length)} 个`;document.querySelector('#more').hidden=limit>=xs.length}q.oninput=g.onchange=()=>{limit=150;render()};document.querySelector('#more').onclick=()=>{limit+=300;render()};render();</script></html>'''
 page=page.replace('STAGES',stagehtml).replace('<pre>GUIDE</pre>','<pre>'+html.escape(guide)+'</pre>').replace('CARDS',cards).replace('CATALOG',catalog)
 write('index.html',page)
 print(f'Indexed {len(files)} files',flush=True)

if __name__=='__main__':
 if '--index-only' not in sys.argv:build()
 index()
