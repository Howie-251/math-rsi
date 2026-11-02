# 两饱和pin删除：29项有限前缀无命中

current42397/245877边，从原596个10pin中取恰2pin满degree12者，删这两点，得到29个不同8pin集合；全部冻结（少于32），无外部未选项。未重跑单删9pin/coreguard规则。

规则：首anchor必须覆盖最稀有corehole，按core/extra覆盖结构取最多16个；第二anchor必须覆盖首anchor遗留的全部coreholes，按extra互补取最多8个。每个选定核心修复pair之后exact≤2尾补extras，非单guard假设。最终接受仍要求actualdegree及native selectedfullR4。

29项全部访问，状态分布{'FINITE_TWO_CORE_PREFIX_NO_HIT': 29}。所选前缀耗尽29项，prepare未知0，前缀限时未知0，0新增，delivery58保持。每项选择的first前缀都没有找到能独自覆盖其剩余coreholes的second：实际核心修复pairs为0，exacttwo尾调用也为0。此次失败位于核心pair生成阶段，不能描述成extras尾部无解。操作性预测“本有限规则至少产1图”未中；first16/second8不是全部核心修复pair，不能判所有4anchors无解。

前10项2.708845CPU，总父＋全部child＋冻结5.928714208CPU秒，单项最大0.428980155<0.7秒。0MIP/seed/全源/互审/Lean，无第五anchor、更多删pin或追加候选。RESULT/items保存完整实际coreholes、前缀和尾部计数；到此停。
