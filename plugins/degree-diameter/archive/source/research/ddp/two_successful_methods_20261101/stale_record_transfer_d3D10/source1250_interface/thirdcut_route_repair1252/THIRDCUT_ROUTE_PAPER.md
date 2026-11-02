# Conder1250三cut+repair：pin-transfer与精确路线门

状态：纸面接口支持；0数值、source矩阵读取、BFS、field、Lean或ARIS。只读旧 `research/ddp/more_graphs_20261027/d3_D10_conder1250_edge_insertions/ANALYSIS_PROOF.md` 的完整scope与数学公式，source1250/C1250.2的simple cubic、D10和edge-transitive事实继承，不重验。旧1251单细分与5614旧two-cut例的NO保持历史，不自动排新三cut规则。

## 1. 全三disjoint-cut规则与pin-transfer的等价

在源G选三条顶点不交旧边。repair只连来自两个不同cut的端点p、h，且p–h必须是**原G非边**。把这两个cut写作e={p,q}、g0={g,h}，第三条写作f={r,s}。剩下四个pins是q,g,r,s，分为两个2点集接两个相邻helpers a,b。若g分给a，写最终A'={g,u}、B={v,w}，其中{u,v,w}={q,r,s}。

先构旧two-cut候选J：仅删e、f，helpers相邻，A={p,u}接a、B接b；旧第三条g–h此时仍在。然后作

    H = J − {a–p, g–h} + {a–g, p–h}。

这恰是新三cut+repair图。反过来，从任意旧**两条不交**cuts的J选择一个helper spoke a–p，第三条旧边g–h避开原四个cut端点，取任一orientation作为g/h，要求p–h源非边；这个transfer必给上述合法新规则。helper交换只改变表示，不改变图。因此union over这些合法J/transfer与全三disjoint-cut规则等价，不是只有某种paired-pin分割才被表示。

原source edge-transitivity可在构图前将一条basecut送到锚{0,1}，故旧完整anchored列表足够作为**参数来源**。但旧5614中含4个adjacent-basecut分支；新scope只取其中两条basecuts不交的5610分支，并要求第三cut也避原四端点。共享端点/端点occurrences规则不在本scope，不可混用旧adjacent-case分配。候选J本身不因source edge-transitive而vertex-transitive，不能把candidate的一个root当全部root。

三cut删3、repair添1、四spokes添4、helper间添1，所以1252点、1875−3+1+4+1=1878边，全3度。六个old端点两两不同；p/h各由repair恢复度，余四端点由spoke恢复度；helpers各2spokes+互边。原非边条件避免重复repair。若repair改为同一cut两端即恢复该cut，会退回旧two-cut规则，非本次跨cut新域。

## 2. root已选择的单个新有限子域

root拟从原 `FROZEN_OBJECTS` 选第二cut含1178、且x-pins={0,1178}的lex最早实际旧J。令其第二cut为{1178,q*}，则y-pins={1,q*}。q*、真实case-ID和该J保存的下一失败helper/target由sole metadata owner绑定，本paper不读source矩阵或猜标签。

保持x–1178，故1251旧A的保存缺点1178在J及后续H中都是x直接邻点；y经互边也至多2步到1178。只允许移其余三pins：p∈{0,1,q*}，a为该pin当前连接的helper。第三cut避{0,1,1178,q*}，保两orientation，repair p–h须原非边。后续针对该固定J的新保存缺点t设计repair，而不是把旧A已修的1178反复当新证据。

该固定J/三可移spokes族是第1节全三cut族的**真限定子域**；任何完整负结果也只能闭这个子域，不外推全部5610basecases/一般三cut。不会从旧two-cutNO直接继承新族NO。

**可推翻预测：** 至少存在一个该有限子域的合法transfer，在保持x–1178的同时修复所选J保存的失败helper–t，并使两个helper到全部1250旧点均在10步内。它比“把t接成直接邻点”更强，但仍不是完整D10预测；若仅单pair被修而另一target失去覆盖，则这项联合覆盖预测尚未通过。

## 3. 两helper的精确新根门

令最终old-only host

    T = G − {e,f,g–h} + {p–h}。

