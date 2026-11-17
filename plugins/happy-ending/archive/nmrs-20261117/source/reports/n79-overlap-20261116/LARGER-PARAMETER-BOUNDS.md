# 更大参数的现用工作上界登记

2026-11-16。现用平面强迫工作上界为八边形319、九边形1148；十参数237是受限容量。本页汇总现有原件，逐项取本研究已记录的较强结果；不启动新推导、求解、重放或独立审阅，不认证公开最佳纪录。正文中的旧阶段数值仍保留在原稿，现用数值以本页所指的最终章节及计算回执为准。

## 2026-11-17 八、九边形上界对照

| 平面强迫阈值 | 文献及已公开定理的组合 | 项目现用工作上界与证据层级 |
| --- | --- | --- |
| $ES(8)$ | Schroeder 2026预印本明确给出319 | $193+124+2=319$；193／124来自公开有限数据加项目signotope迁移，完整迁移待独立审阅，不认领新的平面数值。 |
| $ES(9)$ | Mojarrad–Vlachos明确给出1508；此前核验的已公开定理组合另给1501，后者不是原论文印出的数值 | $688+458+2=1148$；有限整数证书已在Linux检查通过，实际配置到证书行及完整装配推导仍待独立审阅。 |

八、九边形共23行的文献基线、组合推论、原始工作文件及认证边界见[逐项核对说明](../n7-progress-talk-20261117/BOUNDS_AUDIT.md)，其中22／29是Baek文献已给出的精确值。这里只登记此前核验，不作全行最优性、原创性或公开检索完整性结论，不启动新数学工作。

## 1. 对象、单位与保证状态

$N_{\rm sig}(m,r,s)$ 是完整有序 rank-3 signotope 中，同时禁止蓝 $r$ 点路径、红 $s$ 点路径及 weak $m$ 的最大避免人口；路径长度按顶点数。weak $m$ 要求同一对实际首末点的异色路径，其顶点数和为 $m+2$。写 $U_m(a,b)=N_{\rm sig}(m,a+2,b+2)$，状态目录大小为 $\binom{a+b}{a}$。原定义、实际 pair 标签和坐标删除接口见 [PROOF §1](PROOF.md) 及 [坐标删除原稿 §7](../n78-row-compression-20261115/PROOF.md)。

令 $C_m=N_{\rm sig}(m,m-1,m-1)$，$Q_m=N_{\rm sig}(m,m-1,m)$，$F_m=N_{\rm sig}(m,m,m)$。真实双侧残余 $D_m$ 额外满足原 R7 的 junction 条件，不能用一个普通容量的名称替代。原 [R7 §8.4](../../.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) 与 [R20 合法 chart 接口](../../.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) 给出

$$Q_m\le C_m+D_m,\qquad F_m\le Q_m+1,\qquad ES(m)\le F_m+1.$$

最后一项是实平面一般位置点集的凸 $m$ 边形强迫阈值；几何子类包含关系和“避免人口再加一”必须保留。受限容量 $N_{\rm sig}(m,r,s)$ 本身不是 $ES(m)$。

未逐行列出的小帽区域沿用经典精确容量：当 $2\le r,s\le m$ 且 $r+s\le m+3$ 时，weak条件自动，有 $N_{\rm sig}(m,r,s)=\binom{r+s-4}{r-2}$，例如 $N_{\rm sig}(8,5,6)=35$；换色可交换 $r,s$。该基线的对象及适用域见 [N7策略综合 §1](../../.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRATEGY_SYNTHESIS_20261116.md)，不将未列出的参数误作没有上界。

