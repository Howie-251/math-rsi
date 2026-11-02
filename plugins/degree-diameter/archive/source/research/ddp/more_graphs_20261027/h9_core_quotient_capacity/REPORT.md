# 固定42342图只合并核心φ-pairs不能降到最大度11

冻结预测得到更强结果：原Dhar42342图的986个extras中，有672个当前degree12点，**全部672个的邻域都不含任何一个完整的可合并核心split φ-pair**。所以不论合并7959个允许pairs中的哪一子集、即使全部合并，这672个extra的degree仍恰为12。该固定source、只合并核心pairs、保留全部extras的路线不能直接给最大度11图。

## 一次实际必要筛

复用已有66430个original point→core映射 `point_to_core.u16.bin`，并从已有τ置换取φ=τ²。对p<φp且两者core像不同的generic fibers，得到7959个不同、互不相交的corepairs，覆盖15918个核心split点。没有重建几何坐标或关联图。

只读原 `deg12_diam5_n42342.txt`，不含新加的vertex42342及之后顶点。对extra labels41356..42341中每个degree12点，检查其完整当前邻域是否包含允许pair的两端。

| 项目 | 数量 |
|---|---:|
| 固定source n / m | 42342 / 245217 |
| 共同核心 / extras | 41356 / 986 |
| 允许的互不相交split corepairs | 7959 |
| degree12 extras | 672 |
| 含至少一个完整允许pair者 | 0 |
| 对任何允许quotient均degree12者 | 672 |

`RESULT.json`保存7959对的core与original labels，以及全部672条extra邻域、pair命中数和全合并后的degree。pair-count分布只有 `0:672`。

首见证为vertex41359，完整12邻集：

```text
4160 4557 4943 6087 6717 7374 40951 41394 41402 41496 42329 42330
```

其中任意两个邻点均不属于同一个可合并核心pair；其余非核心邻点按规则不允许合并。

## 严格结论和未外推处

设v为一个这样的extra。允许等价类仅为7959个互不相交corepairs中被选择的二元类，其余点各自单独成类。由于N(v)不含任何二元类的两端，quotient映射在N(v)上为单射；又v不参加合并，不会在v处生成loop。因此12条邻边仍通向12个不同邻类，degree恰保持12。这个论证同时覆盖所有2^7959个允许子集，无需枚举。

若合并r个pairs，阶数成为42342−r，quotient不会增加直径；但这并不能降低这里的672个degree12 extras，故无需MIP或继续找S/c。结论只关闭**这个固定42342图、core-pair-only、保留全部extras和quotient边**的降到Δ11入口。不排除删点、合并extras、其他等价类、改变原核心/边或其它Δ11构造；本次未研究这些操作。也没有将必要筛通过误当充分条件：若所有extras可降，仍需检查merged core的degree。

单worker CPU **0.155920494秒**，15秒预算内已完整结束；`pending=[]`。没有BFS、MIP、搜索、优化、图生成或哈希。冻结预测与复现程序为 `PREDICTION.json`、`check.py`；旧42343历史产物与同批42345扩张未修改。
