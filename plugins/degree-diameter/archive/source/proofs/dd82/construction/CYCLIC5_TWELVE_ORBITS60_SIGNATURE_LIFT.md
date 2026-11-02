# 实际 20 坏对种子的 C5 签名类提升成功

2026-10-12。输入仍是
[petersen_all_matchings_run/candidate.best.edges](../../../computations/dd82/construction/petersen_all_matchings_run/candidate.best.edges)，
即真实的 60 点、240 边、8 正则、20 坏对图，不是旧 50 坏对种子。
本次找到一个真实的 $5^{12}$ 自同构，逐条验证其保持全部 240 条原边，
并导出该图在一般 354 轨道域中的全部电压。
没有优化、SAT 或重复全图 BFS；原图仍有 20 坏对，不是目标解。

## 实际签名接口与无损端点归约

已有坏对恰涉及端点集合 $E=\{40,\ldots,59\}$。
其余 40 个点按在 $E$ 中的邻点集合分成十个四点类；
十个二元签名恰组成 $E$ 上一个完美匹配。
这些集合和坏对均来自
[endpoint_structure.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/endpoint_structure.json)。
本次从原边表重新读取并核对签名和端点诱导边，坏对与已有 BFS 文件一致。

实际接口结构为：

- 十个四点类内部全部无边；
- 类商连通，每类商度 6，共 30 个非空接口；
- 每个非空 4×4 接口矩阵都恰是置换矩阵。

全部 4×4 矩阵及类商边保存在
[interface_structure.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/interface_structure.json)。

任意真实图自同构都保持坏对集合，故保持 $E$，也保持上述签名类划分。
在 $E$ 上同时保留下列三种关系，仍不丢失任何真实图自同构：
原图诱导边、原图距离超过 2 的坏对、十个签名对。
代码使用关系位掩码作为边颜色，因此即便关系重叠也不会错误合并颜色。

真实 $5^{12}$ 自同构在 $E$ 上必须为 $5^4$，在十个四点类上必须为
$5^2$。后一个必要性来自：一个阶 5 置换若固定某四点类，
就在这个四点类上逐点固定，与全图半正则性矛盾。

## 每个端点候选只需一类的 24 种双射

记非空接口的实际匹配为 $f_{ab}:C_a\to C_b$。
端点自同构决定十个类的置换 $\pi$。若提升在 $C_a$ 上为 $\phi_a$，
则匹配保全严格要求

$$\phi_b f_{ab}=f_{\pi(a)\pi(b)}\phi_a,$$

即

$$\phi_b=f_{\pi(a)\pi(b)}\phi_a f_{ab}^{-1}.$$

因此选定 $C_0$ 到 $C_{\pi(0)}$ 的 24 种可能双射之一后，
连通类商上的所有其他类映射都被唯一传播决定。
遇到两条传播路径给出不同映射就拒绝；若目标类接口不存在也拒绝。
最后仍直接核验整个 60 点置换的 240 条原边像。
这给出候选保全的有限提升方法，而非假设四点类中的顶点有唯一签名。

## 唯一运行的真实结果

源码：
[cyclic5_twelve_orbits60_signature_lift.py](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift.py)。
运行结果：
[result.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/result.json)。
端点候选与实际传播见证：
[endpoint_candidates.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/endpoint_candidates.json)。

三色端点自同构枚举到第二个元素时找到第一个 $5^4$ 候选，
其类作用为 $5^2$。该候选的第一种根类双射即成功提升，
所以只测试了一个根类双射。
**最初提升的全图置换阶为 10，循环型为 $5^4\,10^4$；取其平方，
才得到保存的 $5^{12}$ 自同构。** 两个置换都逐边核验，未把端点阶 5
直接误认为全图阶 5。

得到的阶 5 自同构的十二个循环为：

$$
\begin{aligned}
&(0,35,25,37,27),&&(1,15,28,26,29),\\
&(2,18,23,7,24),&&(3,16,32,9,4),\\
&(5,38,36,39,22),&&(6,10,8,11,31),\\
&(12,30,20,14,13),&&(17,34,21,19,33),\\
&(40,44,43,48,45),&&(41,49,42,46,47),\\
&(50,53,51,54,52),&&(55,58,56,59,57).
\end{aligned}
$$

成功后立即停止端点群枚举。因此结果中的 enumeration_complete=false
仅表示没有继续求完全部自同构，并不影响已经明确验证的存在性见证。
没有超时。内部 CPU 0.017545428 秒、wall 0.023971394 秒；
含 Python 和 NetworkX 导入的进程 CPU 为 0.209209548 秒，
单核、CPU 限制 10 秒。

## 可直接使用的 20 坏对电压种子

以上十二个循环按列出的顺序编号为 $a=0,\ldots,11$，
各循环的五个点按 $t=0,\ldots,4$ 编号；新标签是 $5a+t$。
所有产物位于
[signature_lift_run/seed20](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/seed20/)：

- [automorphism.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/seed20/automorphism.json)：完整原标签置换、十二循环、原到新标签映射及逐 240 边验证。
- [seed.edges](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/seed20/seed.edges)、
  [seed.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/seed20/seed.json)：真实完整图的重标号边表。
- [palette.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/seed20/palette.json)：全部 354 个不交边轨道，其中恰选中 48 个；各轨道在原标签中的五条边均保留，并严格重建原来的 240 条边。
- [voltages.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/seed20/voltages.json)：完整 12×12 位移集合、每纤维度 8、全部缺失位移和坏对。

直接计算位移的一步及二步和集，只发现

$$
(a,b)=(8,11)\ \text{缺位移 }2,4;\qquad
(a,b)=(9,10)\ \text{缺位移 }2,4.
$$

每个缺位移对应五个坏对，合计 20 个。该精确电压覆盖结果与原有独立
全图 BFS 的坏对集合逐对相等；本次没有重复调用 BFS 检查器。
这把实际 20 坏对种子放入了允许全部内部/外部边轨道变化的完整 C5 参数域，
并保留了所有缺口，供新的有界构造实验直接使用。

后续直接从选中轨道读出的商矩阵为 M=2I+A(K6,6)，两侧分别为
{0,2,5,7,9,10} 和 {1,3,4,6,8,11}。该固定商已被
[纯数学障碍](CYCLIC5_K66_QUOTIENT_EXCLUSION.md) 排除；允许改变内部轨道的
[一次完整切换邻域实验](CYCLIC5_TWELVE_ORBITS60_SWITCH20_RESULT.md) 没有严格改善。
它仍只是一个 20 坏对失败种子，实际 C5 提升并不使其成为直径二图。
