# degree83／350742：k2唯一候选fresh独立数学验收

2026-11-01。**PASS：350742点、14547195边、maxdegree83、exactD3。** 两块各4225个clone均逐项绑定到原H restricted-to-U邻域，完整H及accepted346516旧边保留；只做预先指定的68个新根BFS，全部距离hist和same-center／hub距离预测匹配。以下明确区分实际测量与全点对纸面覆盖，不重复旧根或其余4158个newoff根。

## 1. 实际边表、两copy标签与原始pin绑定

三个literal输入各单stream：原H342290／13862745、accepted346516／14204970、新350742／14547195。新表header/body一致，所有edge满足0≤a<b<n且严格全局lex，无loop/duplicate。

U标签0..342224，原fillers为342225..342289。中心h=65i+j为585*o_i+S_j，diagonal条件j=真实ovoid_owner[i]，不假j=i。第一clone是342290+h，第一hub346515；第二clone是346516+h，第二hub350741。

完整H body逐条相同，accepted346516的全部14204970旧边也逐条保留，没有删除或额外old–old edge。新增342225边全是第二clone–U342160条及第二hub–F65条，新增new–new边0。

从本次H stream独立收集每center的N_H(c)∩U，与**两个copy blocks**全部实际邻居比较，共8450行PASS。diagonal 80pins，off-diagonal 81pins，两个copy在相同h的pinlists完全相同且非空；不同h的pinsets两两不交。每copy的pinunion为342160个U点，恰为U减去65个diagonal旧center。实际两copy使这些U点负载2，65个旧D负载0；fillers负载来自两个hubs，亦为2。

完整绑定见ALL_8450_BOTH_BLOCK_TRUE_U_N_BINDINGS.tsv。旧source geometry表只是小recipe输入，未重算field、projection或旧geometry结论；pin正确性来自实际H与新候选的逐项stream绑定。

## 2. 实际degree及计数

|degree|顶点数|来源|
|---:|---:|---|
|65|2|两个hubs|
|80|130|两块各65个diagonal clones|
|81|8385|65个旧D＋两块各4160个off clones|
|83|342225|342160个被clone覆盖的U点＋65fillers|

实际edge分解为H13862745＋两copy×342160＋两hub×65=14547195；degree和29094390。每个实际CSR row都核对已填满且degree符合，不仅比较总degree。

## 3. 预先选择68根，而非按结果选择

PRESELECTED_BFS_ROOTS.json在读取候选和BFS之前写出：65个第二copy实际diagonal，actual first two off indices **h=1、2**，以及第二hub。共68个普通queue radius3遍历，旧根0，第一copy根0。

|实际测量类别|根数|预先预测hist(0,1,2,3)|实际|
|---|---:|---|---|
|second diagonal clones|65|(1,80,5251,345410)|逐根全部匹配|
|second off clones，h1/h2|2|(1,81,5330,345330)|两根均匹配|
|second hub|1|(1,65,5266,345410)|匹配|

R3未覆盖目标0，hist mismatch0。每根全部实际层数、预测、reached和same-copy距离见ALL_68_PRESELECTED_NEW_ROOT_BFS.csv。**其余4158个newoff根没有BFS**，没有把这两个样本作为它们的实测hist或对称性代表；其D≤3由第5节全部端点的证明覆盖。

## 4. 本次真正检验的新机制：同center两copy与两个hubs

67个被测clone根（65diag＋2off）到其第一copy的实际距离均为2；第二hub到第一hub的实际距离也是2。

完整8450行绑定还给出所有4225对same-center twins的严格距离2证明：两者是不同顶点、无clone–clone edge，且相同非空N_U，所以共享一个旧U邻点。不同center的clone pinsets不交，又没有clone边，因而不同center的clone之间无1／2路线；第5节D≤3接口使它们距离恰3。这解释“同center copy给B2新增一顶点”，无需对其余4158根另跑BFS。

两个hub的邻居都是全部原F，hub间没有边，故也恰好共享F形成距离2。hub到任何clone没有edge或common neighbor：hub邻居只在F，clone邻居只在U，而F∩U为空。于是D≤3时距离恰3。这一结构性非D2见证不依赖Moore或一个旧U特例，p>0/k≥1时适用。

在本次原定hub BFS内，实际得到

