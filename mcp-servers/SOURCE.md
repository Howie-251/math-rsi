# 桥接来源与本仓适配

来源为 [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)，固定提交 [`c485faa59a68e51c6575dea67ca57abc7a6a2b9c`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/c485faa59a68e51c6575dea67ca57abc7a6a2b9c)。复制时通过本地 Git 对象读取该提交，不依赖工作树中可能存在的修改。MIT 版权和全文许可保留于 [LICENSE.ARIS](LICENSE.ARIS)。

以下运行文件与该提交逐字相同：

- `grok-exec/server.py`
- `antigravity-exec/server.py`
- `antigravity-exec/aris-antigravity-review.md`
- `codex-exec/server.py`
- `claude-review/server.py`

这四个 Python 文件均是独立标准库程序，不 import 相邻桥接或 `base/`。因此无需复制 `gemini-review`、`llm-chat`、ARIS 安装器或原作者全局配置。随附 Python 协议回归测试来自上游 `tests/test_grok_exec_bridge.py`、`test_antigravity_exec_bridge.py`、`test_codex_exec_bridge.py`、`test_claude_review_parse.py`；将仓库根定位从测试上一级改为上两级，以适配 `mcp-servers/tests/`，并在 Codex 测试 fixture 的 `close()` 补上 pipe 关闭及 kill 后 wait，消除 Python 3.14 的资源警告。本仓新增 `test_bundle_contracts.py` 覆盖明确的 Gemini 4 请求、Codex 跨服务重启续接和 Claude 的实际 stdio／后台状态恢复。

同目录 README 以相同提交版本为底稿：加入本仓入口提示，适配测试目录，将未打包 `gemini-review` 的链接改为固定上游地址；Codex 注册步骤改指本仓，移除要求另克隆／更新 ARIS 的前提；Claude 说明移除未打包且依赖作者 shell 的 AWS wrapper 安装段。历史 CLI 版本与连通性记录保留为历史，不能当作 MathRSI 本轮实测。完整当前操作约定在 [REVIEWER_MCP](../docs/REVIEWER_MCP.md)。

加入 Codex 与 Claude 桥接的原因是现有 [reviewer_route.py](../base/tools/reviewer_route.py) 确实提供这两条路由：Claude Code 宿主的 Codex reviewer 需要 `codex` MCP；显式 `claude-code` reviewer 需要 `claude-review` MCP。Codex 宿主使用 native reviewer 时不需要再启动 Codex MCP。遗留 `oracle-pro`、`agy`、`manual`、`copilot` 等路由不是本套四服务的别名，继续按调用者的旧协议处理；没有据路由名称声称这些额外服务已打包或可用。
