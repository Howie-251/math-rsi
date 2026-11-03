# 78点degree5 Cayley任务：按已知最优性报告停止，未枚举

拟议群为F13⋊₄C6，78点，五元逆闭生成集合给出普通degree5 Cayley图。项目旧来源笔记已记录纯Cayley(5,3)的最优阶报告60；本次重新定位原文后停止，不为已知文献范围重做16887个生成集合枚举。没有生成图或执行BFS。

## 原文位置和适用范围

|位置|PDF页码|实际内容|
|---|---:|---|
|Introduction|印刷第1页，PDF index0|把所讨论最优Cayley图归于Conder；同时说明本文新增非同构实例的搜索并非穷尽。|
|§3.2|印刷第6页，PDF index5|以(5,3)=60为节标题，称这些Cayley图optimal，并指MC60 / SmallGroup(60,5)。|
|References [5]、[6]|印刷第15页，PDF index14|[5]指Conder的Combinatorics Wiki最优Cayley目录；[6]为Conder相关稿，仍标2026年5月准备中。|

来源为Francesc Comellas，[*Non-Isomorphic Optimal Cayley Graphs*, arXiv:2606.10954v2](https://arxiv.org/pdf/2606.10954v2#page=6)，并对照[HTML原文](https://arxiv.org/html/2606.10954v2)。[引言](https://arxiv.org/pdf/2606.10954v2#page=1)的范围是Cayley图，不限制为阿贝尔、metacyclic或某个固定群，所以拟议78点Cayley族属于该外部最优性报告覆盖的类型。78大于60，故不再作为突破一般图72门槛的入口。

必须区分报告与证明：[References](https://arxiv.org/pdf/2606.10954v2#page=15)中的Conder [6]尚属准备中，本次没有取得或复核其原始分类证明，也没有把Comellas新增实例的非穷尽搜索误当成上界证明。这里采取的是项目既有的文献选题止损，不登记本地新的78点不可行性穷尽结果，更不把纯Cayley最优性移用于一般图或双轨道图。

## 执行状态

`SOURCE_SCOPE.json`记录原文页码、Conder引用的准确scope及引用边界。旧笔记为`research/ddp/SOURCE_UPDATE_20261026_22.md`。未找到本地完全相同群/degree/D的既有完整枚举，但由于上述全Cayley文献范围，不另启动它。

计划16887个逆闭集合保持“未执行”：0相位筛枚举、0真实群生成集合枚举、0图、0BFS。没有额外group/degree/seed队列。lamplighter384的已完成30容量证据不变。本任务terminal，pending为空。
