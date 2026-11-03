# S80结构门终态

**后续本地纸面结论：当前S80/两type normal-scaling chart框架整体不能超过1920点。** PROOF第9节证明：假设N25，则存在t2,c40根；其NB2/NB3供需tight。Mixed三步词对固定(a',b')最多四hidden值，故所有非邻NB2须mixed，迫根的两个triangles分别纯A/纯B。同fiber可选择a',b'各避开至多三个normal levels，其五个hidden目标全不可达，矛盾。结合此前N≥26门，N≤24。这个结论未新增任何计算或solver，也不是一般(16,3)上界。

小检查SUPPORTED：S80={z≠0,x−y≠0}四方向每条line为0或4点；保持另一normal零平面的inverse-paired charts给每port恰4邻，不需T_p S=S。1920个pre/post像均16且含direct4，通用76上界纸面成立。CPU0.025032128秒，0大图/solver。

初始controller预算N≤29−2t−c4成立；修正N上界逻辑须用76门另排N27，再以三角整除排N26，目标只剩N25。进一步无需新计算已证N25局部恰t1/c41或t2/c40，故全部非triangle边是vertex-disjoint C4，控制器必须具有(10tri,5C4,5t2)或(14tri,2C4,17t2)的必要inventory。

PROOF.md给完整推导及一般T0/T2矩阵参数，不枚模板。固定三triangle链+六K3的prepare子域若使用这些门，extra2factor必须3+4^5或3^5+4^2；额外cross-cycles和全覆盖仍需处理，未声称可构。

这是新fiber/chart/controller机制，不是已闭旧3750诱导域重命名。未生成2000图、未跑SAT、未扩其它fiber族。所有结果为本地证明/125点校准，未外审或形式化。当前框架已有直接障碍，不需要继续C25控制器求解；其它新规则由root另行判断。
