# 局部验证：L7 的双配额实际caller

调用方为本试用的 `mathrsi-prove`，返回点是PROOF_DRAFT的“消费局部验证并结束原调用”。本次只核一般有限实数推导和指定单槽caller，**不是**Property B整证或任何新下界的审计。

已读取当前 `mathrsi-verify/SKILL.md`全文并按局部scope执行：现有正文完整，不另调全主定理assemble；核L7参数对应、当前实际数据满足前提、精确计算及对原调用的用途。不运行正规proof-checker、Lean或付费服务，也不生成 `PROOF_AUDIT`。

## 确定性结果

实际执行 `/usr/bin/python3 -B check_instance.py`，cwd为本目录，退出0。原始工具结果及argv见RUN.json；脚本stdout见CHECK.json。

直接由配额和容量推得可行区间退化为$z_s=1$，实际成本1。与修复界独立计算的结果：两个原下界各1，错误叠加同一成本下界为2，实际输入反驳它；共同系数2，容量罚项1，修复下界1，合法且取等。45个标量带符号诊断同时覆盖正/零/负系数的样本，不能替代正文的全实数证明。

## 条件与一般证明检查

本题有限性允许交换求和；只需乘子非负，没有把$a,w$误限为非负。负系数分支用$z\ge0$，非负分支用$z\le c$，容量非负由原假设推出。复用L7的纸面实数版本；不把有理Lean声明升级为实数Lean结果。实例两条配额作用于同一个$z_s$，假设全满足。

## fresh局部审阅与返回

实际派发fresh reviewer `/root/aris_pipeline_workflows/quota_local_review`，以无历史上下文输入读取原件；全文意见见[local-review/REVIEW.md](local-review/REVIEW.md)。它检查一般实数不等式、参数映射、单槽caller、脚本和CHECK，未发现该scope内的实质问题；重放原脚本exit0，另以独立写的Fraction算例核前提及$(cost,raw,t,penalty,repaired)=(1,2,2,1,1)$，exit0。原脚本重放与另写算例分别命名，未冒称另一个完整通用证明实现。

记录为 `review_independence: same-family`、`acceptance_status: provisional`；不是跨家族或正式proof-checker审计。调用方实际读取原始回执，未将其中意见重写成canonical PASS。

**返回原prove调用**：局部caller和一般代数推导在本次范围内无待修项，允许它继续应用L7，把实例结论$w_sz_s\ge1$接回原目标。返回没有进入全主定理assemble/handoff，也没有升级任何历史项目claim。
