# 固定两cut＋第三cut的四helper K1,3：精确路线接口

状态：paper支持以下有限门，当前0数值、source/矩阵读取、BFS、field、Lean或ARIS。source Conder1250/1875 simple cubic/D10沿用旧绑定，不重复source验收。

## 1. 旧scope读取与当前新域

旧 `d3_D10_conder1250_edge_insertions/ANALYSIS_PROOF.md` 的严格域是单细分及“两cut、两相邻helpers、各2pins”；本source interface中的第三cut pin-transfer规则仍只用两helpers，并撤回一个spoke另添oldoldrepair。对这些原始scope及同source目录/canonical关键词只读定位，未找到**三条disjointcuts、三leaf各保整cut双端点、centre只连三leaf**的已执行严格NO。未定位不是全repo不存在证明，但已知旧NO均不能直接套入本规则；若sole history owner另找到同域旧终态，应继承而不重跑。

本次固定e0={0,1}、eF={869,1178}，第三cut e2={g,h}避这四pins。三cut均为原source边，互不相交；Pi为第i条cut的两个旧端点。只删三cut，令T=G−{e0,eF,e2}。加三个leaf l0,l1,l2，每个li接完整Pi；加centre c仅接三个leaves，helper图恰K1,3，不尝试P4或其它拓扑。实际第三边1865域由sole owner绑定；本paper不枚边。

旧六端点各删一旧边、添一spoke，仍度3；leaf为2spokes+centre、centre为3leaves，均度3。因此1254点，1875−3+6+3=1881边，全3regular。没有oldoldrepair，也没有撤回某个cut端点的helper连接。

## 2. 四个新root的精确距离

记d_T(P,t)=min_(p∈P)d_T(p,t)，允许∞。helper内距离是centre–leaf1、不同leaf间2。不同leaf经T再到另一leaf至少需两spokes加旧腿，Pi不交使其至少3，不能比helper内2步短。任何到旧target的最短路取其**最后leaf**，此前段可直接用helper K1,3最短路替换；最后leaf之后只走T。因此精确有

    d_final(li,t)=min(1+d_T(Pi,t),
                      3+d_T(Pj∪Pk,t))；
    d_final(c,t)=2+d_T(P0∪P1∪P2,t)。

这不是只列几条可能路线的充分条件；反向每一项都是真实Walk，正向最后leaf分解覆盖了反复访问helpers/base的路线。helper之间距离已经≤2，不再另有新新目标障碍。

所以四newroots全部R10覆盖旧1250点的充要条件先可写为：

    R8_T(P0∪P1∪P2)=V(G)；
    对每i，R9_T(Pi)∪R7_T(Pj∪Pk)=V(G)。

所有R均为闭球，pin自身允许0步。各leaf的合作radius是7，不是旧相邻twohelper规则的8：从一个leaf经centre到另leaf再出spoke需3步。

## 3. 更强的last-cut引理：weighted leaf式也能精确替回G

**纸面纠正记录（未看新numeric）：** 初版在本节将“单个Pi距离不能各自替回G”误扩大为“weighted leaf minimum也不能整体替回G”。后者过强，已由root提出、独立核对的以下last-cut论证更正。原T公式始终正确；本节现给与它相等的G公式，不更改任何数值结果。

全pin集P=P0∪P1∪P2包含全部删除边的两端。若最短P→target旧路穿某条被删边，可从该边后一端重新起步得到更短路，故

    d_T(P,t)=d_G(P,t)。

因此centre门可精确用source `R8_G(P)=V(G)`，而不是仅必要放松。对leaf i，令group权重w_i=1、其它两个group权重为3。虽然单个 `d_T(Pj,t)=d_G(Pj,t)` 未必成立，但有更强且足够的weighted等式：

    min_j[w_j+d_T(Pj,t)] = min_j[w_j+d_G(Pj,t)]。

证明取右侧任意一项对应的G最短路，从某p∈Pj到t，长度L。如果不经过cut，已有T路径。否则取最后被删cut属于group k，上游r、下游s；设从p到r的prefix长m、cut本身1步、之后无cut的suffix长n，故L=m+1+n。最终图可从leaf i直接经helper-star到leaf k，再出spoke到s并接该suffix，总代价w_k+n。

