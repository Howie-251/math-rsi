---
name: mathrsi-handoff
description: 将数学研究的原题、可读证明和真实验证证据整理成可复现交付与恢复入口，按需求调用 ARIS render-html、引用审计或编译，准备独立目录复现材料、最终 wiki 与 NEXT_SESSION。支持准确部分交接，不重开已闭数学或把展示成功当证明。
---

# MathRSI 可读交付与研究交接

本技能是研究主线的交付阶段。它消费原题、证明、真实验证和当前未闭义务，整理给读者使用的正文、复现入口、需要的文件包以及下一会话状态。用户只要阶段性交接、当前研究需暂停，或证明已完成等待分享时，都可以进入；交付内容的状态跟随实际数学证据，不能因排版漂亮或ZIP生成而升级。

本阶段不重选求解方法，不默认重做证明，不把交付失败当作先前定理失效。若发现真实数学缺口，交回 [mathrsi-prove](../mathrsi-prove/SKILL.md)；若仅验证证据待补或某版本未审，交回 [mathrsi-verify](../mathrsi-verify/SKILL.md)。已有原题证明成立而一项展示、外部复现或所需审阅尚缺时，分别报告，不合成一个模糊的PASS或FAIL。

**组合调用完成指定scope后返回原caller。** 正常交付、部分交付或发现缺口，都把实际产物与建议下一动作交回唯一主dispatcher，不自行再启动prove/verify或另一轮handoff。本文“回verify/prove”表示后继建议；内部所需assemble、引用审计、渲染或复现仍实际执行并回到本handoff。独立调用只做用户授权的交付；若用户明确要求持续研究，由本agent接主调度一次处理缺口，避免父子double-dispatch。

## 进入与恢复

先读原规格、实际证明入口、`VERIFICATION.md`或现用验证记录，以及最新恢复页。检查引用的真实audit、计算/形式证据是否存在，当前证明是否正是这些证据所支撑的版本。不凭一个状态标签重新解读所有日志；只深入与本次交付结论有实际关系的材料。

明确本次读者需要什么：单份Markdown证明、LaTeX/PDF、离线HTML、源码和证书、可解压的复现包，还是未完成工作的精确恢复。沿用用户已有名称；没有约定时，交接说明用 `HANDOFF.md`，恢复用 `NEXT_SESSION.md`，证明入口与verify阶段一致。目录只为实际材料出现，不建立一套所有任务都必须填满的空树。

恢复交付时，先查看上次哪项失败：渲染、引用查验、文件缺件、独立目录执行、还是数学/审阅未完成。已有正确正文和有效证据直接复用；修对应问题并读回产物。旧研究暂停保持暂停，整理资料本身不启动Goal、模型研究或云发布。

## 1. 整理读者可以从头读通的正文

证明正文先陈述对象、主要结果和证据，再按定义、定理/引理、证明组织有效论证。必要假设放在使用处，引用指向实际版本与定理/公式/页码。读者应能看出原输入怎样进入归约、计算或形式接口，又怎样回到结论。正文不堆内部任务指令、已废弃错误和模型对话；相关历史通过研究记录查阅。

若原稿已经完整而准确，直接使用其Markdown或TeX，不为展示多造一份canonical正文。只是标题、符号解释、引用定位或衔接不够，可在不改变数学的范围内修订。需要重写章节时可内部调用 [mathrsi-assemble](../mathrsi-assemble/SKILL.md)来使用proof-writer，并让它返回本handoff；保持已有证明和verification的对应关系。引入新断言、改假设或改结论时，将影响交回原caller建议verify检查，不能把它当纯排版。

部分交接也应有可读结果：正式写明已经证明的条件引理、局部定理或已核见证，保留准确适用域。原题未完成则在交接入口直说尚缺哪一个全称连接、分支或核验，不将一堆局部文件包装成原题解答。对外正文直接呈现正确内容，细节失败留在适当研究记录。

## 2. 按实际引用形态完成引用核查

