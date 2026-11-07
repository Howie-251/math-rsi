#!/usr/bin/env python3
"""Build the requested offline viewing copy; originals stay unchanged."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, quote
from html import unescape, escape
import argparse, json, re, shutil, zipfile, subprocess

ROOT = Path(__file__).resolve().parents[4]
parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path)
parser.add_argument('--audit-dir', type=Path)
parser.add_argument('--zip', type=Path)
parser.add_argument('--tracked-list', type=Path, help='Previously collected Git tracked paths, one per line; avoids running Git')
args = parser.parse_args()
OUT = args.output.resolve() if args.output else ROOT / 'deliverables/MathRSI_homepage_offline_20261108'
AUDIT = args.audit_dir.resolve() if args.audit_dir else Path(__file__).resolve().parent
AUDIT.mkdir(parents=True, exist_ok=True)
ZIP = args.zip.resolve() if args.zip else OUT.with_suffix('.zip')
GH = 'https://github.com/lisresearchgroup/math-rsi/blob/main/'
TRACKED = set(args.tracked_list.read_text().splitlines()) if args.tracked_list else set(subprocess.check_output(['git','ls-tree','-r','--name-only','-z','HEAD'],cwd=ROOT).decode().rstrip('\0').split('\0'))
LIMIT = 5_000_000
SITE = Path('development/homepage-redesign-20261105/site')
selected = set()
missing = []
class Refs(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.refs=[]
    def handle_starttag(self, tag, attrs):
        for name, val in attrs:
            if name in ('href','src','poster') and val: self.refs.append((tag,name,val))
def target(owner, value):
    u=urlsplit(unescape(value))
    if u.scheme or u.netloc or not u.path: return None
    p=(ROOT/owner).parent / unquote(u.path)
    p=p.resolve()
    if not p.is_relative_to(ROOT): return None
    return p.relative_to(ROOT)
def add(path):
    p=ROOT/path
    if p.is_file(): selected.add(Path(path))
def tree(path):
    for p in (ROOT/path).rglob('*'):
        if p.is_file() and not any(x in p.parts for x in ('.git','__pycache__','.DS_Store')): add(p.relative_to(ROOT))
tree(SITE)
for d in ['case-studies/property-b/readers','case-studies/property-b/assets','case-studies/degree-diameter/assets','case-studies/degree-diameter/data','case-studies/happy-ending/n7-20261103/figures']:
    tree(Path(d))
for f in ['case-studies/property-b/index.html','case-studies/degree-diameter/index.html','case-studies/degree-diameter/index.zh-CN.html','plugins/ecc/archive/source/paper/main.pdf','plugins/hypercube-extremal/archive/source/START_HERE.html','plugins/hypercube-hamilton/archive/source/Ruskey-Savage_Q6_研究报告.html','plugins/hypercube-hamilton/archive/source/Ruskey-Savage_Q6_证明资料汇编.html','case-studies/happy-ending/n7-20261103/START_HERE.html','case-studies/happy-ending/n7-20261103/n7-upper-bounds-20261103.html','case-studies/happy-ending/n7-20261103/proof-reader.html']:
    add(Path(f))
# Follow only HTML navigation, never the references in raw source/Markdown/data files.
# Include direct small files; newly reached readable HTML may expose another reader.
seen=set()
for depth in range(4):
    htmls=sorted(p for p in selected-seen if p.suffix.lower()=='.html')
    if not htmls: break
    for owner in htmls:
        seen.add(owner)
        p=Refs(); p.feed((ROOT/owner).read_text())
        for tag,name,value in p.refs:
            q=target(owner,value)
            if q is None: continue
            source=ROOT/q
            if source.is_file() and source.stat().st_size<LIMIT and not any(x in q.parts for x in ('.git','.lake','__pycache__')): add(q)
            elif name!='href' and tag!='a': missing.append({'owner':str(owner),'reference':value,'kind':'unresolved live load'})
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
rewritten=[]
unavailable=[]
attr=re.compile(r'(?P<before>\bhref\s*=\s*)(?P<quote>[\"\'])(?P<value>.*?)(?P=quote)', re.I|re.S)
for rel in sorted(selected):
    dst=OUT/rel;dst.parent.mkdir(parents=True,exist_ok=True)
    if rel.suffix.lower()!='.html': shutil.copy2(ROOT/rel,dst);continue
    source=(ROOT/rel).read_text()
    def replace(m):
        value=unescape(m['value']);q=target(rel,value)
        if q is None or q in selected: return m.group(0)
        u=urlsplit(value)
        if q.as_posix() not in TRACKED:
            unavailable.append({'owner':str(rel),'original_reference':value,'target':str(q),'reason':'Not included in this viewing archive and absent from repository HEAD'})
            return 'data-original-reference='+m['quote']+escape(value,quote=True)+m['quote']+' title=\"Not included in this viewing archive; unavailable in current source repository\" aria-disabled=\"true\"'
        url=GH+quote(q.as_posix(),safe='/')
        if u.query:url+='?'+u.query
        if u.fragment:url+='#'+quote(unquote(u.fragment),safe='-._~:')
        rewritten.append({'owner':str(rel),'from':value,'to':url})
        return m['before']+m['quote']+escape(url,quote=True)+m['quote']+' title="Online source · requires repository access"'
    dst.write_text(attr.sub(replace,source))
(OUT/'START_HERE.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=development/homepage-redesign-20261105/site/index.html"><title>MathRSI offline homepage</title><p><a href="development/homepage-redesign-20261105/site/index.html">Open MathRSI homepage / 打开首页</a></p></html>''')
(OUT/'README.txt').write_text('''MathRSI 首页与可读证明离线包 / Offline homepage and readable proofs
2026-11-08

使用：请先完整解压 ZIP，再用 Microsoft Edge（或现代桌面浏览器）打开 START_HERE.html。无需启动服务器。不要在压缩包内直接预览，文件夹相对位置请保持不变。
首页、交互、字体、原图及六个 Read 成果入口均随包提供。已附主要证明阅读页和这些 HTML 直接链接的小型材料；本包是成果阅读包，不是完整的科学复现实验档案，未包含全部扫描数据、工具链或构建缓存。
未随包附带且不在当前仓库中的原引用保留标签，但链接已禁用，鼠标悬停可见说明；详见 OMITTED_MATERIALS.txt。现有文献 DOI、GitHub、项目源码及快速安装入口需要联网及适用的访问权限；本包不会授予收件人 GitHub 权限。Markdown/Lean/JSON 等源文件可能以原文显示或下载。
所有数学结论及其原有验证状态沿用源材料；打包不增加审阅或验证保证。请保留材料的署名及来源。

Extract the complete ZIP, then open START_HERE.html in Microsoft Edge or a modern desktop browser. No server is required. Keep the directory layout intact; do not preview inside the ZIP.
The homepage, interactions, fonts, original figures and six Read entries are local. Principal proof readers and small files linked directly from their HTML are included. This is a viewing package, not a complete scientific reproduction archive: full scan data, toolchains and build caches are omitted.
Original references omitted from this package and absent from the current repository retain their labels with disabled links and explanatory hover text; see OMITTED_MATERIALS.txt. Existing DOI links, GitHub links and installation instructions require network and applicable repository permission. The ZIP does not grant GitHub access. Source Markdown/Lean/JSON files may display as raw text or download.
Mathematical statements and verification status remain those of the original materials. Packaging does not add mathematical validation. Preserve attribution and sources when forwarding.
''')
# Truthful inventory of excluded references; this is an omission list, not fabricated source content.
(OUT/'OMITTED_MATERIALS.txt').write_text('Materials not included in this viewing archive and absent from repository HEAD.\nThese original reference labels remain in the reports, with disabled links and an explanatory tooltip.\nNo GitHub URL is claimed for these files.\n\n'+''.join(f"Report: {x['owner']}\nOriginal reference: {x['original_reference']}\n\n" for x in unavailable))
with (OUT/'README.txt').open('a') as f:
    f.write(f'\n导航修订 / Navigation corrections: {len(rewritten)} 个链接指向已核对存在于当前 Git HEAD 的 GitHub 源文件；{len(unavailable)} 个原引用未随包附带且不在当前 Git HEAD，已禁用链接并保留原标签，详见 OMITTED_MATERIALS.txt。\n{len(rewritten)} links point to verified tracked GitHub source paths. {len(unavailable)} original references are omitted and absent from current Git HEAD; their labels are preserved with disabled links. See OMITTED_MATERIALS.txt.\n')
# Audit actual staged HTML navigation, load references, and CSS url() files.
fail=[]; external_load=[]
for file in OUT.rglob('*.html'):
    owner=file.relative_to(OUT);p=Refs();p.feed(file.read_text())
    for tag,name,value in p.refs:
        u=urlsplit(unescape(value))
        if u.scheme or u.netloc:
            if (name in ('src','poster') or tag=='link') and u.scheme not in ('data',):external_load.append([str(owner),value])
            continue
        if not u.path:continue
        q=(file.parent/unquote(u.path)).resolve()
        if not q.is_file():fail.append([str(owner),value])
for file in OUT.rglob('*.css'):
    for value in re.findall(r'url\([\"\']?([^\)\"\']+)',file.read_text()):
        u=urlsplit(value)
        if u.scheme or u.netloc:
            if u.scheme!='data':external_load.append([str(file.relative_to(OUT)),value])
        elif u.path and not (file.parent/unquote(u.path)).is_file():fail.append([str(file.relative_to(OUT)),value])
with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for f in sorted(OUT.rglob('*')):
        if f.is_file():z.write(f,f.relative_to(OUT.parent))
EXTRACT=AUDIT/'extracted'
if EXTRACT.exists():shutil.rmtree(EXTRACT)
with zipfile.ZipFile(ZIP) as z:z.extractall(EXTRACT)
files=[f for f in OUT.rglob('*') if f.is_file()]
report={'staging':str(OUT),'zip':str(ZIP),'extracted':str(EXTRACT/OUT.name),'files':len(files),'uncompressed_bytes':sum(f.stat().st_size for f in files),'zip_bytes':ZIP.stat().st_size,'rewritten_navigation_count':len(rewritten),'unavailable_navigation_count':len(unavailable),'unavailable_navigation':unavailable,'broken_local_references':fail,'external_live_loads':external_load,'unresolved_live_loads':missing,'included_sources':[str(x) for x in sorted(selected)],'rewritten_navigation':rewritten}
(AUDIT/'BUILD_RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('included_sources','rewritten_navigation','unavailable_navigation')},ensure_ascii=False,indent=2))
if fail or external_load or missing:raise SystemExit(1)
