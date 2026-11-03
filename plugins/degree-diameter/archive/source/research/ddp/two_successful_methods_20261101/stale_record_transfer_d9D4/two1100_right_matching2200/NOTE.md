# 两份Loz1100→2200：完整rightmatching域NO

本题是15格老题外的补充机会：8度1100源保两copy全部8800旧边，加1100匹配，条件参数2200/9900/degree9。当前主表1768；没有得到D4候选，不能计新图/纪录。

先预测P1：某相位的old-leg endpoint-pairs容量小于55；实际全部至少66，P1被推翻。随后完整1100个t按精确U_t=并_{a=0..3}B_a t B_(3-a)检验，没有fullU_t，P2被推翻。B3复用旧R4边界补集426，只生成B0/B1/B2，不重源D4/BFS。闭球四项式、onecross、同步leftH论证见PAPER_INTERFACE。

相对phase10的候选endpoint-pairs共66，但全部t真实端点最多43/55（首max参数t115=(2,5)）。因此每个t在该层至少12缺点，候选对映像重复至少23；这里66不是已去重的独立路线数。四个相位能局部满55也不能修复phase10的缺口。无需再优化总坏对或第二次后处理。

只排固定Loz1100源全部leftH等变rightmatching，不排非等变matching、改旧边或一般9D4。无2200图、候选BFS、Lean、ARIS。native0.795619759 CPU，含read/prep.8与root处置.1，case1.695619759/10。完成停止，不自动换S/source/参数梯。下一回到15格中的4D5，先读保存的364→365样本，问联合portmatching与star是否存在有根据的接口，不授权续随机样本/旧solver。
