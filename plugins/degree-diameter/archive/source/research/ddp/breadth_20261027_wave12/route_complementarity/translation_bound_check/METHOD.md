# 独立平移的精确覆盖上界

目的：把“低rank子空间是否互补”变成一个能被具体slot推翻的判断。对固定maps/vectors，在一个base slot收集全部真实长度≤4路线的branch-image线性子空间S_i。把每条路线的仿射平移暂时独立放开，求max|⋃(t_i+S_i)|。此值是两个consistent global offsets所能实现覆盖的上界；若小于16，当前maps/vectors不能仅靠offset补全该slot。若等于16，只说明这个独立放松没有阻断，不能推出存在consistent offsets。

## 可推翻预测

待攻击假说H：保存bestID68的1152失败图，存在至少一个实际坏base slot，使其全部真实≤4 route子空间在独立任意平移后仍不能覆盖F2^4。一个足够简单的正例形状是：全部路线仅给两张法向不同的rank3 hyperplane，且没有其它路线贡献能填剩余4点。实际slot是否具有这种形状尚待source_scout材料，不能由坏对数量或rank直方图猜定。

若具体slot独立上界<16，则必须改变线性maps或branch directions，或者改变route结构；继续只换offset无效。若所有相关slot均可独立盖16，H才被完整反驳；只检查少数通过slot不能证明全体。这两种结果都会改变下一次实验所应检验的参数。

## 有限coset-mask动态规划

Fq^d的向量按base-q整数编号，F2^4即0..15。对每个线性子空间S_i，枚举所有独立平移t，只保留不同coset的位mask（代表t可取最小编号）。线性子空间大小q^r时恰有q^(d−r)个不同cosets。

令D_0={0mask}，递推

    D_i={m OR c : m∈D_(i−1), c为S_i的任一coset mask}。

归纳可知，D_i恰为前i条路线所有独立平移可能产生的覆盖集合，故终态最大popcount就是精确最大union；同一覆盖mask安全去重。F2^4最多65536个mask状态。若某阶段产生全16点mask，已达到绝对上界，可停止并给剩余路线任意平移；否则所有路线必须处理完才可报告严格上界。

代码返回精确最大union、达到它的一组平移代表、缺点集合、每阶段状态数和OR次数，并用原子空间及返回平移重新直接构造union核对见证。见 [translation_cover.py](translation_cover.py)。

特别不能去重相同的S_i：两条方向相同的路线仍是两个独立平移变量，可选该hyperplane的两个互补cosets而盖满16。代码只去重同一路线的等价平移coset及最终coverage状态，保留route multiplicity。

不允许给子空间额外旋转或变换方向。此阶段也不施加两global offsets引起的路线间耦合；因此求解的是一个可证明的上界，不是实际offset可行性。要阻断实际slot必须包含全部≤4路和所有长度、重复路线；只取最短路、只按rank分类或把所有方向的线性span当union，均不正确。

## 手算fixtures与实际结果

每个fixture都在运行前给定手算最大值。运行 [fixtures.py](fixtures.py) 一次，结果见 [FIXTURES.json](FIXTURES.json)，总CPU0.04675秒。

| 输入 | 子空间规模 | 手算/DP精确最大union | 理由 |
|---|---|---:|---|
| F2^4，两同向rank3 | 8,8 | 16 | 两个cosets互补；此例同时检查不误删重复route |
| F2^4，两异向rank3 | 8,8 | 12 | 任意平移均交4点，union=8+8−4 |
| F2^4，共codim2的三不同hyperplanes | 8,8,8 | 16 | F2二维商的3个方向通过同一点即覆盖4点 |
| F3^4，共codim2的三不同hyperplanes | 27,27,27 | 63 | F3二维商三不同方向的直线最多盖7点，乘fiber9 |
| F3^4，共codim2的四不同hyperplanes | 27,27,27,27 | 81 | F3二维商的4个方向通过同一点覆盖9点，乘fiber9 |

这些是合成线性子空间fixtures，尚不声称它们就是原5832成功图或best1152中的某个具体slot。F3对照显示“同为多张hyperplanes”不足以预测互补性，必须看方向、共同商与平移耦合。

方法及fixtures之后已完成唯一实际槽0→10的独立攻击：两张rank3像法向6/9，任意独立平移精确max12，全部16源fiber各至少漏4。具体341条控制walk的完整性重算、branch模拟及结论见[REPORT.md](REPORT.md)、[ACTUAL_SLOT_CHECK.json](ACTUAL_SLOT_CHECK.json)。实际槽分析1，其他1023候选分析0，global或edge-local offset搜索0、图BFS0、新图0；当前任务已完成，不扩展搜索。
