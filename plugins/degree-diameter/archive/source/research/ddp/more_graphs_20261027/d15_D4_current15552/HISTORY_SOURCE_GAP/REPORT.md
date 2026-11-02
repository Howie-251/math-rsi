# (15,4)当前15552：主表已确认，actualsource尚缺

本轮只作有界source恢复，没有得到15552的实际边表或recipe，因此没有degree、freeport或纤维profile，也没有构造搜索或旧D4验收。不能用192×81或64×243的阶数分解代替真实结构。

## 当前数值与详情滞后

2026-10-27读取的 [官方当前主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) 明确列(15,4)=15 552，非bold。近期更新名单将(15,4)列于Dharunish Yugeswardeenoo的Oct26–27条目。旧taula_delta_d.html只是跳转页，当前main应使用table_degree_diameter.html。

但该格链接的 [D4详情](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html) 仍停在Comellas13608，而 [Bhakar数学仓库](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg15/dia4) 当前文件树也只有deg15-dia4-n13608.edges.txt；其README给出168×81的五符号routechart。这两处13608描述还不是同一个配方，不能只按相同阶数混用，更不能冒充当前15552。

elder-plinius数学仓库main中 [biggest-graphs索引](https://github.com/elder-plinius/V3R1T4S/blob/main/known-knowns/biggest-graphs/INDEX.csv) 仍只有旧13365。配合source_scout针对近期PR的精确15552及15,552索引查询均无命中，最近更新100条PR中未找到15552的新来源。该子任务证据见 [PR scout结果](../d15_D4_current15552_pr_scout/RESULT.json)；没有API故障，也未下载旧13608、13365或重读无关旧PR。

## 已冻结、尚未检验的覆盖直觉

[PREDICTION.json](PREDICTION.json) 在实际source profile前冻结了可反驳假说：当前15552具有192个独立81点F3^4纤维，每点在五个邻纤维中各接三点。它目前是UNRESOLVED，不是由因数分解证明的事实；64×243等表示仍未排除。

若实际recipe确认这一模型，下一项针对性覆盖问题是：第五种controller路由是否为同一端点槽补上四符号route所缺的仿射方向，而非仅增加重复短路。对路由词t1...tk，关系

~~~
x -> M_t x + lambda*d_t
~~~

的末端集合是

~~~
M_tk ... M_t1*x
  + span(M_tk ... M_t2*d_t1, ..., M_tk*d_t(k-1), d_tk).
~~~

因此必须用实际controller的长度≤4路由，检验对应仿射子空间并是否对全部81个source fibre点覆盖全部81个目标。一个rank4路由足够；否则路线间方向与平移的互补才是承重条件。这个问题需要当前chart、inverse关系及controller，不能沿旧13608的矩阵或电压猜参数。本轮没有执行这项路由检验。

## 实际范围与停止

[SOURCE_STATUS.json](SOURCE_STATUS.json)、[RESULT.json](RESULT.json) 和 [terminal.json](terminal.json) 保存准确缺口。actualsource URL、header、degree及fiber字段均为null；当前known baseline仍为15552。下载actualsource零、profile零、sourceBFS零、searchgraph零。

在给定三分钟source阶段内没有获得当前literal或recipe，故按边界收束，不转旧source、不运行新图搜索，也不把source缺口写成构造失败或整个routechart族被排除。重新启动需要一个明确绑定15552的primary边表或生成配方。
