# C192 / identity binary chart：在接口处停止

状态：**指定 identity-chart3072 候选关闭，不启动 exact-point gate。** 真实五端口不是全 self-reverse；五个 distinct circuit offsets 不满足逆关系，而按真实逆对合并 offset 后，零常数 identity chart 必不连通。

## 实际输入（只读继承，不猜端口）

`formal/DegreeDiameter/Portfolio/F3Graph15552Definitions.lean:29–30` 字面给出

`inverseType = [0,3,4,1,2]`，

并有已闭 `controller(controller(a,p),inverseType(p))=a`。因此只有 type0 self-reverse；另有两对 `1↔3`、`2↔4`。controller0 的实际五个目标是 `[0,11,59,79,180]`，并非五个 holding ports。

source 的 step 约定是**输出噪声**

`step_p(x,t)=B_p x+c_p+t v_p`。

全部 `c_p=0` 已由 Definitions:27–28 的实际常数及已闭 `constant_zero` 确认。完整五组原 F3 matrices 在 `../NEW_ROUTE4_TYPES_AND_TRANSITIONS.json` 的 `types` 字段；实际方向依次为

`[1,2,1,0]`，`[1,2,2,0]`，`[0,1,0,1]`，`[1,1,1,1]`，`[1,2,1,2]`。

这些原 B 是关系的 quotient representatives，不能当可逆4×4 matrices或自动降到 F2；本候选是重新固定 `M_p=I`，不是复用旧 F3 proof。这里只读了保存类型表，没有新矩阵运算。

holding 的实际契约也已读取：原 `affine_relation_recovery/generator.py:27` 仅当 `other==vertex` 才删除 virtual self；Definitions:74–77 同样以**完整 global label 不同**作为实际 SimpleGraph 邻接的条件。controller 相同但 fibre 不同的输出不能删除。旧 F3 的648 degree14 点不能直接当成新 binary 余度 profile。

## Identity chart 的必要逆条件

固定本提议的零常数与 global identity matrices，binary step relation 是

`y=x+t v_p`, `t∈F2`。

它的 inverse relation 仍为 `x=y+t v_p`。若 reverse port `bar p` 也只有一个非零 binary noise direction，则真正互逆要求二元 line 相同，即

`v_(bar p)=v_p`。

真实端口因此强制 `v_1=v_3`、`v_2=v_4`。所提五元 circuit `{e1,e2,e3,e4,e1+e2+e3+e4}` 的五个向量互不相同，无论如何指派到五个 labels，都不满足这两对等式。它不是合法的五端口 true-inverse baseline。若强行取 forward/reverse 的无向并图，则已更换关系并丢失“每端口仅两个邻点、max10”的论证，不能当本候选继续。

## 合法地重复方向也不能修这个 identity 候选

若为满足真实 bar 而令每对共享 direction，则全部 step 的 fibre 增量落在

`W=span(v_0,v_1,v_2)`，`dim W≤3`。

因为 `M_p=I`、`c_p=0`，任何长度的 controller path 都保持 fibre coset `x+W`，不只是四步路径。F2⁴ 至少有两个这样的 cosets，故3072点候选不连通，不可能 D≤4。删除完整-label holding steps 只删边，不能消除这个分量障碍。

“两个二步 backtracks 的方向和覆盖16”在反事实的五个独立可用 circuit directions 下是正确容量直觉：零向量、五个单方向和十个不同二方向和恰为16。但实际 identity/true-inverse 契约只留下至多三个不同方向，不能套用该直觉。

## Scope 与停止

本结论只排 **同一 actual C192 controller、global `M_p=I`、旧零常数、每port一维F2噪声** 的提议。既没有排重新设计非identity矩阵、非零常数、不同 reverse/port 接口，也没有排一般(10,4)3072或所有binary构造。它与已实际失败的 signed-integer-F2 chart 是两个不同规则；旧 signed gate不重跑。

本次已在输入处得到充分障碍，按 root 优先指令不再扩查其它模型/旧packet或启动数值。未声称没有任何相关历史。原 sourceD4/field/kernel证据继承，不重编或重验证。

标准库只读进程实测0.000781136 CPU秒；含源码定位和文档准备保守charge0.25/1秒。新 controller/word/field/matrix/图/BFS/solver/Lean/外审与新图计数均为0。完成即停。
