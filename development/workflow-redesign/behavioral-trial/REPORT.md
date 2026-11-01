# 双配额 caller 的真实 forward-use

本轮完成了指定的已知引理复用任务，并实际走通 `main → prove → 领域L7/proof-writer → 局部verify → 返回原prove → 总目标`。不是只读流程后写意见，也不是重启旧研究。

## 实际成果

- [INPUT.md](INPUT.md)保存原始量词、假设、目标、实例与执行边界。
- [PROOF_DRAFT.md](PROOF_DRAFT.md)给出完整有限实数证明和实际caller。系数$a$、权重$w$无需非负；只用$\delta\ge0$及$0\le z\le c$。没有弱化原目标。
- [check_instance.py](check_instance.py)已实际运行exit0，精确输出见[CHECK.json](CHECK.json)，argv/cwd/退出码/完整stdout见[RUN.json](RUN.json)。实例成本1；两个单下界各1；错误叠加2被同一可行输入反驳；容量罚项1使共同修复界为1且取等。45次带符号标量检查只作诊断，一般实数域由正文证明。
- [VERIFICATION.md](VERIFICATION.md)是局部scope回执。fresh Sol实际读取原件、重放脚本并另写Fraction算例，原始意见见[REVIEW.md](local-review/REVIEW.md)，无本scope实质发现，`same-family/provisional`。
- 调用者已读回验证结果并返回原prove，完成最后的$1\ge1$连接与错误叠加解释；记录见[CALLS.md](CALLS.md)。未在局部verify成功后误跳全项目交付。

## 选择与跳过的阶段

实际全文读取新main和prepare，并按main的短证明/已有明确方法分支直接进入prove。领域bound-lab全文已读，仅执行当前L7数学任务；L7原文、完整纸面证明及其输入边界已读。ARIS proof-writer全文已读并执行其命题、假设、依赖、正文与检查步骤，显式指定本目录输出。

没有外网文献调查或完整survey：用户给定原目标与已证库引理，仓内原文足以核条件；没有查新要求或未确认关键进口。没有route-loop：方法与目标已明确，无须发明候选和模型评分。没有formula-derivation：对象与公式已固定，直接证明更短。

**没有正规proof-checker整证审计、Lean或付费review。** 本次明确允许已知引理及caller的局部验证；未准备完整TeX审计输入、未执行其完整必要步骤，因此没有创建PROOF_AUDIT，也不声称已执行完整research-review共识循环。fresh同家族局部意见与确定性精确结果各按实际范围报告。原先已完成项目的数学状态未被本试用升级或重验。

## 接口观察

本任务未遇到阻止执行的接口缺陷。新main允许已有方法直接prove；prove允许准确局部scope提前verify；verify明确返回原调用处，这三点在实际文件与执行中一致，避免为一个已知短引理制造全套准备、路线和整证审计。

本轮读取main时源文件仍在由Root完善；执行结束对其Markdown相对链接作实际只读检查，缺失为0。没有为了测试修改任何SKILL或研究源工程。没有将同一agent执行技能称为额外宿主工具调用；技能调用的真实含义及读取/产物消费顺序在CALLS写明。fresh reviewer是另外派发的实际agent。

这是一项已知答案、设计者参与执行的开发行为测试，确认上述小任务的连接和产物，不能据此声称盲测、新发现能力、跨领域效率或通用RSI有效性。没有阻塞项；全部文件只写在本目录，可用所列脚本重放算例。
