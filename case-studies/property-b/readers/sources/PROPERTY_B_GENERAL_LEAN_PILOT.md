# 一般RS概率核心与17元Lean试点

本阶段已完成一般真实RS失败概率界、原染色充分判据，以及任意有限简单17元、至多2^17边超图的完整Lean调用；三个最终导出已通过指定Lake构建，构建后的独立原命题caller与公理审计也已通过。证明从实际重染算法出发，将任意p的加权正关联、初始单色边平均、真实排列次序和精确积分接到原顶点集上的Bool染色。

**形式证明、本机独立审计与两家最终审阅均已完成（2026-10-21）。** 指定`lake build Aris4Math.General.RS.PilotMain`成功，构建后独立根审计`ReviewAuditGeneralRSPilot.lean`也exit0；七项传递公理均仅标准三项。Grok与Gemini均在一般RS概率界、原染色判据和17元调用的范围内认可结果，未发现实质问题。两家静态读取当前源码与已有日志，没有执行Lean。正式证据为[final-build.log](context/propertyb-general-lean-pilot/final-build.log)、[final-build-result.json](context/propertyb-general-lean-pilot/final-build-result.json)、[final-audit.log](context/propertyb-general-lean-pilot/final-audit.log)、[final-audit-result.json](context/propertyb-general-lean-pilot/final-audit-result.json)，完整审阅记录在[reviews/C/](context/propertyb-general-lean-pilot/reviews/C)。


## 阶段结果与最终接口

设E是任意有限简单k元超图的实际边集，m=|E|，γ(E)计**有向**恰交一点的原边对。置

$$a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,\qquad d=2^{k-1}.$$

三个已正式构建并审计的实际导出接口如下。

|导出|原始假设与结论|源码|
|---|---|---|
|`rs_recoloring_failure_le`|任意`[Finite V]`、`Uniform E k`、k≥2及0<p≤1；真实RS失败概率≤$1-a_k(p)^{m/d}+\gamma(E)J_k(p)/d^2$|[ProbabilityBound.lean](formal/Aris4Math/General/RS/ProbabilityBound.lean)|
|`propertyB_of_rs_bound`|上述显式右侧严格小于1，即给原顶点集上的实际Bool染色，每条原边同时含两色|[ProbabilityBound.lean](formal/Aris4Math/General/RS/ProbabilityBound.lean)|
|`propertyB_seventeen_of_at_most_two_pow : PilotTarget`|任意`[Finite V]`上的简单17元超图，边数≤2^17，具有Property B|[PilotMain.lean](formal/Aris4Math/General/RS/PilotMain.lean)|

通用判据保留的是用户可检验的数值充分条件；实际算法、失败覆盖、正关联、单交对概率和有限并界均已在证明依赖链内连接，相关外部前提已经消去。17元接口只留下原来的有限性、uniformity和边数假设，没有概率界、内部证书、点数、度数或点对覆盖前提。

17元数值调用取p=1/17。已核的精确有理数计算给a₁₇(p)>1/2，且J₁₇(p)≤1/17。m≤2^17使m/2^16≤2，故a的幂项大于1/4；实际γ(E)≤m²使积分项至多4/17<1/4。于是目标右侧严格小于1。该调用包括空边族。

## 一条真实概率链

样本由三部分组成：均匀初始Bool颜色、独立Bernoulli(p)资格位，以及均匀全顶点排列。`SampleLaw.sampleWeight_nonneg`和`sum_sampleWeight`显式证明这个联合样本的权重非负、总和为1，已导入正式主入口。`σ x`表示x的处理时刻，按时刻递增扫描。一个点仅在有资格、属于初态单色且至今没有点翻转的原边时翻转；每点只处理一次。

`Algorithm.failure_covered`把每个实际失败分到初态原色残留，或某个真实有向单交原边对和最终颜色。后一分支选最后由反色翻来的点；触发边当时尚未翻转，迫使两边恰交该点。初态全为反色而最终全换色的边也在同一分支内。

初态残留项由实际初始单色边族的共同hit事件控制。Bernoulli Harris适用于这些重叠边，均值与有限Jensen给第一项。这里没有把边事件当作独立事件。

对于指定单交边对和指定颜色，`PairProbability`从实际`PairEvent`证明精确概率

$$\Pr(\text{PairEvent}_{f,g,q})=2^{1-2k}J_k(p).$$

