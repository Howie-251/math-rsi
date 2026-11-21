<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# ordinary858的65点反设：真实P、缺角与同标签行充账

当前状态：**两次实际完整DRAT均已通过，普通858≤64已闭合。** 首次退出0、唯一VERIFIED，7447.126秒；独立完整重建第二次退出0、唯一VERIFIED，7558.774秒，前后CNF/proof哈希一致。[最终封存回执](../../../evidence/858/ordinary858-64-final-receipt.json)与[稳定入口](ORDINARY858_64_VERIFIED.md)均已落地。没有外部审阅。

## 1. 证书绑定

原查询 `<private-artifact-root>`，298421变量、5187084子句，CNF SHA256
`f8f5cdead0740948641ea3f025c21a0a37e342eb8ab16968bdf90b022db3ba26`。
原源 `near65.py` SHA256 `ce0325d8c8dda4c34b0d2d34c5aebb61f85f79149587211e6871efa94fe6ac86`。
原proof SHA256 `ace3d9e1479d998fdb883a429803b09e05005b9bc08b276c59838d50054bea05`，2438439752字节。

独立源 `rebuild_near65.py` SHA256 `c3e888f93d14b68c3bde09d64a011a1c8202b5f1d4012c4c811985eb6a733514`，不导入或执行原near65 builder。它逐项再生完整语义域、逐次核对215369个语义变量的ID，并重算数字counter与后插入语义变量交错的所有ID，完整新CNF与原件SHA逐字节相同；再枚举2^20→908→843首六色表并再生563洞行/24横块，12.503967779秒完成。独立目录 `near65-independent-v1`。

首checker实际PID3776608与第二checker实际PID3777413都已自然返回0。两原日志均477字节、唯一VERIFIED：195853个原句核心，14905851个引理核心，443251915次resolution，8735个核心RAT引理。两个进程使用同一权威drat-trim实现，均无deadline。不能把两个进程描述成不同checker实现或外部审稿。

## 2. 原对象与真P赋态

反设有65点完整有序rank3 signotope，禁蓝5、红8、weak8。对实际pairxy，l_B,l_R为最长同色结束于xy的边数，故l∈[3]×[6]。两色分别在对应色三元组后严格增长。取

P(y)=↓{l(x,y):x<y}。

每个实际pair的l在P(y)\P(x)，故P注入84个3×6理想。任何可比占态的包含序与实际时间序一致。将空态加入这份实际序的线性扩张即可满足全部84态owner order。19个h为洞；没有采用66冻结、Q=E、所有pair l=u、真实末两态或后六模板。

## 3. 真实进角与缺失出角

P(y)每个极大角g必由一个实际前驱pairxy实现l=g。源码E(a,b,g)枚举所有可能实际owner顺序、差格和来源extent的候选，包括不可比态；只在可比时绑定已有同一l onehot。真输入将所有真实pair的精确l候选置真，其余置假，能同时满足所有进角存在式及每pair唯一。

来源extent是l_B≤width(P(x))+1、l_R≤λ1(P(x))+1。若l=(1,1)，源必为全体第一点：否则任一更前点以其三元色将该色结束秩提高到至少2。故仅g11的E候选可排非首源。这与66的u精确无关。

对P(x)最小可加角g，定义missing(x,g)当且仅当没有真实出pair的l恰为g。令Q=G\↑{l(x,z):z>x}，使用同一份固定l，而不是实际forward上理想Imax(u)。若g缺失，则g∈Q：否则有出l≤g，因出l不在P、g为最小外角，只能该l=g，矛盾。因此P(x)+g可以独立替换P(x)。

任意各点同时在各自[P,Q]内改态，所有原l仍属于目标减源，原色严格增长保持，故新chart仍注入。源码missing为洞态取假；未缺角由同一实际E出边见证，缺角则满足出角OR中的missing项。没有将“未缺角”解释成u=l。

## 4. 九坐标的缺角费用：e=1总数至多3

一次添最小外角只把字码中一个坐标j−1换成j，j原本不在该字中。不同最小外角引入不同j；相邻可加列需严格高度差，所引j甚至相差至少2。

