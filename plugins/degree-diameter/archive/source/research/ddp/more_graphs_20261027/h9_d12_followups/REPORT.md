# 已验42343图的固定六条 Q-line 后续：找到42344、42345完整扩张

本批从已独立验收的42343点、245229边图出发，固定原pool的candidate1..6，按顺序只作一遍。**candidate4与5各找到完整新点**，逐步得到42344、42345点的构造序列；最后建议图有245253边、最大度≤12。完整邻集与覆盖路径已立即交root，等待root对最终展开图作唯一一次独立全源BFS。生产方没有生成最终边表或运行全源BFS，现阶段不提前填最终实测直径。

此任务由用户新的继续构造要求授权，研究问题是：新基图的捷径及度数消耗，能否使剩余固定几何线继续给出完整扩张？不是优化缺项分数。冻结范围和预测见 `PREDICTION.json`；旧42343历史图、参数和验收文件均未修改。

## 六项完整结果

| 原pool candidate | 实际base阶数 | mandatory缺项数 | 可用anchors | 结果 |
|---:|---:|---:|---:|---|
| 1 | 42343 | 82 | 14376 | 所有≤2anchor方案无解 |
| 2 | 42343 | 78 | 14376 | 所有≤2anchor方案无解 |
| 3 | 42343 | 90 | 14376 | 所有≤2anchor方案无解 |
| 4 | 42343 | 23 | 14376 | anchors1654、22911成功，添vertex42343 |
| 5 | 42344 | 22 | 14365 | anchors4648、30940成功，添vertex42344 |
| 6 | 42345 | 31 | 14354 | 所有≤2anchor方案无解 |

6项mandatory度数均合法；没有用旧42342/42343缓存代替新base的覆盖或可行性。4个失败项的单anchor交集为空，且每个允许first anchor都穷尽，与未覆盖目标的second-anchor coverers相交后全为空。失败仅针对各行记录的base和≤2anchors；前项未在后来base自动重试，不排除第三anchor、另一条线、另一个中心或改变旧图的情形。

## 两个完整新点

第一步source为已验42343图，添vertex42343，完整邻集为

```text
1654 1848 7419 10915 12357 15028 22911 23120 26376 29049 33855 37651
```

其中anchors为1654、22911，其余10点为candidate4的固定line像。所有邻点在加入前degree<12，新点degree12；23个mandatory缺项均有来自anchors的≤4旧base路径，详见 `candidate4_complete_extension.json`。

第二步source包含刚加入的vertex42343，共42344点，添vertex42344，完整邻集为

```text
3107 4648 5031 11356 14628 17832 19358 20154 28389 30234 30940 38487
```

其中anchors为4648、30940，其余10点为candidate5固定line像。该步同样全部邻点旧degree<12，新点degree12；22个mandatory缺项全部有≤4的当时base路径，详见 `candidate5_complete_extension.json`。保留全部旧边，所以最终m为245229+12+12=245253。

`accepted_extensions.json` 给出初始图、完整增边顺序、每步source_n/source_m/newlabel、12邻集、旧degree、全部缺项路径及最终建议n/m。root可只读此文件依次添加两点，不需重跑有限搜索或枚举52569条lines。

## 精确覆盖算法与归纳保证

每项先依据实际currentbase重新检查mandatorypins的degree，再从10pins运行一次完整多源R4。若仍有缺项，只针对实际缺项targets各运行一次反向R4 BFS，得当前degree<12顶点作为anchor时的覆盖bitmask。排除mandatorypins，先查1anchor，再穷尽每个firstanchor，交所有未被它覆盖目标的coverers以确定不同secondanchor。这是≤2anchors的完整判定，不按badcount选择或延长搜索。

接受条件是完整12邻集R4覆盖当时base全部点，且所有旧degree及新degree均≤12；保存的缺项路径只使用加入新点**之前**的base。旧baseD≤5和保留旧边保证old–old；新点到每个旧点经一个邻点加≤4步，故≤5。按两次归纳，数学覆盖证书给最后42345点图D≤5。这里仍将生产证书与root的独立最终展开图验收分开记录，不借用未来点证明较早一步。

## 成本与终态

实际单worker CPU **1.869369204秒**；6次全mandatory多源R4、326次缺项反向R4，共332次有限radius4检查。每项完整CPU和first-anchor计数在 `RESULT.json.rows`。未耗满180CPU秒预算。6项全部终态，无UNKNOWN，无追加line/center/anchor，不新增外审或Lean。

状态 `COMPLETE_FIXED6_BATCH`；生产结果为两个完整扩张、最终建议42345。`pending`只保留root最后展开图生成及一次独立全源验收；未将失败项外推成整个Q-line族无解。旧图出处与署名继承 `../../global_coverage_20261027/candidate42343/README.md`：Dharunish Yugeswardeenoo的42342原图及Rishabh Rajiv的H9/partial-fold基础仍获得原始credit。

文件：`batch.py`、冻结预测、`RESULT.json`、`accepted_extensions.json`、两个完整新增点JSON，以及6份实际base的mandatoryR4距离行缓存（255表示>4）。不创建哈希或校验清单。
