# 当前D3–D5主表：点数纪录长期未变的开放条目

2026-11-01实际读取Comellas主表及D3、D4、D5描述页。确认 **9格** 当前同点数已存在至少10年；若只取degree4..12则是8格。**没有确认5–9年备选**，不为凑表补未知年份。这里的“开放”按当前维护表未标optimal；不把“未证最优”说成“容易提高”。

优先给D4／D5选题参考，D3只列账，不启动degree梯子；N8/D2/n61暂停保持。

| 参数 | 当前n | 日期证据（不是页面更新时间） | 强度 | 当前状态 |
|---|---:|---|---|---|
| (3,5) | 70 | 至迟1983年底已列；2024/2026只是同阶重构 | firstknownbyyear | 未标optimal |
| (4,5) | 364 | 保守至迟1983年底已列；当前页另明确追溯Delorme1981 | firstknownbyyear；另有作者年1981归属 | 未标optimal |
| (8,4) | 1100 | Loz于2006年7月communicated；2023同阶实例不重置 | 作者年月 | 未标optimal |
| (4,3) | 41 | Allwright1992论文已给当前41；未核首发现日 | firstknownbyyear | 未标optimal |
| (5,3) | 72 | Exoo明确1998-05-22communicated | exactdate | 未标optimal |
| (8,3) | 253 | Comellas–Mitjana明确08/1994；另有1996网页快照 | 作者年月 | 未标optimal |
| (9,3) | 585 | Delorme原文Table2截至1983末已列同值 | firstknownbyyear | 未标optimal |
| (10,3) | 650 | 同一1983末表已列同值 | firstknownbyyear | 未标optimal |
| (11,3) | 715 | 同一1983末表已列同值 | firstknownbyyear | 未标optimal |

