# 安装和调用实际 reviewer MCP

MathRSI 将四个真实 Python MCP 服务打包在 [mcp-servers](../mcp-servers/README.md)。[reviewer_route.py](../base/tools/reviewer_route.py) 只解析选择，不启动服务、不加载宿主工具、不执行模型调用。执行者应先看当前工具目录，找到实际首轮和续接工具，再将路由选择转换成下面对应的参数。宿主常将 `grok-reply` 显示成 `mcp__grok__grok_reply`；实际名字以当前目录为准，不能仅凭生成的字符串断言可调用。

## 依赖与安装边界

Python 3.9+ 即可执行随附服务和离线测试，没有第三方 Python 包。每条路线只需对应的已安装 CLI 和现有登录／provider 配置。先在自己的正常终端检查 `python3 --version`、所用 CLI 的 `--version`，按该 CLI 官方方式完成安装和登录。仓库不带模型二进制、账户、配额、网络代理或认证材料，也不替使用者安装这些客户端。

Grok 需支持 headless `-p`、`--resume` 和原生会话摘要；上游历史版本为 1.0.46。Antigravity 需支持 NDJSON headless、`--conversation`、自定义 agent、`--sandbox` 和所需模型；上游历史版本为 1.2.17。Codex 需支持 `codex exec` 和 `codex exec resume`；上游历史核验为 0.153.4／0.154.0。Claude 需支持 JSON 输出、`--resume`、`--strict-mcp-config` 和 plan 权限模式。这些是被桥接使用的实际接口，不是对当前发布版本的声明。新版本先运行本仓离线测试；真实 CLI 接口变化仍需要实际检查。

以下示例在 MathRSI 根目录运行。`MATHRSI_ROOT` 只影响当前 shell，不修改系统默认值；注册项要保存绝对路径，因此注册后移动仓库需更新相应路径。配置一次使用哪条服务就注册哪条，不要求全开。

```bash
export MATHRSI_ROOT="$(pwd -P)"
mkdir -p "$HOME/.gemini/config/agents"
cp "$MATHRSI_ROOT/mcp-servers/antigravity-exec/aris-antigravity-review.md" \
  "$HOME/.gemini/config/agents/aris-antigravity-review.md"
```

复制 agent 是 Antigravity 路线的一次安装操作。它选择文件读取／搜索工具并关闭命令执行；若本机已有同名定制 agent，先比较文件并保留需要的定制。CLI 原生权限和 sandbox 继续生效；工具声明不等于已经证明所有平台上的操作系统级写入隔离。需要容器运行时与否由所安装 CLI 的 sandbox 实现决定。

## Codex 宿主

用下列命令注册需要的服务。`command -v` 得到实际 CLI 路径；若客户端不在当前 PATH，直接填自己的绝对路径。已有同名服务时先检查原注册项，按需要更新对应项，避免覆盖无关设置。

```bash
codex mcp add grok \
  --env GROK_BIN="$(command -v grok)" \
  --env GROK_EXEC_MODEL=grok-4.7 --env GROK_EXEC_EFFORT=xhigh \
  -- python3 "$MATHRSI_ROOT/mcp-servers/grok-exec/server.py"

codex mcp add antigravity \
  --env AGY_BIN="$(command -v agy)" \
  --env AGY_EXEC_MODEL=gemini-4-argon-high --env AGY_EXEC_EFFORT=high \
  -- python3 "$MATHRSI_ROOT/mcp-servers/antigravity-exec/server.py"

codex mcp add claude-review \
  --env CLAUDE_BIN="$(command -v claude)" \
  -- python3 "$MATHRSI_ROOT/mcp-servers/claude-review/server.py"
```

在 `~/.codex/config.toml` 对相应服务的现有表加长调用超时。完整示例中的 `command`、路径须替换为本机值；`env` 中的模型选择与上述注册命令一致，勿重复建立同名表：

```toml
[mcp_servers.grok]
command = "python3"
args = ["/absolute/path/to/MathRSI/mcp-servers/grok-exec/server.py"]
tool_timeout_sec = 3660

[mcp_servers.grok.env]
GROK_BIN = "/absolute/path/to/grok"
GROK_EXEC_MODEL = "grok-4.7"
GROK_EXEC_EFFORT = "xhigh"

[mcp_servers.antigravity]
command = "python3"
args = ["/absolute/path/to/MathRSI/mcp-servers/antigravity-exec/server.py"]
tool_timeout_sec = 3660

[mcp_servers.antigravity.env]
AGY_BIN = "/absolute/path/to/agy"
AGY_EXEC_MODEL = "gemini-4-argon-high"
AGY_EXEC_EFFORT = "high"
```

Grok／Antigravity 桥接自身默认 3600 秒，宿主留 3660 秒容纳终止清理；进度通知不会延长宿主硬期限。Claude 默认 600 秒，长审阅优先使用后台工具。Codex 宿主的 Codex reviewer 使用 native agent 时不需要注册 `codex` MCP；native 工具及可选型号仍以宿主实际能力为准。

## Claude Code 宿主