\[350741\;—\;342225\;—\;5265\;—\;342290\]

且distance(350741,342290)=3。HUB_CLONE_STRUCTURE_WITNESS.json同时记录literal domain分离与实际Walk，extra BFS=0。

另在原定新diag根BFS中得到distance(346516,0)=3，Walk346516–80145–5833–0，见NON_D2_ACTUAL_NEW_ROOT_WITNESS.json；没有为此跑旧根。

## 5. 完整all-pair证明，覆盖未测新根

### 所有old–old

accepted346516所有边完整保留，因此它的所有点对D≤3继续成立，包括第一block clones及第一hub。

### 所有clone–U与clone–clone

继承经典opposite U图的GQ projection D≤3接口，不重算geometry。对clone x_c到U目标t≠c，取U中c到t的最短路并替换首端点；到c用任意u∈N_U(c)作x_c–u–c。

两个不同center在U距离2或3时替换源路径两端点；距离1时用x_c–d–c–x_d。相同center的两copy如第4节共旧邻点距2。所有这些路线内点都在旧U，不要求未来clone或任何hub。它同时覆盖未测的4158个第二off根与全部旧/新clones的点对。

### 所有clone–原fillers

非diagonal center不是flag，所以N_H(c)=N_U(c)，任意H中center到filler的≤3路径首步在U，替换端点即可。

diagonal c=(p,S_j)到own filler F_j的被遗漏边，改走clone–(p,M)–F_j，M为经过p但不同于S_j的线，(p,M)是保留的U flag邻点。到另一F_l，H中的≤3路径不能首步走F_j：不同fillers没有edge或共同flag邻点，F_j到F_l无1／2路线。因此其首步仍在U，同样可替换为任一copy的clone。

### 任一hub–U／clones／fillers／另一hub

hub到原F一步、到U flag两步。对非flag(p,L)，取p在L的投影q及连接线M，flag(q,M)邻接(p,L)，hub–F_owner(q)–flag(q,M)–(p,L)给三步。

每个clone保留一个flag邻点：非diagonal用同一projection，diagonal取(p,M≠S_j)。故hub–owner filler–flag–clone至多3步，适用于每个copy。两个hub通过任一F相距2。

以上类别覆盖完整新图的所有点对。68根BFS是对新机制的额外实际对照；没有用两个off样本、旧maxgraph BFS或删顶点论证替代未测点对的证明。

## 6. 两种prefix都无未来顶点依赖

**从原H构建：** 添加两copy blocks的modified clones，再添加hubs。每个clone到H／当前其他clone的上述路线只用U/H内点；每个hub到当前图的flag路线只用H与目标clone，已有hub通过F可达。每个prefix已D≤3，不靠最后maxgraph删除顶点倒推。不同center N_U不交，最多两copy使U负载≤2，hubs使fillers负载≤2，故所有prefix degree≤83。

**从accepted346516构建：** 切换cap83，保留全部旧边，依次添加第二copy clones，最后第二hub。旧U中非D原degree82，每个只收到一次新clone边到83；旧D保持81。原fillers在第二hub前保持82、最后各到83；旧clones/hub不增边。

第二clone到旧第一clone用U端点路线或same-center共享邻点；到旧第一hub用clone–flag–F–hub；到已添加的第二clones用U路线。这些内点均已在当前图，无future vertex。第二hub最后的所有flag和F路线也已存在。因此每次插入保持完整current D≤3及cap83，而不是只验证一个最终图。

## 7. 成本、范围与终态

总5.825614568 CPU秒／40；compile1.114332931、validator加driver4.690340548；validator中完整binding4.40996、68新根BFS0.212694 CPU。wall5.952975秒，单worker，两子进程均exit0，HANDLE真实终态。

0旧根/第一copy/off4160或额外4158 roots BFS，0field/geometry/projection/Lean/solver/付费审阅，0下一k/84+。本次只读取已有实际H、accepted346516与唯一新候选各一次，没有重跑旧公开门或旧toy。

root STATE/REPORT/progress/Wiki、计数及冻结包未修改。新graph/parameter是否计入由root读取实际receipt后决定；本次不宣称具体Lean、已有A559/B/C覆盖新83或全球优先权。公开优势仍只是已核范围比较，精确fill/reallocation优先权UNKNOWN；不自动派下一候选。
