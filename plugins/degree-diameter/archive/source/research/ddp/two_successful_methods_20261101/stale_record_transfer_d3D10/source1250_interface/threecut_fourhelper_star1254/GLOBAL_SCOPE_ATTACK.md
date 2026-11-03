# 三 matching-cut／K1,3 helper：全域表示与覆盖掩码的纸面检查

本文件先作 root 所定 GLOBAL/FULL_DOMAIN 的事前范围审查，随后只读已完成的 `global_three_matching_gate/{ACTUAL_DOMAIN.json,BALL_SCHEMA.json,run_once.cpp,RESULT.json,TERMINAL.json}` 绑定实际实现。未读取 source 边表、计算球/词、运行候选 BFS/solver/Lean/ARIS，也不重跑已完成 fixed-pair 1865 域。

## 1. Anchor 表示完整，但不把候选当 vertex-transitive

族限定于同一实际 Conder1250 source：删除三条顶点不交旧边，各条边的整对端点接同一叶，三叶接一个无旧 pin 的中心；不允许六端点任意重新配三对，不包含 P4、旧旧 repair 或其他 host。

任取该族的三 matching-cut，利用继承的 source edge-transitivity 将其中一条送到 e0={0,1}。另两条变成避开0、1且相互不交的源边；按实际 edge index 排成 e1<e2。因此枚举这个 anchor 的全部 unordered matching-edge pair，足以覆盖全族至同构。三叶可随三条 cut 一起置换，所以不需额外枚举叶标签或 cut 方向。

这只使用编辑前 source 的 edge-transitivity；没有说编辑后 1254 图 vertex-transitive，也没有把 source 的某一根代表性用于候选旧根验收。不同 anchor 像或不同参数可产生同构图，访问数不是非同构图数。

预期域：避 e0 两端的源边有 1875−(3+3−1)=1870 条。继承 girth16，e0 外的四个邻点不同；删除0、1后，1244个顶点保三度、4个顶点为二度。边对中共享端点者为 1244*C(3,2)+4*C(2,2)=3736，所以 unordered disjoint pair 数为 C(1870,2)−3736=1743779。实际实现仍应对每对检查两个端点集合不交；预期数量不替代 input/domain 实际回执。

## 2. 四根 source-ball 条件精确

设三 cut 的端点对为 Pi；E_r(ei)=R^G_r(Pi)，闭球含半径0。`STAR_SCOPE_ATTACK.md` 中的 weighted-lastcut 证明给出

- 中心至旧点 t：2+d_G(P1∪P2∪P3,t)；
- 叶 i 至旧点 t：min(1+d_G(Pi,t),3+d_G(Pj∪Pk,t))。

因此中心 R10 覆盖掩码应为 `C=E8(e0)|E8(e1)|E8(e2)`；三个叶分别为 `Li=E9(ei)|E7(ej)|E7(ek)`。四掩码都含全部1250旧点，精确等价于四个新根到全部旧点≤10。helpers之间距离为1或2，故没有遗漏 helper-to-helper 义务。

不能换成 R8 other-pins，也不能把每叶强行要求 own-pair R9 全覆盖。各单独删边球不等于 source 球，但上述 weighted minimum 等式成立；本全域 gate 依靠的是这个等式，而非错误的逐球不变假设。整对 cut 接同叶、cut 互不交是证明契约。

## 3. Closed-ball / bitset 实现契约

源闭球 DP 应从 R0(v)={v} 开始，每步保留当前集合再并邻点的前一层集合；只保存“长度恰好r的 walk”或忘记0步，不能直接当 Rr。对一条无向边，并两个端点的球得到 E_r；无需 source all-root D10 验证。

1250个 source labels 恰是1250bits。若用20个 uint64，则最后一块仅低34位有效（19*64+34=1250），其 ALL/tailmask 为 `(1ULL<<34)-1`。补集必须相对 ALL 取；不能把最后30个 padding 位计为 missing，亦不能因填了 padding 假称覆盖。所有根覆盖只比较 source-label universe，不混入1250..1253四个 helper labels。

centre或leaf在首失败槽早退时，未检查的槽应留 NOT_TESTED；不能说它们也失败。若所有1743779合法边对均被任一精确必要槽拒绝，可以严格关闭本架构；若尚有未访问域则 UNKNOWN。

## 4. 位集通过不是完整 graph hit

若任一 triple 四掩码全过，才构造其真实1254/1881 simple cubic 图：原1250/1875 source仅删三 cut；添六条 old-pin/leaf 边和三条 centre/leaf 边。必须给出实际完整边表、参数和真实四个新根 ordinary BFS，与精确掩码预测比较。

旧旧≤10仍需最终候选的全部旧根验收或另一完整证明。source geodesic 可能使用已删 cut；恢复其两端连通需经叶多走一步，四个新根覆盖不保证这种旧旧损伤已有替代路线。旧 A 的 D11 上界、旧 B/transfer 的失败、以及 source 本身 D10，都不自动完成这个旧旧阶段。若仅四根通过，状态只能是 NEW_ROOT_COVER_PASS，不能称完整(3,10)图。

root/bounded 的唯一全域窗口仍累计计入 fixed-stage 成本及新准备/执行，原定总30CPU不重置；本纸面 note 不授权第二窗口、第二 helper-tree 或其它 pin 分配。0图/参数/Lean计数变更。

## 5. 唯一实际终态的只读实现绑定

新文件实际前缀/目录是 `global_three_matching_gate/`，而非 FULL_*。代码已检查：候选边先排0/1端点，双层 i<j 再查两边不共享端点；闭球从 self 开始并前一层邻点集合；E[0/1/2]分别对应7/8/9；ALL末块34位；四槽公式与上文逐项一致。没有发现将 open ball、padding 或单球不变误作本门依据的问题。

实际 `ACTUAL_DOMAIN` 为1870条候选边、1743779合法 matching pairs。`RESULT` 的 visited 同为1743779；centre 调用/失败均1743779，其余三叶调用均0，四根全过0，候选 newroot BFS0、oldroot BFS0。`TERMINAL` 真实完成且退出0，累计3.511239973/30 CPU（含旧 fixed-stage1.916663729）；本读审不重新产生这些数值。

因此实际否定由**所有参数均有 centre 缺失旧目标**给出，结合 centre 精确公式和 anchor 完备性，足以严格关闭本文件定义的全部同源三 matching-cut／整对接叶／K1,3 helper 星形架构。不是只关固定第二 cut，也不是声称叶或旧旧实测失败；无需在已全 centre FAIL 后补跑它们。一般1254图、任意六 pin 的不同分组、P4、repair、其他 host 仍不在结论内。此终态不授权第二数值窗口。
