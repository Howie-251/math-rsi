# Exoo72：源路线与最小单点扩张的承重条件

源为项目已保存的 [source72.implicit_adj.txt](../../d3d4_transfer/source72.implicit_adj.txt)，72行隐式0基编号，Geoffrey Exoo来源，出处见同目录SOURCES.json。已知72点、180边、全5正则直接继承，没有重新BFS验证旧图。本次只做邻接、长度≤3简单路支持和16个循环边轨道的critical图匹配；没有扫描三边组合或随机修补。

删三个不接边M，取其六端点中的五个为S，新点z连S。H=G−M时，新根覆盖的精确条件是R²_H(S)=V(G)。另两条被删边若两端都在S，不影响这个集合距离，因此等价于只删除漏pin端点v与其mate u的那条边后检查R²(S)。互补代理已在 [root_cover_preflight/REPORT.md](../root_cover_preflight/REPORT.md) 完成832020个matching triples×6个漏pin，共4992120项；连更宽松的原图R²_G(S)都无完整覆盖，故这个最小操作已闭，不需本代理重复枚举。

旧点对有另一独立条件：经z的≤3路线要求至少一端在S，另一端在N_H[S]。所以两端都不在S的旧对，一旦失去所有旧≤3路就不可修复。定义K_e：当且仅当旧对的每条≤3简单路都含e，才把它列为边。删除e后S必须vertex-cover K_e。六条互不接的critical pairs足以反驳任意五pins；matching≤5却不证明存在可用覆盖。

事前预测“每条源边都有六条互不接critical pairs”被推翻。实际同步C12平移rho(12t+i)=12t+(i+1 mod12)是自同构，给6个顶点轨道与16个边轨道。只有内部halfturn两轨道代表(24,30)、(48,54)达到matching6，各轨道6边；其余轨道最大matching3至5。因此可确证这12条halfturn边不能由一个degree≤5新点单独修复，但没有从该证书统一排除全部其它删边。

源无triangle或4cycle，旧距离3的1656对中有1080对只有一条三步路。由girth≥5，若漏pin端点v的旧边uv被删，旧u、v之间没有替代≤3旧路；必须另有pin直接邻v，才可通过u−z−s−v修复。因此“为了分散覆盖选induced matching”反而不能保住这条被删边。

原始 [RESULT.json](RESULT.json)、[CRITICAL_PAIR_GRAPHS.json](CRITICAL_PAIR_GRAPHS.json) 和 [CRITICAL_MATCHING_CERTIFICATES.json](CRITICAL_MATCHING_CERTIFICATES.json) 保存全部范围、路线及匹配证据，预测见 [PREDICTION.json](PREDICTION.json)，复现 [analyze.py](analyze.py)。CPU0.146835983秒，源BFS0、候选生成0、三边组合扫描0。没有扩展证书审计。后续同源循环生成规则的单次比较另见 [CYCLIC_REPORT.md](CYCLIC_REPORT.md)；此处不声称一般73点图不存在。
