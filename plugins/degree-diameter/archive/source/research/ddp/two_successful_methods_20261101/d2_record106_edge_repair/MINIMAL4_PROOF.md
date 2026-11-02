# 最小4matching模型的完整forcing反例；不排一般107点改造

实际source106/582、degree10点T={34,54}及所有oldD2共邻事实均继承root的
SOURCE_RESULT.json，本门没有重读sourcebody、重做sourceprofile或BFS。
PRED先写，唯一数值过程读取已有criticalprofiles，实测约.004010CPU；
首次Python语法解析错误发生在任何计算前，修正后只执行一次数值检查。

## 该生成规则的精确覆盖义务

删4条不相交且不触T的旧边M，P=ends(M)，新增z106连接S=T∪P，|S|=10。
所有old最终degree11，zdegree10，总107/588。新z到oldv的必要充分条件是
N_{G−M}[S]=V。因M全部在S内，该闭覆盖等于N_G[S]。

oldpair若两端都在S，由newz自动提供commonneighbor。若一端v在S外，
v不可能是deletededge端点，其oldN完全不变。另一端u至多丢掉matching中
一条边uv0；若原来非邻的(u,v)失去全部commonneighbors，则原commonneighbor
必然唯一且为v0。这恰是root已保存的edge方向criticaltarget。原相邻pair若
被删就是M端点pair，已在S中。因此每deletededge的全部criticaltargets⊆S，
连同闭支配就是这个matching4规则的准确D2接口。可能有同时丢两个old共邻的
pair，但两端必都是P端点，newz已修复，故没有漏算联合损伤。

## 完整有限forcing证书

令C_e为saved required_if_both_endpoints_pin（含两个端点及两方向criticaltargets）。
若存在合法M，则其每条edge e不触T，且C_e∪T⊆S，故|C_e∪T|≤10。
在全部saved582个edge profiles中符合者恰21条，这给完整必要候选池E0。
记U为E0所有端点的并。本门实际检查：

    K={7,23,46,59}, K∩(T∪U)=empty;
    对每个e∈E0，C_e∩K非空。

MINIMAL4_FORCING_CERTIFICATE.json逐条列出21个edge、整个C_e以及强迫的
K点，另列完整U/T/K。对任何非空M⊆E0，选其任意edge e；它强迫某k∈K
必须属于S，但S=T∪ends(M)⊆T∪U，与上式矛盾。特别所有4matching都失败。
因此无需枚举C(21,4)=5985组合，更无需sourceBFS或图生成即可严格关此子域。
combinations_enumerated=0不是timeout或抽样；是短证书已经覆盖完整必要域。
未枚举的disjointmatching数量不被谎报为0。闭合候选数=0是证明结论。

这里不是Brown57/Brown91旧诱导不变界，也不是一般106→107无解。它只排
“4matching删边、无old-oldrepair、newz接全部10个释放pin”的最小模型。
source本身是公开重连成功得到的106图，D2补全方向没有被否定。没有新图、
参数或Lean计数，没有更改source/root/Wiki/冻结包。

## 下一具体改规则接口（尚未运行）

允许删5条matching M、不触T，加1条原来不存在的old-oldrepair edge xy，
再把其余10个释放点S=(T∪endsM)\{x,y}连接newz。仍净删4旧边，目标仍是
107/588、old全11/newz10。旧forcing中“criticaltarget必须作为pin”不再成立：
addedoldedge可以直接或通过一个旧中间点修复oldpair，即使target不邻z。

一个明确的anchor是：从上面21edge e=(a,b)取一个方向被迫K点k，使(a,k)
原来不相邻且其唯一oldcommonneighbor是b。新oldrepair选a-k；M包含a-b和
某k-l（给饱和k腾一槽），再选另外3条matchingedge。a/k的释放槽用于oldrepair，
二者不作为zpin。先只问H0=G−{a-b,k-l}+{a-k}中a和k是否已两步覆盖全部old106。
这是一条可推翻的必要anchor门：后续只删边，且a/k不接z，不能修复它们在H0
已遗漏的任何oldtarget。若anchor通过，再对其余三删边做精确oldbadpair⊆S×S
与N_H[S]=V检查。没有现在运行anchor或5matching搜索；root须另选这次改变规则。
失败不能扩大为所有old-oldrepair或一般N(11,2)107排除。
