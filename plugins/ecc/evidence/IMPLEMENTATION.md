# ECC v3实施与真实使用

2026-11-04，MathRSI现有v2分支上的原位升级，协调入口为mathrsi-meta-evolve，源发布包只读。不恢复43/10旧研究或45/11 Goal，不操作aris4math_v2，不重跑大域，不新增付费模型调用。本报告是插件作者执行记录；Root负责base caller、双端别名、全局文档和最终集成/审阅。

## 原有能力与实际改变

保留约200行的mathrsi-ecc有效指导，补原件自包含、实际调用/返回与形式深化。新增独立技能 `ecc-certificate`，职责是消费实际矩阵/覆盖/保存集/pair/Lean参数并交出scope证据，供通用verify消费；不是再造ECC2主干。数学定义、归约公式、真实失败与重试条件放references，普通命令与完整固定母码例子可执行。

原件在archive/source保持相对路径和原文。1326文件、1,723,685,941字节的输入中复制1155文件、44,064,662字节；包括三证明、16项论文/PDF相关材料、47项两Lean工程文件、全部数据、检查器与扫描器、全部172例输入/完成结果/接受集和发布核验。没有复制工具链、.lake、olean、Python缓存、认证文件。保留index169完整pair流；省略171流1,679,621,279字节，逐项原相对路径/字节/原因在archive/INVENTORY.json。没有>100MB文件。归档本身不升级数学结论。

archive/legacy-context复制本仓v1已接收的两份原交接；archive/intake复制本次四份派生阅读笔记，明确两者性质与缺件。原包未给的完整旧wiki、原失败轨迹、模型对话、第三方全文和Kohnert证书未冒充已拥有。

## 真实命令与产物

以下均在MathRSI仓库根执行。输出是本轮生成的evidence/scratch，未来使用换成当前任务的新scratch目录，保持archive只读。

```sh
python3 -B plugins/ecc/archive/source/computation/check_data.py \
  --output plugins/ecc/evidence/scratch/finite-data.json
python3 -B plugins/ecc/tools/check_saved_sets.py \
  --manifest plugins/ecc/archive/source/evidence/manifest.json \
  --output plugins/ecc/evidence/scratch/saved-sets.json
python3 -B plugins/ecc/tools/replay_one.py \
  --output-dir plugins/ecc/evidence/scratch/one-mother
python3 -B plugins/ecc/tools/check_matrix.py \
  --matrix plugins/ecc/evidence/scratch/matrix42.json --n 42 --k 16 --distance 12 \
  --output plugins/ecc/evidence/scratch/matrix42-result.json
python3 -B plugins/ecc/tools/check_matrix.py \
  --matrix plugins/ecc/evidence/scratch/matrix43.json --n 43 --k 10 --distance 17 \
  --output plugins/ecc/evidence/scratch/matrix43-target17-result.json
```

- 原check_data exit0/PASS：五实际下界矩阵71,675非零消息；172实际母码21,844非零重量；rank/even/distance/full-support、完整存储字/重量和45个重量处多项式恒等式。历史覆盖数被读回，未当前执行全域。
- 保存集薄适配exit0/PASS：全部172例429,024保存记录，独立基秩、Gray下标/实际40位字、正规化运输及两集合精确相同，历史完成标记检查。没有重新判定2³²个代表。原数学检查脚本逐字保留，仅导入路径解析器改为不检查从不读取的缺失pair路径。
- 单母码重放exit0/PASS：index169 catalog_after163_169，546成员，69,888条F距离，148,785 pair全部真实低权，严格EOF；零invalid/nonrejecting，F_domains_rerun=0。native CPU0.005509秒，PROCESS保存编译/执行命令、退出码、stdout/stderr/wall；这是当前硬件单例native时间，不是全证明速度。实际完成一次C++17编译，生成二进制在运行后删除，源码及结果保留。
- 新通用矩阵检查器对归档42/16实际矩阵exit0/PASS：rank16、完整65,535消息、精确d12；独立Gray枚举不使用check_data的码字列表缓存。输入matrix42.json从归档lower-generators的实际rows导出。
- 同检查器对43/10下界矩阵**期望17**，exit1/FAIL：rank10、完整1023消息、实际d16，谱A16=12，并保留最小权消息/码字。这是有用的失败见证，不将合法seed误作目标解。输入matrix43.json来自同档案首项。

