# 保旧边的source-N设计补全：最后有限批，UNKNOWN

本批未找到总数≤16的available pin cover。实际162个模板各一次greedy与extra冗余删除均得到 **21 pins＝11固定seed＋10extras**。唯一冻结模板v=12312的残余setcover在20秒窗口后仍为10extras；结论保持UNKNOWN，不是21最优、5extras不可能或全族NO。没有16417图，本Ccase停止。

## 用原完整覆盖设计改变矩阵

[PRED](PRED.md) 先提出：原source完整N(v)已能在current16416上以R3覆盖，去掉其中4个当前满度点后，能否用总≤16的当前available pins补回缺口。全程保留所有129240条current边，没有再牺牲donor路径或扩helperH。

实际候选来自旧profile的全部“未选且zero_residual_neighbours=4”行，读得 **162**，没有只挑示例或把expected162硬筛成162。每v的原Nv由current graph邻接过滤<15552得到；四blocked均currentdegree16，其余11点全在4050 available域。cachedoldsourceR3的完整Nv并对所有16416点均为full；没有生成新球或重验sourceD4。

每v固定seed不删，使用所有4050 available点（含currentclone）做一次maxgain／actuallex greedy，只对extras做一次逆序冗余删除。保存的 [ALL_TEMPLATE_GREEDY_RECORDS.jsonl](ALL_TEMPLATE_GREEDY_RECORDS.jsonl) 逐模板给Nv、blocked、seed、initialholes、4-bit blocked覆盖类别、每extra实际修复target bitmask／类别数及完整cover。不是只汇报剩余holes总数。

[TEMPLATE_GREEDY_SUMMARY.json](TEMPLATE_GREEDY_SUMMARY.json) 的actual162模板全部21点，tielex唯一冻结v=12312；greedy没有命中≤16，所以才进入这一模板的唯一residual window，没有换第二个v重试。

## 一个实际设计中的覆盖责任

冻结v=12312的四blocked按bit顺序为 **8438、8449、14134、14174**；保留11个available seed，已覆盖14672点，initialholes **1744**，其中1670原source点、**74个currentclone**。这些74点仍留在模型，未被旧source子图筛掉。

例如类别0x1表示“原四blocked中只有8438的R3覆盖该hole”，有334点；0x2只有8449，334点；0x4只有14134，317点；0x8只有14174，317点。还存在两／三blocked共同覆盖类别，完整15类与0类计数见 [FROZEN_TEMPLATE.json](FROZEN_TEMPLATE.json)。0类为0，符合原完整Nv覆盖。

第一个extra8425修478个holes：其中0x1修157、0x2修103，并同时修多种共享类别；第二个extra8426修446，其中0x1修96、0x2修150。记录还保留它们修复的全部真实target bitmask，及后续extras（包括currentclone pins）的对应责任。这样可以区分不同路线在互补哪些缺口，而不是把每个extra简单称为覆盖更大。

## 一次残余求解及真实返回

固定seed后仅保initialholes **1744行**，删除已由seed保证的14672行；仍保全部4050 available extras，经空列与相同残余coverage合并得 **3771列、1,028,362非零**。actual row／column标签全部在 [RESIDUAL_COLUMN_ROW_MAPPING.json](RESIDUAL_COLUMN_ROW_MAPPING.json)，该矩阵不同于此前完整16416行cover模型。

预先写 [SOLVER_PRED.md](SOLVER_PRED.md)，唯一HiGHS以10extra实际fullcover暖start，binary minextras、threads1、time_limit20，目标budget为5extra。passModel／setSolution实际kOk；返回kTimeLimit，solver实际CPU20.66267475，warm10extra仍可行、node0／dualbound0。无独立不可行或最优性证据，不升级为5extraNO。

[RAW_RESIDUAL_SOLUTION.json](RAW_RESIDUAL_SOLUTION.json) 保原返回和actual wholecover复核。[RESULT.json](RESULT.json) 给最终21个真实pins与union16416；21会使新Z超过degree16，所以没有新边表、PIN_SET或newroot route文件。正预测本批未支持也未被严格推翻。

## 成本与停止

唯一driver1251353／child1251356、session99662已exit0。新增childCPU **32.562183**，parent **0.016980510**，准备0.50；沿prior **37.985870069**（含已记录K5启动前语法失败，不reset），本Ccase累计 **71.065033579 / 120 CPU秒**。child hard65／soft60，唯一求解配置20秒。

本批current literal作为Nv／degree／若命中则产图输入parse1；全部R3从旧4050可用pin及cooperative oldsource完整表复用，newballs0。sourceD4／oldallrootBFS、field、Lean、ARIS均0；没有positive命中，新Z routeBFS与图生产也为0。图／参数／Lean计数没有增加。

[TERMINAL](TERMINAL.json)、[HANDLE](HANDLE.json)、[CHECKPOINT](CHECKPOINT.json)、[seed_child.py](seed_child.py) 和 [run_once.py](run_once.py) 保留actual过程。此为授权的最后Ccase批，完成STOP：不第二模板、随机seed、第二solve、H／S5或局部参数梯；旧16416及专家包未改。完整R3数据、source设计holes与修复类别已保存，未来由root另择新问题。
