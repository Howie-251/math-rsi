# ARIS 实现入库报告 — 2026-11-01

已完成有界上游实现快照：真实技能、随附资源、两套 shared references 与 helpers 进入 MathRSI `base/`。不需要源作者的另一份 `aris_main` 目录。所有上游内容按固定提交原字节保存，MathRSI 说明和测试另外编写；未调用上游安装器、修改全局安装、调用付费模型、创建 Goal 或提交 Git。

## 来源与数量

- 上游：`https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep`。
- 固定提交：`c485faa59a68e51c6575dea67ca57abc7a6a2b9c`。
- 复制方式：从该 commit 的 `git ls-tree -r` 筛选路径，使用每个 tracked blob 的原始字节，保持 `100644/100755` 模式。工作树的 untracked 文件、缓存、仓库 `.git`、用户资料与凭据没有进入快照。
- 源文件清单：[`base/ARIS_SNAPSHOT.json`](../../base/ARIS_SNAPSHOT.json)，每项保存源路径、源 Git blob、模式、字节数。MIT 许可证在 [`base/LICENSE`](../../base/LICENSE)。
- 上游合计：**207 文件 / 2,915,213 字节**。

| 类别 | 路径 | 数量 |
| --- | --- | --- |
| Claude 主线技能 | `base/skills/<selected>/` | 30 技能，44 文件 |
| Codex 适配技能 | `base/skills/skills-codex/<selected>/` | 30 技能，44 文件 |
| Claude shared references | `base/skills/shared-references/` | 32 文件 |
| Codex shared references | `base/skills/skills-codex/shared-references/` | 32 文件 |
| 工具目录 | `base/tools/` | 53 文件 |
| Claude bounded leaf | `base/agents/aris-fanout-leaf.md` | 1 文件 |
| MIT 许可证 | `base/LICENSE` | 1 文件 |

完整 selection：

```text
research-lit research-wiki wiki-enrich formula-derivation
proof-writer proof-checker proof-orchestrator research-review
auto-review-loop lean-formalize render-html citation-audit
system-profile novelty-check result-to-claim training-check
citation-crosscheck paper-compile analyze-results
arxiv alphaxiv deepxiv semantic-scholar openalex
exa-search keenable-search firecrawl-search web-debug-search gemini-search
paper-claim-audit
```

上游 catalog 的硬依赖闭合：wiki-enrich → research-wiki；proof-checker/citation-audit/paper-claim-audit → render-html；auto-review-loop → result-to-claim、training-check、render-html。所选30技能的 catalog 硬依赖都在 selection 中。原 catalog 为完整上游清单，保留它不意味着另外的专利、机器人、实验平台或全论文流水线也已复制。

实际资源包含 proof-orchestrator 的六份 references 与主线 NOTICE、Lean 的三份 references 和 Codex agent metadata、两宿主各自的 renderer 及两套模板。53 tools 保留同目录 import 和 shell 调用布局，包括 research_wiki → threat_scan、save_trace → review_gate。部分 tools 用于本包没有选择的上游技能，保留为原始支持源码；未测试或宣传其对应的省略技能可执行。

## 新增集成文档与测试

- [`base/README.md`](../../base/README.md)：版本、布局、调用边界。
- [`docs/ARIS_REUSE.md`](../../docs/ARIS_REUSE.md)：实际分阶段输入、执行方式、输出、外部依赖和数学适用范围。逐一链接全部30个实际技能，说明文献身份核验与数学解释、结果统计与全称证明、ML review分数与数学验收的差别。
- [`base/tests/smoke_bundle.py`](../../base/tests/smoke_bundle.py)：小型、纯离线、可重跑的副本集成检查；不提供新调度平台。
- [`base/tests/evidence/RESULT.json`](../../base/tests/evidence/RESULT.json)：9条实际命令、环境、cwd、退出码和输出；保留生成HTML及fixture wiki。

MathRSI 运行要求：每个 shell 显式设置 `ARIS_REPO=<当前MathRSI>/base`，通过仓库副本的绝对 helper 路径调用，不 fallback 作者其它安装。上游 resolver 的任务本地 `.aris/tools/`／`tools/` 优先于 ARIS_REPO，故文档明确要求确认本地 alias 或用绝对路径，避免假定 export 覆盖已有陈旧 helper。没有改写上游 resolver。

上游安装／更新脚本保留原字节，但本包设置不执行它们：其全局指针和绝对链接行为与便携副本目的不同。reviewer_route 仅解析路由，模型/MCP、登录、工具名与当前宿主能力仍须执行方检查。源码中的模型默认值如实保留，不能当当前服务能力已测；本轮未安装或探测模型服务。

## 真实验证

先运行实际 `--help`，确认 wiki `init/add_claim/ingest_paper/add_edge`、reviewer router 和 renderer 的参数；未猜测接口。然后执行：

```bash
python3 -B base/tests/smoke_bundle.py --out-dir base/tests/evidence
```

结果：**PASS**，207个源文件与manifest内原 Git blob全部一致。测试把副本搬到 `/private/var/folders/.../mathrsi-aris-smoke-.../relocated-base`，从另一个临时 `task-workspace` 使用绝对helper路径执行，每条子进程均显式设置该副本的 ARIS_REPO。原 HOME 未修改，未读取其它ARIS安装来补helper，命令不经过任何global fallback resolver。实际临时绝对路径完整留在 RESULT.json；临时目录已删除，输出已经复制入库。

| 实际调用 | 结果及检查范围 |
| --- | --- |
| wiki `init` | exit 0；本地wiki目录和导航生成 |
| wiki `add_claim --slug smoke-local-obligation --status unproven` | exit 0；claim明确保留未证状态，不是数学成果 |
| wiki `stats` | exit 0；实际wiki可读，query_pack存在 |
| router 默认 Codex | exit 0；解析为native默认路由 |
| router 项目Grok配置 | exit 0；读取任务`.aris/reviewer.json` |
| router inline `--reviewer gemini --effort high` | exit 0；正确归一化为Antigravity并覆盖项目选择 |
| router 非法backend | **预期exit 2**；拒绝未知路由，没有模型调用 |
| Codex renderer + academic模板 + `--offline` | exit 0；HTML与原公式文本保留，无MathJax/highlight CDN加载 |
| Claude renderer + dashboard模板 + `--offline` | exit 0；另一宿主完整模板路径正常 |

对所选技能目录中的 Markdown 本地链接做了实际路径检查：仅6处是上游示例字面量 `(url)`，其它真实文件目标齐全。两套shared references和skill资源路径保持原布局，没有为了链接检查改写上游原文。

`--offline`只关闭CDN，输出含原始数学文本，**没有预渲染／内嵌SVG公式**。这不能冒充Property B历史离线数学卷的排版流程；相应限制已在使用说明和RESULT中明确。

## 验证的实际边界

本轮验证的是本地文件来源、搬迁后的wiki/路由/renderer调用链。未运行文献网络API、第三方CLI、MCP reviewer、Lean、LaTeX、上游全量测试或被省略技能。复制源码不安装可选Python SDK，不等于外部服务可用；`requests`、Exa/Firecrawl认证、DeepXiv、Gemini CLI/MCP、具体reviewer bridge、Lean/Mathlib和TeX均在使用说明中按需列出。

ML导向的auto-review-loop分数、training-check、result-to-claim、analyze-results没有被宣称为数学真值验收。数学任务仍按原题连接、条件、全域覆盖、独立算术及实际形式证明的具体义务验收。仓库内已有mathrsi-research、根README/AGENTS和plugins由其它owner维护，本次没有改动。
