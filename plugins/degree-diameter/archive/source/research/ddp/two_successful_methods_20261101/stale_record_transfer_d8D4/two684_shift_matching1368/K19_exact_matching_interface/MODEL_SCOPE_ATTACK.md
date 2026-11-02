# K19 exact-point matching model：纸面反例攻击与条件fresh入口

本文件核对符号模型及准备独立验收入口。只读本案READ_GATE、旧实际recipe和已保存H-endpoint schema；不读取源边表，不重算old DP、orbit表或覆盖集合，不运行BFS/solver/Lean/外审。随后只读数值owner已实际落盘的 convert_cache.py、build_model.cpp 及run_once.py的SAT decode/positive branch；没有读取巨大CNF、运行或复算其数据。

## 左乘旧cache必须保持正确次序

源边是h*s，H law为 `(a,b)(c,d)=(a+23^b*c mod38,b+d mod9)`。对新orbit代表h_r=(epsilon,b)，将旧从(e,tau)出发的typed endpoint u=(u_a,u_b)搬到此代表时，必须使用

`h_r*u=(epsilon+23^b*u_a mod38,b+u_b mod9)`。

不能改成u*h_r。随后按源label `342*rho+9*a+b` 分解为实际K轨道及坐标。这个过程用旧source的完整H左对称搬动旧leg；它不宣称新matching仍H等变。

以36轨道坐标 nu(r,k) 为准，oldleg集合A_ij^(a)表示从(i,0)到(j,k)的恰a步endpoint k。保存≤3的exact长度分别取a,b≥0、a+b≤3；若用累积≤长度集合也应在union层解释，不能把不同root/type合并。位集有效域只有低19位，且必须包含a=0的identity endpoint。

## 36roots与24,624项point义务完整

候选matching为 `M(r,k)=(sigma(r),k+t_r)`。其反向是 `M^-1(s,k)=(sigma^-1(s),k−t_sigma^-1(s))`；不要求sigma²=id或相应shifts互为相反。所有旧边及M都与共同K左作用交换。因此任意起点(r,k0)可归到(r,0)，目标的相对K坐标减k0；36root-orbits不能再按旧H缩成2个。

对每(i,j,k)∈36×36×Z19，selected choice(r→s,t)提供≤4路线，恰当且仅当

`k in union_(a+b<=3) (A_ir^(a)+t+A_sj^(b)) mod19`。

这从prefix到(r,x)、cross到(s,x+t)、suffix再加y逐点得到，是真实endpoint集合，不是walk数量或容量上界。单个choice对同一义务可有多个route，但CNF的OR应按choice ID去重，不能将多路线计为不同selected变量。

跨层≤4路线若含3cross，至多1oldstep，两cross间必有一处连续matching往返，可消成一次cross。故上述义务没有遗漏多cross捷径。全部forward-copy的36²*19=24624义务也覆盖reverse距离，因为图无向。保留两份源内部旧D4后，这些精确cross义务才构成本域的充分且必要覆盖模型。

## One-hot与唯一允许gauge

每(r,s,t)一个binary，变量数24624。36条源orbit恰选一次，36条目标orbit恰入一次，给出完整K-equivariant bijection。不能仅要求rowone-hot而让多个源orbit指向同一目标，也不能加入sigma(0)=0作为无依据WLOG。

`t_0=0`则有真实图同构依据：对copy1全部目标施同一个K左平移delta，其旧source边保持，matching shifts全部变为t_r+delta，orbit permutation sigma不变。取delta=−t_0即可。它不是“只移动目标orbit0”，也不固定sigma0。若choice ID为 `1+((r*36+s)*19+t)`，可禁止r=0且t!=0的36*18=648个choices；row0仍能选任一target orbit。这比此前6804容量-only的outputphase gauge更强：此处K确为实际oldsource automorphism。

## SAT/UNKNOWN与数据绑定边界

SAT必须解码实际36个matching choices，直接检查source/target one-hot、t0 gauge及全部24624point义务；辅助变量不能当matching choices。只有完成这项整数绑定，才有确定的K-equivariant matching函数及可生产的1368点候选；rawSAT字符串本身不是graph acceptance。

完整模型rawUNSAT仅关闭此fixedhost/K19-equivariant域，不能外推arbitrarymatching或其他源。timeout、无assignment、或构模不全均是UNKNOWN；本note不追加第二solverwindow。所有原source度数/D4和旧H全域NO均继承，不重跑。

## 已准备但未执行的独立literal验收

入口为 `independent_acceptance/verify_candidate.py`。它不import producer、SAT、CNF或endpoint masks。未来只有root看见actualSAT、完整1368/5472文件并另给freshbudget后才运行：

- accepted684source和candidate各读取一次，核两份induced source完全相等，共保4788旧边；
- cross恰684条perfectmatching、全部1368点simple8regular；
- 从literalmatching直接还原36orbit/19点shift，独立核K-equivariance；
- 对实际candidate全部1368root做ordinaryBFS，记全部1,871,424orderedpairs及真实distance4路径；失败/预算截止明确剩余未测根。

不会对原source另跑D4/allroots，亦不借producer的representative结果代替fresh全图。当前只做Python AST语法解析，0source/candidate读取、0BFS、0数学PASS；PREPARATION_RESULT.json明确conditional-not-run。

## 已落盘代码的只读绑定结论

数值owner代码位于 `exact_point_model/`。converter确实以 `eps+23^b*ua`、`b+ub` 左乘h_r*u，再以normal奇偶/半值生成K坐标；A0断言对应identity。C++的B(i,j;r,s)是所有a+b≤3的A_ir^a与A_sj^b的19循环Minkowski并。目标k子句对每q∈B加入t=k−q的choice，恰等价于k∈rotate(B,t)，未把walk数当coverage。

72个684-choice exact-one组使用ALO加Sinz链：每组683个aux、2048条AMO；故49176aux、147456AMO加72ALO，加24624pointclauses与648gauge units，合73800vars/172800clauses，与代码声明一致。gauge只禁止sourceorbit0的nonzero shifts，未固定sigma0。

SAT正例分支只解码原24624choices，核36source/target各一次与t0=0，并从A重新算point unions（不依赖CNF或预存B）；literalmatching的nu函数也与actualsource labels一致。未发现这些关键语义的实际遗漏。这个结论是只读代码检查，不是本note运行过SAT、验证过某个assignment或完成过graph验收。数值window状态仍以唯一owner实际终态为准，不代其poll/重启。
