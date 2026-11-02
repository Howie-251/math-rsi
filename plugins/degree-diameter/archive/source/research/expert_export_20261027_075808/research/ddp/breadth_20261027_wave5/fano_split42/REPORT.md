# Fano拆点42：固定13122候选完整失败

已完成预设的3^7×6=13122个候选，没有直径≤3的图。所有候选均逐项检查为42点84边的简单4正则图。最好候选的全42根production三步可达评分仍缺45个无序点对，不能登记(4,3)新下界。整个固定族已结束，不追加端点orientation、任意matching置换或新source。

## 来源与上界止损

2026-10-27读取[Comellas当前主表](https://web.mat.upc.edu/francesc.comellas/delta-d/taula_delta_d.html)及其[Diameter 3原始说明](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)。前者列(4,3)为41；后者的具体条目给出41点、Moore bound53及Allwright和后续同阶图，没有给41上界或optimal声明。与相邻(3,3)条目显式写optimal不同，本次所读页面没有发现禁止42的明确上界。本次并未完成全部上界文献检索，不能把“这些页面未见”写成“已证明42仍未知”。具体阅读范围记在`upper_bound_reading.json`。

## 明确构造和完整范围

O4=KG(7,3)的顶点用七位整数mask表示三点子集，disjoint时相邻；35点70边且4正则，准备程序确认全部根的三步可达覆盖。Fano线A_i={i,i+1,i+3}（模7）组成独立集A，剩余B有28点、每点唯一一个A邻居，B诱导42边的三正则图。

B按mask升序编号0至27。把每个A_i换为相连端点A_i0=28+2i、A_i1=29+2i。将其原来的四个B邻居升序记为b0,b1,b2,b3；choice k∈{0,1,2}令half0={b0,b_(k+1)}，另两点给half1。这固定最小邻居在half0，恰覆盖该点3种unordered 2+2 partition。七个choice独立，共2187种。

第二matching固定为A_i0—A_(i+t)1，i∈Z7、t=1..6。t非零，所以它不重复原来的七条内部边；所有端点新增一条边，B点保留原度4。因此每个候选应为简单4正则42点图；C++仍对全部候选直接检查loop、重复边和度数，没有仅依赖计数推断合法。

production逐候选对所有42个根计算完整的≤3步可达位集，精确统计距离>3的点对；它是本次枚举的评分，不称为root的独立最终BFS。该固定族共13122个参数输入均完成，无CPU截断。最好参数为partition choices [2, 2, 0, 2, 2, 0, 1]（little-endian三进制code953），t=5，坏无序对45。

## 产物和停止

`prepare.py`、`source_structure.json`和`source.edges`给原O4及全部编号语义；`search.cpp`、`RESULT.json`和`stdout.log`给完整枚举与production评分。`best.edges`保存42/84的完整边表，`best_parameters.json`保存最佳构造参数，`best_bad_pairs.json`保存全部45个实际D3坏对。

编译CPU约0.530秒，唯一搜索worker CPU约0.021秒，准备CPU约0.001秒。没有安装依赖、没有调用SAT或旧D2问题。最佳图的独立最终BFS留给root，此处没有重复执行。结论只关闭这些固定partition与六个shift，不外推其他Fano拆点orientation、matching或一般42点图。
