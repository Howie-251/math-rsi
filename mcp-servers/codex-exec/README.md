> ARIS 原版使用说明，源码版本固定于 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`。MathRSI 的当前默认模型、仓库内路径和双宿主安装入口见 [REVIEWER_MCP](../../docs/REVIEWER_MCP.md)。此处历史实测不代表当前机器已经连通。

# codex-exec — the `codex` MCP server, over `codex exec`

codex-cli 0.154.0 removed the `codex mcp-server` entry point that ARIS
registered as the `codex` MCP server. This bridge speaks the same contract —
tools `codex` and `codex-reply`, results `{threadId, content}` — and runs each
call as a `codex exec` subprocess. Nothing in the skills changes.

## Register

MathRSI ships this file locally; no upstream clone or pull is needed. See the
[dual-host installation guide](../../docs/REVIEWER_MCP.md) for registration.
Requires Python 3.9+, a logged-in `codex` executable with `codex exec resume`,
and no third-party Python packages. Original ARIS validation used CLI 0.153.4
and 0.154.0; verify your installed version rather than assuming those snapshots
represent today's CLI.

## What a call becomes

| MCP argument | `codex exec` |
|---|---|
| `prompt` | stdin (no argv limit) |
| `model` | `-m MODEL` |
| `config` `{"model_reasoning_effort": "ultra"}` | `-c model_reasoning_effort="ultra"` (nested objects become dotted keys) |
| `sandbox` | `--sandbox MODE` |
| `cwd` | `--cd DIR` |
| `codex-reply` `threadId` | `codex exec resume THREAD` **plus the model, config, sandbox and cwd the thread was created with** — `resume` alone would fall back to `config.toml` defaults, and ARIS's routing contract relies on a continued thread keeping its reviewer model and effort |

Per-thread settings live in `~/.codex/state/codex-exec/threads/<threadId>.json`, one file each.

A failed turn (unknown model, auth, API error) comes back as `isError: true`
with codex's own error text, so the capability fallback in
`skills/shared-references/reviewer-routing.md` keys on the same wording as before.

While a review runs the bridge streams `codex/event` notifications and, when the
host passes a `progressToken`, a `notifications/progress` heartbeat every 15 s
(`CODEX_EXEC_PROGRESS_INTERVAL_SEC`), answers `ping`, and honours
`notifications/cancelled`. Notifications cannot override a host's hard tool
timeout — deep-audit reviews at `ultra` can run 30+ minutes.

Not offered, because `codex exec` cannot honour them: `approval-policy`,
`base-instructions`, `developer-instructions`, `compact-prompt`. No ARIS skill
passed them.

Debugging: `CODEX_EXEC_DEBUG_LOG=/path/to/log` records every request and the
exact `codex exec` command line; `CODEX_BIN` points at a specific codex binary.
