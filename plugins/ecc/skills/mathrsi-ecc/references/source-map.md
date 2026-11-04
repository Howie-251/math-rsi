# ECC 阅读与执行地图

所有现行关键入口均在本克隆内。归档 [范围说明](../../../archive/README.md) 和 [逐文件清单](../../../archive/INVENTORY.json) 明确省略171个pair大流；不要将完整原发布README描述误用为插件已含全部流。新任务原规格、进度与wiki仍留自己的工作区。

## 按当前义务阅读

|当前问题|先读整理层|承重原件/下一动作|
|---|---|---|
|定义、合法操作、构造与否定|[主入口](../SKILL.md)、[归约§1](reductions.md)|source/proofs三稿；当前目标仍以本题合同为准|
|原目标为何进入172母码|[结构漏斗](reductions.md)|[43/10完整证明](../../../archive/source/proofs/01-main-43-10.md)§7–15；formal/ecc43/ECC/Reduction.lean|
|E1/E2/E3是否适用|同一归约的文献使用条件|[REFERENCES](../../../archive/source/references/REFERENCES.md)；原包未附第三方全文，不谎称现次深读全文|
|目录实际代表与互异覆盖|[ecc-certificate §3](../../ecc-certificate/SKILL.md)|[actual172](../../../archive/source/data/actual172_matrices.json)、[图规范化程序](../../../archive/source/computation/reproduce.py)、历史catalogue_check|
|尾型/陪集/共同pair为何必要|[归约§4](reductions.md)、[固定母码例](../examples/fixed-parent.md)|主证明§16–27；[Coset.lean](../../../archive/source/formal/ecc43/ECC/Coset.lean)|
|新参数联合域或对称性卡住|[失败机制](failures.md)|[历史独立交接](../../../archive/legacy-context/MATH_RSI_DOMAIN_HANDOFF.md)§4；外链旧原件范围明确不齐|
|候选矩阵/保存集/拒绝重放|[ecc-certificate](../../ecc-certificate/SKILL.md)|tools实际命令；source/computation原检查器；[本轮结果](../../../evidence/IMPLEMENTATION.md)|
|形式归约与实际输入|[Lean边界](../../ecc-certificate/references/lean-boundary.md)|[formal说明](../../../archive/source/formal/README.md)，两工程源码与三个audit，verification/lean日志|
|第五项文献短路线|[归约§6](reductions.md)|[42/16证明](../../../archive/source/proofs/03-case-42-16.md)，formal/ecc42/ECC42/Main.lean|
|成果/视觉/持续演进|[发布原README](../../../archive/source/README.md)|[READING](../../../archive/intake/READING.md)、[VISUALS](../../../archive/intake/VISUALS.md)、[EVOLUTION](../../../archive/intake/EVOLUTION.md)；准确已读范围|

## 普通可执行资源

- `tools/check_matrix.py`：原规格显式n/k/d＋JSON整数行，完整非零消息枚举，实际秩/最小距/谱/失败见证。
- `archive/source/computation/check_data.py`：固定五下界/172母码/多项式及历史覆盖读回。
- `tools/check_saved_sets.py`＋`relocated_manifest.py`：数学检查取原实现，只解析实际读取的路径，保留172保存集全读能力。
- `tools/replay_one.py`＋`replay_selected.cpp`：一个完整已存母码拒绝证书，逐项实际矩阵运输/F距离/pair低权/EOF；源码内只放宽原172批次选择。
- `archive/source/computation/{even_scan,literal_gray_replay}.cpp`：两套完整扫描源；`reproduce.py full-f`的路径加载需要全流或相应适配。本轮不跑大域。
- `archive/source/verify.py lean`：两Lean源副本build和三audit，按scope决定执行，不能把历史日志当现次build。

## 原件保留与缺件

`archive/source/`保存完整论文源/PDF、三证明、数据、两Lean工程（无缓存）、扫描/checker和发布验证。原件相对路径保持，因此其中冻结引用仍指发布包布局。`archive/legacy-context/`为本仓v1已有两交接，保留旧失败与开放问题；不是原v2整个工作区。`archive/intake/`为派生笔记，保留实际阅读/执行范围。

原包未提供原冻结FORMAL_SPEC独立文件、第三方PDF、历史模型对话、完整wiki与失败日志、Kohnert CNF/RUP等旧细节；不把它们列成已拥有的可执行资源。完整pair大流在原完整发布包，插件清单逐项标记未分发。无在线下载器或猜测URL。

科学状态沿用原范围：43/10旧计算机辅助证明；邻参数推论；42/16对已发表E3的应用；新Lean归约和实际数据连接；45/11距离17仍未解。普通重放、本轮读回、内核归约、外部文献进口和静态模型意见分别报告。
