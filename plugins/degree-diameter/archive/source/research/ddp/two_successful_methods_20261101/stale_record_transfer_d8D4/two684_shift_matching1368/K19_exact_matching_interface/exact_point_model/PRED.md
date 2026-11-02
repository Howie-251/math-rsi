# K19 actual-point CNF，唯一窗口（pre-run）

继承上层READ_GATE实际law/labels与旧exact lengths0..3的H-typed endpoint cache。只以h_r=(epsilon,b)左乘缓存旧endpoint u，再分解为36orbit×Z19；不重新DP/sourceBFS/旧233928域。Orbit r=18tau+2b+epsilon，nu(r,k)=342tau+9(epsilon+2k)+b。

选择x(r,s,t)，r,s<36,t<19，变量1+((36r+s)19+t)，共24624。36个out groups、36个in groups各684选择且恰一；sigma任意S36，无involution或sigma0限制。global目标K平移postcompose经f9/gq独立paper确认，采用t_0=0 gauge：row0的t!=0共648unit，不固定sigma0。

B(i,j;r,s)=union_(a+b<=3)(A_a(i,r)+A_b(s,j))为19bit actualendpoint set。choice平移t覆盖rot19(B,t)，每(i,j,k)一个完整OR，共24624实际点义务。C++稀疏输出CNF，不用Python全literal对象；72组Sinz AMO，每组683aux/2048clauses，72ALO。预计总73800vars/172800clauses（含648gauge），约37.8mcoverlits/<=250MB；实际尺寸、空clauses、覆盖生成计数会落盘，不拿预计代实际。

可反驳预测：这个严格大于旧H域的K19 exactpoint模型可能有SAT matching。容量可行不代替actualpoints，RAW_UNSAT未checkproof不升级全族数学NO；timecap UNKNOWN不排族。

模型正常构建后唯一现成CaDiCaL argv['-t','60',CNF]、1CPU、无prooflogging/第二窗口/seed。SAT仅取原24624vars，独立整数核sigma/t与全部24624union（由A重新Minkowski而不是复查CNF）才生成graph。实际source是注释+无header边对，复用原parser契约，仅SAT时parse一次；保两684原图全部旧边+684matching边，1368/5472/all8regular。producer普通1368allrootBFS完整核并保存stats/首distance4witness，随后停交fresh；未独验前0新图/参数/Lean。

整个case100CPU含上轮readgate1.0、新prep1.0、cache转换/一次编译/build/parent/native。构建阶段cap20CPU，solver60，单worker；无安装/APIprobe/旧D4验证/field/Lean/ARIS。全部原始返回/失败都计费不reset，完成即STOP。
