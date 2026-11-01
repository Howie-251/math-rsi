# 二十五点至少十七个六度点具有Property B

## 定理与状态

**定理。** 设H为25点上的35条互异五元边，覆盖每个不同点对。若
$$
r=|\{z:d_H(z)=6\}|\ge17,
$$
则H具有Property B，即存在顶点的Bool染色，使每条原边均含两种颜色。

这是该完整子支的纸面证明。r≥18部分及r=17新增收尾均已获Gemini有效静态审阅，Grok的新范围审阅在途；主代理与Sol已核对原H的完整连接。没有据此验收整个25点分支或m(5)≥36，也没有新增Lean。精确依赖和审阅范围见末节。

## 1. 共同低点性质与已有全低边定理

记L为实际六度点集。对任意z∈L，点对覆盖给λzy≥1，而
$$
\sum_{y\ne z}\lambda_{zy}=4d_H(z)=24.
$$
共有24项，所以每项恰一。因此六条z星边删z后，把其余24点划分为六个四块；任何涉及低点的点对共度均一。

[全五低原边定理](TWENTYFIVE_FIVE_LOW_EDGE.md)§1–4已证明：若H存在G⊆L，则H可染。该稿§5还证明r≥18必存在这样的实际G：r≥20由低迹共同矩得到；r=18、19由逐低点六星的整数缺陷得到。因此r≥18全部由该定理覆盖。

以下只须处理r=17。若存在全五低原边，仍直接调用同一定理。**并不声称r=17必存在全五低原边。** 以下反而完整处理不存在这种边的情形。

## 2. 无全低边时，每个低点只有两种入射型

固定r=17并假设每条原边e都有ℓ(e):=|e∩L|≤4。对任意低点z，其他16个低点与z各共边一次，故
$$
\sum_{e\ni z}(\ell(e)-1)=16.
\tag{1}
$$
这六个非负整数各至多3，总缺陷为18−16=2。因此z的六条入射边仅有两种可能：

* pair型：一条低迹大小2，其余五条低迹大小4；
* triple型：两条低迹大小3，其余四条低迹大小4。

低迹大小1会单独产生缺陷3，故不可能。每条含低边都包含某个实际低点，所以全H的非零低迹大小只有2、3、4。

## 3. 整除性迫八名pair型与九名triple型

令p为pair型低点数，nᵢ为低迹大小恰i的原边数。按同一原边的低点关联计数得
$$
2n_2=p,\qquad 3n_3=2(17-p),\qquad
4n_4=5p+4(17-p)=68+p.
\tag{2}
$$
于是0≤p≤17，且p为偶数、p≡0(mod4)、p≡2(mod3)，唯一可能是p=8。因此
$$
n_2=4,\qquad n_3=6,\qquad n_4=19.
\tag{3}
$$
含低原边共29条，剩余6条全高；triple型低点恰有9名。这里“高点”仅指其余8个非低点，没有另设高点度数上限。

## 4. 高点对的共度上界来自互不相交低迹

固定不同高点x,y。令a为含xy的含低原边数，b为含xy的全高原边数。

a所数的边只可能低迹大小2或3：低迹大小4的五边仅有一个高点。这些共同边的低迹两两不交；否则某低点z在两条含xy边中出现，使λzx≥2，违第1节。故其低迹总大小至多17。

全H只有四条低迹大小2的边。若a≥8，取其中八条，其低迹总大小至少
$$
4\cdot2+4\cdot3=20>17,
$$
矛盾。因此a≤7。又b≤6，得到所有高点对均满足
$$
\lambda_{xy}=a+b\le13.
\tag{4}
$$
此处控制的是同一批共同边中互不相交低迹的总大小，没有把低点关联数误当成共同边条数。

## 5. triple型低点的宏星量至多二十四

取第3节保证存在的任一triple型低点z。两条低迹大小3的星边各含两个高点，四条低迹大小4的星边各含一个高点。因此六个实际link四块Q₁,…,Q₆中的高点数为
$$
2,2,1,1,1,1.
$$
八个高点各出现一次。块内点对中，仅有两对由两个高点组成；其余点对均涉及低点，共度超额为零。

[宏星染色门](TWENTYFIVE_MACRO_STAR_COLORING.md)对25点／35简单五边／pair-cover和任意实际六度中心z，定义
$$
W_z=\sum_{f\not\ni z}\sum_i\binom{|f\cap Q_i|}{2}
   =\sum_{xy\text{同一}z\text{块}}(\lambda_{xy}-1),
$$
并证明Wz≤25即H具有Property B。由(4)，当前同一个z满足
$$
W_z\le2(13-1)=24\le25.
$$
因此该门给出原H的proper二染色。r=17的有／无全低边两种情形及r≥18均已覆盖，定理得证。∎

## 6. 精确依赖与审阅范围

* [TWENTYFIVE_FIVE_LOW_EDGE.md](TWENTYFIVE_FIVE_LOW_EDGE.md)：仅调用其全五低G⇒原H染色，以及r≥18⇒存在全五低G。所用20点两划分局部引理的完整264轨道主算、独立逐点染色核验和root重编重放，详见该稿§2、6。
* [TWENTYFIVE_MACRO_STAR_COLORING.md](TWENTYFIVE_MACRO_STAR_COLORING.md)：仅调用W的实际点对表达与W≤25染色门；不需要全λ≤2，也不需要该稿的平交或六型精细门。
* [r=17独立短证](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/R17_MACRO_GATE.md)：与本稿§2–5相同的原H推导；没有新增枚举或计算进口。

[全低边Gemini回应](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/GEMINI_FIVE_LOW_RESPONSE.json)及[r=18、19补审回应](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/GEMINI_R18_R19_RESPONSE.json)已有效返回，均为静态审阅，未执行程序。r=17另由[第三轮新回应](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/GEMINI_R17_RESPONSE.json)有效静态核查，并明确将旧宏星门作为进口；不是把前述r≥18回复扩大。root／Sol审阅保留same-family／provisional，Gemini为独立家族的静态意见。Grok新scope在途不记为已完成。整体目标的其他开放输入仍需各自证明。
