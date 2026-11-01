# Actual reviewer MCP bundle — 2026-11-01

已将 ARIS 提交 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c` 的实际 Grok、Antigravity、Codex、Claude-review stdio Python 桥接复制到仓库根 `mcp-servers/`。四个 `server.py`、Antigravity review agent 和 ARIS MIT license 均与该提交逐字比较相同。没有新增运行时 Python 协议层，也不依赖原作者的 ARIS checkout。当前集成指南为 [REVIEWER_MCP](../../docs/REVIEWER_MCP.md)，具体适配清单为 [SOURCE](../../mcp-servers/SOURCE.md)。

四条现代 route 均有实际实现：Grok／Gemini 为当前指定跨家族 reviewer，Codex bridge 支持 Claude Code 宿主的 Codex route，Claude-review bridge 支持显式 `claude-code` route。Codex 宿主的 native reviewer 仍由宿主提供。遗留 reviewer route 不冒充已打包服务；机器专用 AWS wrapper、另一套 `gemini-review` 后端及其 API SDK 未带入，四个当前桥接不依赖它们。

Python 依赖完全为标准库（上游声明 3.9+；本轮实际使用版本见 CHECKS.json）；无 pip 包。运行时另外需要已安装且登录／provider 配置有效的对应 CLI、账户模型权限与网络。Antigravity 需要安装随附 agent，并满足所安装 CLI 对 `--sandbox` 的运行时要求；没有声称预装了 CLI、登录、Docker、配额或模型。上游 Antigravity fallback 保持 Gemini 3.8，指南以注册环境和显式首轮参数落实本次 Gemini 4 Argon／high；Grok 使用 4.7／xhigh。

验证命令在仓库根执行：

```bash
python3 -m unittest discover -s mcp-servers/tests -p 'test_*.py' -v
```

最终 **61 项通过，exit 0，18.342 秒**。原始输出为 [OFFLINE_TESTS.txt](mcp-evidence/OFFLINE_TESTS.txt)，环境、来源逐字比较、各文件标准库 imports、测试数与本地链接检查见 [CHECKS.json](mcp-evidence/CHECKS.json)。注册命令的 `--env`／`-e`／scope 等选项用本机 CLI 的只读帮助核实，输出保留于 [REGISTRATION_HELP.txt](mcp-evidence/REGISTRATION_HELP.txt)。

| 范围 | 实际测试 |
|---|---|
| Grok | initialize／工具列表／真实 stdio 接线、长提示临时文件及清理、请求与实际模型／effort、服务重启后的固定参数续接、终态错误、ping／进度／取消、超时／宿主断开；新增断开后 fake CLI PID 已回收 |
| Antigravity | 同类协议与长提示、固定 agent／sandbox、服务重启续接、缺元数据为 null、错误模型／effort／ID、ERROR／WAITING／空／非零退出、取消／超时／断开；新增显式 Gemini 4 请求与续接、超时后 fake CLI PID 已回收 |
| Codex | 参数／TOML、实际 stdio schema、请求输入、失败终态及原文、进度／ping／取消、固定设置续接；新增服务重启后重新施加 model／effort／cwd／sandbox |
| Claude | 上游 JSON／NDJSON parser、实际／请求模型区分、同步与异步 cwd、失败终态；新增真实 stdio 五工具 surface、重启后的 reply 与显式 tools／model、后台 job 重启后查回、失败／空／截断／超时及直接子进程回收 |

上游四个测试文件只适配仓库根定位；Codex 测试 fixture 另补 pipe 关闭和 kill 后 wait，消除 Python 3.14 资源警告。新增覆盖集中于 `mcp-servers/tests/test_bundle_contracts.py`。首次执行新增 Antigravity PID 检查时，0.5 秒的超时早于 fake CLI 日志生成，故没有可检查 PID；测试窗口改为 2 秒后最终全套通过。运行源码未因此修改。清理测试证明的是这些 fake CLI 情形；Claude 原桥接同步取消没有整棵进程树清理保证，文档保持这一实际限制。

本执行者未发起付费模型调用，未改用户全局 MCP 配置、CLI 登录或凭据，也未改 `base/` 的上游快照。当前宿主目录可见已有 Grok、Antigravity 与 Claude-review 工具，但未据此断言它们运行本仓副本；没有发现 `mcp__codex__codex`。Root 后续的真实模型咨询与本包实测须另存实际范围和原始结果，不能将本报告的离线通过升级为数学审阅通过。

供 Root 复用的 stdio test fixture：`test_grok_exec_bridge.Client(env, cwd)`、`test_antigravity_exec_bridge.Client(env, cwd)` 提供 `send`、`recv`、`call`、`close`，`SERVER` 已指本仓副本。直接构造 Client 不执行 fake setUp；真实长调用应用 `send()` 后从其 `queue` 按请求 ID 收取结果和通知，避免 `recv()` 默认 5 秒等待影响长审阅。它们仍是测试 fixture，不另包装为运行时通用客户端。

## Root随后执行的真实调用

本报告的离线测试完成后，Root直接启动打包的Antigravity/Grok服务实测：Gemini同会话续接成功，Grok新请求600秒超时。准确命令方式与原响应见[LIVE_MCP_EXECUTION](LIVE_MCP_EXECUTION.md)；不改变上述离线测试的范围。