证明固定颜色和资格位后，剩余事件恰是活跃点A全在枢轴之前、活跃点B全在之后。`OrderCounting.beforeAfter_ratio`在实际全排列样本内给比例a!b!/(a+b+1)!，不要求活跃点占满全部顶点。`Integral.beta_nat`把该比例写为∫₀¹tᵃ(1−t)ᵇdt；有限期望与积分交换，再由坐标因子平均得到

$$\int_0^1\frac p2\left(\frac{1+pt}{2}\right)^{k-1}
\left(\frac{1-pt}{2}\right)^{k-1}dt
=2^{1-2k}J_k(p).$$

因此有限排列表示避免了连续随机过程的可测性和碰撞零概率工程，同时精确保留同一个积分。对两个颜色及实际`singlePairs E`求和，系数恰为γ(E)/d²；共同Sample上的并界再连接原失败事件。最后由失败概率小于1提取实际成功样本，并沿顶点等价把最终染色拉回原V。

## 已执行的局部验证

|范围|已核内容|证据目录／日志|
|---|---|---|
|算法|初始色触发、最后翻转点、完整失败覆盖、成功即原边两色|[algorithm-build.log](context/propertyb-general-lean-pilot/algorithm-build.log)、[integration-first.log](context/propertyb-general-lean-pilot/integration-first.log)|
|Bernoulli|归一化权、任意p Harris、多事件hit、有限Jensen|[bernoulli/build-final.log](context/propertyb-general-lean-pilot/bernoulli/build-final.log)、[bernoulli/audit.log](context/propertyb-general-lean-pilot/bernoulli/audit.log)|
|初态平均|实际单色边均值、残留条件界／平均界，以及独立Algorithm.ResidualEvent caller|[initial-average/build05.log](context/propertyb-general-lean-pilot/initial-average/build05.log)、[initial-average/audit.log](context/propertyb-general-lean-pilot/initial-average/audit.log)|
|实际次序|任意活跃点的均匀相对次序与前／后块阶乘比例|[order-counting/BUILD.log](context/propertyb-general-lean-pilot/order-counting/BUILD.log)、[order-counting/CALLER.log](context/propertyb-general-lean-pilot/order-counting/CALLER.log)|
|精确积分|整数Beta积分、有限双和恒等式、J重标度与界|[integral/build06.log](context/propertyb-general-lean-pilot/integral/build06.log)、[integral/audit-final.log](context/propertyb-general-lean-pilot/integral/audit-final.log)|
|单交对概率|原始PairEvent的完整精确概率，非单交事件为零|[pair-probability/build-final.log](context/propertyb-general-lean-pilot/pair-probability/build-final.log)、[pair-probability/audit.log](context/propertyb-general-lean-pilot/pair-probability/audit.log)|
|数值调用|p=1/17严格预算及实际γ(E)≤m² caller|[pilot-estimates/build03.log](context/propertyb-general-lean-pilot/pilot-estimates/build03.log)、[pilot-estimates/audit.log](context/propertyb-general-lean-pilot/pilot-estimates/audit.log)|
|有限顶点传递|原边、uniformity、边数、γ和染色沿等价传递|[lift/BUILD.log](context/propertyb-general-lean-pilot/lift/BUILD.log)、[lift/CALLER.log](context/propertyb-general-lean-pilot/lift/CALLER.log)|
|共同样本与有限并界|实际Sample、联合权归一化SampleLaw及UnionBound|[sample-direct.log](context/propertyb-general-lean-pilot/sample-direct.log)、[union-build.log](context/propertyb-general-lean-pilot/union-build.log)、[final-build.log](context/propertyb-general-lean-pilot/final-build.log)、[final-audit.log](context/propertyb-general-lean-pilot/final-audit.log)|
|三个最终导出与原命题|一般P／C、PilotTarget及独立bare有限顶点／原边Bool见证caller|[assembly/PROBABILITY_BUILD.log](context/propertyb-general-lean-pilot/assembly/PROBABILITY_BUILD.log)、[assembly/PILOT_BUILD.log](context/propertyb-general-lean-pilot/assembly/PILOT_BUILD.log)、[assembly/CALLER.log](context/propertyb-general-lean-pilot/assembly/CALLER.log)|

正式根审计在实际构建后独立导入，复述裸`[Finite V]`、17元、≤131072边的原Bool两色结论及一般积分判据。七项被查导出和caller的传递公理均仅`propext`、`Classical.choice`、`Quot.sound`，无残留内部前提。以上属于本机独立导入和实际caller，不表示第二台机器复现。

固定环境为项目既有Lean4.24.0及Mathlib锁定版本。日志中的几项实际成本如下。局部项为source编译及olean生成；正式构建与根审计另列，不把它们解释为整个阶段开发时长。

