# 在 MathRSI 内执行 ARIS 工作流

MathRSI 携带可以直接读取和执行的 ARIS 实现。`base/skills/mathrsi-research/` 负责数学任务的方向、衔接与范围；本页说明其调用的真实子技能、资源与命令。任务的原题、wiki、证明、源码与计算证据仍放在任务工作区。修订领域策略时修改插件，修订通用数学研究流程时修改 MathRSI；已复制的 ARIS 源文件保留原字节，需要升级时作为明确的上游更新处理。

## 实现位置、版本与宿主

上游固定为 [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/c485faa59a68e51c6575dea67ca57abc7a6a2b9c)，提交 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`。实际文件在 [`../base/`](../base/)，不依赖另一个 `aris_main` 工作目录。MIT 许可证与逐文件来源保存在 [`LICENSE`](../base/LICENSE) 和 [`ARIS_SNAPSHOT.json`](../base/ARIS_SNAPSHOT.json)。快照共 207 个上游文件、2,915,213 字节：两宿主各 30 个技能、各 44 个技能目录内文件，两套各 32 个公共资源，53 个工具，以及 leaf 和许可证。

Claude 读取 `base/skills/<name>/SKILL.md`，Codex 读取 `base/skills/skills-codex/<name>/SKILL.md`。不要把主线 Claude 的工具声明当成 Codex 工具名，或把两套 `shared-references` 互换。主线 `proof-orchestrator` 的 NOTICE、两个版本的六份 proof-orchestrator references、三份 Lean references、Codex 的 `agents/openai.yaml`、两套 HTML renderer/templates 均在原目录内。Claude bounded fan-out 使用 [`aris-fanout-leaf.md`](../base/agents/aris-fanout-leaf.md)。宿主若支持项目技能发现，可使用指向这些实际目录的仓库内相对别名；直接要求 agent 先读上述 SKILL.md 也能使用，不必执行全局安装。

每次调用一个技能，先完整阅读相应宿主入口，再按该入口读取相关 references。下表链接统一使用 Codex；Claude 用户把路径中的 `skills/skills-codex/` 换成 `skills/` 即可。参数示例中的 `/skill` 是主线写法；Codex 可用 `$skill` 或明确要求“读取仓库内该技能并执行”。宿主实际未提供的工具不能靠名称声明变成可用。

## 每个 helper 都绑定本副本

在**任务工作区**启动命令；在**同一个 shell** 设置绝对 `ARIS_REPO`。路径随克隆位置调整，不能读另一份 ARIS 或作者机器的 `~/.aris/repo` 来补资源：

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/tools/research_wiki.py" --help
```

后文每个命令块都重新设置该变量，因为 agent 的不同 shell 调用未必共享环境。上游源码包含通用 resolver，其顺序通常为任务 `.aris/tools/`、任务 `tools/`、`$ARIS_REPO/tools/`；没有变量时还可能查安装 manifest 与 `~/.aris/repo`。MathRSI 要求显式使用本副本的绝对 helper 路径。若执行上游技能内原 resolver 代码，先确认现有本地 helper 也属于本副本，或将本次实际调用改为绝对路径。旧任务目录里同名 helper 的优先级高于 `ARIS_REPO`，不能仅凭 export 宣称已固定版本。helper 缺失应修复本包或准确报告缺失，不能静默 fallback 外部仓库。

不运行 `install_aris*.sh`、`smart_update*.sh` 或 PowerShell 同类脚本进行本包设置。它们为完整上游安装服务，会写全局指针、绝对链接或安装状态；这里保留的是源码，MathRSI 的项目内调用不需要这些动作。`tools/skill-groups.tsv` 也是上游全量目录，用它看依赖时应与 `ARIS_SNAPSHOT.json` 的 selection 取交集；不能把目录中列出的所有技能都说成本包已有。

## 阶段一：先广泛发现，再从原题和现有知识提出具体问题

