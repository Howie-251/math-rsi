# 从收件到下一次任务与审阅输入（可选 `current_context` 契约）

本参考供 [mathrsi-research](../SKILL.md) 与 [mathrsi-route-loop](../../mathrsi-route-loop/SKILL.md) 的唯一父调度者按需启用。它复用项目既有的 `STATE.json`（含顶层宿主状态 `status`），不新建全局状态库或后台调度器，也不要求无 JSON 状态的项目迁移格式；已有等效恢复视图时直接沿用。

## 单写者与短视图内容

子 worker 与审阅者只交原件和回执，不写 `STATE.json`。父调度在核读作者与核验原件后，调用 [current_context.py](../../../tools/current_context.py) 的 `write_current(state_path, current)` 原子替换 `STATE["current_context"]` 并保留顶层 `status` 及历史区；暂停时允许整理已到事实，不恢复数学运行。若顶层配置可选 `current_context_view`（相对 `STATE.json` 目录或绝对路径），写回时自动刷新该只读视图；若视图写入异常，直接从已提交的 `STATE.json` 重渲染即可。

`current_context` 仅保留决定下一动作的短事实，不把完整 `RESULT.json`、编译重试或历轮审阅全文塞回短区：
- **已验证成果与基线**：按任务结构记录已通过独验的对象及证据路径（领域专有计数由领域插件维护，Base 不预设特定字段）。
- **当前焦点与真实在途**：`current_question`、`next_action` 与 `current_work.in_flight` 表达同一决定，清除过期 `READY / RUNNING`。
- **已停路线（`route_stops`）与未闭缺口**：记录撤下范围、原因及重开条件，并把数学核验通过与具体源 Lean / 最终外审未闭合分开记账。

## 收件 → 派发守卫（拦截漏收与过期状态）

1. **派前登记终态文件**：若任务只在结束时写出唯一最终 JSON（非进度文件），在 `current_work.in_flight.<name>.terminal_result` 登记路径（绝对路径，或相对 `STATE.json` 所在目录）。
2. **生成前阻断漏收**：调用 `request_text` 生成任务或审阅输入时，`require_consumed_results` 若发现已登记的 `terminal_result` 已落盘，立即报错要求父调度先收件写回，防止把已返回的 `UNKNOWN` 继续当作待跑任务重派。只读 `render` 不受阻。
3. **区分返回与数学接受**：作者文件落盘不等于验收通过；父调度可先写回“作者已返回、独验待执行”，移出旧在途后再派独验。
4. **真实故障对照**：DD 研究中曾出现 `42403..42411` 已独验而 `ROUTE_REPORT` 仍停在旧实验、后续审阅重提已撤下的 `88,452` 路线，以及已落盘 `UNKNOWN` 仍挂 `READY`。每次收件写回 `current_context` 并由同源生成首次 Phase A 与后续 Phase D 输入即可消除此类漂移。

## 审阅与派工模式（`review_mode`）

调用者比较数学范围后指定模式；helper 只核声明完备性，不判数学等价，也不免除逐实例核验与最终终审。相对路径（`terminal_result`、`prior_reviews[].path`）统一按 `STATE.json` 所在目录解析：

| 模式 | 何时使用 | 字段要求 | 行为 |
|---|---|---|---|
| `task` | 派发具体研究或核验任务 | `question`；可选 `routes`（精确键名，拼错即报错；省略或空列表带入全部 `route_stops`） | 输出当前快照 + 任务边界 |
| `reuse` | 源进口、覆盖引理与机制未变的后继批次 | 非空 `prior_reviews`（`path`+`scope`）、非空 `reuse_scope`，且 `changes` 为空 | 引用旧审阅收据，**不重发模型调用**；实例独验照常 |
| `delta` | 改变了特定假设、生成域、方向或连接 | 非空 `changes`；有可继承旧审阅时附 `prior_reviews`，无则不声称复用 | 仅审变动点及后果，沿用未变前置证据 |
| `new` | 新路线、新承重命题或需独立新鲜攻击 | `question` | 发起完整初审，不预设历史认可 |

## 最小调用示例

```bash
python3 /path/to/MathRSI/base/tools/current_context.py \
  --state /task/STATE.json --output /task/CURRENT_CONTEXT.txt
python3 /path/to/MathRSI/base/tools/current_context.py \
  --state /task/STATE.json --request /task/next-request.json --output /task/next-input.txt
```

```json
{
  "review_mode": "delta",
  "question": "对 4060 连通分量整体补色换向后，核对度数不变性与 161 非核心根覆盖边界。",
  "changes": [
    "核心相对 37631 源删 186 边、增 212 边，改用 H9/sigma/pi 核心全称定理 + 161 根完整 BFS"
  ],
  "prior_reviews": [
    {"path": "reviews/h9_core_certificate_review.txt", "scope": "任意双射 sigma 下 91 线命中给核心四步覆盖"}
  ],
  "routes": ["d11_fixed_color_1120planes", "d11_canonical_one_anchor"]
}
```
