# C192 / F2⁴ pair-swaps：单一合法 chart 的纸面接口

状态：**true-inverse 与全部 same-controller fibre 四步覆盖支持。** 这不是旧 signed-mod2 chart，未声称全部3072点 D4。本文不生成 controller/words/field/图，不做 source/BFS/solver/Lean 或外审；没有另选矩阵或参数。

## 实际 controller 与类型数据的位置

可直接提取的相对路径是

`research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/NEW_ROUTE4_TYPES_AND_TRANSITIONS.json`。

绝对路径是

`/inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/NEW_ROUTE4_TYPES_AND_TRANSITIONS.json`。

其中 `.transition` 是实际192×5 controller数组，`.types` 是按960个实际 arcs首次出现顺序排列的五组旧 F3 `B/v/c`，`.actual_arcs_bound=960`。**本候选保留 transition/type labels，替换全部旧 fibre matrices/directions；不把旧 F3 values 降域。** 旧完整 relation 输入的路径也在该 JSON 的 `.source` 字段：

`research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/affine_relation_recovery/source15552_AFFINE_RELATIONS.json`。

真实 reverse 为 `bar=[0,3,4,1,2]`，见

`formal/DegreeDiameter/Portfolio/F3Graph15552Definitions.lean:29–30`。

已闭 controller relation 保证 `controller(controller(a,p),bar(p))=a`。source D4、field/旧 kernel均继承，未重验证；controller D4 本身不保证更换 fibre chart 后的 D4。

## 唯一新 chart 的字面约定

fibre 是 F2⁴，bit code 为 `x0+2x1+4x2+8x3`；new vertex label 可用 `16*controller+bitcode`。采用输出噪声

`step_p(x,t)=M_p x+t v_p`，`t∈F2`，全部常数 c=0。

五个 matrices 的 column codes依次为

`M0=[1,2,4,8]`；

`M1=M3=[2,1,4,8]`（交换 e1/e2）；

`M2=M4=[1,2,8,4]`（交换 e3/e4）。

实际输出 noise codes 是

`v=[15,1,4,2,8]`。

因此 v0=1111，v1=e1，v2=e3，v3=e2，v4=e4。这里的 code/输出约定必须保持，不能用旧 F3 `.v` 或输入噪声代替。

## 完整逆关系合法

逐对符号上有

`M_(bar p) M_p=I`，`M_(bar p)v_p=v_(bar p)`。

type0 是 identity 与自反 noise line；1/3 的同一 swap互逆并交换 e1/e2；2/4 同理交换 e3/e4。因此若 `y=M_p x+t v_p`，则

`M_(bar p)y+t v_(bar p)=x`。

正反 completed relations 恰互逆，不需要强行取有向邻接的无向并来补缺逆。此契约与旧 signed-integer chart 的失败无关，也不受 all-identity 只能保三方向的障碍约束。

每个端口输出两个不同 fibre 点。实际五个 controller target labels 不同的输入契约使不同端口输出不会重合；删除完整-label holding 后最大度至多10。holding 只在完整 global source/target相同时删除，不能删除同 controller 下 fibre不同的邻接。

## same-controller fibre 的四步覆盖

从任意 controller a、任意 x出发，实际 controller word `p,bar p` 返回 a，fibre 输出恰为

`M_(bar p)(M_p x+t v_p)+s v_(bar p)`

`=x+(t+s)v_(bar p)`。

所以每一个实际 return direction 都能在至多两步加入，并且五个可用 return directions仍恰是

`V={e1,e2,e3,e4,1111}`。

连续作两个 returns即可实现 `x+αu+βv`，其中 u,v∈V、α,β∈F2。V是五元 circuit：零向量、五个单方向、十个不同二方向和两两不同，共16点。等价地，weight≤2的向量用至多两个 basis方向；weight3是1111加缺少的basis方向，weight4就是1111。因此两个 returns覆盖整个 F2⁴，结论对**每个** x成立，不只 x=0。

这些都是长度至多4的 completed walks。若某步为相同完整 label的 holding，删去该步后端点不变、长度只减；所得是真正 SimpleGraph Walk。尤其不能因某次 return在 controller上 backtrack，就把改变 fibre的两步误删。

## 尚未通过的全局门与停止范围

该论证只完成192个 controller各自内部的16点 fibre覆盖。它没有完成不同 controller之间的覆盖；旧 F2³ four-arc 的相邻层三平面引理也不能直接外推到本 F2⁴ five-circuit。因此后续唯一获授权的 exact-point gate仍须检查全部相应源点/目标层的真实 image union或实际距离，不能用controller D4、word数、noise rank计数或同层成功替代。

未定位到可直接继承的同 literal pair-swaps strictNO；本 paper没有为此另作历史扫描，亦未重跑 signed-F2。若这一个固定 chart最终为NO，只关闭它并停止，不选下一matrix、field或controller梯。3072目前仅是192×16的候选order，新增图/参数/Lean为0。
