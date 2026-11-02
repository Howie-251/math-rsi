# Sampels672：两份源＋右匹配1344的读取门

有限本地same-source/history查询未定位“固定Sampels672源、两copy保边、M(h)=h*t、t遍历H672”的完整NO或旧UNKNOWN窗口。本轮没有枚t、生成邻接或候选、计算endpoint、运行BFS/field/solver/Lean。当前684/H342全部233928等变匹配NO是不同source，不可套用。

## 精确primary身份

缓存 `research/ddp/m1_sources/desc_g4.html` 的182–189行（latin1编码）是former7D4的672点Cayley源：M. Sampels，1997-07-29通信，论文 *Large networks with small diameter*, WG97/LNCS1335, pp288–302, 1997，[DOI](https://doi.org/10.1007/BFb0024505)。官方 [D4说明#74](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#74) 的184行逐字给出 `Z6 ⋉39 Z112` 与

`[2,73]<>[4,23], [5,54]<>[1,22], [5,71]<>[1,31], [3,42]`。

第189行给 [作者原NX邻接表](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD4/672_6_112_39_sampels_adjlist.txt)；这次未下载。source D4只继承这项published former-entry事实，本地未定位672完整literal/独立D4回执；不得拿684的两个轨道BFS证书补上。官方随后列的2024其他672 generators不是本轮固定源。

## law不可沿用684的数值约定

本次冻结RIGHT law为

`(x,y)(u,v)=(x+u mod6, y*39^u+v mod112)`，

`(x,y)^-1=(-x mod6, -y*39^(-x) mod112)`，

S为上面七个实际字面pairs。旧 `m1_sources/SOURCE_NOTES.md` 第31–35行已警告，684恢复代码采用normal坐标在先的LEFT law；不能保留S的数字却换乘法。若未来要复用LEFT law `(n,a)(m,b)=(n+39^a*m,a+b)`，一条正确坐标同构是 `phi(x,y)=(39^(-x)*y,-x)`，每个generator也必须同时变换。此处仅给符号，不做新pow/order/inverse测试。

可为新recipe自行取label `112*x+y`、identity0，但这不是已绑定到作者NX原标签的map。若root授权后续有限gate，应先绑定该RIGHT recipe/S的真实inverse与canonical labels；这是新输入语义，不是重做source全D4。现有672 primary定义足以指定一个可生成的源，但本门不虚构本地validated artifact。

## 一个完整672t接口，尚未执行

取两份这个7regular源，保全部旧边，加入 `(h,copy0)--(h*t,copy1)`。right乘t为bijection，因此若原输入绑定正确，条件候选是1344/5376、全8regular，旧两copy共保4704边，加672条perfectmatching。

令A_a为该实际S的旧长度a endpoint集合，含A0={e}。跨copy长度≤4的路径若有3次matching步，至多一条旧边，必有连续匹配往返，可消为一次cross。因此精确条件为

`U_t = union_(a+b<=3) A_a*t*A_b = H672`。

源right edges与matching都和共同leftH作用交换，故copy0的identity代表就覆盖所有crosspair，反向由无向距离覆盖；这次确是Cayley672，不能沿用684的two-type框架或其source证书。源内部D4仍由published输入继承。t可按6×112全域一次有限枚举，无需改action、phase或S。

本轮未定位source672的旧≤3endpoint缓存，未生成任何新set，未对t=e或其它t数值判断。若以后出现全U_t命中，仍应按root授权生产实际图并fresh验收，不据symbolic read门提前报新图/纪录。若未来全域NO，也只关此固定source/rightmatching，而非任意matching。

读取整理保守计0.8 CPU秒/cap3，含一次HTML UTF8 decode失败后改latin1；一条辅助搜索在工具dispatch前中止，没有数学执行。0HTTP/源解析/BFS/DP/field/solver/图/Lean。当前停止，后续672t实际批另由root决定。
