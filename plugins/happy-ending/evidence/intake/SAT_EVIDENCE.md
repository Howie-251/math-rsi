# Happy Ending：756 SAT 证据摄取（2026-11-04）

本次为原包只读理解与证据边界核对，没有恢复研究、运行 SAT solver、重放大型证明或编译 Lean。源根为 `mathrsi_new_results/happy ending problem/n7-upper-bounds-20261103/`；下文 `P` 指其 `working/package/proofs/sat-756/`。主阅读入口是源根的 `source/report.md`，不是历史首页。本记录不把收据中的 PASS 改写为本次重新验证通过。

## 结论与范围

报告的基础结果是：对所有有限、完整、有序 rank-3 signotope，若无蓝色 5 点路径、红色 6 点路径与 weak 7，则顶点数至多 25。因此 `N(7,5,6) ≤ 25`；包内另有完整 25 点抽象染色见证及历史无 solver 核验记录，合成 `N(7,5,6)=25`。报告还引用经典几何构造，得到 `N_geo(7,5,6)=25`。这里的 N 是**最大避免规模**，对应强迫阈值为 26。25 不能误读为原始 ES(7) 的强迫阈值。

上界的性质是“数学归约 + 55 单元历史 SAT 证明检查”，不是纯手算证明，也不是这个项目的端到端 Lean 定理。该包能够说明归约、展示编码源码、追踪历史检查与人类接受链，但**不能单独重放这 55 份不可满足证书**。原始大文件仍指向 Linux `/data/ktqiu_hdd/math_agent/...`；本次未访问该服务器或断言这些远端文件今天仍存在。

更大参数的 40、50、76、77 和 ES(7)≤78 是报告后续结构证明的结果，不是 55 份 CNF 各自直接证明的结论；本子任务没有验收那些结构证明。

## 55 个单元如何覆盖所有原始输入

对末对 `(u,v)` 取两色最长路径长度减一，形成 `σ(u,v)`；顶点状态 `D(v)` 为这些末对剖面的向下闭包。禁蓝5、红6使状态落在 `[3]×[4]`，共有35种。不同顶点状态不同：若 `u<v` 且 `σ(u,v)∈D(u)`，某个前驱末对逐坐标支配它，而 `(t,u,v)` 的颜色必延长其中一种路径，矛盾。这个注入论证用完整三元组染色和路径递推；signotope／weak7并不是该注入本身的前提。

35种状态中普通25种、异常10种。异常列高条件为 `h1=4, h3≥1`，对应蓝4、红5路径共用**右端点**；两条路径起点可以不同，不能直接当成 weak7。令 e 为已占用异常**类型**数，m 为缺失普通类型数，注入给出 `|X|=25+e−m`。

第 r 层 `C_r: e≥r ⇒ m≥r`。若前层成立而本层失败，则 `m=r−1`；固定 `e∈{r,…,10}` 后，`N=26+e−r`。于是反例全落在 `A[r,e]`，`1≤r≤e≤10`，共55单元。全部行归纳得到 `m≥e`，所以 N≤25。`E01/cardinality-layer-theorem.md` 也记录更弱的数值捷径：十个 N26 对角单元排除，再由遗传性限制到26点并**重新计算**状态，可得 N≤25；它不能替代完整55单元对所有 C_r 的证明。

本次机械检查了 `55-case-register.json`：55条、无重复或缺失的 `(r,e)`，每项都满足 N 公式。登记分类全为 `VERIFIED_UNSAT`。这只是索引覆盖和字段一致性检查，未读取 CNF 或证明主体。

## 从真实 signotope 到 CNF 的桥

实际源码主要是 E03 `erdos.py`／`sat_tseitin.py`、E04 `downset_state_cnf.py`、E05 `cardinality_layers.py`、E06 `f3_main_rank.py` 和 E23 compact 两模块。核心编码已按所列函数阅读，并与 E01、E07、E23 的数学说明对照。

- 三元组变量按字典序组合首先分配，true=red，false=blue。旧 clause-group 名称 `no_red_5_path`／`no_blue_6_path` 与该实际极性相反，不能用标签推断颜色。
- `etv_signotope(7,5,6,N)` 包含真正的两色路径禁止、weak7禁止和四点包；不是移除 target 后用于发现的 `etv_signotope_extension`。每四点包的六条蕴含正是颜色序列至多一次换色。
- 旧 base 记录外端点 cap/cup 与固定起点／末前驱等路径存在辅助量，正反定义配合传播规则。单色路径保端点缩短由 signotope 给出，负责满足 base 的路径单调性；在蓝≤4、红≤5的范围内，唯一非冗余 weak7 组合为同外端点蓝4／红5。没有额外“内部不交”假设，也没有固定首三元组颜色的对称破缺。
- 独立 terminal 递推精确定义“长度 d 且最后两点为 u,v”；长度2为真，长度d由所有前驱的 `(旧terminal ∧ 三元组该色)` 析取。状态格点精确定义为同一个末对能同时支持相应蓝／红阈值。S 为12格精确位型，O 为 `∨_v S[v,H]`。四个串接且辅助ID不碰撞的 totalizer at-most 编码分别约束 e、10−e、m、25−m，从而等于要求的 e/m。
- compact 不是简单删去定义再照旧计数。其外路径标记只是单向闭包，用于禁止实际坏路径；计数另保留精确 terminal。`F_v↔(蓝4终于v)∧(红5终于v)` 精确，注入使 `sum F_v` 等于异常类型数，`m=25+e−N` 随之确定。E23 给出错误地计数单向外路径标记的具体7点反例。
- bridges 是由实际状态格点与下一三元组颜色推出的额外蕴含；F3 是已占用状态的包含关系在顶点顺序上的必要秩界。固定状态 H 的真子集只能出现在该顶点之前，真超集只能在之后，故数量≤v−1／N−v。源码使用1基顶点；E17 保存的 erratum 修正旧“零基等价”的文字，不改公式。

