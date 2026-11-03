# 完整 H-left-equivariant matching：事前预测与有限域

继承 shared-right-t 完整 NO 后，root 明确授权此新自由度；不重旧342参数判定。本次仍固定 actual Michel684 两份源图、H342、原 source 电压与 degree8，只允许所有 H-left-equivariant bijections。

完整域为 `π∈{id,swap}` 和独立 `t0,t1∈H342`：
`(σ,h,copy0) ↔ (πσ,h*tσ,copy1)`。
反向 matching 是该双射的逆，不要求 t1=t0^-1。总域 2×342²=233928，其中 π=id 且 t0=t1 的342项已严格排除并跳过候选判定，剩233586个新参数。

本轮可推翻预测：放开两个 type 的平移后，来自不同中间 type 的路线互补可令至少一个参数补齐四个跨 copy 槽。使用原保存 exact-length0..3 endpoints，不重 DP/source parse/source D4。对每个 π、σ、tσ 预计算四槽 mask：
`C[τ,σ,ρ](tσ,πσ)=union_{i+j≤3} A[τ,σ](i)*tσ*A[πσ,ρ](j)`。
完整 slot 为两 σ masks 的 OR；**保留 σ 分量**，不能沿用 shared门将不同 σ 的 `(a,b)` 合并后丢其归属。

逐候选四槽到首失败，保存 π/t0/t1、首失败槽、missing count/首missing及可恢复完整missing的预计算mask。后续槽视为 NOT_TESTED。第一全四槽 hit 保存完整1368/5472边表、参数和每槽每个target的实际≤4路线后停，交 root fresh 验收；所有项 NO 才完整关闭本 fixed-host H-equivariant matching 族，不排任意matching/其他host。

原case cap10 CPU不重置：已用1.846522801，新准备保守计0.25，唯一进程hard cap7；准备/失败/输出均在该余量内。0 sourceD4/BFS，0未命中图构造，0 field/Lean/solver/远程；用 FULL_* 区分旧终态。
