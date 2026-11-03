# 固定 C8 作用 Z32 的 256 点 Cayley 规则：只读排重门

状态：**未在本次有限本地范围内定位到同一固定族的完整 NO 或实际 UNKNOWN 求解批**。这不是声称历史上无人研究，也不是可行性判断。按授权在只读门停止；未运行词/系数、参数、图或 BFS。

## 冻结的唯一新规则

顶点 `(a,b)∈C8×Z32`，其中 Z32 是循环加法群，非 F32、非 F2^5。RIGHT 乘法

`(a,b)*(c,d)=(a+c mod8, b*3^c+d mod32)`。

四个正生成元为 `(1,b0),(2,b1),(3,b2),(4,b3)`，每个 normal 参数在 Z32 中任意，连同其真实逆生成无向 Cayley 图。逆公式是 `(-c,-3^(-c)*d)`，不得套特征2的加法/XOR逆。目标 n=256、最大度至多8、D<=3；尚无合法实例。

## 已查到而范围不同的历史

1. `research/ddp/m2_coset_tower/nonabelian4_256_search/SCOPE.md` 与 `REPORT.md`：Q64 的四个64点orbit，K4拓扑匹配重数3,3,2,2,3,3，13个自由Q64电压。Q64乘法是 `(x,s)*(y,t)=(x+(-1)^s*y+16*s*t,s xor t)`。旧64起点有界批完成、最佳832坏无序对，结论是该有限程序无命中，不是整族NO。它既非本轮256阶群，也非四个固定phase的全局Cayley连接。
2. 同一 Q64 256 目录下 `nonabelian4_256_capacity/STRUCTURE_SCOPE.md`、`TIGHT_RING_SCOPE.md` 及 central/triangle 后续仍围绕上述4-orbit、D64/Q64参数。出现 Z32 或 mod32 不能把这些范围视为 C8-action3 固定族。
3. 已继承的 `research/ddp/breadth_20261027_wave5/binary_route_chart3/REPORT.md` 是 F2^3 的四个全局线性/单噪声端口图表条件；旧 signed-F2 移植也使用不同加法与矩阵。它们不能排除本轮循环 Z32 群。
4. CM253 的 fourcut 与 fivecut+repair 排除只关实际 C11⋉C23 源的局部改边规则，不涉及新的256点全局Cayley生成。

本轮有限查询覆盖 canonical Wiki experiment 节点、DDP相关报告/recipe/源码关键词及全部含256的已有scope入口。未重导Wiki或读全部历史，未把未匹配关键词当数学排除。

## 可推翻的下一门预测（未执行）

**预测：** 固定四个phase与真实逆后，长度至多3的非回退词按8个终phase分组，每个phase的不同 Z32 四变量端点系数形式数量均至少32，因而最初的路线/系数容量门不会直接关闭该族。

新门应直接用 RIGHT 递推 `L'=3^c*L+d`，正dart normal为对应变量，逆dart为 `-3^(-c)` 倍对应变量；空词只进入phase0。所有系数按模32完整向量去重，不把ring当field，不除以偶数。

若任一phase不足32个形式，即严格排除所有四normal参数选择。若全部达到32，也只说明形式容量必要条件通过，不能推出实际取值覆盖32，更不能推出共享 b0..b3 同时满足8槽。此时再由root基于实际反馈授权下一个有限兼容门，不自动枚32^4或换action/phase/group。

只读与文档准备保守charge **0.8 CPU秒 / 2秒上限**；0新词枚举、0参数、0图、0BFS、0field、0solver、0Lean、0外审。未开启数值进程，等待root另行授权。
