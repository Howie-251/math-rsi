# E16 μ=0 结构化闭合的独立终审

**PASS · sound-modulo-imports · same-family · provisional。** 审计者 /root/q6_a8_easy_audit，按指定 GPT-6.1-sol/high 与 ARIS proof-checker 本地流程。原域为 \(Q_7\) 任意 56 边短匹配 \(M\)，且七坐标位一半面的最小绝对孔差 \(\mu=0\)。存在包含全部原边的全短 Hamilton 单圈。服务端模型身份未经独立认证。

| 义务 | 核验 |
| --- | --- |
| 原域剥离与实际匹配 | 原匹配每条短边覆盖两色各一，故每色八个原孔。短邻原孔可增广一边调用完整 E14。独立原孔有至少两条平衡轴时，适用已审双平衡轴回代。唯一平衡轴下，以原短跨和压缩端口保留实际匹配，平衡小面每色三或四孔及零、两条规定跨边均有入口。剩余 \(a=0,1,2\)。内切近平衡与差二小块两桥压缩用实际大面 \(K(Q_6)\) 匹配，并按辅助边标签展开恢复规定原边。 |
| 定向与全局其余轴 | 逐内位翻转使大面位一差 \(-g\le-2\)，差二必须 \(2\le p\le r-4\)。六位全补加换色在必要时令物理 α 为奇，并保留上述方向。全图另一平衡轴排除有符号零，可能的绝对差一局部孔数恰落入旧中央 D。由此全局其余六轴绝对差至少二。若差二仅中央保留，差三仅剥已证单色小面。各旧入口都按物理轴、角色和实源检查，无需整层高 μ 定理。 |
| 三基及运输 | 三套重量归约完成。独立逐标号生成及相邻交换共同分轨分别得 4,950/19、42,000/98、32,287/72。作者每个物理大面代表均严格重建。固定外位六后，奇组 \(64+\ell\)，偶组 \(127\operatorname{xor}v\)。同一个内位置换同时输运两组、全体小面孔及实际原 M，小面孔保留实际位置。独立构造也闭合空小面十九轨。 |
| 反例到静态 PB | 除索引 1140–1144 的五条全局差排序外，变量、约束和元数据全部逐条未改。189 行正表作用于 hole_64 到 hole_127，故不同的代表置换可以改变已去掉的序关系；对源的物理定向及所有其它必要条件无影响。若原匹配是反例，运输后的同一实际原孔与实际短邻伙伴给出物理孔指示及计数、阈值和桥源旗标的真值，所有充分入口均失败，赋值满足修正 PB。独立从旧源及审过的三基重建全部 PB 字节。 |
| PB 到实际 CNF 的可满足性运输 | 基于已审核的 edge_cnf 及 even/odd 编译器。旧规则保留，同一 PB 的每个满足赋值给阈值和计数等辅助量可取的真值。新正表实际独核有 189 个新选择变量，对每行加 64 条选择蕴涵再加一条至少一；取其实际匹配的一行，设置相应选择变量，即延拓任一 PB 满足赋值。逐句重建冻结 CNF 的全部字节和映射相同。无宽多区间约束。 |
| 实际终端及逆回代 | 冻结原 CNF 上实际 Glucose4 产生 21,116,326 字节 DRUP，无外来学习。原 CNF 与完整 DRUP 用独立官方 DRAT-trim 的 RUP 模式 -I -U -t 590 验真，退出码零、唯一 s VERIFIED、零 RAT 引理。独立散列核对其执行器、源码、原 CNF、证明和实际日志，并核证书末行空子句。故 PB 不可满足，排除所有剩余原反例。凡在前置门闭合的圈，展开后并沿原自同构逆运输，仍是一条覆盖 128 点的全短圈且包含最初的 M。 |

## 冻结绑定

| 文件 | SHA-256 |
| --- | --- |
| MU0_FULL_CLOSURE.md | 801b9366b09c34e26a8ce474d0656998ab40fba9fc3803352e54e803cbf99530 |
| MU0_STRUCTURED_SOURCE_REVIEW.md | 41f887dd8150f017bd0fe8c2bdc990df1c66e663a23ff1112ebe0ce1b8a204fe |
| MU0_STRUCTURED_SOURCE_REVIEW_check.json | 2250075068f1a28269e9a460a5413023ef9e050fceaa8209aeb5c90c469dfc39 |
| MU0_STRUCTURED_CNF_REVIEW_check.json | 60430c8f9155ee0d12fb2da287225977b5f2f0750d2a1db1ad7375cbbaaa7712 |
| MU0_STRUCTURED_PROOF_REVIEW_check.json | 416b94fa74d47493911bd85a967498edf12b4e0907ce22e924ac945a1de53b84 |
| MU0_STRUCTURED_JOINT.pb | 6e37bc98707b75beb29f9d37aa0c8f9a2e72acfa2672dc8bd263763185734d30 |
| certificates/mu0_structured_joint.cnf | 9371c1c91efeb0555b1a568e884611e61bcf183348eb66bc2316208685e47b68 |
| certificates/mu0_structured_joint.drup | a16947d033fea515d476d79b031e6b2508cf275fd05e5026c03079c86bc7dabf |
| certificates/mu0_structured_joint.verify.json | bddad665bb30edda4f0814ecfa27f9482bb8a162640875adaeac5595b6a0c929 |
| certificates/mu0_structured_joint.verify.log | 1cecd01b276829c15ae87828ecfe56121e6811a9e108683c5852debc9a8b5dd2 |

[最终整装](MU0_FULL_CLOSURE.md) · [归约及静态源核验](MU0_STRUCTURED_SOURCE_REVIEW.md) · [独立重建 CNF](MU0_STRUCTURED_CNF_REVIEW_check.json) · [实际证明与官方 RUP 回执绑定](MU0_STRUCTURED_PROOF_REVIEW_check.json) · [实际官方日志](certificates/mu0_structured_joint.verify.log)

E16 全层的并合使用已审初始归约的 \(\mu\le4\)。每个有相邻孔的实际输入已由 E14 接受。其余短匹配本身见证独立孔集可实现，故五个全局最小值 \(0,1,2,3,4\) 穷尽输入。此处核准的 \(\mu=0\) 与已审四个整层共同给任意 56 边短匹配同一保边 Hamilton 结论。加上 E14 的至少 57 边原域，得到整装推论的至少 56 边阈值。 [E16 初始归约审计](../R7_E16_INITIAL_REDUCTION_REVIEW.md) · [μ=1 终审](../mu1_global_2026_11_15/delta2_extension/MU1_STRUCTURED_CLOSURE_REVIEW.md) · [μ=2 终审](../R7_E16_MU2_FULL_REVIEW.md) · [μ=3 根验收](../mu3_hard_first_2026_11_15/ROOT_ACCEPTANCE.md) · [μ=4 终审](../R7_E16_MU4_FULL_CLOSURE_REVIEW.md)

