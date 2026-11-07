# 可直接供给当前义务的数学内容

以下把原包定义和承重接口整理成可调用形式；完整证明随archive保留，当前结构稿的unreviewed/unaccepted状态不因整理而改变。`P`指[原证明目录](../../../archive/source/working/package/proofs/READING_GUIDE.md)，`R`指其中source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research。当前任务应给自己的原对象与caller，不恢复R中历史任务。

## 状态注入与基数归纳

完整三元染色、禁B5/R6下，每个末对(u,v)给LB/LR；D(v)是(LB−1,LR−1)在[3]×[4]的向下闭包。若u<v且σ(u,v)∈D(u)，某t<u同时支配蓝红阈值，三元组tuv的颜色必延长一色路径，矛盾，所以σ(u,v)∈D(v)\D(u)。因此D(v)互异，35状态上界并不依赖split禁形。

25普通状态宽+高≤6，其余10异常。异常可以出现：本次重验的25点见证e=m9。不能以weak7-free推“异常皆空”；同右端蓝4红5只是split7，可能不同左端。

精确恒等式n=25+e−m。Ct: e≥t⇒m≥t，t1…10。t1失败必m0；已得C(t−1)且Ct失败时，e≥t而m≤t−1，同时m≥t−1，故m=t−1。e=t…10，n=26+e−t，55域对每一个真实反例覆盖。全部对应CNF不可满足与lifting结合，才有Ct；取t=e得m≥e，所以n≤25。原[cardinality-layer-theorem](../../../archive/source/working/package/proofs/sat-756/evidence/E01/cardinality-layer-theorem.md)及编码说明给逐项细节。历史接受与本次见证核验分列。

## 实际覆盖与严格增广

对禁B_r/R_s的X，A为不能结束B_(r−1)的点，B为不能开始R_(s−1)的点。若v不属A∪B，蓝前路径和红后路径在v连接，桥三元组任一颜色都超帽。于是实际A∪B=X；先核诱导禁形，再用相应容量。

766得到≤2b；严格扣一不能从同一公式免费取得。757的a+b−1需要在无交叠情况下，保留全部阻止合法单点增广的实际路径支持，并用共同点对偏序排支持有向环。否则每点有出边迫环矛盾，故可增广/交叠。原[R5](../../../archive/source/working/package/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md)包含完整证明和外部偏序定位。其q6混接范围不能自动迁到766。消费a16和b25给40/50，而非只凭b25得40。

## 767的共同母体与补偿

[最新双向稿](../../../archive/source/working/package/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)使用ambient R6首末点S/T；D=X\(S∪T)的内部R5首末交集C0，w=|C0|。canonical→promotion→M0必须从任意X取得；[义务审计](../../../archive/source/working/package/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)§2补参数无关M0，使旧缺额≤2接口不再被未经证明地套到3或任意缺额。

中间图边是实际R5的外端点并保留路径；左右图边是全部实际R6末对/首对。容量和König给实际匹配下界。在同一份固定中间匹配上扣左右未覆盖端口，才能证明两侧击中同一中间边。其j<r<s<k由禁R7迫蓝(j,r,s)、蓝(r,s,k)，得蓝4，与R5(j→k)同端，违反weak7。

旧低前驱集合漏了末根落Ω的实际贡献。改收全部普通低前驱ℛ，把同一τ=|ℛ|个点合法加进对侧修补核，左匹配损≤τ和右容量收益≥τ抵消。双向也对高后继实行；严格交错、严格分离、共根三入口共用真实母体，交点损失只扣一次。最新双向稿推n+w≤3b+1，早单向稿仅有加权≤3b+2再排w0临界层得无权≤3b+1。不能把这两版加权式混为矛盾或把旧audit视为已独审最新稿。

以上是旧单向/双向稿阶段：代b25曾得767≤76，w≥1子类≤75。完整新原件已经补齐最终替锁：当前工作界767≤75、777≤76，w≥1子类≤74；仍为same-session/unreviewed/unaccepted。取等链、两个实际容量域与端点相容性的详细步骤见[新执行说明](equality-exchange.md)。旧稿保留作依赖，不再将其当今日开放缺口。

## 合法chart、两次加一与几何边界

[R20](../../../archive/source/working/package/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)先刻画weak子集的balanced packet，再证明两个合法chart间不变。只取原最左pivot作径向排序，以排列奇偶运输三元符号，另核非pivot四点合法；不是任意排列、内部pivot或保packet操作都可用。删除pivot并换色后实际得到767，逆向向任意767左添蓝点证明反方向，故777=767+1。

N_geo≤N_sig，加最大避免到强迫的定义转换后才有ES≤N_sig777+1。于是旧工作链25→76→77→78、新工作链25→75→76→77有不同指标，不是同一函数随时间增加，也不宣称抽象极值可实现平面坐标。25抽象见证只能给N_sig756≥25；几何25下界要另核外部坐标或构造进口。

## 实际使用任务例

给作者：“任意当前767母体X，已有canonical和M0入口见指定稿。请只补低前驱ℛ→对侧合法扩核的证明，包含末根在Ω与多新点混合路径，返回τ剪枝损失/对侧收益如何在**给定同一中间匹配M**上结算。只写本任务子目录；条件未满足就给准确反例/缺口。” 收回后把真实集合代回原X：若只能处理Ω外前驱，保持全义务开放；若全部供给成立，继续交会与共根分流，不再请作者重排一遍全文。

## 新原稿的使用次序

[临界取等与交换](equality-exchange.md)§1–4从全供给的角色/实际点夹等式开始，消费旧根排除，再在两个实际b+1域容量迫证；不是从历史稿末尾的“开放”恢复旧研究。§5以新人口层重新算非负松弛，保留regular共根n+Λ≤3b的全部前提与剩余三支。无条件全局≤74和n+w≤3b均未得到。§6给原色规则、反例否定范围和真实小checker入口，供route-loop否定准确过强引理。
