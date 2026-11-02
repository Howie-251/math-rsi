# 实际 684 源的双副本 shared-right-shift 接口

这是只读 source/scope 门；本轮未生成 1368 图、未枚举 t、未计算任何球或 BFS。

原先“684 是 Cayley 图”的前提被实际缓存 primary 说明推翻：官方 D4 `#74` 明确它是 H=C38⋊23 C9 上的两基点 voltage lift，automorphism action 有两个 vertex orbits，且不是 vertex-transitive；旧 672 项才是 Cayley。故不得把 684 个标签当成群元素、固定单一根枚举 684 个 right shifts。

修正后冻结的候选规则是：源点为 `(τ,h)`，τ∈{0,1}，h∈H342；保留两份完整源图，添加 matching `(τ,h,copy0) ↔ (τ,h*t,copy1)`，同一个 t∈H342 用在两个 τ 上，反方向为 t^-1。这确为 perfect matching，所以若生成则 n=1368、m=5472、全 8 regular。同层 D4 继承；cross≤4 尚未检验。

待授权数值批的可推翻预测是：存在一个 shared t，使四个 τ→ρ cross endpoint slots 同时覆盖 H342。所有长度≤4 的最短跨 copy 路径只需一次 crossing：若有三次 crossing，因只有至多一个源内步，必有相邻 matching 来回可删。于是条件可写为 `union_{σ,a+b≤3} A_{τσ}(a) * t * A_{σρ}(b) = H342`，其中 A 是实际源的端点字集合。这里只登记公式，不枚举 A 或 t。

相同 fixed-host/shared-right-t342 旧 strict NO 若定位，应直接继承；现有 684 拆点、p43 电压迁移与删一个 cross matching 是不同规则。读门预算≤5 CPU，后续有限 342t 门须由 root 另授权，不自动改 host/degree/twist。
