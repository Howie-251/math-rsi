# Twin-class八F-packet容量门：上界与greedy等价的纸面检查

只读 NEXT_STRUCTURAL_READ_GATE.md/json、旧FP_MODEL的labels和FP_once.py生成器必要段；未读FP_MODEL_MATRIX系数、A2/source邻接或任何packet数组，未运行DP/solver/BFS/field/图。纸面未发现本上界及root所提greedy优化的缺口；实际pair数据/终态仍由root sole数值回执决定。

## 1. 原变量语义与class quota

旧代码69–93行：每F最多一cut、每P最多一cut、starP必须有donorcut、总cut8、starP2；coverage coefficient来自原source闭R2。每个cut_FP(f,p)列的F-target覆盖只依赖f，star_P(p)列则依赖这个实际p。

65个class各有两个twin-P及共同8个F；这些F_c分割520F。对原合法选择，令k_c为该类选中的不同F数，h_c为指定两starP落在该类的数，则

`0<=k_c<=2, k_c>=h_c, sum k_c=8, sum h_c=2`。

反过来，对每类任意1/2个不同F，都可分配给1/2个不同P并包含该类指定starP，因为两个P都邻接整类8F；跨类不冲突。因此520binary y_f及130实际starP变量的这项计数投影支持旧F-cover语义。两starP可以在同一个twin类（h=2），不得无依据只留不同类pairs。

旧1040cut列不是1040个不同F选择：同一F的两个P-cut列coverage相同，而且F行禁止同时使用。应按实际F标签取得520个C_f，再按actualtwin映射分class；不能把一个F的两个cut列当两个不同donor。模型开头cut labels就有同f=1分别配p=0/585的例子，说明不要猜P连续编号或p//2就是class。

## 2. 为什么T是严格有利上界

固定两个不同实际starP标签p,q，D_p/D_q为各自source闭R2到F的mask，U=F\(D_p∪D_q)。设合法cut选择在class c选S_c⊂F_c，|S_c|=k_c。若F-cover可行，必有

`|U| <= |union_(c,f in S_c)(C_f∩U)| <= sum_c |union_(f in S_c)(C_f∩U)| <= sum_c m_c(k_c) <= T(p,q)`。

其中m0=0，m1为单F mask∩U的最大大小，m2为两个**不同F标签**的mask并∩U的最大大小。类内重叠已精确并，跨类重叠被忽略，所以只会高估。故T<|U|能严格排这一starPair；T>=|U|只说明这个界尚未排，不能声称真实F并覆盖，更不是651图或后续PP/旧旧D3。

m2须保真实F身份。两个不同F可以恰有相同packet mask，不能因为按mask去重只剩一项而把cost2写成不可用；这是会低估上界的实际实现风险。反之不应报告同一F重复为合法donor。标量最大值与最终真实prototype是不同事情，本门没有生成prototype。

130个D_p不能仅因同类FP-neighborhood相同就并成65个：twins的PP邻点可能不同，D_p的R2-to-F范围未证明相同。必须使用实际star_P列。只有实际packet/hprofile已绑定相同才可讨论等价计算；本paper不做这种合并。PP repair原已存在边的underdegree9合法分支不改变本F-cover门：repair端均非starP，z到F若用新增PP repair至少4步。

## 3. root的top-six边际优化确等价于小DP

每类有8个不同F，故给最大单包再补任意另一个F可得m2>=m1；两个包各自大小<=m1又给m2<=2m1。因此

`Delta1=m1 >= Delta2=m2−m1 >=0`。

这是标量profile m(k)的离散凹性，不要求达到m1的F包含于达到m2的双F中。先放mandatory h_c，baseline=sum m_c(h_c)，剩余cost正好6。每类h0可用Delta1/Delta2，h1只剩Delta2，h2无剩余边际。

按value取全局最大的6个可用边际，并在同class同value时优先first再second，结果自动满足class内prefix precedence：若second入选，first value更大或同值排在其前，也必入选（或已在mandatory baseline中）。所以这个选择达到忽略precedence的top-six和上界，且本身又合法，恰为DP最优。所有类总容量足够8，零边际也可填满exactcost；不应仅取positive而误少于6个。

mandatorycost不是事先固定某几个F。若最后某类cost从1变2，必须按最终cost重取该类单/双argmax；不能要求原best single不能撤。这不会破starP donor条件，条件只要求同类数量，不指定某个F。最终即便得到各类argmax，它们跨类真实并集仍可能大量重复；greedy精确的是**容量上界DP**，不是原cover或cut/repair解。

## 4. 完整pair域与停止范围

两个starP是130个实际binary标签中的任意不同两点，所以unordered域为C(130,2)=8385，其中65个同twin-class pair不可漏。p/q交换不改变D并与h，故无序即可；没有额外source对称归一化。必须分别记录实际访问/未访问pair。

若8385全部严格T<|U|，才可关闭该八FPcuts/两starP规则的必要F-cover子问题，从而拒绝其所有PP repairs（含旧PP边不重复添加的分支）；原20秒MIP的UNKNOWN仍保为当时raw历史，不冒作当时UNSAT。若有pair通过，结论只是容量门不够解释旧UNKNOWN，不自动续MIP/配15repairs。预算中断则未查pairs UNKNOWN，不能用已查部分的最大值外推全族。

