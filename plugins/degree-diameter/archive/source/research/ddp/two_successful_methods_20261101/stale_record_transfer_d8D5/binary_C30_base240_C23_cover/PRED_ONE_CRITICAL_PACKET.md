# 固定binary240的最紧packet：先forms，再唯一四系数C23规范域

已有事实：同一base的240源NB≤5计数完成，最小pair 8→70有66条，按长3/4/5为1/10/55；全部pair容量≥23。仅容量通过，尚无5520图。

此前未知：66条实际路线有多少对全部四系数永远同电压？它们是否至少允许这一pair覆盖C23？

预测：该pair的distinct integer four-coefficient forms至少23；若支持，再预测至少一组共享电压能在这一pair得到全部23个phase。任一预测可由本批直接推翻。系数顺序(cA,dA,cB,dB)，每条实际point-edge按(p,λ)给±(1,λ,0,0)或±(0,0,1,λ)。先整数累加再mod23，不先mod2。

唯一输入TYPED_BASE_ARCS.json与BASE_RESULT.json。不再生成base或计算任何source验证/BFS，只从已保存标签枚举源8的NB≤5路径，保存到70的66条完整path与coeff/multiplicity。NB只禁止紧接实际同edge返回，不能按controller p/bar删不同λ路线。

若forms<23，严格关闭这一个固定base/四全局系数C23族，STOP；不枚参数。若forms≥23，授权对这一packet完整12720个非零projective代表（第一个非零系数1）做phase-union，保存每rep覆盖量及所有幸存者。全0给不连通copies可省。0幸存关闭仅此四系数族；有幸存只是该pair必要门，不是完整cover，不自动开展全pairs/另一base/field/fold。

预算：本samecase先前1.148210378 CPU，新增准备按0.15 CPU，native Python仅一遍，墙时15s/CPU3s硬限；samecase上限5 CPU。返回paths、forms、phase表或跳过原因、实际费用及scope。没有solver/Lean/ARIS/新完整target图，参数测试不得记为图数。
