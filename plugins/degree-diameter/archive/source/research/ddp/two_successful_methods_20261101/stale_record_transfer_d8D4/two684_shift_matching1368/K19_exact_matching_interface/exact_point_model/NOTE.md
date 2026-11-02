# K19 36轨道 exactpoint 模型：单60秒窗口终态UNKNOWN

本批0新图。它严格大于旧H342等变的233928个闭合参数域，但仍不是任意684点matching域。36orbit×Z19表示绑定上层READ_GATE的实际law和label；任意sigma∈S36、36个独立shift，反向取bijection逆，不加involution。global目标K平移gauge合法，只把选中row0的t0固定0（648unit），没有固定sigma0。

## 实际生成，而非容量或旧DP

只转换保存的exact-length0..3旧H端点，用h_r*u左乘并按actual label分解；翻译10656条storedendpoints为5184个19bit masks，没有重新DP/sourceparse/BFS。A_EXACT_LENGTH0_3.u32与ORBIT_MAPPING/CACHE_CONVERSION保存坐标绑定。

C++从A做集合Minkowski，保存1679616个B(i,j;r,s)掩码，其中500256非零；BASE_COVER_MASKS.u32/MODEL_SCHEMA定义低19bit与索引。每个actual obligation(i,j,k)直接OR所有能覆盖该point的choice，不是walk计数：24624pointclauses，空clause0，每条长度1190..1202，coverliterals29499552。36出/36入各684选项恰一；Sinz共49176aux/147456AMO条，72ALO，加648gauge，总73800变量/172800子句/29844360总文字。CNF实际166236739bytes；没有Python巨型literal列表。

## 唯一实际求解返回

existing CaDiCaL实际argv是分离的“-t”“60”与本CNF路径，唯一一次；实际stdout为“c UNKNOWN”、无s状态行，exit0。132263 conflicts、338929 decisions、81741996 propagations、492 restarts；native实际60.041635 CPU。没有SAT模型或UNSAT结论，不判K19族NO。ordinarypoint模型虽精确，timecap没返回答案仍是UNKNOWN；不能用旧H域NO顶替。

因为没有SAT，独立原vars/sigma/shift/全部24624实际点union的正例分支没有进入；实际source literal parse0、684matching生成0、1368graph0、候选BFS0。run_once.py保存了正例分支：先由A重新Minkowski独立核union，再按原comments+无header边对parser读source一次，生成1368/5472，全1368roots BFS只是成功正例的新图验收，未在本轮运行。f9的conditional fresh码也不得在无候选时执行。

## 终态与费用

整个case继承readgate1.0，新prep1.0，converter.034366、compile1.044323、build.458167、native60.041635、parent约.019453，执行终态63.597950855；最后只读stdout/摘要保守.1，最终63.697950855/100CPU。构建远低于20CPU cap，compile/build/native均一次成功，没有格式/启动失败。RESULT/TERMINAL/NATIVE_EXECUTION/BUILD_RESULT与原始SAT_STDOUT完整保存，无prooflogging/check或hash。

停止当前窗口，不第二solve/seed/solver梯/继续旧timer，不自动转source/参数。K19 exactmatching是否可行仍UNKNOWN，本次可复用构造的是精确点模型与二进制路线数据，不能计作完整新图或数学族排除。原source D4验证、旧H233928重复、field/Lean/ARIS均0；0新增图/参数/Lean。
