# 双配额容量修复的有界局部审阅

review_independence: same-family  
acceptance_status: provisional  
reviewer: fresh delegated Codex agent `/root/aris_pipeline_workflows/quota_local_review`  
日期：2026-11-01  
返回点：原 prove 调用，消费本回执后完成其下游。

本记录保留本次 reviewer 的原始意见。只审一般有限实数 quota 修复推导与给定单槽双 quota caller；不是全项目或 Property B 证明审计，没有运行完整 proof-checker，没有生成 PROOF_AUDIT，也没有运行 Lean、网络或付费外呼。

## 原件与实际范围

完整阅读本仓 `AGENTS.md`、`base/skills/mathrsi-verify/SKILL.md`、`base/skills/skills-codex/research-review/SKILL.md` 的入口；完整阅读本目录上一级的 `INPUT.md`、`PROOF_DRAFT.md`、`check_instance.py`、`CHECK.json`。另外读取来源 `plugins/propertyb/skills/mathrsi-propertyb/references/mathematics/03-permutations-bad-pairs-and-duality.md` 的 L7 定理、实数纸面证明及应用范围说明（第78–118行；命令还显示了相邻段落）。没有检查其链接的历史 Lean 证明或其它 Property B 分支。

这里复用 verify 的局部返回约定与 research-review 的原始材料审阅、准确执行范围和原始意见保留机制。当前代理是调用方新委派的 reviewer，直接核对上述原件；没有另起完整研究评分、额外审阅代理或上游正式审计。

## 原始审阅意见

**未发现本次范围内的实质数学或 caller 连接问题。** 一般修复定理按原假设成立，具体输入既可行又使修复界取等；错误加强被同一原始输入直接否定。

1. 一般推导的符号与条件足够。令 `t_s = Σ_q δ_q a_qs` 后，用 `δ_q ≥ 0` 乘配额并交换有限求和，得到 `Σ_q δ_q b_q ≤ Σ_s t_s z_s`。对任意实数 `e = t_s − w_s`，`e < 0` 时由 `z_s ≥ 0` 得 `e z_s ≤ 0 = c_s max(0,e)`；`e ≥ 0` 时由 `z_s ≤ c_s` 得同式。求和移项就是目标，既不要求 `a,w,b` 非负，也不依赖最优性或强对偶。`c_s ≥ 0` 已由原来的区间约束推出。空索引集合未造成例外。来源 L7 的 `q_q` 映到本题 `b_q`，没有变更假设或结论。

2. caller 确实提供全部前提。单槽、两配额、所有指定数据为1时，每条 quota 为 `z ≥ 1`，容量给 `0 ≤ z ≤ 1`，所以实际 `z=1`。每条独立应用的罚项为0，因此各得同一个成本 `wz ≥ 1`。相加所得只能是 `2wz ≥ 2`；重复使用共享成本后声称 `wz ≥ 2` 不成立。原输入已经显式指定 `z=1`，无需另造见证。

3. 共同修复使用同一个槽：`t=2`、容量罚项 `1·max(0,2−1)=1`，故共同下界为 `2−1=1`，等于实际成本。错误加强要求实际成本1至少为2，已被这份满足全部前提的原输入否定；它不是被不可实现的 quota 表否定。

4. 检查器与记录的范围表述准确。作者脚本的45次带符号标量检查只是诊断，不能证明一般实数域；一般域由上述逐项代数论证覆盖。脚本中的单槽特化与原输入一致，`CHECK.json` 和实际输出相符。

没有要求作者修复的局部发现。`PROOF_DRAFT.md` 的“待局部verify回执后继续下游”是调用状态标记，原 prove run 可据本回执完成最终消费段；这不是本 reviewer 获得的其它文件写入授权。

## 实际执行证据

- 执行 `python3 /Users/rfy_naiveai/Desktop/MathRSI/development/workflow-redesign/behavioral-trial/check_instance.py`，退出码0。实际输出：`feasible_z=1`、`actual_cost=1`、两个单独下界均为1、错误共用成本和为2、`incorrect_bound_refuted=true`、罚项1、修复界1、`repaired_bound_valid_and_tight=true`、`signed_scalar_checks=45`。这是原脚本重放，不称独立算法核验。
- 另在临时标准输入中运行 reviewer 自写的 `fractions.Fraction` 小检查，逐一核 `0≤z≤c`、两条 quota 与两乘子非负，独立计算 `(cost, raw, t, penalty, repaired)=(1,2,2,1,1)`，检查 `cost<raw`，并与原 `CHECK.json` 的成本／罚项／修复界比较；退出码0。原始标准输出：`Independent exact caller check: hypotheses hold; cost=1, raw sum=2, t=2, penalty=1, repaired=1; recorded CHECK agrees.` 该精确算术只核这个实际 caller。

本次只新写本 `REVIEW.md`。一般定理与 caller 的局部结论可以返回原 prove 调用继续；不据此升级任何历史数学结论、全项目审计状态或通用工作流有效性。
