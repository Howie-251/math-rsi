# 完整 H-equivariant matching 域：没有补齐第一跨层槽

本批把 shared t 改成两个 source type 的独立 t0/t1，并允许 type permutation π=id/swap。它不是围绕遗漏点数的续算，而是检验同一已定位源中两个中间 type 的传输路线能否真正互补。该参数化覆盖全部 H-left-equivariant perfect matchings：每个自由 H orbit 的基点像决定整 orbit 像，双射条件迫使两个 target orbits 构成 π；随后 `f(σ,h)=(πσ,h*tσ)`。

完整域 233928 个参数中，已经排除的 id/shared342 项全部跳过、没有重复 candidate 判定。本次新访问 233586：id 部分 116622，swap 部分 116964，均在第一个 `τ=0→ρ=0` 跨 copy 槽失败。没有任何项进入后三槽；后三槽只标 NOT_TESTED，不称全图坏点对统计。正向预测被推翻，完整命中为 0，未生成任何 1368 图。

首失败新参数为 `π=id,t0=0,t1=1`，0→0 槽缺 138 个 H targets，首缺 group label1。每个参数的 first-failed slot、缺失数及首缺标签保存在 `FULL_ALL_NEW_PARAMETERS.tsv`；完整缺失集合可由 `FULL_PER_SIGMA_MASKS.json` 中两份实际 mask 的 OR 精确恢复。这里保留 σ，并对每个 σ 使用 suffix `A[πσ][j][ρ]`，没有错误地将 shared 门里跨 σ 去重的 `(a,b)` 当作独立参数的共同项。

所有 mask 只读取并复用原先冻结的 exact-length0..3 endpoint cache；0 重新 source raw parse、0 endpoint DP、0 source/candidate BFS、0 未命中图构造。对于跨层长度≤4，三次 crossing 必有相邻 matching 逆步可删，因此一次 crossing 的端点 OR 已经是精确短路线条件。结合旧 shared342 完整 NO，本次严格关闭 **固定 actual Michel684 双副本、所有 H-left-equivariant perfect matching** 的范围；不排任意不保持 H 对称的 matching、修改 source oldedges、增加第二跨层边或其他 host。

新进程 0.827105678 CPU 秒，新准备计 0.25，继承 1.846522801，wholecase 为 2.923628479/10。`FULL_TERMINAL.json` 为本批实际终态，所有数值进程已停。下一规则需 root 重新根据该结构结果选择，本批不自动展开。
