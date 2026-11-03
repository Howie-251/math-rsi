# 两份固定6804源＋matching：实际全point域NO

结论严格限定：保留两份同一simple13regular6804源的全部旧边，**只增加两copy间的任意perfect matching**，不能得到13608点、最大度14、D≤4图。无需matching保phase、affine、group或任何source对称性。一般(14,4)问题仍开放。

这是有限球数据与 `POINT_BALL_OVERLAP_PAPER.md` 的覆盖证明结合，不是sourceD4重验、Lean或付费外审。一次只读核对 `OVERLAP_RESULT.json`、`overlap_gate.cpp` 与profiles摘要后，未见与公式不符；没有独立重跑。

实际全source R2/R3 maxima为B2=154、S2=140、B3=1588、S3=1434，B1=14。旧“所有roots均为(1,13,138,1400,5252)”已被root1/2的实际profiles反驳，不再作为证明前提。正确union raw上界

    Umax=1588+13·154+140·14+1434=6984。

实际witness y=0对全部6803个z≠0的 `|B3(0)∩B2(z)|` 排序，13个最小值均20，和为260。对任意M取u=M^−1(0)，13个旧邻点的M-images互异且≠0，因此跨copy R4覆盖至多

    6984−260=6724<6804。

至少80个对面targets不能在4步内到达，故全匹配族NO；只需这个存在性witness，不依赖Aut84的81个代表或未计算的all-y Lmin。全部6804 profiles取max消除了先前uniform/Aut上界依赖。若源D4也沿用，则该两copy规则有上界5、现在又排4，条件上只会得到D5；没有实际生产失败图或登记新图。

可选同域单调推论：若只加一部分cross matching（每点至多一条cross），它可在两个等大copy的剩余未匹配点之间补成perfect matching；加边不增距离。若某partial cross matching已D≤4，其补全也会D≤4，与上证矛盾。因此同一only-cross规则下partial matching也不行。由于旧源每点13度、cap14，only-cross额外边本来就必须构成partial matching。这个推论**不包含另加copy内oldold边**，因为那些边也消耗余度且不能直接按该单调补全保留。

仍未排：允许新增copy内oldold边、删改旧边、多helper/新顶点、非本cap的cross连接、其他source或一般13608/14D4构造。ordinary phase capacity已FEASIBLE；NB phase capacity仍原始8秒UNKNOWN，不冒INFEASIBLE。必要模型没解/可行与实际point族的更强NO各自保留原状态。

实际query line累计 **13.170781895/15CPU秒**，包括初始输入格式失败及初81之后扩全6804的修正。当前0sourceD4-validation BFS、field、Lean、ARIS、额外solver或新图计数。停止本两copy only-cross机制，不加验证或换phase/fibre随机梯。
