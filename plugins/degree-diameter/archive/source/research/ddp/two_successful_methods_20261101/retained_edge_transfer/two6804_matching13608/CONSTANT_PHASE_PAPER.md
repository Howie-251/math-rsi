# 两份6804保边＋matching：常数相位偏移的R4计数障碍

状态：纸面推导支持；没有运行卷积、source/field验证、BFS、图生成、solver、Lean或外审。root另行执行的纯整数商gate负责实际系数回执。本文件只用已读source6804 construction/REPORT给定的phase profile，不从6804因式分解臆定模型，也不声称13608/D4候选已存在。

## 给定接口与scope

源有12个C12相位，每相位7·81=567点，共6804。每个顶点的旧邻点相位增量为：±1、±4各有3个邻点，6有1个邻点。因此在整数群环Z[z]/(z^12−1)中，普通单步walk的统一相位分布是

    Q=3(z+z^−1+z^4+z^−4)+z^6。

保留两份源的全部旧边，仅加一个连接两copy的perfect matching M，故若实际源simple13regular，则双copy图simple14regular、13608点。匹配端点可以是任意fibre/deck bijection；本域唯一额外要求是某个固定c∈C12使

    phase(M(x,copy0))=phase(x)+c（copy1）。

逆向自动是−c。这包含任何具有常数相位偏移的rightshift以及任意层内affine/更一般bijection，不要求M是源图automorphism。

## 1. 跨copy长度≤4的最短路只有一次cross

每条旧边留在同copy，matching边交换copy，所以跨copy路的cross数为奇数；总长≤4时只有1或3。若有3cross，至多有1条旧边。三个cross之间的两个间隔不可能都含旧边，因此有两个相邻cross。

perfect matching中从一个点跨出去后，再立刻cross只能沿同一matching边回来。这两步是回退，可消去，既不改端点也不增长长度。故任一≤4跨copy可达点都有恰一次cross、至多3条旧边的路线；最短路本身不可能保留这样的相邻回退。

这里没有把M与旧步交换顺序，也没有假设rightshift/affine关系。若新增连接不是perfect matching，连续cross未必回退；那是另一个scope，本证明不适用。

## 2. 指定root相位j+c的walk数与fibre映射无关

固定root在copy0、phase j，考察copy1中phase j+c的567个target。一次cross路线写成a条旧步、cross、b条旧步，a+b=l≤3。若prefix旧相位增量s，则cross后相位是j+s+c；要到目标phase，suffix增量必须−s。

统一的Q row-profile意味着：从任意实际顶点出发，长度a旧walk的phase增量s个数是[Q^a]_s；这仅由逐步相位邻点数递推，不需要fibre公式。对每个具体prefix endpoint，M把它送到相位j+s+c的某实际顶点，从那里长度b旧suffix增量−s的个数仍是[Q^b]_(−s)。因此固定a,b的路线总数恰为

    sum_s [Q^a]_s [Q^b]_(−s) = [Q^(a+b)]_0。

M在该相位内怎样置换567个点，不改变这个计数。它可能造成更多路线落到同一target，只会减少distinct可达target，不会超过walk数。

长度l旧步有l+1个cross位置，故所有≤4跨copy路线在这个target class中的distinct images至多

    U=[sum_(l=0..3) (l+1)Q^l]_0。

这不是非回退或简单路的精确数量：Q普通walk允许旧边回退、重复点与多路碰撞。但它们都是合法上界的额外计数；最短跨copy路已被一次cross分类覆盖。因此无需旧NB/field/rank计算，不能因这些重复而怀疑上界漏掉真实短路。

## 3. root的整数系数预测给出严格缺口

root事前给出待其实际商gate绑定的系数 `[Q²]_0=37`、`[Q³]_0=54`；另Q无零相位单步，Q^0有一个零步。代入上述式子为

    U=1+2·0+3·37+4·54=328<567。

本文不独立运行卷积或把root尚未保存的numeric标成已验数据；结论可按该显示代数式由root整数回执直接绑定。其数学后果是每个copy0 root至少有239个对面phase j+c target不在R4；copy1 root用逆offset亦同理。

所以一旦给定Q/profile与该小整数式绑定，整个常数相位偏移perfect-matching族均不可能D≤4。不能继续在同c/不同c的deck h、fibre affine参数或层内随机置换上寻找D4：它们全在这个已排计数域内。

若源D≤4也已继承，则任意cross target可先沿matching一步，再在另一份源走≤4步，整个双copy图D≤5；结合上述缺口，常数offset族实际只能D5而非D4。这是条件纸面距离说明，不是实际新图生成、验收或record声明。

## 4. 停止和未排范围

改变相位匹配为非平移permutation π 时，prefix相位j+s跨后成为π(j+s)，不再是j+s+c；同一[Q^l]_0推导不成立。这里不自动排其它phase π，更不排一般13608点14/D4图、多条cross边、改旧边或其它source。

当前定位主表14D4为9720仅作root已查背景，13608不是已生成合法candidate或全球新纪录。负结论只指导下一机制须实质改变phase匹配；本paper不枚π、不续fibre参数、不启动第二群/域或独立模板，完成即停。
