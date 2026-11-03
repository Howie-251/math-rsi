# 双29圈与自由跨边的精确模型

固定左侧`0..28`和右侧`29..57`各自的诱导图为标准`C29`，侧内其余边固定为无。
唯一841个主变量是跨侧矩阵`C[i,j]`，每行每列精确为6。侧内点的度数为2，
故完整图必有58点、232边、全8度。全部跨边自由；不固定`P=I`、循环矩阵、
对称性、匹配分解、旧几何或旧种子。两侧分别按各自Hamilton圈顺序重标，
可无损得到这两个标准圈，因此模型覆盖整个所述Hamilton子族。

每个跨侧点对的覆盖恰是五项OR：直接跨边，或先走左圈的一步，或最后走右圈
的一步。每侧圈距离1或2的点对已固定覆盖；其余348对各用29个完整双向AND
表示真实的共同跨侧邻居，再取OR。没有放开侧内非边，也没有省略同侧覆盖。
因此CNF的SAT赋值与这个Hamilton子族的8正则、直径至多2图相互对应。
行列和6及跨覆盖还推出`HC+CH+C=J+P`，其中`P`自动为某个置换矩阵；模型
不引入或预选`P`。解码时从实际`C`计算并核对它。

准确计数：841主变量；58个长度29、目标6的计数器各182辅助位/694子句；
20184个共同邻居AND各1位/3子句；841跨覆盖子句和696同侧覆盖OR。总计
31581变量、102341子句。计数在源码中作为正式准备时的断言，尚不表示已经生成输入。

复用范围只有旧通用`CNFEmitter`、`enforce_exact`及其`unary_thresholds`、
`add_iff_and`，以及`joint_boundary_completion_run/encode.py`的通用
`evaluate_clause`与`check_dimacs`。未实例化旧ABEncoder，未调用任何旧图
补全build、几何生成器或搜索器。完整图BFS在本文件直接从全部实际边执行。

`python encode.py sanity --output-dir DIR`只建立小模型，保存`small_sanity.json`。
它核对AND全部8个真值、小三棱柱及三个有意区分跨覆盖/同侧覆盖的小矩阵，
再核对行正确列错误及转置情况。每个显式矩阵补全所有计数/路径辅助赋值，
逐条检查CNF，覆盖失败点对必须与完整图BFS完全一致。

`python encode.py prepare --output-dir DIR`生成`input.cnf`、`encoding.json`、
`variable_map.json`、`sanity.json`，状态为`PREPARED_NOT_RUN`，不启动solver。
正式准备还用一个明确但失败的六连续offset矩阵核查全规模赋值语义和写回CNF；
这个矩阵只是sanity输入，不约束搜索。`decode --output-dir DIR --model PATH`
默认读`DIR/solver.log`，要求SAT标志和所有变量完整赋值，逐条检查保存的CNF，
再输出实际`candidate.json`、`candidate.edges`和完整坏对，独立执行BFS及P检查。
非目标必须失败退出；`main(argv=None)`正常成功返回，便于受限runner调用。
根代理仍从完整边表调用现有独立检查器。

初次交付只运行小矩阵sanity，不生成29正式CNF或启动solver。UNKNOWN、
失败候选或有限运行无目标都不是排除；即使本CNF被认证UNSAT，也只排除
两侧都为Hamilton圈的子族，不排除其他二正则圈型或任意58点图。

已实际执行小sanity：8个AND真值和6个显式矩阵全部通过，记录见
`small_sanity.json`。其中`m=6,S={0,2,4}`跨坏对为0、左右坏对各3；
`m=7,S={0,3}`跨坏对为7、左右坏对均0；两个正例的全部点对均由BFS覆盖。
两份度数负例分别只破坏列或行计数，即使直径仍为2也被CNF拒绝。
