# H19 Petersen subdivision：port assignment SAT的完整性

**纯paper，支持充要接口。** 固定本次选定的19点H：Petersen的9条edge各细分一次，实际Hdiam4由父任务metric gate提供，不在本文重验。旧自然364/714源G、28个degree3 ports、其余degree4、D≤5及不同ports旧距5全部继承；不使用公开364/728源，不扩大旧k≤14 NO。

**度数模型。** H有10个degree3点及9个degree2点，故24条H边，`a_j=4−d_H(j)`分别为1/2，`Σa_j=28`。设532个binary `x[p,j]`。每个实际port恰选一个j，每个j至多a_j个ports；全部28次选择与总容量28相等，自动每个j恰填a_j。oldport只增加1边，所有old/helper最终皆4度；总order383、边数714+24+28=766，且fresh helper labels保证spokes不重边。

**helper到old目标的精确式。** 对assignment的port集合P_j，任意helper h及旧点t有

`d_new(h,t)≤5 ⇔ ∃j,p∈P_j: d_H(h,j)≤4 且 t∈B^G_(4−d_H(h,j))(p)`。

充分性直接接一条H最短路、一条spoke、纯old路径。必要性取≤5最短路：若进入旧源又返回H，两个不同ports之间该段至少 `1+5+1=7`，不可能；同port返回只能回其唯一owner，重复段可删除。因此路径必为H内前缀、一次spoke及纯old后缀，分别由d_H与旧closed ball界定。这里不把旧source距离或cell覆盖当成新图距离proxy，而是完整last-entry分解。

于是对19×364个(h,t)，加入positive clause

`OR x[p,j]  over { (p,j): d_H(h,j)≤4, t∈B^G_(4−d_H(h,j))(p) }`

恰等价全部helper-old pairs≤5。R0为port本身，R1为实际source邻接加self，R2为已保存完整R2 cell，R3/R4为旧source缓存；都须只指old labels0..363，不能将二进制尾部padding当helper目标。重叠按OR处理，不能把覆盖次数当不同目标。

**为什么这是全383 D≤5的充要条件。** old-old由全部oldedges保留及原G D5保证；helper-helper已有H内≤4路。所以没有遗漏另一类pair。反之任一此固定H上的合法D≤5扩张必使用全部28ports：未挂接port不能在5步内从任何helper到达（最后old entry在另一port后还需5步）；其容量强制上述assignment，故满足全部clauses。若SAT构成实际图，383大于max4图的radius4上界 `1+4+12+36+108=161`，故其直径恰5，不只≤5。

**轨道与结果边界。** Petersen automorphism把subdivision pattern映成pattern，并诱导H同构φ，保持degree/a_j及全部H距离；`x'[p,φ(j)]=x[p,j]`直接转移assignment。故可按其120元作用归轨道，无需oldsource对称或重标ports。选择一个metric轨道代表的一次SAT仅检该H：SAT给可导出的candidate，须交root实际绑定/验收；UNKNOWN不排它，固定H的NO也不排其它metric轨道或一般19-helper图。235个Hdiam4 patterns不能因只试首代表而写成assignment全集已测。

本文件没有生成H、枚pattern/ports、构CNF、数值或BFS；source/旧balls/field/Lean/外审均未重跑。新增图、参数、Lean计数0，后续由root唯一有限批决定。
