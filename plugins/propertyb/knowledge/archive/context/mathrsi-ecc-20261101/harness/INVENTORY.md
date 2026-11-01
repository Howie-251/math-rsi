# ECC Harness 有界源码盘点

2026-11-01。源根 ` /Users/rfy_naiveai/Desktop/aris4math_v2/ecc_mathagent_harness_20260929/`（下文路径相对此根）。它包含四个实际 Python 包，并非单个 verifier。

**可复用：** `project/mathagent/protocols.py` 已分离 Task.evaluate/public_config 与 ProposalProvider，ProposalContext 带岛、代、角色、探索轨道。`models.py` 的分数／排序键与 goal_reached 分离；`engine.py` 有候选谱系、预算停止、检查点及恢复时重新调用 evaluator。`llm.py:590` 将父候选、见证反馈和坐标组成上下文。它适合作为 base 的“有确定性评价器的候选搜索后端”，不宜直接承担全部数学研究调度。

**需拆除领域绑定：** `mathagent_team/provider.py` 虽有四角色、共享调用钩子、审阅／修订，但 `_exact` 直接读取 verification.proof_level/distance；controller 又输出 best_distance。`ledger.py` 的请求前预约、失败记账、STOP 检查可抽取，固定四角色／单岛坐标需参数化。`mathagent_portfolio/search.py` 直接导入 ECC LocalEvaluator，以重量谱和行空间管理候选，五操作器均改生成矩阵；roles.py 的计划 schema 同样是 ECC 专用。它不是通用策略组合器。

**验证边界：** `mathagent_ecc/evolution.py:342` 固定 n/k、预检资源后调用 verifier；`verifier.py` 区分 rank/probe/exact，不把探针未命中当证明。GF(2)、码规格、低权见证、本地变异留在 ECC 插件；分阶段证据／inconclusive 的设计可借用。

**与提案差距：** 所读接口围绕候选 JSON＋现成 evaluator；未见原命题义务图、AND/OR 证明路线、实际输入到条件引理的连接、文献检索／长期知识治理、插件瓶颈驱动的重新决策、独立核心改进评估。Portfolio 已有近期实测历史和停止建议，但不是这些能力的实现。建议组合现有搜索内核与新增研究流程层，不整体改名为 mathrsi-base。

阅读范围：完整读根 AGENTS/README/START_HERE/SCOPE、project/README、protocols；读 CONTEXT §1–3、handoff_manifest；对上述核心代码只读相关片段及定义定位，另定位 database/models 接口。对照本项目 MATH_RSI_DESIGN.md。未做全面代码审计，未检查所有历史实验；未安装、运行测试／模型／扫描，未改 v2。按本次只读任务约束，未执行包默认 quick 验证。
