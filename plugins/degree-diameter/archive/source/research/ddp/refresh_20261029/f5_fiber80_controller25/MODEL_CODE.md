# 25 点控制器、80 点纤维：必要路线模型已准备

实际执行 `python prepare.py --prepare-only`，PID **2721111**，exit **0**，
准备 **2.399239534 CPU 秒**。`model.cnf` 共 **333343 变量、1129292 子句**。
没有启动 solver、生成控制器或2000点图，也没有构造 charts。

## 固定 motif 的完整补边范围

顶点0..24，固定链 `(0,1,2),(2,3,4),(4,5,6)`，另固定6个独立K3，标号从7起。
固定27条边；2、4各已度4，其余23点各已度2。全部233条两个free点之间尚非固定
的边都有变量，包括7点链内部的潜在补边，没有预先固定任意外边。

每个free点恰选2条新边：一条OR确保非空，每个真selector要求另一个真selector；
随后用旧C31模块的forward前缀阈值1/2及overflow禁止式编码至多2。故实际图必为
25点、50条边、简单4正则，其中23条为新选边。此阶段1165变量、2750子句。
`INPUT_SCOPE.json` 保存全部固定边及自由顶点，`EDGE_VARIABLES.json` 映射233变量。

没有复制C31的canonical标号条件，也没有添加新的canonical或local `2t+c4≤4`。
固定motif不是全部25点控制器的WLOG代表，任何失败结论只能限定于本motif。

## 完整 NB2 / NB3 及精确重数门

对不同端点 u<v：

- `NB2` 为全部中间点a的 `edge(u,a) AND edge(a,v)` 的OR。
- NB3 word完整枚举四点互不相同的 `(u,a,b,v)`；每个word门精确等价于三条实际
  edge同时存在。仅丢掉含恒假边的word；固定边为真，不只使用固定motif路线。

nonadj端点的三步nonbacktracking walk恰为上述简单路径。对于adj端点，这些路径
与该邻接边合成真正C4，排除了原路折返。

不同word分别作为计数叶子，即使它们的布尔门碰巧相同也不作计数去重。两个
互不交word列表的饱和计数门按下式平衡合并：

```
one = left.one OR right.one
two = left.two OR right.two OR (left.one AND right.one)。
```

所有中间AND/OR均完整双向Tseitin定义，故 `one` / `two` 精确表达至少1/2个实际
word，不是只能推出阈值的单向辅助变量。逻辑表达式缓存可合并相同布尔函数，但
不改变计数叶子的word重数，例如两个相同叶子 `[x,x]` 的 `two=x`。

每个不同点对的三条必要条件为

```
adj OR one
adj OR NB2 OR two
NB2 OR one。
```

第一条要求非邻至少一个NB3；第二条要求无NB2的非邻至少两个NB3。第三条与第一条
合用，等价于每个相邻端点对有triangle或C4：非triangle边若无C4，六个回退像的
并至多 `4+6*12=76<80`，不能覆盖目标纤维。该76门由独立数学检查确认后、实际
prepare运行前加入。

27个固定邻接对均有固定triangle，第一、二条因adj为真而恒成立，第三条因NB2
为真而恒成立，故无需为其建立路线门。其余273对完整记录 **5021个可能NB2项、
100756个可能NB3 word**，见 `PAIR_ROUTE_GATES.json`，包括内部点、word变量及
NB2/one/two的标志。这里数字是可能路径项，不能当作某张已存在图的实际路线数。

独立只读源码检查确认：四点distinct枚举、计数重数、Tseitin方向、三条最终子句
与固定边跳过条件一致。没有为该检查运行数值、图或求解器。

## 后续边界

本 CNF 只是 fiber80 的必要控制器门。即使 SAT，也必须先实际验收25点控制器，
再处理4正则图的端口分解和共同chart覆盖；不能直接声称存在2000点16度D3图。
本次未加入local循环计数门，因此SAT仍可能违反其他已知必要条件。

`MODEL.json`、`PREPARE_TERMINAL.json` 保存真实状态；准备代码只有 `--prepare-only`
入口。交 root 审阅后才考虑唯一60CPU控制器调用，UNKNOWN即停。没有触碰正在由
root运行的完整D14 K2 driver。
