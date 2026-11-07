# 饱和源的局部增点、全点对修复与有限编辑重放

这条路线接现有 dd-construction、dd-transfer-diagnosis 与 dd-obstruction-certificate，不另开调度器。触发是：源已达到当前 degree cap，保边增点没有合法 pins，但当前任务允许删除／替换旧边。真实正向实例是 MathRSI **v2 + DD + PR7 handoff repair** 得到的 (10,4) 2567 图；v4吸收工具，不改写执行归属。[原运行版本](../archive/pr11-2567/case-studies/degree-diameter/evidence/execution_version.md)与[原构造说明](../archive/pr11-2567/case-studies/degree-diameter/reproduce/d10_d4/README.md)保留完整依据。

## 1. 输入与实际操作的合法性

从父route/prove接收：实际简单无向源G（标签、边集格式、孤立点也计入的顶点集）、cap d、目标D、允许的旧边修改、当前源距离证据、一个候选matching M以及当前任务写域。源D不明确不妨碍试候选，但不能进口它的全部旧距离结论。先检查M中每条确为源边、端点两两不同，新标签z不在旧顶点集，`2|M|≤d`。这里的一次增点不是任意重接，也不是冻结完整N克隆。

令U为M的全部端点，定义实际新图

`V(H)=V(G) ⊔ {z}`，`E(H)=(E(G)\M) ∪ {{z,u}:u∈U}`。

**度数与简单性引理。** 每个旧端点删一边再加一边，度数不变；非端点不变；新点度`2|M|`。因此旧最大度≤d且`2|M|≤d`时H最大度≤d。因为源简单、M是matching、z是新点，新增边互异且无loop。阶增1、边数增`|M|`。特别是偶数d的d正则源，取`|M|=d/2`，新图仍d正则。奇数d或不足大小matching不自动给d正则；只能按实际度数说结论。证毕。

**距离义务是独立的。** 上述引理没有证明任何D界。新点到旧v的距离满足 `dist_H(z,v)=1+min_{u∈U}dist_{G\M}(u,v)`（存在时）；必须在删边后的旧图计球，不能用源G旧球替代。旧点对可经z绕行，也可能因删边变远，故新根覆盖只是必要一部分。完整验收可选当前literal图全根BFS，或覆盖所有old-old和new-old的数学路径/可靠证书；不能仅凭degree和新根通过收卷。

### 需要时做 old-only 2-switch

在当前H选旧点a,b,c,e（四点互异），现有旧边ab、ce，候选旧非边ac、be；删除前两条并加入后两条。逐条核存在／不存在、标签仍为旧点，故每个旧点度数保持、新星不变、简单性保持。其它配对可以研究，但必须写实际四点及边集合，不能只记“做了switch”。对switch后的最终图重新接距离义务；前一步已验距不能自动继承。

这项操作是有用候选机制而非任意源都可增点的定理。找不到matching只否定所试选择；没有完整匹配域枚举就不写NO。切换源或允许新操作后，父transfer-diagnosis重判旧排除的假设。

## 2. 用失败点对改变下一次局部选择

在当前任务先保存source身份与候选完整边delta，再评估合法性。格式错误返回缺的源边／重复端点／已有新边与具体标签，修输入或操作，别交距离优化器。新图度数超cap返回该顶点及增删贡献；不能以坏对少掩盖不合法。

距离探针返回实际坏对(u,v)、它属于new-old还是old-old、当前距离（或明确无≤D路线）、被删边及原短路径（若已找到）。若只测了部分roots，要同时返回测过roots和未覆盖域；超时不是全域失败或通过。坏对计数可排序候选，但最终验收消费的是完整覆盖。

- new-old失败：在实际删边图恢复U的球并，找漏点；改变切边／端点覆盖，不能仅增加非法pins。
- old-old失败：读那对原路径用了哪些cut，尝试另一条matching边或合法old-only 2-switch，给出该pair的新实际路径；同时保留已经通过new-root的义务，不把它当整个图通过。
- 修一对又坏另一对：在**同一最终邻接**上联合测试这些见证，保留整组反例驱动下一次选择。不得把不同候选各自的成功路径拼成同一图的证据。

每次候选按当前任务预算决定筛选roots、完整检查或数学归约，插件不内置历史搜索次数。精确反例直接回父prove当前图修改；相同坏对反复出现时回route重新选择操作／源，不只扩大种子。命中完整图后按原目标交verify，不自动继续更大阶梯。

本PR说明失败点对引导后续切边选择，但未包含完整搜索轨迹或搜索器。因此这里只吸收有依据的诊断动作，**不提供可复跑原发现搜索或效率提升的声称**。旧“小源cut-star新根过、old-old坏”的反例仍有效，它反对错误继承，不排这次完整检查通过的图。

## 3. 真实十图链与最小重放

