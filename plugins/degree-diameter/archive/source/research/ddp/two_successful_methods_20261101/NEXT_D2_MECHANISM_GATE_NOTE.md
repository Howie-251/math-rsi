# 下一D2接口：在公开106点图上删边释放pin，并修复old–old两步路线

这次只选actual公开(11,2)106宿主，不恢复N8/n61，不换q或从零找图。
原Brown57/cap9的≤72和Brown91/cap11的≤106都要求其指定旧诱导图不变；
这里source已经是公开重连改造后的106图，而且明确删除旧边，所以不套旧排除。
旧5度22点是实际合法经典复现，低于公开24，不能说D2一个合法答案都没有，
也不能把它计新下界。公开104→106本身的删旧edge/加旧旧edge/接newpins先例，
说明D2迁移可以成功，关键要同时维护旧点对的共同邻点，而不只支配新点。

实际小输入现已由root一次取得，无需我重新download/profile：

    d2_record106_edge_repair/source106.author.adjlist.txt
    d2_record106_edge_repair/source106.header.edges
    d2_record106_edge_repair/SOURCE_RESULT.json
    d2_record106_edge_repair/CRITICAL_EDGE_PROFILES.json

primary literal是Comellas desc_g adjacencies/adjD2/deg11_diam2_n106_adjlist.txt。
实际n106/m582、degree10:2/11:104，两个余度点T={34,54}。root已单次检查
全部5565 unorderedpairs都相邻或有commonneighbor，0sourceBFS；本门直接继承。
以前的582/two-spares推算到此才有actualreceipt，不再当假定。

## 一个具体且最小的可推翻模型

目标107点、maxdegree11、D2。删4条不相交且不触T的旧边M，令P是8个端点，
新增点z=106只连S=T∪P，共10pins。source旧边少4、newold加10，若成功则
107/588，degree10只剩新z一个、其余106点全degree11。无需oldnew之外的边时，
这是更省删除的最小degree10-newvertex子模型；不是把原图单纯补边当n改善。

旧图删边后的H=G−M。精确两类D2义务是：

1. 新z到每个oldv：v∈S或N_H(v)∩S非空，即N_H[S]=V。因所有删边都在S内，
   这个闭覆盖等于N_G[S]，不必重复sourceBFS。
2. old–old：每个删边后既不相邻又无oldcommonneighbor的pair必须两端都在S，
   由u–z–v补回。至少一端在S外的pair绝不能靠z修复。

root已存每edge方向的unique-common-neighbor criticaltargets。M是matching且
全部端点在S，因此若oldpair一端在S外，其邻域没被删；最多从另一端丢一条边。
它失去最后一条二步路线恰对应单edge的criticaltarget。所以要求每deletededge
的全部criticaltargets包含于S，结合闭支配就是此模型的精确覆盖接口。两个端点
都被M触及可能同时丢两条commonneighbor路线，但二者已在S，新z自动修复，
没有漏掉这种联合损伤。

下一实际小门总≤20CPU、一worker：先用已存profiles核21条必要候选及forcing，
如无短forcing证书，再枚最多C(21,4)=5985个matching/criticalclosure/closedcover；
有解才导出107完整图并单次共邻/degree检查，无解只关这个matching4模型。
不重复sourceprofile/field/rank/BFS，0Lean/solver/新query/paid/hash。

## 若最小模式失败，下一次应怎样真正改变规则

不要换seed重跑。一个明确更灵活的下一接口是：**删5条matching旧边，加1条
新的old–old repair edge xy，再用10pins接一个newz**。仍净删4旧边，最终仍
107/588、old106全degree11/newzdegree10。若M不触T，12个空余端点是T∪ends(M)；
oldrepair的x,y各消耗一槽，z的pins固定为其余10点。把xy选作先前某个被迫
criticalpair的直接修复，而不是强迫该criticaltarget一定成为z的pin。

对新H=G−M+xy，再精确检查oldbadpair是否两端在S，以及N_H[S]=V。新增oldedge
还可能给多对旧目标一个共同邻点；这正是公开成功改造利用而固定旧诱导上界
没有允许的自由度。该5删+1oldrepair规则目前仅是下一具体prediction接口，
没有被搜索或生成；root须先读最小4门实际结果再决定。失败也不排更一般重连。

本note不是新定理/record，0图/参数/Lean增量，未改root/Wiki/冻结包。D4pilot
保持112CPU终态，新D3参数线STOP。
