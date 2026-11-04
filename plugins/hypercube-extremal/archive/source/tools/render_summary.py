"""Rebuild the offline summary from the package guide and source inventory."""
from pathlib import Path
import html,re,json
B=Path(__file__).resolve().parents[1]
G=B/'guide'
inventory=json.loads((B/'inventory.json').read_text(encoding='utf-8'))
items=inventory.get('files',inventory.get('entries',[])) if isinstance(inventory,dict) else inventory
mapping={}
for x in items:
 if isinstance(x,dict):
  src=x.get('source',x.get('source_path',''));dst=x.get('stored_path',x.get('destination',x.get('archive_path','')))
  if src and dst:mapping[re.sub('/+','/',src.replace('\\','/'))]=dst.replace('\\','/')

def inline(s):
 s=html.escape(s)
 def link(m):
  u=html.unescape(m[2]);u=mapping.get(re.sub('/+','/',u.replace('\\','/')),u)
  if re.match(r'^[EF]:',u):return '<span title="历史源路径">'+m[1]+'</span>'
  return '<a href="'+html.escape(u,quote=True)+'">'+m[1]+'</a>'
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 return s
def render(s):
 lines=s.splitlines();out=[];i=0;ul=False
 while i<len(lines):
  l=lines[i]
  if l.startswith('```') or l.strip()=='\\[':
   end='```' if l.startswith('```') else '\\]';a=[];i+=1
   while i<len(lines) and not lines[i].startswith(end):a.append(lines[i]);i+=1
   out.append('<pre>'+html.escape('\n'.join(a))+'</pre>');i+=1;continue
  if not l.strip():i+=1;continue
  if l.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    row=lines[i].strip().strip('|').split('|');i+=1
    if all(re.fullmatch(r'\s*:?-+:?\s*',x) for x in row):continue
    rows.append(row)
   out.append('<div class="tablewrap"><table>')
   for k,row in enumerate(rows):
    tag='th' if k==0 else 'td';out.append('<tr>'+''.join('<'+tag+'>'+inline(x.strip())+'</'+tag+'>' for x in row)+'</tr>')
   out.append('</table></div>');continue
  m=re.match(r'^(#{1,6})\s+(.*)',l)
  if m:out.append('<h'+str(min(4,len(m[1])+1))+'>'+inline(m[2])+'</h'+str(min(4,len(m[1])+1))+'>');i+=1;continue
  m=re.match(r'^\s*(?:[-*]|\d+\.)\s+(.*)',l)
  if m:
   a=[]
   while i<len(lines) and (m:=re.match(r'^\s*(?:[-*]|\d+\.)\s+(.*)',lines[i])):
    a.append('<li>'+inline(m[1])+'</li>');i+=1
   out.append('<ul>'+''.join(a)+'</ul>');continue
  a=[l];i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|\\\[|[-*] |\d+\. )',lines[i]):a.append(lines[i]);i+=1
  out.append('<p>'+inline(' '.join(a))+'</p>')
 return '\n'.join(out)