闭域仍固定actual10D3/650源、八个不同F/P donor cuts、两starP为donor、六余P配repair及newroot10pins，非一般651图或任意10D3改图。此次只为root现有一次finitegate提供证明，不开启第二模型或新参数。本文0系数/packet读取、0source/A2/BFS/DP/solver/graph/Lean/外审，完成即停。


## 5. 实际容量终态：上界全过，没有得到F-cover

本节只读容量 `run_once.py` / `run.cpp`、RESULT及首见证的小metadata；没有重新读取COEFFICIENT_BINDING的mask payload、旧NPZ/source/A2，亦未重算8385 pairs。实现按实际F分组、每类枚不同F的28个双包；greedy按边际value降序，类内同值first在second前。尾mask保520个实际F位置。没有发现与上面上界证明不一致的步骤。

实际RESULT为8385/8385完整访问，upper-pass8385、upper-fail0、最小 `upper−residual=46`，`actual_F_cover_found=false`。root已读取的系数绑定报告C_f均72、D_p均86，65对twins的D列全部不同；这里继承该实际绑定，不重新读系数验算。不得合并同类两个star-P。

首pair实际P标签0/73：U有366点，上界T=449；按各类argmax取出的八F，其在U中的真实并只有337，尚缺29（总F覆盖491/520）。449是忽略跨类重叠后的容量之和，337才是这一个八F选择的实际residual覆盖。这个见证不能排除同一starPair的其它八F，更不能排F-cover全域。容量门的结论只是**该容量障碍未排任何pair，且本次未找到F-cover对象**；不把上界通过冒作cover，也不把argmax失败冒作无解。容量阶段累计23.728512182/45 CPU，原1170变量窗口的UNKNOWN原样保留。

## 6. 650binary投影代码与整数还原

只读后续 `../projected_F_cover_once/run_once.py`、MODEL中的labels/bounds及实际RESULT/SOLVER_RETURN；未读取MODEL_MATRIX或任何cover coefficient数据。独立数学依据见 [PROJECTED_F_COVER_EQUIVALENCE.md](../PROJECTED_F_COVER_EQUIVALENCE.md)。该文保留“未启动”的写作时历史；本节记录后来已实际完成的一次窗口。

代码确实建520个y_f和130个实际z_p，binary上下界0/1。每类65条 `sum y<=2` 与65条 `sum z−sum y<=0`，两条总数等式8/2，520条原F目标覆盖下界1，共652行。列循环将C_f加入该F变量、D_p加入该实际P变量；mask bit位置按既有F_labels对应cover行，而不是以实际vertex label直接当bit位置。650/652/50440为实际模型metadata，与代码声明一致；本paper没有独立重算nnz。

整数投影是精确等价：旧cut模型中令y_f为该F所有cut变量之和，旧F容量保证binary；同类两个P的容量给k_c=sum y<=2，star必须donor给h_c=sum z<=k_c。覆盖列对同一F不依赖donor P，因此覆盖值不变。反向，对每个K_(8,2)类，取k_c个已选F以及h_c个指定starP，选择大小k_c且包含这些starP的P集合并任取双射。`h_c<=k_c<=2`保证可做，类间F/P不交，合并后恰八条F/P端各异的实际FP cuts，原520条cover值逐项相同。故本模型不是悄悄放宽的整数覆盖条件；但未声称LP relaxation等价，亦未承诺压缩必然更快。

**同一y/z不唯一确定实际cuts。** 每类合法还原数为：k=0时1；k=1,h=0时2；k=1,h=1时1；k=2时两个F到两个P有2个双射，不论h为0/1/2。最多八个非空类，因此安全上界为2^8=256种指派。一个按label排序的canonical还原足以展示F-cover的存在，却不能代表所有指派的P距离或旧旧路线。若该指派的后续图失败，只能拒该实际指派/已测repair范围；不能排同y/z其它指派，更不能把该整数primal改记为不可行。

每个实际指派余下六个非star donor P有15个无序perfectmatchings。已有PP边保留为一条simple旧边、不重复添加；相应端点可以为degree9，目标只要求maxdegree<=10，不能据“未全10regular”删除这些分支。不同donor指派和不同PP配对会改变删边及修补路线，F-cover等价不保证最终z到P或old-old D3。是否逐项继续只由实际授权和剩余预算决定，本paper不启动它们。

## 7. 投影窗口实际终态与停止结论

`projected_F_cover_once/RESULT.json` 与原solver return实际为status1，Time limit reached，primal=None/incumbent=null；solver CPU18.007674689，完整process CPU18.28768091，累计42.316193092/45。确实是新投影的一次18秒feasibility窗口，未续旧1170变量solver。代码仅在非空primal时做整数/652行/520实际mask并检查；本次该分支未进入，故0 F-cover对象、0donor/PP枚举、0候选图/BFS。

结论保持 `UNKNOWN_PROJECTED_F_COVER_NO_INCUMBENT`。这个raw限时结果既不证明F-cover不存在，也不证明精确压缩无效；容量8385全过同样不证明存在。旧窗口UNKNOWN、容量必要门通过、新窗口UNKNOWN分账保存。root已决定停止650，不第三solve、seed或下游图套件。此独立检查0新数学数值、0系数/source/A2读取、0solver/BFS/field/Lean/外审。
