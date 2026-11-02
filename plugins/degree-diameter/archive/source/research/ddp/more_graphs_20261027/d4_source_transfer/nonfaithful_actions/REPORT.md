# nonfaithful actions最后检验：薄层预测支持，完整D4仍无解

本次只检查此前未运行的11个非平凡、非primitive20的r，保持原四inversepair相位±1/±12/±11/±16。事前预测至少一个action能使phase10有幸存者；**8个容量通过actions中实际得到532个phase10幸存者，预测获支持**，但它们全部在其它phase0/1/2遇到失败，完整hit0。未生成图或运行BFS。

对每个r≠1，phase1的A经共同共轭归0，(B,C,D)按C1、C0/B1、B=C0/D1规范为3783项，11r总41613scope。全0不连通，直接排除。不同于旧primitive20，直接按每个数值r生成三变量线性端点forms，不错误使用Phi20；旧8个actions没有重跑。

| r | order | 最薄phase容量 | phase10容量 | 参数实算 | phase10幸存 |
|---:|---:|---:|---:|---:|---:|
| 3 | 10 | 111 | 111 | 3783 | 112 |
| 9 | 5 | 118 | 118 | 3783 | 30 |
| 11 | 4 | 50 | 66 | 0 | 未数值枚举 |
| 20 | 5 | 110 | 110 | 3783 | 16 |
| 27 | 10 | 111 | 111 | 3783 | 108 |
| 34 | 5 | 118 | 118 | 3783 | 30 |
| 41 | 10 | 111 | 111 | 3783 | 112 |
| 50 | 4 | 50 | 66 | 0 | 未数值枚举 |
| 52 | 10 | 111 | 111 | 3783 | 108 |
| 58 | 5 | 110 | 110 | 3783 | 16 |
| 60 | 2 | 19 | 19 | 0 | 容量可证0 |


3个actions共11349规范项被必要容量直接排除，其余8个actions的30264项完整枚举。**532只是在所有phase容量都通过的actions中得到的phase10幸存数**，不是全部11r的raw phase10总数：r11/50因其它phase容量50<61已不可能D4，未再数值查其phase10；该层的formal容量66不等于数值0。r60的phase10容量19则直接证明该层不可能。

order4仍有r10=−1、phase10全部自逆；orders2/5/10才有r10=1，不能统一写成所有nonfaithful都消除了对合。对于r10=1，phase10逆元将x映到−x，原primitive情形逆词落同一端点的折叠改变，确实允许修复旧薄层。例如r3、B5/C1/D5完整覆盖phase10，但phase1失败。532个幸存者按序查其它层，均在0/1/2首遇失败，不是声称19层逐一都跑完。

预测支持的含义是算术结构能修好这个单层；无完整命中则说明这些连接无法同时满足所有相位覆盖。它不是新图或新下界，phase10幸存数也不是全图坏对数。actualn/D/bad保持null。

容量CPU0.019798331秒，native0.005647秒，编译另计；单worker，预算内。结合旧8个primitive actions关闭，以及r1的abelian Lee sphere上界321<1220，可精确关闭**p61、这四个inversepair相位pattern的全部20个actions**。这不关闭其它phasepattern、两对合生成元组成或一般C61⋊C20图。

[PREDICTION.json](PREDICTION.json)、[CAPACITY.json](CAPACITY.json)、[ENUMERATION.json](ENUMERATION.json)、[RESULT.json](RESULT.json)保存完整实际范围。所有D4计算到此停止，不加phase、prime、seed、MIP或旧图重验。
