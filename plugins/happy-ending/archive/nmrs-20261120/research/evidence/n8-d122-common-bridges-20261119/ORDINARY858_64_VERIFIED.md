<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# 普通858≤64：双实际DRAT与完整独立重建

**已完成。** 任意完整有序rank3 signotope若禁蓝5、红8和weak8，人口至多64，即

$$N_{\rm sig}(8,5,8)\le64.$$

结合[普通866≤57](../../N866_57_GLOBAL_20261119.md)，真实残余 $D_8\le57+64=121$；再结合[已证 $C_8\le188$](../../N8_C188_311_20261119.md)，得到

$$Q_8\le309,\qquad F_8\le310,\qquad ES(8)\le311.$$

普通868由十个同输入含坐标858面计数给 $4N_{\rm sig}(8,6,8)\le10\cdot64$，故亦有 $N_{\rm sig}(8,6,8)\le160$。

## 原始证据

* [最终封存回执](../../../evidence/858/ordinary858-64-final-receipt.json)：2026-11-19 17:08:02 UTC重新完整核对原/重建CNF、proof、源码、输入库及checker哈希，全部匹配。
* [原查询结果](../../../evidence/858/near65-v1/result.json)：AE20、首checker0、唯一VERIFIED；核验7447.126秒。
* [完整独立重建](../../../evidence/858/near65-independent-v1/reconstruction.json)：另一程序不导入原builder，逐项再生完整语义域、全部子句与counter/语义变量交错ID，重建CNF逐字节SHA相同，12.504秒。
* [第二次实际DRAT结果](../../../evidence/858/near65-independent-v1/second-result.json)：checker0、唯一VERIFIED；原日志核验7558.774秒，前后proof与CNF哈希不变。
* [完整真实输入映射](NEAR65_SEMANTIC_BRIDGE.md)：真P、3个缺角预算、同标签坐标/洞行充账、首六覆盖及全部路径/packet接口。
* [缺角几何独立小核](../../../evidence/858/missing-geometry-audit.json)：全部84态、168最小角、293角子集像及2520理想区间通过，确认没有同一点同一新坐标重复收费。

两份检查为不同实际进程、同一权威drat-trim实现；未调用外部审阅。两日志均完整处理2,438,439,752字节proof，195853个原句核心、14905851个引理核心、443251915次resolution、8735个RAT核心引理。

|绑定|值|
|---|---|
|变量 / 子句|298421 / 5187084|
|原及重建CNF SHA256|f8f5cdead0740948641ea3f025c21a0a37e342eb8ab16968bdf90b022db3ba26|
|proof SHA256|ace3d9e1479d998fdb883a429803b09e05005b9bc08b276c59838d50054bea05|
|原源 `near65.py` SHA256|ce0325d8c8dda4c34b0d2d34c5aebb61f85f79149587211e6871efa94fe6ac86|
|独立源 `rebuild_near65.py` SHA256|c3e888f93d14b68c3bde09d64a011a1c8202b5f1d4012c4c811985eb6a733514|

## 数学连接

反设65点，取真实结束秩l及其canonical下理想P，19洞。一个最小可加角g若没有实际出pair的l恰g，则它在同一固定l的上包络内，各点可独立改态。每个坐标面至多22点，因此九坐标总亏只有3，全部缺角总数至多3。对每条合法纯洞行，把所有能通过缺角从行外进入的物理点同时改态，每源只收费一次；得到同一份原l下的行充账不等式。

这些条件连同真P进角实现、同一pair/原三元色、完整843个首六模板及同端weak路径禁制构成该必要CNF。任意真实65点输入必给满足赋值；两次实际DRAT排除了它。更大输入取65点诱导子域重算真P，亦被排除，所以这是全域≤64。

本证明**不依赖**66全冻结、全pair l=u、末两态、后六模板、后来新增的rank fan/整区间/Hall层束，也不依赖老full66作业终态。容量进口为同输入Baek22、完整857≤50纸证与由22面计数得到的66；后者没有被冒作计算证书。

## 权威Linux文件与回放

本地保存源码、完整语义、重建/检查回执与两份完整短日志（见最终回执的checks字段）。大CNF与proof权威文件保持在Linux：

* `<private-artifact-root>`
* `<private-artifact-root>`
* `<private-artifact-root>`

使用 `<private-artifact-root>` 对上述重建CNF、原proof执行 `-t 2147483647` 可再回放；不要覆盖已有目录、输入、证明或日志。全部科学运行在Linux。原full66及各64加强作业继续自然运行，其未终结部分不被计入本结论。

[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
