# Reserved-N0 模型单次只读复核

结论：未发现负载、预留、cap2、32块门槛或UNKNOWN范围的逻辑错误。这只是代码/回执纸面复核，不是源/矩阵重验、求解证书或图验收。

读取仅限 `PRED.md`、`run_once.py`、`MODEL.json`、`RESULT.json`、`BEST_HANDCHECK.json`。未读取source邻接、MODEL_INPUT或A矩阵，未运行测试/solver/BFS/field/Lean。

* **literal负载定义正确。** 每列i对accepted27 offsets的每个中心逐个遍历其原simpleN，A[w,i]累计该块的全部真实clone负载；没有把它简化成controller邻接或假定每块/不同块邻域互斥。新点只复制原15552图的N，非final16416邻域。
* **预留N0与cap2正确。** 对每旧w的约束是 `A*y <=16-dG-1[w∈N0]`。未保护的14度点仍有capacity2；被N0保护的14度点先留一槽，块负载最多1，最后clone0补回第二槽。被保护的15度点块负载必须0。`export`再次检查N0插入前度<=15、插入后全部旧度<=16，没有只核32条件就出图。
* **压缩等价。** key含整行所有非零列及其实际系数；相同LHS取最小RHS等价于这些原始约束的合取。全部15552旧行保留group映射；没有把只支撑相同但系数不同的行误合并。code构造的columnwise matrix也增加了每列的sumy行。
* **865distinct与32门槛正确。** W27含offset0，只有block0会包含source0；y0 upper0排除重复centre。其余块各27中心且彼此分属不同controller，所以32块＋extra0恰865，n=15552+865=16417。sumy<=32、minimize−sumy是有上限的存在性寻找；返回31本身不证明32不可能。若返回32，binary/all15552reservedcaps手检及865distinct检查后才export。目标不保旧private16416的clone边，这一范围在PRED/export中明确。
* **warm与结果语义正确。** 由旧I32删除所有会占N0中旧15度槽的块，并明确删block0；warm再以全部15552行核cap，cap2点未错误删除。实际warm31、setSolution kOk，best31也做了全行整数手检。actual kTimeLimit、7811nodes、primal约−31、dual约−32只能说明该窗口尚未解决32；不得称max31/无32或全fullN族NO。RESULT确为UNKNOWN、candidate_generated=false，符合这个边界。

若未来真得32，原source15552全部边＋这些865完整旧N的全点对D4/非D3可由已闭source与genericFullNeighborhoodClones继承，但仍需新literal/roles fresh绑定。当前没有candidate，fullN验收草稿保持未执行。

本次仅新增这份review，未改raw数值、STATE/ROUND/progress/builder/Wiki；无新图/参数/Lean/方法计数。完成STOP，不重开原模型或另v0。
