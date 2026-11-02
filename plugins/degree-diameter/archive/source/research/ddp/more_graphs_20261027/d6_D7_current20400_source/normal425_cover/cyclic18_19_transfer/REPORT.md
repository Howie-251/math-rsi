# 正规425电压覆盖迁移：生成前被精确端点条件排除

本producer没有编译、生成图或运行BFS。真实source recipe已恢复，但预定m18/19两项在共享精确短词端点计算中均失败，因此按约没有再重复实际负图检查。后续有理论上界的完整m18..23判断也均失败，固定centered规则的全部更大模数至此关闭。

## 实际recipe及原生成预案

共享 [COVER_RECIPE.json](../COVER_RECIPE.json) 将原20400/61200源精确恢复为48点底图在N=F5²×C17上的regular voltage cover；全部122400个source darts已逐项MATCH，反向port一致。坐标为(base,i,j,k)，i,j mod5、k mod17，idx=i+5j+25k；每base六个dart带to,a,b,c17及reverse_port。原D7公开事实沿用，没有重验。

本任务原计划保留48底图与F5²坐标，将唯一的c17代表写为[-8,8]，分别模18、19，预期阶数21600、22800。不改变basis、section、整数代表选择或其它电压，也不假设原完整Aut延伸到新模数。新加法deck F5²×Cm本身即可给48个根轨道。

若有通过必要条件的m，producer应在实际新邻接检查simple、degree6、connected，先base0 identity R7，通过后再其余47个代表根。全部48通过才由deck平移提升为全图D≤7；exactD取48根实际偏心率最大值，不能由旧source D7直接继承。预案代码 [probe.cpp](probe.cpp)、[run.py](run.py) 已保存，但未编译或运行。

## 为什么没有启动实际新图

共享 [初次精确计算](../../centered_lift_quotient/RESULT.json) 的raw word最小容量66通过18/19必要数量筛；但同一次计算保存的整数标量端点集模m给出的实际R7 image已经反驳两项：

| m | 条件性阶数 | root0词端点R7缺项 | 一个缺项(base,a,b,c) |
| --- | ---: | ---: | --- |
| 18 | 21600 | 37 | (1,3,2,6) |
| 19 | 22800 | 68 | (1,0,2,5) |

这些是精确普通短路端点缺项，足以在生成前拒绝D7；不是raw词数不足、实际图直径或全图普通无序坏对。没有将21600/22800写成已生成的图。

对固定整数recipe，某requiredslot的完整整数标量端点集恰有23个元素，所以m>23统一不能覆盖m个标量。Root因此只授权检查由计算给出的完整有限剩余域18..23；[modulus_closure/RESULT.json](../../centered_lift_quotient/modulus_closure/RESULT.json) 已完成，18/19复用旧结果，20..23也各有root0缺项，admissible为空。

该结论严格覆盖同一basis、section、F5²电压及centered代表的全部m>17。它不排不同gauge、basis、其它整数代表或一般更大(6,7)图；本任务不继续这些变化。

## 终态

[PLAN.json](PLAN.json) 保留最初两项未执行预案；[RESULT.json](RESULT.json)、[terminal.json](terminal.json) 记录前提失败后的producer零执行。没有在已知负结果后补写“事前正向预测”；词端点任务自己的冻结预测与原始证据由其独立目录保留。

本producer实际候选数零、编译零、BFS零、source decode/Aut/normal恢复零；actual_n、actual_D及普通坏对均为null。原定10CPU实际构图窗没有消耗，没有额外验负图或新建独立方法条目。