|模块|墙钟秒|user CPU秒|日志|
|---|---:|---:|---|
|Bernoulli|12.05|3.61|[bernoulli/build-final.log](context/propertyb-general-lean-pilot/bernoulli/build-final.log)|
|OrderCounting|41.97|6.48|[order-counting/BUILD.log](context/propertyb-general-lean-pilot/order-counting/BUILD.log)|
|PairProbability|18.69|7.29|[pair-probability/build-final.log](context/propertyb-general-lean-pilot/pair-probability/build-final.log)|
|Lift|7.82|1.45|[lift/BUILD.log](context/propertyb-general-lean-pilot/lift/BUILD.log)|
|ProbabilityBound|7.97|4.12|[assembly/PROBABILITY_BUILD.log](context/propertyb-general-lean-pilot/assembly/PROBABILITY_BUILD.log)|
|PilotMain|7.21|2.65|[assembly/PILOT_BUILD.log](context/propertyb-general-lean-pilot/assembly/PILOT_BUILD.log)|
|独立原命题caller|9.63|4.65|[assembly/CALLER.log](context/propertyb-general-lean-pilot/assembly/CALLER.log)|
|正式PilotMain构建（既有缓存后）|18.58|29.54|[final-build.log](context/propertyb-general-lean-pilot/final-build.log)|
|构建后独立根审计|7.23|4.94|[final-audit.log](context/propertyb-general-lean-pilot/final-audit.log)|

局部运行与项目统一管理的共享依赖构建有重叠；共享依赖构建已完成2527 jobs，随后正式PilotMain构建完成2538 jobs并由确认调用记录exit0。这些是Lake依赖任务计数，包含缓存／重放，不能解释为新模块数。各时长不能相加成整个阶段成本，也不能按源码规模推算下一阶段；未独立计时的模块不补填数字。

## 审阅和复现入口

命题表达、实际算法／概率接口及最终导出分别接受审阅；最终C覆盖本阶段的三个完整结果和构建／公理证据。

|最终审阅|实际返回|结论与执行范围|原回应|
|---|---|---|---|
|Grok|`grok-4.7-build`／`xhigh`，`end_turn`|在P／C／Pilot范围内认可；静态源码与日志审阅，未执行Lean|[reviews/C/GROK_RESPONSE.txt](context/propertyb-general-lean-pilot/reviews/C/GROK_RESPONSE.txt)|
|Gemini|`gemini-4-argon-high`／`high`，`SUCCESS`|在P／C／Pilot范围内SOUND／ACCEPTED；静态源码与日志审阅，未执行Lean|[reviews/C/GEMINI_RESPONSE.txt](context/propertyb-general-lean-pilot/reviews/C/GEMINI_RESPONSE.txt)|

Gemini的型号与effort来源为CLI选择记录（`cli_selected_model_variant`）。模型审阅用于检查语义、数学连接和验收范围；内核证明与本机实际执行证据独立保留。本次终审没有把一般k≥17增长整数增益定理升级为已Lean验证。

