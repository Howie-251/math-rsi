# 任意反向一致 point-edge 电压：flow / gauge 接口

**纯纸面，未新增路径、参数或求解。** 沿用已绑定的简单8正则240点base及保存的66条8→70 NB paths。旧全pair NB容量非零已保证base连通；m=960。

**Flow是这里不可拆分的准确单位。** 给960条无向edge固定方向u<v，设电压θ_e∈F23，反向取−θ_e。路径w的signed edgeflow为 `f_w(e)=正向次数−反向次数`，其lift相位增量恰为 `f_w·θ`。同flow mod23的路径对任意此类电压永远相同；当前长度≤5，整数flow差的每坐标绝对值≤10，所以同mod23也就是同整数flow。不同flow可逐对分离（改一个差非零的edge），但不能据此假设所有路径相位能同时独立指定。这是**加法C23电压**的结论，不排任意S23 permutation cover。

**树gauge恰剩721变量。** 取base任意生成树T，重标每个fibre坐标 `k'=k+h(u)` 给

`θ'_(u,v)=θ_(u,v)+h(v)−h(u)`。

从一根逐树边选h，可将239条树边电压全置0，剩 `960−239=721` 个chord电压自由。此重标不改图或覆盖性质。同endpoint路径的flow差是cycle；若其chord部分全0，则是树上的cycle而必为0。因此这个gauge不把原本可区分的同pair flows错误合并。对固定pair，现只用其721维chord-flow `g_w`。

**下一必要门与一个构造性充分门。** 若保存packet的distinct g少于23，立即排此base上的全部ordinary **C23-voltage** covers达到D≤5；不只是旧四系数族。若不少于23仍未保证可覆盖。一个直接可实施的单packet构造是选w0及22条其它路径；若22行 `g_w−g_w0` 在F23上独立，则解

`(g_wi−g_w0)·t=i`，`i=1,…,22`。

秩22保证有解，free variables可置0；这23条路径的相位为 `g_w0·t+{0,…,22}`，故整个packet满23。此为条件线性构造，不是本次rank计算；rank不足**不**排覆盖（低维投影也可能有23个不同值），不得重复“每条路线单独满rank”的过强门。

**精确有限求解规则。** 对packet可直接设721个t变量、每条保存路径的 `z_w=g_w·t mod23`，约束 `对每a∈F23，OR_w(z_w=a)`；这精确描述该pair满覆盖，不把路径的z当独立变量。全D≤5必须对全部base pairs同时使用同一个t满足此式。单pair满足至多给一个合法电压候选，不能代替完整cover验收；其它pair的路径数据须另经授权准备，不能由这66条推断。旧66→26 forms及12720全NO仅是旧四系数约束的结果。

**反向与空walk。** 反向路径flow取负，故pair u→v满F23等价v→u满F23；可去掉互逆pair重复，但保留所有diagonal pairs。空walk flow0只给同base fibre的phase0，不覆盖其它22点。C23整体平移使每个base源只需lift phase0，但不同base源不能因电压已变自由而假定仍有旧controller对称。真正point-edge backtrack的flow0可消去；controller inverse但不同λ不能自动删除。

本paper未等待或计算EDGE_FLOW_RESULT，未改旧结果/目标计数。只读文件存在检查CPU0.000082777秒；图、BFS、field、Lean、solver、外审均0，后续选择由root决定。