新题先按[文献发现闭环](../base/skills/mathrsi-research/references/literature-discovery.md)覆盖异名、等价命题、前后引用链、反例与勘误；不能只在既有wiki内查询。恢复同一已调查问题时做增量查漏。

输入是用户原题、现有已证／未证义务、领域插件的定义及旧失败记录。总控先决定需要补哪一条事实：找一个已有定理、核对归约条件、理解一篇论文，或辨明候选是否已有人做。已冻结命题不能因检索结果而被静默改成更弱命题。

使用 [`research-wiki`](../base/skills/skills-codex/research-wiki/SKILL.md) 查已有实体和关系，使用 [`research-lit`](../base/skills/skills-codex/research-lit/SKILL.md) 补文献。`research-lit` 先查可用的 Zotero／Obsidian／本地 PDF，再搜索；`sources: all` 按原技能只覆盖默认层，Semantic Scholar、DeepXiv、Exa、Gemini、OpenAlex 要显式列出。数学项目通常先用 `local, web`，再按缺口加 `semantic-scholar, openalex`。这只是选择建议，实际请求及可用服务决定来源。

例如要求“读取 research-lit，查有限超图二染色精确下界，sources: local, web, semantic-scholar；只解释与当前义务有关的定理和所需假设”。产物包括候选清单、身份核验状态、逐篇提取与覆盖、按问题组织的关系，以及精确到版本、页码和定理位置的原文依据。`verify_papers.py` 核验的是论文身份；它不能证明抽取的数学解释正确。没有原文／摘要等本地可读依据的 leaf 不应凭标题编造结论。取回原文后仍要由主代理核对量词、前提与调用位置。

本包携带的具体检索技能如下。使用前读相应入口；第三方服务的可用性与价格以实际环境核验，源码中的模型和服务默认值属于这次固定上游版本。

| 任务 | 实际技能 | 所需能力及产物 |
| --- | --- | --- |
| arXiv 检索、元数据、下载 | [`arxiv`](../base/skills/skills-codex/arxiv/SKILL.md) | `tools/arxiv_fetch.py` 与网络；记录实际版本和 PDF，下载行为遵循任务授权 |
| 单篇快速理解 | [`alphaxiv`](../base/skills/skills-codex/alphaxiv/SKILL.md) | AlphaXiv 页面及原文 fallback；摘要先帮助定位，关键证明仍核原文 |
| 分层读论文 | [`deepxiv`](../base/skills/skills-codex/deepxiv/SKILL.md) | `tools/deepxiv_fetch.py`、第三方 `deepxiv` CLI/SDK、其实际认证；输出段落／章节依据 |
| 正式发表记录 | [`semantic-scholar`](../base/skills/skills-codex/semantic-scholar/SKILL.md) | `tools/semantic_scholar_fetch.py`、网络；输出 venue、作者、标识符及可用摘要 |
| 开放引文与机构元数据 | [`openalex`](../base/skills/skills-codex/openalex/SKILL.md) | `tools/openalex_fetch.py`、Python `requests`、网络；输出可追溯记录 |
| 网页搜索和内容提取 | [`exa-search`](../base/skills/skills-codex/exa-search/SKILL.md) | `tools/exa_search.py`、`exa-py` 与 Exa 凭据；按需启用 |
| 免 key 网页检索／抓取 | [`keenable-search`](../base/skills/skills-codex/keenable-search/SKILL.md) | `tools/keenable_search.py`、Python 标准库及外部网络服务；实际失败应保留 |
| 网页全文 Markdown | [`firecrawl-search`](../base/skills/skills-codex/firecrawl-search/SKILL.md) | `tools/firecrawl_search.py` 与 Firecrawl 凭据／端点；按实际服务约定使用 |
| 软件报错检索 | [`web-debug-search`](../base/skills/skills-codex/web-debug-search/SKILL.md) | Web 搜索和官方技术资料；用于 Lean/API/工具问题，不能充当论文证明依据 |
| 多角度文献发现 | [`gemini-search`](../base/skills/skills-codex/gemini-search/SKILL.md) | `gemini-cli` MCP 或已认证 Gemini CLI；这是检索路由，与 Antigravity reviewer 协议有别 |
| 候选查新 | [`novelty-check`](../base/skills/skills-codex/novelty-check/SKILL.md) | 候选的明确贡献与相似文献；输出差异及证据，未搜到相似结果不等于已证全新 |

