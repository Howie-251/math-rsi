# 固定72控制图：26必需词留1024候选，全部零offset图仍失败

结论：全部2419200个规范输入中，恰1024个满足固定72点控制图真正必需的26种唯一四步词全部rank4，八个companion各128个。随后经明确授权，对这1024个固定global-label、offset全零的1152点图逐一计算完整R4：全部失败，最好仍缺12384个无序点对。因此关闭的是**固定72标签控制图、四个global线性maps/vectors、offset0**的完整模型；非零offset及逐边独立映射仍开放。没有新下界，没有SLS、新seed或offset优化。

## 与旧通用108词空间的实质区别

已检索唯一方法账本的 `ddp-wave3-binary-route-chart4`。旧结论要求全部108个约化四词均rank4，允许先用bbbb循环性淘汰。此处只要求固定72控制图中真正唯一长度≤4路线对应的26词；两种要求不同，旧排除不能直接外推。

本次标签逆为[3,2,1,0]，0=a、3=a⁻¹、1=b、2=b⁻¹。26词只有aaaa和dddd两个纯重复词，**bbbb和cccc均不属于必需词**。因此代码没有bbbb循环预筛，没有要求B及b1构成循环基，也没有测试其余82个非必需词。

## 控制图必需词的独立恢复

从 `wave5/mizuno_d4_source/controller72.labels.json` 重新枚举每根长度0至4的全部walk，含立即回退。恰468个有序控制点对的长度计数为[0,0,0,0,1]，即只有一条四步walk且无更短路线；取其label序列恰26种。所有词与逆反向词均在集合中，且都约化。本次完整slot/word集合与root保存的 `wave10/binary1152_edge_local/unique4_controller_slots.json` 一致。

每个这样的slot只能沿这一条控制walk到达其16点fiber。无论选择什么affine offsets，该walk端点集都是一个仿射子空间，方向由四个branch参数的四列生成。因此其rank必须等于四。此要求对所有global-label矩阵/向量都是必要条件；不假定多路子空间并的其余覆盖成立。

## 完整规范空间及反向约定

一步关系为 `x -> A_t*x + lambda*b_t + offset`，lambda∈F2。反向标签矩阵为A_t⁻¹、branch向量为A_t⁻¹b_t；offset按反向边重新变换，且不影响四列rank。

aaaa满秩等价于循环基 `[b0,A0*b0,A0²*b0,A0³*b0]` 独立。取此为共同线性坐标基，则b0=e0，A0的四列为 `[e1,e2,e3,c]`，可逆性要求c的e0系数为一，恰八个companion `[2,4,8,1+2k]`，k=0,…,7。时间反序的可控性列只作列置换，不改变rank。

在同一次换基下，B=A1仍遍历全部GL4(2)的20160项，b1遍历全部15个非零向量。四标签maps严格依序为 `[A,B,Binv,Ainv]`，branch向量依序为 `[1,b1,Binv*b1,Ainv*1]`。没有再删减B轨道或向量，因此规范空间完整为8×20160×15=2419200。

对词t0t1t2t3，实际计算四列

`[A_t3 A_t2 A_t1 b_t0, A_t3 A_t2 b_t1, A_t3 b_t2, b_t3]`。

二进制四位整数表示向量，矩阵四列各用同样整数表示；运算为F2异或消元，不使用实数秩。GL4由全部65536个四列编码按真实rank筛得，逆作用表由运行时实际映射生成。

## 枚举终态与阻断统计

完整examined=2419200，survivors=1024；八个companion的survivor数均128。正式rank测试6822848次，按26词字典序遇首失败即停止该输入；首失败数与1024通过数之和恰2419200。没有遇到软/硬时限。

`search_result.json`/`terminal.json`保存全部26词首失败计数。实际首失败非零词共有12种：0100、0111、0131、1000、1011、1100、1101、1110、1131、1311、2000、2220。这里的“首失败”依词序，不是最小矛盾集或一般纸面分类证明。

