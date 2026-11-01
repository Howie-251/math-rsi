# MathRSI 的 ARIS 实现副本

这里保存实际 ARIS 工作流、资源与 helpers。MathRSI 的数学总控技能位于 [`skills/mathrsi-research/`](skills/mathrsi-research/)；它在适用阶段调用下面的实现。完整用法与输入输出见 [`../docs/ARIS_REUSE.md`](../docs/ARIS_REUSE.md)。

来源是 [Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) 的固定提交 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`。[`ARIS_SNAPSHOT.json`](ARIS_SNAPSHOT.json) 逐文件列出源路径、Git blob、原模式与字节数；[`LICENSE`](LICENSE) 保留上游 MIT 许可证。上游文件按该提交原字节保存；MathRSI 的说明与测试单独存放，不改写上游实现。

- `skills/<name>/`：30 个 Claude 主线技能的完整目录。
- `skills/skills-codex/<name>/`：对应 30 个 Codex 适配目录。两个宿主版本分别保留。
- `skills/shared-references/` 与 `skills/skills-codex/shared-references/`：各 32 个完整公共资源，保持原相对路径。
- `tools/`：上游 53 个非缓存文件，保留 sibling imports。选中技能使用其中的 wiki、检索、路由、证据与 trace helper；其它工具按原样保留为支持源码。
- `agents/aris-fanout-leaf.md`：Claude 有界只读 leaf 定义。
- `tests/smoke_bundle.py`：MathRSI 编写的离线副本集成检查；`tests/evidence/` 保存实际输出。

从任务工作区运行 helper，每次在同一个 shell 明确设置本副本；下列路径按实际克隆位置修改：

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/tools/research_wiki.py" --help
```

必须使用这个仓库内的绝对 helper 路径，或确认任务目录的 `.aris/tools` 实际指向本副本。上游 resolver 优先本地 `.aris/tools/` 与 `tools/`，仅设置 `ARIS_REPO` 不会覆盖旧本地 helper。不能用作者的其它 ARIS 安装或 `~/.aris/repo` 补齐本包。不要运行本副本的安装／更新脚本来完成 MathRSI 设置：它们保留了上游写全局指针和绝对链接的行为。宿主发现与调用说明见集成文档。

技能源码自包含；网络服务、MCP reviewer、Python 可选 SDK、Lean/Mathlib 与 LaTeX 工具链仍按具体任务准备。保留的工具目录含面向未选技能的 shim，不能把它们当作已交付的技能；以快照清单中的 selection 为准。
