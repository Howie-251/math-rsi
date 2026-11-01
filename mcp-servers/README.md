# MathRSI 本地 reviewer MCP

这里包含可直接执行的 ARIS Python 桥接，不要求另一份 ARIS checkout。安装、模型选择、首轮／续接和故障处理见 [完整操作说明](../docs/REVIEWER_MCP.md)。源码与许可证来源见 [SOURCE](SOURCE.md)。

| 服务名 | 实现 | 底层依赖 |
|---|---|---|
| `grok` | [grok-exec/server.py](grok-exec/server.py) | 已安装并登录的 Grok CLI |
| `antigravity` | [antigravity-exec/server.py](antigravity-exec/server.py) | 已安装并登录的 Antigravity CLI，以及 [专用 agent](antigravity-exec/aris-antigravity-review.md) |
| `codex` | [codex-exec/server.py](codex-exec/server.py) | 已安装并登录、支持 `exec resume` 的 Codex CLI |
| `claude-review` | [claude-review/server.py](claude-review/server.py) | 已配置 provider 的 Claude Code CLI |

四个服务和随附测试只使用 Python 标准库（Python 3.9+）；无需 `pip install`，没有隐式 SDK、上游仓库或后台下载依赖。CLI、账户、模型权限、联网及各 CLI 原生会话存储由使用者准备。Antigravity 的 `--sandbox` 是否还需要本机容器运行时，按所安装 CLI 的要求准备。

在仓库根目录执行全部离线测试：

```bash
python3 -m unittest discover -s mcp-servers/tests -p 'test_*.py' -v
```

这些测试启动真实桥接进程，注入临时 fake CLI，不访问模型、账户或网络。它们核验协议和故障语义；实际模型连通性与审阅内容质量由具体运行另记。
