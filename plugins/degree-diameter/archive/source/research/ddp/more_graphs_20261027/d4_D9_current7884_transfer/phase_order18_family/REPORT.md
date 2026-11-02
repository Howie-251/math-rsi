# p109阶十八phase族：四新轨道完整无解，旧轨道继承

没有新图。本轮固定p109、M36、六个primitive18 actions、C=(1,6)及D=(0,3)，只改变A/B的阶十八phase落点。四个新轨道代表的285144个设置全部完成，0完整survivor、0图/BFS、0UNKNOWN/未试；原正向预测被推翻。旧(10,14)轨道的71286项直接继承，不重跑。

## 源机制与为什么改变phase

原7884源是三点底图的regular metacyclic voltage lift。此前canonical多项式lift及旧phase(10,14)的全部自由A/B均失败，说明只修normal平移不足。因此本轮仍保留四个非平凡电压元素的阶18/18/6/12，但改变quotient中的phase落点，而非继续减少旧失败分数。

固定A/B的phase集合为

~~~
E={2,10,14,22,26,34}.
~~~

这恰为C36中阶十八元素的phase。A/B两个phase必须不同，所有无序phasepair共15对。

## 等价与继承边界

[ISOMORPHISM.json](ISOMORPHISM.json) 与 [PROOF_SCOPE.md](PROOF_SCOPE.md) 在参数搜索前确认：u∈{1,13,25}作用为

~~~
(i,j) -> (i,u*j mod36),  r_new=r^(u^-1 mod18).
~~~

它固定C的phase6与D的phase3，并置换六个primitive18 actions；排序无序phasepair时相应交换A/B，而全部A/B域保持不变。15个phasepair分成五个三元轨道。

| 规范phase代表 | 本轮处理 |
| --- | --- |
| (2,10) | 新算全部71286设置 |
| (2,14) | 新算全部71286设置 |
| (2,22) | 继承旧(10,14)完整排除 |
| (2,34) | 新算全部71286设置 |
| (10,22) | 新算全部71286设置 |

旧轨道为{(2,22),(10,14),(26,34)}。因此新计算285144、继承71286，共356430个规范设置覆盖全部五个orbit。若以原15个无序phasepair计，等价覆盖的域大小为1069290；后者不是本轮显式计算次数，更不是生成图数。

## 完整覆盖计算

[PREDICTION.json](PREDICTION.json) 在任何新设置求值前冻结至少一项完整成功的预测；forms导出任务的预测另存 [FORMS_PREDICTION.json](FORMS_PREDICTION.json)。二者保存分开，未重复任何已算设置。

四份ABF1输入包含24个actionframes、7776槽、2457436个generic coefficient triples。端点仍为ua*A+ub*B+uc mod109，包含全部≤9非回退词。不同forms数仅用于先查必要薄槽；必须全部324槽各覆盖109个域元素才接受。四frame最小forms数277/205/144/215均大于109，故本轮capacity预剪零，所有285144项均实际数值求值。

| 新phase代表 | 新设置 | 槽求值 |
| --- | ---: | ---: |
| (2,10) | 71286 | 75617 |
| (2,14) | 71286 | 71464 |
| (2,34) | 71286 | 71286 |
| (10,22) | 71286 | 71682 |
| 合计 | 285144 | 290049 |

每项在首个不满109的requiredslot拒绝即可排除D9，无需继续其余槽。没有完整survivor，因此实际邻接生成、三个轨道根BFS及边表导出均为零。没有保存最小坏对分数或以分数继续修补。

native合计0.479326CPU秒，编译1.047358CPU秒，整批1.536202CPU秒；forms生成另由互补任务用2.174545CPU秒。程序为 [search.cpp](search.cpp)、[run.py](run.py)，结果为 [RESULT.json](RESULT.json)、[terminal.json](terminal.json)，每frame详细cursor及action计数在frames子目录。

已闭范围仅为该p109/M36、固定C1与loop3、六个primitive18 actions、A/B不同阶十八phases及全部A/B值。设置不是图，actual_n、actual_D及普通无序坏对数均为null。其它prime、M、C0、不同phaseorder或一般11772点D9图不在结论内；本轮停止，不自动扩这些变化。
