# 单个 C5-invariant Q 与完全自由 P：事前预测

这是共同 C5 域完整 NO 后的实际生成规则改变：只保 Q 的已有 C5，允许 P 是40points上的任意 perfect matching。两侧不再共享 C5 对称；不重旧双自由1560变量窗口，不更换 action 或第二个 Q。

本次正假设：按以下唯一确定规则选出的 Q 存在一个 P，使80/200达到 D3。先读已存全部65625个 Q，用 `PAPER_INTERFACE.md` 已证的完整 unrestricted 必要条件筛 `i_Q(l)<=3`、`j_Q(p)<=1`。i_Q 数 Q edges 双端在13元 closedC(line)，j_Q 数 Q edges 双端在4line-pencil；各Q四blocks的8orbit-rep整数系数相加，不能把重复系数去重。合格者按旧 contribution coverage 最大、旧matchingindex 最小选唯一 Q；保存全部筛选结果与实际profile。

固定该Q后，原1080 exact far clauses中被Q满足者删除，其他保原780个P边变量的正OR；40 matching equations，P保全部 collinear choices。添加已读证明的 full-valid cuts：`i_P(p)<=3-3*j_Q(p)`，以及 `j_P(l)<=floor((3-i_Q(l))/3)`。这些是必要后果，不另加 girth5。

显式排除已闭共同C5域：引入 w_e，要求 `w_e=>x_e`、`w_e=>not x_g(e)`，且存在一个 w_e。存在这样的边界 iff P不保持该实际C5；不限制成新的未证明 WLOG。使用现成单线程CaDiCaL唯一一次窗口，配置19秒、CPU hard20秒（上限不超过root授权20），无安装/重试/第二solver。

SAT须核实际assignment、全部原80matching等式/1080覆盖式和真实<=3路，然后才写80/200候选交root独验；UNSAT只属于此固定Q/Pfree有限模型及数值solver证据尺度，其他Q仍UNKNOWN；timeout保存UNKNOWN原handle终态，不延时。全case cap30，继承3.272020095，新准备计0.25；Python自身soft5/hard6与child hard20合计仍在30内。0重C5/side枚举/source BFS/field/GQ/Lean/远程。
