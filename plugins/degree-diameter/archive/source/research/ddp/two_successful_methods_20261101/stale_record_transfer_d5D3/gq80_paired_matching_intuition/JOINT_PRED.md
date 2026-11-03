# C5 两侧匹配完整互补性检索：事前预测

容量障碍已被实测227≥216反驳，现由root另行授权同一 C5 action 下的完整 joint cover。可推翻正预测：存在一对匹配，其联合216far-orbit mask完整，尽管两个分别首argmax的联合只为158。这里不假定需要或一定来自单侧argmax。

只读取已保存 P/L 各65625项 matching TSV 与 compressed block model，不重 action、geometry、原1560模型或 side枚举。由完整单侧maxQ=113、maxP=114，成功必须 Pcoverage≥103、Qcoverage≥102。容量不足项作严格prune，不只是启发式排序。

对每个合格 Q，用其216覆盖bits建立216个 candidate-membership bitsets。对每个合格 P，遍历其缺失orbit，将Q候选集与相应membership依次AND。非空 iff 存在一个完整搭档；空则该P无任何合格Q。这样隐式完整判定65625²=4306640625个matching对，不显式逐对循环、没有SAT/MIP。

保存全部P的prune/query状态、每个实际missingbit后的Q survivor counts、eligibleQ位置到旧matchingindex的映射及membership。若首hit，立即保存80/200字面图、两20edge matchings、blockIDs与全部1080原far-pair覆盖式/真实≤3路绑定，再停交root独验。首hit的candidate绑定只用旧cached incidence，0旧GQ/field/sourceBFS；不重建1560变量model。若完整全空，只关闭此实际固定C5匹配子族，不能排 unrestricted GQ80。

同case cap10CPU，继承1.700985481，新准备计0.25；单worker hard CPU7（soft6用以保存UNKNOWN）。预算或异常中断时保存已查P/remainingP，不续timer/换action。未命中图0、candidate/source BFS0。
