# 新GF4源的同机制迁移：两张局部改进终图

> 2026-11-01最新形式化补记：3984/4192两实际Sum图、Fin标签等价、ordered144/352中心与recipe逐项绑定、无前提degree≤21/22、真实WalkD3和非D2均已kernel及独立Audit PASS，最终新scope Gemini审阅也实际SUCCESS/PASS。详见[编译证据](formalization/FINAL_COMPILE_RESULT.json)与[最终审阅处置](../../reviews/F4_CLONES_FINAL_DISPOSITION.md)。不扩大为ASCII解析、exact histogram或全球纪录证明。


已完成一次固定批次，共1.589214495 CPU秒、单worker、两次单线程HiGHS调用。GF4横截核对和300弧的16条邻线分割全部通过，4800条实际中心—弧邻线与新3840点源的边表一致。源D3直接继承已存在fresh全3840根独验，本批旧源BFS为0。

| 参数 | 新终图 | 边数 | 新点 | 项目此前点数 | 增量 |
|---|---:|---:|---:|---:|---:|
|(21,3)|3984|41280|144|3900|84|
|(22,3)|4192|45440|352|4125|67|

完整边表为 `graph_d21_D3_n3984.edges`、`graph_d22_D3_n4192.edges`。对应RECIPE含完整控制器整数向量、16中心平面、每个新点的20个原邻点、加入前度数和当前完整R2覆盖结果。496次覆盖均0遗漏；全部旧边保留，最大度分别21/22。D3由当前覆盖归纳及完整原邻域复制引理保持，阶数超过D2 Moore界所以直径恰3。

固定GF4平面normal为(1,1,w)，与五个实际方向的点积(2,1,2,2,1)全非零。五端口使容量模型为60个整数变量、每个控制邻域Σr≤k，计数上界Σr≤12k。可行向量分别Σr=9/22。两次HiGHS均返回optimal status、mip_gap=0；本批没有独立最优性证书，所以严格保留lower/upper为[9,12]、[22,24]，不声称已证最优，也不追加求解。冻结的12/24可达预测未获支持。

详细证明见 `PROOF.md`，原始搜索返回见 `SEARCH_k1.json`、`SEARCH_k2.json`，总结果见 `RESULT.json`，终态见 `TERMINAL.json`。这两张是相对本项目先前例子的局部改进；公开最高仍待核，不计confirmed record。fresh独立新终图验收由root负责，本批producer记录保留pending，不冒PASS。

批次已停止；无k3、plane/seed阶梯，也不扩已完成工程pilot。
