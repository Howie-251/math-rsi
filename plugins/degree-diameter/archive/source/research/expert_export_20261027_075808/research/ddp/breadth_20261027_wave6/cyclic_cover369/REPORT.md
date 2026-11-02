# Allwright41(1a) 的 C9 普通覆盖：容量不足，未启动搜索

本轮固定选择维护者页面列出的 Allwright Graph1(a)，不是其他41点图。定向检索项目未发现同一底图/C9/369点profile；本地名为 `candidate_41.edges` 的文件实际有425点，不能当作41点来源。

已浏览 [维护者D3原始说明页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)，从其 [Graph1(a) 原始NX邻接表](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/deg4D3-41_1a_allwr_adjlist.txt) 下载。原表把无向边只列一次，已据此对称化。实际得到41点82边，min degree=max degree=4，无自环、无重边；不是默认假定四正则。此前registry标记该底图尚未本地核验，所以只做了一次小规模41根普通BFS，确认连通、D3，CPU0.0011秒；以后可复用 `base41_check.json`。

若C9-cover成功，顶点为 `(v,i), i∈Z9`，基边u<v赋电压z_e，连 `(u,i)~(v,i+z_e)`。其阶数369、度四，D5会超过保存364。普通覆盖没有额外同fiber边或仿射控制自由度。

然而必要容量在首根0即失败。对根0完整枚举长度零至五的全部1365条walk，按正向边+z_e、反向边−z_e相消后，在0→0槽只有以下五个整数线性形式：

```
0, T, −T, P, −P
T 为三角形 0–11–22–0 的电压和
P 为五圈   0–1–5–6–2–0 的电压和。
```

取mod9后仍只有五个不同函数。无论怎样赋值电压，从 `(0,0)` 五步内到达同一0-fiber的状态都属于 `{0,±T,±P}`，至多五个，不能覆盖所需九个。完整walk枚举包括所有立即反走和重复顶点的walk，未漏算较短walk或因反走产生的净零电压。

按确定性生成树规范40条边为零后有42条自由边；固定端点的walk系数差是circulation，仅支撑在树上的circulation必零，因此树投影不损失不同线性形式。这里三角与五圈正好各对应一个自由电压，也可直接看成两个任意C9变量。

只检查了首根的41个目标槽便停止，其中最少槽有四个形式；选择base距离零的0→0作为最短清晰见证，五形式已经足够排除。`capacity.json` 保存全部系数、代表walk与41槽计数；`capacity_witness.json` 给出稀疏可读五形式。容量CPU0.0023秒，源检查加容量约0.0034CPU秒。

因此该固定Allwright1(a)底图的任意普通循环C9覆盖都不能D≤5。本结论不排除其他41点底图或不同覆盖机制，但它们不属于本轮任务。

按规定未产生电压起点、未进行任何单边提案、未生成369点图，因而也没有369点最终BFS或待审计产物。`terminal.json` 为 `CAPACITY_FAIL_NO_SEARCH`，无续跑队列。
