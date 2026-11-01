# Archon-Horizon 对本项目的价值

这是一份历史阶段记录。2026-10-07 已补读具体 Lean 技能、实际搜索及构建/审计实现，详见 [Horizon 深读](HORIZON_DEEP_DIVE_20261007.md)和[两项目综合说明](MATH_AGENT_HARNESS_SYNTHESIS.md)。

2026-10-06。只读评估，未安装、初始化或运行 Horizon，未修改 Lean 源码或项目配置。
核查的是 GitHub API 当时返回的 `main` 实际提交
`0df5571f81aae29130c8ec621c9fe7419ca28d6a`；下列链接固定该提交。

**判断：审阅方法有用；立即引入整个运行平台的收益有限。**
本项目已经有并行任务、Lean 编译、公理检查、跨模型核对、显式依赖义务与实际日志。
Horizon 的主要增量是把这些协作长期保存在统一运行平台；它不会直接提供本题缺少的
超图、条件排列计数或结构选点证明。

## 立即采用的一项方法

对重要接口做一次**盲回译，再独立对照**：让 Grok 只读冻结的完整 Lean 声明及其
定义依赖，写出其实际数学含义，不提供预期定理或先前审阅结论；随后让 Gemini
将回译与 `FORMAL_SPEC.md`、P1及相应计数论证对照，定位多余假设、量词次序、
空条件或遗漏的对象转换。相同声明和定义不变时复用该记录，不为每次证明代码微调
重做一轮。

这直接来自当前
[statement-alignment/SKILL.md](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/statement-alignment/SKILL.md#L17-L38)。
可先用于 `Greedy.failure_event_cover`、`propertyB_of_successful_permutation`
以及 Counting 的条件计数接口。这样补充的是语义独立性，不将 reviewer 赞同变成证明前提。

## 核查到的真实审阅资产

| 资产 | 实际要求及与本项目的关系 |
|---|---|
| [statement-alignment](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/statement-alignment/SKILL.md) | 读完整展开类型、隐式参数和定义，而不是凭定理名称判断；与纸面比较对象、量词和结论。盲回译是本次建议的增量。 |
| [semantic-probes.md](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/statement-alignment/references/semantic-probes.md#L14-L47) | `(h:P):P` 或含 `conclusion:P` 的 certificate 只是接口，须有从原假设构造的 producer 及到目标的 consumer；空结构不自动有错，要指出实际缺失内容。还检查自然数减法、零分母等约定。与我们明确区分通用P6/P7接口、实际P1、尚未实例化义务一致。 |
| [proof-review](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/proof-review/SKILL.md) 及 [trust-and-closure.md](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/proof-review/references/trust-and-closure.md) | 顺着真实输入到最终消费者追踪证明贡献；区分本地编译范围、公理依赖、传递性缺口及目标闭合。标准公理报告不能排除“证明了错误或过弱命题”。这些检查我们已经执行，仍需在最终T的依赖闭合时汇总。 |
| [mathematical-fidelity reviewer](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/subagents/reviewers/mathematical-fidelity.md) | 从公共定理回看定义、构造输入和实际消费者，拒绝以局部helper的通过冒充整个结果。属于模型审阅指导，不是自动数学保证。 |

当前完整仓库树共520项，API返回 `truncated=false`，未包含任何 `.lean` 文件。
这不是可直接导入的超图或排列计数数学库；数学复用仍来自固定版本 Mathlib 及本项目证明。
[reviewer_guidance.py](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/reviewer_guidance.py)
的实际功能是读取这些 Markdown 描述并与审阅合同合成指令。
当前架构文档也明确：运行时测试不建立数学判断力或完成时间保证。
[architecture.md](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/docs/architecture.md#tradeoffs-and-validation)

## 网页缓存与当前版本的差异

本轮 `web` 打开的 GitHub 仓库主页返回旧介绍（“first public release”“stable”、
workspace/config.yaml、Horizon Agent/Ground helper及 `horizon run my_task`）。
直接读取固定提交的原始文件，实际是 **0.2.0 alpha**：

- [当前 README](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/README.md)
  声明0.2.0发生重大架构变更：PostgreSQL控制平面、`/api/v3`、`/pipeline`，旧SQLite与`/api/v2`退役；
  从0.1.x的迁移不是自动完成。
- [当前 architecture](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/docs/architecture.md#work-and-maintenance)
  的默认是一个 root maintainer 选择工作、委派 workers、审阅并关闭阶段；
  原 `orchestrated: true` 路径保留兼容，不是新run推荐默认。
- 当前技能目录是 `src/archon_horizon/pipeline/skills/`；审阅技能位于其 `review/`，
  reviewer描述位于 `pipeline/subagents/reviewers/`。
  不应把旧版 `formalization-review` 路径或旧配置示例直接当成当前安装说明。
- [当前 reviewer workflow](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/docs/pipeline-reviewers.md)
  的新项目preset默认使用持久 reviewer assignment；短任务仍可显式选 native subrequest。

这些差异不削弱上述审阅方法的价值，但意味着不能基于缓存旧文档承诺低成本直接接管本项目。

## 模型继承：概念仍在，配置接口已变

实际代码
[reviewer_invocations.py:302–342](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/reviewer_invocations.py#L302-L342)
给出明确规则：

- reviewer与父执行使用同一harness时，以父thread已经生效的 `applied_model_options` 为基础，
  再以该reviewer descriptor的 `model_options` 覆盖。
- 使用不同harness时，以该harness的 `model_options` 为基础，再覆盖descriptor选项。
- native subrequest要求使用兼容的父harness；不同harness的reviewer须走独立assignment。

[ModelOptions](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/models.py#L263-L276)
包含 `model` 与 `reasoning_effort`；想继承就省略字段，显式 `null` 会被拒绝。
因此“未覆盖时继承”仍成立，但不能泛化成“每个reviewer自动使用不同模型”。
换persona或新上下文不自动提供跨模型家族独立性；我们现有Grok/Gemini桥接仍需
保留实际模型与effort记录。未检验Horizon与这两个本地桥接的直接集成。
