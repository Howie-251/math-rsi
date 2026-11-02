# v2：在现有v1上吸收DD研究经验

本轮v2保留v1的九项解题技能、五个子workflow、ARIS调用适配和Property B插件，新增独立外层维护技能与Degree–diameter插件，并在原技能的真实调用处作增量修改。没有另建一套base。执行顺序是先写成并集成[mathrsi-meta-evolve](../base/skills/mathrsi-meta-evolve/SKILL.md)，再由Root读取该技能，消费DD原件并组织本轮实现；此前的阅读是输入，不追认为已经运行了尚未存在的技能。

本页解释当前实现与用法；最终讨论、修法、采用及未测范围由[本轮EVOLUTION](../development/evolution/dd-v2-20261102/EVOLUTION.md)维护。原DD由其历史研究流程完成，Property B先由ARIS完成；这些结果是方法来源，不是MathRSI v1/v2的解题率、提速或递归改进实验。

## 原流程具体改了什么

| 真实触发 | 现有实现中的增量改变 | 谁消费结果 |
|---|---|---|
| 仅核固定Lean公式图时，完整候选措辞容易把它先送TeX/checker | [verify](../base/skills/mathrsi-verify/SKILL.md)直接Lean分支；[research](../base/skills/mathrsi-research/SKILL.md)入口与调用同步，[assemble](../base/skills/mathrsi-assemble/SKILL.md)不强迫为形式目标写正文 | 原caller核原声明、定义、实际export/build/传递公理和pending；仍需自然语言正式审计时执行原checker合同 |
| 新公开保证超过正在追的门槛，但只追加文献链接而任务照旧 | [survey](../base/skills/mathrsi-survey/SKILL.md)返回同域代入与受影响候选；prepare/specify、[route-loop](../base/skills/mathrsi-route-loop/SKILL.md)及[prove](../base/skills/mathrsi-prove/SKILL.md)消费到实际队列 | 竞争目标撤掉只服务旧门槛的待派任务并接新输入；用户固定对象/定理继续，旧合法性不撤销 |
| 图源、连接规则或域已变，旧失败仍被整体沿用，或所有正证据被整体清空 | route-loop/prove先写新旧对象关系，再逐项核正定理假设与负记录限制 | 可继承结论继续用，只补受影响连接；限制已解除的否证收回原域，旧障碍未变不换seed重复 |
| 单路满秩等局部充分门失败，被误写为共同覆盖不可能；必要门通过被写成构造已得 | route-loop/prove回读实际量词，要求插件返回同一源输入的路线像、共同参数、并覆盖或未覆盖见证 | 保留真实共同覆盖义务；只有已证必要且全域拒绝才闭准确族，PASS存活输入继续证明实际构造 |

这四项不是新原则表替代执行。每项都落在原技能的输入、具体动作、产物消费或返回点；原始触发和修订链见[meta证据参考](../base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md)。DD公式与特定模型进入插件，历史n、预算、旧Goal状态和模型路由留源任务资料，未变成通用默认。

## DD如何接入五个子workflow

[Degree–diameter插件](../plugins/degree-diameter/README.md)研究有限简单无向图的最大度与直径。它提供四个实际入口：

- [mathrsi-degree-diameter](../plugins/degree-diameter/skills/mathrsi-degree-diameter/SKILL.md)：固定对象、目标与当前阶段，选择领域方法。
- [dd-construction](../plugins/degree-diameter/skills/dd-construction/SKILL.md)：当前图覆盖增点、冻结源邻域克隆、仿射共同路线与GQ构造，交实际定义与caller。
- [dd-obstruction-certificate](../plugins/degree-diameter/skills/dd-obstruction-certificate/SKILL.md)：有限必要域、精确证书、覆盖及原图到Lean接口，区分UNKNOWN与已排除范围。
- [dd-transfer-diagnosis](../plugins/degree-diameter/skills/dd-transfer-diagnosis/SKILL.md)：换源、field、连接规则和公开基线后重判旧证据与下一任务。

prepare/survey共享一次原文与公开基线调查；route-loop交失败输入给迁移诊断和构造探针；prove执行实际构造或排除；verify消费有限命题、原图连接与形式出口；handoff取所需证明、源码、命令和准确状态。父流程持有当前义务与唯一后继调度，领域技能返回原调用点，不复制新主控。详细输入返回见[插件契约](PLUGIN_CONTRACT.md)与[工作流地图](WORKFLOWS.md)。

插件随仓提供原research-wiki及支撑它的证明、程序、失败、结果、审阅和形式化资料；整理层告诉使用者何时深读哪些原件。源包原本未包含的大文件或工具链不因复制而补齐，范围见[归档说明](../plugins/degree-diameter/archive/README.md)。归档只读，新题规格、证据、wiki与恢复入口写当前工作区；历史ACTIVE和恢复命令不是当前授权。

## 怎样使用

新DD题可直接给agent：

```text
读取本克隆base/skills/mathrsi-research/SKILL.md和
plugins/degree-diameter/skills/mathrsi-degree-diameter/SKILL.md。
在我的任务工作区处理<原图目标>，先恢复规格、wiki与实际证据。
按已有材料进入prepare、route-loop、prove、verify或handoff；
在阶段内调用相关DD技能，读取结果后回原义务继续。
公开比较与图合法性分开；新结果写任务wiki，不改archive或base。
```

项目发现支持Claude的`/mathrsi-degree-diameter`及Codex的`$mathrsi-degree-diameter`，其余三个入口同理；`.claude/skills/`与`.agents/skills/`均为仓内相对链接。发现未刷新时直接读真实路径。模型服务、Lean和外部工具仍按[快速开始](QUICKSTART.md)准备。

单独维护现有MathRSI时：

```text
读取本克隆base/skills/mathrsi-meta-evolve/SKILL.md并执行。
基于当前版本，消费<研究来源/关键原件/已有报告>，改进<具体调用或领域能力>。
允许写入<范围>；源研究保持只读，计算和review按已有授权。
有EVOLUTION.md则从真实下一动作恢复；形成实际diff、具体讨论和使用结果，
修真实问题后决定采用，不新建一套解题主workflow。
```

meta是独立外层能力，不是每次handoff后的自动第六阶段。它接受真实数学档案而不伪造events或强制五条记录；需要独立数学核验仍服从原题合同，但不把无历史agent重跑整流程设为普通维护前置。ARIS原版meta-optimize/meta-apply保持自己的双端合同，不能与数学适配混称。

## 本轮实际支持的范围

B1作者已按新verify入口读取仓内F4实际导出、定义、历史构建和公理审计，准确返回固定形式目标；[实现记录](../development/evolution/dd-v2-20261102/implement/BASE_FORMAL.md)明确本轮没有新Lean构建、proof-checker运行或独立全流程试用。DD有界程序与其余行为消费的真实结果，以插件evidence和EVOLUTION所链接记录为准，不以本文补写未执行项目。

现有v1的搬迁、协议与局部行为试用继续在[VALIDATION](../development/VALIDATION.md)中保留自己的范围。原数学证明不因插件复制升级；链接、别名和格式检查也不能认证新定理。新长题和系统效率评测仍需后续真实运行。
