# 相邻 controller 层的二元 pencil 覆盖：条件纸面引理

状态：**支持，但依赖下列完整 chart contract；尚未绑定任何 actual C32/matrix 表。** 本文不选 controller、不读新 source/矩阵、不枚 words、不运行数值、BFS、field、solver、Lean 或外审。

## 1. 必须固定的输出噪声及逆关系

每条 controller dart `p : a → b` 的 completed affine 邻接必须按 **输出坐标** 写成

`step_p(x,t) = A_p x + c_p + t v_p`,  `t ∈ F2`。

这里 `v_p` 是实际 step offset，不是未经变换的输入端 direction。若实现把噪声放在 `A_p` 内，必须先转换成实际输出 offset，不能直接借用本式中的 `v_p`。

对每条 `q : b → c`，有真正 reverse dart `bar q : c → b`，且 completed 邻接关系互逆。另有

`A_(bar q) v_q = v_(bar q) ≠ 0`。

**仅这一条方向等式不等于完整 inverse contract。** 本文还使用真正互逆所保证的“从任意 y 经 q 再经 bar q 可以返回 y”。等价的充分代数条件是

`im(A_(bar q) A_q − I) ⊆ <v_(bar q)>`，

`A_(bar q)c_q + c_(bar q) ∈ <v_(bar q)>`，

连同上面的方向等式。常数 `c` 不必为零。

直接复合得到

`step_(bar q)(step_q(y,t),s)`

`= A_(bar q)A_q y + A_(bar q)c_q + c_(bar q) + (t+s)v_(bar q)`。

最后两项的系数随 `t,s` 穷尽 F2；完整 inverse contract 保证这个二点 affine line 包含 y。因此 **q,bar q 的实际二步返回集合恰为**

`y + <v_(bar q)>`。

这不是把两个 controller reverse labels 自动当作同一条具体边的折返。若选择到另一个 fibre 点，这两步本身就不是具体边折返。

## 2. 三个 rank-two planes 已足够

固定 `p : a → b`、源 fibre 点 x。先走 p，再走 q,bar q，所有输出恰为

`A_p x + c_p + span(v_p, v_(bar q))`。

在 b 的输出 chart 中，要求所有可用返回 offsets `v_(bar q)` 恰构成一个四元 Fano arc，且 `v_p` 是这个 arc 的一员。特别地，可用

`V = {e1,e2,e3,e1+e2+e3}`。

更一般地，只需 V 有四个非零向量且任意三个线性独立。对固定 `v_p ∈ V`，其余三个向量在 `F2³/<v_p>` 中的像两两不同且非零：像为零会使两个方向相同，像相同会给出 V 中三个向量线性相关。二维商空间恰有三个非零向量，所以这三个像全部出现。

于是三个 planes 的并为全空间：

`⋃_(v∈V\{v_p}) span(v_p,v) = F2³`。

因此对任意 x 和任意目标 fibre 点 z，都可选一条 q,bar q 返回使 `p,q,bar q` 到达 z。结论为：

**凡由实际 dart p 相连的有序 controller 层，其任意两 fibre 点之间都有长度至多 3 的 completed walk。** 无需任何单条三词的 noise matrix 具有 rank 3；这里三条 rank-two image planes 的并已经覆盖全部八点。`A_p` 本身也无需可逆。

若实际 SimpleGraph 只删除 completed 邻接中的相同完整 vertex-label holding steps，则删去这些停留得到真正 graph Walk，长度仍至多 3。不能删“controller 相同但 fibre 不同”的步骤。

## 3. 适用边界

四 arc 必须用实际输出 offset 表绑定。在不同 endpoint charts 中，既要确认返回方向与 `v_p` 在同一坐标系，也要确认 reverse labels 实际提供全部三个所需返回方向。不能因旧原始表曾写过 e_i 就自动套到另一组 best chart。完整 inverse/holding-edge contract 同样尚需实际模型满足。

本文仅解决相邻 controller 层的 fibre 覆盖，不保证同层或非相邻层，不证明存在合法 C32，不绕过 [Cayley32 商障碍](CAYLEY32_QUOTIENT_GATE_PAPER.md)，也不排任意非 Cayley/permutation/其它端口模型。旧“各三词分别 rank 3”的 NO 保持历史范围，不能拿它否定这里的多路线并覆盖。

本次为纯纸面条件结论，新增图、参数、Lean 和数值批次均为 0。
