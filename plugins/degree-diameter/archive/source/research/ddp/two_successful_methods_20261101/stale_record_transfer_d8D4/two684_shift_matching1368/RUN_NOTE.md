# shared right-t 的完整结果

事前“存在非 automorphism t 同时补齐四个跨层槽”的预测被推翻。实际 H342 域完整处理 342/342 个 t：labels 0、171（坐标 `(0,0)`、`(19,0)`）对全部四个 source voltage sets 均满足共轭保持，因此 right shift 是源自同构；对应双副本图同构于 source□K2，继承源 exact D4 得 exact D5，纸面 prune，没有运行其 endpoint coverage。

其余 340 个 t 均在第一个 `τ=0→ρ=0` 槽失败，故不再检查后三槽。`ALL342_T_SLOT_RESULTS.json` / `.tsv` 对后三槽明确记 `NOT_TESTED`，不能把它们写成已知失败或转成普通坏点对数。正向命中数为 0，未生成任何 1368 图。

首具体失败为 t label 1、坐标 `(0,1)`：0→0 槽只覆盖 288/342，缺 54 个目标，包含 group identity。这给最终图 copy0 label 0 到 copy1 label 684 没有长度≤4 的跨 copy 路线；匹配一步加 inherited host D4 给长度≤5，故该 pair 距离恰 5。结论来自完整 one-cross word endpoint union 和纸面上界，不是额外 BFS。

实际源 cache 只 parse 一次，2394 条字面边与 recovered recipe 的 h*s 关系完全相等。一次 exact-length 0..3 endpoint DP 后复用四槽 factor-pair 集合，大小分别为 576、621、621、576。对 source 两 τ 左 H 平移给所有 copy0 出发点覆盖；反向跨层由无向路径反向继承。总长度≤4 含三次 crossing 时必出现相邻 matching 来回可删，因此 one-cross 条件没有漏掉短跨层路线。

所以本次完整关闭的是 **固定 actual Michel684 源、完整双副本、type-preserving matching `(τ,h,0)–(τ,h*t,1)` 且两个 τ 共享同一个 t∈H342** 的族。两个 τ 取不同 t、更一般匹配、换 host 或一般 (8,4) 均未排除，本批不自动继续。所有 source/candidate BFS 数均为 0，未重验源 D4。

新实际进程 0.096522801 CPU 秒；继承 readgate 保守计 1.5、新准备计 0.25，累计 1.846522801/10。新终态独立保存为 `RUN_TERMINAL.json`，原 `TERMINAL.json` 仍是先前只读 gate 的历史。无 active process。
