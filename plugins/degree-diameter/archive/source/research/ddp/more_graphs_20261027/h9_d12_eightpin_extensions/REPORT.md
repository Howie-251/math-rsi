# 固定13个八pin生产批：final42377，0新增

以已独立验证的42377点图为起点，13项按冻结canonical顺序一遍走完：5项mandatory点已满度，8项3/4-anchor补全UNKNOWN，未得到完整新点。没有加第5anchor、改pin、重试既有UNKNOWN或扩池；没有重审旧基图、运行全源BFS或触碰38snapshot。

8项degree-legal者都完整做了mandatory R4；以4轮按边传播精确生成所有eligible anchors对全部missing targets的mask。同mask留一个代表，完整exact1/2均无解；再作Σanchors≤4的完整set-cover feasibility。去重后仍约1.38万列、97–141个missing行，均未返回verified incumbent。UNKNOWN不表示不可行。

| pool index | source n | mandatory遗漏 | 状态 |
|---:|---:|---:|---|
| 71 | 42377 | 108 | ≤2排除；3/4 UNKNOWN |
| 125 | 42377 | 108 | ≤2排除；3/4 UNKNOWN |
| 502 | 42377 | — | 度阻断：31174 |
| 103 | 42377 | 125 | ≤2排除；3/4 UNKNOWN |
| 205 | 42377 | 99 | ≤2排除；3/4 UNKNOWN |
| 134 | 42377 | — | 度阻断：28986 |
| 110 | 42377 | — | 度阻断：30154 |
| 577 | 42377 | 141 | ≤2排除；3/4 UNKNOWN（当前handle中断，不重试） |
| 532 | 42377 | 97 | ≤2排除；3/4 UNKNOWN |
| 40 | 42377 | — | 度阻断：39502 |
| 123 | 42377 | 108 | ≤2排除；3/4 UNKNOWN |
| 11 | 42377 | — | 度阻断：40447 |
| 206 | 42377 | 121 | ≤2排除；3/4 UNKNOWN |

## 实际限时与核验范围

最初使用HiGHS内部4秒time_limit，调用含setup/presolve实际耗9.60/9.75/11.22/9.09 CPU秒，均无verified incumbent。发现后停止当时活动的第5个handle，保留UNKNOWN且不重试；尚未尝试的剩余3个MIP改为独立硬4CPU进程，实际3.03/3.92/3.15 CPU秒，仍UNKNOWN。没有为证明UNSAT或dual追加时间。

前7条完整处理测得40.539192341 CPU秒；恢复段10.57205223 CPU秒。中断活动handle未输出CPU统计，故完整总CPU保持null，没有把两段之和冒充全成本；编译亦未计入这两个数字。初段内部limit的实际超出被如实保留。

完整mandatory R4共8次；接受前selected R4为0（无可接受邻集）；新图0、全源BFS0、旧图重审0。若有incumbent才会实际完整核8+anchors的R4并保存新图；没有把solver中间状态或局部覆盖当完整point。已有42377的D5仅作为继承基图事实，未计新成果。

[RESULT.json](RESULT.json)保存13项currentdegree、source_n、覆盖计数和solver状态；[terminal.json](terminal.json)的pending为空。[冻结范围](PREDICTION.json)、[覆盖程序](cover.cpp)、[原始生产程序](batch.py)、[仅剩余项的恢复程序](resume.py)、[硬限solver](mip_once.py)及items下的原始mask均保留。

本批执行已结束，但8项3/4-anchor可行性仍未决；没有首命中可交付，final图仍为原42377。到此停止，不增加anchors、换base或追中间覆盖分数。
