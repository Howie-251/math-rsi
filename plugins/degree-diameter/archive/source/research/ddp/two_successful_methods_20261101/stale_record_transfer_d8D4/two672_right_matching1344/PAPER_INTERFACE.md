# 经典Cayley672两copy＋rightmatching：exact identity-root接口

状态：纯paper，0数值、source解析/生成、word枚举、BFS、field、Lean或SAT/ARIS。f9独占旧scope与primary读取；本文件只接收其实际只读结果，不重复打开/下载原文或验证旧source。

## 1. 真正的672源，与684分开

cached primary `research/ddp/m1_sources/desc_g4.html` 的latin1第182–189行给former(7,4)672，Sampels，1997-07-29，paper DOI10.1007/BFb0024505；第184行的S7与root给定一致。源是H672的Cayley graph，坐标RIGHTlaw为

    H=C6⋉_39 Z112，
    (a,b)(c,d)=(a+c mod6, b·39^c+d mod112)，
    S={(2,73),(4,23),(5,54),(1,22),(5,71),(1,31),(3,42)}。

oldsource的simple7regular/D4在当前接口仅从published来源继承。本地尚未定位对应672完整literal或full-D4验收回执；不能拿684的源/labels/D4证据替代。若后续以112*a+b编码，只是此recipe的新canonical编号，不宣称已绑定作者NX标签。source inverse/no-loop/involution事实按既有published source前提使用，本paper不重算其数值；RIGHTlaw的inverse形式是 `(-a,−b·39^(−a))`。

f9的有限本地source/Wiki查找未定位same672/two-copy/all-right-t域的旧NO或UNKNOWN。未定位不是全局不存在证明；如history owner后来发现same-scope严格终态，应直接继承而不运行。旧684是H342的2-vertex voltage lift、非VT，全部H-equivariant匹配NO与本Cayley672不是同一输入或参数域。

## 2. 固定t候选与simple/degree账

保两份同一个G=Cay(H,S)的全部旧边，只加

    M_t:(h,copy0) ↔ (h*t,copy1)，t∈H。

right乘t为bijection，reverse是right乘t^−1；无需t自逆。copies不交，所以即使t=e也不是selfloop，旧边均同copy，cross边无重复。若source为simple7regular，则joined graph有1344点、5376边、全8regular。这里仅是条件参数账，不代表实际图已生成或已达D4。

## 3. 所有≤4跨copy路线恰由one-cross域决定

跨copy路线cross数为奇数；≤4时只有1或3。三cross加至多一oldstep，必有连续两个matching steps，沿唯一matching边立即回退，可消去。因此任何≤4跨copy可达target都有恰一次cross、总oldsteps≤3的路线。

令S^a为exact-length=a的generator-word endpoint set，S^0={e}。从identity copy0出发，a旧步到x∈S^a，cross到x*t，再b旧步到x*t*y（y∈S^b）。所以exact cross target set是

    U_t= union_(a,b≥0,a+b≤3) S^a * t * S^b。

乘积顺序不可交换，必须按实际RIGHTlaw计算；不能改成`t*S^(≤3)`除非另有t-normalizer条件。ordinary oldwords含回退/碰撞无妨：集合记录真实endpoints，反向任何元素都给≤4真Walk，因此这不是walk-count容量上界或概率门，而是exact point condition。

## 4. 为什么identity root足够且不要求rightshift是源automorphism

旧Cayley边为h→h*s，任意left乘g保持这些边。又

    M_t(g*h)=g*(h*t)=g*M_t(h)，

所以在两个copy同步left乘g，是整个joined graph的automorphism。所有copy0 roots由identity传递：从u0到v1在≤4当且仅当u^−1*v∈U_t。因此

    U_t=H iff 全部crosspairs距离≤4。

reverse crosspairs由无向性自动覆盖；也可用inverse-closed S得到U_(t^−1)=(U_t)^−1。无需candidate完整vertex-transitive，source的regular left H作用已经够用。

right R_t并非总是source graph automorphism。它仅在t^−1 S t=S时有该性质；那时模型是换标后的prism，U_t=t*S^(≤3)。因此不能把所有rightmatchings都按Cartesian prism判掉，也不能假设t与S交换。另一方面，所有**left-H-equivariant** source-to-source bijection都恰是某个R_t（取t=M(e)）；本672域有一条regular H-orbit，故672个t就是该equivariant matching域的全参数，而非684两orbit时的π/t0/t1域。

## 5. cross门与oldsamecopy的不同义务

保旧source边意味着samecopy点对可直接用旧Walk。只有已读published/实际binding提供

    S^(≤4)=union_(a=0..4)S^a=H

时，才能继承所有samecopy D≤4。不能因source名叫672就冒已本地full验收，也不能把exact-length4误当≤4。如果此source事实已绑定，joined graphD≤4恰等价于U_t=H；若U_t≠H，cross缺点已足以拒绝该t，不需另做samecopy验证。

positive时仍需actual recipe/原source/literal joinedgraph与独立验收；后续formal另触发，不预编旧kernel。negative时若完整672个t均未满，仅严格排固定此source的rightmatching（等价left-H-equivariant）族，不排任意nonequivariant point matching、其它source/oldedge edits或一般(8,4)。

## 6. 为什么选这一个对照与当前停止点

该source来自独立published7D4/Cayley recipe，regular left-action使全域只672个t的exact集合门；目的正是用tiny完整域对照K19的assignment/shift CSP，而非继续其UNKNOWN窗口或换SATseed。主表8D4当前1100只作root已查背景；1344从未在本paper登记为合法candidate或record。

当前只读scope尚无same-rule旧排除，数值仍须root明确门后由sole owner运行；本paper不执行sourcewords、t、图/BFS/field或额外模板。完成即停。
