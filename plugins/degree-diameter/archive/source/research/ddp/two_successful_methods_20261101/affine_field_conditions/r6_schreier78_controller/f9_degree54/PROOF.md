# 完整F9/C78图：56862点、54正则、直径恰3

本文件证明 `PARAMETERS.json` 与 `generate.cpp` 的具体图，完整字面边表为 `graph_d54_D3_n56862.edges`。生产已实际PASS：56862点、1535274边、全部54正则。这里没有运行BFS或Lean；fresh独验及最终审阅分别记录。

## 1. 来源与具体定义

控制器是父目录已实际PASS的唯一C78：三base×Z26，参数 `(α0,α1,α2,σ,τ)=(2,6,17,5,10)`，self shift13，ports `[a+,a−,b+,b−,s,t]`，inverse ports `[1,0,3,2,4,5]`。完整78×6邻表在本目录 `PARAMETERS.json`，其234边及全部234类三port证据在父目录。

三base `(a,b,s)` 的一般Schreier框架及零电压b三角形继承Bhakar作者仓库 f4t4nt/degree-diameter-graphs，在 `../../../f7_c60_d35/PARAMETERS.json` 有准确来源；本次增量为固定m26的新参数、明确第六匹配t、实际C78词证书及其F9完整图绑定。不称本次发明一般Schreier lift或仿射提升思想。

取 `F9=F3[w]/(w²+1)`。code `a+3b` 表示 `a+bw`，其中a,b取0、1、2，故

`(a+bw)(c+dw)=(ac−bd)+(ad+bc)w`。

V=F9³，纤维label=`x0+9x1+81x2`。六方向依ports0..5为

`ell0=(0,0,1), ell1=(1,0,0), ell2=(1,1,1), ell3=(1,2,1), ell4=(1,3,2), ell5=(1,6,2)`。

它们与所有实际矩阵直接继承 `../../r6_f9_projective_halves/cross_port_extension/PARAMETERS.json` 中已PASS的固定六方向局部接口。实际仅用八张chart，按本目录编号0..7为：

| index | chart | inverse |
|---|---|---|
| 0 | cross_0_1_forward | 1 |
| 1 | cross_0_1_reverse | 0 |
| 2 | cross_2_3_forward | 3 |
| 3 | cross_2_3_reverse | 2 |
| 4 | self_4_plus | 5 |
| 5 | self_4_minus | 4 |
| 6 | self_5_plus | 7 |
| 7 | self_5_minus | 6 |

八张实际3×3矩阵、其source／target ports与完整78×6 dart-chart表均保存在本目录 `PARAMETERS.json`，`actual_parameters.hpp` 是生产程序读取的精确导出。

对controller dart `u,p→v,q`，q=`inverse_ports[p]`。p<q取canonical跨port正向；p>q取对应真逆；p=q时，u<v取self正向，否则取self反向。因此a±使用chart0／1、b±使用chart2／3，s使用chart4／5、t使用chart6／7。记其矩阵为T_e。

图顶点为 `(u,x)∈C78×V`，label=`729u+x0+9x1+81x2`。精确边关系为

`(u,x) ~ (v,T_e x+t ell_q), t∈F9`。

## 2. 无向、简单、54正则与完整边表

对每实际dart，反向选择的chart为T_e的真逆，且 `T_e ell_p=ell_q`。正向 `y=T_e x+t ell_q` 后，反向使用噪声−t得到x，所以两dart定义同一无向关系。

controller简单6正则，故其六个目标层互异且均异于u。每目标层中ell_q非零，九个噪声参数给九个不同邻点。因此新图简单54正则，阶数78·729=56862，边数56862·54/2=1535274。

实际生产逐一生成全部56862点的54邻点，检查标签范围、无自环、无重邻；全部3070548有向邻接计数吻合。另逐一核验八chart×729坐标×9噪声的52488个真逆等式，及468个controller dart的端口／反向chart绑定。

输出按source label递增、每点54邻点先排序，仅存source<target。故完整边表无header，每行 `a b`、a<b，全部1535274行全局lex排序且无重复。程序从输出的每条边同时增加两端literal degree，全部56862点最终均为54。

## 3. 实际八chart的共同局部证书

`ACTUAL_LOCAL_CHART_CERTIFICATE.json` 保存本次实际用到的全部八张chart检查。每张chart均验证两侧矩阵乘积为I、精确方向运输，以及全部25个中央turn

`det[T_e ell_i,ell_q,ell_j]≠0, i≠p,j≠q`。

八张共200个实际非零行列式；这里只核新图实际使用的八张，不重跑旧42张完整分类。

每张chart还保存十个互异平面的规范法向量：

`span(T_e ell_i,ell_q), i≠p`，和 `span(ell_q,ell_j), j≠q`。

程序分别实际枚举每个平面81向量，确认十平面互异，并集为全部729个向量。它们共享线span(ell_q)，其覆盖大小也为 `9+10(81−9)=729`。

## 4. 全部图顶点对的三步覆盖

给定任意 `(u,x),(v,y)`，源坐标x任意。以下证据不假设纤维平移为图automorphism，也不把零坐标测试当成全坐标覆盖。

若u、v不相邻（包括u=v），父目录证书为其deck平移类保存NB3词 `(p0,p1,p2)`。相应实际controller路径为u0=u、u1、u2、u3=v，实际三矩阵为T1、T2、T3。路线末点为

`T3 T2 T1 x + t0 T3 T2 ell_inv(p0) + t1 T3 ell_inv(p1) + t2 ell_inv(p2)`。

左乘T3真逆后，三个噪声方向的秩等于

`rank[T2 ell_inv(p0),ell_inv(p1),ell_p2]`。

NB3条件给 `inv(p0)≠p1`、`p2≠inv(p1)`，所以第3节中央turn使该秩为3。三个噪声参数由此双射到整个F9³，无论实际仿射中心 `T3T2T1x` 为何，总能达到y。

生产程序对全部5616个实际同层／非邻有序controller pair，从234类证书导出实际deck平移词，再核实际端点、NB3与实际中央dart矩阵的非零行列式。这里deck平移只用于controller词；s/t的chart正反可能因端点label顺序改变，程序使用每条实际dart对应的矩阵，而不是假设fiber平移保图。

若u、v相邻，令e为该controller边，矩阵T、端口p／q。前回退路线 `u→u'→u→v` 的像是

`Tx + span(T ell_i,ell_q), i≠p`。

后回退路线 `u→v→v'→v` 的像是

`Tx + span(ell_q,ell_j), j≠q`。

真逆外边矩阵保证这些路线有共同中心Tx；第3节十平面覆盖全部V，故任意y均由某条长度3回退路线达到。实际共有468个相邻有序controller pair，每个使用八张已核chart之一。

5616+468=6084，覆盖全部78² controller有序层对；每个论证同时覆盖任意x、y。因此完整56862点图直径≤3。最大度54的简单图半径2球至多 `1+54+54·53=2917<56862`，故其直径恰为3。

## 5. 生产实况与边界

唯一单worker准备、实际八chart证书、编译、生成及全部生产检查，实测总 **0.961254264／30 CPU秒**：prepare0.048353834、compile0.701562019、generate0.211304870。全部进程已终态，各步exit0，见 `TERMINAL.json`、`GENERATION_RESULT.json` 及实际日志。

生产运行0 BFS、solver、Lean、hash、install，未重验旧1620／20580或其他已接受图；未继续controller参数搜索。完整新图fresh独立验收与具体Lean分别在各自scope记录，不由本生产结果冒充。

已定位degree54公开保证55350，本图阶56862多1512；最新全球最高与首创未由本目录认证。