除了j=i而k≠i以外，w_k≤w_j，显然不长于w_j+L。唯一增权情况w_k=3、w_j=1时，matching cuts使Pi与Pk不交，p≠r，所以m≥1，从而 `3≤1+m+1`，仍有 `w_k+n≤w_j+L`。这对最后cut之前曾经跨过多少cut都成立，不漏多次helper/base协作。反向因T⊆G，原weighted-T式逐项≥weighted-G式；结合实际Walk构造得到等号。

因此本三条matching cuts、每leaf保整条cut双端点的规则下，四root门可以**整体精确**写成

    centre：R8_G(P0∪P1∪P2)=V(G)；
    leaf i：R9_G(Pi)∪R7_G(Pj∪Pk)=V(G)。

matching和完整双端点分组是关键前提。不能从weighted等式推出各Pi单独删边前后距离不变，也不能把该替换迁移到前一pin-transfer/只保部分cut端点的规则。

一个具体失败分类：若centre门已通过，则任何target都有全P距离≤8。使用上述精确G式，leaf i失败恰须自身Pi的source距离≥10，另外两Pi的source最小距离正好8；这时其它leaf有近端点，但合作多出的两helper步使该leaf仍需11。保留所有pins消除了“撤回pin即丢该点”的旧P3障碍，并未自动消除这些远域合作预算。

## 4. 为什么旧twohelper NO不能经收缩直接推出新star NO

旧twohelper域要求两个newvertices都度3、互边、各两spokes，且只删两条旧边。把K1,3的centre与一leaf收缩，合并点会有4个邻点；再把两个leaf并入centre，合并点则有更多spokes，不落旧degree3/2+2模型。这样的收缩不保旧族。

若改为删除一leaf/centre、恢复第三条旧cut并让剩余leaves直接相邻，也不显然保持距离：原star使第三cut的两个pins可以经该leaf/centre快捷连接其它leaves，恢复它们之间一条旧边只恢复这两个pins的互通，不保这些跨区域helper路线。没有一个已证的distance-nonincreasing、fix所有旧点且落旧twohelper域的映射。故旧完整NO不排本四helper域，不能为省计算直接继承。

## 5. 四newroots通过仍需旧旧验收

旧source三条边已删除，oldold距离未由新root覆盖自动保持。第3节weighted lemma只证明helper-root到旧target的等式，不允许把下面oldold式中的全部T直接换G。对旧u,v，helper路线的完整分解是

    d_final(u,v)=min(
      d_T(u,v),
      min_i[d_T(u,Pi)+2+d_T(Pi,v)],
      min_(i≠j)[d_T(u,Pi)+4+d_T(Pj,v)])。

同leaf为两spokes，不同leaf要再经centre两边。它与前面四root条件合起来才是完整D≤10门。若sole finite批先查四newroots，只有通过者才值得完整oldold验收；不把newrootpass冒作新1254/D10图。没有给本规则套单细分的全径≤11定理，也没有从sourceD10盲继承新图exactD10。

## 6. 当前唯一可推翻预测与停止范围

预测：在固定e0/eF及合法第三边实际1865域中，至少一例使centre的source-R8全pin条件与三个leaf的source-R9/R7条件同时满足，即由last-cut引理四个新root完整R10覆盖。这是**合作覆盖预测**，不是只修1058或只让某个savedtarget成为邻点，也不是完整图成功预测。

若1865域完整均失败，严格只排固定这两cuts、第三cutdisjoint、helper拓扑K1,3、每leaf接整条cut双端点的域；不是所有三cut/其它固定cut/source/四helper拓扑。预算中断只能UNKNOWN。无论结果如何，不增加cuts、换seed或试P4，本paper完成即停。

## 7. 固定两cut实际负结果与下一全matching域

root随后报告：固定e0/eF的1865例实际全部centre覆盖失败，首thirdcut(2,6)给centre1253→old886距离11；没有进入以四rootpass认证新图的分支。该固定域的正向合作覆盖预测被实际完整门推翻，不能改称只是不够快或oldold损伤。本paper只衔接root实际回执，不重新读取/计算该数值。

下一唯一授权释放的是固定第二cut eF：仍同source、三matchingcuts、整cut双pins给leaf及K1,3；由source edgeVT锚定e0，遍历其余两条disjoint边。不是P4、更多cuts、新source或blindseed；全域的参数与exact门见 `GLOBAL_DOMAIN_PAPER.md`。第3节last-cut更正完整保留；当前paper不在全域结果尚未返回时声称wholefamilyNO。
