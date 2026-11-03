`— composed: development/evolution/dd-v2-20261102/EVOLUTION.md`

### 1. 本轮定点复核的实际阅读范围

1. Base 阶段派发与消费修订段：
   - [base/skills/mathrsi-prepare/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prepare/SKILL.md)（50–80 行）
   - [base/skills/mathrsi-survey/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-survey/SKILL.md)（70–130 行）
   - [base/skills/mathrsi-route-loop/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md)（75–95 行）
   - [base/skills/mathrsi-prove/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md)（75–110 行）
   - [base/skills/mathrsi-verify/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md)（65–85 行）
   - [base/skills/mathrsi-research/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md)（160–178 行）
   - [docs/WORKFLOWS.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/WORKFLOWS.md)（35–50 行）、[docs/PLUGIN_CONTRACT.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md)（18–35 行）
2. DD 插件任务 `cwd` 调用与展开执行段：
   - [plugins/degree-diameter/README.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/README.md)（1–24 行）
   - [plugins/degree-diameter/references/programs-and-replay.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/references/programs-and-replay.md)（1–96 行）
   - [plugins/degree-diameter/skills/dd-construction/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/skills/dd-construction/SKILL.md)（1–103 行）
   - [plugins/degree-diameter/skills/dd-obstruction-certificate/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/skills/dd-obstruction-certificate/SKILL.md)（1–91 行）
   - [plugins/degree-diameter/examples/affine-common-coverage.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/examples/affine-common-coverage.md)（1–36 行）、[examples/frozen-clones-and-diagonal.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/examples/frozen-clones-and-diagonal.md)（1–38 行）、[examples/mizuno-exact-dual.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/examples/mizuno-exact-dual.md)（1–35 行）
   - [development/evolution/dd-v2-20261102/implement/TASK_CWD_REPLAY.json](file:///Users/rfy_naiveai/Desktop/MathRSI/development/evolution/dd-v2-20261102/implement/TASK_CWD_REPLAY.json)（1–29 行）

---

### 2. 逐项确认结果（原三项具体问题均已解决，无新增阻塞问题）

1. **五阶段 Base $\leftrightarrow$ DD 插件的派发与返回消费已完全打通（已解决）**：
   - [mathrsi-prepare/SKILL.md:59-68](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prepare/SKILL.md#L59-L68) 与 [mathrsi-survey/SKILL.md:95-115](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-survey/SKILL.md#L95-L115) 已增设 `### 已启用 DD 时，实际接入构造族与公开比较` 分支，将随仓 `archive/source/research-wiki/` 与 `public_baseline_audit/` 作为本地种子，共享唯一一次 `research-lit` 与 `LITERATURE.md` writer，并将“旧比较 $\to$ 新保证 $\to$ 受影响候选/可用新源 $\to$ 剩余条件”返回原 caller 调整队列。
   - [mathrsi-research/SKILL.md:167](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md#L167)、[mathrsi-route-loop/SKILL.md:82](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L82)、[mathrsi-prove/SKILL.md:84-96](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md#L84-L96)、[mathrsi-verify/SKILL.md:69](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md#L69)、[docs/WORKFLOWS.md:42](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/WORKFLOWS.md#L42) 及 [docs/PLUGIN_CONTRACT.md:26](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md#L26) 已全部对齐：明确了各阶段传给 DD 技能的实际图/参数/允许操作输入、返回原义务的消费动作，以及 `dd-obstruction-certificate` §4–5 同时承担正构造的字面属性、覆盖、证据继承与固定 Lean 导出核对。
2. **任务工作区 `cwd` 下的命令调用路径与写域隔离已统一（已解决）**：
   - [plugins/degree-diameter/README.md:15-21](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/README.md#L15-L21)、[programs-and-replay.md:3-68](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/references/programs-and-replay.md#L3-L68)、[dd-construction/SKILL.md:18, 64-72](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/skills/dd-construction/SKILL.md#L64-L72)、[dd-obstruction-certificate/SKILL.md:56-61](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/skills/dd-obstruction-certificate/SKILL.md#L56-L61) 和三个 `examples/` 均已统一为在当前任务工作区通过 `DD_PLUGIN="/path/to/MathRSI/plugins/degree-diameter"` 与 `TASK_DIR=$(pwd -P)` 调用，`--workspace`/`--output` 均落入 `$TASK_DIR` 下的新目录，保持 `archive/` 只读。
   - [TASK_CWD_REPLAY.json](file:///Users/rfy_naiveai/Desktop/MathRSI/development/evolution/dd-v2-20261102/implement/TASK_CWD_REPLAY.json) 已记录在独立临时任务 `cwd` 下实际调用 `replay_mizuno_dual.py` 返回 `exit 0`、`source_writes: 0` 的实测回执。
3. **具体展开执行段与文本清晰度（已解决）**：
   - `dd-construction/SKILL.md`（§展开执行A/B/C）与 `dd-obstruction-certificate/SKILL.md`（364列 exact dual 与删边后新根 PASS 消费例）补充了可直接照做的 caller 连接模板，此前的英文词粘连已清理完毕。

本轮设计的跨文件调用、工作目录约定与返回消费均已闭合，可直接收束并合入 `EVOLUTION.md`。

