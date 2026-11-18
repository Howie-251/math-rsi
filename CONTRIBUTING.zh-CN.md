# 参与贡献 MathRSI

[English](CONTRIBUTING.md) | [中文版](CONTRIBUTING.zh-CN.md)

感谢你关注并愿意参与 MathRSI 的建设！本文说明仓库结构、核心约定，以及如何贡献领域插件、核验器、工作流改进与文档。

## 贡献方式

- **领域插件与数学成果**：在 `plugins/<domain>/` 下新增领域插件，或补充现有插件的归约方法、失败诊断、精选证书与独立核验程序。
- **验证与形式化**：为现有工作手稿、计算证书或开放参数贡献独立重放核验脚本（`plugins/<domain>/tools/`）、有界反例检查或 Lean 4 形式化（[六题统一索引](case-studies/README.md)）。
- **Base 工作流改进**：基于真实研究瓶颈和实证证据，通过 [`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md) 提出并验证工作流改进（[演进维护指南](docs/EVOLUTION_WORKFLOW.md)）。
- **文档、公开阅读页与问题反馈**：修复命令或链接错误、澄清证明与核验边界、提交 bug 报告，或完善双语文档与公开阅读页（[公开站点说明](docs/PAGES.md)）。

## 开始之前

1. 在 GitHub 上 Fork 本仓库并克隆到本地（仓库维护者请在独立 `git worktree` 中工作）：
   ```bash
   git clone https://github.com/YOUR_USERNAME/math-rsi.git
   cd math-rsi
   ```
2. 为本次改动创建独立分支：
   ```bash
   git checkout -b feat/your-topic
   ```
3. 参考[快速上手](docs/QUICKSTART.md)，在 **Claude Code**（`/skill-name`）或 **Codex**（`$skill-name`）中运行与测试技能。

## 开发与仓库约定

### 三层边界

- **Base**（`base/`）提供领域无关的五阶段编排（`Prepare → Route → Prove → Verify → Handoff`）以及固定快照的 ARIS 副本（[`base/ARIS_SNAPSHOT.json`](base/ARIS_SNAPSHOT.json)）。不要在单题解题过程中把领域策略硬编码进 `base/`；如未同步更新上游溯源信息，请勿改动 `ARIS_SNAPSHOT.json` 锁定的文件（[来源说明](docs/PROVENANCE.md)）。
- **领域插件**（`plugins/<domain>/`）包含领域技能、数学参考、失败图谱、精选 `archive/` 归档输入与可运行的 `tools/` 检查器。请遵循[插件契约](docs/PLUGIN_CONTRACT.md)，并在 [`docs/DOMAIN_ROUTING.md`](docs/DOMAIN_ROUTING.md) 登记各阶段入口。
- **活跃任务工作区**在研究进行期间保存在仓库外部（如 `../my-problem/`，见[工作区与记忆](docs/WORKSPACE.md)）；待结果稳定交付后，再整理精选证明、核验程序与可复用方法收入 `plugins/` 与 `case-studies/`。

### 技能编写与双宿主发现

每个技能是一个 `SKILL.md` 文件，包含 YAML frontmatter（`name`、`description`）和可执行的散文指令，明确覆盖适用范围、前置输入、具体工具/资料调用、失败恢复与返回产物（[技能验收标准](docs/SKILL_ACCEPTANCE.md)）：

```markdown
---
name: my-domain-skill
description: 说明该技能处理的数学义务或研究阶段。
---

# 技能标题

写明适用范围、前置条件、数学参考、核验命令与返回约定……
```

新增 MathRSI 或领域技能后，请分别在 `.claude/skills/<skill-name>`（Claude Code）与 `.agents/skills/<skill-name>`（Codex）添加相对符号链接，以便双宿主同时发现。

### 证据诚实与文件体量约定

- **准确标注验证范围**：清晰区分结果属于 Lean 形式化验证、独立程序完整重放证书、跨模型或同族初步审阅（provisional），还是未经独立审阅的工作手稿。切勿私自拔高结论等级，也不要移动已固定的版本标签（`v1`–`v6`）。
- **可读源文件、单文件 `< 50 MiB`、禁用 Git LFS**：请将精选证明、源码与紧凑证书直接解包提交，**不要**提交未解包的 `.zip` 或 `.rar` 压缩包。单个入库文件必须**小于 50 MiB** 且不使用 Git LFS；被省略的大型 SAT/CNF/DRAT 轨迹或搜索池请登记在对应目录的 `INVENTORY.json` 中，注明字节数、SHA-256 哈希与复现方式。

## 提交前检查

提交前请在仓库根目录运行以下离线标准库检查：

```bash
# 1. 检查本地 Markdown 链接与 .claude/.agents 技能软链接
python3 tools/check_links.py

# 2. 若修改了 base/，运行捆绑 ARIS 快照与离线辅助工具冒烟测试
python3 base/tests/smoke_bundle.py --out-dir /tmp/mathrsi-smoke

# 3. 若修改了公开主页或阅读页，检查白名单站点构建
python3 tools/build_public_site.py --output /tmp/mathrsi-site
```

如新增或修改了 `plugins/<domain>/tools/` 中的领域检查器，也请在真实输入上运行验证，并在 Claude Code 或 Codex 中实测受影响的技能。

## Pull Request 流程

1. 保持每个 PR 聚焦单一明确的改动，并编写清晰的提交说明。
2. 若新增技能、插件或关键数学结果，请同步更新 `README.md`、`README.zh-CN.md` 与 [`docs/DOMAIN_ROUTING.md`](docs/DOMAIN_ROUTING.md)。
3. 在 PR 描述中写明实际验证范围，以及尚未验证的分支或外部依赖。

### PR 检查清单

- [ ] 链接与 `.claude`/`.agents` 技能软链接通过 `python3 tools/check_links.py`
- [ ] 已准确说明验证状态、审阅范围与材料来源
- [ ] 未提交原始 `.zip`/`.rar` 压缩包、Git LFS 对象或 `>= 50 MiB` 的大文件
- [ ] 已在本地实测受影响的领域核验器、技能及冒烟/站点构建脚本

## 行为准则

- 保持尊重、建设性与实事求是的讨论氛围，以可复现的数学和程序证据为准绳。
- 严格区分已确立的定理、有界计算核验与尚未闭合的猜想或工作手稿。

## 问题与联系

如有 bug 反馈、使用疑问或研究合作意向，欢迎在仓库中提交 GitHub Issue。

## 开源协议

向 MathRSI 的工作流、文档与脚本提交贡献，即表示你同意这些贡献采用 [MIT License](LICENSE) 开源；归档论文与第三方原始材料保留其各自原版权（[来源说明](docs/PROVENANCE.md)）。
