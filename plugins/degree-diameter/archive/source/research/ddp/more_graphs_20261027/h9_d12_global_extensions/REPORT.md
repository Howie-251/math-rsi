# 固定592条新 Q-line 批：32次完整扩张，建议图42377点

达到预先冻结的**32个新增点复评节点**，程序已停止。由独立验收的42345点、245253边图出发，依次接受32个完整degree12/D5扩张，最终建议n42377、m245637。每步新点均degree12，全部邻点加入前degree<12，完整邻集对实际当时base的R4覆盖通过；新增点邻集、旧degree及全部缺项路径保存在 `accepted_extensions.json` 和32份逐步JSON中。root已获增边序列，负责最后strongest graph的一次独立全源验收；本代理没有生成最后边表或运行全源BFS，最终实测直径暂不填写。

这批目标是更多完整图，不记录缺项分数的下降best。冻结问题、范围和停止条件见 `PREDICTION.json`；没有改历史42343/42345图或重跑旧7项覆盖。

## 精确范围与停止

源pool共有609个degree可行pinsets。只取其中新的592个10pins/cap2项，排除原7-item池所有仍出现的项；13个8pins/cap4项完全未执行。按canonical pins字典序一遍，成功后更新base供后项使用，失败前项不在laterbase重试。

| 项目 | 数量 |
|---|---:|
| 固定本批scope | 592项 |
| 已尝试且终态 | 367项，ordinals0..366 |
| 成功完整新增点 | 32 |
| 当时base下精确≤2anchors无解 | 280 |
| 因当时base已有满degree mandatory pin而排除 | 55 |
| 未测试 | 225项，ordinals367..591 |
| 当前半项UNKNOWN | 0 |
| 13个8pin项 / 原7项重试 / laterbase重试 | 全部0 |

**225项未测试不是失败，也不是全592或全Q-line族排除。** 280个精确失败仅针对记录的source_n/source_m和mandatorypins≤2anchor范围；后续改变base可能改变可行性，未据此重新试验。55个degree失败同样只对应当时实际base。到达32接受条件后没有继续原列表、扩大中心或增加第三anchor。

## 实际构造与可复用证据

每行重查actualcurrentbase的mandatory degree；合法时从完整10pins运行一次R4，缺项由 `range(source_n)` 全量取出，包括所有此前新加入点。随后仅对本项实际缺项targets作反向R4 BFS，枚举所有当前degree<12非mandatory顶点作为anchor。先精确判单anchor，再逐firstanchor与其未覆盖目标的coverers相交判第二anchor。全部≤2方案均覆盖，没有用oldbase的R4缓存拒掉新base可行项。

接受后的新点保留所有旧边；每条缺项补覆盖路径只用加入该点**之前**的base。若baseD≤5且完整新邻集R4覆盖所有旧点，则old–old距离继续≤5，新–old距离≤1+4=5。因此32步可数学归纳，给最终42377图D≤5的生产证书。root仍独立验证最终展开图，不将该归纳证明冒充32次全源BFS。

首成功为ordinal43、pool_index187，source42345，新增vertex42345的12邻点为

```text
136 4426 6854 10349 17862 18596 21339 26545 27264 27995 33782 40649
```

其中anchors为4426、26545；原mandatory缺项24个。最后一成功为ordinal366、pool_index305，新增vertex42376，使阶数到42377。完整32步都在 `accepted_extensions.json.records`，每条带source_n/source_m、新label、固定mandatory、anchors、完整邻集、邻点旧度、此前接受pool indices、全部补覆盖路径和CPU。最终m为245253+32×12=245637。

## 真实成本

首10真实项profile：CPU4.449551秒，10次mandatory R4、882次reverse R4，0接受，全部包含在同一批cursor中，没有重跑pilot。最终单worker CPU **97.650981664秒**，低于180CPU预算；312次mandatory多源R4、16079次缺项反向R4，共16391次有限radius4检查。55个degree排除项无需距离计算。新点1在18.117CPU秒被找到，32新增节点在97.643CPU秒达到。

第一次及阶段性新阶数已即时交root，不逐点刷完整长消息。没有外审、MIP、Lean、依赖安装、全几何重枚举、全源BFS或哈希。

终态 `ACCEPTED32_REVIEW_POINT`，scope结果全部明确；`pending`只保留root最后图的生成和唯一独立全源验收。新base初始信用与原source作者署名继承 `../h9_d12_followups/` 和Dharunish Yugeswardeenoo/Rishabh Rajiv的已有H9基础，本批是该规则下的明确有限整体扩张。

文件：冻结预测、`batch.py`、`profile10.json`、`RESULT.json`、`accepted_extensions.json`及32份 `accepted_XX_poolY.json`。本任务到此复评，不自动执行剩余225项或13个8pin项。
