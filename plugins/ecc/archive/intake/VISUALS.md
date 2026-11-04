# ECC 包已有可视化与数据素材

日期：2026-11-04。仅盘点与理解，不开发网页。源目录：`mathrsi_new_results/ecc-five-case-release-20261103/`。

## 已有成品

包内媒体清单只有 `paper/main.pdf`（16页）。没有独立HTML、SVG、PNG、照片或视频；没有可直接复用的互动网页。不能把原ECC工作区旧 `PROOF_PACKAGE.html` 当成本包已提供或已检查的素材。

PDF是双栏正式数学草稿，黑白为主、有行号与匿名作者占位，后半为单栏附录和矩阵长表。实际看过p1及p5截图。本次在本笔记目录保存：

- `paper-page01.png`：结果表＋摘要，1600像素预览；从原PDF转出，只是intake预览。
- `paper-page05.png`：证明流程图＋最优距离推论与AI贡献小节。
- `paper-extracted.txt`：16页文本提取，作导航，不是新证明／新排版。

## 论文内可以复用的图表

| 位置／源 | 现有内容 | 可说明的成果 | 使用限制 |
|---|---|---|---|
| PDF p1 Table1；`paper/sections/01-introduction.tex` | 五个排除目标／路线／最优值表 | 五结果一眼比较，明确45/11仅区间 | 表中五项不是五个独立新证明；42/16是E3应用 |
| PDF p4 Table2；`paper/sections/04-computation.tex` | 172母码、每例2³²、总738,734,374,912、F429,024、pair619,053,789、0兼容边 | 结构归约后实际计算规模及检查类型 | “coset visits”不是同数量128距离全算；早停／掩码实现有不同计数单位；历史完整扫与本次发布复验分开 |
| PDF p5 Figure1；`paper/sections/06-ai-formal.tex` | 5个黑白圆角框的纵向TikZ流程：任意43/10→满支撑40/7→双扫描／pair证书→主结果与推论；第五项另框 | 两条证明路线及依赖结构 | 已有可编辑代码；第五项与172计算独立，不能加箭头画成由扫描推出 |
| PDF p5 Corollary5.4；`paper/sections/05-consequences.tex` | 四精确值＋45区间的数学排式 | 成果卡片的简洁数字来源 | 不把45区间写为已确定17 |
| `proofs/01-main-43-10.md` §17七行表 | 三尾消息、尾重量2/4、陪集阈值16/14 | 解释“为什么要兼容三角、为何无边已足够” | 三重和阈值14未进行不必要扫描，不能展示成做了七类枚举 |
| 同证明§26及论文附录08 | 母码分组统计；拒绝重量2…14的7档直方数 | pair证书为何是局部、便宜、确定的反证见证 | 这不是原目标码重量分布，也不是算法成功率 |
| `paper/sections/09-data.tex`；`proofs/01-main-43-10.md`附录A/B | 五下界矩阵／重量谱、172母码矩阵／hull／F数 | 可以给专家展开“数据确实在包内” | 密集原表适合作证据页，不适合首屏主图 |

Figure1已是代码原生TikZ矢量：主文件加载tikz的 `arrows.meta,positioning`；不需AI重新画。后续若需要网页图，可从同一结构作SVG/HTML重绘，保留E1/E2/E3及外部计算的关系。本轮没有导出／重写源图。

## 可复用的确定性数据

| 包内路径 | 数据语义 | 可支撑的未来展示 |
|---|---|---|
| `data/lower-generators.json` | 五个实际生成矩阵，整数bit编码，n/k/d | 可复算重量谱或切换码参数；第一层展示精确值与一份真实矩阵 |
| `data/actual172_matrices.json` | 每母7整数行、128字、127非零重量、hull维 | 172对象库、母码查看器、完整性说明；不能仅凭hull分类宣称穷尽 |
| `evidence/manifest.json` | 172母码到双扫描input/result/F、pair流的相对路径与显式坐标置换 | 可点击的证据导航；目录覆盖信息不由路径本身证明 |
| `evidence/cases/*/original_scan-result.json` | 每例全域完成数、F数、CPU、prefix掩码统计 | 解释精确筛除如何减少工作；CPU不是统一硬件基准测试 |
| `evidence/cases/*/independent_full_F-result.json` | 独立反向主元、32基、Gray全域、实际距离计数、CPU | 双实现差异与覆盖分离；不能把profile当full |
| `verification/certificates/pair-replay/native_result.json` | 全172、429,024 F、54,915,072距离、619,053,789见证、严格EOF、直方计数 | 短而准确的检查证据卡：重放全部pair，0无效 |
| `verification/lean/RESULT.json`及audit日志 | 两构建、三个import/type/axiom检查的退出码／耗时／最终类型 | 可展开Lean边界，展示显式参数与已核归约；不能只显示无sorryAx徽章 |
| `verification/single-case-scan/full_f/SUMMARY.json` | 发布复验只重扫new172一例的两实现 | 把“历史172完整扫描”和“本次重放/重建/单例复算”分成准确标签 |

本轮两项读回输出 `finite-data-readback.json` 与 `saved-sets-readback.json`可作接收核对证据，不应替代发布包正式来源。它们只分别验证有限数据和保存集合一致性。

## 可讲清楚的视觉主线（素材理解，不是网页开发）

最强叙述是“任意10×43矩阵的否定问题，变成172个有理论覆盖的母码；每母偶商恰2³²；找到完整429,024个候选后，全部pair都有一个低权拒绝见证”。画面中应把**数学归约／覆盖依据**与**计算拒绝见证**连到同一原对象，避免只有巨大计算数字。

第五项适合另一个很短的支线：`42/16/≥13 → 43/16/≥14 → 41/14/≥14 → exact14 → E3`，说明识别已有理论连接本身可以结束目标，无需再生成大搜索。

AI贡献有两件可定位的论文叙述：Gemini建议native early-rejection profiling（测得早期固定码平均约3.38次检查，非最终172总负载）；Grok要求第二完整扫描以补无遗漏义务。原模型记录未收入包内，图上可写“论文记录的干预”，不可夸大为原始轨迹已完整公开或因果速度提升实测。

## 身份和传播语境

PDF p1页脚包含样式默认“Under review by ICML/Do not distribute”，但README及 `paper/STYLE_SOURCE.md`明确仅用ICML样式，未宣称投稿／录用。已有PDF不适合直接截图当正式发布海报的权威背书。包没有真实作者／机构／新许可证信息，后续网页需由负责人给定发布身份；本次不代填。