最终helpers a,b邻接，旧pins分别A'=(A\{p})∪{g}与B。对任意旧target t，允许距离∞，严格有

    d_H(a,t)=min(1+d_T(A',t), 2+d_T(B,t))；
    d_H(b,t)=min(1+d_T(B,t), 2+d_T(A',t))。

任何最短路若到达另一个helper，都可用直接a–b替代其此前段；最后一次离开helpers后完全在T中。反过来各式给出的Walk均可实现，故不是只有充分性。于是两helper完整R10覆盖恰等价于

    R9_T(A') ∪ R8_T(B) = V(G)，
    R9_T(B)  ∪ R8_T(A') = V(G)。

helper互距已为1。这里必须用删三cut**并加入repair后的T**；不能直接替成旧G或旧J的球。p、h没有newspoke，故“删边两端全为pin所以minpin距离不变”的引理不适用；repair也可能与helper路径共同使用，在10步预算下不能将两种路线硬拆成互斥。

若需解释repair怎样影响T，可令U=G−三cuts，使用精确一边增加公式

    d_T(x,y)=min(d_U(x,y),
                 d_U(x,p)+1+d_U(h,y),
                 d_U(x,h)+1+d_U(p,y))。

此式只含一次repair，因为最短路无需重复同一新增边；它并没有允许忽略未来已删第三cut对旧腿的破坏。

## 4. 旧旧点对也有精确门，不能只查helpers

对旧点u,v，令r_A(u)=d_T(u,A')、r_B(u)=d_T(u,B)。相邻helpers的最后进出分解给

    d_H(u,v)=min(
       d_T(u,v),
       r_A(u)+2+r_A(v),
       r_B(u)+2+r_B(v),
       r_A(u)+3+r_B(v),
       r_B(u)+3+r_A(v))。

同helper经两spokes，对面helpers经三边；反复进出不提供更短的漏项，因为两helper间已有直边。该式处理old腿中的repair与第三cut损伤，是oldpair的充要条件。两helper到allold通过，仍不能推出全部oldold≤10。反之，任一指定oldpair该式>10即给整个候选的严格反例。

## 5. 保存失败pair的13-route精确预筛

可用同一接口产生有解释力的单pair预筛，不仅记总badpairs。令共同图

    K=J−{a–p,g–h}，新增边E+={a–g,p–h}。

对任意指定pair x,t（helper–old或old–old均可），最短H路使用E+中的每条边至多一次。故d_H(x,t)恰为以下13个K-distance拼接的最小值：

* 不使用新增边：d_K(x,t)；
* 只使用一条新增边：选E+中一条、任一orientation，代价 `d_K(x,s)+1+d_K(r,t)`，共4项；
* 两条都用：两种边顺序、各两orientation，代价 `d_K(x,s1)+1+d_K(r1,s2)+1+d_K(r2,t)`，共8项。

每项都是真实Walk；任何最短路按新增边出现顺序也必落其中。若保存pair在J已>10，则K⊆J使零新增项仍>10，任何成功修复必能展示使用a–g、p–h或两者的具体新路线。这是该pair的**充分且必要**预筛；失败可立即拒绝候选，通过只说明此pair，不能当全graph通过。所用距离是K而不是未经删两边的J cache。

针对saved t直接选g=t若合法，确实让a直接邻t，另一helper也≤2；但它可能同时删除承担其他target覆盖的a–p，且第三cutg–h还会破坏别的短旧腿。因此“saved t已修”不蕴含两个R10union条件，二者更不蕴含旧旧条件。actual批若有passer，应分别报告savedpair、两helper覆盖、旧旧阶段，不能把不同阶段的失败混称同一个原因。

## 6. 接受与停止边界

上述门不使用source bipartite假设；该实际source旧nonbipartite记录保留。没有继承单细分的全图D≤11上界给新三cut图。若最后候选所有pairs≤10才可声称达到D10；若失败，只给真实失败pair及路线，不补造actual全径。若root只授权固定J三pin-transfer有限批，sample/timeout只能UNKNOWN该批，不能变成全三cut排除。

本次只完成paper；不枚第三边、pins、13项数值，不跑图或source验证，不扩cut数量/新source/另一模板，完成即停。
