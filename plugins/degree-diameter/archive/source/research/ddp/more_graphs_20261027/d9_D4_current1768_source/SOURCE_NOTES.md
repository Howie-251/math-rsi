# (9,4) 当前1768：查重后继承停止

本轮只读查重及来源。Root 最新主表确认仍为1768、未标optimal；本子代理重新读到的官方 D4 细页也列 Com_1768。没有新增数学试验、profile、BFS、构图或solver，没有新增method row。

唯一账本已有 [当前D3/D4源保边扩点条目](../../../../research-wiki/experiments/ddp-more-graphs-20261027-source-slack-monotone.md)。其原证据 [d3d4_transfer/REPORT.md](../d3d4_transfer/REPORT.md) 已明确：官方基图1700全9正则，减191条边，加68点和497条边，成图边数为7956=1768·9/2；配合最大degree9，强迫每个点degree9。这是来源构造计数推论，不是本轮literal度数统计。

官方来源：[D4说明页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html) 将该图归于 Francesc Comellas（2026-10-21），说明基图1700来自W(7) incidence的Z2 lift与spread twins，之后进行了删边与插入交换。官方 [Sage脚本及预存结果](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD4/1768_comellas_SageMath.txt) 的结果头也报告1768/7956、全9正则、D4、非vertex-transitive；脚本没有运行。原作者不明的1700基图链接是 elder-plinius/V3R1T4S 的 G_9_4_n1700.edges。

当前1768的完整D4作为公开成图事实继承。因经历191条删边，不能仅从1700基图D4声称该性质自动保留；本轮也不做这项重验。

保旧边且最大degree9的任何连接扩点都需要旧点空位，当前固定图不存在这种空位。所以whole-neighborhood prototype或其它保旧边append入口已由既有证据关闭。本轮按Root指令停止，不重新profile，不转删边，不另拟模板。

实际literal尚未新绑定：官方细页的local edge链接解析到desc_g/adjacencies/adjD4/deg9D4_1768_.edges，一次读取返回404；没有继续尝试替代路径，也没有下载1700旧边表或1768完整图。这个literal缺口不会改变既有正则性计数与停止决定。

主表地址：[current table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html)。本轮主表数值与非bold状态由Root fresh确认；本子代理的网络读取仅为当前D4细页及相关来源定位。精确归因见 [PROVENANCE.json](PROVENANCE.json)。
