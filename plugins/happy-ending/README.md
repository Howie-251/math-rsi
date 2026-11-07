# Happy Ending / Erdős–Szekeres七边形插件

主入口[mathrsi-happy-ending](skills/mathrsi-happy-ending/SKILL.md)组织有序signotope数学研究；[happy-ending-certificate](skills/happy-ending-certificate/SKILL.md)核具体颜色、SAT证据边界和结构caller。它们被base当前阶段调用并返回原义务，不另起总控。

本插件随仓保存[完整原报告](archive/source/source/report.md)、[结构证明与历史索引](archive/source/working/package/proofs/READING_GUIDE.md)、[原图](archive/source/figures/)及编码/收据。不是只把外部作者路径写入source-map。[归档说明](archive/README.md)明确包含、排除与原包缺件。

读取结论分层：b25有历史human acceptance，保持same-family/provisional；本次标准库独立checker确验一个25点抽象见证；40/50/76/77→ES≤78属于原结构工作稿链，未经独立复审。新完整[75/76原证明包](archive/n7-20261103/README.md)已经收入，给40/50/75/76→ES≤77，仍为same-session/unreviewed/unaccepted。旧76/77/78链保留历史，不提升数学接受状态。抽象见证不证明平面实现，25→76→77→78也不是同一数字的时间增长。

仓库根可立即执行的小核验：

```bash
python3 plugins/happy-ending/tools/check_lower25.py \
  plugins/happy-ending/archive/source/working/package/proofs/sat-756/color.tsv \
  --output /tmp/mathrsi-happy-ending-lower25.json
```

本轮实际命令与范围见[evidence/IMPLEMENTATION.md](evidence/IMPLEMENTATION.md)。这是下界见证检查，不运行SAT或Lean，不证明全域上界。原55份UNSAT证明约3.879TB未随原包提供，不描述为本次重放。

新任务写自己的工作区wiki/正文/结果，archive只读。源研究暂停和当前数学状态不会因插件安装而改变。

取等、交换与端点相容的可执行入口是[领域参考](skills/mathrsi-happy-ending/references/equality-exchange.md)：从m≤实际删点≤角色覆盖≤m迫单例和精确覆盖，再在替锁后的实际b+1域迫R6、定位前驱及同端R5；也保存t=0重算、regular共根条件加权和三个未闭分支。仅在相应实际条件满足时消费，不把≤74子类当无条件结论。

两个新策略反例可有界复算：

```bash
python3 plugins/happy-ending/tools/check_strategy_examples.py \
  --output /tmp/mathrsi-happy-ending-strategy-examples.json
```

它枚举11点/10点固定例的全部packet和递增路径，分别确认逐点供应不保证兼容、单点插入不保证联合插入；不是75/76上界checker。v4维护使用及精确验证范围见[使用记录](../../development/evolution/v4-20261108/HAPPY_ENDING.md)。