关键进口在证明推进和verify中已经核过的版本、条件和实际调用可以复用；本阶段检查正文是否仍准确引用它。新增bibliography、正式paper或用户要求引用审计时，读 [citation-audit Codex](../skills-codex/citation-audit/SKILL.md)／[Claude 主线](../citation-audit/SKILL.md)并执行。其原生合同读取 `.bib`与TeX cite contexts、实际外部检索并保存 `CITATION_AUDIT.{md,json}`，选择的reviewer还须能完成独立web lookup，文件只读意见不能冒充检索。

只有Markdown中的少数准确文献定位时，可以按实际一手来源核查每条被用的定理及上下文，记录版本、位置和结果；不要宣称这种人工核查已经执行完整citation-audit。若为了正式审计准备TeX/bib输入，保留原句和引用对应，不能凭空发明条目。单独需要字段级比对时再读 [citation-crosscheck Codex](../skills-codex/citation-crosscheck/SKILL.md)／[Claude 主线](../citation-crosscheck/SKILL.md)，保留其真实blind能力边界。

引用条目真实不证明所引数学推论正确。未核关键进口保持准确pending；若影响定理接受范围，回verify明确它的状态。若只是待补年份或链接，修相应条目和正文，再做相称检查。无需把所有旧参考从零多模型复查。

## 3. 生成用户需要的阅读版本

需要HTML时，完整读 [render-html Codex](../skills-codex/render-html/SKILL.md)／[Claude 主线](../render-html/SKILL.md)执行，传入真正正文及需要展示的真实验证JSON，不用render替代数学审计。其脚本与模板位于技能自己的 `scripts/`，不是 `base/tools/render_html.py`；按[仓内调用约定](../../../docs/ARIS_REUSE.md)绑定本副本。

例如在任务工作区，下面是本副本实际脚本的调用形态；路径按当前克隆位置填写：

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/skills/skills-codex/render-html/scripts/render_html.py" \
  PROOF.md --template academic --out PROOF.html --title "Proof"
