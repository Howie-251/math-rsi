# 两份684：K19等变匹配的实际接口读取门

结论：K19动作、36个19点轨道及24,624个one-hot选择的参数域，在实际source约定下成立；它严格大于已经完整排除的H342等变域。有限same-source历史读取未定位相同K19域的strict NO。本轮只读现有PAPER/FINAL/DOMAIN/recipe，不计算新endpoint、生成图、运行source/候选BFS、field、solver、Lean或外审。

## 实际law与labels

`research/ddp/m1_sources/684_recovered_construction.json` 和只读 `recover_684.py` 明确

`(a,b)(c,d)=(a+23^b*c mod38,b+d mod9)`，

旧点label为 `342*tau+9*a+b`，边为 `(tau,h)--(rho,h*s)`。实际源是H342的两个左作用轨道，不是684点Cayley图；degree7/D4/2394边及恢复与literal相等都继承旧证据，本轮不重新验。

令 K={(2*l,0):l∈Z19}。其左作用直接是 `(tau,a,b)->(tau,a+2*l,b)`；作用自由，并且共轭 `h(2*l,0)h^-1=(2*23^b*l,0)` 仍在K。因此K为正常C19。轨道固定tau、b和epsilon=a mod2，总数2*9*2=36，每轨道19点。

为避免未绑定的orbit编号，可明确取

`r=18*tau+2*b+epsilon`，
`nu(r,k)=342*tau+9*(epsilon+2*k)+b (0<=k<19)`。

代表是nu(r,0)，左(2*l,0)恰使k→k+l。反解actual label时，先tau=floor(v/342)，a=floor((v−342*tau)/9)，b=(v−342*tau)mod9，再epsilon=a mod2、k=(a−epsilon)/2。这里a=epsilon+2k本身已在0..37，无需猜新的顶点重标。

对实际port s=(c,d)∈S_tau,rho，令m=[epsilon+23^b*c]_38。旧邻点的orbit为 `(rho,(b+d)mod9,m mod2)`，K-voltage为 `lambda=(m−(m mod2))/2 mod19`；因此 `(r,k)->(rprime,k+lambda)`。这是符号入口，未重新计算36×7常数表或旧graph。

## 新完整域及旧NO的准确边界

自由K作用的等变bijection必为

`(r,k,copy0) <-> (sigma(r),k+t_r,copy1)`，

其中sigma∈S36、t_r∈Z19各独立。等变性强制每轨道斜率1；反向按sigma^-1及−t，不要求sigma是involution，也不要求相配shift互为相反。36²*19=24624 binary选择，36条出轨道与36条入轨道等式，恰好定义一个perfect matching。

旧 `ROOT_DISPOSITION.json` 已完整关闭全部 `(tau,h)->(pi(tau),h*t_tau)` 的H-left-equivariant匹配（233928参数，含旧342）。因K⊂H，旧域包含于新域；且严格包含：仅在一个K轨道shift1、其余35轨道不动，仍K-equivariant，但不是H-equivariant。非identity的H右移在整个同一tau的342点轨道上没有fixed point，不能只移动其中19点。

因此旧NO不能套给本域。反过来不能把K域称任意684点matching；不同K轨道的非平移内部置换、归一化K而不逐元素交换它的maps等仍在本域外。这里没有提出额外WLOG/gauge。

## exact-cover入口：端点集合而非walk容量

以A_ij^(a)⊂Z19表示旧source从(i,0)经恰a步到j轨道的实际K坐标集合。对每源根轨道i、目标轨道j和相对坐标k，有一项cross-point义务，共36²*19=24624项。

选择变量(r→s,t)覆盖该义务，当且仅当存在a+b≤3、x∈A_ir^(a)、y∈A_sj^(b)，满足

`k=x+t+y mod19`。

prefix到(r,x)，matching到(s,x+t)，再由旧K对称把suffix坐标加到x+t+y。全部selected choices的覆盖并正是实际≤4的一cross端点集合，不是walk数上界。三次cross在总长≤4时必有连续匹配往返可消；该论证对任意perfect matching成立。因此one-hot约束加全部实际endpoint OR clauses在本域是精确cross覆盖模型。

K只把同一19点轨道的roots互相归一化；必须36个source代表，不可继续只用旧完整H对称的两个tau根。另一方面forward-copy全交叉义务已覆盖反向距离，因为matching与图均无向。旧两份source内部D4全保，不需重复oldsource全验；数学上所有精确cross义务通过才会给一个确定matching的条件D4构造，实际graph/binding/fresh验收本轮均未执行。

可复用 `OLD_LENGTH_LE3_ENDPOINT_SETS.json`（已有exact lengths0..3的H-typed rows）。对任一新代表h_r=(epsilon,b)，源旧路endpoint由旧缓存u变成h_r*u，再按actual label分解成K的orbit/坐标。旧legs仍有完整H左对称，因此这一坐标转换不要求重新DP；但最终matching只有K对称，不能把whole-candidate roots也缩回2个。

## 处置

这是实际source与未闭自由度的读取门。没有新36orbit表、端点coverage或模型数值结果，不能写SAT/UNSAT或candidate存在。累计read/prep保守计1.0 CPU秒（cap5），0sourceparse/DP/BFS/field/solver/图/Lean/外审/HTTP。停止；是否进行完整预计算与哪一个有限窗口由root另定，不追加host、degree或phase清单。
