# proof-checker 的实际输入、局部范围与无损适配

调用本仓 ARIS checker 前读此文。它是 MathRSI caller 对固定上游接口的适配，不改上游技能、不扩张上游 detector 支持，也不生成 canonical 审计结果。

## 原生 LaTeX：保持源和依赖

若尚未形成正文，而且已确定需要正式proof-checker审计，可在assemble阶段直接选 `PROOF.tex`为唯一canonical正文。原生定理/证明环境直接交审计，不先生成Markdown、转换稿和额外SOURCE_MAP；用户需要其它阅读视图时再从该正文生成。已有项目和用户指定格式仍沿用，不为适配更换正确源文件。

已有 `.tex` theorem/proof 工程时，给完整相关入口、实际 `input/include` 内容、引用原材料与代码。声明本次 input set；checker 按它自己的 source-unit extraction、完整读取、全局 ledger 和 reviewer 合同工作。引用了某个本地引理，只给结论不让 reviewer 找到证明，会留下未读依赖；允许作为进口时明确它的完整条件和接受范围。

完整审计可以在现用 proof/paper 目录执行。真正 checker 会写那里约定的 `PROOF_AUDIT.json`等产物；原输入 freshness 沿它自己的 artifact合同保存。MathRSI `VERIFICATION.md`只链接真实结果，不手动补 PASS JSON。

## Markdown 证明：可读原稿保留，另造逐段可追溯审计输入

当前 checker 以 TeX theorem/proof 环境、`.tex` source units和对应 detector 为主。它虽接受自然语言 proof description，但没有保证所有 Markdown标题都会成为 theorem inventory。只把 `PROOF.md`路径交给它，然后接收“无theorem”并不能审清这个证明。

已有Markdown需要保留并要运行正式审计时，在任务现有审计位置准备TeX输入，例如 `verification/full-proof/main.tex`；原 `PROOF.md`仍为正文源。先完整读Markdown，按其原有定义、定理/引理、假设和证明结构转为TeX。使用已有可靠转换流程或直接编辑均可，不为这项任务写一个通用转换平台。短稿的原文↔TeX对应可直接写入已有audit说明；多章节或复杂转换有实际阅读需要时才另设 `SOURCE_MAP.md`。

转换仅改变载体：保留原对象、量词、假设、公式、常数、分支、依赖和证明次序。把原文的每个定理/引理放入可识别 theorem/lemma环境，其证明放 proof环境；定义和允许进口也保持显式。文本引用应保持对应来源，代码/证书仍引用实际文件，不能用“所有检查通过”一句话替换原论证。若需要定义 LaTeX环境或展示宏，它们不承载额外数学。

源对应记录至少按实质源单元给出原Markdown标题/行号或稳定段落、对应TeX环境/label/行号，以及真实转换差异；短稿可用一段audit说明，不强制额外文件。原句必要时直接并列，尤其是假设、量词、阈值、边界和结论。映射是可阅读对应，不是另一套hash系统；已存在git revision或准确diff可复用。正文改动后更新受影响的TeX与对应记录，旧audit不自动覆盖新正文。

checker可能在修复阶段直接改审计TeX。此时必须把实质修复回写到canonical Markdown，核对对应假设、结论与证明，再更新原有源对应记录（若使用SOURCE_MAP则更新该文件）；必要时从已修Markdown同步TeX。保持一个正文owner负责这次往返，避免两个作者分别改不同载体。最终verify确认交付正文与最后实际审计输入表达相同论证；不能拿修好的TeX的PASS交付仍有旧错误的Markdown。若只改排版宏、不改论证，记录这个差别即可，不重做数学。

调用checker时同时给原Markdown、审计TeX、源对应记录、原规格与依赖，要求核对载体未改变命题。审计的declared theorem-bearing input set包含实际TeX。`VERIFICATION.md`另外指出原稿和适配位置的关系、核对范围及原文后续变化；不要把上游只列TeX的输入身份说成已经自动追踪了所有原Markdown修改。

转换中发现原文缺定义或证明，不由适配者补成已证。回到 assemble/prove修原源，再同步TeX。若TeX无法诚实表达原证明，保持适配pending，先对具体义务做本地核验或 research-review；不能把较弱转写的通过当原稿通过。

checker 的编译与报告阶段按原入口执行。缺TeX引擎或引用源就记录实际环境/交付限制，已有数学核验照实保留，不虚构编译成功，也不为调用自动升级工具链。没有用户要求的依赖不预先安装。

## 局部义务：三种不同强度

一项算术重算直接由确定性程序执行，报告其准确谓词、输入域、结果和连接，不因此调用整个 paper audit。

一个归约、接口或候选引理的具体疑问可使用 `research-review`。让 reviewer读原始定义、局部证明与caller，问“这个推理和实际输入是否成立”。它的研究评分或意见不是canonical proof-checker verdict，VERIFICATION保持这种区别。

要对局部定理执行严格 proof-checker，可以在任务的专用目录如 `verification/lemma-L/`准备**自足局部输入**：精确声明、完整局部证明、它所用的定义/前提/进口、实际caller及需要追溯的依赖。已有相关TeX直接指定它；Markdown按上述方式转写并保留原文对应。只隔离范围，不能把正在被质疑的结论改成假设以获得通过。

局部目录真实产物仍可叫 `PROOF_AUDIT.json`，但其scope明确是L及所声明依赖；不得覆盖 `verification/full-proof/PROOF_AUDIT.json`或把局部audit当整个原题的audit。完整主证明如何使用L、其它分支是否齐备仍需在最终装配验证。

## 可直接发出的适配后调用

```text
读取本仓当前宿主 proof-checker/SKILL.md 并执行其完整适用流程。
本次scope是 PROOF.md 中的完整原定理，审计工作目录 verification/full-proof/。
主TeX输入是 verification/full-proof/main.tex；必须一起读原文PROOF.md与
已有audit中的源对应说明（复杂稿使用SOURCE_MAP.md）以核对逐段对应。
原题 FORMAL_SPEC.md；引用和依赖见证明中的真实路径。
请按source-unit覆盖、义务ledger、反例、修复及复审合同完成，
保存你真正的PROOF_AUDIT产物；若必要源未读或证明缺口仍在如实报告。
不要把Markdown没有可识别theorem环境误判成原定理无需审计。
```

实际路径由任务替换。若是局部审计，把第一句scope换为精确局部定理，列出其允许进口与原caller；不要沿用“完整原定理”字样。

## 宿主差异继续保留

Claude主线 checker Phase3复用reviewer thread，Codex版每轮fresh agent；它们的state记录、可用flags不同。使用对应入口，不从本适配文复制另一宿主的调用模板。route selection只能改变review transport，不能取消scope、source coverage、反例pass、blind review或确定性义务。

checker顶部/表格若对不可用review使用不同术语，保留真实失败与其实际artifact中的raw状态，VERIFICATION说明未完成；不由caller把未知状态改成PASS。`NOT_APPLICABLE`仅表示该次输入没有被检测到适用定理，不是可读原稿被证明。