[只读来源](../archive/pr11-2567/SOURCE.md)及[清单](../archive/pr11-2567/MANIFEST.json)自包含在插件，不依赖网站开发目录。源是发布的2557顶点输入，十步产出2558…2567；公共表比较的2566不是该seed。每步cut五条matching边并连十端点；**只有生成2565和2566的步骤额外old-only 2-switch**。最终从本地2566删

`(193,2362), (192,2363), (417,2555), (2508,2565), (2511,2528)`，

新增标签2566连十端点，无后继switch。最终2567点、12835边、10正则。示意图见[原SVG](../archive/pr11-2567/case-studies/degree-diameter/assets/construction_d10_d4.svg)，图只解释实际delta，不是完整邻接图。

先读原[reproduce.py](../archive/pr11-2567/case-studies/degree-diameter/reproduce/d10_d4/reproduce.py)与[edits.json](../archive/pr11-2567/case-studies/degree-diameter/reproduce/d10_d4/edits.json)。脚本仅标准库：解压源、检查源大小/每步删除存在和新增非边、执行literal delta、检查边数并写排序边表。它不会搜索、访问网络、验距或编译Lean。源/edits由脚本自身路径定位，历史绝对路径只是归属信息，不会读取。

从**当前任务目录**执行，设置当前克隆的插件真实路径：

```sh
DD_PLUGIN="/path/to/MathRSI/plugins/degree-diameter"
TASK_DIR=$(pwd -P)
run_dir=$(mktemp -d "$TASK_DIR/dd-finite-edit.XXXXXX")
python3 -B "$DD_PLUGIN/archive/pr11-2567/case-studies/degree-diameter/reproduce/d10_d4/reproduce.py" \
  --all --output-dir "$run_dir/graphs"
```

只要最终图时改用 `--order 2567 --output "$run_dir/g2567.edges"`；两种选择互斥。输出首行`n m`，后每行一个无序边，标签`0..n−1`。十图m依次12790…12835，每步增5。新任务的source/delta不同，就在任务目录保存自己的输入和配方，不能改只读归档冒作历史图。

非零退出时返回实际exception和首个不适用step，读压缩source／delta／格式；不自动启动原大搜索或拿旧receipt覆盖错误。退出0只说明这份有限编辑成功，未独立验证matching／regular／D。父prove消费生成图与精确delta；父verify按当前任务缺口选literal绑定、全点对或形式化，不重复把重建当数学验收。

## 4. 怎样消费历史证据而不升级状态

[十图原BFS收据](../archive/pr11-2567/case-studies/degree-diameter/reproduce/verification/d10_d4/README.md)保存2558…2567每个literal图全部roots检查。最终记录2567根，6,589,489 ordered含对角／3,293,461无序异点对，diameter=4，distance-four见证(0,2)，不调用producer缓存或source距离进口。重放是生成相同配方；本轮没有重新执行这些BFS。

[原出版重放记录](../archive/pr11-2567/case-studies/degree-diameter/reproduce/verification/D10_D4_SOURCE_REPLAY.json)另记十图完整无序边集与accepted originals匹配。当前克隆未包含这些独立accepted edgefiles，不能把新重建／header检查说成再次全边比对。

原[Lean收据](../archive/pr11-2567/case-studies/degree-diameter/reproduce/verification/d10_d4/n2567_ROOT_GRAPH_RELEASE.json)记录2558和2567的具体原目标kernel与独立import；2559…2566无另计completed concrete Lean条目。2567传递公理为propext、Classical.choice、Quot.sound；原Fin目标无条件。最终外部[formal C仍INCOMPLETE](../archive/pr11-2567/case-studies/degree-diameter/reproduce/verification/d10_d4/n2567_FORMAL_C_DISPOSITION.md)，不能写ABC全过。仅收据、无完整Lean工程/依赖，不能从本插件独立重build这项证明。

prepare/survey可消费“2026-11-05 Comellas2566→2567”这一有日期比较；公开优先权与最优性未确认。累计163实例/44参数对/49具体Lean是历史目录总数，早153归ARIS，新十图归v2+DD。换日期／新竞争目标先用当前survey，不能把旧表永久当最好。

## 5. 当前任务wiki与返回点

沿用任务现有wiki命名，至少将这次真实对象、cut/switch差分、当前源身份、引理假设、失败点对/其scope、真实argv/exit、已覆盖及未覆盖pairs、历史进口与新检查分别接到对应实体。已有wiki就更新同一图和失败实体，别为每次重放建一个平行“主状态”。下一步由父任务消费：

- route收到合法但反复同坏对：改候选操作或源，保留未排域；
- prove收到完整图：装配degree引理与all-pair义务，精确D另有见证；
- verify收到replay输出：分清本轮生成／literal核查与历史BFS/kernel/import；
- handoff引用规范结论及可运行插件路径，继续保留formal C未完与Lean缺工程的准确范围。

一次成功的cut-star不自动推广任意d/D；可迁移的是度数引理、共同最终邻接上的修复动作与薄replay入口。新研究成果在任务wiki积累，达到可复用证据后交外层meta-evolve维护插件，不在内层研究改base。
