# 一般RS概率核心与17元Lean试点

本阶段已完成一般真实RS失败概率界、原染色充分判据，以及任意有限简单17元、至多2^17边超图的完整Lean调用；三个最终导出已通过指定Lake构建，构建后的独立原命题caller与公理审计也已通过。证明从实际重染算法出发，将任意p的加权正关联、初始单色边平均、真实排列次序和精确积分接到原顶点集上的Bool染色。

**形式证明、本机独立审计与两家最终审阅均已完成（2026-10-21）。** 指定`lake build Aris4Math.General.RS.PilotMain`成功，构建后独立根审计`ReviewAuditGeneralRSPilot.lean`也exit0；七项传递公理均仅标准三项。Grok与Gemini均在一般RS概率界、原染色判据和17元调用的范围内认可结果，未发现实质问题。两家静态读取当前源码与已有日志，没有执行Lean。正式证据为`final-build.log`、`final-build-result.json`、`final-audit.log`、`final-audit-result.json`，完整审阅记录在`reviews/C/`。


## 阶段结果与最终接口

设E是任意有限简单k元超图的实际边集，m=|E|，γ(E)计**有向**恰交一点的原边对。置

\[
a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,\qquad d=2^{k-1}.
\]

三个已正式构建并审计的实际导出接口如下。

|导出|原始假设与结论|源码|
|---|---|---|
|`rs_recoloring_failure_le`|任意`[Finite V]`、`Uniform E k`、k≥2及0<p≤1；真实RS失败概率≤\(1-a_k(p)^{m/d}+\gamma(E)J_k(p)/d^2\)|`ProbabilityBound.lean`|
|`propertyB_of_rs_bound`|上述显式右侧严格小于1，即给原顶点集上的实际Bool染色，每条原边同时含两色|`ProbabilityBound.lean`|
|`propertyB_seventeen_of_at_most_two_pow : PilotTarget`|任意`[Finite V]`上的简单17元超图，边数≤2^17，具有Property B|`PilotMain.lean`|

通用判据保留的是用户可检验的数值充分条件；实际算法、失败覆盖、正关联、单交对概率和有限并界均已在证明依赖链内连接，相关外部前提已经消去。17元接口只留下原来的有限性、uniformity和边数假设，没有概率界、内部证书、点数、度数或点对覆盖前提。

17元数值调用取p=1/17。已核的精确有理数计算给a₁₇(p)>1/2，且J₁₇(p)≤1/17。m≤2^17使m/2^16≤2，故a的幂项大于1/4；实际γ(E)≤m²使积分项至多4/17<1/4。于是目标右侧严格小于1。该调用包括空边族。

## 一条真实概率链

样本由三部分组成：均匀初始Bool颜色、独立Bernoulli(p)资格位，以及均匀全顶点排列。`SampleLaw.sampleWeight_nonneg`和`sum_sampleWeight`显式证明这个联合样本的权重非负、总和为1，已导入正式主入口。`σ x`表示x的处理时刻，按时刻递增扫描。一个点仅在有资格、属于初态单色且至今没有点翻转的原边时翻转；每点只处理一次。

`Algorithm.failure_covered`把每个实际失败分到初态原色残留，或某个真实有向单交原边对和最终颜色。后一分支选最后由反色翻来的点；触发边当时尚未翻转，迫使两边恰交该点。初态全为反色而最终全换色的边也在同一分支内。

初态残留项由实际初始单色边族的共同hit事件控制。Bernoulli Harris适用于这些重叠边，均值与有限Jensen给第一项。这里没有把边事件当作独立事件。

对于指定单交边对和指定颜色，`PairProbability`从实际`PairEvent`证明精确概率

\[
\Pr(\text{PairEvent}_{f,g,q})=2^{1-2k}J_k(p).
\]

证明固定颜色和资格位后，剩余事件恰是活跃点A全在枢轴之前、活跃点B全在之后。`OrderCounting.beforeAfter_ratio`在实际全排列样本内给比例a!b!/(a+b+1)!，不要求活跃点占满全部顶点。`Integral.beta_nat`把该比例写为∫₀¹tᵃ(1−t)ᵇdt；有限期望与积分交换，再由坐标因子平均得到

\[
\int_0^1\frac p2\left(\frac{1+pt}{2}\right)^{k-1}
\left(\frac{1-pt}{2}\right)^{k-1}dt
=2^{1-2k}J_k(p).
\]

因此有限排列表示避免了连续随机过程的可测性和碰撞零概率工程，同时精确保留同一个积分。对两个颜色及实际`singlePairs E`求和，系数恰为γ(E)/d²；共同Sample上的并界再连接原失败事件。最后由失败概率小于1提取实际成功样本，并沿顶点等价把最终染色拉回原V。

## 已执行的局部验证

