# 实际 H342 shared right-t 完整有限门：事前预测

在只读 source gate 后、数值枚举前登记。本 case 累计 CPU cap 10，继承只读门保守 1.5；本次准备再计 0.25，唯一单 worker 进程 hard CPU cap 7。不重 source D4/BFS，不执行旧 recover_684.py，不扩 t0/t1、source、phase 或 degree。

实际源是两 type τ∈{0,1} 的 H=C38⋊23 C9 右电压图，labels `342*τ+9*a+b`，边 `(τ,h)—(ρ,h*s)`。只把完整旧 source edge cache parse 一次，与已恢复 H law/S 的字面关系绑定一次作为新输入。H 的字面 342 个 t 是全部参数域，不假定 source 为 Cayley684。

跨 copy 匹配为 `(τ,h,0)—(τ,h*t,1)`。保留两份原图后每点度 8，若完整成功则 1368/5472。一次生成 exact-length i=0..3 的旧步端点集合 `A_{τσ}(i)`；它们只是本新跨层问题的词端点输入，不是源 D4 验收。所有跨 copy 长≤4 最短路只需一条 matching：三次 crossing 配至多一个旧步时必有相邻 matching 逆步可删。故四个实际 slots 必须且只需

`C_{τρ}(t)= union_{σ, i+j≤3} A_{τσ}(i) * t * A_{σρ}(j) = H`。

正向、可推翻的预测：存在一个非 automorphism t，使四个 C slots 全覆盖 H342。按 t 的 label 升序查到首失败 slot 即可停止该 t，后续 slot 明标 NOT_TESTED，不冒普通坏点对数。对满足全部四集合 `t^-1*S_{τρ}*t=S_{τρ}` 的 t，right shift 是源自同构，twocopy 图同构于 source□K2、直径5；该 t 可以纸面 prune，不运行其 endpoint coverage gate。

第一完整 hit 保存全 1368 图、参数及四 slots 的逐 target actual word-factor witnesses 后立即停，交 root 独立验收。全部342 t 被严格拒绝时，只关闭 fixed actual684 host、type-preserving one shared right-t 的本族；不排一般1368/max8/D4图或更自由的matching。未命中项不构造1368图，不运行candidate BFS/Lean/solver/外审。
