# URSA 源感知双循环插点：满秩自返路成立，65-controller 全局覆盖失败

唯一冻结的 rank-guided graft 被 coarse R4 反例推翻。新 65 点 controller 简单、4 正则；全部 65 根的四步覆盖检查得到 24 个有序缺项，即 12 个 controller 无序点对。新点 64 到 19、38 亦超过四步，因此不生成 16640 点 lift。未换下一个 graft、词、offset 或 controller。

## 依据真实源与缓存选择一次 graft

已查相关 Wiki：旧 C19、974 规则及其它 GF4 固定 phase 族与此 source-aware 双 cycle 插点不同，没有重复执行它们。沿用实际 [64-controller 接口](../INTERFACE.json)、[cycle 结构](../CONTROLLER_SUMMARY.json) 与 [341 词缓存](../route_capacity/WORD_IMAGES.json)，没有重 parse 原 16384 源或重跑源 BFS。

实际 a=type0、A=type3，b=type1、B=type2；a 为八个 8-cycles，b 为十六个 4-cycles。cached abAB=(0,1,3,2) 的 noise image rank4、大小 256，basis=[1,4,16,64]；其 composite linear map rank2 并不改变 noise 满秩结论，不能混淆两种 rank。因此无需 a³b fallback。

按事前 lex 规则，首个合法旧点为 u=0：

~~~text
v=a(u)=16
t=A(b(v))=46
c=B(t)=48
w=64
~~~

四旧端点 0,16,48,46 互异。删 a-edge 0→16、b-edge 48→46，分别插入 0→64→16 与 48→64→46。全部逆类型由新的 a,b permutations 求出；四个方向没有独立拼旧 inverse。

新闭路真实为 64−a→16−b→57−A→46−B→64，故缓存 rank4 给新纤维任意 source x 到任意 target y 的四步 noise 覆盖。这个局部正向保证真实成立，但不是完整 D4 保证。

## coarse 必要检查与反例

新 controller 有 65 点、130 边、每点四个不同非自身邻点，全部 inverse ports 和无向反边吻合。对全部 65 根作截断 R4，而不是只检查新点或抽样根。保存 24 个 ordered 缺项，首项 0→11；其中旧旧缺项 20 个 ordered，新旧缺项 4 个 ordered。新点 64 缺 19、38。

任一 lift 路径投影为 controller 路径，因此 controller 没有长度至多 4 的路时，任何同一 skeleton 上的纤维 charts 或 affine offsets 也不能填补对应点对。对这个固定 graft，coarse 反例足以否定 D4，不必构造大图、求全部 rank4 证书或再做 w/fiber0 actual R4 gate。

worker CPU 0.007038142 秒，硬 RLIMIT_CPU 5 秒，无编译。actual 大图 n/D、普通大图无序坏对数均为空；12 是 controller 的无序点对数，不能写成 16640 图的实测坏对数。controller 的精确全局直径没有计算，只知至少 5。

## 关闭范围

只关闭此 cached abAB 引导、lex u0 的一次双循环插点。满秩返回词保护自身纤维，但同时把原 a/b cycles 延长后，全局 controller 路由发生损失；保住这一局部几何资源不足以推出其它点对覆盖。没有外推所有 65-controller，也不追加其它 u、word、offset 或 group 参数。

证据：[冻结预测](PREDICTION.json)、[实际选点](BINDING.json)、[65-controller](CONTROLLER65.json)、[完整 coarse 缺项](COARSE_R4.json)、[终态](RESULT.json)、[复现入口](run.py)。条件 rank4 与投影逻辑由互补 proof 记录说明，本轮没有源图重复验收或新下界。
