# 第二规模：346516完整图fresh独立数学验收

2026-11-01。**PASS：346516点、14204970边、max degree82、exact diameter3。** 三份边表各单stream，实际delta为65删65添，H全部13862745边保留；4225个clone的真实N_U全部绑定。65个changed diagonal clones与hub共66次普通新根BFS全部命中预测。4160个off-diagonal roots没有重新BFS，其未测点对由下述U-only及H路线证明覆盖，不能从旧maxgraph删除顶点或边的单调性推断。

## 1. 三个实际输入与精确delta

H是已接受balanced degree81源342290点/13862745边；U为其经典旧部分0..342224；fillers为342225..342289。旧degree82图为346515点/14204970边，仅作为本次delta输入。

新表header346516 14204970，全部unordered edge满足a<b和严格全局lex，无loop/duplicate。完整H、旧346515、新346516各打开并读取一次。新图H内部edge stream与完整H逐条相等，源前缀/后缀无遗漏。新旧图merge仅得到：

- 对每个真实diagonal h=65i+j（j=ovoid_owner[i]），删(342225+j,342290+h)，共65条。
- 加(342225+j,346515)，j=0..64，共65条。

其余14204905条旧346515边全部保留。实际ovoid、spread及owner来自已接受小表，不假设owner(i)=i，也没有重测域或小几何。EXACT_65_REMOVED_65_ADDED.tsv保存全部130个实际delta项。

## 2. 全部4225个真实U-neighborhood与degree

中心c_ij=585*o_i+S_j，clone标签342290+65i+j。由本次H stream收集每center在U中的实际邻居，并与新图每clone的全部实际邻居逐项比较：

- 65个diagonal clone真N_U大小80；H中原fullN的唯一filler已剥掉。
- 4160个off-diagonal clone真N_U大小81，恰等于其N_H。

4225行全部绑定，未从producer的passed cache读取pin结论。实际342160个clone pins两两不交，其union恰为U减去65个diagonal旧center；无filler pin，hub的全部65pins则恰为fillers。ALL_4225_TRUE_U_N_BINDINGS.tsv保存每个index/center/newlabel/diagonal标记及所有实际U pins。

实际edge分解为H13862745＋clone–U342160＋hub–F65=14204970，new–new边0。实际degree histogram：65:1、80:65、81:4225、82:342225，全部346516顶点逐项符合，degree和28409940。

65个旧D center保持81度；其余342160个U点增加一个clone到82度；65fillers失去diagonal clone边后由hub补回，到82度。新增clone分别80/81度，hub65度。这与字面结果一致，不是只按预计degree分配CSR后忽略未填满检查；每个CSR row都检查了实际完整degree。

## 3. 本次仅66个changed-root实际BFS

每个root均用普通queue作radius3遍历，不假定轨道、deck translation或类别对称。

|实际测量类别|根数|预先预测hist(0,1,2,3)|实际|
|---|---:|---|---|
|changed diagonal clones|65|(1,80,5250,341185)|每根逐项匹配|
|hub|1|(1,65,5265,341185)|逐项匹配|

未覆盖目标0，hist mismatch0。全部记录见ALL_66_CHANGED_ROOT_BFS.csv。

**off-diagonal的4160个根BFS=0。** root预测的(1,81,5329,341105)在RESULT中明确标为predicted_histogram_not_measured，不能列作实际分布。旧root、旧346515根及旧source根BFS也均为0。

## 4. 完整old–old/new–old/new–new证明

本节继承已有GQ projection及经典opposite graph接口，不重跑任何field/geometry/旧根BFS。与7532的成功机制相同，但实际大图binding及66根测量是本次fresh完成的。

### H–H：全部保旧边

H的已接受D≤3路线完全保留，故所有old–old对至多3步。

### 所有clones–U及clones–clones：只用U内点

经典U本身D≤3。一般构造说明：从(p,L)到(q,M)，取a∈L与q共线，B为经过a、q的线；取b∈M与p共线，A为经过b、p的线，则

\[(p,L),(a,A),(b,B),(q,M)\]

