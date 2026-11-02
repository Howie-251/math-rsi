# External边的五条短路共用中间点闭包

这是纸面核查，不构图、枚举3750点路径或运行BFS/SAT。源固定为成功F5字面图及其C30 controller。C30每个点恰有两条external边，external边不在三角形内，且C30无四圈。

取有向external控制边u→v，出端口p；取u的另一端口q≠p。令r=inv(p)、s=inv(q)。对u-fiber坐标w，定义

    L=(w+span(ell_q))去掉w，4点；
    Y=N_p(w)={T_p w+beta ell_r}，5点；
    Z=N_q(w)={T_q w+gamma ell_s}，5点。

## 路径集合恰为五条

任取x=w+t ell_q∈L，t≠0，及y=T_p w+beta ell_r∈Y。因为T_p ell_q与ell_r独立，

    y−T_p x = beta ell_r−t T_p ell_q

不在edge line方向ell_r，所以x、y不直接相邻。external控制边没有共同邻控制点，故也无两步源路径。C30无四圈，故任何长度3控制walk只能前/后回退。

相对于起点x，y恰落在first-q的前回退平面span(ell_r,T_p ell_q)的exclusive部分。成功六平面pencil中该部分不属于其它五个平面。因此所有源长度≤3路径的控制投影只能是u→C[u][q]→u→v。

设该路线回到u-fiber的中间点为w'。前两步迫w'∈x+span(ell_q)=w+span(ell_q)；最后一步又迫y−T_p w'∈span(ell_r)。方向独立使w'=w。

又T_q ell_q=ell_s，所以N_q(x)=N_q(w)=Z。每个z∈Z都给出且只给出一条源路径

    x — z — w — y。

全部5条路径均共享w，另一中间点遍历Z。这就是完整的≤3路径集合，而不是只选出的5条见证；路径长度恰3。

## 保留闭包与压缩

对任一诱导保留集，若L和Y各至少保留一点，则对应保留端点的D3要求恰为：w保留，并且Z至少保留一点。令O_L/O_Y/O_Z为各集合的保留OR，得到两个必要（对此Cartesian端点类也充分）的clauses：

    keep[w] ∨ ¬O_L ∨ ¬O_Y；
    O_Z     ∨ ¬O_L ∨ ¬O_Y。

这里必须排除x=w，否则它与Y直接相邻，不能要求经过Z。也必须要求控制边external，否则可能有三角形两步路径；q=p同样不满足exclusive论证。

这捕捉了“多条最短路虽不唯一，但全部共享一个中间点”的结构，不属于单纯独立选择一条测地路的规则。旧258规则只从唯一distance3控制词产生；本对端点的控制投影是回退词，故并未由那类模板直接编码。没有声称新clauses在完整旧松弛中全部逻辑独立。

## 规模与门绑定

60个ordered external darts、3个q、125个w，共22500组，产生45000个上述闭包clauses。每个(u,q,w)都出现，O_L为15000个不同OR4；不同w的同一五点线删除不同中心，得到不同四点集。Y、Z都是既有四方向五点线，可以复用原3000个OR5 flags。

45000只计闭包clauses。若新OR4使用标准exact iff绑定，每个另需5条clauses，15000个共75000，所以新增总量为15000 flags、120000 clauses。不能创建OR4变量却遗漏绑定；若省略某向定义，须另证投影等价。

本引理不要求三角形沿port0/1，不假定cycle holonomy为恒等，也不增加新的controller或域。没有在本目录启动新的保留模型或续旧timer。
