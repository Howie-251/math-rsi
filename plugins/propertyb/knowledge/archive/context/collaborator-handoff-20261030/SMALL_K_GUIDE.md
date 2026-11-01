# 小参数下界：最新正文、证据与复算

2026-10-30。m(k)≥L 表示每个有限简单 k 元超图只要边数≤L−1就具有 Property B。证明中的点对覆盖、点数窗口、度数与锁点都属于内部完整归约；不是原始命题的附加假设。

以下路径均相对解压包根目录。请完整保留目录层级；有些历史程序含原作者机器路径，便携入口负责在临时副本中处理，不修改收到的原证据。检查算术时也应核对原始超图到完整局部型域、再到原染色结论的数学连接。

## 最新结果地图

|k|下界／可染边数预算|最新正文|实际证据与验收范围|
|---:|---|---|---|
|5|35／34|[M5_GE35.html](../../M5_GE35.html)；`context/propertyb34/round01/PAPER_CANDIDATE_MAP.md`|完整自然语言候选与分支精确证书；35 的完整 Lean 尚未闭合。m(5)≥33、≥34已完成端到端Lean。|
|6|67／66|[M6_GE67.html](../../M6_GE67.html)；`context/propertyb-m6-67-progress-20261029/PROOF_M6_GE67.md`|27–44全部实际分支接齐；按分支的独立精确复算齐备；`PROOF_AUDIT.json`为PASS，sound-modulo-imports；无本参数Lean。|
|7|131／130|[PROOF_M7_GE131.md](../propertyb-m7-131-20261029/PROOF_M7_GE131.md)|37–73点全部424型与2115296个共同坏对整数向量已独立精确复算；尚无跨家族终审或Lean。|
|8|267／266|[M8_M9_IMPROVEMENTS.html](../../M8_M9_IMPROVEMENTS.html)；`context/propertyb-m8-267-20261029/PROOF_M8_GE267.md`|47–120点2094型全部独立重算，299组件配额另由递归DP核；audit PASS，sound-modulo-imports，无Lean。|
|9|543／542|同上；`context/propertyb-m9-543-20261029/PROOF_M9_GE543.md`|57–195点3450型全部独立重算，完整决策树独立重建；audit PASS，sound-modulo-imports，无Lean。|
|10|1112／1111|`propertyB_small_k/propertyB_k10_k11_research.md`|合作者原证明和28545个原整数外舍入型重放；另独核一份最紧双锁型Fraction值；保持原交接状态。|
|11|2275／2274|同上|合作者原证明和70472个原整数外舍入型重放；另独核一份最紧双锁型Fraction值；保持原交接状态。|
|12|4664／4663|[PROOF_M12_GE4664.md](../propertyb-k12-4664-20261029/PROOF_M12_GE4664.md)|91–782点692个点数、664355型完整原计算及固定切点重跑；独核完整参数域、全部迹重数／度数／共度和20个Fraction紧型／端点；不是全表第二概率实现，无Lean。|

6、8、9已有Grok 4.7-build/xhigh与Gemini 4 Argon/high的有效整卷静态终审；两者未执行程序。7尚无跨家族终审，不能借用其他参数审阅。12的Grok新审阅针对明确进口下的完整覆盖链，准确范围见其 `reviews/DISPOSITION.md`；不把它写成全表双实现或双模型终审。独立数学判断的same-family/provisional与确定性实际算术结果分别记录。

## 先读最新正文，再核证据

六元的分流较多：新正文已经把小点数、34／35点中段、36–38点、39点、40–41点与42–44尾段连接到同一原始超图。目录 `context/propertyb-m6-67-progress-20261029/` 中的 `PROOF_AUDIT.md`、`audit/PROOF_SKELETON.md`给出整卷义务；独核分别在 `independent31_33/`、`independent34_min10/`、`independent36_38/`、`independent39/`、`independent_new_branches/`、`root/` 等处。它还复用较早六元诊断／66证明的已闭部分；请随证明引用查看，不能只抽取新目录的一份表当全部论证。

七元的 `RESULTS.json` 与各原分段输入记录原计算，`independent/REPORT.md`、`independent/check.py`和`independent/RESULTS.json`给出完整独核。独立程序以下降阶乘注入公式替代原二项式公式，重建全部度数域、三锁迹与避免配额的完整整数向量，并逐项比较精确分数。

