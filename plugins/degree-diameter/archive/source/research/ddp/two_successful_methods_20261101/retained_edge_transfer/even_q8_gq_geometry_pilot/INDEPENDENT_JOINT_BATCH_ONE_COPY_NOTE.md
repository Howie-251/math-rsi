# 独立攻击结论：一轮full-product复制后的任意helper批次障碍

**预测在声明范围内成立。** 未找到遗漏短路线；下列纸面证明给出必要条件。一次有界toy穷举亦无反例，含汇总共0.522388157 CPU秒／15秒预算。该结论只关闭不可变一轮完整复制、固定cap、仅从现有自由pin接入任意有限新helper批次的局部扩张，不是全图阶数上界或新图纪录。

## 1. 实际需要的结构，及唯一ownership的来源

记源为δ正则图，C=O×spread，|C|=R²。对o_i令σ(i)为其spreadowner，并令τ为σ的逆置换。中心c=(o_i,S_j)的唯一中心邻居候选为

\[T(c)=(o_{\tau(j)},S_{\sigma(i)}).\]

当j=σ(i)时是被删除的selfloop，对应D；否则T是C_off上的无固定点对合，C_off诱导perfect matching。所有中心的open Nδ两两不交；D点到任意其他center没有1／2步路线。这些均是此前owner／incidence机制的性质，本次没有重跑域或小几何。

给每个center恰好一个clone x_c，且只连不可变的原N(c)。在cap Δ=δ+1下，每个旧非D点已饱和；D与每个clone都恰好剩一个degree。任何新helper只能接D或clones。尤其每个x_c至多接一个新helper：若同时接两个，degree会超过Δ。因此off-diagonal clone的owner是唯一helper或unused。这不是对新helper之间是否相邻的假设。

## 2. 到旧off-diagonal center的所有≤3步路线

固定新helper h和旧center c∈C_off。c已经饱和，所以不存在helper–c边。h的第一步只能到一个旧自由pin，或到另一新helper。

- 若第一步到旧D点d，剩余两步不能到c，因为d到c没有1／2步旧路线。d不会邻接任何现有clone；若下一步到新helper，最后一步仍不能接饱和的c。
- 若第一步到clone x_e，两步路h–x_e–c只有e=T(c)。三步经旧source顶点u到c，要求u∈N(e)∩N(c)，由openN不交强迫e=c；此时确有h–x_c–u–c。这个分类同时排除了diagonal clone的帮助。
- 若第一步到新helper g，只有再接x_T(c)才能在第三步到c。g接D也不能到c；若第二个内点还是helper，其最后一步又被c饱和排除。

现有clones之间没有边。经一个旧freepin在不同helper之间绕行也不能在三步内结束于饱和c。旧source中的fill点已经包含在N集合及D的短路线排除中，不能漏作额外自由点。

因此准确的中心覆盖条件是

\[\operatorname{owner}(c)=h\quad\text{或}\quad
\operatorname{owner}(T(c))\in N_B[h],\]

其中B是任意内部helper图，N_B[h]含h自身。第一项给三步，第二项分别给两步或三步。这里只要求helper能到所有旧C_off center，是完整D3的必要条件，尚非充分条件。

## 3. Unused与inactive helper均不能绕过计数

设t=|B|≥2。若x_c未使用，那么对每个helper h覆盖目标T(c)时，第二项不存在，只能要求owner(T(c))=h。这将同一个x_T(c)分给至少两个helper，违反唯一ownership。因此全部M=R(R−1)个off-diagonal clones都已分配，记a_h为h的分配数，Σa_h=M。

取有至少一个pin的h，设它拥有x_c。任意g≠h若不拥有x_T(c)，为了覆盖T(c)，必须与h在B中相邻。因此h最多能省去与owner(T(c))的那一条边：

\[\deg_B(h)\ge t-2.\]

若partner也归h，实际上要求t−1，不会削弱下界。无off-diagonal pin的inactive helpers仍必须被这些active owners服务，必须计入t，不能只数active helpers。

其他D或diagonal clone pins只会进一步消耗helper degree，所以

\[a_h\le\Delta-\deg_B(h)\le\Delta-t+2.\]

M>0保证至少一个active owner；若右边非正则直接矛盾。否则对至多t个owners求和得到

\[M\le t(\Delta+2-t)\le
\left\lfloor\frac{(\Delta+2)^2}{4}\right\rfloor.\]

这证明覆盖任意有限t≥2。t=1由此前单helper的R²下界处理，不能把本段的unused论证无条件套在t=1。

## 4. 一次有限实验实际检验了什么

固定标准matching T(c)=c xor1。对M∈{2,4,6}、t∈{2,3,4}，枚举全部simple内部helper图与全部owner取值{-1,0,…,t−1}^M，包含unused。每个配置先检验所有helper／center的上述准确覆盖条件，再计算实际最小helper cap=max_h(a_h+deg_B(h))，检查unused排除、active degree、抛物线及全局二次界。

共实际访问1078182个配置，7250个满足中心覆盖。未出现任何unused-valid配置或下界反例。全部九个有限范围的计数与cap分布保存在INDEPENDENT_JOINT_BATCH_ONE_COPY_RESULT.json。穷举只核抽象有限必要条件，不能替代第2节对完整图路线的纸面分类。

另给sharp中心路线toy：t=4，每helper拥有a=3个clone，M=12，T把owner组0／1和2／3配对。令内部B为K4删去这两条组配对边，内部degree2，总helper degreeΔ=5。此时全部48个helper／center都有显式≤3步路线：12条own-clone、12条own-partner、24条neighbor-helper-partner路线；每条边和长度均逐项检验。得到

\[M=12=4(5+2-4)=\lfloor49/4\rfloor.\]

这说明仅靠此中心路线必要条件，二次上界能够取等。辅助route图不声称具有q8源的全正则、完整D3或其他全点对性质。没有生成q8 one-copy图，没有oldgraph BFS或任何新Lean。

## 5. 对两个q8机制的结论与下一生成决策

|源|R|δ|one-copy cap Δ|M=R(R−1)|必要上界|
|---|---:|---:|---:|---:|---:|
|balanced q8|65|81|82|4160|1764|
|Payne q8|64|80|81|4032|1722|

两者均严格超过必要上界，因此t≥2任意有限helper批次都不可能；t=1也分别需4225／4096 pins而cap不足。结论允许批次内任意边，没有把helpers强行设为独立集。

它关闭的只是“先完成每center一copy的full-product饱和，再在同cap下追加只接freepins的jointbatch”这个机制。现有q8源已数学验收，one-copy大图本次未生成；这是对该声明扩张结构的局部定理，不新增完整图或record。

因此下一代不应再给这个固定scope派joint-helper搜索。若继续同A线，必须实质改变饱和发生的位置或连接规则，例如在饱和前联合生成、改变初始center code，或选新的cap；这里没有启动这些动作。k≥2时clone不再只有一个spare slot，唯一owner论证会失效，不能把本结论自动外推。改旧边、不同code、提高cap与其他参数也都未被排除。

PRED先于唯一toy执行；RESULT／TERMINAL及48条显式route CSV已保存。全部进程终态、无续timer。旧SATURATION单helper文档及root状态均未修改。
