# 一次assignment→fixed-shift分解：必要projection与exact固定σ模型

状态：纯paper确认，0新cache/source读取、数值、BFS、field、solver、Lean或ARIS。原fullpoint CNF唯一60s返回cUNKNOWN、无candidate的历史保持；本次是root另授权的不同分解策略，不续原SAT时钟，不变更该原始状态。

## 1. packet B与assignment容量projection

沿用 `MODEL_EXACTNESS_PAPER.md` 的36个K-orbits、C19 shifts与exact oldendpoint缓存。定义

    B(i,j;r,s)=union_(a+b≤3)[A_a(i,r)+A_b(s,j)] ⊆C19。

选choice(r,s,t)的actual targets恰为B(i,j;r,s)+t。因为C19平移是bijection，packet大小

    m(i,j;r,s)=|B(i,j;r,s)|

与t无关。它已是同一choice内部跨old splits去重后的distinct point数，不是ordinarywalk multiplicity。

对任意actualmatching(σ,t)，完整targetorbit j的19点需由

    union_r [B(i,j;r,σ(r))+t_r]=C19

覆盖。因此必要有 `sum_r m(i,j;r,σ(r))≥19`，但一般不充分，packet间可能反复覆盖相同点。这是projection的全部数学含义，maxmin提高本身不登记graph/record成果。

用1296个binary X_(r,s)，36row/36col各sum=1表示任意σ，保留σ非involution、σ(0)不固定。加integer bottleneck z，全部36²个i,j约束

    sum_(r,s) m(i,j;r,s) X_(r,s) ≥ z。

最大化z寻找容量较好的唯一assignment。安全上界可用36·19，任何更紧上界都必须是实际有效上界。只有**实际integer incumbent**手检成permutation且把所有36²个真实packet和重算后minimum≥19，才冻结为本轮唯一σ；不能仅信浮点z或fractional assignment。

若限时只得minimum<19的incumbent，不能从“不合格的当前解”推出所有σ失败，也不据此启动注定不满足必要条件的fixed-shift模型。数学上只有完整证明projection最优<19才可排整个K19族；native rawstatus的证据边界照实际回执保存。本批无第二assignment求解或σ2。

## 2. 固定σ后的shift模型是完整点覆盖

冻结一张已手检的σ后，变量只有Y_(r,t)，r=0..35、t∈C19，每row恰一个shift。无须再加column constraints：σ本来是permutation，任意这些shifts都在目标orbit内给19点bijection。

对每个实际target(i,j,k)，coverage clause精确为

    OR {Y_(r,t) : k∈B(i,j;r,σ(r))+t}。

由旧paper的once-cross和K-equivariance，这些正OR连同每row exactly-one，SAT当且仅当这张**固定σ**存在一组shifts，令两份源图的全部crosspairs≤4。samecopy D4由source旧边全保继承。不是packet容量近似，也不允许每个target选择不同的全局shift。

36×19=684个真实shift变量。每组19的标准Sinz AMO用18个aux，36组共648，因此总1332变量。未简化schema中：每组1个ALO+53个AMO clauses，共1944；点覆盖36×36×19=24624；row0的18个非零shift unitfalse。因此预计总26586 clauses。合法dedup/已真子句消除可改变实际数，不改变exact scope；空coverage OR不能误删。

## 3. 固定σ也能用t0=0，不必重择σ

上层paper的gauge是在copy1后compose同一个globalleftK(−t0)。它是actualsource automorphism，且K循环，使所有t_r同减t0而σ完全不变。因此在该固定assignment下令t0=0仍不丢任何可行shift解；只禁row0的18个非零shifts，不能顺便固定σ0或引入σ自逆约束。

## 4. 输出状态与预算的精确解释

* projection有合格整数incumbent，只说明可以执行该唯一fixed-σ窗口，不是K19 graph已存在。
* fixed-σ SAT须手检36choices、展开684matching边与全部actual point coverage，再写完整1368/degree8字面图交root/fresh；不以solver字符串或maxmin数值计成果。新formal另由root触发，当前不编旧kernel。
* fixed-σ rawUNSAT至多排这张σ的所有shifts（t0 gauge已证明不丢域），不能覆盖其他projection-feasible σ；原全point60s UNKNOWN不能因该单σ失败改成全K19 NO。
* projection或offset时限无witness都保持相应UNKNOWN。没有合格σ就跳过offset；不续MIP、不换σ2、seed或secondoffsetwindow。早期退出省下的CPU不是自动扩范围授权。

同case100CPU原账继续，包含oldread/prep/compile/build/原60s以及本次≤5s assignment与≤20s shift窗口的父子全部成本。两个不同阶段要分别保存status与witness；不能把maxmin、SAT与actualgraph三个层级合成一个PASS。packet/caches只复用、不新sourceDP/BFS；完成paper即停。