`first_diagnostic_candidate.json`是第一个正式规范输入的全部26词四列和rank，不经bbbb筛选；`first_survivor.json`是首个通过者，保存四个矩阵、四向量、全部26项四列与rank。最多保存这一个survivor，没有保存或展开1024张图。首诊断和首通过者的数据导出额外计算不包含在正式rank_tests计数内，均包含在native CPU内。

## 覆盖、未闭义务与成本

第一阶段1024个结果只说明唯一四路slot的16点fiber能完整覆盖。其他控制点对仍可能需要多条低rank affine子空间的并；self及短路修补没有从原F3定理自动移植。第一阶段没有关闭global-label族，第二阶段只关闭了其中offset0范围，均不能关闭144条边独立映射的edge-local族。

若26词必要筛为零，唯一四路rank障碍会同时排除global-label矩阵/向量加任意逆一致offset（甚至offset逐边变化）；实际不是零，所以没有作这项更广排除。后续完整零offset检查是另行明确授权的下一精确步骤，并非恢复wave10 seed。

第一阶段native CPU约0.166861秒，含编译及driver总CPU1.504111秒；词恢复另0.008694秒。单worker，native软18/硬20CPU秒未触及，complete=true。该阶段没有图或BFS。root已用全部16个branch取值逐词模拟独立核对首诊断及首生存者的26项rank，并复用wave10的468个唯一slot独立枚举，全部MATCH，见 `root_rank_check.json`。

## 后续精确步骤：完整1024个offset0图

第一阶段只保存了首个通过者。因此按root明确授权，允许且仅做一次把相同2419200枚举接上collector，重新得到同样1024项；没有换criterion、规范空间或增加新参数。随后完整参数已持久化为 `all_passers.json` 和 `all_passers.txt`，全部1024分数保存为 `all_passers_scores.json`。native后续若已有cache就直接读取，不再枚举；driver遇完成终态也拒绝自动重跑。

每个passer使用同一组global maps和vectors，所有offset固定零。直接构建全部1152点八正则图，逐项计算完整 `R4=(I OR A OR A²)²`。首个真正finalist另从全部1152根枚举5392512条长度0至4的walk，逐bit与R4 MATCH，正式评分复用；仅这一次校准，无producer BFS。

1024/1024项完成，hits=0，最少坏对12384、最佳ID68。同fiber坏对为0，全部12384缺项跨fiber；这只描述保存best。`coverage_result.json`/`coverage_terminal.json`保存完整终态，`first_finalist_calibration.json`保存首图校准，`coverage_production.log`保留日志。

`best.edges` 带头1152/4608，保存唯一best；`best_parameters.json`给四global矩阵列、branch向量、零offset、逆标签和完整controller邻接，可直接重建。生产检查简单、全部八度、邻接对称及4608边。root已从best明确边表完成唯一全1152源BFS，确认simple、connected、8regular、实际D5、12384个>4无序对；全部144条source-label关系、global矩阵/向量逆及4608边精确匹配，见 `best.independent_check.json`。

该步骤native CPU约0.430204秒，其中重新收集并持久化1024项约0.163142秒；含编译/driver总CPU2.151637秒。native18软/20硬限均未触及，单worker。全部预定项完成即停，SLS提案0、新seed0、offset改动0；未因最少坏对下降到12384而自动延长。

完整模型排除来自两层证据：其余2418176个规范输入已经违反唯一四路的必要rank；剩余1024个规范输入在offset0的全图R4均有缺口。共同线性换基只重命名fiber点，故规范化不丢失任何offset0 global-label图。对任意非零offset（global或edge-local）并未做完整覆盖检查，不能把这项排除外推过去。

root的rank/word与最终best两项独立检查均已完成，两阶段terminal的pending均清空。本批终态，无在途或待验项，不追加offset或搜索。
