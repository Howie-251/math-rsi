# 唯一首最优平面：实际 packing811 对照

2026-11-01。此前 source17 实际运输诊断已经闭合，现仅用它改变一个生成规则。此记录先于新 solver 调用。

**正假设 P2。** 固定 retained4=[31,59,60,72] 的324个中心，保留全部15个 admissible 变量层。仅 source17 从旧 W={(a,b,4a)} 改为实核首最优平面 W'={(8t,s,t)}，normal=(1,0,4)、basis=(0,1,0),(8,0,1)。其他14个变量层仍旧W。这个实际1539点候选池存在至少811个完整N54互不相交的中心。

依据是 source17 的7个共享目标约束在W上有5种 projective 方向，在W'上只有4种，且W'继承全部六条 dart transversal。方向少一种并不保证可行；真实 pin 冲突可推翻此正假设，UNKNOWN也不当不可能。

一次生成1539个中心各54个原source pins；324固定，1215个点变量与3个合法 target48 mincut binary。逐actualpin约束负载≤1，变量数≥487。只做一次 scipy.milp feasibility，threads=1，wall44秒、solver CPU≤45、总CPU≤60。target48 min(w17,w35,w74)≤20 的已证cut继承，不重复域/旧rank检验。旧810集合（ret4加32/44/45/61/73/74全plane，不含17）直接代入新模型，必须只违反新增≥487这一行；不重跑原fixedW solver。

如找到≥811，使用独立dict逐pin核不交并保存真实坐标/有序N54；如INFEAS只关闭这唯一新normal池、按数值MIP证据尺度报告；如UNKNOWN保留incumbent/bound与未决范围。无第二plane、phase/seed变动、自动续timer、旧图读取、旧field/rank/BFS/Lean或自动图生产。
