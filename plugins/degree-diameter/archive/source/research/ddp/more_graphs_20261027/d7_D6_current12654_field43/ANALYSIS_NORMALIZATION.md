# (7,6)12654→14706：CRT与projective规范化

**结论：指定两action、每action1893项的规范化完整，全部非零项simple七正则且连通。** 本文件只核配方和代数，不枚词、不构图、不 BFS；producer的数值终态另记，不以连通性或raw容量代替D6覆盖。

## 源绑定与两种乘法

官方D6页给 C18⋉85 Z703，RIGHT law为
(x,n)(u,m)=(x+u,n·85^u+m)，
三正元(17,397),(13,486),(10,188)，另h=(9,0)。

[作者recipe](AUTHOR_construction.json) 与 [README](AUTHOR_README.md) 用LEFT坐标(normal,phase)，正元为(1,1),(24,5),(289,8)。这不是冲突：映射

ψ(x,n)=(n·85^-x,-x)

把RIGHT群同构到LEFT群 (b,j)(d,k)=(b+85^j d,j+k)，并逐项把上述官方正元送到作者正元，h不变。只读取了287-byte配方、1684-byte README及官方说明，未下载完整源图或重验旧BFS。精确来源见 [SOURCE_BINDING.json](SOURCE_BINDING.json)、[PRIMARY_RECEIPTS.json](PRIMARY_RECEIPTS.json)。

## CRT与具体actions

703=19·37。85模19为9、阶9；模37为11、阶6。目标换37→43，N=817，阶18·817=14706；43为下一个大于37且为1 mod6的素数。F43中exactorder6的两个根为7、37，CRT合成a=351、123，两者全模817阶18。

关键区别是a9在mod19为+1，在mod43为-1；全模817的a9=343，不是-1。下面所有中心化只在field43分量进行，不能把a9−1当成全环可逆元。

三正元的mod19 normals固定为17、11、17。源mod37 normals为27、5、3，共同乘27^-1=11得到[1,18,33]=[1,18,-4]，故这项parent控制确是源的独立field-scale规范化。所有小算术见 [ANALYSIS_ARITHMETIC.json](ANALYSIS_ARITHMETIC.json)。

## involution中心化无损

目标群中phase9 involution的mod19 normal必须为0，field43 normal h可任意。RIGHT law下，translation共轭

(0,c)(j,b)(0,c)^-1=(j,b+(a^j−1)c)。

选择c19=0、c43=h/2，则phase9 field normal变h−2c=0，而所有mod19 literal保持不动。field中心唯一；这不声称全CRT环上的中心唯一。原三正元field normals任意，中心化后仍给任意三元组(b1,b2,b3)，没有丢失设置。

## 共同scale与1893项

对任意s∈F43*，变换phase及mod19坐标不动、field normal乘s，是群自同构。其CRT整数乘子满足k19=1、k43=s，因此不改变固定19分量。h=0也保持。

全部非零field三元组在共同scale下恰有唯一首个非零坐标为1的代表：

(1,b,c)：43²=1849项；
(0,1,c)：43项；
(0,0,1)：1项。

合计1893/action，两action合3786个规范settings。这里是对上述共轭及field-scale的完整商，不声称每项代表不同图同构类。全零项排除有理由：field从identity永远保持零，不能覆盖43个normal状态。

真逆必须沿固定RIGHT law形成：(-j,-b·a^-j)。共轭、共同scale是群自同构，均与真逆相容；不能将source旧inverse数字当新field值。

## 非零三元组的连通证明

342阶投影Q=C18⋉9 F19的 [controller结果](controller_capacity/RESULT.json) 已独立得到全部342槽raw count≥152，所以投影生成全Q；这里不借旧source全图BFS证明新field连通。

设H为目标生成子群，K=F43为纯field normal核。phase9的h=(9,0,0)在Q中央，因为9^9=1，却在K上作反演。对某个field normal b≠0的正元g，其hg与gh具有同phase、同19分量，field部分分别为b与-b。因此

(hg)(gh)^-1

是一个非零纯F43 translation，其值为2b·r^-(j+9)。因43为素数，它生成全K。H已含K且投影ontoQ，故H等于整个14706阶群。每个规范非零三元组都有这样的g；没有误把342投影连通当成field自动连通。

## 合法性及实际范围

七个dart的phase为17、1、13、5、10、8、9，互异且非零。三正元不自逆，phase9元是非平凡involution，因此每个setting都simple、七正则。Cayley左平移在全图传递，实际identity完整BFS的ecc才等于全局D；raw≥152只给每43状态槽的必要容量，不给完整覆盖。

本paper核对新增wordscan、图、BFS、solver均为零。完整source/proof范围仅是固定mod19 action/normal、固定C18 phases、两exact6 field actions及三free field normals的这一族，不涉及其它phase、19分量、field或degree7全部Cayley图。
