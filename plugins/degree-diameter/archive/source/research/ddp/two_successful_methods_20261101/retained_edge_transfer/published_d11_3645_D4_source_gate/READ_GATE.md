# (11,4)3645：实际源与旧范围读取门

结论：完整实际源早已缓存，且七个 free 点的保边补点路线已被严格排除；本轮不需 HTTP，不重做 degree profile、source D4、BFS、field 或求解。

源来自 [Nishant Bhakar 的作者目录](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg11/dia4)。原始 [README](https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg11/dia4/README.md) 明确是 Dharunish Yugeswardeenoo 的 W(9) incidence double／spread-twin 基图3444，经201次 absorbed-deletion insertions 得到3645。不是从3645=45·81猜出的 affine chart，也不是 reflection 模型。作者源码入口为 [search/insert_grow](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/search/insert_grow)；该 order 的首次达到日期本次材料未确认，不拿缓存日期替代。

本地原始文件在 `research/ddp/more_graphs_20261027/d11_D4_current3645/`：`source3645.edges` 是带类型注释的作者20044边表、无数字header；`source3645.header.edges` 仅格式补3645/20044 header。`construction.author.json` 为实际显式边表 recipe，`insertions.author.txt` 保存201步，`README.author.md` 和 `verification.author.txt` 保存原作者说明与验证。本轮没有解析边表。当前3645主表值继承 root 刚完成的 primary 核对，本地2026-10-27 BASELINE也为3645；desc_g4仍写旧3444的历史滞后，不应用低门槛。

## 已知结构和余度

继承 `SOURCE_PROFILE.json`：n3645/m20044，degree11有3638点、degree10有7点。唯一free为

`3456,3489,3564,3571,3583,3603,3643`。

它们全在3444..3644的201插入层；3444个原类型点均饱和11度。插入层内有645边。当前前3444点 induced 只有18485边，原11regular基图的457边已删，不能把原 W(9) 完整方块/覆盖性质直接套给当前图。旧 contiguous81分块全部不equitable；没有据此排除任意其他重标分块。

## 不能再跑的旧严格域

`COVER_RESULT.json` 已精确给七free闭R3并集2902点、遗漏743个原基图点；首漏6距全部七free均4。任何保留所有source旧边的cap11新点扩张，即使允许多helpers及额外旧旧边，也必须通过原free进入旧源。取新点到6的路上最后一条非source边，其旧端为free，剩余至多3条旧步，因此不可能R4到6。这是严格全保边范围NO，不是仅某个7pin星形的样本失败。

另继承三项准确旧范围，均不重跑：

- 原 twin/line host 两边吸收2673项：2626新根失败，47新根通过后旧旧失败。
- 由这47项firstbad导出的一条现存copy-switch规则：679实际项，541新根失败、138旧旧失败；不是所有switch或所有第三删边。
- 删除冗余旧点、双helpers的 intact twin/line-square入口：当前完整结构0例；不是任意删点构造NO。

## 已有R3接口与未选的历史猜测

`absorbed_pair_probe/free_R3.u64le.bin` 保存七free联合球，`FREE_R3_CACHE.json` 含743缺点；`endpoint_R3.u64le.bin` / `ENDPOINT_CACHE.json` 保存1964个明确label根、每行57个u64；`absorbed_switch_probe/new_R3.u64le.bin` / `NEW_R3_CACHE.json` 保存另29根（7free单球和22switch端点）。使用前按label查根，不假设全201插入层球已备齐。`HOST_BINDING.json` 保存作者原host映射，不能因有该映射而恢复已删边。

若 root 仍选此源，只有一个小而可推翻的下一覆盖问题：当前645条插入层旧边中，是否有 uv 的源闭R3端点并集补齐上述743缺点？若有，删 uv 并使新点连 `{u,v}∪free7`，由于删边两端均为pins，源R3覆盖就是新根R4的精确条件。此域不同于已闭两host边与firstbad-derived switch域；有限旧范围检索未定位全645层边的已完成同门回执。作者原方法本来就是 absorbed-deletion，不能把这个复用问题称新方法或保证能推进。

这只是下次可证伪的猜测，本轮未枚边、算球或验证候选。即使新根覆盖通过，仍需删除该边的旧旧义务；只有其crit4为0或实际候选的完整旧旧证明才能提升到合法3646图。所需新数据应限制为缓存未覆盖的端点R3支持及命中后的旧路线义务，不是source D4重验。若该门全失败就停该具体域，不据此扩大为所有3646图NO。

本轮只创建本门 READ_GATE.md/json；0网络请求/源解析/新profile/BFS/field/solver/图/Lean/外审，保守计读取整理1.0 CPU秒，cap5。停止，任何后续数值需 root 另定基于实际接口的范围。

root 最新决定：3645读门到此停止；上面的645层边猜测未获数值授权，本轮不选、不启动。下一题另属two684/K19读取门，不把此未测猜测登记为新失败域。
