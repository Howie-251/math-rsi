# Actual3645：单旧边删除＋全部可用端点新星的历史读取门

本次限定历史读取未定位同源、全20,044条旧边的 one-cut＋F7 maximal-star 的既有严格NO或UNKNOWN终态。不是断言此前从未有人试过。现有645条插入层边建议确为该规则的子域，但原READ_GATE明确为未选择、未执行的提议，没有数值终态。本门只定位历史和数据，不解析源、不计算球、不枚举候选。

冻结源G为作者actual3645，m=20044，degree10有7点、degree11有3638点；D4沿用原作者与既有源验收。F=[3456,3489,3564,3571,3583,3603,3643]。唯一源输入是 `research/ddp/more_graphs_20261027/d11_D4_current3645/source3645.edges`，作者格式为带类型注释的无向边表，没有数字n/m首行；同目录 `source3645.header.edges` 只是增加 `3645 20044` 首行的格式副本。两者均含全部20,044条源边，不仅645条插入层边。标签为0..3644。原作者recipe为同目录 `construction.author.json`，metadata见 `SOURCE_PROFILE.json`。

下一规则仅删除一条实际旧边uv；P=F∪{u,v}去重；保留其余旧边，新增z=3645并连接P全部点。新点degree为|P|≤9，端点失一补一，其余F各加一，故maxdegree≤11。条件参数为n=3646、m=20044−1+|P|，本门未生成该图。因为两个cut端点都属于P，source中到P最近路径遇uv时可从下游端点重起，故d_(G−uv)(P,t)=d_G(P,t)。新根R4完整的精确条件是R3_G(F∪{u,v})覆盖全部3645点，等价于R3_G({u,v})覆盖已保存的743个F-union缺点。通过该条件后，旧点对D4仍需在实际候选中另验。本门不将必要的新根门当作完整3646图。

历史范围区分：

- `COVER_RESULT.json` 严格关闭保留全部源边的任意非空增点扩张；不排除删uv的新规则。
- `absorbed_pair_probe/RESULT.json` 的2673项删除两条原twin/line-host边，四端点加F7接新点；不是单cut。
- `absorbed_switch_probe/PLAN.md` 明确使用三条cut：沿47个保存反例产生paired-switch，并按degree上限选择free子集；679项并非全20,044个单cut。
- `redundant_vertex_buddy/REPORT.md` 是删一旧点加两helper且要求完整twin-square的另一规则。
- 上层原 `READ_GATE.json.next_single_falsifiable_question` 仅建议当前645条插入层边，并记录 `NOT_SELECTED`。它不是completed NO，也不是UNKNOWN计算。
- 普通degree2单边细分没有F7新星边，不等于本规则；不能将该范围的NO继承到此处。作者在历次旧图上的growth步骤也不是对最终3645源的完整全边终态。

可直接复用的数据位于原源目录：

- `absorbed_pair_probe/FREE_R3_CACHE.json` 与 `free_R3.u64le.bin`：F7的完整R3并集，已覆盖2902、缺743；JSON保存缺点标签。原严格证明见 `COVER_RESULT.json`。二进制按57个little-endian uint64，word j bit k对应vertex 64j+k，末尾padding为零。
- `absorbed_pair_probe/ENDPOINT_CACHE.json` 与 `endpoint_R3.u64le.bin`：1964个明确root标签的完整source R3，57 words/row；逐JSON的roots顺序绑定，不能按label直接偏移。
- `absorbed_switch_probe/NEW_R3_CACHE.json` 与 `new_R3.u64le.bin`：另29个明确root标签（含F7单球及22个switch端点），57 words/row。只能按实际标签合并缓存，不能把1964+29当成无重叠总根数，也不能假设201插入点全部已缓存。
- 全20,044边的唯一数据入口是上述raw/header源文件；本门不读取其边正文。后续唯一数值owner可只补实际未缓存endpoint的R3，不重源D4验收。

限定查询实际读取了原source canonical Wiki节点、459行ledger中包含3645的现存记录、原源两probe的范围文件、上层原READ_GATE与其恢复入口。未导入或重建Wiki。新增操作：web=0、sourceparse=0、binary球读取=0、BFS=0、候选=0、solver=0、Lean=0。此次one-cut历史定位保守read/prep费用0.5 CPU秒，作为读取费用保留，不作为数值批重置。此前preserved-edge recheck读取费用独立保留。停止本门；等待root另给全边实验预算，不自行跑645子域、换源或扩模板。

纸面接口入口已由gq保存：`research/ddp/more_graphs_20261027/d11_D4_current3645/ONE_CUT_STAR_INTERFACE.md`。
