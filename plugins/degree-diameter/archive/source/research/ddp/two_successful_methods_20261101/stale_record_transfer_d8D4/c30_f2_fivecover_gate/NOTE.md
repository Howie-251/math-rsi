# C30/F2/五覆盖：字面降域门停止

2026-11-01。结果 `STOP_LITERAL_F2_SPECIALIZATION_NOT_DEFINED`，0新图、0新参数、0Lean实例。此结论只针对已经接受的同一字面GF4构造降到标准F2³；不是C30所有binary构造或五覆盖的不存在证明。

## 实际输入与反例

输入为作者保存的 `research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json`，实际q=4、controller30点、120张有向边局部3×3矩阵、1920点、degree16。作者[源包](https://github.com/rmizuno42/ddp/tree/main/results/degree16-diameter3)及本地 `PROOF_ja.md` §1–2明确编码2=α、3=α+1，α²+α+1=0。旧q4合法性直接继承，没有重新生成或验收。

矩阵共1080个系数，其中0:420、1:376、α:152、α+1:132。实际首条arc是controller0、port0到controller18，其矩阵为

```
0 1 α
1 0 0
0 1 α+1
```

取原binary点x=(0,0,1)、noise=0，映像为(α,0,α+1)，不在F2³。因此保存的字面maps不保持标准binary fiber。这个检查只是读取矩阵的一列，没有重跑旧field/rank/邻域/距离证书。

不能把整数编码直接mod2作为同一域特化：α²+α+1在F2没有根，故不存在保1的F4→F2域同态。重新编码或另选binary edge-local matrices属于新构造，需要新的true-inverse/direction/源合法性输入，本批没有这样做。

## 继承旧失败的准确范围

已读 `research/ddp/breadth_20261027_wave5/binary_route_chart3/REPORT.md` 和 `terminal.json`：其完整排除仅针对四个global逆标签矩阵、要求36个约化三步词各自单route满秩的模型。它不排edge-local矩阵、多route联合覆盖或一般binary C30源。`f4_degree19_retained_vertices_gate/check_controller.py`实际使用GF4/C60/五ports保点删边规则，也不提供C30/q2排除。

指定缓存没有定位到已验收的q2/240源。这是当前输入缺口，不是全局不存在结论。由于当前字面源不能直接定义所需binary关系，条件中的degree8/order240和五覆盖order1200都未成为实际图。

## 路线计数与下一步

≤4非回退walk最小计数/实际pair均为空值，状态为 `NOT_RUN_NO_VALID_LITERAL_BINARY_BASE`。不在虚构的240点关系上做容量计数，也没有生成1200图、调用solver/BFS/Lean/外审。

此固定降域规则停止。若之后提出真实的F2 edge-local charts及其旧验收或新合法性证据，才有输入可检验每对至少5条≤4非回退路线；即使该必要门通过，也不等于存在保degree8的Z5-cover。本批不启动这样的新chart搜索。

可复现小脚本 `check_literal_domain.py` 只读取参数和标准basis列。成功进程CPU为0.034669秒；加先前metadata读取的已计部分为0.036295606秒。短只读命令、文件准备及首个路径索引失败未单独计时，故此数字明确是已测进程小计而非伪精确累计；全批只发生少量本地读写，预算10CPU。第一次repo路径索引错误及最小修复保存在 `ATTEMPTS.json`，不是数学失败。
