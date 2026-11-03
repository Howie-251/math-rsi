# pre-run：保留四arc，修唯一conjugate路线

实际C30冻结非邻pair0→5；根据字面controller预测其≤3路线恰word[0,2,1]，当前ARC在此只有rank2，覆盖4/8。它不能被同pair其它路线补足。原ARC三column maps A=[2,1,4],B=[1,2,7]、stepoffsets[1,2,4,7]。改B为[2,1,7]（B_repair=A*B_old），B_reverse同值，A不动、offsets四arc不动。B_repair仍involution且111↔e3，完整反向保持。

[0,2,1]满秩条件可左乘A化为{B e1,e3,e1}独立；B_repair e1=e2，因此预测P1该pair对全部8源坐标从4变8；P2 actualadjacent0→18仍8，且只靠pencil也全8。实际全部36约化三词只作这两个手选chart的结构对照，预测repair将四种A-conjugate词变满秩、其它原满秩词不损伤，计数从24/36变28/36；这不比旧已知28最优更高，不计新结果，不重搜197568输入。

同Bcase cap10，prior2.312243086+rootprep.1=2.412243086，worker8CPU。0新controller/完整图/BFS/solver/Lean/ARIS。通过仍不代表C30完整图D3、更不代表256图；下一是保留该chart的typedC30→C32明确插边族，不自动换field/group或扫chart。