sections=[('result','成果与边界','01_RESULT_AND_SCOPE.md'),('theory','约束与完整证明','02_THEORY_AND_CONSTRAINTS.md'),('search','搜索与全域认证','03_SEARCH_AND_FULL_DOMAIN.md'),('trajectory','真实迭代与失败转折','04_TRAJECTORY.md'),('rsi','RSI可接续状态','05_RSI_REUSE_AND_STATE.md'),('replay','复现与真实成本','06_REPRODUCTION_AND_COSTS.md')]
if (G/'07_EVIDENCE_AUDIT.md').exists():sections.append(('audit','证据审计','07_EVIDENCE_AUDIT.md'))
nav=''.join(f'<a href="#{i}"><small>{k+1:02}</small>{title}</a>' for k,(i,title,_) in enumerate(sections))
body=''.join(f'<section id="{i}"><div class="eyebrow">CHAPTER {k+1:02}</div><a class="source" href="guide/{f}">Markdown 原稿 ↗</a>{render((G/f).read_text(encoding="utf-8"))}</section>' for k,(i,title,f) in enumerate(sections))
css='''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:25px}body{margin:0;background:#f5f3ee;color:#24332f;font-family:"Segoe UI","Microsoft YaHei",sans-serif;line-height:1.85;font-size:15px}a{color:#116558;text-underline-offset:3px}aside{position:fixed;left:0;top:0;bottom:0;width:246px;padding:36px 24px;background:#132f2b;color:#fff;overflow:auto}aside .brand{letter-spacing:3px;font-size:12px;color:#b0d2c4}aside h2{font-size:22px;line-height:1.6;margin:20px 0 38px}aside a{display:block;color:#dbe9e2;text-decoration:none;padding:10px 0;border-top:1px solid #ffffff20;font-size:13px}aside small{display:inline-block;width:30px;color:#8ebdad}aside p{font-size:12px;color:#b0c7bb;margin-top:35px}main{margin-left:246px;max-width:1400px;padding:48px 6% 90px}.eyebrow{font-size:11px;letter-spacing:2.8px;color:#54756a;font-weight:700}h1{font-size:clamp(30px,3.3vw,48px);line-height:1.3;margin:18px 0}h2{font-size:27px;line-height:1.5;margin:18px 0 26px}h3{font-size:20px;margin:34px 0 14px}h4{font-size:17px;margin:25px 0 12px}p{margin:13px 0}header{padding-bottom:38px;border-bottom:1px solid #cbd6cc}.lede{font-size:17px;max-width:790px;color:#51665d}.result{background:#153e35;color:white;border-radius:10px;padding:28px 32px;margin:28px 0}.result .number{font:500 clamp(25px,3vw,43px) "Consolas",monospace;letter-spacing:-1px;margin:12px 0;overflow-wrap:anywhere}.result .fraction{font-family:Consolas,monospace;font-size:13px;overflow-wrap:anywhere}.pill{display:inline-block;border:1px solid #6f9b85;padding:2px 10px;border-radius:20px;font-size:11px;letter-spacing:1px}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:23px 0}.stat{background:white;border:1px solid #d8dfd7;padding:18px;border-radius:8px}.stat b{display:block;font:600 25px Consolas,monospace;color:#1b5547}.stat span{font-size:12px;color:#68776e}.notice{padding:16px 20px;border-left:4px solid #bd8a37;background:#fff8e9;color:#63512e;font-size:13px}.flow{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:24px 0}.flow div{background:#e4eee7;padding:14px 12px;border-radius:7px;font-size:12px}.flow b{display:block;color:#175947}.flow small{color:#64766b}section{padding:38px 0 34px;border-bottom:1px solid #cbd6cc}.source{float:right;font-size:12px}.tablewrap{width:100%;overflow:auto;margin:20px 0;border:1px solid #d4dfd5;border-radius:7px;background:white}table{border-collapse:collapse;width:100%;font-size:13px;min-width:620px}th{background:#e2ece4;color:#234e40;text-align:left}td,th{padding:12px 14px;border-bottom:1px solid #e1e7df;vertical-align:top}tr:last-child td{border-bottom:0}td{overflow-wrap:anywhere}tr:nth-child(2n+1) td{background:#fbfcf9}code{font-family:Consolas,monospace;font-size:.9em;background:#e8ede5;border-radius:4px;padding:2px 5px;overflow-wrap:anywhere}pre{overflow:auto;padding:18px;background:#e8eee6;border-left:3px solid #79a18a;font:13px/1.8 Consolas,monospace;white-space:pre-wrap;overflow-wrap:anywhere}strong{color:#1b5946}li{padding:4px 0}footer{font-size:12px;color:#6d7c70;padding-top:35px}.links{display:flex;gap:12px;flex-wrap:wrap}.links a{padding:6px 12px;border:1px solid #a8c0b0;border-radius:5px;text-decoration:none;font-size:12px}@media(max-width:980px){aside{position:static;width:auto;padding:22px}aside h2{margin:6px 0}aside nav{display:flex;gap:10px;flex-wrap:wrap}aside a{border:0;padding:5px;font-size:12px}aside p{display:none}main{margin:0;padding:30px 5%}.stats{grid-template-columns:1fr}.flow{grid-template-columns:repeat(2,1fr)}}@media print{body{background:white;font-size:11px}aside{display:none}main{margin:0;max-width:none;padding:0}section{break-before:page;padding-top:10px}h2,h3,h4{break-after:avoid}.tablewrap{overflow:visible}table{min-width:0;font-size:10px}td,th{padding:6px}a{color:inherit}.source{display:none}.result{background:#edf4ef;color:#163e32;border:1px solid #779b86}.stats{grid-template-columns:repeat(3,1fr)}.flow{grid-template-columns:repeat(4,1fr)}@page{size:A4;margin:16mm}}'''
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Erdős 86 · Q4 上界成果与研究交接</title><style>'''+css+'''</style></head><body><aside><div class="brand">RESEARCH HANDOFF</div><h2>Erdős 86<br>Q4 上界研究</h2><nav>'''+nav+'''</nav><p>2026-11-04 整理<br>离线展示 · 可复现证书<br>真实轨迹 · RSI 接续</p></aside><main><header><div class="eyebrow">ERDŐS PROBLEM 86 / CERTIFIED Q4 UPPER BOUND</div><h1>从局部共同来源<br>到全域整数证书</h1><p class="lede">完整保存共同 Q4 补全、同根两旗的相对朝向、活动集与全量分离，以及从失败反馈到精确认证的实际过程。</p><div class="result"><span class="pill">最佳已认证 Q4 渐近界</span><div class="number">0.591551531948944775</div><div class="fraction">π_Q(C₄) ≤ 23662061277957791 / 40000000000000000</div></div><div class="stats"><div class="stat"><b>3,312,331</b><span>逐图整数检查的全域覆盖代表</span></div><div class="stat"><b>6</b><span>有效 PSD Gram 块，保留共享根朝向</span></div><div class="stat"><b>0.011628468…</b><span>相对 Baber 0.60318 的绝对下降</span></div></div><div class="notice">本包最优指已找到的最好证书；未证明 SDP 全局最优、未突破 0.59。结论为渐近密度上界，不能直接当作小维数边数界。本次从源码重编并重放了有限全域验证，未宣称第三方审稿或形式化认证。</div><div class="flow"><div><b>01 共同补全</b><small>四种观察来自同一真实图</small></div><div><b>02 保留朝向</b><small>共享根变换同步作用</small></div><div><b>03 搜索与反馈</b><small>活动池优化、全域找违反行</small></div><div><b>04 精确接受</b><small>整数 Gram、全域覆盖与平均证明</small></div></div><div class="links"><a href="certificate_final_q4/README.md">最强证书与复核入口</a><a href="guide/trajectory.json">机器可读研究轨迹</a><a href="inventory.json">原件与哈希清单</a><a href="guide/06_REPRODUCTION_AND_COSTS.md">复现和成本</a></div></header>'''+body+'''<footer>本页由包内 Markdown 确定性生成；原始文件与本次导读分别保存。历史指令不自动触发新的研究作业。数据缺失保持未知，复制的日志不重复计作新实验。</footer></main></body></html>'''
(B/'START_HERE.html').write_text(page,encoding='utf-8')
print(json.dumps({'html_bytes':len(page.encode()),'chapters':len(sections),'source_mappings':len(mapping)},ensure_ascii=False))
