# 完整旧路线义务门：固定源的最小三cut六星被排除

预测得到支持，并且实际数据给出比mask-pair搜索更短的容量证书。对三个首canonical旧边类，缓存critical义务分别为32、21、32对。对每个类，都实际流扫描全部994161个positive oldedge参数，**先**剔除触firstcut两个端点的11条边，再将剩余994150条按所命中的义务mask分组。

得到的mask类数分别431、203、419；零mask类完整保留，边数940914、956564、939533。全部类的计数/完整mask/前12条不同真实edge代表写入三个 `OLD_TYPE*_MASK_CLASSES.tsv`。没有把代表层的过滤冒成全域过滤。

决定性结果是：一条额外旧边的两个端点最多分别命中 **11、7、12** 个首cut义务。因此任意两条额外边即使暂不要求互相不交，其总覆盖也至多22、14、24，严格小于所需32、21、32。三个type所有mask-pair都被这一严格上界排掉；实际 OR checks、代表edgepair/disjointness checks均为0。这是完整源edge域的容量证书，不是试过12个代表后没找到。

为什么这些是必需义务：每个保存的critical pair在原图距离9，而且全部九步geodesics穿firstcut。删这个cut后，不管另外两cut在哪里，旧路径都不可能再≤9。firstcut两pins到该pair两端各至少4；如另外四pins均不在任一端的B3里，到六pin集的两距离都仍是4，于是任何经新star的路线也至少4+2+4=10。故每个critical bit都必须由另两旧边的端点命中，无法用“新根已cover”绕开。

完整性范围：任意源旧边都是三positivegenerator代表之一的Cayley左平移；把任意合法三cut方案的一条cut归一化到对应canonical edge，其余两条仍是本次admissible pool中的真实源边。因此三个firsttypes均NO，**完整排除固定actual331387源、恰删三条顶点不交旧边、加一个连接六端点新点的 minimal3cut6star 规则**。不排一般(6,9)、更多cut、额外old-old repair、多helper或换源。

没有首可行triple，所以本轮没有进行新的M交检查、normal选择、其它cut的postfilter或fullseam，也没有候选图。12代表存在性定理已按其前提准备，但本次更强maxbound使它不必进入数值分支；不能声称做过实际disjoint pair检查。所有d/c/B3/critical/M均来自PROFILE缓存，0新BFS/DP/sourceD9或field重验。

compile1.742025CPU、native0.068249CPU，含父进程、准备0.25及继承PROFILE累计2.511387697，case为 **4.575818955/20CPU**。原session17922实际exit0，`OLD_TERMINAL.json`已终态。按授权停止，不normal优化、第二triple或新规则续计。
