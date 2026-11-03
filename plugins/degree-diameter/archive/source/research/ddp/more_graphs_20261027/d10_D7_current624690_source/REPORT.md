# (10,7) 624690 的真实 metacyclic 源：备用配方恢复

仅恢复小型公开配方及必要算术；不下载 3,123,450 条大边表，不重验已知图，不搜索新 embedding、生成元或候选图。唯一账本按 624690/6941 精确检索，未发现此源或其迁移已执行的条目。当前优先级仍是已在跑的 (8,7) 有限对照。

原作者 [construction.json](https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg10/dia7/construction.json) 与 [README](https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg10/dia7/README.md) 给出
G=Z6941⋊316 C90，6941=11·631。记 (i,j)=x^i y^j，则

(i,j)(k,l)=(i+316^j k mod6941, j+l mod90)。

左乘 (a,b) 把 (i,j) 送到 (a+316^b i,b+j)；图边按右乘 g→g s±1 定义，顶点标签为 i+6941j。逆为 (-316^-j i,-j)。五个正生成元的 (normal,phase) 是

(35,35)，(509,5)，(4285,37)，(6911,49)，(3639,34)。

公开源报告 degree10、D7、n624690。本轮没有 literal header/完整度分布或旧 BFS，不能把上述来源元数据说成本地完整图复验。

## 作用 kernel 与可迁移部分

316 在模11、模631、模6941 上的阶分别为10、45、90。所以整体 C90 作用忠实，但两 CRT 分量分别有9阶、2阶 kernel。其 phase45 元素满足 r45=3156；(i,45) 为 involution 的解数是 gcd(1+r45,6941)=11，与作者刻意使用小 involution 类的说明相符。

若直接改成 prime field 并保留忠实90阶作用，最小 p>6941 且 90|(p−1) 的素数是7561；前六个候选7021、7111、7201、7291、7381、7471均为合数，分解保存在 ARITHMETIC.json。明确假设目标为

G'=F7561⋊C90，action exactorder90，n680490，目标(10,7)。

这里只选群阶与作用条件，未选择具体 embedding 或 offset。这个 faithful field 的 phase45 是反演，involution 类会有7561个元素，不能保留原源的11个 involution 结构。若反而保持模11分量，并把631分量替换成同为45阶作用的下一素数811，则阶跳至802890，更大。两种迁移均不能仅靠 group order 或 raw word 数宣称保留覆盖。

## 精确规范化接口

源中 phase37 与90互素，故令新 phase j'=73j，新 action r'=316^37=5304。先以 normal translation z=5968 共轭，把该 phase1 生成元 normal 置零，再乘单位2820^-1，把 phase5 生成元 normal 置一。排序后的等价源生成元为

(0,1)，(1,5)，(2847,35)，(3471,52)，(3355,67)。

3471 在模6941下等于1/2。此步骤只给可复用的 gauge；尚未建立其余两个非平凡 offset 的低系数跨 field 公式，不能把这些整数拟合成原作者的一般 cyclotomic 定理。

## 继续还是降级

建议降为备用 source。上述最小忠实 field 目标比源大8.93%，当前 (8,7) 的6211/6073仅大2.27%；本源同时还改变关键 CRT/involution 结构，尚无更小、更可信的跃迁优势。先等当前 degree8 完整有限对照，不因本源尚未试过就另开90阶 embedding 或自由 offset 批次。

本轮终态是 SOURCE_RECIPE_RECOVERED_ARITHMETIC_ONLY；新图、图 BFS、solver、参数批次均为零。来源和逐项算术见 SOURCE_FACTS.json、ARITHMETIC.json 及可复现小脚本 source_arithmetic.py。
