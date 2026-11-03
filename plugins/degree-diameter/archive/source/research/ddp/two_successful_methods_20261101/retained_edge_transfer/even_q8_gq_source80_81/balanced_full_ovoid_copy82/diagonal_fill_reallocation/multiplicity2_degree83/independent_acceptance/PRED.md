# 独立预登记：degree83／k2唯一完整候选

2026-11-01。已读root PREDICTION_AND_SCOPE，等待root实际ready后才执行一次独验；不修改producer或root计数。

**P1。** 原H342290全部13862745边与accepted346516全部14204970边保留。两块clone各4225点：block0标签342290+h、block1标签346516+h，均只连同一原H center的真实U-neighborhood；hub0=346515、hub1=350741，各只连65原fillers。所有新边342225条，无新–新边。预测n350742/m14547195，degree65:2/80:130/81:8385/83:342225。

H、accepted346516及new350742各单stream，绑定全部8450个clone pinlists及所有degree。真正source pins取原H∩U，不从演化center邻域选取，不假diagonal owner是i。

**P2。** 仅BFS block1的65个实际diagonal、两个预先指定off indices及hub1，共68根。由accepted owner table在读新图及BFS之前确定first two actual off indices并保存PRESELECTED_BFS_ROOTS.json；若h0/h1是diagonal就跳过，绝不按结果另选。预期diag(1,80,5251,345410)、off(1,81,5330,345330)、hub(1,65,5266,345410)。实际检验67个clone根到其oldcopy距离2、hub1到hub0距离2；全4225个same-center pairs还须由实际相同非空pinlists/无clone边证明距离恰2。4158未测newoff roots明确不冒测量。

全pairs及prefix不用删除maxgraph推断：U内端点替换覆盖clones与U/彼此，H路线与ownF flag绕行覆盖fillers，hub–F–flag覆盖所有clone/U，hubs共享F两步。从H添加两copy blocks再加hubs、以及从accepted346516添加第二blocks/第二hub两种prefix都要给无future vertex路线。

40CPU含prep/compile，单worker；0旧根/旧off4160/field/geometry/projection/Lean/solver/付费审阅，0其他k或84+。hist预测差异与图合法性分开保存；从本次授权BFS保存distance3见证。实际收据交root再计新图/新参数，不提前写146/37。

执行前root补充的结构性非D2见证亦纳入：hub邻居只在F，clone邻居只在U，U∩F空，且两者无边，故无1／2路线。已有D3证明于是给距离恰3；在本次原定hub BFS内保存hub到旧clone342290的实际三步Walk，不增加BFS。
