# ECC 来源与检查器地图

本地图按“当前要证明什么”定位资料。路径是历史 ECC 项目内的相对路径；MathRSI 不复制这些大数据、搜索器和检查器。
使用者在当前任务里明确 `${TASK_ROOT}` 为单题工作区，`${ECC_SOURCE_ROOT}` 为有权读取的领域资料根，或由本题 source-map 给出等价位置。
这些是路径代号，不是自动配置；未提供历史目录时不猜作者机器路径，也不启动别的项目。

## 首版采用的来源与阅读范围

|来源|本次采用内容|边界|
|---|---|---|
|Property B 来源项目的 `MATH_RSI_DESIGN.md`|五类接口、义务与替代路线、共同对象和成本|架构方法，非求解器实现|
|同项目 `MATH_RSI_ECC_COMPARISON.md`|构造与全域排除、发现与覆盖、旧 harness 的适配范围|历史对照与有界源码盘点摘要|
|ECC 项目 `MATH_RSI_DOMAIN_HANDOFF.md` §1–7|原对象、五层否定义务、完整扫描修补、固定母码、群作用、规范冲突和停止条件|实际阅读交接主体与案例，不把交接日期当新数学进展|
|该交接的 §2 阅读地图|原规格、verifier 函数、完整覆盖及重放入口|以下原始文件入口来自交接；本次插件开发未逐一重读所有源码或重跑|
|该交接 §8|历史断点隔离与后见答案泄漏|本插件不执行复放，也不以已知答案示例宣称新发现能力|

原领域工作使用 ARIS（[上游仓库](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)）组织知识、推导和审阅。本插件重新组织领域指导，不复制其完整技能；宿主调用时读实际安装版本。
旧题的 `sound-modulo-imports`、模型审阅和本机计算状态属于对应原命题，不迁移为新任务的证明。

## 原规格、数学链与文献

|需要回答的问题|历史项目内相对路径|如何使用|
|---|---|---|
|构造与否定分别要求什么|`FORMAL_SPEC_45_11_17.md`|旧任务示例；当前参数仍以本题规格为准|
|完整旧题为何能收尾|`HANDOFF_FOR_REVIEW.md` §1–5|检查归约、外部输入与计算连接，不当作后续新题的证明|
|详细义务依赖|`work/goal-20261006-wave2/global_closure/PROOF_SKELETON.md`|定位 T/E/R/C/X/F/G/Z 具体义务；不是新任务固定编号|
|外部定理与分类上限|旧 handoff §3 及其原文定位|核对域、满支撑、偶性、维数、距离和实际读到的版本|
|经验与失败边界|`research-wiki/ECC_LESSONS.md`|按当前疑问继续读；本插件未将它全部复制|
|旧 harness 适配边界|`ecc_mathagent_harness_20260929/project/` 的实际说明与源码|候选后端，不当通用证明引擎；确认当前依赖再调用|

目录导航可能滞后于原始报告，恢复时读最新规范与实际结果；不根据旧聊天或单个“在途”词判断今日 Goal 状态。

## 检查器按义务接入

|义务|现有入口定位|检查能力与未覆盖部分|
|---|---|---|
|显式矩阵构造|`ecc_mathagent_harness_20260929/project/mathagent_ecc/verifier.py` 的 `verify_code`；`gf2.py` 的 `gf2_rank`、`exact_distance_analysis`|合法形状、实际秩及设置范围内的距离；调用者仍核对原规格与精确模式|
|直接独立验距|同项目 `idea-stage/verification/independent_binary_code_verifier.py` 的 `verify`、`_enumerate_words`|实际矩阵全词；先读真实 CLI 或函数接口，不猜参数|
|分类代表与执行绑定|`work/goal-20261006-wave2/global_closure/COMPUTATIONAL_COVERAGE.json`、`REPRODUCE.md`|阅读已完成范围，区分轻量读回与重扫描|
|陪集无遗漏|`work/goal-20261006-wave2/even40k7_rank3_extension/coverage_audit/full_replay/REPORT.md`|另一套完整生成的实际范围；成员比较不能冒称新生成|
|pair 拒绝见证|`work/goal-20261006-wave2/global_closure/pair_certificate_replay/REPORT.md`|重放相关 pair 的低权见证与成员距离；不负责重新生成 F 全域|
|固定父码 SAT 证书|`work/goal-45-11-17-20261007/wave6/kohnert48_complements/proof/REPORT.md`|CNF 证书的确定性重放；母码到编码的数学连接另读对应 `DERIVATION.md`|

以上是函数／报告入口，不是可直接粘贴的统一 CLI。先在授权资料范围内读当前 README、源码参数和重现说明，再将实际命令写入本题核验工作包。
不要因插件有检查器地图就认为依赖、二进制、数据或工具链已经安装。
确需运行时使用当前任务允许的资源和输入；历史一次完整重扫不授权现在重扫整个域。

## 联合表示与效率案例

|当前困难|历史路径与定位|提炼的判断|
|---|---|---|
|固定输入能否先做便宜必要判定|`work/goal-45-11-17-20261007/wave6/no40_q42_a16_joint_structure/REPORT.md` 与同目录 `PROOF_AUDIT.md`|pair 图为空可终止该已推导尾型，不扩大为全域不存在|
|共同核是否值得批量执行|同 wave6 的 `cube110_whole_branch_plan/SHARED_KERNEL_MATH.md`、`all162_shared_cube_batch/REPORT.md`|先证共享交集与尾基运输，再按实测完整做完；计算齐备与整支审计分开|
|取商怎样保留共同坐标|同 wave6 的 `n37_pair_swap_compression/REPORT.md`|同一群作用、第一行稳定子和后续运输；一个快实例不代表全分支|
|为何少量核心仍太贵|同 wave6 的 `allcore_joint_global_compression/DERIVATION.md`、`allcore_support5_joint_gate/REPORT.md`|计共同自由度和组合距离；局部全非空且零新增排除时重新选路|
|多个规范化是否兼容|同 wave6 的 `joint_module_columns/INDEPENDENT_MODEL_REVIEW.md`|检查三锚与边际规范是否同时可满足|
|类图是否丢共同嵌入|同 wave6 的 `module_graph_feasibility/NOTE.md`|逐边存在嵌入不能推出共同三头嵌入|

这些文件是历史案例的进一步阅读入口，本次技能编写主要依据交接中已说明的事实与精确范围，没有冒称重新执行这些程序。

## 本题核验说明的最小内容

给 base 的说明应包含：要检查的明确命题；实际矩阵／母码／集合／模型的所在位置；期望参数与完整输入域；必要的基、坐标或尾空间运输；已有程序真正输出什么；还缺什么数学连接。
独立核验说明共享了哪些源码、数据或生成步骤。另一算法、完整拒绝重放和同一集合再次读取分别命名，不制造虚假的独立实现次数。
如果一个义务没有现成 checker，写出需要证明或实现的具体内容；不要伪造可运行入口。

本题新产物与真实运行记录保存在 `${TASK_ROOT}`，旧证据保持只读。
构造已经通过原合同可直接收回；否定只有在完整覆盖、每个必要输入排除和原题连接都成立时收回。
