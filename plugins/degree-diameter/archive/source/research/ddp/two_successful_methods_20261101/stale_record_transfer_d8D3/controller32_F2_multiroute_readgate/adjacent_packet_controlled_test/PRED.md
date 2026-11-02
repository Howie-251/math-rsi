# pre-run：实际C30一条边的双向合法binary路线对照

不是256图/C32候选，不重旧197568 charts或3750验证。冻结已有C30的0→18/p0，bar=[1,0,3,2]，用同一实际controller路线包（全部长度0..3，含controller backtracking）。只新测两个手工设计、真实反向约束相容的F2³ charts，目的检验低秩路线互补如何改变下一生成规则。

按vector code x0+2x1+4x2、矩阵以3个column code记录：A=swap(e1,e2)列[2,1,4]。ARC的B=I+110*e3ᵀ列[1,2,7]，stepoffsets[1,2,4,7]；COLLINEAR的B'=I+111*(1,0,1)列[6,2,3]，stepoffsets[1,2,4,3]。四maps分别A,A,B,B。这里v_p是实际forwardoffset，不是原F5的directions[p]；如用其API，directions[bar(p)]=v_p。

P0：两套chart都满足完整逆A_bar A_p=I与A_bar v_p=v_bar；对所有8个x/λ直接验证reverse-membership，不仅查方向身份。
P1：ARC三条packet p0,q,barq的rank2 images（q=0,2,3）有共同一维方向，在F2²商中三线互补，对全部8个源x并覆盖8个目标，而每条实际0→18路线仍rank<=2（无单一rank3）。
P2：改变为COLLINEAR仍完整可逆，但这三packet只并6点；实际整个0→18/≤3包预测并7点、不是8（x=0漏111=code7）。controller多一条三角形2步路可补其中一个缺点，却不补全。这是具体可推翻预测，不根据坏对数优化。

单新worker cap8 CPU，B同case cap10，prior/read1.6+input.3+paper/rootprep.4=2.3累计不清零。0图/BFS/solver/Lean/ARIS/新controller。即使全部局部预测支持，也不外推30*8完整图D3或32*8新图；下一必须解决对角/非邻路线与实际非Cayleycontroller输入。
