# Payne(6,8) 的49点ovoid／49线spread选择门

核查日：2026-11-01 UTC。对象是当前公开比较中使用的标准 Payne 派生几何 \(D=W(3,7)^P\)，而不是所有未知的抽象 \(GQ(6,8)\) 的分类。

**结论：这个已发表源有49线spread，但不可能有49点ovoid；更强地，其任何partial ovoid至多42点。因此，49×49复制式不是该源给出的公开下界，不能据此停止73及以上的构造。**

## 实际读到的出处

1. Tao Feng、Weicong Li，*The point regular automorphism groups of the Payne derived quadrangle of W(q)*，JCTA 179 (2021), 105384，[arXiv v2 §2.1](https://arxiv.org/html/1908.10659v2#S2.SS1)，PDF第4页（印刷页4）。该节定义派生点为 \(PG(3,q)\setminus P^\perp\)，保留不经P的原totally isotropic lines，另添经P的非isotropic线；阶为 \((q-1,q+1)\)。
2. Michela Ceria、Jan De Beule、Francesco Pavese、Valentino Smaldore，*On large partial ovoids of symplectic and Hermitian polar spaces*，[arXiv:2203.04553 §1及Table 1](https://arxiv.org/html/2203.04553#S1)。其引言明确重述Tallini的奇数q上界 \(q^2-q+1\)。该文参考文献[13]为G. Tallini，*Fibrations through lines in a nonsingular quadric Q4,q of PG(4,q)*，Atti Accad. Peloritana Pericolanti 66 (1988), 127–146 (1989)。本门实际读了上述研究论文的重述，未冒称已取得Tallini原文全文。该上界也与已存Cimráková–Fack2007 Table5的W(7)理论上界43一致。
3. Charles Delorme，*Grands Graphes de Degré et Diamètre Donnés*，EJC6 (1985), 291–302，[§8(a)，印刷p298](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)。该节在原symplectic GQ中构造 \(q^2+1\) 条两两不交、分割所有点的线。

这些来源直接给定义、原空间上界及原spread存在性；以下派生空间结论是本次由它们推出的简短推论，不冒作论文列出的新数值纪录。

## 为什么ovoid不可能

设O是D的partial ovoid。O中任意两点若在原W(3,7)共一条isotropic线，该线不可能经过P，因为O中各点都在 \(P^\perp\) 外；它于是仍是D的一条线，违反partial ovoid条件。因此O在原W中也两两不共线。P与O中任何点都不共isotropic线，所以 \(O\cup\{P\}\) 是原W的partial ovoid。

代入已发表上界：\(|O|+1\le7^2-7+1=43\)，即 \(|O|\le42\)。而GQ(6,8)的full ovoid必须有 \(6\cdot8+1=49\) 点。因此不存在所需49点ovoid，更不可能与49线spread同时存在。这里使用原W的理论上界；没有把“只找到33”当上界，也没有把派生点数343或原点数400混用。

## 为什么spread确实存在

从原W的50线spread取唯一经过P的线L0。L0全在 \(P^\perp\) 内，派生时被删去。其余49条spread线不经P，也不包含于平面 \(P^\perp\)：在这个平面内的isotropic线均经P。每条因此恰删去一个平面交点，留下7个派生点，仍是一条派生线。原spread的分割性质说明这49条线两两不交，覆盖全部 \(7^3=343\) 个派生点。

这是同一个D内的spread存在性推论，不能把对偶Q(4,7)的ovoid搬入D。对偶会交换point／line及ovoid／spread；q为奇数时也没有可随意使用的W自对偶。

## 对后续参数选择的实际影响

沿用已核opposite-GQ公式，D只给degree63／n151263的源。原来暂列的 \(151263+2401(\Delta-63)\)，及最有利的先fill49版本 \(151312+2401(\Delta-63)\)，均需要不存在的49点ovoid才能实现指定矩形49×49规则；不能登记为公开构造下界。

进一步，对**指定的partial-ovoid×spread、每升一度复制一次该中心集**规则，即使宽松赠送最有利49个fill点，并假设42点partial ovoid达到上界，中心数也至多 \(42\cdot49=2058\)。因此该规则的宽松上包络为

\[ U(\Delta)=151312+2058(\Delta-63). \]

U是上包络，不是已发表或本地已实现的下界；没有声称42点对象存在。与当前P33规则的条件延续 \(C(\Delta)=160050+1650(\Delta-64)\) 比较：

| degree | 条件P33点数C | 指定Payne规则上包络U | C−U |
|---:|---:|---:|---:|
| 73 | 174900 | 171892 | 3008 |
| 74 | 176550 | 173950 | 2600 |
| 75 | 178200 | 176008 | 2192 |
| 76 | 179850 | 178066 | 1784 |
| 77 | 181500 | 180124 | 1376 |
| 78 | 183150 | 182182 | 968 |
| 79 | 184800 | 184240 | 560 |
| 80 | 186450 | 186298 | 152 |

故这个具体Payne矩形复制机制不能从73开始阻断P33；至80仍不能。73以上这些P33数值只是用于选择的公式预测，本门没有生产或接受任何新图，也没有授权延伸k。

范围限制：未优化任意非矩形packing、其他诱导复制／嵌套增强，未分类所有抽象GQ(6,8)或未知非经典parent；这些均不能由本门排除。本门也不是73..80全部公开族的重新核查，不认证全球纪录。下一步可依据这项负结论选择一个明确的新参数窗口，再核其其他公开竞争者，不能自动批量生成。

## 执行回执

只使用一次3条primary查询，随后跟读明确论文和既有Delorme来源；无第二批检索。查询为：Payne derived generalized quadrangle odd q no ovoid W(3,q)；Ahrens Szekeres generalized quadrangle ovoid spread no ovoid；partial ovoid W(3,q) odd upper bound q^2-q+1。只使用primary研究论文承重；未用搜索摘要代替上述实际段落。

本地只有8行整数公式计算，CPU及可复现代码见同名JSON和`PAYNE68_CONTINUATION_SCALAR_20261101.py`。0构造／大图读取／BFS／solver／Lean／外部互审／安装／哈希。旧65..72窗口不重验、不改写；所有本地进程终态。