```

这只是生成步骤；完整render-html技能的展示保真review、实际浏览检查与sidecar状态仍须按其合同消费。检查公式、表格、源码链接和窄屏是否可读；展示审阅只判正文到视图的保真，不判定理真。失败时保留原正文，修实际展示问题，不改数学适应渲染器。

脚本 `--offline` 去除CDN而保留raw math，不会把公式预渲染成离线SVG。用户要求真正离线排版公式时，复用任务已有可用生成流程或适合的文档工具，检查离线实际显示后再宣称达标；不能用该flag名称冒充完成。用户要PDF且已有LaTeX时，可读 [paper-compile Codex](../skills-codex/paper-compile/SKILL.md)／[Claude 主线](../paper-compile/SKILL.md)执行相应构建与版面检查，报告实际工具和结果。没有PDF/HTML要求，不强迫所有短证明多导出一套网页。

## 4. 准备可在独立目录执行的复现材料

依据verify中的实际义务—证据连接，选取复现所需原规格、正文、源代码、输入/证书、依赖锁定与已有运行命令。小纯解析证明不需要附一个虚构脚本；计算证明给准确参数域和实际checker入口；Lean项目给固定toolchain、package/manifest、真实主模块及audit命令。不要把作者私有缓存或整个历史工作区打包为普通读者必须读取的输入。

在交接说明写明入口、执行顺序、预期输出/范围和实测资源。命令必须从包或明确的任务材料中找到输入，不能暗中依赖作者另一个工作区。已有远端大证据按用户认可的存储和获取方式说明；没有复制进包就别说包完全离线自包含。凭据、机器专用工具链和无关缓存不进入共享材料。

用户要求或任务验收需要独立目录复现时，将必要材料放到任务授权的独立目录或解压副本，再运行与本次结论有关的复现命令，记录实际cwd、输入、退出码、输出和覆盖。尽量复用兼容依赖缓存，避免破坏原工程；复算会更改文件时就在副本进行。重放一个固定证书、重建项目输出、全域独立第二实现是不同范围，按真正完成者报告。第二目录由同一代理执行也不是“他人独立复现”。

Lean按原技能验证实际模块和导出，不用默认lake build成功替代；Mathlib缓存可复用时不删全库、不执行lake update漂移锁文件。具体独立目录步骤读 [Lean handoff reference](../skills-codex/lean-formalize/references/verification-and-handoff.md)（Claude的[同名reference](../lean-formalize/references/verification-and-handoff.md)），其例名和版本相关命令按真实项目调整。

执行因缺依赖/资源无法完成时，把准确待执行项和现有证据一起交出，不自动安装大型运行环境，不宣称失败命令已通过。没有要求重建所有历史结果就不重跑它们；本次选取的复现范围应足以支撑要交付的结论。若检查暴露代码与数学不符，回verify/prove修实质问题。

用户需要ZIP或其他包时，在材料和入口就绪后生成，解压读回关键入口、相对链接、源码与输入，必要复现放解压副本执行。包名和目录可按项目惯例，不要求额外hash框架；原audit已有freshness字段保持其既有合同，不以新散列替代读回或数学核验。

## 5. 更新原wiki与下一会话入口

读本仓 [research-wiki Codex](../skills-codex/research-wiki/SKILL.md)／[Claude 主线](../research-wiki/SKILL.md)，沿用原任务唯一wiki及canonical helper，不新建“交付wiki”。正文阅读到的真实论文、可复用引理条件、研究失败与重启理由接到适当原记录；graph和generated Connections用真实helper维护。自动query pack不保证列出每项关键结论，恢复页直接链接相关实体。

proof-axis claim的出生与升级沿proof-checker真实audit与其wiki hook。handoff不能凭正文完成或zip成功自行add verified claim；缺audit时保留普通研究记录和准确状态，若任务需要canonical claim再返回verify走实际流程。已存在claim需同步新审计范围时，引用真实audit和声明，不能伪造模型认可或扩大进口状态。经验性搜索结果另作实验/idea证据，不改成全称定理。

`NEXT_SESSION.md`或已有恢复页最后写出原题入口、当前严格结果与scope、完成还是未闭、真实证据、尚需的数学/验证/交付、在途任务及下一动作。完成就写明完成及交付入口，防止旧未闭快照复活；部分交接给最小未闭义务和实际caller，接手者能直接继续，而不是重读整个研究史。

最终 `HANDOFF.md`将读者需要的结论放前面，再给正文、verification、复现命令和已知依赖。它应明确区分“原命题已证”“只证某变体/子域”“Lean核验”“计算核验”“模型静态审阅”“独立目录复现”“另一人复现”，只陈述真正发生的事实。用户要求的某项交付缺失时列为pending；没有此要求就不主动制造验收障碍。

## 调用与继续例

```text
读取本仓 mathrsi-handoff/SKILL.md 并执行。
原题 FORMAL_SPEC.md，正文 PROOF.md，真实验证 VERIFICATION.md。
保留已核数学，生成所需可读HTML并检查实际公式显示；
把证明、证书、checker及固定依赖整理到可独立解压的材料中，
在副本运行交接所需的证书重放，准确报告范围。
本次需要ZIP，同时更新原wiki和NEXT_SESSION.md。
若正文中的新数学缺口出现，返回原caller并建议verify/prove，
不自行重复派发后继，也不靠排版补成已证。
```

若用户说“先暂停，交接尚未完成的证明”，同一流程消费当前严格部分，不必先求出整题。最终应交出已证什么、原题缺什么、从哪里恢复；不把“交接完成”写成“数学Goal完成”，也不由文档状态恢复暂停研究。

主流程组合调用到此只收到一次handoff返回，依据实际交付和数学状态决定完成、继续或等待；不由handoff与父流程各自再启动一次验证。独立交付请求到授权范围即结束，明确的持续授权才由本agent转入单一主调度。
