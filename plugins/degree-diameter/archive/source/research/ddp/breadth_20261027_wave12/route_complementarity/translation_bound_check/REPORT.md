# bestID68 的0→10槽：独立平移也只能覆盖12/16

可推翻预测P1在一个真实槽上被支持：保存best1152（ID68）的base0→10，全部长度≤4控制walk仅有AACA=0020与DCC=322。两条路线像为方向不同的rank3超平面，因此即使让两条路线分别任意平移，其并也恒为12点，至少漏4点。这组固定maps/vectors不能仅靠两个global offsets修好；允许144条边各自的offset仍不能修好同一槽。没有分析其他1023个输入，也没有搜索offset。

## 独立重算，而非只复述rank摘要

[check_actual_slot.py](check_actual_slot.py) 直接读取 [best_parameters.json](../../../breadth_20261027_wave11/binary72_tight_words/best_parameters.json) 的原72控制图及ID68四个maps/vectors。只从base0枚举全部341条长度0..4控制walk，包含立即回退，确认到base10恰有这两条；随后直接逐步模拟每个binary branch赋值重算image，没有使用source_scout的rank算法。

| 路线 | 长度 | 逐branch重算列 | image | 法向量 |
|---|---:|---|---|---:|
| AACA/0020 | 4 | [14,9,7,1] | [0,1,6,7,8,9,14,15] | 6 |
| DCC/322 | 3 | [2,15,11] | [0,2,4,6,9,11,13,15] | 9 |

向量用四位整数、最低位为x0；两像分别为H6={x:x1+x2=0}、H9={x:x0+x3=0}。image及列与source_scout保存结果逐项一致，见 [ACTUAL_SLOT_CHECK.json](ACTUAL_SLOT_CHECK.json)。

## 精确coset DP与逐源fiber的结论

独立DP为每个H列出两个不同cosets，对覆盖mask取OR。状态数为[1,2,4]，共6次OR尝试，最大popcount为12。四种不同coset配对的交集大小全部4、并集大小全部12；达到上界的一个平移代表是[0,0]，其缺点为[3,5,10,12]。

这也有直接纸面证明：6和9是F2上两个独立非零法向量，所以任意两个affine hyperplane的方程不论右端是什么，都有4个共同解。故union=8+8−4=12。对任一源fiber状态x，路线终点形如M_i*x+c_i+H_i，只改变平移、不改变法向；相同结论对全部16个x成立。

程序还只对该base槽的全部16个源x逐branch模拟原offset0路线，确认每个实际union都为12、各漏4点。任意offset时至少4miss/源的结论来自上述独立平移上界，不是从零offset试验外推。于是两个base fibers0和10之间至少存在16×4=64个无序距离>4点对。这是固定maps/vectors下的条件性理论计数，不是新做全图BFS所得的ordinary坏对总数。

## 同一控制槽的F3成功对照

原成功F3^4的 [controller_routes.json](../../../breadth_20261027_wave5/mizuno_d4_source/controller_routes.json) 对同一0→10槽直接指定full-rank AACA：一条路线便覆盖全部81点。该槽在F2 best中有两条路线，仍因方向不互补而失败。因此“真实route数增加”或“唯一四路26词已全rank4”都不能预测一般槽的联合覆盖；AACA不因该槽而属于唯一route必要条件，必须额外看其实际image。

另一种成功互补机制见root已核对的 [F3首pencil0→1](../ternary_success_fixture.json)：四个27点超平面，共同core9，联合81，且全部81个源fiber状态均覆盖。它与本槽的“仅两张异向F2超平面”具有可辨别的覆盖结构差异，不是只比较坏对数。

## 对下一次maps/offset选择的具体影响

当前ID68的线性部分已在此槽被排除，下一步不应做offset搜索。改变线性部分时，这个二route槽有两个明确方向：让AACA升到rank4；或让两个rank3像成为同一hyperplane，才有机会用互补cosets覆盖16。

即使第二种方向达到“平行”，独立平移可行仍不是consistent offsets存在。若两像同为H=ker(n)，全源fiber覆盖的精确条件为

    n(M_1+M_2)=0，且 n(c_1+c_2)=1。

因为两个affine hyperplane要对所有x互补，其右端之差必须恒为1。这给下一次可冻结检验的drift一致性预测，而不是自动启动偏移优化。本报告不声称有任何新线性输入满足这两式。

方法及5个合成fixture见 [METHOD.md](METHOD.md)、[FIXTURES.json](FIXTURES.json)，精确最大值为16、12、16、63、81。实际槽核对CPU0.00141秒；没有图BFS、其他slot/候选枚举、offset搜索或新图。本任务所需单槽攻击已完成。
