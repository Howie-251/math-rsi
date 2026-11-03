# 固定650点源加perfect matching：只读/模型校核，尚未搜索

当前状态：本模型已按root/scout给出的两个结构起点完成有限profile，实际结果见 [REPORT.md](REPORT.md) 和 [terminal.json](terminal.json)。本文件保留搜索前的数学校核；没有重跑源BFS。

真实源为 [rithwik650_source.edges](../../m1_degree5_transfer/rithwik650_source.edges)。复用 [source_graph_validation.json](../../m1_degree5_transfer/source_graph_validation.json) 中rithwik650的全650根结果：650点1625边、简单连通五正则、D5，全部根eccentricity为5。原距离五有序对175600，即87800个无序对。

限定历史检索未发现同一个“固定650点、增加perfect matching、degree6/D4”profile。旧 [matching_single_vertex650](../../matching_single_vertex650/REPORT.md) 是删两边后增加第651点、维持degree≤5、目标D5；[degree_deficit651](../../degree_deficit651/REPORT.md) 也仅移动该651点图的度缺口，不是本目标。

## 精确匹配与目标条件

取650点上的perfect matching F，恰325条边，每条F边都不能是源图旧边。G′=G∪F保留全部旧边，得到650点1950边六正则图，目标D≤4，超过保存(6,4)=441。原图D5且仍为子图，所以新图总有D≤5；若存在未修好的点对则新图恰D5。

添加边不会延长任何旧距离，因此原距离≤4的全部点对永久合格。唯一评分目标是旧d>4、即旧d=5的87800个无序对。不能把旧d=4点对误当作目标或漏掉旧d=5对。

合法switch选F中两条不同边ab、cd，四个端点自动互异；替换为ac/bd或ad/bc，只需排除新边落入旧G。perfect matching、无self-loop和F内无重边由该操作保持。源图五个邻居固定，只更新每点第六个matching邻居。

计划每proposal在完整650图计算R₂=I∨Adj∨Adj²，再作布尔平方得真实距离≤4关系，最后与旧D5 masks相交计无序缺项。即使只读旧D5 masks，评分也与新图全部距离>4无序对完全相同，不是代理目标。若没有现成旧距离mask，可仅为新模型用相同布尔关系构建一次，核对其175600项数目；不需要重复旧650源的普通BFS。

首个正式proposal将用独立长度零至四walk枚举（650×1555条）逐bit核对布尔评分，直接复用该proposal进入批次；最终最好图留root唯一全650源普通BFS。这些步骤现已按正式批次执行，具体证据见REPORT。

## 等待起点规则的已有结构

已有 [compressed_graph.json](../../source650_hierarchy/compressed_graph.json)、[ALGEBRAIC_DIAGNOSIS.md](../../source650_hierarchy/ALGEBRAIC_DIAGNOSIS.md)、[algebraic_reconstruction.json](../../source650_hierarchy/algebraic_reconstruction.json) 保存准确边表和层结构，后者已重现全部1625源边，不必重新recover。

V0有500点、V1有125点、V2有25点；源度型分别为4V0+1V1、4V0+1V2、5V1。matching若按层设计，边数m_ij必须满足

    2m00+m01+m02=500，
    2m11+m01+m12=125，
    2m22+m02+m12=25。

因此不能令两个奇数大小层V1、V2各自完全内部匹配。这里仅校核计数，不预设新的层间配边限制或用纯随机起点抢跑。

预定有限范围仍为两个fixed starts、每start至多5000次合法matching switch、单worker且含编译总20 CPU秒；计划种子2026102776501/2026102776502，结构起点已按root指定规则执行完成。不会因预算剩余追加seed、交换或顶点。本文件为模型说明，当前准确执行计数在 [model_check.json](model_check.json)。
