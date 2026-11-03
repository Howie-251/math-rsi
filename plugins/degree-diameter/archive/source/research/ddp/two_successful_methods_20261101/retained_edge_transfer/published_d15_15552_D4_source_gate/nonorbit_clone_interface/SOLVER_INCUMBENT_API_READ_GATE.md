# 本机 incumbent API 只读门：实际确认 bundled HiGHS incumbent 入口

最新状态为 **CONFIRMED_BUNDLED_HIGHS_INCUMBENT_API_NO_SOLVE**。原3CPU失败及随后静态读取完整保留如下；root再明确授权同case累计cap8CPU，并要求进程启动前固定四个线程环境变量。该唯一修正后的API探测实际exit0，不建LP、不passModel、不setSolution、不solve。

项目内对Python源码的定向查找 `highspy|setSolution|passModel|mip_max_improving_sols|_Highs` 未定位已有直接API调用。已有 controller-pack32 回执记录 SciPy 1.15.3，但这只是既存环境证据，不冒作本轮成功取得的库version。

唯一实际探测进程设置 `RLIMIT_CPU=(3,3)` 后，尝试通过 `importlib` 读取 `highspy` spec 与 `scipy.optimize._highspy._core` 的类/docstrings，并查看 `_Highs` 的 `setSolution`、`passModel`、选项和callback字段。该进程实际 exit137/Killed；stdout未刷新，故没有取得可用API/docstring回执，不能确定具体导入或introspection停止位置。代码没有任何 `run()` 调用，没有传模型，也没有求解。

未固定数值库导入线程是这个成本探测的限制；不能从此失败判断 `_Highs` 或 `setSolution` 不存在。保留本次失败，3CPU硬限账不重置、不原样重试。保守计费3CPU秒；实际rusage未收集，不能把此计费冒作实测精确CPU。

以上是首attempt的观察边界；静态后续新增的实际证据见下节。不能据首attempt失败承诺或否定避免从零启动，也不能把 `scipy.optimize.milp` 的无x0公开签名推断成其 bundled internal `_Highs` 无incumbent入口。

## 实际静态后续：可确认与仍未知

root用stdlib定位包路径后，本门只读 `/opt/conda/lib/python3.11/site-packages/scipy/optimize/_highspy/_highs_wrapper.py` 和对应dist-info metadata。`scipy-1.15.3.dist-info/METADATA` 第3行明确 `Version: 1.15.3`。

安装的真实wrapper给出下列已使用接口：

* 第117行构造 `_h.HighsLp()`，填列数/行数、CSC矩阵、目标、bounds、integrality；
* 第135行构造 `highs = _h._Highs()`，其中 `_h` 是 `scipy.optimize._highspy._core`；
* 第136行构造 `_h.HighsOptions()`，第183行 `highs.passOptions(highs_options)`；
* 第193行调用 `highs.passModel(lp)`；第206行才调用 `highs.run()`。本任务只读这些代码，未执行它们。

因此 constructor 和 `passModel(HighsLp)` 已获**当前安装wrapper实际使用**的正面证据，无需猜测 standalone highspy。目录未发现对应pyi/header，wrapper也没有 `setSolution` 用法；这不证明二进制 `_core` 未暴露该方法。`setSolution` 的存在性/签名和known864整数start是否可传，仍为 **UNKNOWN**，所以当前不能声称已经具备或已经排除 warm start。

wrapper对 MIP 的结果处理认识 `HighsModelStatus.kSolutionLimit`，并在 time/iteration/solution limit 后检查是否有可行incumbent。但这只证明结果状态被处理，**没有确认停止after-first-improvement的选项名、值或其是否把初始解计入限制**。不能把这一状态常量替代真实stop选项文档。bundled HiGHS本身版本也未从本轮静态文件确认，不能用SciPy1.15.3充当HiGHS版本。

后续静态读取与记录保守计费1CPU秒，连同原失败3CPU保守账为4/5CPU秒；无新import、LP/MIP或安装。当前输出足以确认本机有bundled `_Highs`/`HighsLp`/`passModel` 入口，但不足以确认incumbent入口。本门到此停止，不为未知部分自动再做运行期探测或full15552求解。

## 同累计cap8的单次线程修正：实际API已确认

保留上节为当时状态。随后经root新授权，在启动进程前设置 `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1`，进程内仍设hard3CPU。实际一次导入 `scipy.optimize._highspy._core` 成功；空 `_Highs()` 与空 `HighsSolution()` 仅用于读version/default fields。原始结果在 [API_READ_ATTEMPT002.json](API_READ_ATTEMPT002.json)。

实际环境是 **SciPy1.15.3，bundled HiGHS1.8.0**，并存在：

    from scipy.optimize._highspy import _core as h
    h._Highs()
    h.HighsLp()
    h.HighsSolution()

`_Highs.setSolution.__doc__` 实际给出两个重载（均返回 `HighsStatus`）：

    setSolution(self, arg0: HighsSolution)
    setSolution(self, arg0: int,
                arg1: numpy.ndarray[numpy.int32],
                arg2: numpy.ndarray[numpy.float64])

同时 `passModel`、`getOptions`、`getOptionValue`、`setOptionValue`、`version` 均实际存在。`HighsSolution` 字段为 `col_value, row_value, value_valid, col_dual, row_dual, dual_valid`。

因此本机无需安装即可通过bundled internal API提供完整known864整数解。将来若root授权真实全中心模型，可先按实际wrapper的 `HighsLp` 结构建立incidence模型并 `passModel`，再把15552维0/1旧incumbent赋给 `HighsSolution.col_value` 并按该接口设置value validity，调用 `setSolution` 并检查返回状态。应该传完整已知0/1向量，不能把“只传864个1”的部分解冒作已给出其余零的完整已接受incumbent。本次没有实际测试任何模型的start接收，所以不能声称该具体15552模型已经暖启动或保证搜索更快；可以确认的是**真实方法与数据入口存在，未来无需被迫只用无x0的高层milp包装**。

实际默认options包含 `mip_max_improving_sols=2147483647`、`mip_max_nodes`、`mip_max_leaves`、`mip_max_stall_nodes`、`objective_bound=inf`、`objective_target=-inf`、`threads=0`、`time_limit=inf`。这里只确认字段存在，不猜初始incumbent是否计入 improving-solution 限额；也未把某个callback/option测试为“首次改善即停”。root未来可直接选择known864 start、单线程和固定time limit、返回best；无需为了本门再探测callback或开启MIP。

本次修正进程实测 **0.222222089CPU秒、exit0**；额外准备保守charge0.1，连同之前保守4，累计 **4.322222089/8CPU秒**。原导入kill历史没有删除或重置。全case的LP/MIP模型创建、passModel/setSolution调用、求解、图/field测试仍全部0。API门完成即停止。
