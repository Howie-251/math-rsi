# 本机 ARIS Lean 技能安装 — 2026-10-07

已按用户要求完成 Codex 与 Claude Code 双端安装，每端新增 `lean-formalize`，并更新 `proof-writer`、`proof-checker`、`proof-orchestrator`、`formula-derivation`、`research-pipeline` 五个技能入口。入口按具体证明义务和用户需要转入 Lean，普通数学任务不默认启用。

| 宿主 | 上游目录 | 安装目录 | 结果 |
| --- | --- | --- | --- |
| Codex | `aris_main/skills/skills-codex/` | `/Users/rfy_naiveai/.codex/skills/` | 新增 1，更新 5 |
| Claude Code | `aris_main/skills/` | `/Users/rfy_naiveai/.claude/skills/` | 新增 1，更新 5 |

源仓库为 `/Users/rfy_naiveai/Desktop/aris_main`，提交 `26b95cfa0d8747078e9e43b42e20952709e561b8`。Lean 技能及入口来自已合并的 PR #461。

## 更新方式与私有配置

复用 `tools/smart_update_codex.sh` 和 `tools/smart_update.sh`，向更新器提供仅含六个目标技能的临时上游目录。预览后执行 `--apply --add-new`，未向更新器提供共享配置目录。

更新前，十份已有入口文件均与 Lean PR 合并前的对应上游文件一致；完整目录对比也确认差异仅在 `SKILL.md`。Claude 更新器完成新增和五项更新。Codex 更新器保守地将已有差异归为需合并，因此只新增技能；随后逐个核对备份未变化，再同步已审查的五份 `SKILL.md`，保留其他资源。

已有 `shared-references/reviewer-routing.md` 和 `fan-out-pattern.md` 在两端均与更新前内容逐字节一致。其他技能和本地私有资料不在此次更新范围。未更改 MCP 配置。

## 安装核验与调用

- 两端共十二个目标技能目录，其文件集合及内容分别与正确宿主的上游目录完全一致。
- 新技能两端的本地 Markdown 引用均存在，三份参考文档完整；Codex 同时包含 `agents/openai.yaml`。
- 五个已有技能均包含 Lean 入口；`~/.aris/repo` 仍指向本机 ARIS 主仓库。
- 这里核验的是本机技能安装，不是重新运行数学证明或外部模型审阅。

Codex 下一轮可尝试 `$lean-formalize`，Claude Code 可使用 `/lean-formalize`；已打开的会话若未显示，重开会话加载。磁盘安装已核验，界面加载以各会话的实际技能列表为准。

同目录保留 `plan.json`、双端 dry-run/apply 日志，以及 `before/` 中的原入口文件和两份共享配置备份。
