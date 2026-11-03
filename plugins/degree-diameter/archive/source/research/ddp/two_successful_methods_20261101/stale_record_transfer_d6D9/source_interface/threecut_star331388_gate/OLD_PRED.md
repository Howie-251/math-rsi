# 三cut六星的完整旧路线义务门：事前预测

沿同case cap20CPU，继承2.511387697，新准备计0.25；唯一compile/run，含父子CPU与失败输出，不重BFS/DP/sourceD9/field/F6959。只读取PROFILE的d/c、sphere4与三critical关系。

可推翻预测：对每个首canonical positiveedgeclass，另外两条与它顶点不交的源旧边，其四个pins不能覆盖该首cut的全部critical(u,v)义务。每个义务需要某pin在B3(u)或B3(v)，因为本cut两pins对该对均为distance4；否则新old-old距离恰10。全部三个firsttypes无解才完整排fixedsource minimal3cut6star。

使用cached d<=3导出B3标签，对每个criticalpair将u*B3、v*B3的每个vertex置相应bit。所有正向源edge{h,h*s_k}的mask是两个端点vertex masks的OR。全扫描3*N=994161旧edge参数，**先**剔除任一端点为firstcut的0或s者，再group mask/count/前12条不同undirectededge代表；实际有效pool应为994150。

完整保留zero class、允许same-mask class自配，但两真实edges必须不同且四端点互斥。任意固定edge的两端最多触及11条源边，所以一类有至少12条时，其任意12个distinct reps必含一个与固定edge不交者；小类全保。这个压缩只对mask union+disjointness的存在性完备，不对后面的newroot或其它cut义务一并完备。

每firsttype完整查mask-pair OR=ALL及代表disjointness；若找到仅取首真实triple，核一次cached完整M平移交/newrootR9和其它两cut的translatedcritical义务，保存首反例；不得因其失败继续选第二triple或宣布该mask类无解。过滤全过也不证明全D9，不生成331388，不扩fullseam/normal搜索。
