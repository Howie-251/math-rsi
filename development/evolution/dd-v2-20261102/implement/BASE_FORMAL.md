# B1：仅形式目标直接进入 Lean 验证

2026-11-03。按本轮已集成的`mathrsi-meta-evolve`及`EVOLUTION.md`执行：先读技能与本轮采用决定，再修改现有base v1。范围仅verify、research、assemble及verify的一份具体参考；没有改ARIS原件、docs、README、历史源资料或旧Goal。没有另建主流程、设置开工独立验收门或重跑DD Lean。

## 原执行、证据与实际修改

旧verify支持按需Lean，但图中Lean仅在checker之后的汇合点出现，§2又说“完整候选仍进入checker”；research完整候选调用块同样默认先proof-checker。对于只要固定形式见证的输入，容易先要求TeX/自然语言审计。上游lean-formalize明确standalone Lean不自动要求paper-audit，DD固定F4出口是具体触发。

修改文件：

- [mathrsi-verify/SKILL.md](../../../../base/skills/mathrsi-verify/SKILL.md)：执行图增加B→Lean；输入表和进入段直接选择仅形式目标；§2限定自然语言正式审计；§4写明原声明对齐、实际导出/定义/build/传递公理、缺口返回与局部caller；§5不虚构未运行的canonical audit。
- [mathrsi-research/SKILL.md](../../../../base/skills/mathrsi-research/SKILL.md)：同步执行图、起点表、路线阶段的审计边界、verify调用块及父消费。只验Lean出口无需先assemble/TeX/checker；同时要求自然语言正式审计时两项按原合同执行。维护段沿本轮meta合同写实际使用核查，未继续要求独立试用必经。
- [mathrsi-assemble/SKILL.md](../../../../base/skills/mathrsi-assemble/SKILL.md)：形式目标不需写作时直接返回caller建议verify的Lean分支；实际模块尚缺连接交caller处理，不自动造正文。保留自然语言装配、writer实作与原caller唯一调度。
- [references/lean-target-entry.md](../../../../base/skills/mathrsi-verify/references/lean-target-entry.md)：随仓真实F4公式图输入、导出、定义与历史审计的完整消费例，所有原件链接到DD插件archive，未copy整库或依赖作者机器外部路径运行。

实际差异见[BASE_FORMAL.diff](BASE_FORMAL.diff)，含新增参考。三份原技能是同一入口契约的原位修订，保留原有流程和有效调用；新增参考承载具体例子，实际最终diff为准。

## 本作者按新入口静态消费F4出口

本轮输入是“仅核固定F4公式图的形式出口，复用历史构建，禁止重跑旧Lean”，因此直接按verify§4消费原件，未调用assemble、proof-writer、TeX或proof-checker。

实际读取：仓内archive的`formal/DegreeDiameter/Portfolio/F4Graph3840Exact.lean`、图定义中`stepVec/fiberStep/forward/graph`、`SingleExtension.lean`的`DiameterAtMost`、`F4Graph3840Diameter.lean`的实际decoder调用、`formal/F4Graph3840Audit.lean`，及`research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/`中的Exact_RESULT、Audit_RESULT与完整Audit.log。已有关键证明阅读继续复用，本轮不声称重审全部依赖证明体。

消费结果：

1. `DegreeDiameter.Portfolio.F4Graph3840.concrete_order_degree_and_D3`给3840阶、任意点degree≤20及`DiameterAtMost graph 3`。`diameter_exact_three_in_project_definition`另给非D≤2。不是把名字当结果，而是对照源码类型与Audit.log实际展开打印。
2. `DiameterAtMost`确为每对端点存在实际`G.Walk u v`且length≤D，相等端点可零步。`graph`是Fin3840上的实际公式邻接，未把外部直径certificate作为主定理假设。
3. 历史Exact_RESULT记录exit0、2.141916 CPU秒；历史独立import审计Audit_RESULT记录exit0、2.132108 CPU秒。Audit.log打印定义、两个实际导出及传递公理，均为`propext, Classical.choice, Quot.sound`。
4. 本次只静态消费上述历史证据，未在本机运行Lean，不能称新构建、干净重建或第二台独立复现。所读源码与日志支持该固定形式目标的历史验收；没有认证ASCII文件解析/一致性、恰20正则、Mathlib ediam等式、全参数构造或世界纪录。
5. 自然语言正式审计不是本次输入，故未生成PROOF_AUDIT；指定跨模型review状态不从exit0推断。结果交本轮维护协调者。若同一调用来自prove局部义务，仍回该原prove，不自行转handoff或调度第二条同级链。

这是一项实际入口选择与历史证据消费，非新的数学证明/编译实验，也非独立使用者试跑。

## 语义核查与结果

逐项读回三份实际diff，核对两种请求没有合并：仅形式目标直接Lean；同时需要自然语言正式审计则沿原§2–3执行checker并分别消费。局部返回原prove、完整verify返回唯一主dispatcher、checker内部Lean回原audit均保留。数学缺口回prove与API问题内部修分开；`Certificate→Target`仍须供给实际certificate。旧证据复用不伪称本次执行，缺build/axiom仍待核。

实际机械检查见[BASE_FORMAL_CHECKS.json](BASE_FORMAL_CHECKS.json)：四份改动文件63个本地引用全部存在；`git diff --check` exit0。首轮引用检查发现F4图定义文件误写为不存在的Definitions后缀，已改为实际`F4Graph3840.lean`并重查为0缺失。检查没有运行历史数学命令，不把链接成功叫数学通过。

交回Root：B1实际修改与F4静态消费已完成，可直接纳入本轮真实diff讨论和采用判断。未执行新Lean、新proof-checker、新付费review或独立全流程试用；不声称通用提速或新版解题率已验证。
