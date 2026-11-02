# 两cut＋相邻双helper：weighted source距离恰可替代删边host

**支持全部三种2+2 partitions；纯paper，无新数值。** 源G为本目录READ_GATE绑定的Exoo600。删两条不交旧边F，四端点分成A/B各2，添h1–h2，并分别接A/B。令T=G−F；规则给602/903全3度。本文不parse源、不算球/BFS、不枚配置；旧三/四cut＋repair样本不当作本域结果。

**先得到精确T式。** 对任意old目标t，最短h1→t路线若先入old再到h2，可将到h2的整个prefix替换成直接h1–h2，严格缩短；若回h1则是可删重复段。因此最短路只有“H内prefix＋一次spoke＋纯T suffix”，给

`d_J(h1,t)=min(1+d_T(A,t), 2+d_T(B,t))`。

**再用last-cut restart证明G式。** 对h1给每个pin权重w=1（A）或2（B）。取任意pin q到t的G最短路径。若不含cut，原路线就在T中。若含cut，取最后一条cut的downstream pin s；其后suffix完全在T中，cut之前至下游的prefix长度L至少1。直接从h1到s的实际helper/spoke成本 `w_s≤2≤w_q+L`，故重启到s后接suffix，同长或更短即可实现原weighted-G路线。

于是 `min_p(w_p+d_T(p,t))≤min_p(w_p+d_G(p,t))`；反向由T⊆G得到。结合上式：

`d_J(h1,t)=min(1+d_G(A,t), 2+d_G(B,t))`，

`d_J(h2,t)=min(1+d_G(B,t), 2+d_G(A,t))`。

证明只用全cutends都在pins及权差≤1，**不要求每cut整对属于某一helper**。因此ab|cd、ac|bd、ad|bc三种partition全部成立，不只cross-only。

双方new-root R9精确条件为

`[R8_G(A)∪R7_G(B)] ∩ [R7_G(A)∪R8_G(B)] = V(G)`，

亦即 `R7_G(A∪B) ∪ (R8_G(A)∩R8_G(B)) = V(G)`。

这里R为闭球。**并未证明**单独 `d_T(A,t)=d_G(A,t)`；相等的是有1/2起步权重的最小值。旧旧距离也不能直接换成源距离：删cut可能毁旧geodesic，双方new-root全过仍须最终602图的旧旧检验或另一完整证书。

这个接口允许获授权后用原源R7/R8做精确新根门，不表示现有通用R7/R8缓存已存在，也不代替source literal绑定或实际枚举计数。不能推广到cutends未全部挂接、不同helper权差或含其它old-old repairs的旧规则。本次只读READ_GATE并完成证明；图、BFS、枚举、solver、field、Lean、外审与新计数均0。
