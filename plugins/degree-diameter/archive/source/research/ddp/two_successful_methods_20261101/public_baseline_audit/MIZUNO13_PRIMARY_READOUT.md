# 作者当前13度88452点旁证：与旧14度图分列

检索日2026-11-01，仅只读primary；没有下载/运行边表、生成器或BFS。

GitHub页面与GitHub Contents API均取得当前README，其“Published records and new graph — 2026-10-23”栏明确列(13,5)=88452，package为 `results/degree13-diameter5/`。README最近修改的提交日期为2026-10-23T05:13:27Z；提交说明为“Update published records and document successors of the diameter-five graphs”。这不是用搜索摘要单独判定。

该package的[README](https://github.com/rmizuno42/ddp/blob/main/results/degree13-diameter5/README.md)明确称2026-10-13加入：simple13regular、88452顶点、574938边、exactD5。它与旧 `results/degree14-diameter5/` 共用364个控制状态和同一88452点集合，但**affine数据与额外边不同**；普通部分度数为87696点度12、756点度11，加一个perfect matching M，再加覆盖756个剩余点的378边matching P，得到13regular。作者并未把旧14度边表原样改名为13度。

作者保存的[独立验证说明](https://github.com/rmizuno42/ddp/blob/main/verification/independent-2026-10-13/README.md)及[result.json](https://github.com/rmizuno42/ddp/blob/main/verification/independent-2026-10-13/result.json)报告：measured vertices88452、edges574938、minimum_degree=maximum_degree=13、connected、diameter5、all_sources_checked88452、ordered_pairs_reached7823756304、unreachable0，completed_at_utc=2026-10-13T02:20:21.475464+00:00。其方法是仅输入发布边表的独立普通queue BFS、无depth limit、不用generator/affine/matching/symmetry数据。这里引用的是作者现成报告，不冒充本机重新独验。

旧14D5 package同时保留，其当前摘要为756点度13、87696点度14。当前13度package则每点度13。两者的相同阶数不能当成相同图或旧源错标。

这证明存在当前可查的更强13D5公开primary声明及完整数据入口，足以阻止把本地51418..51457称为截至今日全球公开最好；旧“超过所核主表51417”的历史比较仍可保留。作者明确说明该88452尚未反映在其2026-10-23所读主表。本次没有认证全球最高或重新验其图。

本地保存的当前API选读为mizuno_current_0.md、mizuno_current_1.md、mizuno_current_2.md、mizuno_current_3.json；检索及README日期见MIZUNO_CURRENT_RETRIEVAL.json，package路径的提交日期选读见MIZUNO13_PACKAGE_HISTORY.json。来源中无关的摘要/标识字段已省略，不生成或比较产物哈希。
