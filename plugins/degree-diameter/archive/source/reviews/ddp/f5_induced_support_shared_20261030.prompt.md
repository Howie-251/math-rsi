Continue the same fixed F5 induced-subgraph mechanism. Static mathematical counterattack only: do not run experiments or restart old search. Your earlier PASS covered the transversal >=2000 argument and original unique-control-word compression, not the new claims below. Review three load-bearing additions: (1) completeness logic of the 30-variable Horn-support NextClosure enumeration, taking its literal six-large-support data as finite evidence, (2) missing external pencil plane implies |S_u|+|S_v|<=125 for arbitrary partial fibers, hence all 30 fibers nonempty for any D3 induced graph with >1875 vertices, (3) external p,q shared-middle family has exactly five paths x-z-w-y, and the two conditional OR clauses are necessary. Pay special attention to triangle edges, absence of alternative two/three control paths, affine translations, the exclusion of w from X, and whether all30 assumes whole fibers. Distinguish paper validity from enumerator/CNF implementation and solver certification. Return SOUND AS STATED or a concrete flaw/counterexample and required correction. New 315221/1290903 model has just started its single bounded batch; no new graph claimed. Full paper follows:

# F5诱导图的支持层密度与共享中间点约束

## Target

在固定3750点F5成功图中寻找最大度≤16、直径≤3、阶数≥1921的任意诱导子图。需要证明可安全用于生成的必要条件，不把松弛模型满足当作完整图。

## Status

COHERENT AS STATED。本地独立静态核对已通过两条几何引理。支持层有限枚举已完整结束，另有不同算法的小SAT反例攻击返回rawUNSAT；严格支持分类的依据是完整闭包枚举与其完备性，而非未认证SAT单独证明。外部静态审阅另记真实回执。

## Invariant Object

保留集S的控制层支持Q={a:S_a非空}，以及给定端点对的**全部**≤3路线共同要求哪些中间点存在。单点保留变量仍独立，不假定整fiber保留。

## Assumptions and inherited facts

固定参数见../f5_full_d20_D3/PARAMETERS.json。每fiber为F5³，共30层。四方向为ell0,ell1,ell2,ell3=(e0,e1,e2,(1,1,1))；反向端口inv=(1,0,3,2)。边为y=T_p x+t ell_inv(p)。

继承已有证明：T_p可逆且反向关系成立；36种非回退转向全部秩3；相邻控制点的六个回退平面均为25点，公共线5点，线外120点各只属于一个平面。控制器C30简单4正则、三角10个、无四圈。external控制边指不在三角中的边，因此它也没有长度2替代控制路。此处不将六平面证书登记为本轮新发现。

## Notation

S_a是fiber a中保留的点，n_a=|S_a|≤125。Q为非空fiber集合。对外部控制边u→v，端口为p，L_p=span(ell_inv(p))。N_p(w)表示w在p目标fiber中的五个邻点。q-line(w)表示源fiber内w+span(ell_q)。

## Derivation Strategy and Map

1. 真正D3诱导图的Q必须对258条唯一控制距离3词的中间点闭合。
2. 完整闭包分类留下6个proper支持：3个16点、3个19点。
3. 控制距离排掉16点者；缺pencil平面的密度界及四边匹配排掉19点者，推出目标Q必须全30。
4. 对external相邻控制fiber，虽有5条不同三步路，它们仍可共享一个中点。这给旧唯一控制词模型之外的新精确路线约束。

## Main Derivation

### 1 支持分类与最初预测的反驳

若唯一控制词u–a–b–v的两端在Q，则选任意保留端点，其原唯一三步路必须保住，所以a,b也在Q。原258有序词去反向重复为129个双结论Horn规则。

NextClosure完整枚举24575个闭支持。proper最大为19；proper大小≥16者恰有6个，即三16和三19。因此“所有proper闭支持≤15”的最初预测被反驳，不能仅凭这个预测强制Q全30。

枚举完备性的自包含说明：以闭支持A为当前项，检查i从29递减到0；对不在A中的i取B=cl((A∩{0,…,i−1})∪{i})，仅当B与A在i之前一致才接受。任何闭支持D在lectic次序中大于A，令j为其与A第一个不同坐标，则j在D且不在A，种子包含于D，故其闭包也包含于D并满足前缀条件。选最大的合格i给出不大于D的下一闭支持，所以不会跳过任何闭支持。从cl(empty)到全30即穷尽全部闭集。check.cpp忠实执行此算法并在到达全30时记录complete。

完整mask文件和6个大proper支持见../f5_induced_support_closure/。一个独立30变量SAT模型同时要求Horn闭合、proper、≥16并禁止这6个精确支持，返回rawUNSAT；这只是不同算法的错误攻击，不代替上述完备枚举。