不需要为同一问题同时调用每一种服务。先使用已有资料和一个足以回答问题的来源；确有缺失再扩源。凭据只进入相应运行环境，不放进 wiki、prompt 或证据输出。拷贝这些技能不安装或验证远端服务，也不要求把服务 key 交给 MathRSI。

## 阶段二：把文献和结论接回任务 wiki

输入为实际读到的论文元数据、关键断言、证明义务及现有 wiki。已有 `research-wiki/` 时复用其实体和关系；不要初始化覆盖原库。新任务确实没有 wiki 时，可用真实 helper 创建。下面命令是经 `--help` 核实的本副本接口：

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/tools/research_wiki.py" init research-wiki/
python3 "$ARIS_REPO/tools/research_wiki.py" ingest_paper research-wiki/ \
  --title "实际论文标题" --authors "实际作者" --year 2026 \
  --venue "实际版本或刊物" --thesis "本次核读支持的一句结论"
python3 "$ARIS_REPO/tools/research_wiki.py" add_claim research-wiki/ \
  --slug candidate-main --name "当前候选命题" --status unproven \
  --statement "原量词和准确命题" --evidence "待完成的实际义务及现有材料路径"
```

示例标题与作者是占位符，不能原样写进真实研究。论文已知 arXiv ID 时使用 `ingest_paper --arxiv-id <id>`；这会访问网络。手工元数据形式适用于离线或无 arXiv 的来源。本 helper 会生成页面、更新索引和 query pack；不要另起第二个 wiki 管理器。状态 `verified` 只能在对应数学或计算义务的真实验收之后使用，helper 接受该字符串本身不构成验收。

[`wiki-enrich`](../base/skills/skills-codex/wiki-enrich/SKILL.md) 用于补足 paper 页的 TODO。输入是未充分展开的页面和可读论文，输出是实际读过的核心贡献、公式、条件与关系；缺资料的部分保持待读，不用模型常识填成事实。对候选结论用 `add_claim`，已有实体间的关系用 `add_edge --from ... --to ... --type ... --evidence ...`，每条边都写出依据。原题失败、限制条件和重启条件也留在任务记录，以便后续研究直接复用。

## 阶段三：从推导线到完整证明

[`formula-derivation`](../base/skills/skills-codex/formula-derivation/SKILL.md) 接收尚未完全固定的理论对象、假设、散落公式和目标，帮助选择主对象并形成推导线。产物应明确符号、每一步来源、常数／参数依赖与尚待证明部分。其原始定位包含 ML/AI 理论；应用到组合、优化或数论问题时，使用符合该问题的定义与证明，不虚构训练目标或实验评分。

当命题已经足够明确，交给 [`proof-writer`](../base/skills/skills-codex/proof-writer/SKILL.md)。输入必须包含原命题、允许进口的定理、已有正确引理和具体缺口。产物是完整论证、精确的条件定理、严格反例，或明确定位仍无法完成的义务。一个条件引理应保留长期价值，同时主目标仍记录尚未接上的条件；不得把条件定理写成原题已证。

跨运行续接和困难义务交接使用 [`proof-orchestrator`](../base/skills/skills-codex/proof-orchestrator/SKILL.md)。它有实际 run 目录、来源快照、local proof、audit、next 与人工 GPT Pro 交接合同；读取它自己的 `references/`。优先本地完成，只有出现具体卡点才准备窄交接包。该技能的 GPT Pro／DeepSeek 分支按原入口约定另行授权，不能把调用本地 orchestrator 当成上传材料或付费调用授权。新 run 保留旧 run 的来源和未解义务，避免反复重读或覆盖历史。

## 阶段四：按义务选择审阅与验证

输入是原命题、完整候选、所需进口与实际证据。优先确定尚存疑问：是归约保真、全域覆盖、算术值、形式化接口，还是论述不清。然后只把相关材料给相应检查，不以整篇反复送审代替补缺口。

[`research-review`](../base/skills/skills-codex/research-review/SKILL.md) 适合路线、方法与证据是否支撑研究目标的具体判断；[`proof-checker`](../base/skills/skills-codex/proof-checker/SKILL.md) 负责严格证明审计、义务清点、发现和修复缺口，并保留 `PROOF_AUDIT` 等约定输出。两者使用实际 reviewer 路由。先解析路由，之后检查本轮宿主是否提供所需工具，再发起已授权调用：

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/tools/reviewer_route.py" \
  --project "$PWD" --host codex --tier deep --reviewer grok
```

