# (7,8)264440→282040：LEFT law与CRT迁移证明

本文件仅核配方和代数，读取既有source与controller缓存，不重新算order/constants、不枚词、不构图、不BFS。实际源见 [AUTHOR_construction.json](AUTHOR_construction.json)、[AUTHOR_README.md](AUTHOR_README.md)。

## 真实literal及目标规则

源群为 F6611 normal与C40的semidirect product，6611=11·601、action193，采用AUTHOR的LEFT坐标(normal,phase)：

(n,I)(m,J)=(n+r^I m,I+J)。

三正元为(1,4),(4755,9),(2638,6)，另h=(0,20)。source h已normal0，首正元normal本身为1，无需再做坐标gauge。这里与上一轮RIGHT convention不同，不可复用错误的normal更新方向。

source小算术已确认action在mod11、mod601、全mod6611的阶分别为10、40、40；193^20=3004是CRT(+1,-1)，不是全环-1。source normals分解为mod11 [1,3,9]、mod601 [1,-53,234]。

目标仅换601到下一兼容素数641，保C40及mod11 action6/normals[1,3,9]，field641保同一冻结整数向量[1,-53,234]。目标N=11·641=7051，群阶282040。CRT full normals为[1,2511,1516]，这些值由source owner的receipt给出，本分析未重新求值。

## 真逆、involution及七正则

LEFT真逆为

(n,I)^-1=(-r^-I n,-I)。

代入可得左右乘积都为单位；producer必须从每个目标正元形成此真逆，不沿用旧source的inverse数字。

任一exactorder40的field action α 满足α^20=-1，但mod11的6^20=+1。所以h20在440商群中中央，在field核上反演；两者不能混写为globalaction20=-1。由于h normal0且phase20，h²为单位，h不是单位。

三个正phase为4、9、6，inversephase为36、31、34，加20一共七个不同非零phase。因而所有这些目标模型都是simple七正则，无需从normals偶然不重合推出度数。

## 投影onto440和新field连通

记Q=F11⋊6 C40，大小440。投影的g1=(1,4)、g2=(3,9)已经生成Q：在mod11中6^4=9、6^9=2，LEFT乘积g1g2、g2g1的normal分别为6、5，而phase相同。因此

(g1g2)(g2g1)^-1=(1,0)

是pureF11 translation。g2的phase9生成整个C40，故投影ontoQ。[controller缓存](controller_capacity/RESULT.json) 又独立给全部440槽raw≥4964，支持同一投影绑定；本分析没有重枚这些词。

目标纯field核K为F641。对h=(0,20)和某个正元g=(b,j)，hg与gh的Q部分完全相同，而field部分分别为-b和b。因此

[h,g]=(hg)(gh)^-1

为纯field translation -2b。首元field b=1，所以这个元素非零；641是素数，它生成全K。目标生成子群含K并投影ontoQ，因此为整个282040阶群。这里没有将source或商群连通错误地当作新field连通，K的生成已单独证明。

## 16个actions与覆盖结论的边界

641-1=640，exactorder40 roots共有φ40=16个。可用α^40=1、α^20≠1、α^8≠1判定exactorder40。本轮固定完整测试这16个embedding，不是沿用上一轮order6的两个根。

抽象群的phase重标通常改变这组固定phase、本轮CRT11分量或normal attachment；没有额外等价证明时，不可省略primitive roots。本文件不声称16项是不同图同构类，也不把它们当16种构造方法。

source中两个endpoint表达式的mod601碰撞，不必在mod641下保持；一个primitive embedding的失败也不自动排其它embedding。只有普遍整数／cyclotomic恒等式才支持这种统一外推。此次规则只是fixedphase、fixedmod11及fixedfieldnormal三整数的受控迁移，不是全部自由normal或所有degree7 Cayley集合。

NB≤8 controller prefix总2351462、最薄槽4964≥641，仅为必要容量，不是field端点全覆盖。真实Cayley左平移在全目标上传递，实际identity完整BFS的ecc才给全局直径；本paper不提供目标D8成功，也不填写全图普通坏对。

本分析新增word枚举、graph、BFS、solver均为0；源码/producer独立记录数值终态，可把本证明并入同一family row。
