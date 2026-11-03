# 两个phase10对合的新规则：容量通过，全部自由参数仍0幸存

这一规则与已闭四inversepair pattern清楚分开：保留±1/±4/±8三对，将原±9一对替换成两个不同phase10对合。固定p61、全部8个order20根r，度数仍8，假设n1220，对比L(8,4)=1100。没有主张整个C61⋊C20不可行。

对源乘法(i,x)(j,y)=(i+j,xr^j+y)，r10=−1，所以每个(10,t)自逆。共同共轭先把第一个t归0，再整体非零标量把两者之差归1，规范成h0=(10,0)、h1=(10,1)。剩余三对正phase1/4/8的translations A/B/C全部自由，合计8·61³=1815848参数。可能重复同构，不是1815848张已生成图。h0h1给非零translation，phase1投影生成C20，因此这些参数均保持简单8regular、连通的群图形式。

## 事前预测和实际门槛

预测明确为：至少一个case可覆盖旧薄层phase10的全部61点，不保证其它层。先精确枚举全部≤4 reducedwords（1/8/56/392/2744），20层形式容量最小85，phase10也为85，必要容量通过。

只profile首1000项一次。按其总native CPU投影并留3秒编译/准备余量，低于15CPU，才执行剩余1814848项；没有重放profile。全批实际完成，phase10 survivor **0**、完整hit0，预测被推翻。各action均查226981项；r8/23/24/28/33/37的单层最大58，r38/53最大59，全部<61。没有其它19层的检查需求，不能把这些数当全图坏对或D值。

profile和remainder native合计0.331709秒，容量计算0.005172605秒，编译/系数写入另计；单worker，预算内。没有生成图、BFS、旧source复验、MIP、外审或Lean。直接给phase10两条边虽改变了路线，却仍不足以让该固定pattern完成薄层；不以最大58/59当可续算的近似成绩。

完整数据见[RESULT.json](RESULT.json)、[CAPACITY.json](CAPACITY.json)、[PROFILE1000.json](PROFILE1000.json)、[REMAINDER.json](REMAINDER.json)；事前预测在[PREDICTION.json](PREDICTION.json)，native程序在[enumerate.cpp](enumerate.cpp)。仅关闭这个两对合+三inversepair相位模式，停止，不扩其他phases、prime或seed。