使用 UNSAT 的关键方向是：**每个真实数学反例都有满足完整 CNF 的辅助扩展**，而不是只有“SAT赋值解码后看来合理”。E01 Lemma4、E07 与 E23 分别陈述这项 all-order 投影／lifting 义务；bounded SAT 测试只是辅助证据。附加剪枝必须对真实输入成立，并绑定具体生成的 CNF。当前编码源码不等于所有历史封存编码；40条记录的 `encoding` 字段甚至明确是 `not_explicit_in_row`。

## 此包实际有什么，缺什么

| 项目 | 包内实际状态 | 本次判断的意义 |
|---|---|---|
| 55单元索引 | JSON/CSV，完整55三角域，含原路径、散列、字节数、原始收据字段 | 可追踪历史绑定；不是证书本体 |
| 55份原始CNF | 全部 `cnf_local_available=false`；本包及交付zip均无 `.cnf` | 无法本地逐份检查／比较生成字节 |
| 55份原始证明 | 全部 `proof_local_available=false`；无 `.proof/.drat/.lrat/.gratl/.gratp` | 无法本地重放UNSAT |
| 证明检查器 | 索引列出10个历史可执行路径；无对应二进制、C/C++或检查器源码 | 无法审核实际检查器实现或运行历史同版本 |
| 核心Python源码 | exact、compact、bridges、F3主要模块可读 | 可理解编码；不是完整可运行历史环境 |
| 完整生成闭包 | `state_charging/corpus.py`、`obligations.py`等进口未随P提供；历史多个封存runtime仍外部 | 无法把源码直接当作完整可重建的全部55单元发布包 |
| 小型历史原件 | E10–E19行收据；E20 A88 checker.out/exit、generator/seal；E21 solver.out与25点数据 | 比纯总结更具体，但仍须区分记录和本次执行 |
| 25点抽象见证 | P/color.tsv及E21副本，2300条；两副本逐字节相同 | 下界可独立小型重验 |
| 25点平面坐标 | 本包未见 `restricted_25_points.json`；只在Schroeder比较材料中提及 | `N_geo≥25`依赖引用构造，不是本包的坐标复验 |

索引记载 CNF 合计 **1,772,639,502 bytes**，证明合计 **3,878,666,467,578 bytes**（约3.879 TB，按登记相加，未读大文件；没有未知字节字段）。全源目录扫描及两个zip目录扫描均未发现隐藏的原CNF／证明／检查器主体；交付zip只有282文件，不能按“有zip”推断大证书已包含。

`EXTERNAL-MATERIALS.tsv` 有220行（55×CNF/证明/检查器/收据），只有 A[8,8]收据有非空 `package_path`，指向 E20/verification_result.json。注册表45条 `checker_receipt_local_available=true` 是继承的历史盘点字段，**不等于45份独立检查日志已在这个包中**。P 实际仅两份 `.out`：E20/checker.out、E21/solver.out；其余不少检查结果嵌在源行 JSON，或只给外部路径与散列。

`evidence-manifest.json` 的95项全部标记本地可得，它枚举的是这95份小型源码／文档／收据原件，并未枚举为“已打包”的55份CNF和DRAT。`case-register-validation.json` 自己明确写着 `Proof/CNF bytes were not read`。本次没有做一轮95项散列审计，也没有把其历史验证声明升级为独立证书检查。

## 历史检查链的实际强度

E10–E14保存C1到C5的接受收据，分别记录接受时fresh checker replay为5、9、8、7、6，并有byte-equal重建字段。C1的最终10单元包括此前已检查结果的复用，所以“该次fresh=5”不是只有5例被历史检查。E15(C6)复用5个既有checked case，fresh=0；E16(C7)复用4个，fresh=0；E17(C8)复用3个，fresh=0；E18(C9/C10)复用5个，fresh=0，其中含A[8,9]/A[8,10]的较窄前置。它们不应统称“接受时又重新跑完55份”。