八元、九元分别在最新目录保留 `SUMMARY.json`、原证书及作者程序，独核为 `independent/REVIEW.md`、`independent/check.py`和`independent/CHECK.json`。八元完整域包含120点四锁的六种实际迹；九元包含新增195点端点。两者的独核都从原始预算重建完整域，不沿用旧265／541边的截断。

十二元的 `SUMMARY.json`、`SUMMARY.log`和完整逐型原计算记录给原始结果；`repro/`及`REPRODUCIBILITY.json`保留固定693／694切点后的一次完整重跑，全部数学行与原记录相同，计时字段除外。`independent/COVERAGE_REVIEW.md`、`DOMAIN_CHECK.json`、`RESULTS.json`及`check.py`给第二实现的准确范围。694点起统一三锁收尾不依赖运行机器CPU速度；完整证书约70.6 CPU秒是历史实测，不是接收方耗时保证。

## Python复算

从包根目录运行，使用Python≥3.10，保持断言开启，不要加 `-O`。标准库可运行本入口6／7／8／9／12的独核；作者十二元全表重跑另需NumPy。macOS／Linux可运行，六元使用Unix计时信号；不依赖原作者环境缓存。

统一便携入口及各模式可先列出：

```sh
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --list
```

七／八／九元完整独核可分别选择：

```sh
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --case m7
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --case m8
python3 -B context/collaborator-handoff-20261030/scripts/replay.py --case m9
```

入口在独立副本运行已有程序，默认输出到 `reproduction-runs/<时间戳>/`；可用 `--output` 指定新目录。收到的原始证书不被覆盖。`--case all` 依次运行m6、m7、m8、m9、m12：六元含全部实际使用算术分支，十二元只独立重建完整域并重放20个Fraction型，不把它称为全表第二概率实现。完整命令、作者生成器模式、依赖和本次实际运行证据见 [PORTABLE_REPRODUCE.md](PORTABLE_REPRODUCE.md)。原始程序和输入均按原目录随包。

## 保留的合作者原材料

[旧原稿合卷](../../PROPERTY_B_SMALL_K_6_11.html)逐字保留四份合作者原稿。其中6／7／8／9的65／130／266／542是历史结果；目前10／11的1112／2275仍以该原稿为正文。原文件保留在 `propertyB_small_k/`；六组旧证书合计103190型已实际重放，不等于对最新新预算的复算。详细旧日志在 `context/collaborator-small-k-20261019/`。

10／11的可运行完整依赖已解包保存，可从包根使用下面的原命令；它们会生成自己的结果文件，建议在工作副本执行：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B context/collaborator-small-k-20261019/m10-m11/propertyB_k10_k11_verified.py 10
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B context/collaborator-small-k-20261019/m10-m11/propertyB_k10_k11_verified.py 11
python3 -B context/collaborator-small-k-20261019/m10-m11/independent_checks.py
```

前两项需NumPy；最后一项是保存的最紧型Fraction重放，不是两组全表第二实现。不要孤立复制 `propertyB_small_k/propertyB_k10_k11_verified.py`，其同目录导入依赖原先仅存于归档，已有完整解包副本才是推荐运行入口。

## 五元35与已完成的33／34

35的纸面候选按19–25点分流；完整文件地图、生成器、精确证书和实际输入绑定均保留。`context/propertyb34/round01/PAPER_CANDIDATE_MAP.md`、`paper-audit/PROOF_AUDIT.md`、`reviews/REVIEW_DISPOSITION.md`定位正文与既有审阅。旧[小参数指南](../collaborator-handoff-20261021/SMALL_K_GUIDE.md)保留各五元分支的细化原命令，作为补充索引，不覆盖本次最新6–12结论。

`formal/Aris4Math/ThirtyFour/`是35下界的暂停形式化，完整主定理尚未装配；Assembly的等价定理不能代替剩余义务证明。已完成的五元33／34及一般增长Lean的准确命令见 [LEAN_REPRODUCE.md](LEAN_REPRODUCE.md)。本次只交接现有材料，没有恢复35形式化或36研究。
