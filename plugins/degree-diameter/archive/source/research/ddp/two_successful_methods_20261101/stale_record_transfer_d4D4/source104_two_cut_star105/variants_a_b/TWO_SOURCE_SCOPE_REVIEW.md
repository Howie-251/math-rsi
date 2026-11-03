# 小D4两cut／四星对照：范围与旧路线反例核读

本次只读Rajiv252的RESULT、run.cpp、run_once.py、source绑定及104 unlettered(a)/b的RESULT、输入绑定、driver和两个FIRST_OLD_FAILURE。未读原始边表、未重算距离球/边对/BFS，未运行solver、field、Lean或ARIS，也未写Wiki。没有发现这三个新源对照的newroot等价门、完整边对域或负结论范围有实质缺口。旧104c同规则NO只继承，不是本次第四次数值运行。

## 1. 四端点集合使source闭R3门精确

固定simple源G，删两条顶点不交的原边，P为全部四端点，T=G−cuts；新图J添z且N(z)=P，不作其它修改。

删除边只会增加距离，故d_T(P,t)≥d_G(P,t)。另一方面，从P到t的G最短路线若用了任何cut，在该cut下游端点（仍属于P）重新开始，会得到更短的P到t路线，矛盾。因此最短距离可由一条避cut路线达到，得到

`d_T(P,t)=d_G(P,t)`。

J中从z到旧t的最短路不必重复经过z，故恰有

`d_J(z,t)=1+d_T(P,t)=1+d_G(P,t)`。

因此四个source **closed** R3的并等于全部旧点，恰好等价于newroot R4全覆盖；不是仅有利上界。generic engine的深度3 BFS包含root和0..3全部层，四个uint64 masks保留全部n<256实际点位，full mask只置0..n−1。这里的新支持查询针对改图问题，不是重新验source D4。

这个等价只管newroot。即使四球并满，删边仍可能把旧旧距离4拉成5；必须检查实际J，不能将source D4直接继承给修改后的旧旧点对。

## 2. 完整域、度数与actual candidate检查

generic run.cpp对全部原边编号i<j枚举，剔除共享任一端点的边对。simple图中两条不同边至多共享一个端点，故合法数精确为

`choose(m,2)−sum_v choose(deg(v),2)`。

252源的630边给198135 raw、2520共享端点对，合法195615；104源的208边给21528 raw、624共享端点对，合法20904。代码末尾在无hit且完整时核对这个计数，RESULT均给domain_complete=true。未借未证图自同构减少域，也不将参数个数当非同构图个数。

四端点互异保证删除两旧边、添加四条新旧边后simple；每个旧端点失一得一，其它旧点不变。Rajiv252全5regular变n253/m632，旧252点仍degree5、新z degree4；104全4regular变n105/m210、全部4regular。实现检查degree≤cap，构造账已保证这些更精确的profile，无需本次另读边表重复核验。

仅newroot门通过时，engine才在内存构造J、真正删除两条旧边并加四星。先查四pins，再查其余全部旧labels；每个root用普通BFS得到最短距离，遇首个距离>4或不连通即拒该实际candidate。对失败图提前停止旧roots是完备的拒绝证据，不是遗漏必须通过的正例检查。只有全部旧roots通过才会额外查z并保存完整candidate文件；本次没有进入这个hit分支。

## 3. 实际层次不同的三个新源终态

| 固定literal源 | 完整合法边对 | 精确newroot门通过 | actual candidate旧根失败数 | candidate旧root BFS次数 |
|---|---:|---:|---:|---:|
| Rajiv252 | 195615 | 0 | 0 | 0 |
| Bhakar104 unlettered，实验alias a | 20904 | 16 | 16 | 18 |
| Bhakar104b | 20904 | 24 | 24 | 27 |

252的source R3四球并最大仅222<252，所以所有参数在构造candidate前已拒，无oldroot BFS、无source单pair诊断。104 a/b最大覆盖达到104，说明newroot预测得到支持；所有16/24个过门案又被actual旧旧最短路拒绝，完整图预测没有得到支持。18/27是actual旧root BFS累计次数，不是失败candidate数，也不是全source D4复验。新深3支持分别252、104、104次，104的source单pair诊断各1次；source D4全根验收均0。

原始stage回执CPU为252的2.151099672/10与104双源的0.574206988/10。本核读不另造聚合预算或改变root后续正式归档费用。

## 4. 两个保存旧路线损伤反例

两个FIRST_OLD_FAILURE均来自cuts `{0,8}`、`{4,12}`，newroot已通过精确R4门。

* unlettered(a)：旧点对0→19。source最短距4，保存一条旧路 `0–8–2–27–19`；它经过被删cut0–8。实际candidate最短距5，保存路 `0–14–6–31–23–19`。
* b：旧点对0→22。source最短距4，保存一条旧路 `0–8–16–47–22`；同样经过被删cut0–8。实际candidate最短距5，保存路 `0–4–60–52–14–22`。

这两个source path上的cut均明确是0–8；另一cut4–12不在所显示的旧路上。只需读保存labels即可解释机制，无需再查询路线。一次source单pair BFS只给一条旧最短路，不证明该旧路唯一，也没有枚举全部旧geodesics。真正拒绝candidate的是实际J的最短距离5：四星虽给newroot全覆盖，却未提供该旧点对的≤4替路；不是仅看到一条旧路被cut就宣称全部替路不存在。

## 5. literal命名与停止范围

Rajiv252的官方raw是headerless两整数边表，首行是边而非n/m；driver一次必要格式/labels/simple/全5度绑定后写供engine使用的`252 630 5`输入。104两份官方raw也为headerless边表，labels0..103保留，一次绑定为104/208/全4度。内部`source104a.header.edges`和`a_unlettered`仅实验alias；官方文件是`104_d4D4.txt`，不能编造一个官方104a文件。官方页面第三href误指b的历史及实际单独取得unlettered输入的绑定已保留；本核读不再下载或执行官方Sage。

旧104c的同fixed-literal/two-disjoint-cuts/four-star完整20904 NO直接继承，没有重新跑。它原本不能推出另外a/b；本次a/b各自完整有限域才补上这两份literal的同规则NO。三个104输入的primary非同构/D4身份继承原文，不在此重验。

当前可接受的结论是：**在Rajiv252、Bhakar104 unlettered(a)、104b各自固定literal上，任意两条顶点不交原边删除、其四端点接唯一新4-star、没有其它改边的完整架构NO**；另104c同架构NO继承历史。不是一般(5,4)/253、(4,4)/105或其它source NO，不排old-old repair、第三cut、其它新点邻域或多个helpers。没有新合法图/参数/Lean/独立方法，也没有正例fresh验收任务。完成即停，待root另行聚合终态；本文件不触发Wiki发布或新数值。