|范围|已核内容|证据目录／日志|
|---|---|---|
|算法|初始色触发、最后翻转点、完整失败覆盖、成功即原边两色|`algorithm-build.log`、`integration-first.log`|
|Bernoulli|归一化权、任意p Harris、多事件hit、有限Jensen|`bernoulli/build-final.log`、`bernoulli/audit.log`|
|初态平均|实际单色边均值、残留条件界／平均界，以及独立Algorithm.ResidualEvent caller|`initial-average/build05.log`、`initial-average/audit.log`|
|实际次序|任意活跃点的均匀相对次序与前／后块阶乘比例|`order-counting/BUILD.log`、`order-counting/CALLER.log`|
|精确积分|整数Beta积分、有限双和恒等式、J重标度与界|`integral/build06.log`、`integral/audit-final.log`|
|单交对概率|原始PairEvent的完整精确概率，非单交事件为零|`pair-probability/build-final.log`、`pair-probability/audit.log`|
|数值调用|p=1/17严格预算及实际γ(E)≤m² caller|`pilot-estimates/build03.log`、`pilot-estimates/audit.log`|
|有限顶点传递|原边、uniformity、边数、γ和染色沿等价传递|`lift/BUILD.log`、`lift/CALLER.log`|
|共同样本与有限并界|实际Sample、联合权归一化SampleLaw及UnionBound|`sample-direct.log`、`union-build.log`、`final-build.log`、`final-audit.log`|
|三个最终导出与原命题|一般P／C、PilotTarget及独立bare有限顶点／原边Bool见证caller|`assembly/PROBABILITY_BUILD.log`、`assembly/PILOT_BUILD.log`、`assembly/CALLER.log`|

正式根审计在实际构建后独立导入，复述裸`[Finite V]`、17元、≤131072边的原Bool两色结论及一般积分判据。七项被查导出和caller的传递公理均仅`propext`、`Classical.choice`、`Quot.sound`，无残留内部前提。以上属于本机独立导入和实际caller，不表示第二台机器复现。

固定环境为项目既有Lean4.24.0及Mathlib锁定版本。日志中的几项实际成本如下。局部项为source编译及olean生成；正式构建与根审计另列，不把它们解释为整个阶段开发时长。

|模块|墙钟秒|user CPU秒|日志|
|---|---:|---:|---|
|Bernoulli|12.05|3.61|`bernoulli/build-final.log`|
|OrderCounting|41.97|6.48|`order-counting/BUILD.log`|
|PairProbability|18.69|7.29|`pair-probability/build-final.log`|
|Lift|7.82|1.45|`lift/BUILD.log`|
|ProbabilityBound|7.97|4.12|`assembly/PROBABILITY_BUILD.log`|
|PilotMain|7.21|2.65|`assembly/PILOT_BUILD.log`|
|独立原命题caller|9.63|4.65|`assembly/CALLER.log`|
|正式PilotMain构建（既有缓存后）|18.58|29.54|`final-build.log`|
|构建后独立根审计|7.23|4.94|`final-audit.log`|

局部运行与项目统一管理的共享依赖构建有重叠；共享依赖构建已完成2527 jobs，随后正式PilotMain构建完成2538 jobs并由确认调用记录exit0。这些是Lake依赖任务计数，包含缓存／重放，不能解释为新模块数。各时长不能相加成整个阶段成本，也不能按源码规模推算下一阶段；未独立计时的模块不补填数字。

## 审阅和复现入口

命题表达、实际算法／概率接口及最终导出分别接受审阅；最终C覆盖本阶段的三个完整结果和构建／公理证据。

|最终审阅|实际返回|结论与执行范围|原回应|
|---|---|---|---|
|Grok|`grok-4.7-build`／`xhigh`，`end_turn`|在P／C／Pilot范围内认可；静态源码与日志审阅，未执行Lean|`reviews/C/GROK_RESPONSE.txt`|
|Gemini|`gemini-4-argon-high`／`high`，`SUCCESS`|在P／C／Pilot范围内SOUND／ACCEPTED；静态源码与日志审阅，未执行Lean|`reviews/C/GEMINI_RESPONSE.txt`|

Gemini的型号与effort来源为CLI选择记录（`cli_selected_model_variant`）。模型审阅用于检查语义、数学连接和验收范围；内核证明与本机实际执行证据独立保留。本次终审没有把一般k≥17增长整数增益定理升级为已Lean验证。

正式复现入口为`formal/Aris4Math/General/RS/PilotMain.lean`。在项目根执行下列命令；Lean4.24.0、`formal/lean-toolchain`及`formal/lake-manifest.json`固定既有依赖，不升级库，也不以旧默认Main的构建代替本模块。

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.General.RS.PilotMain
lake env lean ReviewAuditGeneralRSPilot.lean
```

正式Lake确认与独立根审计均记录exit0。根审计已从裸`[Finite V]`及原始Finset边集复述17元Bool染色、一般积分判据，并打印实际导出、定义与传递公理；源码为`formal/ReviewAuditGeneralRSPilot.lean`，日志为`final-audit.log`。

后续完整增长定理的准确剩余与建议见[FUTURE_FORMALIZATION.md](FUTURE_FORMALIZATION.md)。该阶段不自动启动，不恢复旧35／36研究。
