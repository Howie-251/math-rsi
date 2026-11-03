# 唯一7532候选的fresh独立数学验收

2026-11-01。**PASS。** 完整字面图有7532点、97750边，max degree26，exact diameter3。H全部90525边保留，实际delta恰为17条diagonal clone–filler边删除与17条hub–filler边加入。全部289 clones与hub的普通新根BFS逐根命中原预测。原PRED、producer文件和root计数未改；这里只给独立验收，不宣称Lean或全球优先权完成。

## 1. 实际读取与绑定

接受的源H为7242点/90525边，经典旧U为标签0..7224，H的17个fillers为7225..7241。旧7531仅用于本次delta比较，不重跑其BFS。H、旧7531及新7532边表各打开并解析一次；新表header为7532 97750，所有body edges满足0≤a<b<n且严格全局lex，所以无loop/duplicate。

ORDERED_CENTERS的289个center依旧按index确定clone标签7242+index。diagonal用实际is_incident_flag与spread_index识别，其17个owner恰覆盖0..16，**不假设j=i**。

每个clone的实际邻居逐项等于N_H(center)∩U，也等于旧raw Cartesian neighborhood去掉center自身。17个flag行的raw25项含self，剥掉self后真N_U为24；其余272行真N_U为25。实际绑定全289行，无filler邻居，无clone–clone或clone–hub边。所有clone pins共7208个不同U点、最大load1。

精确set difference对旧7531只有：

- 删除(7225+spread_index,7242+index)，仅17个实际diagonal行。
- 加入(7225+j,7531)，j=0..16，hub没有其他邻居。

新表的H内部边逐条等于全部90525源边，缺失0、额外H内部边0。实际degree histogram为17:1、24:17、25:289、26:7225，degree和195500。7208条clone–U边加17条hub–F边与H90525相加恰为97750。

全部289绑定见ALL_289_CLONE_BINDINGS.tsv；实际删添列表及17个真实diagonal index/owner见EXACT_LITERAL_DELTA.json。

## 2. 直接覆盖全部点对的实际验收

old–old：新图保留完整H，所以继承已接受H的D≤3。

new–old和new–new：对全部289 clones及hub，运行290次普通queue BFS到radius3，覆盖全部7532点。对每个新根都检查全部目标，所以这已经与old–old继承合起来覆盖全图所有点对，并不依赖抽样或对称性。

|实际类别|根数|预测hist(0,1,2,3)|实际hist|
|---|---:|---|---|
|diagonal clones|17|(1,24,418,7089)|全部相同，逐项命中|
|off-diagonal clones|272|(1,25,441,7065)|全部相同，逐项命中|
|hub|1|(1,17,425,7089)|逐项命中|

hist预测错误数0，R3未覆盖点数0。原预测没有被静默修正。ALL_290_NEW_ROOT_BFS.tsv保存每根的actual/predicted hist及missing字段。旧根BFS=0，旧7531 BFS=0。

## 3. 为什么删掉17条边仍有完整路线，不依赖hub修补远对

以下纸面论证单独解释机制与prefix；它和第2节实际全点对验收分别记账。

### U与clones：保留原U邻域已足够

经典opposite GQ图U的D≤3接口由既有GQ结构继承，不重新检几何。其一般路线可写为：从(p,L)到(q,M)，选a∈L与q共线，取线B经过a、q；选b∈M与p共线，取线A经过b、p。则

\[(p,L),(a,A),(b,B),(q,M)\]

依cross-incidence给长度≤3的Walk；若相邻项相同，删除重复项即可得到loopless图中更短的真Walk。若所选点相同，取任一经过该点的线即可。这里用既有projection存在性，未枚举旧geometry或运行U根BFS。

clone x_c保留全部N_U(c)。到U目标t≠c，取U中c到t的≤3步最短路，替换首端点为x_c；到c本身用x_c–u–c，其中u∈N_U(c)，该集合大小24或25非空。对两个不同center，U距离2或3时同时替换两端点；距离1时用x_c–d–c–x_d的三步路线。因此所有clone–U及clone–clone路线都只用U作为内点，不需要任何filler、其他clone或hub作为未来内点。

### clone到H fillers：真正需要检查的删边影响

非diagonal center在H中没有filler邻居，N_H(c)=N_U(c)。H到任一filler的≤3步源路径首步就在N_U(c)，可直接替换成clone。

diagonal c=(p,S_j)仅邻接自己的filler F_j，此条clone–F_j边被删除。取经过p、不同于S_j的线M，flag u=(p,M)仍在N_U(c)，也邻接F_j。因此

\[x_c,u,F_j\]

是长度2的实际路线。

对另一filler F_l（l≠j），H中c到F_l有≤3步路径。它不可能首步走F_j：fillers之间无边，且不同filler的flag pinsets不交，故F_j到F_l没有1／2步路线。因此该H路径首步必须在U，仍能用clone替换首端点。删边不造成任何clone到其他filler的远对。

### hub路线

hub到所有fillers距离1。每个U flag (p,L)由其唯一spreadowner filler覆盖，所以到hub距离2。

对U非flag (p,L)，投影给q∈L与p共线，令M为pq线。flag v=(q,M)邻接(p,L)，hub–F_owner(q)–v–(p,L)给长度3。

每个clone至少保留一个flag邻居：off-diagonal center用同一投影构造；diagonal center取上述经过p、不同于自身spreadline的M，flag (p,M)仍是pin。因此hub经某个filler和这个flag到clone也至多3步。所有这些route都是具体旧H内点及目标clone，没有未来clone依赖。

## 4. prefix保证来自新的构造顺序

prefix定义为**从H出发直接添加modified clones，最后添加hub**，并非先接受7531后边删边加的单调过程。H的所有边始终保留。

添加任意当前clone后，以上clone–H以及与此前clones的U内点路线已存在，所以每个clone prefix均D≤3，且不依赖未来clone或hub。pin load≤1实际绑定、原H degree25及最终maxdegree26保证所有这些只加边的prefix不超cap；clones degree24/25，fillers在hub前保持25。

最后hub的路线只用H和当前clone作为端点，逐一成立；hub degree17，17 fillers各增加一次到26。无需从最终maxgraph的BFS删顶点反推prefix。

## 5. exact D3与实际非D2见证

本次授权的root7242 BFS实际得到target0距离3，并保存真Walk

\[7242\;—\;3145\;—\;1\;—\;0.\]

target0不在该根的0／1／2层，故是实际非D2见证；无需另外运行旧根。NON_D2_ACTUAL_NEW_ROOT_WITNESS.json保存标签与路线。

旧独验原本用Moore论证而未存具体old-U pair。本图同样有7532>1+26+26·25=677，因此maxdegree26也独立排除D≤2。这里不冒称存在一个可把hub也collapse回H的图同态。

## 6. 预算、边界与终态

总1.189883820 CPU秒／20，BFS0.921411620，wall1.221577秒，单worker；本次不需编译。全部进程已终态，未续timer。0field/旧geometry重验，0旧根BFS，0Lean/solver，0其他候选生成。

这次确实修改了17条已接受7531图中的clone边，因此不属于旧“所有已有adj固定”的饱和障碍scope；同时H的全部旧边仍保留。这是生成规则的具体改变，不能把本次成功解释为旧固定adj不可能性错误。

root STATE/REPORT/progress、Wiki、旧冻结包与计数均未修改。完整数学验收已PASS，后续具体Lean、公开比较及root是否计图仍由root收取实际receipt后处理；不自行扩展到更大q或下一图。