### 2 控制距离及缺平面的两fiber密度界

三16支持各自在其诱导控制器中有距离4的见证，分别(10,29)、(2,7)、(0,25)。投影不可能缩短保留图路线，因此它们不能支持D3图。

三19支持的控制器距离都≤3，不能据投影排除。取其中一条external边u–v，若u或v有某个控制邻居不在Q，则至少一个回退平面W完全没有可用路线。因为external边没有2步控制路、C30无四圈、六pencil线外互不重叠，所以任意保留端点变换为x∈X=T_p S_u、y∈Y=S_v后，必须满足

    y−x 不属于 W\L_p。

按F5³/W的五个coset分组。同coset内若X和Y都非空，任取一对基点便迫两集合都在同一条L_p仿射线中，各至多5点，总计≤10；若一侧为空，另一侧最多25点。因此每个coset总计≤25，故

    n_u+n_v ≤125。

这适用于任意partial fibers，甚至不要求S_u与S_v实际保留一条边，只要求u,v∈Q。不能用于triangle控制边，因为那里有额外两步平面。

三19支持各有4条两两不共端点的上述bad external边。匹配见证分别为

    A: (1,13),(3,21),(5,12),(6,15)；
    B: (0,20),(4,18),(5,12),(6,15)；
    C: (0,20),(1,13),(2,11),(4,25)。

具体支持与每边被省略的控制邻点见DENSITY_RESULT.json。相加四个密度界，再对其它11层用125上界，得N≤(19−4)125=1875。

### 3 生成器可强制全部30层非空

任何N≥1921诱导图的支持至少16层。所有proper Horn支持中，≤15层者最多1875点，三16者控制距离失败，三19者密度界最多1875点。因此目标支持只能是全部30层。生成器可加30个OR125的非空约束，但各层点数完全自由。

### 4 五条路线也能共享必选中间点

取external控制边u→v、端口p，q≠p。在fiber u取任意w，令

    X=(w+span(ell_q))\{w}，Y=N_p(w)，Z=N_q(w)。

|X|=4，|Y|=|Z|=5。对x=w+t ell_q(t非零)及y=T_p w+s ell_inv(p)，差y−T_p x落在唯一first-q回退平面的线外部分。因此所有≤3路线都由该控制回退提供；其它平面、直接边及两步控制路都不可用。

回到u-fiber的中点w'需同时满足w'∈x+span(ell_q)且y∈N_p(w')。T_p ell_q与ell_inv(p)独立，迫w'=w。完整K5,5线关系又给N_q(x)=N_q(w)=Z。所以所有旧三步路恰为

    x–z–w–y，z∈Z。

保留端点的必要且充分条件（对这20对端点的路线类）是保留w且至少保留一个Z点。因而可精确压为

    keep[w] ∨ ¬OR keep[X] ∨ ¬OR keep[Y]；
    OR keep[Z] ∨ ¬OR keep[X] ∨ ¬OR keep[Y]。

共60个有向external控制边×3个q×125个w=22500组。旧OR5门复用；新增15000个exact OR4门（75000绑定子句）及45000路线子句。另加30层非空子句，模型从300221/1170873变为315221/1290903。

固定字面校准为w=0、p=1(0→20)、q=0(0→18)：X={1,2,3,4}，Y={2500,…,2504}，Z={2250,2255,2260,2265,2270}。全部20对直接枚举所有原2/3walk，都只有上述5条三步路，共同内部点恰为0。未做BFS或导新图。旧控制距离3闭包不作用于这个相邻控制点对。

## Remarks and Interpretation

独立路线的条数与真正可用的覆盖不能混同：五条路径可能只替换同一个z而共享不可缺少的w。反之，最初支持闭合预测确实被19点反例推翻，必须用额外几何密度而非把该预测硬写进生成器。

## Boundaries and Non-Claims

所有条件只服务这张固定F5图的诱导保留机制，不给N(16,3)一般上界。没有要求whole fibers。增强CNF仍可能漏其它D3约束；SAT必须实际核诱导图所有根，失败则用全部原2/3路线添加精确cuts。准备完成不算求解、更不算新图。原大模型UNKNOWN、14度K2 UNKNOWN及小压缩门仍保留各自终态，不重置旧预算。

## Open Risks

支持分类依赖完整有限枚举，密度禁区依赖已核六平面互补性，故原始mask、控制词、匹配见证与OR门变量绑定都须保留。外审仅核数学推导，不能代替CNF实现、数值求解、独立图验收或最终Lean。

