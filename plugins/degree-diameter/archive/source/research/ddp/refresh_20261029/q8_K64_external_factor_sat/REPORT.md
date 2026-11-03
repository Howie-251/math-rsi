# q8辅助图的跨pencil二因子完整模型未决

研究目标是Rajiv Theorem1点名未解决的q8、13度纤维构造：辅助K64若含8个pencil Q3、最大度5且D≤3，则产生1088点13度D3主图。2026-10-29新查Comellas主表(13,3)为972。作者已有3regular gadget的1088/14，不称原作者没试。

固定仿射J5⊕I1的3840三元S类已经完整失败。本批未换A/seed，而是让全部1792条跨不同pencil的额外边自由共同选择，各vertex额外度恰2。允许额外边在同pencil内部的更大范围不在本模型中。

## 规范化保留的完整范围

若每个vertex的两个额外邻点都在同一个目标pencil，则一条E边跨A到B后，B端的下一条E边必回A。对任一root，三步以内的外pencil目标最多为：E/EI/EII/EEE全部在同一目标pencil，合至多8；IE/IEI至多3×2×4=24；IIE中非回退cube两步只有3终点，至多6；EIE至多12。IEE/EEI回源pencil。总至多50，小于必需56。因此D3图必有两个外邻点处于不同pencil的vertex。

重标pencil并在三个相关cube内分别平移，可令该vertex为0、两邻点为8和16。故固定(0,8),(0,16)不漏本跨pencil二因子域。独立代理只读核对了此计数及规范化。

## 编码与实际执行

1792无向edge变量，degree exactly2用非空+每个已选边需另一已选边、前缀atmost2共同编码。R2由实际直接邻接或任一中介二步的完整等价门定义；每个跨pencil无序对要求R2(u,v)或Adj(u,w)且R2(w,v)，覆盖所有≤3路径。同pencil的固定Q3已保证D3。总197152变量、684450子句、1792目标对。

一次CaDiCaL-t90返回UNKNOWN/code0，childCPU90.043175、driverCPU0.93266972、aggregate90.975846255秒。没有辅助正图、没有1088点主图、没有生产allroot验收。独立代理只读检查了exact2、Tseitin双向性和R2/R3量词，没有追加SAT或数值运行。

所有作业终态。这个完整模型仍未解决，不自动续timer/邻居case，不把UNKNOWN排除一般辅助K64或q8主构造。原104目标图/4参数、confirmed103/3、Lean1及3750最新全球纪录pending均不变。
