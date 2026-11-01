# 图与实际工作流：对齐、修复与真实试用

2026-11-01。用户要求核查两张图是否对应真实、可执行的工作流。结论是：**图2的解题主线有完整agent执行入口与产物消费；图1原先缺少明确的独立维护入口，本轮已补齐。可执行性由实际技能和宿主能力共同提供；不能把静态对齐、一个成功试用和完整长期研究效果混为一谈。**

## 核查与修复

独立Sol实际打开两张PNG，读取九项MathRSI入口，并追到ARIS原件、wiki argparse、领域checker和既有执行证据。[逐节点映射](ALIGNMENT_AUDIT.md)记录修改前的准确状态：主调度、文献回流、单一修法owner、局部verify返回、wiki读写及插件输入/返回均有明确实际衔接。

唯一必要的产品修复是把图1的“General workflow lessons → Distill · Review · Evaluate → next base”从原则补成 [EVOLUTION_WORKFLOW](../../docs/EVOLUTION_WORKFLOW.md)：维护owner读实际run/wiki → 区分单题、插件与base变化 → 修改真实caller/子技能/消费处 → 针对性审阅 → 未参与作者的使用者实际试走 → Root读证据决定修正、拒绝或纳入 → 记录实际版本和任务采用时点。README、主技能、WORKSPACE、PLUGIN_CONTRACT与WORKFLOWS均接入此入口。它不是第六个解题阶段，也不是发布v2或自动改核心的声明。

Gemini 4 Argon/high有效SUCCESS静态核读新入口、相关调用处及原research-review合同，认可该缺口已补齐，未发现新的真实接口冲突。原[请求](GEMINI_REQUEST.md)、[完整回应](GEMINI_RESPONSE.md)和[envelope](GEMINI_RAW.json)保存实际范围；它没有替代下面的实际试用，也没有宣称新长期研究通过。

## 新执行证据：接到有错误的完整证明之后

给未参与编写技能的Sol一个自包含原题和一份候选TeX，要求按主入口核查、修复及交接。没有提前告诉它预期漏洞或修法。它实际选择 `mathrsi-research → mathrsi-verify → proof-checker → mathrsi-handoff`，无需先重做文献/路线阶段。详见 [TRIAL_REPORT](trial/TRIAL_REPORT.md) 与 [CALLS](trial/CALLS.md)。

| 实际动作 | 产物与后继消费 |
|---|---|
| 首次fresh reviewer全文审原候选 | 返回FAIL：顶点颜色独立不能推出相交边坏事件独立 |
| 精确反例核验 | 五个顶点全部32种染色中，两坏事件各为1/8、联合为1/16而非1/64；只反驳原中间步骤 |
| 保持原题修复 | 以指标函数证明并集上界，得到任意四元、至多七边超图的合法染色概率至少1/8；原定理环境逐字不变 |
| fresh复审及另一次blind review | 两次均无数学问题；三位reviewer串行执行，真实原文与trace保存，same-family/provisional |
| 实际编译尝试 | 本机缺pdflatex，退出127；没有PDF，不把该阶段记成功 |
| 交付与恢复 | [完整可读证明](trial/PROOF.md)、VERIFICATION、[HANDOFF](trial/HANDOFF.md)、NEXT_SESSION说明成立结果和准确编译待办 |

Root读回完整证明、具体算例程序、原始问题与theorem一致性记录、audit和handoff，确认其全称结论来自解析证明，32例仅用于验证错误步骤的反例。未重跑原Property B或ECC研究。

该试用的数学audit为PASS，`acceptance_status=provisional`；同时 `details.workflow_complete=false` 明确保留TeX编译未完成。两种状态分别陈述，不能将数学审阅成功写成所有工作流操作均完成。已有Markdown可直接阅读；本轮没有为了核查安装全局TeX或改变用户服务。

## 现在能依据哪些证据判断

- **有具体执行证据**：已有领域证书复放、wiki/router/renderer副本运行、真实Gemini桥接续接、局部prove→verify→返回caller；本次新增有错误全稿→修复→复审→交接。
- **有明确代码/指令但未完整实测**：全新问题的联网调查到交付全链、路线A–E完整实作循环、新编排下的Lean、通用核心改进对长期研究效率的影响。它们不因图画齐而升级。
- **范围已知**：ECC是draft插件；v2为后续迭代方向；MCP需要实际CLI/登录，正式PDF需要TeX，Lean需要对应工程依赖。仓库自包含技能与桥接源码，不捆绑这些运行时。

使用方式仍是让宿主agent读取 `base/skills/mathrsi-research/SKILL.md`，给原问题、任务目录与需要的插件；agent按证据选入口并执行。这里的workflow是可读、可调用、可恢复的agent程序，不是假定有一个自动跑完所有研究的Python命令。

当前结构检查见[VALIDATION](VALIDATION.json)：Checked 61 documents and 983 local link targets; 0 missing. 旧61项MCP协议测试与未变资源验证复用，无无关重跑。完整运行依赖和未来实测仍按各自范围报告。
