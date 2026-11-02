# 二元域多路线：已实现的局部覆盖与两个控制器族终态

## 此前未知的问题与实际预测

旧197568全域只排全部36约化三词各自满rank3，并不排实际controllerpair多个低秩image联合覆盖。本轮按真实inverse/offets规则，在已有C30实际pair0→18固定两套手选binarychart。ARC的三rank2 packet对所有8个source坐标并满8；合法COLLINEAR对照只并6，全部9条≤3controller路线也只并7。两chart完整反向关系均实际通过，没有将x0平面并外推所有x。局部成功不是256/264新图。

依此保留四arc方向，针对唯一0→5三词021改B：该pair从4变8且adjacent保8，但4个conjugate词变好同时4个cyclic词变坏。原‘goodword24→28’预测被反驳，实际两者同24；不得把局部修好或goodword数量当整体优势。

## 理解改变了实际生成器

先以ARC/R两chart对照typed C30插两点。A两不同directededges上插30/31、B两不同directededges同样插入，规范A tails i<j、B保持orderedk!=l，共378450参数，simplequad通过284310。完整pointpacket含0/1/2和36reduced3、adjacentpencil shortcut，全部simple候选两chart均失败于newroot30。

随后提出可推翻预测‘所有参数都已root30容量不足’，只读保存tails做ordinary Σ2^l controllerwalk容量（保backtracking）。283388 min0、907 min4、15 min8，原预测被15个反例推翻。只对这15个幸存者检查newroot31：全部min0。因此整个插边controller族在任意8fiber/每dart≤2choices的投影提升下都不可能D3；换其它矩阵也无用，停止。

据此改变拓扑，用11个三角单元生成33点controller，是本三型模板超过253的最小规模。选择ARC，因为003/030/300三个cyclictriangle词保所有同层fibres，而R会损其中030。冻结p1/q,r非零100规范代表，实际每个同层fibre都通过，显示这项拓扑修改确实保住预期覆盖。然而保存数据表明每个controller至少一个type-root在三步内到不了全部33点，projection存活0。故该三型C11voltage族本身D>3，不只一次ARC失败；停止，不m12/换field或chart梯。

另有paper：32点Cayley且两个globalinversepair生成的接口由C2²商kernel8点/≤3最多5点排除（cyclic情形25<32），不排非Cayley32。完整scope与推导各在子目录。

## 结果与边界

0新增完整图/参数/Lean，0图生成/全图BFS/付费ARIS。B samecase最终5.653785158/30CPU，含原读门1.6（较其计划1.5多约.1如实保留）、输入/手算准备、两局部实测、一次编译/两chart全族、保存行容量诊断/15对象、C33全100与root整理，不清零。

当前可以继承的生成条件是：真实四arc噪声方向和反向maps可自动修好相邻层，多路线确有实际互补；同层需真实闭路线包，三角单元可提供。但必须换控制器拓扑，不能在已被projection关闭的两族上继续调矩阵。一般N(8,3)、一般C32/C33控制器或多路线affine机制均未排。Goal ACTIVE未完成。