[当前主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) · [D3实际条目](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html) · [D4实际条目](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html) · [D5实际条目](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html)。1983末同点数的直接依据是[Delorme1985原论文Table2／p301](https://web.mat.upc.edu/francesc.comellas/delta-d/old-files/delta-d/papers/81981341.pdf#page=11)，不是因为该族“发表于1985”就假定所有值首次出现于1985。作者所说截至1983末说明known-by上界，未声称精确最后提升日就是1983。

## 四个特别容易误记的条目

- **41／(4,3)**：当前D3条目确实把41和13张非同构图归给Allwright1992（DAM37/38,pp3–8）。2026年10月另加三张41点图并未把点数提高。原publisher全文本次403，因此只说“至迟1992”，不猜更早发现日。
- **364／(4,5)**：当前维护页明确写Delorme1981、指Bermond–Bollobás1981survey p11，后列1984／1985文献；1981原文入口未成功完整取读，本表保守用实际原论文截至1983末的364。无论哪一层，都不能按1985当第一次提高日期。
- **70／(3,5)**：vonConta1983／Alegre–Fiol–Yebra1986是原条目文献；1983末表已经有70。Comellas2024的Coxeter构造与2026的Bosák构造是同阶重构，不能当2026数值新纪录。
- **额外专项132／(3,6)**：[当前D6条目](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g6.html#36)本次明确读到Exoo1998-05-22communicated132；2001是后续论文，2025增加132点非同构实例，都不重置数值纪录。本项只回应用户专项，不扩为D6全表扫描，也不计入上述9格。

已经证明optimal的(3,3)=20和(3,4)=38排除；后者维护页还明确给Buset2000最优性证明。另须排当前2026新提升：(7,3)=170是2026-09-30新值，旧168的2005记录及2011“Cayley最优”不能套给一般图170；(4,4)=104也已在2026提高，不能继续选旧98／2010。其它主表新大值若与描述页旧值不一致，不用旧描述页年份计算新值的停滞时间。

## 不是“以前没试过”：本地已关范围和UNKNOWN

- **(8,4)=1100**：固定72控制图／global F2⁴／offset全0的规范族已经完整关闭：2419200输入筛出1024，全部完整R4失败。逐边自由映射两起点失败不是整族排除；不能机械重启已经全关的offset0模板。 [ddp-wave11-binary72-tight-words.md](../../../../research-wiki/experiments/ddp-wave11-binary72-tight-words.md) · [ddp-wave10-binary1152-edge-local.md](../../../../research-wiki/experiments/ddp-wave10-binary1152-edge-local.md)
- **(4,5)=364**：自然364点714边host的28个degree3ports，在保留全部旧边、不加old-old边条件下，1..13helpers已全部排除；k14未查、该host逐阶长尾STOP。任意重连、其它host、一般365..377图并未被排除。另有固定SL2(F3)×C8和Allwright41的C9覆盖模板排除。 [ddp-h3-364-helper-minimum13-20261027.md](../../../../research-wiki/experiments/ddp-h3-364-helper-minimum13-20261027.md) · [ddp-h3-helper13-tree-class-exclusion-20261027.md](../../../../research-wiki/experiments/ddp-h3-helper13-tree-class-exclusion-20261027.md) · [ddp-wave2-sl23-c8-biorbit384-d5.md](../../../../research-wiki/experiments/ddp-wave2-sl23-c8-biorbit384-d5.md) · [ddp-wave6-cyclic-cover369.md](../../../../research-wiki/experiments/ddp-wave6-cyclic-cover369.md)
- **(3,5)=70**：本次有限Wiki标题／目标行扫描未定位专门提高70的本地实验；70作为另一个D6 twofold问题的源不等于本题已排或未被所有人尝试。 [REPORT.md](../../more_graphs_20261027/cubic_D6_twofold70/REPORT.md)
- **(4,3)=41**：相邻单点拆分42且完整邻集互斥分配规则由36<42排除；固定Allwright1(a)的F5／F4 affine-line transfer和C9覆盖也已关闭。一般42点图没有被这些结论排除。 [REPORT.md](../../more_graphs_20261027/d3_vertex_split/REPORT.md) · [REPORT.md](../../refresh_20261029/controller41_transfer_gate/REPORT.md) · [REPORT.md](../../breadth_20261027_wave6/cyclic_cover369/REPORT.md)
- **(5,3)=72**：clean split73由59<73排除；固定Exoo72的删三条不交边／新root接五pins规则完整4992120项无覆盖；Exoo／Michel源的clean-split+absorbed-edge也各自关闭。GQ80 paired-matchings仍UNKNOWN、该批已停，不写成不可行。 [ddp-exoo72-minimal73-rootcover-20261027.md](../../../../research-wiki/experiments/ddp-exoo72-minimal73-rootcover-20261027.md) · [ddp-wave11-gq80-paired-matchings.md](../../../../research-wiki/experiments/ddp-wave11-gq80-paired-matchings.md) · [REPORT.md](../../more_graphs_20261027/d3_vertex_split/REPORT.md)
- **(8,3)=253**：固定CM253的相邻拆分254全部32131分割无通过；固定F7³ polynomial343加一个partial complementary matching已严格被B3≤302<343排除，不再是UNKNOWN。其它一般(8,3)图仍开放。 [REPORT.md](../../more_graphs_20261027/d3_vertex_split/REPORT.md) · [ddp-wave11-polynomial343-matching-scout.md](../../../../research-wiki/experiments/ddp-wave11-polynomial343-matching-scout.md) · [ddp-wave5-binary-route-chart3.md](../../../../research-wiki/experiments/ddp-wave5-binary-route-chart3.md)

这些只是已有工作查重摘要，没有重跑数学、图、BFS、field、solver或Lean。旧题保持久可能反映真实结构障碍或搜索难度；开放不保证有简单的补点／复制办法，也不把固定scope失败当全参数不可能。完整JSON保存当前42个单元的点数快照、9个日期证据、专项132和原链接；未核的精确firstdate保留unknown。