固定j，同时把所有能通过缺角引入j的物理点各添该角，其他点不动。这是同一l下的合法独立改态。含j面压成2×6实际输入，继承禁蓝4、红8、weak8，Baek短帽容量22。于是

deg_P(j)+#missing_introducing_j≤22。

完整含j目录有28态，故源码精确源不等式为

holes(F_j)≥6+#missing_introducing_j。

九式求和，19洞各被计三次，57≥54+Σmissing，即65点反设最多3个缺角。64点版同理最多6。基准CNF用nine seqcounter不等式表示，不能把这一e>0结论误作全冻结。

另有独立有限几何程序 `audit_missing_geometry.py`，直接按列高检查全部84态的168最小加角：所引入j逐点互异，且都不是原字坐标；293个缺角子集改态全部合法。它还检查所有2520理想区间，验证固定l区间面积≤3×新增可用坐标数。`missing-geometry-audit.json`为PASS；该小核未更改任何CNF或进程，不以数值枚举替代上述同标签独立改态的实际输入论证。

## 5. 每条纯洞行的共同改态费用

任一合法同输入纯洞支持S，要求holes(S)≥d。令Entry_S(x)为当前P(x)在S外、但有至少一个missing最小角添后进入S。为每个Entry点任选一个这样的角，同时改全部这些点，S内原占点保持不动。同一l保证改态chart注入并保留实际颜色/weak禁制。因此新S人口恰增Entry点数，得到

holes(S)≥d+#Entry_S。

源码对每个S、每个物理源只用一个OR旗，即使多角进入同一行也不重复收费；7279个missing→entry蕴含、7149个行/物理源组。CardEnc编码holes + negative-entry ≥d+#entry。这不是在不同独立chart相加结论：每条式各取一份同一原l允许的共同改态。

所有563支持是原生反单调边界迹、其单坐标迹、同输入数值子域及24横压缩。原生行在任意admissible chart上保持同端遗传路径，见EIGHT-MOVE §2；改态无需仍canonical。数值子域压缩保留原实际颜色，仍能重算canonical后调用普通容量；2×6用22、3×5用完整纸证N857_SHARED_ROWS_NEXT的50、3×6用九个22面得到66。程序独立再生每个支持与需求，不把原857≤50纸证冒作checker验证。

## 6. 其余全部组的真实满足赋值

可比pair的l onehot取真实l，颜色取同一实际三元色。严格增长与四点packet直接继承；洞端点的这些变量可任取合法域，不激活物理约束。固定源红DP、共同端蓝3/4旗取真实存在性，所有单向激活式成立。红7+B3或红6+B4同端会产生weak8，故两类禁制均真。

极大入角(g_B>1,1)的实际见证pairax有红结束秩1，因此任何p<a三元pax都蓝；a不能是全体第一点（其出l必11），取全体第一点给至x的真实蓝3。这项只用真l，既不需要u=l也不需要末态。

真P首两态必为123、124，第一pair l11；第二点出pair l依与第一点的共同三元色精确为12或21。首六点的l只依首六原色，完整843个避蓝5色表覆盖所有实际首六点；共用每个可比pair和颜色变量，shadow仅排除该六态之前另有占态。无后六、末态或未来秩假设。

数字counter的源不等式已如上逐项证明，因此标准seqcounter有相应辅助变量赋值。真19点owner-C色表按原三元重算全部l/P，实际校准所有物理子句与各新充账源不等式；只有65人口预算不要求19点fixture满足。校准是方向检查，非65点存在。

## 7. 与其他当前作业分离

此次已双核UNSAT是最基础near65-v1，**不依赖**后续rank fan、整区间图像、actual full16/full31 Hall匹配、混合P/E或66全冻结。那些加强全部独立目录/源/运行；未给本证书补不存在的依赖。仅此固定必要式已排65点，得到ordinary858≤64；配既有普通866≤57得真实D≤121。主线C188已完成独立第二DRAT，故可组合Q≤309、F≤310、ES≤311；ordinary868同输入坐标计数为≤160。
