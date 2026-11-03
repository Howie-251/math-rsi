# AG(2,4) rainbow trade的80旗标控制器：八个固定方案终态

结论：构造逻辑成立，前八个lex canonical rainbow方案均已实际生成80点、160边、简单四正则控制器；其self、邻接及二步点对都满足已有宽chart的覆盖条件，但**八图均未覆盖全部80²个有序点对**。最佳宽规则缺784个有序对。root随后对最佳图唯一一次全80源普通BFS得到D=5、208个距离大于四的无序对，因此该最佳控制图的6480点提升必有D≥5，不生成大图。其他七图未作root普通BFS，不把它们全部写成D5。

这是同一degree12/D4线性提升机制下的全局几何控制器变体；没有继续小base或Cayley限制，也没有据失败追加parallel class、exact-cover解、B次序或orientation。

## 真正的F4几何与rainbow exact cover

使用F4=F2[α]/(α²+α+1)，加法为bitxor，乘法按二进制多项式约去x²+x+1；不是整数mod4。点编码p=4x+y，x,y∈F4。保留16条非vertical旧线y=m x+c，其ID为4m+c，m,c∈F4；删掉vertical的四条线。

枚举16点上的全部无向简单C4共5460个，只保留四条边均非vertical、且原旧line ID两两不同的936个cycle。每个row覆盖四个point columns和四个line-colour columns；32-column exact cover选四row，得到四个不交新块与其A循环，并恰用遍16条保留旧线的颜色。

DFS依最小未覆盖point分支，row按无向C4的最小旋转/反转表示排序，因此得到规范方案集的lex前缀；在第238个search node取满前八解，CPU约0.004秒，没有枚举全部exact covers。完整field/line编码、八解及统计在 [exact_cover.json](exact_cover.json)。首解为

    (0,4,1,5)，(2,6,3,7)，(8,14,9,15)，(10,12,11,13)。

四圈边颜色依次为 `(0,5,1,4)`、`(2,7,3,6)`、`(11,12,10,13)`、`(9,14,8,15)`，全体恰为0–15。

## 旗标规则及已成立的局部覆盖保证

每点属于四条保留旧线与一个新块，共80个flag(p,L)。每个块的四flag构成A±的C4；每点的五flag构成B±的C5。取标签A/B/C/D=0/1/2/3，逆映射[3,2,1,0]，即A⁻¹=D、B⁻¹=C。

每条旧线L唯一的selected edge(p,q)固定为其A循环的opposite pair，另两点为另一opposite pair，采用规范方向。每点p的两条selected edge颜色L1,L2不同，且过同点的不同旧线方向不同。固定其B五圈，让新块N_p与L1、L2相邻，中间两旧线只取两种无向次序中lex较小者，最后定规范方向。没有另做B次序或方向优化。

几何保证如下。

- 对selected edge(p,q)所属旧线L，p/q所在同一新块为N。L的另一个点r给出简单五圈 `(p,N)—(q,N)—(q,L)—(r,L)—(p,L)—(p,N)`。
- 两个r选择覆盖L全部四条old A边；每条new A边本身也是某条selected edge。因此全部80条A边都在这样的五圈上。去掉任一A边，替代四步恰含2A类和2B类。
- B边沿自身C5的另一方向有纯B类四步替代。
- source72的8个坏四步词全是A/B类别3+1，其余100个RG4满秩；上述两类四步替代均为good word。source的同fiber修补和12个R2 pencil只需逆一致标签，继续适用。

实际生成时，程序保存32个五圈见证，逐个检查A边四步替代确为good且2+2；并对全部八图逐根核对self、邻接、两次邻居步可达点均已进入宽覆盖。局部保证确实兑现；仍未保证其余较远controller pairs。来源为 [mizuno_d4_source/proof_ja.md](../mizuno_d4_source/proof_ja.md)。

## 全80根的实际宽规则评分

评分集合为I∪12个R2 pencil词∪100个RG4词；I和R2使用作者已验证的fiber修补，不把长度零/二的单一路线误算成单条满秩矩阵。逐80根计算controller端点并集。

| exact-cover解 | 宽规则缺失有序对 | 单根最少覆盖点 |
|---:|---:|---:|
| 0 | 784 | 69 |
| 1 | 1104 | 63 |
| 2 | 1162 | 60 |
| 3 | 1158 | 59 |
| 4 | 1158 | 60 |
| 5 | 1096 | 61 |
| 6 | 1154 | 60 |
| 7 | 1158 | 59 |

[controller_0.json](controller_0.json)至controller_7.json保存各图完整flags、blocks、A/B循环、带标签邻接、边表、五圈见证及缺失对。最好图另存为 [best.json](best.json)、[best.edges](best.edges)、[best.labels.json](best.labels.json)。

root只从best.edges重建邻接进行一次普通全80源BFS，确认简单、连通、四正则、D5，208个无序对距离五；证据在 [best.independent_check.json](best.independent_check.json)，CPU约0.00314秒。宽规则的784个有序缺项与普通BFS的208个无序坏对是不同对象。由于提升路径投影到controller路径，best控制器的D5已阻止对应提升达到D4；未生成6480点图。

本次producer CPU约0.040秒、墙钟约0.577秒，单worker、30 CPU秒硬限未触及；没有producer BFS，root只做上述最佳图的一次全源核查。准确终态及八项评分在 [terminal.json](terminal.json)，可复现程序为 [run.py](run.py)。

范围只限固定vertical parallel class、lex前八rainbow exact covers和每解固定的A/B规则。没有排除全部rainbow trade、全部80点几何控制器或其他label方向，也没有把其余七图提升为D5不存在性结论。本有限任务在此收束，无新下界。
