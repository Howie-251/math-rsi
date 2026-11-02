# 全部精确组、全部目标：K2 整数模型准备

冻结范围为现有完整 3589 个 `(R3,R4)` 精确覆盖组及全部 94186 个旧目标。
不使用分数权重删列，不继承 391 正组限制，不做稀行抽样或新的对称规范。
每组每 helper 至多选择一次；两侧各≤13，容量1组两侧互斥，容量2组可共享。
每目标加入 `R4(A)∨R3(B)` 与 `R4(B)∨R3(A)`；只合并完整 literal 集合相同的行。

本次准备检验完整共同整数条件能否被实际生成，不预言 SAT 或 UNSAT。
先前 391 池 UNKNOWN 不能排全部合法组；原 all-port 稀行 UNKNOWN 也不是此完整模型。
3589 组约简保全原 3685 个 freeport 的 K2 操作，具体组成员与 spare 继承现成证据。

准备单 worker、编译及 native/driver 合计 CPU≤90 秒。只读原 57 uint64/target
的 R3/R4 支持缓存和 PORT_GROUPS，不读 literal 图、不 BFS、不导图、不求解。
若准备未完成或超预算，保存实际状态，不把删减目标的产物冒作 fulltarget。
生成后交 root 审阅；拟后续最多一次 solver300 / whole420 CPU，UNKNOWN 即停，
该调用尚未启动。本目录无自动 solve 入口。
