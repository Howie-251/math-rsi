# 独立攻击预测：uniform多copy的任意helper batch

2026-11-01。保留旧one-copy记录不改。先登记本次新预测，再运行一次新subset-owner toy，总预算15 CPU秒含编译及汇总，单worker。

**P1：** source的完整中心code C=O×spread的N(c)两两不交、pinunion=H\D，C_off诱导matching T，D到C_off无1/2source路线。对每个c统一加k≥1个完整原N(c) clones，在cap Δ=δ+k下保留全部旧边，再加入任意非空有限helper batch及任意内部边，若最终D3，则M=R(R−1)≤floor((Δ+2)²/4)。本次不假设clone或cloneclass只有一个owner。

拟攻击处：经剩余k个degree的旧D/clones是否出现新三步路线；S_c为helper owner任意子集时，覆盖与求和有没有漏记或重复计数导致反向错误；a_h=#owned offdiagclasses是否确实给helper degree成本下界。

拟独立证明：精确helper h到旧c的≤3路由为h∈S_c∪N_B[S_T(c)]。因此t≤|S_c|+|S_T(c)|+Σ_{h∈S_T(c)}d_h；T置换令Mt≤Σ_h a_h(d_h+2)。因a_h+d_h≤Δ，逐点整数二次界给结论。不要求任何S非空、disjoint、singleton，也不使用k²容量界。

**新有限检验。** M4/t4枚举全部16^4个owner-subset assignments及64个simple helpergraphs；M6/t3枚举8^6 assignments及8个graphs，共6291456配置。包含empty/multi-owner。对每个满足所有旧center覆盖的配置计算真实a_h、d_h、最小可行cap max(a_h+d_h)，核全求和链与二次界；保存反例即停，或者各case计数、cap分布、empty/multi-owner witness。该toy只检查中心路线必要条件，不声称整体toy D3或物理k-copy pin slots已实例化。

如果成立，balanced R65/δ81的k1..45及Payne R64/δ80的k1..44被此局部扩张障碍排除；Δ127/125仅等号未排，不是构造存在性。只对uniform全饱和、旧adj固定、保持同cap成立；不排nonuniform/presaturation joint/改旧边/提高cap/不同code或整个A族。0图生产、BFS、域/投影旧检验、Lean、solver；不生成k2图。
