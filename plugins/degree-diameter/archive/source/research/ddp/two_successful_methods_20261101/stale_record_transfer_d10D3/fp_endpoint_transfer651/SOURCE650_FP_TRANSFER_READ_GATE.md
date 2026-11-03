# Actual (10,3)650：八 FP 切边与 P 端点转接只读接口

状态：READ_INTERFACE_READY；没有候选、cut/matching 枚举、BFS、源有效性重验、field、solver 或 Lean。只读账保守计费1.5CPU秒，另 P 行拓扑读取实测0.00087698CPU秒，合计1.50087698/2CPU秒。该保守计费覆盖其余未单独计时的小文件读取与准备，不冒作全部实测。

## 实际源和具体 P 拓扑

实际源是 `research/ddp/more_graphs_20261027/d3d4_transfer/source650.implicit_adj.txt`：650个0-based隐式邻接行，每行10个邻点，无header；650/3250全10正则，公开D3继承。来源/credits 为 Delorme，邻接 V. Pelekhaty，维护者 F. Comellas；官方URL保存在同目录 `SOURCES.json`，文件取得于2026-10-27。

实际 P130/F520、65对共享八个F邻点的 P-twins、每点8F+2P配额、FF2080/FP1040/PP130，继承 `d10_D3_current650_critical_middle_gate/STRUCTURE_ROOT.json`，未重算。只按该P标签集读取原literal的130个P行并追踪2-factor，得到

    G[P] = C79 ⊔ C21 ⊔ C30。

三个环按最小label起始，代表分别0、120、172；完整有向label顺序见同stem JSON。这里只提取 P–P literal metadata，没有 BFS/球/源D3验证。尤其 P2-factor 不是一个130圈，F-neighborhood twins也不等于完整邻域 twins。

该源的既有可执行入口是 `d3d4_transfer/screen.py`（原literal parser/结构筛）与 `d10_D3_current650_critical_middle_gate/critical.cpp`、`run.py`。未定位额外不依赖literal的完整代数生成器；不臆造它。`source650_hierarchy/`、`matching_single_vertex650/` 实际是650/1625的(5,5)另一源；wave7 `shortcut650` 是(6,4)相关模型，均不能替本案输入或失败证据。

## 可直接继承的缓存与停止域

旧 `d10_D3_current650_critical_middle_gate/` 已存：

* `A2.u16le.bin`、`A3.u16le.bin`：650×650 row-major little-endian uint16，源label0..649的普通2/3步walk数，行和100/1000；不是距离或非回退计数。解释见 `WALK_COUNT_SCHEMA.json`。
* `EDGE_CRITICAL_MATCHINGS.jsonl`：全部3250旧边的两侧邻点、unique-distance3 middle-route masks与最大matching。FP1040全部middlematching0；FF中1952为9、126为8、2为7；PP130也为0。
* `forced_pin_cover_search/`：完整排除固定此源删1..5条旧边、新点连**全部不同删边端点**、不添其他边的家族。128个剩余FF锚、2820端点集、260个旧R2通过者仍无合法cut实现，终态completeNO。

本次新规则有8 cuts、漏接6个删边端点、另加3条旧旧 repair，超出该严格域。只读 canonical 节点及这些原始scope/source入口，未定位此 exact FP-transfer 规则的旧 strictNO 或实际 UNKNOWN 尝试；这表示本次未定位，不作全repo不存在声明。FP middlematching0只是特定必要拒绝器没有证书，绝不表示FP删边无损；unique3路的首/末 FP 边及多cut同时损伤仍可能失败。

## 唯一待激活规则及精确度账

选八条不同 FP 边 f_i–p_i，要求八个 f_i∈F互异、八个p_i∈P互异。删除这八条，令新z邻接全部八个f_i及其中两个p_i。其余六个p_i用三条两两不交的 P–P repair 配对；每条repair必须是原图非边。其余旧边保留。

每个F端点删1添z；两个P端点删1添z；其余六个P端点删1添repair。故候选651点，3250−8+10+3=3255边，全10正则。该账不证明D3。repair不能沿原P环已存在的相邻点补重边；C79/C21/C30的实际标签应保持。

## 一个可反驳的下一覆盖预测

**预测：** 存在这样的八FP选择及两个P-spokes，使新根z在3步内覆盖全部520个F目标。只这是前置必要门，不预测完整651/D3图存在，不并行启动数值。

令 S={八个f_i及两个选中p_i}，H=G−八FPcuts。repair只接没有z-spoke的六个P点，所以 z→F 的≤3路不可能使用repair：从z先到F再经P/repair时第三步还在P；从z先到P则该P不接repair，先走旧P–P再repair也仍停在P。因此该门精确为 `B2_H(S)∩F=F`，与三条repair的配法无关。

还可用既有 twin 结构把该 F-only 门写成旧source `B2_G(S)∩F=F`，无需重建源球：删除FP边两端未全在S，故不能直接套全端点 min-distance 引理；但若两步旧路用 f_i–p_i 后到某个F目标x，可改经 p_i 的 F-twin p_i*。f_i只删一条FP边，所以 f_i–p_i*保留；若 p_i*–x也被删，则x就是另一个f_j∈S，已距离0覆盖。若删除边出现在两步路的末尾，其F目标是f_i∈S；若从选中p_i先越过删除边，也可从f_i∈S重新起步。这覆盖所有≤2旧路的受损情况。

所以本预测可只读旧adjacency与A2 positivity，先形成 F-target source-R2 bitsets，再进行实际新选择门；当前没有形成这些新mask或枚举选择。P-target覆盖不能照搬此式：repair可产生 z–F–P–repairP 等3路，必须保留其真实端点耦合。完整图还须检验所有旧旧点对，不能只靠中间critical0或新根覆盖。

激活所需最小输入已齐：literal与P/F、twin表、A2/A3和middlecritical缓存；需要的新数据仅该规则的F覆盖bitset/实际cut与repair约束、首末及多cut损伤检查。仅在root明确激活后再做，当前STOP，无第二source/数值模板。
