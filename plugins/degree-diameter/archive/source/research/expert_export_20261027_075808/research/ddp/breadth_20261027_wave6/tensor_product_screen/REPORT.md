# Categorical / direct / tensor products：保存因子的完整有限筛

结论：**两因子实际有五项数值越线组合，全部被同长度walk障碍排除；附加的三因子两项也失败。** D4/D5没有数值越线组合。没有生成产品图、运行BFS或做产品修补，无新下界。范围是下表保存/经典因子的plain tensor products，不是任意未知更大因子的一般不可能性结论。

历史限定检索未发现同一tensor筛。旧 [graph_products/REPORT.md](../../breadth_20261027/graph_products/REPORT.md) 只排Cartesian/strong，并明确将tensor/direct保留开放；[Kronecker文献摘录](../../SOURCE_UPDATE_20261026_22.md) 是degree18的极性乘积，不是本轮筛选，未重跑这些旧工作。

## 来源和全部因子数值

采用2026-10-26保存基线；degree4–6各D3/4/5值与 [registry/cases.json](../../../../context/DD_PORTFOLIO_START_20261026/registry/cases.json) 一致。cubic20/38/70从维护者原始说明的本地缓存逐项核对：[D3](../../m1_sources/desc_g3.html)、[D4](../../m1_sources/desc_g4.html)、[D5](../../m1_degree5_transfer/desc_g5_source.html)。对应维护者页面为 [Comellas D3](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)、[D4](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html)、[D5](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html)。这里使用历史保存来源，不声称重新刷新当前公开纪录。

| 因子degree cap | D3阶数 | D4阶数 | D5阶数 |
|---:|---:|---:|---:|
| 2：经典C_(2D+1) | 7 | 9 | 11 |
| 3 | 20 | 38 | 70 |
| 4 | 41 | 104 | 364 |
| 5 | 72 | 252 | 650 |
| 6 | 120 | 441 | 1518 |

degree2的最大可能阶2D+1来自普通Moore球计数，由该奇圈达到。其余行是保存的已知因子阶数，不一概当作所有该degree/diameter图的上界。上述各图阶数都超过其degree下D−1的Moore界，所以实际直径确为所列D，而非可能更小的cap。

## 参数范围和乘积阶数表

Tensor产品在且仅在每个坐标同时沿因子边移动时相邻。因此n为因子阶数之积，最大度不超过因子degree caps之积；**直径不使用max公式**。目标D的产品必有每个因子直径≤D。

两因子degree2–6且乘积≤12只有七类；结合律下三个因子仅再有(2,2,2)、(2,2,3)，四个因子因最小degree乘积16而超限。表中列的是阶数乘积，不承诺产品达到列标题的直径。

| 因子degree组合 | 产品degree cap | 取D3因子的阶数积 | 取D4因子的阶数积 | 取D5因子的阶数积 |
|---|---:|---:|---:|---:|
| 2×2 | 4 | 49 | 81 | 121 |
| 2×3 | 6 | 140 | 342 | 770 |
| 2×4 | 8 | 287 | 936 | 4004 |
| 2×5 | 10 | 504 | 2268 | 7150 |
| 2×6 | 12 | 840 | 3969 | 16698 |
| 3×3 | 9 | 400 | 1444 | 4900 |
| 3×4 | 12 | 820 | 3952 | 25480 |
| 2×2×2，附加 | 8 | 343 | 729 | 1331 |
| 2×2×3，附加 | 12 | 980 | 3078 | 8470 |

程序还枚举了因子D可以不同的全部组合：两因子共90个参数行、三因子40行；按目标D3/4/5分为9、36、85行。每行均与全部适用的保存degree-cap目标比较，覆盖27个目标cell，没有凭主表单调性省略较大cap。

更低直径因子不会产生漏项：D≤2因子的阶数至多Moore(d,2)=1+d²。将每一类degree组合中的任一因子替换为这个乐观上界，D3阶数积都已不超过目标基线；D4/D5即使全部使用表中最大已知因子也未过线。具体上界及全部混合参数在 [RESULTS.json](RESULTS.json)。

## 全部数值越线项及短见证

| 数值候选 | 名义degree cap | 阶数积 | 保存D3基线 | 阻碍 |
|---|---:|---:|---:|---|
| C7×C7 | 4 | 49 | 41 | C7无闭三步walk |
| C7×cubic20 | 6 | 140 | 120 | C7无闭三步walk |
| C7×quartic41 | 8 | 287 | 253 | C7无闭三步walk |
| C7×degree6源120 | 12 | 840 | 810 | C7无闭三步walk |
| cubic20×quartic41 | 12 | 820 | 810 | cubic20无三角 |
| C7³，附加 | 8 | 343 | 253 | 投影到前两个C7已失败 |
| C7²×cubic20，附加 | 12 | 980 | 810 | 投影到前两个C7已失败 |

证明只需如下同长度条件。产品中一条长度k的walk恰好对应每个因子中同为长度k的walk；反向也可按步组合。所以若一个因子有距离三的u,v，为使产品D≤3，另一因子每个固定点w都必须有闭三步walk，处理产品端点(w,u)、(w,v)。长度0/1/2已被距离三坐标禁止，只剩k=3。简单无向图的闭三步walk恰表示w位于三角形上。

C7没有三角。每个与它配对的所列因子都有距离三点对：其阶数分别超过degree2/3/4/6的Moore(D2)值5/10/17/37。因此四个含C7的两因子候选均失败；三因子同样沿两个坐标投影继承失败。

最后，若最大度三的D3图有一个三角，从三角顶点作半径三球：第一层至多3点；三角内的一条邻层边消耗两个向外位置，第二层至多4点；第三层至多8点。故全图至多1+3+4+8=16点，与20点矛盾。于是任意20点subcubic D3源均无三角。quartic41有距离三点对，故820阶数积的产品同样不能D≤3。无需读取具体20/41边表或生成820点失败图。

## 终态和边界

[screen.py](screen.py)在单worker、10 CPU秒硬限下完成纯整数筛；[terminal.json](terminal.json)为 `COMPLETE_SAVED_FACTOR_TENSOR_SCREEN_ALL_NUMERICAL_EXCEEDERS_BLOCKED`。无产品图、无BFS、无solver、无随机seed；所有七个数值项均保存了对应的两坐标纸面见证。

结论覆盖保存的degree2–6、D3/4/5因子阶数及上述plain tensor组成，包括低直径因子的乐观补查；不覆盖未来更大因子、degree1因子、加删/重连产品边或其他修改机制。没有称任意因子tensor产品都不可能改进。这个已知源有限筛在此收束，不开启产品修补。
