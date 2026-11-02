# K19-equivariant matching：exact point-CNF与唯一shift gauge

状态：paper接口支持；0source/缓存数值读取、BFS、field、solver、Lean或ARIS。数值子目录 `exact_point_model/` 的唯一CNF/CaDiCaL批次由sole owner执行，本paper不启动或复核旧negative。源实际是two-vertex voltage lift，不是一个Cayley684假设。

## 1. 源作用、标签与left cache transport

继承实际684/2394、simple7regular/D4源。每个type τ∈{0,1}携一个H342，乘法与标签为

    (a,b)(c,d)=(a+23^b c mod38, b+d mod9)，
    label(τ,a,b)=342τ+9a+b。

旧边按h→h*s的right voltage规则生成，故同时left乘h_r是source automorphism。旧exact-length0..3缓存只需两个Hroot（每type的H identity）；要把其某旧endpoint h送到代表root h_r的对应endpoint，必须用

    h_r*h，

不能改用h*h_r。H非交换，方向写错会改变真实point labels，不能靠仅相位/距离统计掩盖。

取K=C19={(2k,0):k∈Z19}的left作用。它在source上free，每type18个K-orbits，共36个。可用(τ,ε,b)，ε∈{0,1}，作为orbit代表h_r=(ε,b)；实际编号顺序以保存的root mapping为准。点(k,r)表示(2k,0)*h_r，标签中的a=2k+ε mod38。因而K坐标是parity分解后的唯一k，不是错误地在Z38中求不存在的2的乘法逆。

两Hroot的actual point缓存先按left h_r展开到全部36个Kroots；再把每个实际endpoint唯一分解为(k,r)。由此定义

    A_a(i,r)={k∈C19 : 从root_i有真实旧length=a walk到(k,r)}，a=0..3。

它是distinct endpoint set，不是walk multiplicity；A0只含同root的0点。oldwalk可有回退，仍是真实walk且长度明确。不能只留一个“≤3可达”集合后同时当作0/1/2层；每个budget必须实际对齐。

## 2. K-equivariant perfect matching的完整choice域

从copy0到copy1任意K-equivariant bijection必且只需

    M(k,r)=(k+t_r, σ(r))，

其中σ是36个orbit的permutation，每row r有一个t_r∈C19。理由是M(root_r)先确定某targetorbit与坐标，equivariance即确定全部19个点；point bijection恰要求targetorbits不重不漏。

σ无需involution，t也不需自逆。无向matching的reverse只是

    M^−1(l,s)=(l−t_(σ^−1(s)), σ^−1(s))。

每个row(r)有36·19=684个候选choice(r,s,t)，每个target column(s)也有684个候选。每row与每col恰选1，选中的是36个orbit-choices，每个展开19条physical matching边，总684条；不是把684个choices都设为true。旧两copy边全留，crosscopy边不会与旧边重复，joined graph1368/5472全8regular。

## 3. 一次cross与Minkowski-set hit是精确点条件

任意≤4跨copy路只有1或3次cross。三cross时至多1条oldedge，必有相邻两matching步而立即沿原边回退，可消去。因此每个≤4跨copy可达point都有恰一次cross、总old步≤3的路线；不需要M与旧步交换或假定fibre affine。

从copy0 root_i出发，a步旧prefix到(x,r)，选中choice(r,s,t)跨到(x+t,s)。K-equivariance of source使b步suffix到target(k,j)当且仅当

    k−x−t ∈ A_b(s,j)。

故该choice在oldbudget≤3中命中实际target(i,j,k)的充要条件是

    k ∈ union_(a,b≥0,a+b≤3) [ A_a(i,r)+t+A_b(s,j) ]，

加法均mod19。每个集合元素都可拼成真实旧prefix/cross/suffix Walk；反向任何一次cross路也按它的exact lengths落其中。相同target多次出现只在set/OR中去重，不拿walkcounts冒作distinct覆盖。这里是exact point条件，不是先前phase容量必要门。

## 4. 为何必须36 roots而非旧2 roots

一般新M只与K commute，不保证与整个H342 commute。旧source可从2Hroots传缓存，并不表示新joined graph只检查2roots即可。需要对36个copy0 Kroot、每个targetorbit j及每个k∈C19保留点覆盖。

由于oldsource与M均K-equivariant，对任意k0，同步left K移动两copy是整个joined graph automorphism：root_i覆盖所有targets就同时给(k0,i)覆盖全部targets。36root therefore覆盖所有684个copy0来源点和全部684个copy1目标。图无向，reverse crosspair距离自动相同，无需误强制σ自逆。samecopy旧点对D≤4由全部旧source边保留继承，故这些cross point约束通过后就是joined graph的完整D≤4条件。

## 5. CNF exactly-one与positive cover的精确性

每个choice有一个Boolean X_(r,s,t)。36个row、36个column各用一个ALO加Sinz sequential AMO，恰表达前述permutation+shift域；AMO只取“任意两个不能同时true”，不需要其辅助变量唯一。

标准prefix AMO具有以下双向投影：若一组最多一个true，以“此前是否出现true”给aux可满足；若有第二个true，carry已迫此前prefix为true，与该处overflow子句冲突。再加ALO，existentially消去aux后恰为exactly-one。每组684是候选数，不是selected数。

对每个实际(i,j,k)，加一个正OR：所有满足第3节hit条件的choice变量之∨。在所有row/col exactly-one成立时，这个OR为true恰表示实际M有一次cross route命中该target。不同old splits/同一choice的重复命中可去重；空OR必须作为false保留，不能删掉。

因此整个CNF（含下面合法gauge）SAT当且仅当存在该K-equivariant matching使两copy图D≤4。不能把LP松弛、每target分别选不同σ或每row某choice能命中替代同一全局matching同时满足全部OR。

## 6. t_0=0是实际图同构gauge，但σ(0)=0不是

给任意合法M，令t_0为row0的shift。只在copy1后compose同一个全局source automorphism left K(−t_0)，copy0保持不动。于是

    M'(k,r)=(k+t_r−t_0, σ(r))。

copy1旧边由source left action保持；cross edges逐一送到M'，所以两joined graphs同构。K循环/交换，后compose的leftK shift与K action commute，M'仍K-equivariant。所有t同时减t_0，row0新shift0，σ完全不变。

因此可将r=0、t≠0的choices禁掉（或仅创建t=0 choices），不丢任何本模型图同构类或D4解。这是实际source action，强于仅商容量column permutation，但不需要source684 vertex-transitive。

leftK固定每个K-orbit，不能改变σ(0)的targetorbit。**不得同时设σ(0)=0**；本paper没有其它normalizer WLOG。也不能对每个targetorbit各自独立作shift：只有同一个全局leftK源automorphism已被此处论证，独立shifts未证明保持source edges。

## 7. 求解输出与scope

若SAT，需抽取36个actual choices、展开全部684条点matching，手检row/col/gauge及全部actual point cover/literal joined graph、degree/oldedge retention，交root/fresh接受。数学CNF exact不等于未验SAT字符串或新graph已接受；newformal只有root另行触发，不预编旧kernel。

若rawUNSAT，只保其实际solver/证据边界，范围为固定source、K19-equivariant perfect matching（含t0 gauge不丢域），不是任意point matching或一般8/D4。若timeout无SAT witness则UNKNOWN，不能借旧H-equivariant No改成K-equivariant No。没有phase/fibre新模板或其它K/seed自动续算。完成paper即停，0新图/参数/Lean/record计数。
