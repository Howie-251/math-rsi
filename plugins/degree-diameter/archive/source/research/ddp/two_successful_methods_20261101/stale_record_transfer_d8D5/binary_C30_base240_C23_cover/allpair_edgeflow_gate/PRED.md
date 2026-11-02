# 独立逐边电压后的全pair必要门与同次witness失效诊断

前一步保存66paths的signed flows全不同，差rank65；已解显式电压让8→70全23phase。新增自由度真正修复原globalcoeff障碍，但未证明全图。

预测P1：全部ordered basepairs的不同signed edgeflows至少23；diagonal除空walk外按±成对。若任一pair不足23，排此base所有ordinary C23 antisymmetric edge-voltage赋值（不排一般permutation covers）。P2：此前21条非零边的局部电压会在其它pair失败，说明局部线性解不自动全局兼容，而非路线数不足。

唯一一次从实际240point arcs枚举NB≤5，不做base/source BFS，不续旧field或12720参数。只禁止紧接同point-edge反向；保空walk与diagonal。反向对称允许只存u≤v；v→u的flow集合为取负，满23等价。累计signed edge计数，抵消后做integer canonical flow；长度≤5系数差绝对值≤10<23，因此integer相等与mod23相等一致。

返回所有28920个unordered packets的NB数、distinctflow数、既有witness的phase并集；最紧packet、diagonal ±类数、零flow情况、首个失败liftpair及其所有phase证据。保存每packet distinct flow的有序二进制cache以便后续共享电压构造不重新枚词（每条记录u16 k，再5个i16 signededge，每packet按u≤v顺序；单edge重复代表系数，正向min→max）。没有重新逐pair BFS。

累计前case1.713051688，新增prep0.2，编译一次/原生一次CPU5秒硬限，同底图当前累计cap10CPU。若容量门通过且P2支持，只授权回看必要数据，不自动随机重启/全局优化；下一生成规则与预算由root按本结果决定。任何参数表/局部witness不计完整新图。