这个命令只输出配置，不调用模型、不检查登录、不证明 MCP 已加载。选择按 inline 参数优先于任务 `.aris/reviewer.json`，再到 host default；路由的模型名与工具名是固定上游描述，具体执行必须匹配当前宿主真实能力，例如 native continuation 不能凭字符串 `send_input` 假定存在。记录请求值、实际返回身份／effort、完成状态、读过的主文件和是否执行命令。默认 Codex reviewer 属于 same-family，语义接受记录为 provisional；跨家族有效审阅、实际确定性复算、Lean 检查各报告其范围。服务失败不能算接受或悄悄换成主代理自审。

[`auto-review-loop`](../base/skills/skills-codex/auto-review-loop/SKILL.md) 已完整复制，包括硬依赖 [`result-to-claim`](../base/skills/skills-codex/result-to-claim/SKILL.md)、[`training-check`](../base/skills/skills-codex/training-check/SKILL.md)、[`render-html`](../base/skills/skills-codex/render-html/SKILL.md)。它原生是 research/ML 迭代流程，有默认四轮、训练健康、结果到 claim、分数及 stop threshold。数学固定命题不能用其 `score >= 6` 或 `ready/almost` 当真值判定，也不应无训练任务时强行造训练指标。仅在实验型任务符合原流程时完整调用；纯证明的迭代由数学总控围绕实际未闭义务调用 proof-writer／proof-checker。需要研究评审循环时，保留原有退出和失败语义，另以任务冻结的数学验收判定定理是否成立。

[`analyze-results`](../base/skills/skills-codex/analyze-results/SKILL.md) 处理实际 JSON/CSV、比较、统计与观察，适用于启发式搜索效率、计算开销、数值实验等。区分原始观察、解释与下一项检验；多 seed 结果或统计显著不等于全称命题的证明。确定性验证仍须按插件与原题检查完整对象域、实际输入连接和算法可靠性。

[`system-profile`](../base/skills/skills-codex/system-profile/SKILL.md) 用于实际瓶颈。输入为程序、工作负载和当前 CPU/内存/GPU/IO 环境，输出是测量数据与可验证的改进方向。数学程序不用 GPU 时直接量相关 CPU／内存／读回成本；不为遵循该技能虚构训练负载，不把模型并行数当实际机器可承载计算并发。

## 阶段五：需要 Lean 时接原题、查类型与公理

[`lean-formalize`](../base/skills/skills-codex/lean-formalize/SKILL.md) 可实现、续写或审计 Lean 工程，携带三份完整 reference。输入是精确命题、已用对象、工具链／Mathlib 版本、实际模块及未闭义务。先对齐形式表达，再实现关键数学和真实 caller；用实际指定模块构建。默认 `lake build` 若只构建旧入口，不能代表新定理已验。

产物必须包括原命题到形式结论的连接、实际导出类型、传递公理、构建／独立导入命令及结果、尚需的外部进口和可复现交接。`Certificate H → Target H` 编译通过还需要为任意原始 H 构造证书。证明缺口不能通过新增未证 axiom、悄悄假设分类表或更换定义来消失。Lean 工具链和 Mathlib 是各任务环境，未随本技能副本预装；本次集成 smoke 也没有构建 Lean。

