# mathrsi-base／PropertyB：证据札记

2026-11-01。仅设计讨论；以下为项目案例支持的设计建议，不是通用效率提升的实验结论。

## 1. 边界

**base**负责固定原命题与授权、记录义务依赖和证据范围、区分数学／表示／工具失败、安排独占写域与实测资源、核对原输入到结论的完整连接、维护失败与重试条件。Lean为可选验证器；导出类型、传递公理与实际调用的验收规则属于该验证器适配，不强迫所有数学任务用Lean。[A §“最值得固化的经验”；B:118–140]

**PropertyB插件**拥有最小反例约化、点对覆盖、整数度数／共度预算、选锁与迹恢复、排列概率的逐位置最小项、真实坏对配额、局部分类及其实际超图调用。组件配额可跨k复用，仍属领域数学；“禁止整图枚举”、特定Grok＋Gemini要求也是项目政策，不能升成base的普遍限制。[B:23–31；C:58–62；D:26–33]

插件提交领域事实、动作建议与证据；base掌握通用完成判定。插件不能直接修改base，只能提出独立的改进候选。

## 2. 三个低效原因及改法

1. **同一搜索域已无新增信息。** T33两类双锁已完整扫462／506位置；相同profile与界下换随机种子没有数学增量。保存固定条件、已扫域、余域及重试条件；只有新结构、配额或未扫位置才重启。[E:31–39]
2. **优化未作用于总界瓶颈。** 20点(7,9)位置12虽扣10/221，C项仍高于端点界，总界下降为零。插件输出逐位置活跃项及slack；base要求下一动作说明将改变哪个未闭义务，不能把名义扣除当进展。[E:53–67]
3. **局部松弛遗失共同结构，扩表只细分失败。** 六元35点四锁q2/q3扩展未解整支；改用全图预算、低共度伙伴及共同中心，最后仅需(12,10,10)与两次51>46矛盾。八／九元也只扩72／73个失败父型，严格父型立即停止。先尝试共同预算、实际选点或整数刚性，再扩大局部域。[D:31–39；F:50–70]

## 3. 最小接口

沿用现有文档即可：①原目标、允许信任与授权范围；②当前未闭义务及真实下游调用；③候选动作的输入域、固定条件、预期新增事实和停止／重试条件；④结果的精确覆盖、失败见证、证据路径及实际成本；⑤插件给出的原对象→局部数据→原结论桥接。base不解释锁点字段，只检查桥接是否齐全及证据状态；先不用数据库、通用事件总线或另一套知识库。[B:118–130、150–170；C:64–70]

## 4. RSI的两类改进

新选锁引理、共同容量和概率分流属于**解题改进**，由插件保留参数与调用条件；例如八／九元嵌套最低度池公式，不能拿任意单位伙伴代入。[F:24–50]

失败归因、活跃项诊断的通用契约、资源调度或验收缺口修补才是**base改进候选**。另留变更、预期机制、受影响任务与验证结果；经base所有者审查再合入，不能由插件自改自验。先在冻结任务上复放，并用不同领域任务检查迁移与退化，比较完整义务闭合、正确性和实际成本；一个PropertyB成功例或reviewer赞同只能支持候选，不能证明通用增益。[G:32–40、65–89]

## 文件定位

- A `context/ARIS_LEAN_WORKFLOW.md`
- B `research-wiki/PROPERTY_B_RESEARCH_LESSONS.md`
- C `context/ARIS_LEAN_WORKFLOW.md`
- D `research-wiki/PROPERTY_B_M6_GE67.md`
- E `research-wiki/PROPERTY_B_FAILURE_ATLAS.md`
- F `research-wiki/PROPERTY_B_M8_M9_INCREMENT_20261029.md`
- G `context/MATH_AGENT_HARNESS_SYNTHESIS.md`

## 附录：现有技能的有界来源映射（仅读入口，不执行工作流）

1. `proof-orchestrator`已有run目录、来源清单、续接与单一当前义务，可复用为base持续证明记录；PropertyB补实际分支地图与哪些分支已返回原染色。源：`/Users/rfy_naiveai/.codex/skills/proof-orchestrator/SKILL.md`，§Run Directory、Continuing a Project、Status Labels。
2. 该技能的GPT Pro／DeepSeek升级是特定授权路线，不能直接当base自动选模型策略；PropertyB项目指定的Grok／Gemini路由另由项目政策提供。源：同路径§Role、Workflow。
3. `formula-derivation`已有固定目标、不变量、假设／符号、恒等式／命题／近似／解释分流及推导图，可复用为base推导组织；PropertyB补共同H、度数守恒、真实坏对等不变量及其推导。源：`/Users/rfy_naiveai/.codex/skills/formula-derivation/SKILL.md`，Workflow Steps 2–6。
4. `research-wiki`已有论文／idea／实验／claim关系与预算内query_pack，可复用为base持久记忆；PropertyB补可复用引理、失败参数域、实际覆盖及重试条件。源：`/Users/rfy_naiveai/.codex/skills/research-wiki/SKILL.md`，Core Concepts、query。
5. wiki严格区分实验证据边与PROOF状态，后者由proof-checker维护；base应保留此区分，不能由搜索器或插件成功日志直接升级定理。源：同路径Hook 3、Hook 4。
6. `research-review`已有主材料审阅、原session续接、异议回应与真实模型／读取范围trace，可复用为base审阅适配；其ML顶会prompt不能原封照搬，PropertyB补选锁、覆盖、量词和计数义务。源：`/Users/rfy_naiveai/.codex/skills/research-review/SKILL.md`，Workflow Steps 1–3、6。
7. `lean-formalize`已有原输入→条件结果→原结论的连接表、最高未闭连接优先、失败层次区分，可复用其通用原则；PropertyB补迹恢复、配额和分类完整性的具体声明。源：`/Users/rfy_naiveai/.codex/skills/lean-formalize/SKILL.md`，§2、Implementation loop、§3。
8. 其指定目标构建、实际类型／传递公理审计和可复现交接可直接成为base的可选Lean验证适配；PropertyB提供目标模块、原题反译和实际caller。源：同路径§5、§6。
9. 这些入口已经提供可复用的指令与部分helper，**不等于已经实现通用自动证明调度器**；跨插件任务选择、停止判断与base变更晋升仍是待设计、待检验的能力，本文未实现或测试它们。
