# 排除与证书：原模型、数学方向与实际输出

本页为具体研究工具。每个NO有对象／操作范围；容量模型可行不意味着图存在。原始源码和失败见证在archive，按[来源地图](source-map.md)定位。

## 1. Controller投影先于field优化

任何fiber路径投影为controller walk，内部fiber边投影为停留。控制器间distance>D时，无fieldchart能用≤D步修复。无fiber 内部边、rregularcontroller、每dart最多q个目标时，非邻distinctpair缺NB3就没有真正三步walk，≤2贡献至多rq²；q>r时不足q³。r6/q9给486<729，排这类actual完整 fiber lift。

控制器某顶点不在triangle中，则≤3返回同fiber只有zero和r个两步backtrack。真逆relation使offset相消，每个backtrack只给过源点的一条q点line，所以同fiber≤`1+r(q−1)`。Michel120/r6/q5为25<125，不需要生成15000点图，且允许edge-local invertible maps与相容offset。新增fiber 内部边会改变此分类，旧NO不自动继承。

## 2. 固定C60/F4：global失败，edge-local成功

五conicdirections、全F4 line、齐次linear真逆、原literalC60。global按port共用chart的57600projective三元组完整失败；不排edge-localchart、offset或不同frame。逐150undirectededge选chart解除共享约束，reverse用actualinverse，7200selectors联合选择，得到3840/degree20/D3。

在这个固定homogeneousC60域，D≤3 iff300dart pencil全五平面且3300equal/nonadjpairs各有rank3 NB3。rank必要性由literal路线词计数给所有低rank像并≤61/64。triangleedge仅多一NB2 plane：若缺pencilplane，四plane覆52；额外plane不含commonline最多补3。若恰是第五plane，则闭triangleword及反向都rank≤2，同fiberzero覆盖≤`1+5·3+2·15=46`，仍失败。故后来proof将最初“trianglepencil仅充分限制”加强为必要；不要把历史PRED与后继定理混为矛盾。

实际finiteSAT是该明确证书的模型；原始 UNSAT未有proofcheck按其证据强度报告。SAT必须重查完整CNF、dartinverse、directions、pencil和所有实际rankroutes，再生成graph。

## 3. Semilinear nucleus-C4：条件工具成立，两个controller失败

F4conic `L∞=(0,0,1), Lt=(1,t,t²)`，nucleus N=(0,1,0)，fiber 内部加N、wN，cross为full4line。T_e=A Frob_s additive semilinear，permutesconic，transportsourceportline非零比例到reverseport，fixNline系数α，reverse为真逆；每dart需 `{1,w,α,α Frob_s(w)}=F4*`。reverse coefficient为`Frob_s(α^{-1})`。

则fiber graph degree22，D≤3 iff控制器直径 D≤3且每控制器距离恰为3的点对至少一个GOODword：`π_middle(incoming)≠outgoing`。distance0用五tangentplanes；1用四secants＋tangent；2用secant的四nucleuscosets；3满rankword覆盖。齐次source0时badconicword的噪声平面都是不含N的secants，哪怕全部并仍漏N，所以GOOD必要。任意offset或不保conic的map不能继承这项必要性。

Exoo72与Michel72在uniquecontrollerword处出现Hall冲突；内部C4无时间修复distance3pair。conic24map域放宽到全部120quotientbijections（加入第五nucleus方向）确能修Exoo一个旧空域，但别处仍3rows→2columns。两实际控制器被排，不否定上述conditionaltheorem或其他controller。

## 4. 删除相邻两点后的边界匹配

Exoo72girth5源删adjacentu,v，A=N(u)\{v},B=N(v)\{u}共8不同且H中independent，每点spare1。保其他旧边、max5的任意新增old-old边只能为边界部分匹配；可补成完美匹配，不增距离，所以全部105完美匹配足够覆盖该操作。

纯跨侧24类旧uniquecrosspair必须directmatching；改成same-side后该论证失效，51–59–36–18实际反例修了旧pair。正确exactboundary条件：`dH(s,t)≤3 OR dH(mate(s),t)≤2 OR dH(s,mate(t))≤2`。新edge居中或两个新边在≤3内都需要旧boundaryedge或matchingbacktrack，不提供新路。旧24×180与新增81×180分开，总18900assignments全失败。范围不含nonadjacent删点、进一步删旧边、别的source或一般70controller。

## 5. 共享参数冲突：global256完整域

固定group RIGHT law `(a,b)*(c,d)=(a+c,b·3^c+d)`，a模8，b模32（不是F32），四positivephases1,2,3,4及四normal。合法oddunit归一给61440tuples，4096断连，57344连通，保degree7alias与degree8两类。