下表所记自主解析结论均是完整工作证明稿，仍为同会话、未独立外审、未正式接受；“自主”表示没有调用 Schroeder 的193／124有限树，仍保留 Baek 短帽等注明的基础文献进口。原生整数证书已由另写程序在 Linux 精确重建并 PASS，已重放范围为有限证书的支持及整数算术，接回原输入的数学接口仍见纸面证明，整体仍未外审接受。八边形193／124则是公开有限数据实际重放加本项目新 signotope packet 桥的进口型工作结论，新桥尚未独立审阅；有限 checker PASS 不等于全链 Lean 或独立验收。本轮整理不改变这些状态。

七边形仅作对照：$N_{\rm sig}(7,5,7)\le39$ 的完整解析工作证明见 [owner 原稿 §§7.5、7.7](../n7-owner-intervals-20261116/PROOF.md)，仍未独立接受，38尚未证明。

## 2. 八边形：受限子参数与两个最终出口

### 2.1 普通受限容量

| 对象 | 现用工作上界 | 原件与实际依据 |
| --- | ---: | --- |
| $N_{\rm sig}(8,4,8)$ | 22 | [CASCADE-63 §2](CASCADE-63.md)：Baek Theorem 2.7 的 ordered-configuration 短帽进口 |
| $N_{\rm sig}(8,5,7)$ | 51 | [THREE-COLUMN-STRICT §§1、6](THREE-COLUMN-STRICT.md)：全参数严格一洞加强 |
| $N_{\rm sig}(8,6,6)$ | 63 | [FIVE-ACTIVE866 §6](FIVE-ACTIVE866.md)：六洞全类型排除接回任意原输入 |
| $N_{\rm sig}(8,5,8)$ | 66 | [坐标删除原稿 §8](../n78-row-compression-20261115/PROOF.md)：由22的含坐标切片双计数 |
| $N_{\rm sig}(8,6,7)$ | 109 | [PROOF §§2—7](PROOF.md)：126态至少十七洞，完整排除十六洞边界 |
| $N_{\rm sig}(8,6,8)$ | 165 | [坐标删除原稿 §8](../n78-row-compression-20261115/PROOF.md)：由66双计数；真实残余124不替代本普通容量 |

### 2.2 普通平衡容量、真实残余与平面阈值

| 对象 | 公开有限数据＋新抽象迁移 | 自主解析线 |
| --- | ---: | ---: |
| $C_8=N_{\rm sig}(8,7,7)$ | 193 | 198 |
| 真实 $D_8$ | 124 | 126 |
| $Q_8=N_{\rm sig}(8,7,8)$ | 317 | 324 |
| $F_8=N_{\rm sig}(8,8,8)$ | 318 | 325 |
| 平面强迫阈值 $ES(8)$ | 319 | 326 |

左列的原输入连接见 [EIGHT-CYCLE-TRANSFER §§1—8](EIGHT-CYCLE-TRANSFER.md)，尤其 §2 的新 packet 桥、§4 两个状态宇宙、§5 的23个 Baek 块及 §6 整数树。真正公开原件为 [octagons.tex](../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/octagons.tex) 与 [certificate README](../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/certificates/README.md)；本项目实际重放范围和信任边界见 [OCTAGON-SOURCE-RECEIPT §§3—5](OCTAGON-SOURCE-RECEIPT.md)，原始 [replay receipt](octagon-source-replay/replay-receipt.json) 与 [finite result](octagon-source-replay/finite-result.json) 均记录 PASS。不能从公开几何319反推任意 signotope 上界，也不能把本轮有限重放称为重建 Lean。

