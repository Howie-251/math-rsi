# (11,4)3645→3646：单cut释放端点，再加全部7个free pins

A线背景：actual3645有7个degree10 free vertices F={3456,3489,3564,3571,3583,3603,3643}，其余11度。旧source保边任意非空增广已严格NO，因F的sourceclosedR3仅2902、余743。原2673 paired-host双cut/679三cut族均已闭，不重跑；限定历史读取未定位本singlecut最大star全域终态，645 inserted-layer子域原为NOT_SELECTED。

新规则：删一个actual旧edge uv，新点z连P=F∪{u,v}，其它oldedges保留。端点与F重叠合法：|P|=9−|{u,v}∩F|≤9；满度端点失一补一，free endpoint失一补一仍10，其余free加一成11。该最大star支配同onecut/仅new-oldspokes的全部合法子star（可用端点只能来自P）。

具体预测：原201个插入点内部的645条edge中，至少一条的两端sourceR3能补齐F遗留的743 holes；这继承未执行的定向直觉，但本批完整测试所有20044个edges并按old-base/cross/inserted-layer分类。通过后仍可能旧路线受损，不预称oldold D4。

全部cutendpoints都在P，故d_(G−uv)(P,t)=d_G(P,t)，新根D4 iff 两端B3并覆盖旧holes743。先完整exact门；对passer在实际删边加星图检查全部旧根深4。若有旧pair失败，源D4与单cut用z替代都给新距≤5，因此深4失败+一条源4步路替换可保存精确4→5反例，无需重验源D4。若全pass保存实际3646边表，之后新图验收另做。

只解析一次既有sourceheader，复用endpoint1964与switch29根cache（重叠去重），只为缺的根补新问题用closedR3。F holes直接沿用cache，不重算F union/旧D4。保存所有20044结果、所补root数、最优holes缺口/类型、通过及oldold损伤。

单次native CPU10秒硬限、墙20s，全casecap15CPU（保守source历史read1.0、新read.5、prep.25另加实际编译/parent/native）。不solver/field/旧UNKNOWN/Lean/ARIS。无hit则STOP本singlecut族，不自动第二cut/repair或seed；不排一般3646/其它源/更广删改。

输入适配修订：两个旧cache分别用roots/new_roots标签；首准备读取KeyError发生在编译/新R3/数值之前，原尝试保留并保守计.1 CPU，不重置预算。按实际字段修正后继续同一批。