使用同一份本仓 Python 服务。下面 `-s user` 是用户级配置；需要项目级时按照所安装 Claude Code 的注册选项选择范围，不把作者绝对路径提交给合作者。

```bash
claude mcp add grok -s user \
  -e GROK_BIN="$(command -v grok)" \
  -e GROK_EXEC_MODEL=grok-4.7 -e GROK_EXEC_EFFORT=xhigh \
  -- python3 "$MATHRSI_ROOT/mcp-servers/grok-exec/server.py"

claude mcp add antigravity -s user \
  -e AGY_BIN="$(command -v agy)" \
  -e AGY_EXEC_MODEL=gemini-4-argon-high -e AGY_EXEC_EFFORT=high \
  -- python3 "$MATHRSI_ROOT/mcp-servers/antigravity-exec/server.py"

claude mcp add codex -s user -e CODEX_BIN="$(command -v codex)" \
  -- python3 "$MATHRSI_ROOT/mcp-servers/codex-exec/server.py"
```

显式选择 `claude-code` reviewer 且宿主还没有对应服务时，也可以同样注册：

```bash
claude mcp add claude-review -s user -e CLAUDE_BIN="$(command -v claude)" \
  -- python3 "$MATHRSI_ROOT/mcp-servers/claude-review/server.py"
```

如宿主版本支持 `MCP_TOOL_TIMEOUT`，在启动 Claude Code 的终端用 `MCP_TOOL_TIMEOUT=3660000 claude` 给长同步工具调用足够时间（单位毫秒）。同时检查该版本实际生效的宿主期限；若返回超时，不能把桥接的心跳当作免超时保证。Claude reviewer 的长任务有后台 job 协议，可以避免长期占住同步调用。

完成注册后重启对应宿主会话或按宿主方式重新连接服务，再检查工具目录。已有交互式 Grok／Antigravity／Claude 窗口不必关闭，桥接续接只使用明确返回的会话 ID。GUI 启动的 MCP 常不继承登录 shell 环境；需要代理时只在相应服务的 `env` 中填自己真实可达的代理，重启服务后生效，不复制作者机器代理或凭据。

## 首轮与续接：将路由转换成真实参数

本项目用户当前指定的跨家族配置为 Gemini 4 Argon／high 和 Grok 4.7／xhigh，以下给出其调用示例；其它任务仍按用户指示、项目配置和宿主默认解析，不强制这两个服务。打包源码保持上游不变，Antigravity 源码 fallback 仍是 Gemini 3.8 Flash；上面的服务环境覆盖和下面的首轮显式参数才落实当前选择。`model` 与 `effort` 应按本次路由传入，不依赖历史工具描述。

Grok 首轮调用 `grok`：

```json
{"prompt":"读取 proof.md，核查指定引理与实际调用的连接。","cwd":"/absolute/path/to/task","model":"grok-4.7","effort":"xhigh","sandbox":"read-only","tools":"read_file,grep,list_dir","max_turns":50}
```

Antigravity 首轮调用 `antigravity`：

```json
{"prompt":"读取 proof.md，核查指定引理与实际调用的连接。","cwd":"/absolute/path/to/task","model":"gemini-4-argon-high","effort":"high"}
```

两者各自续接工具为 `grok-reply`、`antigravity-reply`，参数相同：

```json
{"threadId":"该服务首轮返回的 UUID","prompt":"已修订 proof.md 的引理2，请只核查此修订及其影响。"}
```

这两条续接只接受 `threadId` 与 `prompt`，保持首轮模型、effort、cwd 和对应权限／agent 设置。桥接的持久状态和 CLI 原生会话都需保留；仅复制一个 UUID 到另一台没有会话记录的机器不够。更换模型或目录应开新首轮，用已有产物和准确范围作为新输入。文件应放在首轮 cwd 内；遇到目录外访问授权时，不通过关闭权限检查来解决。

Grok和Antigravity这两份桥接没有`status`或`jobId`轮询工具。同步调用仍在途时，用宿主保留的该次调用句柄等待返回；宿主已失联且无法取回终态时，保留“结果未知”与原请求/会话，查可用的本地原生记录，继续独立工作。不能编造`grok_status`，也不能把`reply`当只读查询来试探——它会真正发起下一次模型请求。Claude下文的后台job轮询契约不能套给这两个服务。

Claude Code 宿主调用 Codex reviewer 时，首轮工具为 `codex`。路由中的 `effort` 要变成 `config.model_reasoning_effort`，不能把 `effort` 当作顶层字段直接传：

```json
{"prompt":"读取 proof.md，核查指定数学义务。","cwd":"/absolute/path/to/task","model":"gpt-6-astra","config":{"model_reasoning_effort":"ultra"},"sandbox":"read-only"}
```

常规档按路由使用 `xhigh`；用户显式选 `max` 时保留真实请求并检查 CLI 是否接受，不静默换档。`codex-reply` 只传 `threadId` 与 `prompt`，桥接从保存文件重新施加原 model/config/sandbox/cwd。native Codex agent 的参数与 MCP 不同，应使用当前 native schema；同为 Codex reviewer 时记录 same-family，不写跨家族审阅。

