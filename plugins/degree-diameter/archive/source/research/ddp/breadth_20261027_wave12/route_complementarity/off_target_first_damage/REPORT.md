# 首个off-target损坏：self路线0123丢失唯一补点5

字典序第一对“旧图≤4、新矩阵图>4”的完整fiber顶点为 **(0,5)**，即同一controller fiber0内的向量0和5。旧完整路线缓存证明其距离恰4；新root距离缓存给5。无需旧/新BFS，也没有分析第二个受损槽。

## 全部路线及直接原因

controller slot0→0共有33条长度≤4walk：长度0一条、长度2四条、长度4二十八条。全部原、新rank、完整线性像、可控列、total linear map及选定输入漂移逐项保存在 `RESULT.json/routes`，包含立即回退，不只取最短路。

旧图只有word **0123** 覆盖目标向量5，实际controller路线为0–18–67–18–0。

| 项目 | 旧图 | 新T/b协调图 |
|---|---|---|
| 0123 controllable columns | [8,13,13,8] | [8,12,12,8] |
| rank | 2 | 2 |
| 线性像 | {0,5,8,13} | {0,4,8,12} |
| total linear map | I | I |
| 输入0的漂移 | 0 | 0 |

因此问题不是旧rank4路线降秩，也不是总线性漂移改变。该rank2路线的方向转了：旧唯一补到的5消失，新补入的4和12已由别的路线覆盖，产生冗余覆盖。旧33路线并集为全部16点，新并集为15点，恰漏5。

另一个确实变化的闭路线是0213，路径0–18–8–18–0：列从[8,9,9,8]变为[8,8,8,8]，rank2降至rank1，像从{0,1,8,9}缩为{0,8}。但它丢掉的1、9仍由其他路线覆盖，并不是最小点对(0,5)失效的直接原因。其余31条route的线性像及total linear map都不变。

## 为什么保持reverse-b还不足以保护原self覆盖

协调变更把第一条边的A改为A'=S*A、b改为S*b，使A'⁻¹b'仍为8，故简单外出/反走的方向保持。可是0123还运输了neighbor18处的B-return方向B⁻¹b_B=11：

`A⁻¹*11=13`，`A'⁻¹*11=12`。

于是nested backtrack像从span{8,13}变为span{8,12}，虽rank仍为二，却失去原self覆盖中不可替代的点5。全部33条self路线的word均free-reduce为空，且每次相邻逆label实际沿同一控制边反向，故不仅数值total linear map为I：任意逐边inverse-consistent affine offsets的确定性composition也严格为identity、闭合offset为零。branch参数生成的方向像不依赖offset。因此对任意source fiber向量x、任意这种offset，整体像均是上述并集共同平移x；新图在fiber0中恒且仅漏x XOR 5。该单槽因此损失8个无序self点对，offset无法修补固定当前T/b的这项损失。

这给出了下一规则的具体承重对象：除了保留全部468个unique4槽和简单return方向，还要保护原来由多个低rank nested-return像拼出的覆盖，尤其是各路线的唯一贡献。只检查每条rank不变或reverse-b不变仍会放过本例。此处没有据此执行新变更或优化。

## 范围与文件

定位按完整顶点对i<j的字典序，只对新缓存中距离>4的项查询旧cached route algebra；第一项即(0,5)。`RESULT.json`包含该完整字典序证据、33条全路线以及两条变化路线。`diagnose.py`是此单槽只读分析，既不构建候选图，也不调用BFS。

root已有整体结果由本报告复用：旧D5/12384坏对，矩阵协调变更D5/12800；目标0→10已完全修复，468tight槽全部保持。这份单槽诊断解释一个真实off-target损坏机制，不把8个self损失归作全部净增416坏对的完整账目。未扫描全受影响槽、其余1023个passer或新候选。
