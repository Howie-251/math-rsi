# 公开来源与研究机制对照

检索日期2026-10-26。仅使用原始论文、作者仓库与维护者公开表；事实、方法建议及本轮验证分开。下列链接供Codex逐项使用，不表示全部PDF全文已读。没有复制原论文全文。

## A. 数值与具体对象

- **S-TABLE** Francesc Comellas, *Table of Large Degree/Diameter Graphs*，主表最后更新2026-10-25；读取了定义、表及更新记录。
  https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html
- **S-D3** 同站Diameter 3说明页；读取本包选定条目和群乘法约定。
  https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html
- **S-D4** 同站Diameter 4说明页；读取本包选定条目。
  https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html
- **S-D5** 同站Diameter 5说明页；读取本包选定条目。
  https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html
- **S-R24** Rishabh Rajiv, *New lower bounds for the degree-diameter problem from Cayley graphs, orbit graphs and lifts*，Zenodo 22928337，2026-09-24。读取作者仓库摘要、文件列表与数据入口，**未读完整PDF**。对应252、441和5334点来源；同文119点(6,3)已被现表120取代。
  https://zenodo.org/records/22928337
- **S-R24A** Rishabh Rajiv, *Improved lower bounds for the degree-diameter problem from metacyclic groups, coset graphs and affine lifts*，Zenodo 22073603，2026-08-24。读取仓库说明和文件列表，未读完整PDF；(6,5)=1518的对象来源。
  https://zenodo.org/records/22073603
- **S-M120** Michel de Messieres 的作者仓库23136968；本轮该仓库访问未成功。120点数值边表通过S-D3读取并已验证，方法介绍来自S-D3，不能声称已读作者全文。
  https://doi.org/10.5281/zenodo.23136968
- **S-M684** Michel de Messieres 的作者仓库23167440；本轮该仓库访问未成功。684点构造介绍与下载导航来自S-D4；未声称已恢复/验算684点图。
  https://doi.org/10.5281/zenodo.23167440

主表是“largest known”的动态维护资料，不是所有格子的上界证明。单个来源通过验证说明存在相应图，不保证它还是最新世界纪录；真正候选出现后须再查最新公开来源。多个源不一致时保留各自日期、对象和验证状态，不挑更低数字报成功。

本轮尝试访问Combinatorics Wiki的general-graphs页面返回502，因此不声称用其独立交叉确认全部纪录。容器HTTP下载也不可用，边表或论文未取回时已在问题卡标记。实际源码或数据应按研究所需恢复，不反复失败下载代替数学工作。

## B. 两篇成功案例：继承动作，而不移植成功保证

**P-MIZUNO** Ryosuke Mizuno, *New lower bounds for the degree/diameter problem via interaction with a browser-accessible LLM*, arXiv:2606.15860v1，提交2026-06-14。读取HTML的初始任务、研究轨迹、构造概述及限制讨论。
https://arxiv.org/html/2606.15860v1

§4.1允许模型在Δ≤16、D≤10内按想法选择参数。可借鉴的是机制优先选参数、控制图与纤维覆盖分工、具体瓶颈出现后改变表示。本文的(12,5)=34992在当前主表已不是该格最新下界；复现论文不是新纪录。本Goal不照搬其禁止组合旧方法或限制浏览的指令；旧技巧得到真实新下界同样有价值。

**P-RAMSEY** Przybocki, Mackey, Heule, Subercaseaux, *Doubly Saturated Ramsey Graphs: A Case Study in Computer-Assisted Mathematical Discovery*, arXiv:2604.21187v1，2026-04-23。读取§1.2与§3方法轨迹。
https://arxiv.org/html/2604.21187v1

可借鉴：用SAT或专用代码得到真实对象、识别同构表示、归纳生成公式，再做证明/形式化。不能据此预设我们所选参数都存在可提升的循环族。九个样本的归纳过程也不是本项目已有数据。

## C. 按需回到原文的经典方法入口

**P-VOLTAGE** E. Loz and J. Širáň, *New record graphs in the degree-diameter problem*, Australasian Journal of Combinatorics 41 (2008), 63–80。
https://ajc.maths.uq.edu.au/pdf/41/ajc_v41_p063.pdf
本轮只由S-TABLE确认书目信息、由条目确认相关来源，未在本轮分析这份PDF。要实际采用具体电压规则，由Codex读原文定义与条件；不是新理论。

**P-CAYLEY** M. J. Dinneen and P. Hafner, *New results for the degree/diameter problem*, Networks 24 (1994), 359–367；作者预印本math/9504214。
https://arxiv.org/abs/math/9504214
本轮确认条目引用与群乘法，未重新读全文。使用群表示时必须确认逆元、操作方向和参数合法性，不能把别人符号机械翻译成不同半直积。

## D. 新Goal中的三个研究机制（建议，不是已证明可成功）

**M1 小商图＋路线位移覆盖。** 从少量底点和群/纤维参数定义全部边；对每一对底点，把长度≤D的可行路线对应到纤维位移集合，要求覆盖全部目标位移。精确实例可计算；统一覆盖定理可转为构造族。群和底图都是选族限制，失败不证明一般原题不可能。

**M2 非等长轨道／陪集作用。** 让少数轨道及稳定子决定大量邻接，把度数和路径控制纳入真实群作用。保留原始图中各轨道的边数一致性，不只选择一个看似可行商矩阵。当前可用来源是(5,4)、(6,4)、(6,5)，不保证换群就有改善。

**M3 仿射纤维与路径满秩。** 给出真实可逆映射及反向规则；检查控制路线是否能让所有纤维坐标可达。满秩只解决相应路线/坐标问题，还必须闭合所有起终底点、允许长度和简单图度数。以(12,3)来源为具体起点，不能照搬直径5的证书到直径3。

任意图修复可作为以上机制的辅助或另有数学动机的路线，但不默认“固定旧核＋加一个点＋无限补洞”。不强制原创工具、不先建立复杂训练系统。

## E. 反例如何帮助挑机制

只攻击明确的承重断言，例如“该路由条件足以保证任意纤维目标D步内可达”。给出满足前提但失败的实际小例后，撤回或修正该断言；没有反例不当证明。局部图、放松矩阵和完整目标图的证据等级不同。复用U5的区分，不重新启动其n61专用实验。

## F. 三种收尾方法在本轮的角色

全图计数、结构传播、完备有限判定仍可用于证明构造正确或结束一个明确小义务。但本轮不是全域上界任务，不要求先穷尽一个失败族才能换参数，也不让证明支线默默接管新纪录目标。
