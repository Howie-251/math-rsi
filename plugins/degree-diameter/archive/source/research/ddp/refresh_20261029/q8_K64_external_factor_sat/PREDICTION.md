# 为q8纤维扩展联合设计64点辅助图

目标参数(13,3)，新查询Comellas主表值972。Rajiv原文Theorem1允许q8、X'={1,x,x²}、X=F8*\X'：若64点图K包含8个指定Q3立方体，且maxdegree5、D≤3，则主图1088点、maxdegree13、D≤3。作者已有3regular gadget的1088/14，并明确尚未找到2regular gadget，不能称为作者未尝试。

已结束的固定J5⊕I1仿射类3840项全失败；不续该类、换矩阵、seed或坏对评分。本批真正释放共同连接：64点分成8个8点pencil，固定每个pencil的Q3边，允许任意跨不同pencil的简单无向2factor作为额外边。各vertex恰2条额外边，故K为5regular。

预测：该全局模型存在一个K64/D3。若SAT，实际重建全部160条边、独验64根，给出pencil标记与13度主图。若rawUNSAT或UNKNOWN则仅报告本明确模型的实际计算结果，不把一般q8 fibre extension排除。

规范化：存在两个额外邻居位于不同pencil的vertex时，用pencil重标及cube平移将其设为0，邻居设为8和16。若每个vertex的额外两邻居都在同一pencil，则EE回原pencil、EEE回第一目标pencil；从root到外pencil的三步目标至多8+24+6+12=50<56，所以D3不可能。因此规范化覆盖本跨pencil2factor域。允许pencil内部新增边的域未包括。

编码：1792个额外无向edge变量，各vertex degree2；R2为实际邻接或两步路的等价布尔门，R3完整覆盖所有跨pencil无序点对。固定cube已保证同pencil≤3。没有把必要的局部覆盖当成充分条件。

唯一CaDiCaL调用，wall90秒、CPU硬限100秒，整个模型组CPU预算120秒；不自动第二次timer/seed/邻居case。仅正例才展开1088主图和安排独验。SAT模型独立按完整实际邻接重算；rawUNSAT无独立证明日志时保持计算证据口径。