满足cross-incidence。若同点时任选经过该点的线；若相邻顶点相同，压缩重复项，得到loopless图中的≤3真Walk。这里仅引用已接受projection存在性。

clone x_c仍连全部真实N_U(c)。到U目标t≠c，取c到t的U最短路并替换首端点；到c本身用x_c–u–c（N_U(c)非空）。两不同clone的center在U距离2或3时同时替换路径两端点；距离1时用x_c–d–c–x_d。故**全部4225个clone**与U以及彼此的所有点对均有≤3路线，不要求重新BFS4160个off根。这些路线内点只属于旧U，不使用hub、其他clone或未来clone。

### 所有clones–fillers：被删65条边的实际影响

off-diagonal center不是flag，其N_H全部在U。因此任何H中center到filler的≤3路径首步在N_U，直接替换首端点即可。这个论证不继承旧346515 BFS可能使用被删边的路径。

diagonal c=(p,S_j)在H中仅邻自己的filler F_j，但clone不再保留该边。选经过p且不同于S_j的线M，flag u=(p,M)仍在N_U(c)，也邻接F_j，所以x_c–u–F_j是真实长度2路径。

对另一filler F_l，H中c到F_l存在≤3路径，不可能首步走F_j：fillers之间无边，且不同filler的flag-neighbor sets不交，F_j到F_l无1／2步路线。于是该路径首步在U，仍可把c换成clone。这覆盖包括65个changed diagonal在内的所有clone–filler对。

### hub–H与hub–clones：flag路线

hub到每个filler一步；每个U flag有唯一owner filler，所以hub到flag两步。对U非flag(p,L)，取q∈L为p在L上的投影，令M为pq线；flag(q,M)邻接(p,L)，给出hub–F_owner(q)–(q,M)–(p,L)三步。

每个clone在N_U(c)中至少保留一个flag：off-diagonal用同一projection构造；diagonal用上面(p,M≠S_j)的flag。所以hub到所有4225clones也至多3步。hub的本次实际BFS还独立确认了所有346516目标的覆盖。

这些类别覆盖完整全点对。尤其off-clone与其他旧点或off-clone之间的未BFS部分有明确U/H真Walk，不是从最大图删边或从少数代表根外推。

## 5. 每个prefix的正确含义

从完整H出发，按原4225index添加上述**modified** clones，最后加hub。这是新的生成顺序；不声称从已接受346515逐条删除边仍保持某种单调覆盖。

每次添加clone时，clone–H及clone–已有clone的路线均只用旧U/H作内点，故当前完整prefix已经D≤3，不依赖hub或任何未来clone。全部U pins实际load≤1，H degree81，clone degree80/81，所以每个只加边的prefix都不超cap82；fillers在hub前保持81，最后hub令其各加一次到82。hub路线也只用H加目标clone，不含未来内点。

最终66根BFS没有被当作这些小prefix的证明。

## 6. actual非D2与验收边界

在本次授权changed-root BFS中，root342290到旧U点0实际距离3，保存真Walk

\[342290\;—\;80145\;—\;5833\;—\;0.\]

target0不在其0/1/2层，故已有实际非D2见证，不另跑旧根。见NON_D2_ACTUAL_CHANGED_ROOT_WITNESS.json。结合上面的完整D≤3，得到exactD3。

总6.192139338 CPU秒／40，compile1.095122782、validator加driver5.079475184；validator完整binding4.78421、66根BFS0.227527 CPU秒。wall6.381810秒，单worker，全部子进程真实exit0，HANDLE终态。

0旧根/off4160 BFS、0field/geometry/projection重验、0Lean/solver/付费审阅，0下一候选。本次改变65条旧346515 clone边，位于旧fixed-adjacency saturation barrier范围之外，同时完整H源边全部保留。数学验收不认证公开优先权，priority仍由root保持UNKNOWN；已有远程原q8三目标的审阅状态不自动覆盖新346516。

root STATE/REPORT/progress、Wiki、旧冻结包与计数均未修改。NOTE/RESULT/TERMINAL、全4225绑定、实际delta、66BFS及distance3见证已齐，等待root收取本次receipt，不自动生产下一规模或Lean。
