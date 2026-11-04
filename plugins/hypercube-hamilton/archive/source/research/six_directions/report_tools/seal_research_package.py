from pathlib import Path
import concurrent.futures, hashlib, html, json, os, re, shutil, subprocess, sys, time
from urllib.parse import unquote,urlsplit
P=Path('D:/Ruskey–Savage 猜想n=6').resolve();S=Path('E:/新问题')
sys.path.insert(0,str(S/'research/six_directions/report_tools/vendor'))
from bs4 import BeautifulSoup
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def js(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
# User explicitly restricts this delivery to the Q6 completion.
target=(P/'research/seven_directions').resolve()
assert target.parent==P/'research' and target.is_relative_to(P)
if target.exists():shutil.rmtree(target)
for n in ('README.md','ARIS_RSI_GUIDE.md'):
 p=P/n
 if p.exists():p.write_text('\n'.join(x for x in p.read_text(encoding='utf-8').splitlines() if 'research/seven_directions' not in x),encoding='utf-8')
indexpath=P/'trajectories/SESSION_INDEX.json';sessions=json.loads(indexpath.read_text(encoding='utf-8'))
previous_scope=P/'trajectories/Q6_SCOPE_FILTER.json'
previous=json.loads(previous_scope.read_text(encoding='utf-8')) if previous_scope.exists() else {}
excluded=set(previous.get('excluded_Q7_sessions',[]))
for s in sessions:
 if re.search(r'seven|q7|p7|七方向|七维',json.dumps(s.get('source'),ensure_ascii=False),re.I):excluded.add(s['id'])
for _ in range(len(sessions)):
 old=len(excluded)
 for s in sessions:
  src=s.get('source') or {};parent=src.get('subagent',{}).get('thread_spawn',{}).get('parent_thread_id') if isinstance(src,dict) else None
  if parent in excluded:excluded.add(s['id'])
 if len(excluded)==old:break
indexpath.write_text(json.dumps([s for s in sessions if s['id'] not in excluded],ensure_ascii=False,indent=2),encoding='utf-8')
def q7record(e):return e.get('session_id') in excluded or bool(re.search('research/+seven_directions',json.dumps(e,ensure_ascii=False).replace('\\','/')))
removed=previous.get('Q7_or_duplicate_stream_records_removed',0)
for p in (P/'trajectories').rglob('*.jsonl'):
 records=[]
 for line in p.open(encoding='utf-8'):
  try:e=json.loads(line)
  except Exception:continue
  if q7record(e):removed+=1
  else:records.append(e)
 p.write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in records),encoding='utf-8')
 if p.parent.name=='sessions':
  transcript=[f'# Visible trajectory {p.stem}']
  for e in records:
   if e.get('kind')=='message':transcript.extend([f'\n## {e.get("timestamp")} · {e.get("role")}',e.get('text','')])
  (P/'trajectories/transcripts'/f'{p.stem}.md').write_text('\n\n'.join(transcript),encoding='utf-8')
for sid in excluded:
 for sub,ext in [('sessions','jsonl'),('transcripts','md')]:
  p=P/f'trajectories/{sub}/{sid}.{ext}'
  if p.is_file():p.unlink()
js('trajectories/Q6_SCOPE_FILTER.json',{'scope':'Q6 completion and Q6 exposition only','excluded_Q7_sessions':sorted(excluded),'Q7_or_duplicate_stream_records_removed':removed,'scientific_seven_directions_directory_included':False})
# Preserve final packaging source files as well.
for n in ('package_research.py','finalize_research_package.py','add_handoff_guides.py','seal_research_package.py'):
 shutil.copy2(S/'research/six_directions/report_tools'/n,P/'research/six_directions/report_tools'/n)
shutil.copy2(S/'research/six_directions/report_tools/package_research.py',P/'archive_builder.py')
shutil.copy2(S/'research/six_directions/report_tools/SEMINAR_BROWSER_QA.json',P/'research/six_directions/report_tools/SEMINAR_BROWSER_QA.json')
for n in ('ARCHIVE_BROWSER_QA.json','archive-index.png'):
 source=S/'research/six_directions/report_tools'/n
 if source.is_file():shutil.copy2(source,P/'verification_runs'/n)
acquisition=P/'literature/ACQUISITION.json'
records=json.loads(acquisition.read_text(encoding='utf-8'))
for record in records:
 if 'CommentatMath' in record['url']:
  paper=P/'literature/Havel_Krivanek_1982.pdf'
  if paper.is_file():
   record.update(status='saved',file='literature/Havel_Krivanek_1982.pdf',sha256=sha(paper),downloaded_via='http://dml.cz/bitstream/handle/10338.dmlcz/106137/CommentatMathUnivCarol_023-1982-1_10.pdf')
   record.pop('error',None)
