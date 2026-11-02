# 预留N(0)再选32块：一次小模型终态UNKNOWN

实际终态 `UNKNOWN_NO32_IN_SINGLE_WINDOW`。唯一session12629/driver1528362/child1528365已exit0；30秒窗口后不重启、不换v0/seed或改模型。返回31块暖解，未达必须32的条件，因此没有865clone图、没有较小替代图，也没有新图/参数/Lean计数。

## 模型与暖启实际绑定

只读原15552/116316作者simple adjacency一次，v0=0的实际N0有14个旧点。192个whole-W27 binary块使用accepted27 offsets实际公式，计数全部15552旧pin的实际clone incidence。相同完整coeff行压成216组，取每组tightestcap；加sumy≤32行，总217行/192变量/1248非零。全部旧row映射在 `ALL15552_ROW_MAPPING.tsv` 与 `ROW_GROUPS.json`，没有按理想controller target推容量。

普通capacity16−source_degree，N0上的capacity再减1；原degree14的容量2在非保护点完整保留，保护点剩1，olddegree15保护点剩0。I32只用于warm，实际丢块0后得到31；全部15552原行与压缩行手检通过。一次passModel、一次完整192维HighsSolution setSolution均kOk，原log确认MIPstart feasible。全域可重选192块，不强制保原I32/原16416边。

## 真实solver终态与信息量

HiGHS1.8.0/threads1/time_limit30实际返回kWarning、kTimeLimit，message `Time limit reached`。返回primal约−31，raw dual约−32（−31.999999999996177），gap0.032258064516；节点 **7811**，LP iterations577486，确实进入branching。不能因浮点dual略高于−32就当整数32被排。

这不同于上次15k全中心模型节点0的阶段，但仍未得到32。returned192向量经binary、sum≤32、额外center0 distinctness和全部15552原容量手检，确为31，未发现新incumbent。31是合法暖解，不是当前16416之外的改善；本次不生成更小16390等图。

当前结论只为**固定v0=0、固定W27 whole-block family的限时未解**。它不是无32证明、非source full-N最优性、非一般(16,4)上界；不借此前local≤4out NO或其他C-line失败扩大范围。若未来有positive32，需865distinct/保护N0扩张前≤15/全部oldcap及完整新literal和fresh验收，不能借旧private16416 PASS。

## 成本和停止

继承本nonorbit line旧global累计68.299114264CPU；本目录准备保守charge0.5，prior=68.799114264。wait4实际child30.503554CPU，driver0.001400001CPU，累计 **99.304068265/120CPU秒**。其中solver进程内计30.002071832，不另外重复加入。另changed-generator CombinationC的成本不混入本line。

完整数据：`MODEL.json/MODEL_INPUT.npz`、rowmapping、`WARM_START_INPUT/RETURN.json`、`PASS_MODEL_RETURN.json`、`RAW_SOLVER_RETURN.json`、`BEST_HANDCHECK.json`、`RESULT/TERMINAL.json` 和原stdout/stderr。所有进程terminal、一次run、retries0、0 sourceD4/field/BFS/Lean/ARIS。模型精确性见 `MODEL_EXACTNESS_PAPER.md`。至此停止，不用余额继续窗口。
