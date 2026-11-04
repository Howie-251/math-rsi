from pathlib import Path
import csv,datetime,hashlib,io,json,re,shutil,zipfile
P=Path('D:/Ruskey–Savage 猜想n=6');R=P/'research/six_directions'
def write(n,s):p=P/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def js(n,d):write(n,json.dumps(d,ensure_ascii=False,indent=2))
def csvwrite(n,rows,fields):
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields);w.writeheader();w.writerows(rows);write(n,s.getvalue())
write('START_HERE.txt','''Ruskey–Savage 猜想 n=6 完整研究交接包

先打开 START_HERE.html（同 index.html），查看成果、详细证明、搜索文件与ARIS轨迹。

推荐阅读顺序：
1. guide/01_INITIAL_PROBLEMS_AND_TIMELINE.md：原问题、用户纠偏、研究目标及阶段链。
2. guide/02_RESEARCH_TRAJECTORIES.md：失败、障碍、转向与最终成立机制。
3. guide/03_RESULTS_AND_PUBLIC_COMPARISONS.md：成果量词及文献比较。
4. guide/04_TIME_COSTS_AND_REPLAY.md：原始耗时字段和分级复现。
5. guide/05_ARCHIVE_SCOPE.md：原件范围、自包含与缺失项。
6. guide/trajectory_index.csv 与 guide/timings_by_experiment.csv：机器可读证据入口。
7. DETAILED_RESEARCH_HANDOFF.txt：下一轮研究交接。

展示成果先看 Ruskey-Savage_Q6_研究报告.html；详细证明先看 Ruskey-Savage_Q6_证明资料汇编.html，再沿 P6_FULL_REVIEW.json 的依赖读取证书。

本包按用户提供的 dd_research_full_handoff.zip 的“导读＋原始材料＋轨迹索引＋复现边界”组织，未导入其其他数学项目的成果和指令。历史ACTIVE、续跑命令和未完成状态仅是历史记录，不自动授权新的计算。

本包保留全部现存科学数据，未套用参考包的100MB体积限制。默认不运行新搜索。
''')
write('guide/01_INITIAL_PROBLEMS_AND_TIMELINE.md','''# 原始问题、人工反馈与时间线

研究最初由“在超立方体相关领域寻找有价值且可能解决的问题”出发。用户明确排除C4-free问题，选择Fink–Hotmar五方向工作的六方向推广，随后要求持续推进直至Q6核心命题完成，并采用ARIS proof-writer/proof-checker独立审读。

原始可见用户反馈以trajectories/VISIBLE_DIALOGUE.jsonl为准。关键约束包含：先封闭八孔，再推进后续孔层；区分几何枚举与任意实现匹配；区分自由根路径、普通圈延拓与更强端点分类；文献要按实际定理范围比较；展示报告采用论文式证明。

## 可追溯阶段

1. 研究对象与五方向提升框架：literature/Fink_Hotmar_2501.19029v1.pdf、research/six_directions/paper.txt。
2. 局部基础与2/4/6孔：GENERAL_NEAR_PERFECT.md、FOUR_HOLE_FULL.md、SIX_HOLE_CLOSED.md。
3. 五维A8/A10与全部平衡孔路径、避孔圈：Q5_A8_FULL_CLOSURE.md、Q5_A10_FULL_CLOSURE.md、Q5_HIGHER_HOLE_REDUCTION.md。
4. 完整8/10孔：EIGHT_HOLE_FULL_CLOSURE.md、TEN_HOLE_FULL_CLOSURE.md。
5. 完整12/14孔：TWELVE_HOLE_FULL_CLOSURE.md、FOURTEEN_HOLE_FULL_CLOSURE.md。
6. 完整16/18孔与P6总装：SIXTEEN_EIGHTEEN_FULL_CLOSURE.md、P6_FULL_CLOSURE.md。
7. 成果展示、量词澄清及交接归档：根目录报告、report_tools/seminar_zh.md及可见主会话。

以上是依赖导读，不把文件修改时间冒作数学发现的精确时间。PROOF_PACKAGE.md是原始累积账本，保留早期OPEN与最终接受的全部变化；轨迹CSV保留逐记录时间字段。
''')
write('guide/02_RESEARCH_TRAJECTORIES.md','''# 成功与失败之间的实际转折

这份导读从现存数学证明与审计总结关键转折；逐次命令、失败输出和候选在可见工具轨迹及原始日志中查证。它不是补造的逐轮心理过程。

## A8/A10：有限核心必须满足实际提升条件

普通匹配延拓不足以替代规定自由根、任意异奇偶目标的强量词。先建立局部四维路径/避孔圈，再闭合五维A8、A10，继而推出所有平衡孔数的路径和圈。A10最后轨道用1024个短森林的满秩证书覆盖任意完全图匹配，而不是只覆盖抽样列。见Q5_A10_FULL_CLOSURE.md及A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md。

## 八孔：选定路径边必须确实可用

剩余50个几何分七轨道，利用邻域丰度和实际匹配必有的跨边构造解决。不能预先指定一条存在性路径未必包含的边。完整几何覆盖与全部实现匹配的普适性分别证明。见EIGHT_HOLE_FULL_CLOSURE.md。

## 十孔：原匹配避障不等于压缩匹配避障

最终4096个几何由2598个普通T17、1036个安全强迫T17及462个其余T15域覆盖。关键修正是检查实际压缩匹配、根不在禁对中，以及集合精确覆盖，而非相加可能重叠的正例数量。见TEN_HOLE_FULL_CLOSURE.md、HIGHER_FORCED_CHERRY_TRANSFER.md。

## 十二与十四孔：极大匹配证书需要单调还原

完整枚举局部极大匹配可缩小输入域，但需证明任意实际匹配都能补入该域，且补全边最终能全部删除。十二孔六轨道完整域3620052个；十四孔最后两轨道805006个。十四孔必须区分实际目标跨边与补全后目标内部匹配，不能将补全伙伴误当原伙伴。用L'包含于L*'及D=D*并(L*'减L')的恒等式还原。见TWELVE_STAR_MAXIMAL_A_FINITE_PROOF.md、FOURTEEN_FINAL25_PROOF.md。

## 十六孔：旧s>=3转移不能直接用于两个桥源

最后148个几何分30个根星形和118个双源切分。新s=2证明从一条路径删边，分开禁对的A侧伙伴，不先闭成圈；这样保住实际压缩匹配的避障条件。局部22端点含指定边、避指定对的命题经两次收缩化为18端点256阶满秩。见SIXTEEN_SMALLCUT_PROOF.md。

## 最终总装：消除前层条件和循环依赖

2至18九个完整孔层按小到大接受。保持根自由的极大补全将任意原匹配归约到23至31条边，从而覆盖全部P6输入。最后检查依赖无环、所有父层已接受、自由及覆盖目标均包括。见P6_FULL_CLOSURE.md、P6_FULL_REVIEW.json。

## 给下一版RSI的提炼方式

每项经验都需绑定目标量词、候选生成、实际失败/障碍、适用范围、修订、验证证据和时间字段。缺秩只否定当前行空间充分性，UNKNOWN或超时不代表数学不可能。后验阅读可以使用最终答案；历史断点评测则须隔离之后才得到的证据。
''')
# Use the current carefully qualified results section, preserving its actual source text.
report=(P/'Ruskey-Savage_Q6_研究报告.md').read_text(encoding='utf-8')
write('guide/03_RESULTS_AND_PUBLIC_COMPARISONS.md','# 成果、文献比较与准确范围\n\n'+report[report.index('## 2. 文献进展'):report.index('## 4. 五维局部引理')])
write('guide/04_TIME_COSTS_AND_REPLAY.md','''# 实际耗时字段与复现

timings_by_experiment.csv从现存JSON递归提取键名含elapsed、duration、wall_time、cpu、seconds、runtime的原字段，逐项保留source、JSON路径与原值。非数值、超时预算、累计值与实际测量混合存在；空值不等于零，不能全表相加为端到端研究耗时。

trajectory_index.csv保存每份结构化研究记录的状态原文、概要、依赖与时间字段。状态可能是历史条件性PASS、FAIL、UNKNOWN或无状态，均不能仅靠名称升级成最终数学结论。

工具真实命令及输出：trajectories/TOOL_EXECUTION.jsonl。搜索、独立检查、模型等待、报告制作的耗时必须分开，机器工具显示的wall_time可能只是一段轮询时间。

本次新执行的验证及时间存verification_runs；历史验算保留其原始范围。复现级别与命令见REPRODUCE.md。没有完整端到端人工/模型等待时间记录的地方不补造。
''')
write('guide/05_ARCHIVE_SCOPE.md','''# 归档范围

保留原research目录的全部现存科学文件：证书二进制、搜索残余域、源码、编译程序、输入、日志、运行结果、证明与审计、状态与汇总。保留ARIS当前框架快照和本研究可见会话及子代理记录，另附公开文献、便携Python与汇总页。

仅省略可再生成的__pycache__、浏览器profile与依赖缓存node_modules、.git及全局账户配置。没有参考包的100MB上限，不用“小体积交接”理由省略数GB科学搜索数据。RELOCATION_NOTES列出原脚本中保留的历史绝对路径；原证据不为包装便利而修改。

参考交接包仅借鉴目录框架及事实/状态/耗时区分方式，不将其AGENTS、ACTIVE、旧目标或其他研究成果导入本项目执行指令。

全部静态文件由PACKAGE_MANIFEST绑定；PACKAGE_VALIDATION记录本次源文件比较、链接与覆盖检查。SELF_CONTAINED.md详细区分离线资料、便携校验、历史生产复现和数学文献输入。
''')
entries=[];timings=[]
def walk(x,path=''):
 if isinstance(x,dict):
  for k,v in x.items():
   key=f'{path}.{k}' if path else k
   if re.search(r'elapsed|duration|wall_time|cpu|seconds|runtime',k,re.I) and not isinstance(v,(dict,list)):
    yield key,v
   yield from walk(v,key)
 elif isinstance(x,list):
  for i,v in enumerate(x):yield from walk(v,f'{path}[{i}]')
