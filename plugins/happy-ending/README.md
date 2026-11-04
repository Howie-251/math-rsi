# Happy Ending / Erdős–Szekeres七边形插件

主入口[mathrsi-happy-ending](skills/mathrsi-happy-ending/SKILL.md)组织有序signotope数学研究；[happy-ending-certificate](skills/happy-ending-certificate/SKILL.md)核具体颜色、SAT证据边界和结构caller。它们被base当前阶段调用并返回原义务，不另起总控。

本插件随仓保存[完整原报告](archive/source/source/report.md)、[结构证明与历史索引](archive/source/working/package/proofs/READING_GUIDE.md)、[原图](archive/source/figures/)及编码/收据。不是只把外部作者路径写入source-map。[归档说明](archive/README.md)明确包含、排除与原包缺件。

读取结论分层：b25有历史human acceptance，保持same-family/provisional；本次标准库独立checker确验一个25点抽象见证；40/50/76/77→ES≤78属于原结构工作稿链，未经独立复审。今日75/76只有作者截图，`reported pending source`，未替换已读证明。抽象见证不证明平面实现，25→76→77→78也不是同一数字的时间增长。

仓库根可立即执行的小核验：

```bash
python3 plugins/happy-ending/tools/check_lower25.py \
  plugins/happy-ending/archive/source/working/package/proofs/sat-756/color.tsv \
  --output /tmp/mathrsi-happy-ending-lower25.json
```

本轮实际命令与范围见[evidence/IMPLEMENTATION.md](evidence/IMPLEMENTATION.md)。这是下界见证检查，不运行SAT或Lean，不证明全域上界。原55份UNSAT证明约3.879TB未随原包提供，不描述为本次重放。

新任务写自己的工作区wiki/正文/结果，archive只读。源研究暂停和当前数学状态不会因插件安装而改变。
