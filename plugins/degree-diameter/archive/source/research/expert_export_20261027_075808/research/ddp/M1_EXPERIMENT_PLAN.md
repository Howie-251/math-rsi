# M1 finite profile: two-orbit 1+5 voltage graphs

2026-10-26. Goal remains a new lower bound, not closing this family.

Vertices (i,g), i=0,1 and g in a finite group. Within each orbit: right multiplication by respective nonidentity involution a,b. Across: (0,g) adjacent to (1,g*s), for five distinct s. This always gives a simple six-regular graph of order2q. Left multiplication is a proven free orbit action. Search uses exact radius3 BFS from both identity roots; candidate acceptance independently rebuilds all adjacency from saved edges and checks every root.

Baseline source has q60. Tested generator with recovered C5×A4 parameters: score0; independent full BFS n120,m360,degree6,diameter3. This check specifically validates the changed generator, not a new result. Target groups q64 give128 vertices, q72 give144, each above current120.

First profile: UT4(F2), D8×D8, Heisenberg(Z4), C6×A4; 60 seconds each, four single-thread processes, seed261026. Exact formula-defined groups, not all groups of these orders. Source baseline and group labeling in computations/ddp/m1/. Save best parameters and complete edges on improvement; terminal report at budget or score0; respond to SIGINT/SIGTERM. No proof logs. Stop the batch at its stated budget and analyze failures before extending it. Up to8 workers total across mechanisms; this profile uses4.

Independent derived obstacles will shape next generation: generalized dihedral groups cannot exceed56 fiber vertices in this template; no runs allocated there. Pure-A4 involutions for C_m×A4,m≥6 are excluded by quotient coverage; C6 half-turn involutions change this condition and remain allowed in this profile. Central involutions constrain q≤67. These are scoped local derivations pending proof review, not new DD lower bounds.

Implementation uses ARIS formula-derivation and experiment-bridge adapted to CPU graph construction. Reviewer is checking actual code and mathematical criterion in parallel with this short profile; baseline regression and all-source BFS already passed. No GPU/training/paper or generic artifact framework is needed.

## Feedback-driven next profile: change internal/cross degree allocation

First1+5 profiles terminated after60s each, with independent all-source BFS: UT4_2 has1024 bad pairs; D8×D8 has1536; Heis(Z4) has800; C6×A4 has792. All are simple6-regular, connected, diameter4, so none is a new(6,3) bound. Best scores were reached in the first0.02s and persisted for22–27million trials; adding unchanged seeds has little justification.

Change the actual generating condition to2+4 or3+3: arbitrary inverse-closed A,B of equal size r, cross set size6−r. For r2, odd-order groups are now allowed, unlike1+5 which needs an involution. In particular C7 semidirect C9 with action2 gives126vertices. Initial0.2s sanity has315 badpairs and independent BFS exactly matches the representative objective; degree6 and diameter4.

Next batch:120s each,6 workers: Meta_7_9_2 withr2/r4, Meta_31_2_30 withr2, UT4_2 withr2, Meta_8_8_3 withr2, C6×A4 withr2. These are finite profiles, no claim of exhaustive search. The purpose is to test changed route structure and identify joint coverage bottlenecks. Record full best edges and all-source validation. At termination analyze before more compute; new group/state definitions are explicit in make_extra_groups.py/search_split.cpp.

## Same M1 mechanism at (7,4), informed by actual recovered source

The6-degree second batch ended without success; all six best graphs independently have diameter4. The C7⋊C9 r2/r4 candidates both have315 badpairs, and the savedr2 quotient skeleton has a complete16807-translation check confirming best315. This does not exclude other skeletons; a bounded complete skeleton search is being profiled.

The684-point source is now fully recovered as two copies ofC38⋊C9, action23, with4 internal and3 cross neighbors. The generalized code (search_lift.cpp) recovers all-source distance histogram of the source:684,4788,28728,159372,274284. This degree7,D4 mechanism permits4-step routes; new candidate orders702 and720 arise from C13⋊C27 action3 andC15⋊C24 action2. These parameters satisfy r^k=1 and exceed684; group and edge rules remain exact.

Budget: two single-thread120s profiles, same finite save/stop protocol. Concurrent q63 exact task≤3CPU and M3 controllers≤3CPU keep aggregate≤8. This is a new parameter/application of the existing M1 mechanism, not a third main mechanism or a generic per-cell queue. After profile, explain actual failure rather than adding unchanged seeds.

## 702点修复终态与(5,5)精确构造入口

原702点(7,4)候选仍有1404坏对。全图低温switch未移动的原因是实际增量远高于温度；改为保留C13的54点简单商图、189个自由电压后，全部2268单电压邻居均变差，120s定向单/双电压退火也未改善。最佳和实际末态均从完整边表全根验证。该批结束，不增加原样seed；结果不排除整个C13电压族。

同一二轨道构造迁移到(5,5)，内部度2、跨度3、容许五步路线。702/720两张原图各4种直接删逆对共8例均失败。新数学规约通过共同内共轭消去一个F13变量，再缩放到P²(F13)，每个商骨架只需183项。商骨架72963项按明确同构归为1464；实际完整267912项中260922合法、6990非法，1464骨架全部完成，约4.07秒CPU。最小代表遗漏12，对应702点五正则图2106坏对、直径6；独立完整图BFS相符。合法数另由项目超平面容斥独立核算，每个骨架均一致。只关闭F13⋊C27 action3的指定2+3构造。

新的有据结构改变是使用忠实循环作用：原C27作用有C9中心核，改为F109⋊C3(action45)、F41⋊C8(action3)、F37⋊C9(action7)，作用阶恰为3/8/9，候选阶654/656/666，均大于最新650门槛。新群不含原来的非平凡作用核；并不声称“有中心就失败”，也不声称忠实作用保证成功。

同一共轭/缩放规约适用，每骨架p²+p+1项。原始生成完整保留，使用独立generic源码；偶数m时明确排除自逆内部生成元，避免单逆对被折成度1。三例商骨架分别9/173/240，候选上限107919/298079/337680。先用旧13/27/3回归同一结果，再三例顺序、总120CPU秒上限，保存每骨架完成度、所有最佳完整图及终态，成功立即独立验图。不增加额外p/m队列。当前状态以实际summary和handle为准。
