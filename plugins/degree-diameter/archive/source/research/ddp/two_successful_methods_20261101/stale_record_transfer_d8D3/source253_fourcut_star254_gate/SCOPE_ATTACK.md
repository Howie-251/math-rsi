# CM253 四cut八星：缓存证据与归一化的只读反例攻击

本次只读 `HISTORY_SOURCE_GATE.json`、`PRED.md`、`NOTE.md`，以及它们明确指向的旧producer、schema、recipe与旧validation metadata。没有执行producer、重新解析source全边表、生成group/graph、重跑BFS/field或旧degree-reduction结论。未扩大本轮数值域。

## 1. 缓存确实是唯一三步最短路，但不是全部关键路线

实际producer为：

- `research/ddp/breadth_20261027_wave10/degree_reduction_scout/screen.py`
- 输出metadata：`source253_to_degree7.json`
- 输出逐边证据：`source253_to_degree7.forced_edges.json`

CM253分支调用 `inspect` 时没有给 `cache` 参数，因此走直接枚举分支。对每个源u，先构造closed两步邻域 `near`，仅对 `v>u` 且 `v not in near` 计数所有三步walk。`counts[v]==1` 才保存四label路径。因此这些是source距离恰3的唯一geodesics，而不是只在某一受限NB词表中唯一。被排除的即时回走 `b==u` 不会贡献到两步邻域外的目标。无序端点只通过 `v>u` 去重，不漏掉另一方向的路径计数。

随后 `forced.setdefault(edge,path)` 对每条该类路径的三条边登记，但每edge只留首先遇到的一条。旧metadata记9108个unique3无序点对，逐边文件为1012项；这两个数量的含义不同。不能把1012个保存项当成全部9108个点对，不能把每条边所保存的一条当成全部穿边geodesics。

首个schema实例是：`edge=[0,33]`、`unique3_path=[0,33,7,245]`。该指定edge处于路径首段，明确不是middle。producer中的 `unique_middle_edge` 字段只在一处blocking-vertex说明中描述路径自身的中段；它没有宣称被登记的每条forced edge都是中段。

本次继承旧producer的有限精确计算，不重新验证9108条路径。没有发现其“唯一3路”语义被误写为仅NB唯一或仅某局部路线唯一的依据。

## 2. 同一RIGHT源与label绑定

旧producer直接读取：
`context/DD_PORTFOLIO_START_20261026/baselines/d8_D3_known.edges`。
旧metadata的 `source` 也为同一路径，旧validation为
`context/DD_PORTFOLIO_START_20261026/validation/d8_D3.json`，本次只继承其253/1012、8regular、D3与253根旧验收状态。

`generator_specs.json` 中actual `id=d8_D3` 给出m=11、n=23、a=9，四个positive generators为(7,2)、(10,4)、(1,16)、(9,17)。`tools/reproduce_known_cayley.py` 的literal生成代码使用

`p=23*x+y; q=23*((x+u)%11)+(y*9**u+v)%23`，

即RIGHT邻边 `h--h*s`，与本轮HISTORY的group-law/label一致。该脚本通过true inverse闭合generators；不是把负坐标误当成逆。旧source与逐边路径采用同一baseline literal，而非另一个253点同参数源。这里是现成provenance绑定的只读核对，不是本轮重新运行generator或证明新旧两大字面文件相等。

## 3. 左归一化何时完备，哪里可能误用

对每条actual undirected source edge，必须先在四个positive inverse classes内确定实际方向 `h -> h*s_i`，再对整条saved path左乘 `h^{-1}`。如果saved path穿edge的方向是反向，应反转整条四label路径，使canonical cut沿 `e -> s_i`；首段随反转变末段，中段仍为中段。不能仅交换cut两个label，不能以label大小代替positive-generator方向，也不能把RIGHT乘法误用成右平移归一化。

例如raw edge0--33的33是primary给定的(1,10)，属于positive(10,4)的inverse。因此canonical正向未必是raw path0→33方向。这是为何“先辨方向、整路反转并保留位置”有实际必要性，而非假设角落情况。

LEFT乘法是RIGHT Cayley源的真automorphism，保持边、距离、唯一性及四条cut的互不相交性。四个positive inverse classes覆盖所有旧边，因此对某一类首cut证明无解，可以通过此同构排该类所有placement；无需假设四类之间edge-transitive。缓存中任何一个经合法平移所得的义务都适用于canonical first cut。去掉重复义务只会减弱筛选，不会误排解。

若只用四条canonical edge各自保存的一条witness，会留下较弱的合法subset；不能称继承了其余1008条saved witness，不能以其通过排除全族。若投影所有逐边witness，须明确每条是按其登记的那条edge投影，而非任取其路径别的边后沿用原class/位置。任何selected subset只要每项合法，都可支持严格NO；subset过门只说明尚未排除，绝不认证254或完整D3。

## 4. 首、中、末段的正确修复义务

设删边集合F的所有端点为P，保留其它旧边且只加新星z。删除边全部在P内部，故到P的距离保持：`d_(G-F)(P,x)=d_G(P,x)`。对一条source唯一三步路径端点A、B，如果它所含的指定cut被删除，旧图部分不再有≤3路线；任何成功修复必须经过z。因此精确star修复门为

`d_G(A,P)+d_G(B,P)<=1`。

按指定cut位置展开：

- middle 1+1：own cut两端只给A、B各距离1，星路长4；其它pins必须包含A或B本身，包含其普通邻居还不够。
- first 0+2：A已经是own pin，own两pin距B均不在closed B1内；其它pins至少一项必须落在旧closed B1(B)，其中包含B本身。
- last 2+0：对称要求其它pins命中旧closed B1(A)。

这些都是实际label条件；不能把first/last也写成“必须命中路径端点”，那会过强而漏解。不能省去closed B1中的中心点，不能要求同一pin只能修一项。反之middle若放宽成closed B1只会得到较弱必要条件，不能把该放宽的通过当成功。

四cut中其余三边给六个pins。若用“每额外edge命中义务的最大数×3”作上界，可以放宽三边之间的disjointness或其它限制；这样得到的NO仍安全，过门仍未知。不能把不同义务所需的pin强迫互异，除非另有actual matching/cover证明。

## 5. 攻击结论与范围

目前只读证据未发现旧unique3缓存语义、RIGHT源绑定或合法LEFT投影本身有漏洞。真实需要避免的误强假设是：一律middle、inverse方向只交换edge而不反转整路、首末段不允许closed B1、或者把一个subset的通过当全D3。

旧degree-reduction NO只针对不加边不加点的spanning subgraph；新增star可以修复被删唯一路，因此旧NO不能替代本轮gate。新根覆盖也不能替代这些old-old义务，反之old-old subset过门不能替代新根或最终D3检查。

本文件不预报f9数值结果，不登记新graph/parameter/Lean/method，不授权新增source/cut/solver批次。reader的保守准备收费为0.25CPU秒，包含一次错误尝试读取不存在的旧`run.py`（随后通过`rg --files`找到实际`screen.py`）；不重复source-read门已收费的0.8。已显式计时的两次metadata读合计约0.00172CPU秒，其余read/process启动统一包含在0.25保守收费内。
