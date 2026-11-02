# 放开W后的必要count模型：上界832仍含不可实现的支撑形状

**一次新MIP最优值832，不能据此关闭retained4达到811。** 返回向量又在三个target的512个projection-support profiles中均无解，因此也不能把832当作实际packing。总0.355682674 CPU秒／20秒预算，solver0.103208585秒；一次call，随后只有无solver的小整数检验。

## 1. 这个新模型与此前point模型的区别

此前INFEASIBLE只涉及原固定W的1215个point变量。本模型不枚举729点，也不限制W、eta或center集合形状；只有15层counts w∈0..81、15个positive indicators y、15个large indicators z。固定31／59／60／72各81，其他不可用层为0。

原target总incoming≤81。令y iff w>0（w≤81y、w≥y），z iff w≥21（w≤20+61z、w≥21z）。每个实际三入射target加入

    sum(w)+8sum(y)≤97，sum(z)≤2。

三者都正时，第一条给sum≤73；有一个零时，原sum≤81更强，不误加三正限制。第二条给至少一项≤20。实际七个triple位于target9、12、19、29、32、48、77，均从controller与reverseport绑定到三个不同noise directions；其rank3继承已接受conic证书，不重验全部rank。64／71均保留。

45个integer／binary变量、152行，一次scipy.milp最大化324+sum(w)。返回HiGHS Optimal，22nodes、gap0，min-objective dual=-508.00000000000006，即total upper832；整数incumbent也832。精确整数代入所有声明行通过。该上界只属数值必要count模型，不是formal packing上界。

## 2. 实际最优向量仍不能生成

除ret4各81外，positive counts为

    16:30,17:12,30:50,32:50,35:31,42:30,43:51,
    44:50,45:50,58:31,61:31,71:11,73:51,74:30；64:0。

对每个三正triple，仅枚举已有几何推导的512个a,b,c∈1..8，并检查

\[A\le bc,\quad B\le a(9-c),\quad C\le(9-a)(9-b).\]

它们来自不同方向完整线族的一维投影互斥，即使family不为矩形也必须满足。没有新LP／MIP、field或几何projection验证。

|target|实际sources|counts|可用profile数|
|---:|---|---|---:|
|9|35,61,71|31,31,11|0|
|19|17,45,71|12,50,11|0|
|48|17,35,74|12,31,30|0|

其余四个triple含w64=0，不套只适用于三正family的512profile。这个具体832向量因此被新的必要支撑条件推翻，不能登记为center集合或图。

## 3. 一个比sum／min／product更具体的阻碍

Target9与48的乘积已超过8000；但target19的12×50×11=6600并未超过8000，sum=73且min=11也满足旧条件，仍无profile。

可直接解释：若A≥12、B≥50且C>0，则B≤8(9−c)迫c≤2；A≤8c迫c≥2，所以c=2。再由50≤7a迫a=8，由12≤2b迫b≥6。于是

\[C\le(9-a)(9-b)\le3,\]

排除C=11。这是同一个局部支撑模型中的精确形状相容性问题，不是把27改成邻近整数就能解决。该推导不依赖固定W，也不要求选择的line families本身是矩形。

## 4. 下一步判断与证据边界

本次没有证明ret4必须改变，也没有支持一个>810真实packing。它明确减少了不确定性：sum≤73与min≤20的粗cuts仍太弱，连加product≤8000也会漏掉target19这样的不相容形状。若要继续必要模型，应先表达完整projection-support相容性及多个target之间的共同center相关性，而不是盲扩大729点池或继续调相邻counts。

本任务只保存PRED、MODEL、WEIGHT_VECTOR、RESULT、TERMINAL及本NOTE。没有第二次solver、没有实现832或重试837、没有大图／BFS／Lean／旧wholelayeropt／全域point搜索。Ret4、其他pointsets和更精确必要模型的真实可行性仍开放，后续动作由root另行决定。
