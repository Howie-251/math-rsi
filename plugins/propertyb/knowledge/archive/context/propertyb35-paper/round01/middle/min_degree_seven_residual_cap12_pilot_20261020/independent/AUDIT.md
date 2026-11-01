# residual cap12 pilot独立核验

**PASS_COMPLETE_SCOPED_INDEPENDENT_VERIFICATION。** 新36quad的完整22684标签、2901真D8代表及2633相关代表全部核对；2620严格证书和13个非严格best均原35索引重放相同。旧10^4的304份已核严格证书没有重跑；本次只核旧库存的tau/context接口，引用其中140个active项（136严格、4非严格）。语义审阅same-family/provisional。

## 实际覆盖

- 从13个实际完整lambda4谱的63个保存余键重新选择全部21 choose4实际degree多重集；同旧covered分类分开后，37个missing quad支持及source IDs完整相同。旧covered门是声明进口，不在本次重复审计其证明。
- 与primary inclusive生成不同，本次先精确枚举cross总数至少13、四个exact cross各不超过剩余paircap、两side exactpair至少一、至多一份triple，共800个高迹形状。全paircap4的inclusive预算t+2p+4q<=16且t>=13迫q=0,p<=1；因此该高迹域完整。
- 对每个实际quad的全部不同degree标签排列恢复singleton/empty，非负域逐键等于保存的22684标签。不是把一个degree排序当作固定侧向，也不要求H有自同构。
- 用swap01、swap23及交换两侧三个生成元BFS闭包，得到真8元D8；逐orbit互不交、并恰覆盖全部标签，代表逐键相同，共2901。没有用任意S4取代外边两侧的标记。
- 所有2633新active代表的已选旧固定位置均在原三菜单内，zero quota。每份展开35个不同原边索引，独立无放回下降阶乘注入重算1190有序不同边对、21个pivot，55293行总数一致。2620 strict，最大strict1101/1105；13失败完整保留，不把失败看作实际不可染反例。

## tau过滤的独立数学核

K内六个实际pair的tau成本先相加，记k。每个selected点i还有17个K外邻点，其共度总和精确为4d_i减去三份K内共度。令该和S，17个lambda在1…4时的最小成本由均衡凸性给h17(S)，与primary逐项DP不同。四个selected-to-exterior的pair域不交，且都不含K内pair，所以可将四行最小成本相加为e，得到tau>=k+e。

如果最高度D点按实际degree重数保证至少一个在K外，它的整行与K内六pair不交，却可能和上述selected-to-exterior部分重合。因此只能用tau>=k+max(e,max(0,4D-40))，不能把后两项直接相加。primary正是这个方向，本次独立重算每条的required_tau与active_contexts，全部一致。

筛选还引用已有高行G_D(tau)表：仅在G_D>=13的原保存key上需要c13局部gate。该已核通用表为声明进口，本次不冒充重新证明；其数值使用和所有63个实际context索引均独立核对。

## 准确成败边界

新13个非严格best以及旧4个相关非严格进口都保存在RESULT.json。新失败数按quad为(8,10,10,11):1、(9,9,10,11):2、(9,10,10,11):10。旧4项均quad10^4、保存界110833/109395，只引用不重放。

63个context的逐quad eligible数量、失败数量及完成状态与primary完全相同；49个context的全部missing-quad门均严格。这个context标志不独立宣称对应原H已染色，还须原共同moment/P及其他容量装配；不把49个context当49种实际H分类，也不把13谱全闭。

## 实际时间和产物

首profile quad为(8,8,8,12)，3库存独立重放0.023732 CPU秒，预计全体约20.83秒后继续；最终总CPU20.301257秒，低于60秒预算。域生成/过滤约1.67秒。没有新位置搜索、Lean或v2。

- VERIFY.py：完整独立程序。
- DOMAIN_CHECK.json：全部独立标签、D8、四外行及实际contexts。
- REPLAY.jsonl：每份新代表35个原迹索引及全部独立A/B/C行。
- RESULT.json：完整coverage、所有13新失败与4旧失败、63contexts及逐证书receipt。
- PROFILE.json：先行实际profile及预算估计。
