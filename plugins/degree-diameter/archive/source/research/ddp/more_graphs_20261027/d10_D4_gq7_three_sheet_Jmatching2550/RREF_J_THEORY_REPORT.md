# 三 sheet GQ：基础 RREF 反例与 J-matching 部分补全

本记录仅为父代理唯一 q7 控制提供纸面证据，没有另一个 producer、图、BFS、phase 枚举或参数试验。原预测、实际 2550 图与首次 R4 反例由主记录管理；本分析不新增方法条目。

## 基础三 sheet 构造的完整义务

W(q) 有 v=(q+1)(q²+1) 个点、同数条线。三 sheet incidence cover 的 line fibres 加 K3；对 spread 的 q²+1 条线，每 sheet 加一个复制其 matched point-neighborhood 的 twin，三个 twin 加 K3。点度 q+2、line/twin 度 q+3，n=3(2v+q²+1)。

base 同点、共线点、相交线以及点线／点 twin 非 incidence 类，都可用相应 line/twin K3 调整 sheet，在至多 4 步内覆盖。真正还要同时满足：

- base 非共线 point pair 的 q+1 条四 incidence geodesics，电压和必须出现全部 Z3。
- base 不相交 line pair 的 q+1 条四 incidence geodesics，同样必须出现全部 Z3。

第二项也负责相应的 line–twin 和 twin–twin opposite 类；纯 incidence 路中可把 spread-line 端点换成其 twin 而不增加步数。不能只检 point–point 一侧。

## 固定 RREF coefficient 函数的原始障碍

取标准 symplectic form B(p,r)=p0r3−p3r0+p1r2−p2r1。令 p=e0,r=e3，二者不共线，共同 collinear 点恰为 z∈PG(span(e1,e2)) 的 q+1 点。两条连接线的 canonical RREF bases 分别是 (p,z)、(z,r)。

如果每个 flag 电压仅由同一个固定函数 f(a,b) 作用于此 RREF basis 的两个系数，则四步路的相位总为

~~~text
f(1,0)−f(0,1)+f(1,0)−f(0,1).
~~~

所有 q+1 路都同色。特殊 f(a,b)=chi(a²−eta*b²) 时，k=chi(−eta)，相位为−2k=k mod3；改变 eta 或 cubic character 本身不能消除这个固定规则的轴反例。base opposite 距离已需四 incidence 步，line/twin K3 不能在四步内额外调相；twins 真复制 line 的 matched 邻接时也不提供另一相位。

父代理实际 J 控制使用下面的另一标准坐标 form。在其坐标里 p=e0,r=e2 的相同轴机制只有至多两种纯 incidence 相位，仍不足三色；此 pair 属于随后 J 能补的类。因此不能把“未加 J 的规则失败”继续当成“加 J 后也必失败”的论据。本分析从未单独生成原无 J 图。

## q7 的新增 J 定理

令 V=F49²，F49=F7[j]/(j²−3)，坐标为 (a,b,c,d)，即 (a+bj,c+dj)。取

~~~text
B(p,r)=a*c'−c*a' + 3*(b*d'−d*b'),
J(a,b,c,d)=(3b,a,3d,c).
~~~

J²=3I；3 在 F7 不是平方，故 J 没有 projective fixed point，定义每 sheet 上的 perfect matching。B(Jp,Jr)=3B(p,r)，因此 J 保 isotropic lines。p 与 Jp 同处其 F49 一维子空间，即同一条 Desarguesian spread line。

对 base opposite point pair p,r，若 B(Jp,r)=0，则 p−Jp 是一 matching 步，Jp 到 r 可经其共同 isotropic line 的两 incidence 步，再花一步 line K3 任意调整目标 sheet，总长至多 4。对 opposite lines L,M，若 M∩J(L) 非空，取 p∈L、Jp∈M，同理 L−p−Jp−M 再 line K3 至多 4，覆盖全部 sheet 组合。

这些都是一整类 pair 的 phase-independent 充分路由，不依赖刚好修复一个已知坏点。固定 p 时，B(Jp,r)=0 而 B(p,r)≠0 的 projective 点数为 q²：两个不同 polar hyperplanes 的点数差 (q²+q+1)−(q+1)。q7 的 unordered 这一类为 400*49/2=9800，与父代理冻结并实测的 J-class 计数一致。

但它不覆盖全部 opposite 类。特别对 spread line S 有 J(S)=S，因此任何 opposite M 都满足 M∩J(S)=空；涉及 opposite spread-twin 的原 phase 义务不能省略。剩余 pair 仍需要原四步路线的全 Z3 覆盖或完整实际检查。

## 度数与验收范围

q7：v400、spread50。基础图 n2550，point copies1200个 degree9，line/twin1350个 degree10；600 条 J matching 边把全部点升到 degree10，最终 2550/12750，全 10 正则。未改其它结构或再使用额外槽。

任意电压赋值都有全局 upper5：对某条 base 至多四步 incidence 路，必要时在 line/twin K3 多花一步调整 sheet；J 只会缩短距离。故唯一实际图某根 R4 有缺项，就足以结合 upper5 得精确 D5，不能把该根缺项数当成全图无序坏对。

父代理实际唯一控制结果：2550/12750、simple10regular，检查 7 个 R4 根后 root6 首次缺 70，首 target171，故精确 D5。native0.016329、整批1.303726 CPU（主记录权威）。预测的 J 部分补类成立，完整 D4 预测失败。本分析不重复这项数值验证、不追 70 个缺项，也不继续 eta、basis、voltage、matching 或 q8 控制。
