请按 MathRSI research-review 的 composed 维护适配给实质设计与可直接采用的中文技能正文。
— composed: development/evolution/v4-global-reassessment-20261108/EVOLUTION.md
执行原件阅读与意见产出，不执行原 Step4–5 论文共识循环，不写文件、不运行数学研究。本次回答交给Root决策实现。
用户最新明确要求：数学研究经常陷入local，虽然不断产出局部表/引理，却无意义消耗token、速度很慢；v4各阶段都要强调，最好强制由几个agent一起评估全题进展、当前路线是否卡局部、是否要跳出来。我们要落实，不停在原则。
请读 base/skills/mathrsi-research/SKILL.md，references/efficiency.md，mathrsi-route-loop/SKILL.md，mathrsi-prove/SKILL.md（均base/skills下），docs/WORKSPACE.md，必要时 development/workflow-redesign/REAL_PROJECT_TRANSITIONS.md。
现有两轮无信息就Root自查不够：能漏掉局部结果增多但主瓶颈不变，也能被已投入该路线的Root自我辩护绕过。
建议一份shared global-reassessment.md由主workflow拥有，各阶段有具体触发hook。不要新建第六解题阶段或堆Python编排器。
请具体解决并写操作正文：
1. 低成本每批启动/收件对原题critical path回看，如何定义真实进展、轮次/预算、局部进展不等于全题进展。
2. 哪些情况强制多agent全局重评：同瓶颈2轮无决策增量、局部结果增长而关键未闭链不变、到预设checkpoint、昂贵扩批/关键假设失败等。别把每次启动和短证明都变成评审。
3. 默认2位独立只读评估者，第三位在成本/覆盖争议时加入？或者3位更合适？要求明确原题全图、反事实‘局部任务成功了还差什么’、新表示/更弱必要条件/直接构造机会、端到端成本。不是证明checker，不需共识评分。
4. 触发后不新增旧路线扩批，保留已有产物和安全在途任务，唯一dispatcher决策continue bounded / reframe / pivot / assemble / abandon branch。怎样防无限‘继续一次’与改名重置计数，又不机械扼杀覆盖充分且有稳态完成估计的必要穷尽计算。
5. reviewer不可用/超时怎么真实降级且不直接解禁盲目扩批；耗尽局部预算不暂停Goal。
6. 给跨prepare/route/prove/verify/handoff的短执行hook及一份可复制派工prompt、Root消费结果字段。要详细可执行，避免空泛和过度防御。
HERO：只针对真实浪费，不删数学验收，不建立新平台。请提出最有价值改法，然后主写上述共享协议草稿；控制在约2500中文字符，文件阅读范围如实注明。
