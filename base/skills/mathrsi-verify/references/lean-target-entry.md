# 仅形式目标：从实际 Lean 出口直接验证

本例说明[mathrsi-verify](../SKILL.md)如何消费已有形式结果，不要求先制造自然语言正文或TeX审计。它来自DD历史构造，适用的是入口选择与证据消费，不把源任务的图参数变成通用要求。历史源码与结果随[DD资料层](../../../../plugins/degree-diameter/archive/source/)提供；新任务状态和运行产物写自己的工作区。

## 输入和实际读取

任务只要求核固定F4公式图的形式出口。读取原目标、[实际Exact模块](../../../../plugins/degree-diameter/archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840Exact.lean)、[图定义](../../../../plugins/degree-diameter/archive/source/formal/DegreeDiameter/Portfolio/F4Graph3840.lean)、[原题审计入口](../../../../plugins/degree-diameter/archive/source/formal/F4Graph3840Audit.lean)。沿Exact的import读取它实际依赖的直径与下界；不要把同目录的未用尝试模块当成证明前提。

两个真实导出位于namespace `DegreeDiameter.Portfolio.F4Graph3840`：

```lean
concrete_order_degree_and_D3 :
  Fintype.card (Fin 3840) = 3840 ∧
    (∀ u, graph.degree u ≤ 20) ∧ DiameterAtMost graph 3

diameter_exact_three_in_project_definition :
  DiameterAtMost graph 3 ∧ ¬ DiameterAtMost graph 2
```

`DiameterAtMost`在[SingleExtension](../../../../plugins/degree-diameter/archive/source/formal/DegreeDiameter/Portfolio/SingleExtension.lean)定义为`∀ u v, ∃ p : G.Walk u v, p.length ≤ D`，包含相等端点的零步Walk。`graph`是`Fin 3840`上的实际公式邻接，方向由有限域仿射步给出；它不是一个将外部直径证书作为假设的定理。

读取[历史Exact构建结果](../../../../plugins/degree-diameter/archive/source/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/F4Graph3840Exact_RESULT.json)、[独立import审计结果](../../../../plugins/degree-diameter/archive/source/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/F4Graph3840Audit_RESULT.json)及[完整审计输出](../../../../plugins/degree-diameter/archive/source/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/F4Graph3840Audit.log)。后者实际打印定义、两个导出类型与传递公理，仅为`propext`、`Classical.choice`、`Quot.sound`；审计结果记录exit0。原命令中的作者机器绝对路径属于历史，不是新克隆可直接运行的命令。

## 按修改后的入口行动

先判断用户要核的是上述形式命题，还是另要可读证明的正式审计。仅形式目标直接进入lean-formalize，交真实模块、原声明、定义和已有证据，执行其适用流程；没有尚待写作的正文就跳过assemble/writer，没有自然语言正式审计要求就不启动proof-checker。不生成一个表示未运行checker的canonical PROOF_AUDIT。

已有有效构建可按任务范围复用。若当前授权仅为历史证据消费，读取源、结果和日志后明确本次未构建；若任务要求在当前工程运行，按lean-formalize选实际目标模块、固定依赖并保存新命令与输出，不能拿历史exit0替代新运行。缺关键定义、原题连接、目标构建或公理证据，标明缺什么并处理；新数学回原caller建议prove，API/工程问题在形式化内部修。指定跨模型审阅是否完成另按真实回执报告，不以源码编译替代。

若还要求自然语言证明正式审计，给该正文及上述形式证据，按verify§2–3的proof-checker合同运行。两份证据各自支撑自己的scope，不把形式定理升级为外部文件解析器、完整论文或公开纪录认证。

## 可消费的返回

只消费上述历史材料时，可以返回：

```text
范围：固定F4公式图的两个形式出口；本次静态读取并复用历史构建/审计，未运行Lean。
已对齐：3840阶、最大度≤20、每对端点有实际≤3 Walk，且项目定义下非D≤2。
证据：Exact_RESULT与Audit_RESULT记exit0；Audit.log给实际定义、导出与标准三项传递公理。
没有由这些声明证明：恰20正则、ASCII边表解析/一致性、Mathlib ediam等式或全球纪录。
自然语言正式审计：本次未请求、未调用proof-checker；其它指定review缺项另列。
返回：原verify调用方消费该scope；若来自prove局部义务，回原prove继续，不转最终handoff。
```

同一返回也可能是“导出只证明Certificate→Target，实际输入尚未构造Certificate”，此时原形式目标保持未闭。对于新任务，不照抄本例参数、公理允许集或历史状态；按真实目标读取和执行。