正式复现入口为[formal/Aris4Math/General/RS/PilotMain.lean](formal/Aris4Math/General/RS/PilotMain.lean)。在项目根执行下列命令；Lean4.24.0、[formal/lean-toolchain](formal/lean-toolchain)及[formal/lake-manifest.json](formal/lake-manifest.json)固定既有依赖，不升级库，也不以旧默认Main的构建代替本模块。

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.General.RS.PilotMain
lake env lean ReviewAuditGeneralRSPilot.lean
```

正式Lake确认与独立根审计均记录exit0。根审计已从裸`[Finite V]`及原始Finset边集复述17元Bool染色、一般积分判据，并打印实际导出、定义与传递公理；源码为[formal/ReviewAuditGeneralRSPilot.lean](formal/ReviewAuditGeneralRSPilot.lean)，日志为[final-audit.log](context/propertyb-general-lean-pilot/final-audit.log)。

后续完整增长定理的准确剩余与建议见[FUTURE_FORMALIZATION.md](context/propertyb-general-lean-pilot/FUTURE_FORMALIZATION.md)。该阶段不自动启动，不恢复旧35／36研究。

## 完整一般增长定理：下一阶段的最小形式化范围

下一阶段有明确的复用边界：保留本阶段同一真实RS概率接口，在其上增加最小反例结构和统一参数分析。无需重新建设随机过程或再证明单交对概率。建议先验证结构削γ的真实caller，再实施全k≥17的增长整数增益；后续阶段需由用户另行启动。

目标仍是已有纸面定理

$$m(k)\ge B_{\mathrm{RS}}(k)+1+
\left\lfloor\frac{\sqrt{B_{\mathrm{RS}}(k)}}{8(1+\log k)}\right\rfloor,
\qquad k\ge17,$$

覆盖每个适用k的全部有限简单k元超图。B_RS是明确RS–FKG–精确积分判据接受的最大整数预算；它不是外部优化器返回的数值。纸面来源为[proofs/propertyb-general/CORE_THEOREM.md](proofs/propertyb-general/CORE_THEOREM.md)、[UNIFORM_INTEGER_GAIN.md](proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)和[CLIQUE_REFINEMENT.md](proofs/propertyb-general/CLIQUE_REFINEMENT.md)。

### 可以直接接用的接口

|已有内容|下一阶段的用途|
|---|---|
|Definitions的实际原边、Uniform、PropertyB、singlePairs和gamma|继续以原边为图顶点和概率事件索引，避免换成不相关的必要松弛|
|Algorithm、Sample、PairProbability、UnionBound|实际重染过程及失败事件估计，不再接受外供概率前提|
|InitialAverage、Bernoulli|任意p的重叠边正关联、初态均值和指数平均|
|Integral的jk、ak与精确恒等式|复用同一个J和a；新增的仅是一般下界及参数不等式|
|Lift|任意有限顶点与Fin n之间的边数、γ和原染色传递|
|ProbabilityBound的通用判据|正式构建与独立根审计已通过；在同一实际反例上代入结构γ上界，再由严格小于1得到矛盾|
|PilotEstimates|k=17数值caller和精确实数运算经验；不能直接替代所有k的参数控制|

上述接口及完整通用判据已通过正式PilotMain构建和构建后独立原命题／公理审计；本阶段两家最终跨家族审阅与实际验收证据集中见[REPORT.md](context/propertyb-general-lean-pilot/REPORT.md)。已有一般纸面claim的verified状态不等于这些新增结构定理已经Lean化。

### 先闭合真实结构削减

第一块是一般最小顶点反例。若预算N内存在非B超图，先用Lift将候选写在Fin n上，再对自然数n取最小值。在该实际反例中，若一对顶点从未同处一条边，则合并二者。需要证明每条原边在商映射上保持注入、像边仍为k元、像边去重后边数不增，且像染色可沿商映射拉回。像超图仍非B而顶点更少，产生矛盾。并不要求商前后γ不变；最终概率估计作用于所选同一最小反例。

由此得到点对覆盖，再双计数

$$v(v-1)\le k(k-1)m\le k(k-1)N.$$

先保留这一整数不等式作为核心接口，最后才在必要处转成v_k(N)的sqrt／floor表达式。这样可减少结构证明中过早的实数和取整转换。不补边至恰好N，也不增加顶点数或点对覆盖作为原定理假设。

第二块是实际单交图。图顶点应取原边的子类型`{e // e∈E}`，邻接表示两条不同原边恰交一点。需要真实计数连接：图的有向邻接对数正好是`gamma E`，补图边数与m(m−1)之差具有正确系数2。先用一个任意E的非平凡caller核准Mathlib的SimpleGraph、有限clique和边计数API，再展开结构层。

对一个实际单交团，公共点分流给

$$q(k-1)+1\le v
\quad\text{或}\quad
q\le k^2-k+1.$$

公共点支中去掉该点后的尾两两不交；无公共点支固定一条边e，对每个x∈e取一条不含x的团内边，证明所有含x边到该边的交点映射注入，因而d_x≤k，再求和q−1=∑(d_x−1)。这些是一般有限族计数，不需要团或超图枚举。

团界接Turán粗界后，应形成真实caller

$$\gamma(E)\le m^2(1-1/r).$$

优先试现有SimpleGraph Turán接口；若其有限图／计数约定转换更长，可复用纸面补图独立集期望和Cauchy证明。二者只需选择一条稳定实现，不并建两套图论平台。必须在同一个实际E上连接clique界、补图计数、γ及RS概率式。

一个可减少工程量的选择是移出Gram线性代数。纸面定义使用

$$r=\min\{v,\max\{k^2-k+1,\lfloor(v-1)/(k-1)\rfloor\}\},$$

其中min的v分支来自Gram秩界。但最终增长证明只需较弱的公共点二分界r₀=max{…}及r₀≤2√M。若直接证明这一上界即可接最终同一个B_RS+s结论，便不必先形式化关联矩阵和秩。若下一阶段还要求逐字复现含min的更强中间充分判据，则Gram分支仍须另证；不能删掉证明后继续声称已得到原较强中间函数。

### 再做全k≥17的参数控制

对一个被旧RS判据接受的整数M≥2^k，固定其**同一个**实际p见证，记d=2^(k−1)、κ=M/d、a=a_k(p)、J=J_k(p)。新增分析应按实际消费顺序证明：

1. 严格判据排除p=0；小p假设p≤1/k²下，用a≤kp和被积函数下界推出矛盾，从而p>1/k²。
2. 得J≥1/(2k²)、a^κ>1/k²、κ<2k以及κ log a>−2 log k。需要在真实域上处理J的区间单调性、幂界和log/rpow转换；本阶段的J≤p不足以代替这些下界。
3. 证明所需指数／对数增长比较，包括2^(k/2)>8k+4k log k和√M≥k²。先固定只为自然k≥17所需的接口；再比较自然数归纳与实变量单调性哪条在固定Mathlib中更短，不为了库定理名扩大范围。
4. 定义自然数s=⌊√M/[8(1+log k)]⌋，证明s≥1、s≤M、N=M+s≤2M，以及实际团预算r₀≤2√M。明确使用Nat.floor的域和转换，不混用整数floor或默认负数约定。
5. 在所有分母／对数参数已证正的真实域上，完成

   $$\log\frac{N^2(1-1/r₀)}{M(M-1)}
   \le\frac{2s+2}{M}-\frac1{r₀}
   <-\frac{2s\log k}{M}
   <\frac{s\log a}{d}.$$

   由此得到新增预算N的严格RS充分条件。最后还需将实际m≤N的概率项单调地压到预算式，接回所选最小反例并给原始输入染色。

其中的关键不是为每个k计算p或B_RS，而是从任意被接受M的见证p统一转换出新增s条边的判据。证明有限参数区间或若干数值点不能替代此统一接口。

### 最大预算及最终闭合

接受集合可直接取自然整数M≥1，条件为存在p∈[0,1]满足

$$\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}.$$