另将插件原件和工具复制到含空格的新临时目录，实际执行原check_data、172保存集检查和完整母码169重放，三命令均exit0/PASS；副本随后删除。结果/命令保留 `scratch/relocation-fixed/PROCESS.json`。第一次复制排除规则误将归档内部evidence也排除，造成缺manifest；修正复制范围后重跑，没有改变检查器数学。此项验证新克隆相对路径消费，不是另一套独立数学实现或第二台机器复现。

工具文件与未改原件的关系：check_matrix是薄普通整数矩阵核验；check_saved_sets仅换路径导入，relocated_manifest只解读本操作读域；replay_one只准备真实输入与执行；replay_selected.cpp相对冻结原checker只放宽固定172批次为1..172、保留原index并把all172输出键改为all_selected，数学检查不变。没有统一研究调度器或下载器。

## Lean与覆盖的实际范围

本轮读两个工程最终入口、审计和参数定义，复用归档fresh build/type/axiom日志；没有再次Lean构建。ECC43真实有限母码参数和前三下界/45区间矩阵接入核内，归约已实现；最终仍显式接受E1/E2/目录互异/所有母码pair不兼容。scan-facts进一步显式接F/projection/retract/coverage/pair witnesses，未核内跑外部扫描。ECC42以E3为参数核归约，42下界只普通枚举。无sorryAx不能消掉这些参数。

未当前执行：图规范化、全172 pair重放、两套2³²全域扫描、Lean、论文编译、外网查新或全部历史研究复验。原catalogue入口不依赖缺失流；需要pynauty时可按技能独立运行。原quick/certificates总入口及full-f manifest加载依赖未分发pair路径，不能直接用精简副本冒充完整包。补齐完整包路径后才能按原REPRODUCE执行相应总入口。

43/10旧主证明与172双扫描不是v3新发现。新包深化是Lean归约/真实数据连接、便携完整发布与复验、42/16文献路线；45/11距离17仍开放。新插件方法未接受等预算效率实验，不声称RSI速度数字。

## 返回合同与集成位置

`mathrsi-ecc`消费原n/k/d、对象域、已选/待选路线、实际瓶颈，返回领域定义、合法操作、条件归约、实际探针/证明、失败输入及下一义务；prepare/survey共享文献调查，route-loop/prove取数学/失败refs，不另起总控。

`ecc-certificate`消费scope、原定义、正文、期望参数、实际矩阵/母码/F/证书、共同坐标、完整域和写入路径；返回实际命令/结果、读域、明确支持的局部结论与未闭连接。矩阵PASS接存在；pair PASS接固定母码排除；保存集读回不填完整性；Lean保留显式进口。嵌入时回原verify/prove，不递归最终verify/handoff。

当前所有curated链接已检查；历史archive内部缺外链按归档范围保留。Root应核base caller及 `.agents`/`.claude` 相对发现别名，消费这里真实输出作同轮集成；这一步由Root负责，不由插件作者重复写其拥有文件。

## Gemini具体意见与最小修订

已消费 `development/evolution/v3-20261104/reviews/gemini-002.response.md` 的三项意见；其审阅接受核心数据/Lean边界，没有执行程序，本段不把静态接受当执行证据。

1. 新增插件根 `README.md`，接两技能、五参数准确状态、数学/失败/Lean references、三条轻量运行命令、169完整流及171缺流、原件和本证据报告。
2. lean-boundary明确三个audit位于 `archive/source/formal/ecc43/` 或 `ecc42/` 工程根，非ECC/ECC42模块目录，并列明RESULT、三audit日志和两build日志的实际文件名。
3. replay_one的manifest和矩阵快照均按真实 `snapshot172_index` 字段查找，避免列表位置假设；未知编号或缺对应快照用argparse.error返回，输入绑定完成后再建新输出目录。冻结原件与数学checker不变。

受影响命令只对当前169完整证书再执行一次，原证据不覆盖：

```sh
python3 -B plugins/ecc/tools/replay_one.py --index 169 \
  --output-dir plugins/ecc/evidence/scratch/gemini-index-fix-replay
```

实际exit0/PASS，546成员、69888条F距离、148785 pair、严格EOF、零无效/非拒绝见证，F_domains_rerun=0，native CPU0.005163秒。新PROCESS/逐例/native JSON均保留，编译产物删除。现行10份curated Markdown链接检查零缺件，记录 `scratch/gemini-curated-links.json`。没有因此重复其它矩阵检查、全域扫描、Lean或整题审阅。
