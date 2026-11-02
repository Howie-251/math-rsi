# Binary cross-coupled3072：唯一 M0 修改的纸面接口

状态：**true-inverse、全部 same-controller fibre 四步覆盖及已知坏 word2022 的满 packet 预测支持。** 本文没有运行数值、枚举矩阵/words、生成图、BFS、field、solver、Lean或外审。旧 pair-swaps 的全域 NO 保留为旧 chart 的实际终态，不被本局部修复覆盖。

## 固定继承与唯一修改

实际 C192 controller/type-label/`bar=[0,3,4,1,2]` 均与 [pair-swaps 接口](../binary_pair_swaps3072/PAPER_INTERFACE.md) 相同；实际数组仍取 `../NEW_ROUTE4_TYPES_AND_TRANSITIONS.json` 的 `.transition`。不改 controller 或其它 field。

fibre=F2⁴，bit code `x0+2x1+4x2+8x3`，输出 step 是

`step_p(x,t)=M_p x+t v_p`，全部常数0。

保留 `v=[15,1,4,2,8]`，`M1=M3=swap(e1,e2)`、`M2=M4=S=swap(e3,e4)`。只把 M0 改为

`T=I+uℓ`，其中 `u=e1+e3`，`ℓ(x)=x1+x2+x3+x4`。

这里 e1…e4 是四个 basis vectors，ℓ 是四坐标之和，不能误作取某一个坐标。column codes相应为 `[4,7,1,13]`：T 将 e1送到e3、e2送到e1+e2+e3、e3送到e1、e4送到e1+e3+e4。这是指定公式的符号展开，不是矩阵搜索。

## 真实逆关系不受破坏

F2 中 `ℓ(u)=0`，故 `(uℓ)²=0`，从而

`T²=(I+uℓ)²=I`。

又因 `v0=e1+e2+e3+e4`、`ℓ(v0)=0`，有 `T v0=v0`。实际 type0 self-reverse，所以其要求 `M_bar M=I`、`M_bar v=v_bar` 均成立。

其它两对1/3、2/4的矩阵和 noise未改，仍分别满足 `M_bar M=I` 及 `M_bar v_p=v_bar`。因此全部五端口的 completed relations 真正互逆，没有靠无向并图修补。

各端口 noise非零、实际 controller targets按原契约不同，故实际图删除 holding 后最大度仍至多10。M0改变后，哪些完整 vertices 出现 holding也可能改变；应继续仅在完整 global source/target label相等时删除，不能继承旧 chart 的具体度分布，或删除所有controller-stay输出。

## 两次 return 保留全部 same-controller16点

对任意端口 p、任意源 x，两个noise分别为t,s时

`step_bar(p)(step_p(x,t),s)=x+(t+s)v_bar(p)`。

此公式对新 type0也成立，因此五个可用 return directions仍为同一 circuit

`{e1,e2,e3,e4,e1+e2+e3+e4}`。

两个return能加入任意至多两个方向之和，恰覆盖F2⁴的全部16向量：零、5个单方向及10个不同双方向和。因此对192个controller、每个源x，同controller所有16目标仍有长度至多4的 completed walk。holding收缩保持端点并只减少长度，所以结论是真正图 Walk≤4。

## 已知0→1坏 packet 的具体修复

继承 root 原 exact-point 结果所绑定的 controller word `2022 : 0→1`，不在本文重新枚举其 endpoint或其它 words。对顺序 `2,0,2,2`，四个输出noise columns是

`M2 M2 T v2`，`M2 M2 v0`，`M2 v2`，`v2`。

由于 `M2²=I`、`T e3=e1`，它们依次为

`e1, e1+e2+e3+e4, e4, e3`。

这是一组基：从第二列加另外三列得到 e2。故新的2022 word自身 noise rank4，**对任意源 x，其 image 都是目标controller1的全部16点**，不只修 x=0。预测该旧坏 packet从union8变full16是严格的条件纸面结论，前提是实际实现按本列/offset约定复合并保留同一 controller word。

旧 `W=span(e3,e4,1111)` 中所有向量的前两坐标相同；`T e3=e1` 不在W。这说明本次修改确实破坏了该旧packet的不变三维空间，而不是只更换word计数或同一空间内的basis。

## 不能外推的结论

满2022仅解决已知的这个0→1 endpoint；same-controller成功也不代表其它controller对成功。仍需 root 唯一获授权的实际全192×16源点覆盖门来判整体3072/D≤4。不得用一个packet rank4推所有roots、把旧source D4迁移到新chart，或把其它rank-deficient packets仅按大小相加。

这一次是从旧具体不变空间反例驱动的唯一手选M0变更。若全局门仍NO，按授权停止，不枚下一矩阵、field、controller或参数。本文新增图/参数/Lean和数值批次均为0。
