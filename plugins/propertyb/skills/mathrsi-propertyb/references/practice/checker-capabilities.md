# 检查器能力地图：按当前缺口复用，不统一盖 PASS 章

同一个退出零可能分别表示“找到真实反例”“必要松弛仍可行”“全部采用型算术严格”或“只核定义”。先读源码与read/write边界，在临时副本运行，保留归档旧结果。命令入口均为本仓`knowledge/archive/`，不借另一个桌面仓库补输入。

|已有入口（从archive根解析）|实际输入/输出与覆盖|改变下一步的结论|不能推出什么|
|---|---|---|---|
|`context/propertyb-m6-66-20261029/independent/check.py`|读ROOT_TWO_LOCKS、avoided/V37_THREE、pilot/tightened、pilot/FOUR四JSON；写independent/RESULTS|379必要型、621579完整共同胞向量，注入计数独立于作者概率函数，全部strict|不是自动核原图选择引理/Lean/第二机|
|`context/propertyb-m7-131-20261029/independent/check.py`|读CANDIDATE.json，重建424型及2115296整数向量，写RESULTS|精确完整叶域相等、全部strict|不能把六元外审迁为七元外审|
|`context/propertyb-m8-267-20261029/independent/check.py`|读CERTIFICATE.json，独立构造2094叶与299组件配额，注入计数；写CHECK.json|全量独核、作者值精确相等|不是Lean/整个组件图可实现性分类|
|`context/propertyb-m9-543-20261029/independent/check.py`|读CANDIDATE，自己重建完整树与3450叶，含319一锁/1702双锁路由；写CHECK|没有遗漏失败父型分流，195端点已含|只检查保存成功leaf不能替代这里的树重建|
|`context/propertyb-k12-4664-20261029/independent/check.py`|读COMPLETE/CONDITIONAL/TAIL三JSON，写DOMAIN_CHECK/RESULTS；全664355域/trace，20例Fraction|完整新参数覆盖；tight/端点算术与定向界一致|不是664355概率全表第二实现；输出明确false|
|`context/propertyb35-paper/round01/twentyfour/six_high_one_internal_high/two_triple_small_gate/CHECK_COUNTEREXAMPLE.py`|自造十点输入、32最小横截与全部1024红子集；写同名JSON|signed泛门真反例，所有前提预算均核|不是35边五元H反例|
|`context/propertyb35-paper/round01/middle/a1_rank_component_wedge_budget_20261020/PILOT.cpp`与`VERIFY.py`|C++stdout JSON；Python读PILOT.json，枚举n≤6共33867图，恢复35点76边literal，写VERIFY|component松弛pilot值13074；定义复核；结合解析恒等应停后续同DP|literal不是实际incidence Gram，不能排A1|
|`formal/ReviewAudit33.lean`|构建ThirtyThree.Main后独立原题/传递公理调用|裸Finite/五元/≤33的Bool两色，34下界|不证明旧35候选的完整Lean|
|`formal/ReviewAuditGeneralGrowth12.lean`|构建General.Growth.Twelve后，原积分最大预算/floor/Bool审计|全部k≥12增长定理，Δ≥2；实际类型/axioms|不形式化比较D/E或逐项4664|

具体重放见[案例目录](../../examples/local-branch.md)。Python前三类时间通常为秒级历史实测，Lean重核有8–11GB模块，不把这两类按一个并发上限调度。

## 读现有checker时的实质问题

先看输入从哪来。若文件提供的是layout，独核可重算概率；若文件已提供概率而程序只比较JSON中同一个数字，那只是读回检查。检查domain循环是否自己生成每个必要v/d/e/f/trace，还是仅遍历提交成功记录。查共度/度数/总count边界，trace是否包含empty/singleton；有序对对角是否用ℓ_T(ℓ_T−1)；真实坏对是否以两个方向总权删除；零槽有没有保留。

最后查输出写到哪里。上述脚本多以`Path(__file__).resolve()`定位并覆盖相邻JSON，不能直接跑归档原件。拷完整相关目录及必要输入到任务工作区即可，无须改平台或patch所有旧脚本。

## 发现不一致后如何处置

- 输入缺失：属于搬运/资源问题，定位read_text/import所需原文件并补齐到副本。不要调用新模型重写一份“近似一样”的证书。
- 域不等：保留第一个missing/extra key及其原选择来源，先修覆盖或分流，不从待验表删除不利输入。
- 精确分数不等：保留同一v/count/layout每位置A/B/C/D，对照二项式与下降阶乘；优先看锁mask、固定公共点因子、无放回分母、对角、双方向与零容量。
- 算术仍strict但值不同：辨明两个合法下界是否不同（例如max_R与共同整数最小化）；不得声称“逐项相等”。完整证明可采用更弱但仍strict的一方，记录实际变化。
- strict不足：先定位活跃min与真实结构缺失，再选有界试验；必要松弛失败不是原题反例。
- Lean编译慢或失败：按[Lean实务](lean-practice.md)定位表示/归约/实际连接，不把退出137/134当数学见证。

## 本次已实际重放的能力

实务作者在隔离副本运行m6、signed、component（含重新编译C++）和k12，全部exit0，见[阅读与验证报告](../../../../../../development/propertyb-rebuild/PRACTICE_READING_REPORT.md)。随后未参与写作的agent按技能完成[m7全链试用](../../../../../../development/propertyb-rebuild/forward-use/REPORT.md)：424型及2115296共同整数向量全过，并诊断原证书不能直接迁移到下一边数预算。

最终[搬迁检查](../../../../../../development/propertyb-rebuild/final-portability/REPORT.md)发现m8/m9缺输入JSON，补齐后在搬迁副本真实重算2094/3450型全部通过，约8.862/27.740 CPU秒；CERTIFICATE/CANDIDATE现随archive保存。这里记录本轮实测，不冒用历史耗时。上述复放没有恢复暂停数学工作或运行Lean，也不替代各原证明的数学进口。
