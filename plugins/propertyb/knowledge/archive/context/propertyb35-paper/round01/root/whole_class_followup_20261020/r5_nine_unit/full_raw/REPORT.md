# 剩余1322个r5九单位彩色轨道：完整raw执行

**COMPLETE_STRICT**：1322/1322轨普通raw严格，0非strict；33050行独立ABC重放全部相等。没有未处理轨，没有触发20非strict早停。

完整装配候选见[R5_COMPLETE_CANDIDATE.md](R5_COMPLETE_CANDIDATE.md)：原25/35/pair-cover、恰五六度H，经非B低迹≤2、Brooks四七单位点或完整三K5例外、完整374目录与1689彩色轨证书，接回原H染色。状态paper candidate、same-family/provisional，待root独立整合和项目审阅，非新Lean结论。

本轮只扫先前真正未覆盖的1322轨，不重复旧3pilot或diverse40。主体CPU323.788661秒，墙332.872043秒，低于600CPU秒/720墙秒授权预算；每50轨落检查点，每轨即时追加完整记录。

新raw最高11351/11440，余89/11440；最紧见证base44、低标签[2,3,4,5,6]、私有数[1,1,3,5]、最大锁迹4、empty5；位置[22,10,11,23,12,14,13,24,25]，RECORDS.jsonl第286行（plan_index285，原domain_record683）。这只是最高raw见证，不是实际不可染H。

最终覆盖分层为旧325至少一个标记strict轨、旧pilot新2轨、diverse40轨、full_raw新1322轨，合计1689轨；对应标记736+12+100+2259=3107。旧325包含原270全标记strict轨和55部分标记strict轨，未重复计数。

COVERAGE.py对每个源证书核其精确counts等于原DOMAIN记录；对全部3107目标逐项核经规范标签运输的完整counts及低色相等、九锁位有效，PASS，CPU0.289072秒，保存逐caller证书来源和实际运输位置。

另串行重放旧325个具体布局：以独立ABC计数加**原嵌套total/pure quota**扣除，8125行及全部冻结affine值精确相等，最大8007/8008<1，CPU1.169377秒。旧修正证书不称普通raw；此次未另加任何quota下界。

实际输出：

- PLAN.json：明确1322个原域来源及颜色轨。
- RECORDS.jsonl：每轨精确counts、锁位、25行ABC、raw值与成本。
- RESULT.json：完整执行状态、最高界和0残余。
- COVERAGE_RESULT.json：1689轨/3107标记的完整证书调用图与运输位置。
- OLD325_REPLAY_RESULT.json：旧325个原配额证书的具体行重算。

复现执行 `python3 RUN.py`；已有完整journal时只显示已存完整结果，不重复扫描或改写实际首次执行成本。`python3 COVERAGE.py`和`python3 REPLAY_OLD325.py`可单独重放最终覆盖与旧证书。主循环每个optional quota显式清零，原始ABC由BareLayout及独立标号注入/下降阶乘实现逐行相等核对；未运行外模型、Lean、新布局菜单或整H枚举，未修改导航/canonical文件。