这些后期接受记录公开写明人类授权复用、若干164项外部历史依赖未再次导出／验核、review为provisional或same-family/provisional、实际backend/effort未知等。人类接受不是新机器证明，也不是跨家族证明审阅。它们并未声称原始case从未检查，而是明确当前接受沿用既有case结果。

A[8,8]特别保留了独立GRAT路线的小型原始收据：E20/checker.out含精确 `s VERIFIED UNSAT`，checker.exit记录returncode0、实际执行argv、约7909.816秒、约251.702 GiB峰值；generator约172601.116秒。原CNF约21.16 MB、原DRAT约235.73 GB、GRATL约21.74 GB、GRATP约96.43 GB仍外部。E20的`row_acceptance=false/theorem_credit=false/accepted_bound=26`是**单元检查阶段**范围；后来的E17完成C8行接受才把总范围更新至25，二者不是互相矛盾。此结果没有在本次重放。

## 25点下界与便携检查

P/color.tsv明确列出全部 `choose(25,3)=2300` 三元组，1=red，0=blue。历史 `verification.json`／`portable-verification.json` 记录：全部 `choose(25,4)=12650` 四点包合法；最长蓝路径4、红路径5；300对外端点无蓝4／红5冲突；25状态互异、35/25/10目录、e=m=9、计数恒等式成立。这里e=m=9的见证也说明“所有异常状态都不可能出现”不是上界论证。

E21/lower_bound_verify.py从原solver.out最先分配的1…2300变量提取颜色，说明了来源映射；P/verify_color.py则只需TSV和标准库，无solver。后者先检查TSV无重复／缺失，按末对动态规划计算最长路径，并保存固定起点集合检测weak7。只有蓝4+红5需要检查，因为其它长度和9组合被蓝5／红6禁形排除。

本机为Darwin，提供的脚本显式断言Linux且会在脚本旁写portable-verification.json。本次没有删除平台断言、没有覆写历史收据，也没有把历史PASS称为fresh replay。原包文档提供的安全复验方式是：把 `verify_color.py` 和 `color.tsv` 复制到**独立Linux临时目录**，在那里运行：

```sh
python3 verify_color.py color.tsv
```

这只重验下界，不证明上界、不证明该抽象染色可由平面坐标实现。若重做上界，必须先取得各单元对应的原CNF、原证明、检查器及封存生成闭包；不能拿当前默认F3生成器配全部旧DRAT。E20保留可重放原理的历史命令形式为：

```text
gratchk @MLton max-heap 254g -- unsat ORIGINAL.cnf proof.gratl proof.gratp
```

该命令的三个大输入和历史工具未在此包提供，本次没有执行。旧compact命令和exact API说明可在E23找到；它们明确依赖匹配的历史runtime／Linux环境，不是解压此包即可使用的统一重建命令。

## Lean／比较材料隔离

P仅有两个 `.lean`，都在E32，导入ES7OrderedData／ES7LRAT或ES7CoverageData等本包不含的模块，属于Schroeder对照材料的摘录。E30 main.tex、README写作者Michael Schroeder，自己的端点为ES7≤81／ES8≤319，并声明使用native evaluation。E33提及其完整208模块、C++重放、平面25点坐标，这些被引用的主体没有一并纳入本项目包。不能把这些字段写成“本项目55单元或ES7≤78已有Lean”。本次未评估该比较工作的完整形式化包，也未核实其公开发布状态。

## 实际阅读与机械核对范围

完整阅读／解析：源根source/report.md；P的README.md、verify_color.py、verification.json、portable-verification.json、55-case-register.json（解析字段与嵌入原行）、case-register-validation.json、evidence-manifest.json（目录字段）、EXTERNAL-MATERIALS.tsv；E01/cardinality-layer-theorem.md；E07两份编码说明；E23/README.md、COMPACT_CARDINALITY.md、compact_cardinality_cnf.py；E21/lower_bound_verify.py；E20/completion_report.md、verification_result.json、seal.json、checker.exit.json、checker.out；E17/review_notation_erratum.md、campaign_acceptance_audit.json；E32两份Lean摘录；E33/README.md。

定向源码／收据阅读：E03/erdos.py的base/path/target/packet部分、sat_tseitin.py的变量分配／Tseitin AND/OR／assert／implies核心；E04 terminal/cell/state/occupancy函数；E05 exact e/m、bridges及生成入口；E06完整F3核心；E10–E18各campaign_acceptance_audit的字段与复用边界；E08 methods-and-results的C1/C2检查历史段；E23/semantic-encoding说明中的投影与部署合同、compact_cardinality.py的导入与命令入口；E30/README.md、main.tex／heptagons.tex／references.tex相关比较与下界段落；E40旧盘点摘要。未声称通读E09长研究日志、全部原始盘点1713项、封存Linux运行闭包或所有Python模块的每一行。

机械核对：55三角域／N恒等式／字段统计；P文件后缀与全源树可见文件盘点；两个zip中央目录；外部表包内路径字段；上下界颜色数据副本字节相同；导入缺件。统计另存`sat/register-summary.json`。无数学求解／证明检查器执行。