acquisition.write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
scopepath=P/'trajectories/EXPORT_SCOPE.json';scope=json.loads(scopepath.read_text(encoding='utf-8'))
scope['sessions']=len(json.loads(indexpath.read_text(encoding='utf-8')))
scope['visible_messages']=sum(1 for _ in (P/'trajectories/VISIBLE_DIALOGUE.jsonl').open(encoding='utf-8'))
scope['tool_records']=sum(1 for _ in (P/'trajectories/TOOL_EXECUTION.jsonl').open(encoding='utf-8'))
scope['scope']='Q6 completion and related exposition; Q7 sessions and records filtered'
scopepath.write_text(json.dumps(scope,ensure_ascii=False,indent=2),encoding='utf-8')
# Index only, never recopy excluded scientific or session material.
subprocess.run([sys.executable,str(P/'archive_builder.py'),'--index-only'],check=True)
page=(P/'index.html').read_text(encoding='utf-8')
guides='<h2 id="handoff">研究交接导读</h2><p>本包仅整理至n=6证明完成，不含n=7探索。</p><ul>'+''.join(f'<li><a href="{p.relative_to(P).as_posix()}">{html.escape(p.stem)}</a></li>' for p in sorted((P/'guide').glob('*.md')))+'</ul><p><a href="guide/trajectory_index.csv">结构化研究记录CSV</a> · <a href="guide/timings_by_experiment.csv">原始时间字段CSV</a> · <a href="START_HERE.txt">先读说明</a> · <a href="DETAILED_RESEARCH_HANDOFF.txt">完整研究交接</a></p>'
page=page.replace('<h2 id="results">',guides+'<h2 id="results">')
(P/'index.html').write_text(page,encoding='utf-8');(P/'START_HERE.html').write_text(page,encoding='utf-8')
# Validate HTML file links without treating embedded formulas as filenames.
broken=[];checked=0
for name in ('index.html','START_HERE.html','Ruskey-Savage_Q6_研究报告.html','Ruskey-Savage_Q6_证明资料汇编.html'):
 soup=BeautifulSoup((P/name).read_text(encoding='utf-8'),'html.parser')
 for a in soup.find_all(['a','iframe']):
  href=a.get('href',a.get('src',''))
  if not href or href.startswith(('#','http:','https:','mailto:','javascript:','data:')):continue
  rel=unquote(href.split('#')[0]);checked+=1
  if not (P/rel).is_file() and rel not in ('PACKAGE_MANIFEST.json','PACKAGE_VALIDATION.json'):broken.append({'page':name,'href':href})
assert not broken,broken
exclude={'PACKAGE_MANIFEST.json','PACKAGE_VALIDATION.json'}
files=[p for p in P.rglob('*') if p.is_file() and 'verification_runs' not in p.relative_to(P).parts and p.name not in exclude]
print('Hash and source-compare',len(files),'files',flush=True)
def item(p):
 rel=p.relative_to(P);d={'path':rel.as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)};mismatch=None
 if rel.parts[0]=='research':
  original=S/rel
  if original.is_file() and sha(original)!=d['sha256']:mismatch=rel.as_posix()
 return d,mismatch
entries=[];mismatches=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for i,(entry,mismatch) in enumerate(pool.map(item,files),1):
  entries.append(entry)
  if mismatch:mismatches.append(mismatch)
  if i%2000==0:print('Hashed',i,flush=True)
assert not mismatches,mismatches
manifest={'schema':1,'date':'2026-11-03 Asia/Shanghai','scope':'Q6 completion only; no Q7 scientific directory','algorithm':'SHA-256','excluded_generated_paths':['verification_runs/','PACKAGE_MANIFEST.json','PACKAGE_VALIDATION.json'],'files':sorted(entries,key=lambda x:x['path'])}
js('PACKAGE_MANIFEST.json',manifest)
replay=json.loads((P/'verification_runs/FINAL_REPLAY.json').read_text(encoding='utf-8'))
validation={'date':'2026-11-03','static_files':len(entries),'bytes':sum(x['bytes'] for x in entries),'source_compare_errors':mismatches,'html_local_links_checked':checked,'broken_local_links':broken,'q7_directory_present':(P/'research/seven_directions').exists(),'portable_runtime_present':(P/'runtime/python/python.exe').is_file(),'final_replay':replay,'excluded_cache_directories':['__pycache__','edge-profile*','.git','node_modules'],'manifest_sha256':sha(P/'PACKAGE_MANIFEST.json'),'integrity_pass':True,'large_local_computations_rerun':False}
js('PACKAGE_VALIDATION.json',validation)
print(json.dumps({k:v for k,v in validation.items() if k!='final_replay'},ensure_ascii=False),flush=True)
