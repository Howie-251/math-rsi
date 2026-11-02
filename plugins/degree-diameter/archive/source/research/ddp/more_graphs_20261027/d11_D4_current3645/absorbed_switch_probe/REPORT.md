# (11,4)单条paired-switch吸收：固定新类完整结束，0新图

本批只从上一批47个新root成功、旧旧失败的原型及其已保存firstbad pair生成一次新规则。35个合法现存switch组中，2组被必要见证界排除；其余679个固定free子集候选全部测试，0完整命中、0未试、0UNKNOWN。事前预测被反驳，已停止，不增加第二switch或跟随新badpair继续修改。

## 新生成规则

旧source仍为3645/20044、max11。对每个原始反例(r,t)，只在其中属于line/twin行1640..3443的端点y取其copyMate=y XOR1，并要求旧switch边(y,y XOR1)当前存在。没有扫描其它851条switch。

新删边集合F为原两条点–host边再加这一条switch。T′是全部不同端点，强制纳入新x的邻集，再从原7free中取最大允许的k=min(7,11−|T′|)点，按标签组合的字典序遍历。所有新邻集恰11点，没有更换free候选集合。

此时新图若成功应为3646/20052，而非上一两删边操作的20053。端点被删边重数计入实际degree；所有展开候选均max11，有2个degree10点、3644个degree11点。新增x自身degree11，不能沿用旧操作的正则性断言。

具体输入与顺序在[PREDICTION.json](PREDICTION.json)先冻结；实际完整生成族在[FROZEN_SWITCHES.json](FROZEN_SWITCHES.json)。47原型给出76个line/twin端点提议，其中41个copy-switch已不在当前source；余35组含32个六端点组、1个五端点组、2个四端点组。

## 原反例必要界与完整覆盖

每组先用宽松Smax=原11邻点∪switch两端判断

    2 + dist_G(r,Smax) + dist_G(t,Smax) <= 4.

旧反例在原扩张图中已没有≤4路径。额外删旧边不会产生不经过x的修复路径；任何新修复路径必须经过x，长度至少上述source距离之和。实际新S⊆Smax，所以不满足此界的整组子集全部不可能。所选y本身在Smax中，另一端只需区分距离0、1、2或>2，未重复source全距离计算。2个四端点组据此排除，对应2个最大free子集；其余33组生成32×21+7=679项。

对每项，全部F端点都属于S，故到S的source最短首次入S路径不使用F，仍有

    dist_(G−F)(v,S)=dist_G(v,S).

因此sourceR3(S)完整覆盖旧图精确等价于新root D4。旧旧点对采用A=closedR1_G(T′)：两端都在A外的旧≤4路径不可能使用F，因为经过任一删边至少2+1+2=5。故检查A的每个旧根及新x即可完整认证，理论至多73根，而非对称抽样。实际A有43–66个旧根；失败时遇首个确定旧反例就停止该候选。

## 实际结果

|指标|实测|
|---|---:|
|合法switch组 / 必要界排除组|35 / 2|
|必要界排除的最大free子集|2|
|实际生成并测试候选|679/679|
|新root R3失败|541|
|新root通过后旧旧D4失败|138|
|modified-root BFS总数|1677|
|单候选实际最多已执行根数|41|
|复用既有endpoint R3球|1964|
|新增R3球|29（7free单球+22个新switch端点）|
|native CPU秒|0.083762|
|含编译及新增缓存总CPU秒|2.744826601|
|导出图 / 未试 / UNKNOWN|0 / 0 / 0|

上一批只有7free的联合球，无法用于5点或6点子集，本批7个单球是新必需数据；旧1964球没有重算，原2673候选没有重跑。新增缓存仅13224字节，根顺序与完整性见[NEW_R3_CACHE.json](NEW_R3_CACHE.json)。

一个具体对照见[first_oldpair_witness.json](first_oldpair_witness.json)：新ordinal6来自原ordinal127、p=40，新邻集中同时含3352和2244，明确有修复路径3352–3645–2244；但旧点66到1863仍超过4步。它说明原反例的局部修复并不等于所有旧路线同时满足。没有为66/1863再选择第二switch。

[RESULT.json](RESULT.json)记录全部679项及第一失败旧对；[probe.cpp](probe.cpp)、[run.py](run.py)与[original47.txt](original47.txt)可复现有限范围。138个新root成功不是138张合法图，也不是某张图的普通无序坏对数；每个候选均有其自身的旧旧反例，确切全图D及全图坏对总数未测。

[terminal.json](terminal.json)已终态，pending为空，实际成功图n/D及普通无序坏对为null。源D4继承已有完整图，没有重做source全源验收。结论只关闭由原47个firstbad pair导出的一条现存copy-switch、指定三条删边和原free集合这项完整固定类；不排除其它3646点图或其它连接规则。
