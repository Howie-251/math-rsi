# 唯一首最优 source17 平面的真实 pin 对照：数值MIP不可行

2026-11-01。PRED 的正假设“只换 source17 首最优平面即可在固定池取得≥811”未获支持：唯一一次 scipy.milp 返回 status2 / HiGHS Status8 **Infeasible**，不是超时。没有 incumbent，没有新增图。

## 实际改变和未改变的对象

retained4=[31,59,60,72]的324个中心固定。全部15个 admissible 变量层仍为[16,17,30,32,35,42,43,44,45,58,61,64,71,73,74]，没有只取容量正support17层而漏64/71。

只把 source17 的81个点从旧W={(a,b,4a)}改为W'={(8t,s,t)}，normal=(1,0,4)。其他14变量层和4固定层全部使用旧W。这个改动继承已实核的六dart transversal，以及7个拉回限制方向从5减为4的依据；未换第二个normal，也未改eta/phase/seed。

按 accepted PARAMETERS 的真实 GF9 乘法、实际 dart matrix 与 noise 逐点生成1539个中心的完整N54，保存 ALL_CANDIDATE_CENTERS.tsv、ALL_CANDIDATE_PIN_ROWS.tsv。center表的a/b是各plane的参数，**实际坐标另列x0/x1/x2**；对source17为(8b,a,b)，其余为(a,b,4a)。不读56862边表。

## 实际模型及负对照

1215点binary加3个target48合法cut binary，共1218变量。37908个actualpin负载约束，加cardinality与logic共37913行、67074非零系数；要求变量中心≥487，即包含324固定点后≥811。target48 min(w17,w35,w74)≤20的已证cut照用；没有重算determinant、field laws或旧all-rank。约束中的方向不因source17选择哪个源平面而改变。

旧U10=[31,32,44,45,59,60,61,72,73,74]直接代入**本次**模型：810个中心，43740个actualpins两两不同，全部pin/logic行通过，唯一违反的是行37908要求486≥487，差1。它不包含source17，所以本次plane替换保留这个已知810对象。负对照保存 BASELINE810_NEW_MODEL_CONTROL.json，无原solver重启或旧图验证。

## 返回值能支持到什么程度

SOLVER_RETURN.json保留原status/message/x。x、mip_dual_bound、mip_gap、mip_node_count均为null，没有rootLP或搜索树日志，不能声称已取得独立UNSAT证书或rootLP不可行。目标函数是0的feasibility，不能把其dual当最大中心数界。

因此本次是**数值MIP证据尺度下**排除这个唯一新normal、固定ret4、其他层仍旧plane的1539点池取得≥811。与实际810负对照结合，该有限池在此证据尺度下仍停于810；没有证明所有plane、所有非线性点集或保留ret4的一般模型最多810。

SciPy关于threads的warning为“unrecognized option passed to HiGHS verbatim”，实际传给HiGHS的threads=1。一次solver3.480811205 CPU秒，全部imports、点/真实pin生成、负对照、建模、solver、汇总共3.933452689 CPU秒，低于60；wall3.935604，低于44秒solver上限。全进程终态。

## 对下一步的实质反馈和停止点

运输方向5→4是真实局部改善，但单独重定向source17平面仍未消除所有层的共同actualpin冲突。它推翻的是这一具体“只改一个plane就足够”的正假设，未定位一个新的解析全局矛盾，也未否定四投影支持接口的价值。

此方向按授权停止：不扫其余7个最优plane、不续timer、不改其他layer、不扩729点池、不自动生产图/degree族/Lean。若root之后选择继续，生成规则需要对同一源点集的多个实际projection supports与其他源层作协调改变，而不能把此次方向数下降直接当作packing增益。本批不提出未经授权的新solver或搜索清单。

本次0sourcegraph读取、0BFS、0field/rank/Lean重验、0旧solver重跑、0新图。q8三个原目标A/B/C审查scope不含本pilot。
