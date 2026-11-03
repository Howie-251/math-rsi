# 四个指定fieldmodule的D7族：2625个设置完整无命中

本轮没有新下界。q7、q8、q9的两个指定表示全部2625个projective设置完成；2625项均有六个不同非identity真正逆生成元，但只有2212项连通，所有连通项均未达D7。没有导出完整图、UNKNOWN或未试。q11/D8控制及其后续projective族另存独立目录，不计入本批。

## 真实source及合法群

继承 [实际H/source配方](../h48_complement/SOURCE_SEMIDIRECT_RECIPE.json)，其半直积规律已逐项MATCH原20400图全部122400个有向邻接。H=beta^u alpha^v，u mod3、v mod16，乘法为(u+(-1)^v u',v+v')；chi17=5^v。

source的正生成元H/C17部分固定为A:(c0,u0,v1)、B:(c1,u1,v12)、C:(c5,u2,v11)。A法向量固定零，B/C的两坐标自由。新群是

~~~
(Fq² × C17) ⋊ H48.
~~~

只有 [representation_tables/REPRESENTATIONS.json](representation_tables/REPRESENTATIONS.json) 明确VALID的四个指定表示进入执行。F8使用t³+t+1的bit编码，F9使用t²+1的base3编码；rho(beta^u alpha^v)=rho(beta)^u rho(alpha)^v。没有创建未证群，也没有重恢复Aut、H或旧sourceBFS。

三个负生成元从每组新正生成元按

~~~
(V,c,h)^-1=(-rho(h^-1)V,-chi(h^-1)c,h^-1)
~~~

重新计算，未独立嵌入旧F5负向量。随后检查六个实际group IDs不同且非identity。右乘为无向simple六正则Cayley关系；每项完整identity BFS同时检查连通与精确偏心率，左平移保证连通时这一根决定全图直径。

## 完整参数范围

Fq全局非零scalar乘法与所有Fq线性rho(h)交换，固定C17/H及A0，所以将四个B/C坐标规范成firstnonzero1不丢失固定族。全零不能生成Fq²，只在816 quotient component内，未作无谓BFS。

[PREDICTION.json](PREDICTION.json) 在任何新fieldgroup或设置执行前冻结。source控制由(0,2,0,4)写为centered(0,2,0,-1)，嵌入prime subfield后规范化，移到各固定域第一项，其余projective点按chart字典序各测一次。GF8中整数2映零，不把编码2误作整数2。

| 表示 | group阶数 | 设置 | 六生成元合法 | 连通 | 不连通 |
| --- | ---: | ---: | ---: | ---: | ---: |
| q7 | 39984 | 400 | 400 | 400 | 0 |
| q8 | 52224 | 585 | 585 | 192 | 393 |
| q9_plusg | 66096 | 820 | 820 | 810 | 10 |
| q9_minusg | 66096 | 820 | 820 | 810 | 10 |
| 合计 | 多阶数 | 2625 | 2625 | 2212 | 413 |

完整Cayley根BFS为2625次，接受D7零，edgefile零，未试/UNKNOWN零。它们是参数设置数，不是2625个新纪录或不同图的同构分类。

## 控制与度量范围

q7源控制连通，实际D8，故不是D7命中。q8控制仅访问3264点，component偏心率七；这不能当整个52224点图D7。其坐标都在F2，binary矩阵保持F2²，解释了不能假设连通。两个q9控制均连通、实际D9。

本轮不选最小坏对，也不作失败分数修边。逐项状态保存在 [cases.tsv](cases.tsv)，其中不连通项的ecc仅为identity component，不是wholegraph diameter。family顶层actual_n/D及普通无序坏对均为null。

native3.654880CPU秒，input准备0.007423、编译0.896225，整批4.561592CPU秒。结果为 [RESULT.json](RESULT.json)、[terminal.json](terminal.json)、[MODEL_BINDINGS.json](MODEL_BINDINGS.json)，实现为 [search.cpp](search.cpp)、[run.py](run.py)。

已闭仅为这四个VALID表示、固定H/C17生成元部分及A0的全部projective B/C向量。没有分类其它表示、q、H/c17选择或gauge；按约停止。后续独立目标(6,8)见 [q11_D8_control](q11_D8_control/REPORT.md) 与 [q11_D8_projective](q11_D8_projective/REPORT.md)，不混入2625计数。