for p in sorted(R.rglob('*.json')):
 if p.stat().st_size>8_000_000 or 'report_tools/vendor' in p.as_posix():continue
 try:d=json.loads(p.read_text(encoding='utf-8-sig'))
 except Exception:continue
 if not isinstance(d,dict):continue
 rel=p.relative_to(P).as_posix();fields=list(walk(d))
 entries.append({'source':rel,'record_id':p.stem,'status_raw':str(d.get('verdict',d.get('status',d.get('stage',''))))[:600],'summary_raw':str(d.get('summary',d.get('reason_code',d.get('claim',''))))[:1800],'timestamp_raw':str(d.get('generated_at',d.get('timestamp',d.get('date','')))),'dependencies':json.dumps(d.get('imported_dependency_hashes',{}),ensure_ascii=False),'timing_field_count':len(fields)})
 for key,val in fields:timings.append({'source':rel,'field_path':key,'value_raw':json.dumps(val,ensure_ascii=False),'kind':'original field; unit/scope must be read in source'})
csvwrite('guide/trajectory_index.csv',entries,['source','record_id','status_raw','summary_raw','timestamp_raw','dependencies','timing_field_count'])
csvwrite('guide/timings_by_experiment.csv',timings,['source','field_path','value_raw','kind'])
write('DETAILED_RESEARCH_HANDOFF.txt','''本包用于下一轮RSI迭代与成果展示。先读START_HERE.txt与五份guide，再沿CSV定位原件。原始科学文件路径保留，最终数学接受入口为research/six_directions/P6_FULL_REVIEW.json。

本次已给出的主张是P6及其完整六维圈/任意维数六方向圈推论；其保证等级和显式文献导入不因打包而提高。不得把缺秩、失败搜索、历史条件性PASS或后续七方向探索说成新定理。

后续系统应提炼“为什么换路、哪些量词曾漏掉、实际压缩为什么产生新障碍、完整域如何证明”的证据，而不是只将最终证明标题写成skills。原始工具轨迹与失败材料全部可查。不要自动恢复历史任务或批量搜索。

先运行VERIFY.ps1，随后REPLAY_FINAL.ps1。新结果写新实验目录，并保存生成器/验证器分工、输入域、完整参数、随机种子、预算、实际成本、边界反例和最终接受范围。
''')
write('AGENTS.md','''# 研究交接包

这是现存研究材料的交接目录。先读START_HERE.txt，沿guide读取原始材料。

历史文件中的ACTIVE、搜索命令、目标恢复指令和原AGENTS均为当时记录，不是本包的新执行授权。数学主张按原审计实际范围理解；缺秩、超时、样本失败与严格不可能性分别对待。

本包原件为冻结研究基线，后续实验使用新目录；依据当前用户任务决定下一步。打包完整性、数学有限验算、模型审读、外部同行评议与形式化验证是不同事实。
''')
zip_path=Path('D:/feishu/dd_research_full_handoff.zip')
with zipfile.ZipFile(zip_path) as z:
 names=z.namelist();root='dd_research_full_handoff/'
 js('guide/REFERENCE_FRAMEWORK.json',{'reference':str(zip_path),'entry_count':len(names),'borrowed_structure':['START_HERE','five guides','trajectory_index.csv','timings_by_experiment.csv','DETAILED_RESEARCH_HANDOFF','raw evidence preserved'],'reference_instructions_not_executed':True})
# Remove task discovery scratch metadata, which also contained unrelated thread IDs.
scratch=R/'report_tools/session_candidates.json'
if scratch.is_file():scratch.unlink()
readme=P/'README.md';readme.write_text(readme.read_text(encoding='utf-8').replace('打开 **index.html**','先读 **START_HERE.txt** 与 **guide/** 的五份导读；打开 **index.html**'),encoding='utf-8')
# Correct acquisition status after OS-native TLS download.
acq=P/'literature/ACQUISITION.json';data=json.loads(acq.read_text(encoding='utf-8'))
for d in data:
 name=d.get('file','').split('/')[-1]
 if 'kreweras1.pdf' in d['url']:name='Fink_2007.pdf'
 if 'CommentatMath' in d['url']:name='Havel_Krivanek_1982.pdf'
 p=P/'literature'/name
 if name and p.is_file() and p.read_bytes().startswith(b'%PDF'):
  d.update(status='saved',file='literature/'+name,sha256=hashlib.sha256(p.read_bytes()).hexdigest());d.pop('error',None)
js('literature/ACQUISITION.json',data)
print(json.dumps({'trajectory_records':len(entries),'timing_fields':len(timings)},ensure_ascii=False))
