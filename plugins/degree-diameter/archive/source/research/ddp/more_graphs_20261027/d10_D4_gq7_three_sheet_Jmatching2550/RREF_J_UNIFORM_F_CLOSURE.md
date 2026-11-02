# 固定 RREF、统一 flag 函数与固定 J 的整族 D4 阻碍

这是唯一控制首反例之后，由父代理 cached coordinates 提出的纸面族闭包；本分析逐式核对，没有生成另一张图、重算 geodesics、BFS 或试其它函数。范围是父实验相同 F7、canonical RREF linebases、同一个 flag 函数 f(a,b)→Z3、相同几何 J-matching 与复制 spread-line incidence 的 twins。它不排 line-dependent 函数、其它 basis、不同 J 或一般 3-sheet voltage 构造。

## 固定一个 base opposite pair

使用父实验的 form 与 matching：

~~~text
B(p,r)=a*c'−c*a' + 3*(b*d'−d*b')
J(a,b,c,d)=(3b,a,3d,c).
p=(0,0,1,1), r=e0=(1,0,0,0).
~~~

直接得 B(p,r)=−1=6，B(Jp,r)=−3=4，均非零。共同 collinear 点满足

~~~text
B(p,z)=−a−3b=0，B(r,z)=c=0.
~~~

故完整 8 点为 z_d=(1,2,0,d)，d∈F7，以及 z_infty=e3。每个 z 唯一给一条 p−L(p,z)−z−L(z,r)−r 四 incidence 路。

## 八条 route 的系数只有两种

记 f10=f(1,0)、f01=f(0,1)、f12=f(1,2)、f11=f(1,1)。对全部七个 z_d：

- L(p,z_d) 的 RREF basis 是 (z_d,p)，故 p 的系数为 (0,1)，z_d 为 (1,0)。
- L(z_d,r) 的 RREF basis 是 (e0,(0,1,0,d/2))，故 z_d 的系数为 (1,2)，r 为 (1,0)。

采用 point→line 为正电压的约定，每条 route 相位均为

~~~text
alpha = f01 − f10 + f12 − f10 = f01+f12−2f10.
~~~

对 z_infty=e3，第一条 line 的 basis 是 (e2,e3)，第二条为 (e0,e3)，相位为

~~~text
beta = f11 − f01 + f01 − f10 = f11−f10.
~~~

因此任意统一函数 f 的 8 条 route 只可能出现 alpha、beta 至多两种相位。Z3 有三个 sheet，至少一个目标 sheet 缺少四 incidence 路。若相关 line 是 spread line，换其 twin 只复制同一 matched-incidence 相位，并不新增相位。line/twin K3 需要额外一步，不能插进 base opposite 已需的四 incidence 步中。

对父唯一 eta3、generator3 cubic character 的 norm，四个函数值为 f10=0、f01=1、f12=1、f11=2，故 alpha=beta=2。这与父代理从 cached coordinates 得到的实际 8-route histogram [0,0,8] 完全一致；该数值诊断不由本分析重新执行。

## 固定 J 也不能给这个 pair 更短的其它路

完整图的 point–point 额外边只有 J matching，且 J²=3I 在 projective 点上是 involution。

- 用一条 J 的至多四步路，除了 matching 外只能用两 incidence 步及至多一步 K3；必须使 Jp 与 r 共线，或 p 与 Jr 共线。两条件相同，均要求 B(Jp,r)=0，这里为 4，故失败。
- 用两条 J 与两 incidence 步：若两 J 相邻则消去，要求 B(p,r)=0；若分处两端，则要求 B(Jp,Jr)=3B(p,r)=0。这里均非零。
- 三／四条 matching 不能在剩余步数内连接这个不同的 opposite pair；不使用 matching 的其它至多四步路已由上面的 pure-incidence／K3 分类覆盖。

因此这些额外边不能补第三种相位。对这个固定 pair，任意统一 f 都至少遗漏一个 sheet 组合，故该完整族不可能 D≤4。结合已证明的任意 voltage upper5，该族实际上恒 D5，但不需要逐个生成来验证。

## 结论与停止范围

J 部分补全 theorem 仍成立，9800 对那一类 opposite point pair 仍全被补上；本 pair 不在该类，B(Jp,r)=4。它不是推翻 J 局部 theorem，而是证明局部补类没有覆盖全部义务。

固定 same-f/RREF/fixed-J 族到此完整关闭，不继续 eta、cubic generator、统一函数选择、同一规则的其它 seed。line-dependent f、不同 basis 或不同几何 matching 不在此证明范围，亦没有自动启动。纸面证据并入同一 frozen candidate 的 raw，不新增实验 row。