非空性用M₀=2^k、p=1/k作统一真实见证：一般Bernoulli／二项式估计给a_k(1/k)>1/2，J≤1/k，k≥17使4/k<1/4。本轮只有k=17的精确数值证明，需要补所有k的统一版本。

有限性由前述参数控制保证全部被接受且M≥2^k的预算满足M<k2^k；较小预算已经在有限区间内。然后用有限自然集合的最大值接口构造B_RS，并从最大值的集合成员资格取得一个实际p见证。这里最大的是整数预算，不是连续p上的函数值；无需另证连续优化器可达。可先在已证有限区间内用Finset定义，随后证明与纸面最大预算定义一致。

最后取M=B_RS，将同一p送入结构加强判据，在N=B_RS+s预算内排除全部原始反例，得最终下界。该连接必须以原始任意有限E为入口；不能把“存在一个满足完整新判据的证书”留为最终假设。

### 工程判断与建议

|模块|下一步最小验收|当前可判断的成本|
|---|---|---|
|商约化／点对覆盖|任意真实反例→更少点像超图→同一最小反例覆盖预算|数学路线固定；商映射和最小化接口仍需试编|
|实际单交图／团界／Turán|任意真实E的γ削减caller|数学自含；SimpleGraph表示及计数对接是首要API试点|
|一般参数／log／floor|任意k≥17和被接受M的统一增预算引理|分析链最长，尚无可信端到端编译样本，不能可靠估时|
|B_RS最大值|非空、有限、最大成员及实际p见证|依赖参数控制完成后再定具体表示；不需数值优化器|
|最终全域装配|原任意有限E→严格新判据→Bool两色见证|可复用本阶段概率核；仍须最终类型／公理审计和指定新编码审阅|

本轮局部编译墙钟包括Bernoulli12.05秒、OrderCounting41.97秒、PairProbability18.69秒、Lift7.82秒；这说明成熟接口的核验成本，并不测量下一阶段数学实现的开发时长。本阶段共享Mathlib依赖构建已完成，但尚无整个新结构链的实测，因此不提供完成百分比或总工期数字。

建议下一次先以“实际最小反例→公共点二分→真实γ削减→已核RS判据”的最短结构caller试点决定工程路线，尤其先验证能否直接用r₀绕过Gram。若这一连接顺畅，再实施一般参数与B_RS最大值的全链。完成全面Lean将增加已有一般纸面增长定理的内核级验收；扩大k范围或进一步改善下界是新的数学问题，二者不互相替代，也不自动并入本阶段。
