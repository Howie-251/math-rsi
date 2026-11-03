# 3750 点 20 正则直径 3 图

日期：2026-10-29。同一 Degree/Diameter 项目中的新完整构造实例。

**实际图已独立验收：3750 点、37500 条边、简单、连通、每点度 20，直径恰为 3。** 全部3750根通过，没有距离超过3的点对。固定参数公式图的3750点、最大度≤20及直径恰3，也已在Lean中完成证明。

[完整边表](graph_d20_D3_n3750.edges) · [全部字面参数](PARAMETERS.json) · [独立全源验收](INDEPENDENT_VALIDATION.json) · [生成器](generate.py) · [最终Lean核对](PROOF_AUDIT.md)。

3750比本次已核对的2026年9月公开下界2783多967点；当前全球纪录尚未确认。本次有界阅读没有取得CombinatoricsWiki最新条目，不能把访问缺口当作新颖性证明，也不声称已经公开采用。比较来源是[Rishabh Rajiv原始资料](https://zenodo.org/records/23052995)，相关[2026-10-22版论文](https://arxiv.org/html/2608.27253)的自身构造仍列2600。详细阅读范围在baseline_check/。

另对原控制器作者的当前仓库做了[定向查重](author_repo_targeted_check/REPORT.md)，所读F4证明未见本3750实例。作者本来已有任q的通用定义及其他F5高维实例，故不把“使用F5”本身作为新贡献；本次查重也不构成最新全球纪录确认。

## 顶点与全部边

顶点为(a,x)，a是PARAMETERS.json中30点四正则控制器的顶点，x∈F5³。编码为a×125+x0+5x1+25x2。

四方向ℓ0=e0、ℓ1=e1、ℓ2=e2、ℓ3=(1,1,1)，反向port为(1,0,3,2)。若控制器port p从a到b，则连接全部五个目标：

    (a,x) — (b,T_p x+t ℓ_inv(p))，t∈F5。

T0=[[0,2,4],[1,0,0],[0,1,3]]；T1=[[0,1,0],[4,0,3],[2,0,1]]；
T2=[[2,3,1],[0,4,1],[1,0,1]]；T3=[[2,1,2],[3,3,4],[3,4,4]]，全部模5。

真逆T_inv(p)=T_p^{-1}和T_pℓ_p=ℓ_inv(p)保证无向；四个目标控制器互异、每方向五个目标互异，保证简单和每点恰20邻点。完整控制器、矩阵、方向和编码均已在PARAMETERS.json中给出，不需原项目或额外Python包。

## 三步覆盖的原因

任三步非回退控制器路线的终点噪声秩，可化为中央弧的三列rank[T_pℓ_i,ℓ_inv(p),ℓ_j]。全部36种转向实际满秩3，所以每条这样的路线覆盖整个125点纤维。实际控制器所有780个非邻或相同有序对均有NB3路线，已从邻接独立枚举1080条路线核对。

剩余120个相邻有序对由前/后回退的六个平面覆盖。它们同中心、共享一条线，商空间中对应PG(1,5)全部六个方向，故并集为6(25−5)+5=125。四个port、全部125个源坐标的500项平移检验已完成。

上述生成论证之外，INDEPENDENT_VALIDATION.json记录了从实际边表重建图的全源检查。最大度20、直径至多2的Moore界为1+20+20×19=401，小于3750，也说明直径不能降到2。

## 独立距离验收

|距离|有序点对数|无序不同点对数|
|---|---:|---:|
|0|3750|不计|
|1|75000|37500|
|2|1177500|588750|
|3|12806250|6403125|

验证器仅读取本包边表，不读生产程序的矩阵、映射或闭球缓存；所有3750根通过，CPU约1.825秒。逐根层计数、运行命令和实际预算保存在JSON中。没有重复检查旧103图。

## 离线复现

本目录所需文件：generate.py、PARAMETERS.json、graph_d20_D3_n3750.edges、independent_verify.py和验证JSON。均使用Python标准库。

```bash
python generate.py --parameters PARAMETERS.json --output rebuilt.edges
python generate.py --parameters PARAMETERS.json --compare graph_d20_D3_n3750.edges --dry-run
python independent_verify.py graph_d20_D3_n3750.edges --output verify.json
```

第二条命令只核对生成边集一致性，不重新做BFS。输出边表首行是n m，随后每行u v为一条无向边。独立检查器的实际调用命令见INDEPENDENT_VALIDATION.json及其源码参数说明。

## 署名与验收边界

30控制器、四port框架及原F4/1920构造来自[Ryosuke Mizuno原证明](https://raw.githubusercontent.com/rmizuno42/ddp/main/results/degree16-diameter3/certificate/PROOF_ja.md)。本项目变更是具体F5互补方向矩阵、完整3750点图及其生成/验证；不主张首创一般仿射提升、平面pencil或经典Moore界。

本图的数学合法性、与已读公开来源的改进、当前全球纪录、跨模型审阅和Lean分别记账。旧103个不同阶数图及三个已确认公开主表改进格保留；本图另列一项已验收、最新纪录状态待定的参数成果。

一次实际Gemini3.8Flash/high审阅接受完整字面图及独验，结论为ACCEPT_WITH_QUALIFICATIONS：[审阅处置](reviews/F5_FULL_GRAPH_REVIEW_DISPOSITION.md)。该审阅只读材料、未执行代码，其“Lean未完”是最终编译前的历史状态。

此后Lean已实际完成无前提定理concrete_order_degree_and_D3，给出Fin3750阶数、所有顶点degree≤20、所有点对存在长度≤3的真实walk；另以0→6的一/两步否证证明不能≤2。900个控制器单元、4500 NB噪声decoder、500相邻位移decoder在kernel核验，不枚3750²完整点对。最终声明仅依赖标准三公理，无sorry、新公理或native_decide。fresh定义/量词/参数对齐审阅PASS；[实际编译结果](FINAL_COMPILE_RESULT.json)与[证明核对](PROOF_AUDIT.md)齐备。

这是1个已完成的具体公式图Lean见证，旧103图未因此形式化。Goal允许确定性生成器+字面参数，已直接核对Lean四组字面表和编码与生成器相同；不额外要求形式化文本parser才承认该见证。未声称Lean已解析磁盘边表、证明所有度数恰20或输出mathlib字面ediam API等式，详见[形式化状态](formal/FORMAL_BINDING_PLAN.md)。包内全部已编译Lean源码需锁定Lean4.24/mathlib环境；Python生成和独立验证不需这些依赖。