显式 Claude reviewer 首轮调用 `review`：

```json
{"prompt":"读取 proof.md，核查指定数学义务。","cwd":"/absolute/path/to/task","tools":"Read,Grep,Glob"}
```

`model` 可按本次路由补入；省略时沿用底层 CLI provider 配置。`review_reply` 需重复 `cwd`、`tools`、所选 `model` 和必要的 `system`，并传 `threadId` 与新 `prompt`。它与前面两个服务不同，不持久冻结这些设置。Claude bridge 没有可强制的 effort 参数；不能据型号推定 effort。省略 `tools` 默认无工具，只有提示正文可见，因此“给文件路径审阅”必须显式加 `Read,Grep,Glob`，且路径在 cwd 的可读范围内。

长 Claude 审阅改用 `review_start`，参数与 `review` 相同，立即保存其 `jobId`。用 `review_status` 的 `{"jobId":"返回值","waitSeconds":20}` 轮询，直到 `done=true`；续接用 `review_reply_start`，参数与 `review_reply` 相同。`completed` 还要检查 `error`、终态和正文；jobId 是后台工作 ID，threadId 才是原生模型会话 ID。服务重启后仍可查同一状态目录中的后台 job。该桥接同步 reader 会阻塞，取消不保证回收整个进程树；不要把 Grok／Antigravity 的清理保证移用给它。

## 返回证据和失败处置

Grok／Antigravity 把正文与 threadId 放在 `structuredContent`，并保留 `requestedModel`／`requestedEffort`。Grok 的 `model` 来自 CLI 输出，`effort` 来自原生 session summary；摘要缺失就为 null。Antigravity 的 `model` 来自 init，`selectedModelLabel` 来自 CLI 解析日志，`effortSource=cli_selected_model_variant`；缺失不拿请求值补齐。这些是 CLI 报告，不是独立服务端身份鉴定。

Codex bridge 保留 `{threadId, content}` 与终态错误，没有提供同等的独立实际 model／effort 字段，不能拿首轮请求冒填实际值。Claude bridge 的 MCP `content[0].text` 是 JSON 字符串，先解析其中的 `threadId`／`response`／`model`／`modelSource`／`reportedModels`；请求值另列 `requestedModel`，没有明确实际值时记 null。Claude Code CLI 可连接非 Anthropic provider，reviewer family 必须据真实配置和报告判断。

保存实际参数、原始响应、会话 ID、读取文件范围、是否执行程序以及对实质意见的处置。有效模型回复也不等于定理证明通过；失败、ERROR／WAITING、空正文、截断、退出非零、取消或缺终态不能写成成功审阅。Grok／Antigravity 不自动重试付费请求，模型或网络故障保留原记录再决定；底层 CLI 可能自行网络重连，连通性诊断可临时设 `GROK_EXEC_TIMEOUT_SEC=75`、`AGY_EXEC_TIMEOUT_SEC=90`。改这些变量后须重启相应服务，且不影响已保留的旧失败记录。

Grok／Antigravity／Codex 默认持久设置目录分别为 `~/.codex/state/grok-exec`、`antigravity-exec`、`codex-exec`；可由对应 `*_EXEC_STATE_DIR` 覆盖。Claude 的 `CLAUDE_REVIEW_STATE_DIR` 默认 `~/.codex/state/claude-review`。这些路径也会被 Claude 宿主使用，因为它们是上游桥接默认值。Claude debug 默认会记录请求和响应到 `/tmp/claude-review-mcp-debug.log`（Windows 为 TEMP）；如需保存证据，设置 `CLAUDE_REVIEW_DEBUG_LOG` 为自己管理的本地路径，并按敏感研究材料处理。Grok／Antigravity 的可选 debug 不记录提示正文，但 CLI 原生会话仍由各 CLI 落盘。

## 本仓验证与可用性

在 MathRSI 根执行：

```bash
python3 -m unittest discover -s mcp-servers/tests -p 'test_*.py' -v
```

测试启动打包的真实桥接，以临时 fake CLI 验证工具 schema、参数传递、长提示、首轮、重启续接、失败终态、元数据缺失、取消／超时／断开以及 Claude 后台状态恢复。它不会发付费请求或修改全局 MCP 配置。准确计数和实际输出见 [MCP_BUNDLE_REPORT](../development/review-loop-integration/MCP_BUNDLE_REPORT.md)。

本轮工具目录可见 Grok、Antigravity 和 Claude-review 工具；这只表明当前宿主载入了已有服务，不能证明它们指向本仓副本。当前目录中未发现 `mcp__codex__codex`，Codex native agent 也不是这个 MCP。打包服务可启动、宿主已加载、真实模型连通、特定数学义务获审阅分别记录；本包的离线测试建立协议证据。随后已另行启动仓内Python服务做真实调用：Antigravity跨进程续接Gemini成功，Grok首轮在600秒后超时、无有效终稿，未自动重试。完整记录见[实际桥接执行](../development/review-loop-integration/LIVE_MCP_EXECUTION.md)。这两次调用均未改变全局注册；没有在新机器验证CLI安装、登录或全部四条模型路由。
