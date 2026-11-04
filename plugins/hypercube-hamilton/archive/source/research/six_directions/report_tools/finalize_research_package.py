from pathlib import Path
import ast, collections, contextlib, hashlib, html, io, json, os, re, shutil, subprocess, sys, time

P=Path('D:/Ruskey–Savage 猜想n=6')
SOURCE=Path('E:/新问题')
def write(n,s):
 p=P/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def js(n,x):write(n,json.dumps(x,ensure_ascii=False,indent=2))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()

write('verify_package.py',r'''"""Offline integrity validation; no third-party dependencies."""
from pathlib import Path
import hashlib,json,sys
R=Path(__file__).resolve().parent
manifest=json.loads((R/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
errors=[];total=0
for i,e in enumerate(manifest['files']):
 p=R/e['path']
 if not p.is_file():errors.append([e['path'],'missing']);continue
 if p.stat().st_size!=e['bytes']:errors.append([e['path'],'size']);continue
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
 if h.hexdigest()!=e['sha256']:errors.append([e['path'],'sha256'])
 total+=p.stat().st_size
 if (i+1)%1000==0:print('Checked',i+1,flush=True)
out={'scope':'all manifest-bound files; not a mathematical proof check','files_checked':len(manifest['files']),'bytes_checked':total,'errors':errors,'pass':not errors}
(R/'verification_runs').mkdir(exist_ok=True)
(R/'verification_runs/integrity.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2));sys.exit(bool(errors))
''')
write('replay_final.py',r'''"""Run the original stdlib-only checker with output writes redirected away from frozen evidence."""
from pathlib import Path
import contextlib,hashlib,io,json,os,runpy,sys,time
R=Path(__file__).resolve().parent
work=R/'verification_runs'/('p6-'+time.strftime('%Y%m%d-%H%M%S'))
work.mkdir(parents=True,exist_ok=True)
checker=R/'research/six_directions/P6_FULL_REVIEW_check.py'
old=Path.write_text
def isolated(self,data,*a,**kw):
 if self.name=='P6_FULL_REVIEW_check.json':return old(work/self.name,data,*a,**kw)
 raise RuntimeError('Unexpected evidence write blocked: '+str(self))
Path.write_text=isolated
sys.argv=[str(checker),'--final'];stream=io.StringIO()
try:
 with contextlib.redirect_stdout(stream):runpy.run_path(str(checker),run_name='__main__')
finally:
 Path.write_text=old
 (work/'stdout.txt').write_text(stream.getvalue(),encoding='utf-8')
 print(stream.getvalue())
report=json.loads((work/'P6_FULL_REVIEW_check.json').read_text(encoding='utf-8'))
summary={k:report[k] for k in ('errors','bound_files_rehashed','transitive_review_nodes','report_dependency_edges','dependency_DAG_acyclic','large_local_certificate_computations_rerun')}
summary['output']=str(work.relative_to(R));summary['original_checker_sha256']=hashlib.sha256(checker.read_bytes()).hexdigest()
(R/'verification_runs/FINAL_REPLAY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
assert not report['errors'];print('Final assembly replay passed; large local computations were NOT rerun.')
''')
ps='''$ErrorActionPreference = 'Stop'
$packageRoot = $PSScriptRoot
$pythonExe = Join-Path $packageRoot 'runtime\python\python.exe'
if (-not (Test-Path -LiteralPath $pythonExe)) { throw 'Bundled runtime missing; see runtime/ACQUISITION.json' }
& $pythonExe (Join-Path $packageRoot '{script}')
if ($LASTEXITCODE -ne 0) { throw 'Validation failed; inspect verification_runs' }
'''
write('VERIFY.ps1',ps.replace('{script}','verify_package.py'))
write('REPLAY_FINAL.ps1',ps.replace('{script}','replay_final.py'))
write('OPEN.cmd','@echo off\r\nstart "" "%~dp0index.html"\r\n')
readme='''# Ruskey–Savage 猜想 n=6 完整研究包

打开 **index.html**，或双击 OPEN.cmd。所有显示页、源码、证书及轨迹均在本目录内，不依赖 E 盘、F 盘或 CDN 阅读。整体移动目录后仍可阅读和执行清单校验。

## 成果

P6：任意 Q6 短边匹配、任意自由根、任意异奇偶目标（含已覆盖目标）的 Hamilton 路延拓。结合已发表完美匹配定理，得到完整六维 Ruskey–Savage 圈结论；结合有限维提升框架，得到任意维数至多六方向的圈延拓。

保证等级 same-family/provisional。原证明包是计算辅助证明，不是外部同行评议或证明助手形式化证明。

## 文件导航

- index.html：离线汇总、嵌入讲稿、搜索全部文件。
- Ruskey-Savage_Q6_研究报告.html / .md：最新成果、文献表、详细证明主线。
- Ruskey-Savage_Q6_证明资料汇编.html / .md：231份原始证明/审读材料的可展开汇编。
- research/six_directions：全部现存证书、搜索源码、程序、日志、失败尝试、审计与状态原件。
- research/openai_math_20261031：最初文献研究的现存材料；目录为空时不补造内容。
- research/seven_directions：后续探索的原件，属于延伸研究，不冒充Q6证明输入。
- trajectories：本研究根会话及显式子代理的可见对话、工具执行、会话索引和审计依赖。
- ARIS_framework：ARIS当前框架快照，含proof-writer/proof-checker说明、模板与工具。
- literature：取得的参考论文、来源与SHA-256。
- runtime：便携Python；VERIFY.ps1与REPLAY_FINAL.ps1使用该运行时。
- PACKAGE_MANIFEST.json：全部交付静态文件的SHA-256清单。
- REPRODUCE.md / SELF_CONTAINED.md / ARIS_RSI_GUIDE.md：复现、边界与后续迭代。

## 快速校验

在本目录运行 `powershell -ExecutionPolicy Bypass -File .\VERIFY.ps1` 校验所有绑定文件；约需读取整个包一次。

运行 `powershell -ExecutionPolicy Bypass -File .\REPLAY_FINAL.ps1` 重新执行原始最终总装检查。输出写入verification_runs，不改原始证据。

不要直接在冻结目录运行带生产输出的搜索程序；先复制到新实验目录。所有历史失败与条件性状态按原样保留，应以最终P6_FULL_REVIEW.json的范围为准。
'''
write('README.md',readme)
write('SELF_CONTAINED.md','''# 自包含范围与交付边界

1. **离线资料自包含**：完整复制现存科学证据、源码、搜索产物与框架说明；HTML、文档、索引、二进制证书均在包内。网络只用于文献原始链接，阅读本包不需要网络。
2. **验证入口自包含**：便携Python运行标准库清单校验及最终P6绑定/DAG检查，不要求原Anaconda安装。验证输出与冻结证据隔离。
3. **数学输入明确**：Fink完美匹配、Havel–Křivánek极大匹配下界、连通矩阵秩定理等仍按原证明显式导入，取得的原论文放literature。本包不是把所有文献定理重新证明一遍的公理化形式系统。
4. **搜索重跑条件透明**：历史C++程序、编译产物、Python生产脚本原样保留。搜索源文件有固定原路径、工具链或第三方库要求；RELOCATION_NOTES.json和DEPENDENCIES.json给出迁移清单。不能因本包可离线验证就宣称任意机器能够零配置重跑每个历史搜索。
5. **轨迹是可见执行记录**：包含已存会话可见消息、工具参数和输出；不含隐藏推理、账户配置、认证信息，也不假装恢复从未保存的过程。现存日志和历史账本补充时间线。
6. **框架版本边界**：ARIS是归档时磁盘快照；若旧记录没有记录精确提交号，不能倒推历史每轮都使用同一框架字节。原件SHA清单用于今后迭代基线。
7. **检查层次**：PACKAGE_VALIDATION证明交付完整与离线链接；FINAL_REPLAY证明最终总装检查本次通过；原审计对大型局部证书的历史验算仍作为显式输入。本次未冒称重算全部大型矩阵和全枚举搜索。
''')
write('REPRODUCE.md','''# 复现与进一步迭代

## 第一级：交付完整性

双击OPEN.cmd阅读，运行VERIFY.ps1重算全部清单SHA。它不证明数学结论，只验证文件未损坏、未遗漏。

## 第二级：最终证明总装

运行REPLAY_FINAL.ps1。使用原始P6_FULL_REVIEW_check.py --final，重新散列绑定证书、核验九个孔层、依赖无环及端点/余域有限逻辑。通过Path.write_text的输出重定向，结果存入verification_runs，冻结源文件不变。报告明确 large_local_certificate_computations_rerun=false。

## 第三级：重算局部有限证据

以research/six_directions/P6_FULL_REVIEW.json为根，沿imported_dependency_hashes和checker_artifact_hashes查找每层的独立检查程序。先读对应REVIEW.md/.json，确认其参数、输入字节格式及实际接受范围，再在新工作副本执行对应checker。不同checker可能复用大量工作文件，不应以文件名相似就混用命令。具体历史命令在trajectories/TOOL_EXECUTION.jsonl中按程序名检索。

## 第四级：重跑原始搜索

从运行轨迹提取真实参数、编译命令与预算；使用包内.cpp/.py与原始输入。编译产物.exe保留供同平台使用，但依赖工具链需另外匹配。先按RELOCATION_NOTES.json替换工作副本中的E/F原路径，再安装DEPENDENCIES.json所列实际需要的库。可将search output与原证书比较，但生成器本身不作为真实性依据。

## 新RSI迭代

保留本包SHA基线，在新目录记录问题变体、输入与算法版本、随机种子、资源、每轮成功/失败和审计结论。重新证明目标不能仅修改原审计状态。Q6成果与七方向探索必须分别记账。

## 目录和解释器

所有顶层验证入口基于自身目录定位，不使用原E/F盘。runtime/python为Windows x64便携解释器；其他平台可用Python3.10+执行verify_package.py和replay_final.py。生产搜索对Python/C++版本的需求以原代码为准。
''')
# Inventory actual imports and original commands, rather than invent a universal dependency set.
imports=collections.defaultdict(list)
for p in (P/'research').rglob('*.py'):
 try:tree=ast.parse(p.read_text(encoding='utf-8-sig'))
 except Exception:continue
 for n in ast.walk(tree):
  modules=[]
  if isinstance(n,ast.Import):modules=[x.name.split('.')[0] for x in n.names]
  elif isinstance(n,ast.ImportFrom) and n.module:modules=[n.module.split('.')[0]]
  for mod in modules:
   if mod not in getattr(sys,'stdlib_module_names',set()) and mod not in ('__future__',):imports[mod].append(p.relative_to(P).as_posix())
js('DEPENDENCIES.json',{'python_for_standard_checkers':'>=3.10','bundled_python':'Windows x64 3.12.10','nonstdlib_or_local_imports':{k:sorted(set(v)) for k,v in sorted(imports.items())},'interpretation':'Includes local modules as well as third-party libraries; do not blindly pip-install every key. C++ producers need a compatible compiler; trace records preserve original commands.'})
print('Support files written',flush=True)
