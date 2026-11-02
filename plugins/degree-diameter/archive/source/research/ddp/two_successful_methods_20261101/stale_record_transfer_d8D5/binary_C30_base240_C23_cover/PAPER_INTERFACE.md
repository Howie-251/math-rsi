# Binary C30 base240 → ordinary C23 cover5520：有限容量接口

状态：**cover定义、逆电压、NB容量必要门及四系数归一化支持；没有搜索或生成。** 本文只使用本任务指定的已有合法C30/ARC二元base事实，不重做旧F5、Loz1100、source/field/BFS，也不枚NB words或cover参数。

## 1. 先固定实际 pointgraph，而非 controller 多值边

base H 是已有30-controller、F2³ fibre、240点的简单8正则 pointgraph。它是本次ordinary cover的输入，不是新的目标纪录；不在本文额外宣称它的直径。其每一条**有向实际 point-edge**有唯一 `(p,λ)`，`p∈{0,1,2,3}`、`λ∈{0,1}`，真实反向为 `(bar(p),λ)`，其中

`bar=[1,0,3,2]`。

这一 λ不变契约来自原ARC关系的完整 inverse：若 `y=M_p x+λv_p`，则 `M_bar M_p=I`、`M_bar v_p=v_bar` 给 `x=M_bar y+λv_bar`。后续输入必须使用已删除完整-label holding后的真实base边，不能把controller-stay或另一个noise选择当成原边的反向。

## 2. 唯一四系数 C23 电压规则

新点为 `(u,k)`，`u∈V(H)`、`k∈C23`。对有向base边 `(p,λ)` 定义

`θ_(0,λ)=cA+λdA`，`θ_(1,λ)=−cA−λdA`；

`θ_(2,λ)=cB+λdB`，`θ_(3,λ)=−cB−λdB`。

cover边是 `(u,k) — (v,k+θ_(p,λ))`。反向保留同λ且电压取负，所以这是合法无向ordinary cover，每个base edge在给定lift点只有一个lift邻点。base简单无loop保证lift也simple；所有参数下都保持8正则、5520点（是否连通/D5尚未保证）。

λ在电压公式中是**整数bit 0/1再取mod23**，不是假定F2→F23存在域同态。累积电压必须先按正负标签累加这些bit，不能先把λ和mod2再移到mod23。

5520=240×23；22×240=5280不超过本任务给定saved main5334，所以23是这个固定base下最小可能超过阈值的整数fold。这只是order比较，不是新下界、优先性或图存在性结论。

## 3. 第一门必须是 point-edge nonbacktracking words

ordinary cover的紧接反向**同一basepoint-edge**会严格原路返回：相反电压互消，两个step可删除而不改lift终点。反复删除可把任意长度≤5的lift walk投影化为长度≤5的base NB walk，且保留base/lift端点。

不能仅见 controller标签 `p,bar(p)` 就删除。若两步的λ不同，第二步未必是同一point-edge的反向；它可能到另一个base fibre点。正是此前controller有两个noise选择时不能删除的情形。

令 `N_(≤5)(u,v)` 为base H从u到v、长度0至5的全部NB walks数，包含u=v时的空walk，按实际paths计数，不是distinct point images。给定一个lift源 `(u,k)`，每条base path的lift唯一，最多贡献一个目标phase。因此若cover D≤5，必须

`N_(≤5)(u,v)≥23` 对所有ordered base pairs成立。

若任何一对计数≤22，则不只排本四系数C23规则，而是排此固定base的**所有fold≥23 ordinary graph covers**达到D≤5，包括任意permutation/其它voltage赋值；依据仅是path唯一lift与真正inverse-edge消去。这个结论不排具有多值liftstep或额外非投影边的controller关系模型。

若全pairs≥23，仅说明这项容量没有排除，不证明任何23-cover存在。特别要保留diagonal pairs；空walk只贡献一个phase，不能借“base起终点相同”跳过其它22个同base fibre目标。

## 4. 容量过后的一对 coefficient-form 门

对于某个实际base pair，按其保存的NB paths给每条path一个四维系数

`f_w=(#0−#1, Σ_(p0)λ−Σ_(p1)λ, #2−#3, Σ_(p2)λ−Σ_(p3)λ) mod23`。

总电压为 `f_w·(cA,dA,cB,dB)`。不同paths可能有同一个四系数向量，因而对全部参数永远给相同phase。故该pair若distinct forms少于23，可严格关闭**这个四系数family**；NB原始path数再大也不能修复。

若forms数≥23，仍只是必要条件：某个参数的实际phase values还可能碰撞；即使此pair全23，也没有保证其它pairs。同一个参数必须同时解决所有base ordered pairs，不能给每对各选参数。

## 5. Projective normalization 的准确域

参数 `c=(cA,dA,cB,dB)∈F23⁴` 共同乘以非零scalar μ，等于在每个base fibre上重标 `k↦μk`，是图同构。固定坐标顺序、把第一个非零系数归一为1，完整代表数是

`23³+23²+23+1=12720`。

全零参数给23份不相连的base，不能D5。**非零不等于连通**：某些非零电压仍可能是base上的coboundary，或有其它退化；12720是完整的scalar规范域，不是12720个连通/非同构图。这里没有进一步gauge或丢掉非零类，也没有授权参数搜索。

## 6. 最小数据及停止次序

仅需沿用这一个已有240点base的完整8邻接与每边 `(p,λ)` 标签、已绑定bar/inverse契约。第一新返回对象应为全ordered pairs的 `N_(≤5)` 最小值、实际最小pair及按长度计数（保空walk），并保存能复核该pair计数的路径/端口记录；不需要source D3/D4验证、旧field/rank或cover图。

若第一门失败，立即停，不搜12720类。若通过，先从同一次保存的路径数据对一个明确选定pair提取mod23 distinct coefficient forms及代表paths，不重跑base搜索。该单pair失败足以排四系数域；通过则回报必要门，交root重新评估，不能自动展开全参数或另一个m/field/base。

当前只是条件纸面接口，新base生成、NB枚举、forms处理、cover、BFS、solver、HTTP、Lean、外审均0；新增图/参数/纪录均0。