普通数学短证明或数值最优性证书不默认强制 Lean。选择 Lean 的理由是用户要求或具体义务能从形式验证获益；它与确定性独立实现、进口定理的出处核对承担不同职责。

## 阶段六：引用、数字和阅读交付

[`citation-audit`](../base/skills/skills-codex/citation-audit/SKILL.md) 需要论文／证明中的实际引用、bibliography 与原始来源，检查存在性、归属和引用上下文。尤其要检查所用定理的版本与假设，不能凭条目真实就宣布进口正确。

[`citation-crosscheck`](../base/skills/skills-codex/citation-crosscheck/SKILL.md) 提供 bibliography 字段级交叉核对，输出并排字段与差异表。真实双盲依赖宿主能隔离 web extractor 的上下文；无法隔离时按原技能标 `blind:false`，仅作为提示差异的 heuristic，不能宣称双盲认证。表格导出和原文抓取所需能力按入口核验。最终字段判断由主代理依据一手来源完成。

[`paper-claim-audit`](../base/skills/skills-codex/paper-claim-audit/SKILL.md) 将正文中的数字／比较／范围连到原始结果。用于计算机辅助证明时，核对范围和证据的工作有价值；其论文实验导向不能取代证明归约及完整覆盖检查。

[`paper-compile`](../base/skills/skills-codex/paper-compile/SKILL.md) 接收实际 LaTeX 工程，检查编译错误、文献与输出版面并生成 PDF；它需要 LaTeX 引擎及项目字体、宏包和资源。PDF 成功生成只验证可编译和相应展示，不证明数学内容。本包未捆绑 TeX、工具链缓存或论文数据。

[`render-html`](../base/skills/skills-codex/render-html/SKILL.md) 是实际 Markdown/JSON renderer，位于技能自己的 `scripts/render_html.py`，其 `scripts/templates/academic.html` 与 `dashboard.html` 必须保持相邻。没有 `base/tools/render_html.py` shim。下面命令与真实 `--help` 一致：

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/skills/skills-codex/render-html/scripts/render_html.py" \
  proof.md --template academic --out proof.html --title "Proof" --offline
```

`--offline` 去掉 MathJax/highlight.js 的 CDN 加载，公式保留原始数学文本；它不会预渲染或嵌入公式 SVG。需要像 Property B 历史交付那样离线显示完整排版公式，应另外使用已有任务的实际生成流程并验证结果，不能将这一选项宣传为同等产物。联网模式也须检查浏览器中实际显示、长公式和窄屏。renderer 退出零与页面忠实核查是不同证据。

## 可重跑的离线副本检查

```bash
python3 -B /path/to/MathRSI/base/tests/smoke_bundle.py \
  --out-dir /tmp/mathrsi-aris-smoke-evidence
```

该小检查核对快照的 207 个源文件 Git blob 身份，把 base 搬到独立临时路径，从不同任务工作区通过绝对路径执行本副本的 wiki 初始化／未证 claim 写入／stats、路由默认／项目／inline 优先级与非法 backend，以及两个宿主的两种 HTML 模板。它不改 HOME、不运行 upstream installer、不访问网络、不调用付费模型，不测试 Lean/LaTeX 或通用研究效率。

已运行的 [`RESULT.json`](../base/tests/evidence/RESULT.json) 保存全部 9 条实际 argv、cwd、ARIS_REPO、退出码、stdout/stderr；[`academic.html`](../base/tests/evidence/academic.html) 与 [`dashboard.html`](../base/tests/evidence/dashboard.html) 是离线 raw-math 展示样例，fixture wiki 中 claim 明确为 `unproven`。临时执行目录结束后已删除；已保留输出可查。集成报告在 [`BUNDLE_REPORT.md`](../development/aris-integration/BUNDLE_REPORT.md)。这项验证只说明本地调用链和资源齐全；任何新数学结论仍须按上述对应义务验收。