作者公开预印本及归档入口见 [Michael Schroeder companion](https://michaelschroeder.ai/research/ErdosSzekeres/companion)；这里沿用本项目已取得、已绑定的原件，不另作线上更新或同行评审状态认证。

右列198见 [CASCADE-63 §1](CASCADE-63.md)，126及完整324／325／326装配见 [EIGHT-LAST §10](EIGHT-LAST.md)，等价详细终稿见 [EIGHT-MOVE §§17—18](EIGHT-MOVE.md)。两列保证分开；本页不将其合成无来源的新证明。

## 3. 九边形：原生证书后的现用结果

| 对象 | 现用工作上界 | 原件与实际依据 |
| --- | ---: | --- |
| $N_{\rm sig}(9,4,9)$ | 29 | [平移行原稿 §9.3](../n78-shifted-rows-20261116/PROOF.md)：Baek Theorem 2.7 短帽进口 |
| $N_{\rm sig}(9,5,8)$ | 78 | [THREE-COLUMN-STRICT §§1、6](THREE-COLUMN-STRICT.md) |
| $N_{\rm sig}(9,5,9)$ | 96 | [平移行原稿 §9.3](../n78-shifted-rows-20261116/PROOF.md)：$\lfloor10\cdot29/3\rfloor$ |
| $N_{\rm sig}(9,6,7)$ | 117 | [GRAPH §§2—5](GRAPH.md)：八洞共同覆盖全排 |
| $N_{\rm sig}(9,6,8)$ | 185 | [TRANSFER-NEXT §§5—10](TRANSFER-NEXT.md)：23洞及全部24洞分支全排 |
| $N_{\rm sig}(9,7,7)$ | 222 | [NINE29.md](NINE29.md)：29洞边界排除 |
| $N_{\rm sig}(9,7,8)$ | 380 | [PROOF §9.3](PROOF.md)：462态至少82洞 |
| $C_9=N_{\rm sig}(9,8,8)$ | **688** | [原生整数证书 RESULTS：Final working upper bounds](direct-cycle-lp/RESULTS.md) |
| 真实 $D_9$ | **458** | [同一 RESULTS](direct-cycle-lp/RESULTS.md)：582态真实允许宇宙的整数证书 |
| $Q_9=N_{\rm sig}(9,8,9)$ | **1146** | [RESULTS 的 R7/R20 装配](direct-cycle-lp/RESULTS.md)：$688+458$ |
| $F_9=N_{\rm sig}(9,9,9)$ | **1147** | 同一 R20 合法 chart 加一，见 [RESULTS](direct-cycle-lp/RESULTS.md) |
| 平面强迫阈值 $ES(9)$ | **1148** | 几何包含再加一，见 [RESULTS](direct-cycle-lp/RESULTS.md) |

688的924态目录至少缺236态；458的真残余582态目录至少缺124态。最终证书分别只含883、532条正权原生迹，权重分母 $\Lambda=10^6$，超载罚项分别为299、165；精确的 $D-P$ 分别为235971673、123539361，严格超过 $235\Lambda$、$123\Lambda$。原件见 [988紧凑证书](direct-cycle-lp/run-988-d2/compact-certificate.json)、[真残余紧凑证书](direct-cycle-lp/run-d9-d3/compact-certificate.json)、[独立整数重建 checker](direct-cycle-lp/compact_certificate_final.py)，实际成功日志见 [988 standalone](direct-cycle-lp/run-988-d2/standalone-check.log) 与 [D9 standalone](direct-cycle-lp/run-d9-d3/standalone-check.log)。这些证书不用公开循环 catalogue、新 packet 桥或整片容量数值进口。

977的222仍为有效纸面上界；[公开循环特定矩阵 LP 值28](nine-cycle-lift/REPORT.md)只说明该矩阵的分数边界，没有给出221人口上界。真实D9的新458也不改写普通978的380或普通968的185。

## 4. 十参数及更大参数：受限容量族

### 4.1 已记录具体数例

以下均是受限 $N_{\rm sig}$ 的工作上界，不是相应平面 $ES$ 强迫阈值。

基础短帽还可逐参数调用：主会话本轮核读 [Baek v2 Theorem 2.7](https://arxiv.org/html/2206.04260v2)，在本项目常用的 $m\ge8$ 范围给

$$N_{\rm sig}(m,4,m)\le\binom{m-1}{2}+1.$$

这同时包含八参数22、九参数29，并给十／十一／十二参数37／46／56；这些是已核文献定理的公式代入，不冒称本项目另作各参数独立证明。下表三列族的十参数113、十一参数157也注明为已有通式代入，其余具名单例保留原稿出处。

| 原参数 | 现用工作上界 | 原件 |
| --- | ---: | --- |
| $N_{\rm sig}(10,5,9)$ | 113 | [THREE-COLUMN-STRICT 式(1)](THREE-COLUMN-STRICT.md)：$\binom{10}3-7$ |
| $N_{\rm sig}(10,6,8)$ | 198 | [FAMILY §8](FAMILY.md) |
| $N_{\rm sig}(10,7,7)$ | **237** | [TEN-NEXT §§1—5](TEN-NEXT.md)：252态至少十五洞，十四洞取等全排 |
| $N_{\rm sig}(11,5,10)$ | 157 | [THREE-COLUMN-STRICT 式(1)](THREE-COLUMN-STRICT.md)：$\binom{11}3-8$ |
| $N_{\rm sig}(11,6,9)$ | 314 | [FAMILY §8](FAMILY.md) |
| $N_{\rm sig}(12,5,11)$ | 210 | [TRANSLATED-PATHS §5.4](TRANSLATED-PATHS.md)：两个奇度三角分解拒绝，比旧211强 |
| $N_{\rm sig}(12,6,10)$ | 474 | [STRICT-FAMILY4 §6](STRICT-FAMILY4.md)，取代 FAMILY 表中475 |
| $N_{\rm sig}(13,6,11)$ | 689 | [STRICT-FAMILY4 §6](STRICT-FAMILY4.md) |
| $N_{\rm sig}(14,6,12)$ | 970 | [STRICT-FAMILY4 §6](STRICT-FAMILY4.md)；后述新通式此处同值 |
| $N_{\rm sig}(18,5,17)$ | 795 | [TRANSLATED-PATHS §5.3](TRANSLATED-PATHS.md)：取代旧801 |
| $N_{\rm sig}(20,6,18)$ | 4759 | [TRANSLATED-PATHS §6](TRANSLATED-PATHS.md)：取代旧4772 |
| $N_{\rm sig}(26,5,25)$ | 2554 | [TRANSLATED-PATHS §5.3](TRANSLATED-PATHS.md)：取代旧2577及中间2574 |

特别地，1077的237禁止蓝七、红七和weak10；它不是一般避免十边形的人口界，也没有据此得到 $ES(10)\le238$。本次核读的现用原件没有将这些三列／四列族装配成 $m\ge10$ 的新平面数表或新的 general $ES(m)$ 显式公式；已装配的一般出口是第1节的 $ES(m)\le C_m+D_m+2$ 接口，需要另有相同参数下的真实 $C_m,D_m$。

### 4.2 三列族的现用统一式

对整数 $m\ge8$，记

$$n=m-2,\quad b=m-3,\quad p_0=\lfloor n/4\rfloor,\quad
f(p)=\left\lfloor\frac{1+\sqrt{1+24p}}2\right\rfloor,$$
$$P_* =\max\left\{p_0,\left\lceil\frac{\lfloor(b-2)^2/4\rfloor}{3}\right\rceil\right\}.$$

[TRANSLATED-PATHS §5.3 式(7g)](TRANSLATED-PATHS.md) 给出

$$N_{\rm sig}(m,5,m-1)\le\binom m3-
\max\{n-1,\ n+p_0-4,\ n+P_*-f(P_*)\}.$$

其中 $n-1=m-3$ 保留 [THREE-COLUMN-STRICT 式(1)](THREE-COLUMN-STRICT.md) 的严格族，避免用新式覆盖小参数更强旧界；$m=12$ 还应取上述特例210。缺额主项为 $n^2/12-O(n)$，原稿不称最优渐近常数。

### 4.3 四列族的分段最强登记

令 $n=m-2$、$g=\lfloor(m-3)^2/4\rfloor$。[FAMILY 式(2)](FAMILY.md) 给全部 $m\ge8$ 的 $\binom m4-g$；[STRICT-FAMILY4 式(1)](STRICT-FAMILY4.md) 将全部 $m\ge12$ 加强为 $\binom m4-g-1$。八参数特例应另取63，九参数117，十、十一参数分别198、314。

对 $m\ge14$，再记

$$c_n=\begin{cases}n+2,&n\text{偶},\\n,&n\text{奇},\end{cases}
\qquad P_4=\max\left\{\left\lfloor\frac n5\right\rfloor,
\left\lceil\frac{3\binom{n-3}3}{40}\right\rceil\right\}.$$

[TRANSLATED-PATHS §6 式(8)](TRANSLATED-PATHS.md) 给

$$N_{\rm sig}(m,6,m-2)\le\binom m4-g-P_4+
\left\lfloor\frac{12P_4}{c_n}\right\rfloor.$$

此式对 $m\ge14$ 至少保留 $g+1$ 洞，缺额达到 $n^3/80-O(n^2)$；不覆盖 $m=12,13$，它们沿用严格族474、689。FAMILY的“抽象覆盖最优值为 $g$”只描述普通行松弛，不表示这些容量上界有实际 signotope 取等构造。

### 4.4 任意列数的可调用下界

对 $a,b\ge3,m=a+b$，[TRANSLATED-PATHS §§1—5.2](TRANSLATED-PATHS.md) 给非蓝洞数

$$p\ge\left\lfloor\frac{m-2}{a+1}\right\rfloor.$$

若 $b-1\ge a$，还有 $p\ge Q_a=\left\lceil\binom{b-1}{a-1}/a^2\right\rceil$；若 $N=b-1\ge a+1$，可再取

$$p\ge Q_a^+=\left\lceil\frac{\binom N{a-1}\lceil(a+1)/2\rceil}{a\binom{a+1}2}\right\rceil.$$

故总洞数至少为上述适用下界的最大值，并可从 $\binom ma$ 扣除；三列、四列应优先用已连接普通行的更强公式。另一个覆盖更广的基础公式见 [平移行原稿 §4.4](../n78-shifted-rows-20261116/PROOF.md)：当 $a,b\ge2,L=a+b\ge m\ge4$ 时，

$$N_{\rm sig}(m,a+2,b+2)\le\binom La-
\left\lceil\frac{(L-m+1)\binom{L-2}{a-1}}{\max(a,b)}\right\rceil.$$

这些都是从同一实际输入获得的必要缺额，不把覆盖松弛的可行解当作原输入存在证据。

## 5. 失败、方法上限与旧值的使用范围

旧八边327—331、九边1171／1172／1177等只作阶段史，不能盖过上表现用界。D8原生LP只给130，弱于126及进口型124；988深三触240秒HiGHS时限且没有证书，保留成功深二688，不能声称完整框架最优。详见 [RESULTS：Exact stopping point and unsuccessful profiles](direct-cycle-lp/RESULTS.md)。

D9深三全部正需求普通坐标切片原生迹的精确分数可行点总缺额为 $123539833/10^6\le124$，全部47635行已逐行整数复核；结合整数对偶证书，仅证明该纯LP缺额界向上取整恰124。这个分数点不是实际输入，不能证明458可达到，也不排除加入新路径条件或整数分支后的加强。公开977特定2775行矩阵的精确LP值28同样只限制其指定矩阵。

生成上述结果时的最近一次独立深审实际失败且零工具读取，没有数学结论，见 [最新脱敏原收据](../../.aris/review-state/claude-review-deep/evidence/5ec834a4404d429999eb00a76e34025c.json)；backend与effort不可核，未自动重试。本次只整理既有结果，没有发起新审阅。登记、有限算术PASS及独立接受分别保留，未升级任何旧证据绑定。
