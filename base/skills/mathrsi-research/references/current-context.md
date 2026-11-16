# 从收件到下一次任务与审阅输入（可选 `current_context` 契约）

本参考由 [mathrsi-research](../SKILL.md) 与 [mathrsi-route-loop](../../mathrsi-route-loop/SKILL.md) 的唯一父调度者按需使用。它不建立第二套全局状态库，不充当后台调度器或数学验证器，也不要求没有 JSON 状态的项目迁移格式。

## 何时启用与谁负责写

- **适用场景**：多批次、多代理或含跨模型审阅的持续研究任务，且工作区已有结构化 `STATE.json`（顶层含宿主状态 `status`）。若项目已有等效的短恢复视图，直接沿用原文件。
- **单写者原则**：子 worker 与审阅代理只返回计算产物、证明与原始回执，**绝不直接改写共享 `STATE.json`**。仅父调度者在读取作者产物与所需核验原件、作出接受或留待核验的明确判断后，调用 [current_context.py](../../../tools/current_context.py) 的 `write_current(state_path, current)` 更新 `STATE["current_context"]`。
- **历史与当前分离**：`write_current` 通过同目录临时文件原子替换 `STATE.json` 的 `current_context` 与 `current_context_updated_at`，保留顶层 `status`（如 `ACTIVE` / `PAUSED`）和一切既有历史字段。暂停状态下允许整理已返回事实，但整理动作本身绝不恢复数学运行。

## 短视图写什么、不写什么

`current_context` 只保存直接决定**下一拍派工与审阅判断**的当前事实：

1. **最新已接受成果与有效基线**：按任务自身结构记录已过独立核验的结果及证据路径（领域专有派生计数由领域插件写入，Base helper 不假定任何特定领域字段）。
2. **当前问题、下一动作与真实在途**：`current_question`、`next_action` 与 `current_work.in_flight` 必须表达同一个当前决定，及时清掉已结束任务的过期 `READY / RUNNING` 标签。
3. **相关已停路线与重开条件（`route_stops`）**：记录本任务已排除或撤下的具体范围、原因与原件路径。下游任务和审阅默认携带这些记录，防止外部模型或新代理反复建议重开已退队路线；存在真正改变原障碍的新条件时仍允许凭据重开。
4. **共享认证与审阅未闭缺口**：明确区分“数学/计算核验已通过”与“具体源 Lean / 最终审阅仍开放”。

**防止短状态回膨胀**：收件时用几行终态结论与原件路径替换该任务的准备/运行摘要；不要把完整 `RESULT.json`、编译重试日志或历轮审阅全文逐份塞进 `current_context`（细节留在任务子目录或 `STATE` 历史区）。若 `STATE.json` 顶层配置了可选的 `current_context_view`（相对 `STATE.json` 所在目录或绝对路径），每次 `write_current` 会自动重新渲染该只读文本视图；视图写入若异常，直接从已提交的 `STATE.json` 重跑渲染即可，无需重放数学验收。

## 标准收件 → 派发顺序与未消费终态拦截

父调度者在两轮之间固定执行以下四步，**不能先派下一批、事后才补写当前状态**：

1. **登记终态输出路径（派工前）**：若待派或已就绪任务会在结束时写出唯一的最终 JSON（而非运行中反复刷新的进度文件），在 `current_work.in_flight.<任务名>.terminal_result` 登记该路径（绝对路径，或相对于 `STATE.json` 所在目录的相对路径）。
2. **拦截漏收（生成新输入前）**：调用 `request_text` 生成下一份任务或审阅输入时，`require_consumed_results` 会检查所有已登记的 `terminal_result`。一旦发现某个终态文件已落盘却仍挂在 `in_flight` 中，立即报错阻断新输入生成，防止把已结束的 `UNKNOWN` 或失败批次继续当作“待运行”重派。只读渲染 `render` 不受此限制。
3. **收件更新（区分返回与接受）**：文件存在不等于数学成立。若作者已出候选而独立核验未跑，父调度可将状态更新为“作者已返回、独验待执行”，将该项移出旧 `in_flight` 后专门派发独立核验，无需等最终验收全部结束才同步事实。
4. **从更新后的同一快照导出下游输入**：使用同一份刷新后的 `STATE.json` 生成 worker 任务单或 Phase A / Phase D 审阅输入。

