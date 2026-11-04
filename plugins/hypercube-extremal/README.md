# Hypercube extremal research

本插件研究超立方体的禁子图极值问题，现有可执行科学资产来自 Erdős 86 的无四环边密度上界。入口是 [mathrsi-hypercube-extremal](skills/mathrsi-hypercube-extremal/SKILL.md)。它接收具体数学义务，帮助建立共同局部对象、保留根相对朝向、寻找证书，并将精确有限核验接回高维平均证明。

历史最终证书证明 `π_Q(C4) ≤ 23662061277957791/40000000000000000 < 0.59155154`，不是解决 `π_Q(C4)=1/2` 猜想。该常数是原包找到的可行证书，不称 SDP 最优或当前全球纪录。最终六整数Gram块没有Q5 cuts，无Lean；本轮搬迁后实际全域重放成功，范围见 [IMPLEMENTATION](evidence/IMPLEMENTATION.md)。

- [数学工具及原题连接](skills/mathrsi-hypercube-extremal/references/mathematics.md)：共同Q4、同步根作用、整数PSD、覆盖及高维平均。
- [失败及继续研究](skills/mathrsi-hypercube-extremal/references/failures-and-search.md)：工作集与全域分离、best与末行、负定价的含义。
- [复现](skills/mathrsi-hypercube-extremal/references/reproduction.md)：Python标准库+C++17，无需重装优化依赖。
- [原件说明](archive/README.md)及[逐文件库存](archive/INVENTORY.json)：原数学、源码、报告、失败history及证书随仓，生成大系数表的省略逐项登记。

archive只读；历史Goal和路径不是新任务授权。新题在自己的工作区保存输入、证明、wiki和输出。外层维护才更新插件。
