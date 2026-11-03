# 事前预测：12相位排列能否同时过所有phase walk容量门

常数phase偏移已被328<567排除。令每个完整phase block按π双射，block内normal/fibre双射暂不限，跨matching仍一次cross。Q为已绑定13-neighbor循环相位矩阵，C(π)=sum_(a+b≤3)Q^a Pπ Q^b是真实普通walk数，distinct endpoints最多此数。每个root-phase到target-phase都有567targets，所以144项Cij≥567是必要条件，不是图D4的充分条件。

预测存在一个π满足全部144项；反驳需有受支持完整证据，单窗口无incumbent仍UNKNOWN。单个native HiGHS8秒／threads1／144binary permutation+24rowcol=1+144C≥567，objective0。可WLOGπ0=0只用Q circulant的输出平移symmetry。原constantphase charge.2＋新prep.5＋父子实际在总15CPU内，无旧source/BFS/field/Lean/ARIS，无warm/retry/secondsolver。任何π用独立直接整数求和重新核permutation及144容量，只记capacity witness、不生成13608图、不新参数计数。