### 真实故障对照例

在 DD `(12,5)` 与 `(14,5)` 连续研究中曾出现两类典型漂移：
- `42,403..42,411` 九张新图已通过独验，但 `ROUTE_REPORT.md` 仍停留在早期拆分实验，同线程后续审阅甚至建议重开数小时前已因 `298s UNKNOWN` 及微增不足而撤下的 `88,452` 克隆线；
- `(15,5)` 第二批搜索已落盘 `UNKNOWN` 终态文件，状态表却仍标 `READY`。
接入上述收件链后：`write_current` 立即同步最新合法图与 `88,452` 退队记录，首次 Phase A 与后续 Phase D 均带上该 `route_stops`；未消费的 `RESULT.json` 在生成下一请求前即被 `terminal_result` 守卫拦停。

## 审阅粒度：`task`、`reuse`、`delta` 与 `new`

调用者比较数学范围后在请求 JSON 中显式指定 `review_mode`；helper 校验声明字段完备性，不代替调用者判断数学等价，也不自动发起模型调用：

| `review_mode` | 何时使用 | 调用者填写的字段 | 下游效果 |
|---|---|---|---|
| `task` | 向研究或核验 worker 派发授权范围内的具体任务 | `question`；可选 `routes`（精确键名列表，拼写错误直接报错以免漏传负历史；省略或空列表则带入全部 `route_stops`） | 输出当前事实快照 + 本次任务边界 |
| `reuse` | 源进口、覆盖引理与生成机制**完全未变**的后继有界批次 | 非空 `prior_reviews`（含 `path` 与 `scope`）、非空 `reuse_scope`，且 `changes` 必须为空 | 引用原审阅收据处理原理层，**不就同一未变原理重复发起模型往返**；每步实例度数/覆盖独验照常执行 |
| `delta` | 在已有路线基础上改变了某项假设、候选域、方向或连接规则 | 非空 `changes`（逐条写明改动的假设/域/代码/主张）；有可继承旧审阅时附 `prior_reviews`，无则不声称复用 | 只围绕变动部分及其下游后果请求增量审阅，未变前置证据直接沿用 |
| `new` | 新路线、新承重命题或需独立新鲜视角攻击 | `question` | 发起完整初审，不预设任何历史认可 |

**路径基准约定**：CLI 与 Python 调用统一以 `STATE.json` 所在目录（`state_dir`）解析相对的 `terminal_result` 和 `prior_reviews[].path`，无论当前 shell 工作目录在何处均可稳定复现；绝对路径原样支持。任何可复用的路线审阅均不免除逐实例验证，也不替代任务合同要求的最终独立终审。

生成输入明确标出该目录，供工作目录不同的下游读取。Python 调用者使用相对路径时也应传入 `state_dir`；直接绕过 helper 的派工仍由原父调度负责收件，脚本不是全局拦截器。

## 最小调用示例

```bash
# 1. 仅从 STATE.json 渲染当前只读事实视图
python3 /path/to/MathRSI/base/tools/current_context.py \
  --state /task/STATE.json --output /task/CURRENT_CONTEXT.txt

# 2. 校验无漏收终态，并生成增量审阅（delta）或后继任务输入
python3 /path/to/MathRSI/base/tools/current_context.py \
  --state /task/STATE.json --request /task/next-request.json --output /task/next-input.txt
```

`next-request.json`（增量审阅 `delta` 示例，相对路径相对于 `/task/STATE.json` 所在目录）：

```json
{
  "review_mode": "delta",
  "question": "固定 4074 split fibers 改为对 4060 连通分量整体补色后，核对度数不变性与 161 外围根覆盖边界。",
  "changes": [
    "核心边相对 37631 源删 186 条、增 212 条，不再使用旧边全部保留的距离继承",
    "改用真实 H9/sigma/pi 核心全称定理配齐全部 160 旧外围根 + 新根 BFS"
  ],
  "prior_reviews": [
    {
      "path": "reviews/h9_core_certificate_review.txt",
      "scope": "任意点线双射 sigma 下平面 91 线命中给出核心四步覆盖，奇路径转换给出核心直径至多 5"
    }
  ],
  "routes": ["d11_fixed_color_1120planes", "d11_canonical_one_anchor"]
}
```
