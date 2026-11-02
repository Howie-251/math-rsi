# FORMAL_STATUS｜未通过内核检查

形成方式：本次02读取实际源码/错误日志，并从上一回复可保存正文转存整理；01时未生成本文件。原转存见`dependencies/research_source/FORMAL_STATUS_INLINE.md`。状态**BLOCKED_ENVIRONMENT / NOT_KERNEL_CHECKED**。本次02新增Lean调用0，没有试编译，没有创建或宣称可编译的lake工程。

## 1. 实际源码、命题及执行

|文件|实际命题|已取得的运行依据|状态|
|---|---|---|---|
|formal/ParentColumnBridge.lean（100行）|N59Continuation.parent_repeat_le_column_budget；isolated_exception_parent_repeat_zero；commonWeight_ge_one；triangle_repeat_ge_one；adjWeight_nonneg|有源码与一般环境记录；**没有本文件单独运行命令/输出**|SOURCE_SAVED；未取得内核检查；不能把另一文件exit127归给它|
|formal/TriangleTransport.lean（123行）|N59TriangleTransport.triangle_shadow_transport；impossible_shadow_avoidance；distinguished_support_must_meet；actual_repeat_distinguished_support_must_meet|formal/triangle_transport_attempt.log：2026-09-28T10:46:47Z，`lake env lean formal/TriangleTransport.lean`，`lake: command not found`，exit127|COMPILER_NOT_STARTED / NOT_KERNEL_CHECKED|
|继承TransportBridge.lean（95行）|N59.edgeCount_swap；no_extra_column；adjWeight_symm；graph_no_extra_column|dependencies/codex_return_20260922/dependencies/implementation/local_checks/formal.json、formal.log，2026-09-21旧03执行exit127|历史环境失败，不是本次运行或通过|

`formal/minimal_network_check.log`保留原最小网络检查及DNS失败；02未重试。Lean/Lake版本未知，Mathlib版本未知；只有`import Mathlib`不能确定库版本。两份源码的`#print axioms`行是待执行命令，**没有任何实际输出**，不能填写空公理集、标准公理集或无sorryAx的内核结论。

## 2. 与自然语言的逐项对应

ParentColumnBridge的`repeatWeight`在对角直接设0，非对角用实际共同邻点式；与N59矩阵式的对角一致性依赖8正则，尚未形式化。其单项界和孤立列零需要真实父邻接、非负性、交换等式、根支撑—异常点的BFS对应；源码没有证明整张A1/A2，也没有形式化N1、N2或N15。

TriangleTransport前三条允许显式非负B和交换假设，最后一条绑定原G的A²+A−7I−J；这只是[T]§9.3的图语义步骤。唯一共同邻点、B(r,α)=0、B(α,e)≥1及非邻支撑避开e等输入应由P核心正文导出，不是新增公理。尚缺§9.2的两个例外计数、R2伙伴位置、全部t1分类、中心第二三角形与η/三角形端口不可重合的形式连接。

N5的封闭B分量/严格换根、§7与N9的非极值根资格、N12/N14/N15的全图类型排除和连续换根均没有完整对应Lean命题。逐条表见CODEX_HANDOFF.md和JSON constraint_registry；空lean_theorems表示实际未生成，不是省略命题名。

## 3. 自然语言与形式化分账

N8和其他有效结果按原完整自然语言证明、明确继承前提及守卫交付。形式化未完成不自动撤回这些证明；也不满足“Lean已检查”。没有一个新根层/粗类关闭标FORMAL_VERIFIED。RAW作为继承工作前提未被本轮两份草稿验证。

源§6.1的K>s合法根资格歧义列SCOPE-01；不能为了编译把“所有见证根均合法”塞入新假设后宣称验证原命题。只能先忠实形式化已明确K=s的应用，其他用途仍阻塞。

## 4. 下一方可做与不能做

Codex可恢复实际工具链/依赖、修复语法/API版本问题、忠实形式化，并保存完整命令、版本、输出、#print axioms。环境/编译失败不等于数学反例；实质桥梁未证须退回理论，不靠axiom/sorry/admit、空化候选集或削弱结论过关。即便两个局部模块将来通过，整P16/K3/N59仍须另行承接完整依赖。
