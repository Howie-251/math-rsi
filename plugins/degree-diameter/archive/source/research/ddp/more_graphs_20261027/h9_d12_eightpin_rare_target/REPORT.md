# 两项8pin稀有目标前缀：有限窗口无命中

current42396，两项103/577 mandatory degree均合法。首anchor强制从最稀有遗漏目标的coverers中取≤32个，按稀有度组覆盖结构排序；second从最稀有残余目标coverers取≤16个，随后exact≤2尾。与旧overall覆盖top32不同。

pool103：mandatory缺125，最稀有target41932有2951个不同mask coverers；实际115个前缀、426240个thirdmask，search CPU5.003630秒，状态UNKNOWN_RARE_PREFIX_TIME_LIMIT。

pool577：mandatory缺145，最稀有target41925有3374个不同mask coverers；实际112个前缀、419230个thirdmask，search CPU5.015863秒，状态UNKNOWN_RARE_PREFIX_TIME_LIMIT。

总父＋全部native child CPU10.314221481秒，0命中、0新图、0MIP/seed/全源/外审，0重跑10pin池，delivery57保持不变。每项5CPU窗口先到，未穷尽所有选定前缀，更不能称4anchor不可行；只记录这次冻结有限规则的无命中结果。全部输出在RESULT.json与items/，到此停，不延时/扩前缀。