实际≤3word在八phase的distinctforms数46..63都超过32；每phase独立都有参数覆盖32。完整tuple检查却无共同R3全满。后读全57344行发现最小不相容subset{0,2}：独满320/1344，共满0；properwitness例如b[1,1,2,23]给phase0满，b[1,0,2,10]给phase2满。它证明共享连接选择不能同时满足，不是缺word数。只排该固定作用/phases/全局 normal 参数，其他Cayley256／edgevoltages不在内。

原包缺该逐tuple TSV，但completegatecpp存在，可在任务副本重建。此重建是有界完整族replay，不是默认每次加载技能就运行；未实际重建时用原scope及savedreceipts，不伪称TSV已随包。

## 6. Helper容量与等号分析

**Brown57 cap9固定旧诱导图。** 源8点degree7、49点degree8，总spoke 预算B≤65。任意helperH，sizei=s_i，degreeK≤9−s_i。每helper两步覆盖57旧目标s，必要57≤9s_i+Σneighbor s_j。求和：`57h≤18B−Σs²≤18B−B²/h`。h≥16时可代B65，需`57h²−1170h+4225≤0`，但h16值97且整数差分114h−1113正，故h≤15,n≤72。没证明72可构造；允许新增old-old边超出旧诱导不变范围。

**Brown91 cap11。** A10/I36/E45，spare2/1/1，B≤101。闭旧coverage c(S)≤10s+1−a，非共线≤9s+3−a。总量先给h≤16。h16时每旧点需owner，非absolute唯一，Iowner size≤6,Eowner≤8；所有helper s≤8。设d=11−s,e=max(0,s−6),δ=max(0,91−c−6d)。真实助手覆盖给Σδ≤Σed，逐几何组给`ed−δ≤4s−a−24`。对16组求和≤`3(B−101)≤0`迫B101且helper度数全部饱和。总degreeH=16·11−101=75奇数矛盾，所以h≤15,n≤106。DP只是发现／核证书的工具，不能把scalar通过当图；解析等号矛盾已足够，无需生成helperH。

## 7. 106→107内部重连的exact模型

固定源106/582、spareT={34,54}degree10，其余11。任何107/max11/D2点degree≥10（根两步≤1+11deg）。选10或11pinsS，新z只连S，只允许修改旧G[S]。

x_v表示selected，y_uv表示finalinternaledge，`y≤x_u,x_v`，不强制clique。z-old iffsourceclosedDom `x_u+Σ_{w∈N(u)}x_w≥1`。selectedv最终degree `d_v−Σ_N(v)x+Σ_y+1≤11`。对每orderedoldnonedge(v,u)，exactmixedroute条件：

```text
(1−x_v)+x_u + Σ_{w∈N(v)∩N(u)}(1−x_w) + Σ_{w∈N(u)}y_vw ≥1.
```

selected-selected经z，outside-outside保所有旧路，mixed只由上述outside旧middle或choseninternalmiddle承担，不能漏directselected点的closedDom。t_e=xuxv用于真实oldeditobjective，6253binary=106x+5565y+582t。实际10秒HiGHS无incumbent UNKNOWN，不排一般internal-S。

source真实C7的invariantS=one7orbit+3/4fixed已由更强paper排除，即使最终内部重连不保C7。非invariant两种one-departure形状10976全在Dom／crossdegree前门失败，0DFS；这两个NO均不关闭generalUNKNOWN。

## 8. Mizuno13完整affine27块的exact dual

本节范围是每个被选原 fiber 至多一个完整27点 affine W-横截块，斜率与相位可依 source 选择；不是同一 fiber 任意多个块。源88452=364×F3^5，四inputdirection为同W的所有projectivelines。同fiber任意disjoint完整邻域中心≤27；81plane方案不可能。局部27transversal可修M重叠，但joint目标法向独占／volume迫controller行。全364source-dependentaffine3space/27完整块的必要模型：每targetordinaryincoming＋matchingmate≤3，源成本203个5/161个6，总cost≤1092。matchingmate也是ordinaryprovider，使每控制器行有coeff2,1,1,1。

exactdual用365row非负multiplierY和364upperboundx≤1的Z，denominatorQ10000。每列ΣA_ijY_i+Z_j≥10001≥Q，RHSΣb_iY_i+ΣZ=2061908。因此QΣx≤RHS<207Q，整数T≤206，至多5562clones，n≤94014，不能达94186。几何必要性与整数combination分别承担证明。

[薄replay](../tools/replay_mizuno_dual.py)读取presentMODEL重建缺失LP_INPUT行，并验证每列、符号、RHS与saveddual一致。无solver、不生产图、不写源；见[实际案例](../examples/mizuno-exact-dual.md)。非lineartransversals、部分块、别的N规则不在NO范围。原始MIPrawinfeasible与后来exactdual是两条证据，不倒改原状态。
