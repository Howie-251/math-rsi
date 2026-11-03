# 170基图的signed double cover加vertical：全部签名均为D4

## 结论

固定维护者给出的170点7正则D3图，任意逐边Z2签名作double cover，再在每个fiber加vertical matching，都会得到340点8正则图，但直径恰为4，不能达到目标D3。一个唯一三路见证已经排除全部595位签名，无需搜索符号或做Gaussian。

## 来源和原图核对

项目检索没有发现同一170源与同一signed-lift+vertical范围的既有结果。维护者[Diameter 3页面](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)将(7,3)170图归于Rishabh Rajiv并链接[Zenodo23057003](https://zenodo.org/records/23057003)；本次取该记录的data-and-verification.zip，提取完整`graph_d7_k3_n170.edges.xz`。不把网页上的群结构文字当作本次证明的前提。

原作者边文件为无header的595条零基边，原样存为`source.raw.edges`；`source.edges`按排序边补上170/595 header。逐项确认simple、每点度7，首次且唯一一次170根BFS确认connected、D3，ordered距离分布为0:170、1:1190、2:6840、3:20700。

对全部20700个ordered距离3点对完整枚举NB3走法。由于旧距离为3，所有三步走法都是最短路，不存在可用的回退三步路线。路径数histogram如下：

|NB3路径数|ordered点对数|
|---:|---:|
|1|10260|
|2|8160|
|3|1440|
|4|720|
|5|60|
|6|60|

`distance3_paths.json`保存10350个无序d3点对的全部路径；ordered统计由每个根实际枚举，反向路径无需重复存储。

## 短障碍

每条原边e有任意签名σ_e∈Z2；horizontal边为(u,i)—(v,i+σ_e)，vertical边为(u,0)—(u,1)。

旧距离≤2的点对，沿一条旧最短路并可在末端用一次vertical，就能在≤3步覆盖两个sheet。若旧距离为3，lift中任何≤3步路径都不能用vertical，否则投影只有≤2条旧边，与旧距离3矛盾。因此两个sheet目标都必须由原图三路的不同签名parity覆盖。

本源中0至50的旧距离为3，唯一三路为0–46–21–50。直接邻集证书为：N(0)=[6, 8, 10, 16, 34, 37, 46]，N(50)=[21, 89, 91, 120, 124, 140, 160]，两邻集之间只有边46–21；0和50既不相邻也无共同邻居。任意签名下，该唯一路径只有一种parity，所以从(0,0)到50-fiber的另一个sheet不能在三步内到达。

另一方面，原图任何两点都有≤3步路，提升这条路后至多再接一次vertical即可到任意sheet，故全部签名图均connected且D≤4。结合唯一三路障碍，全部签名图都恰为D4。原图共有5130个无序唯一三路点对，每个强迫至少两个lift无序坏对，因此每个签名图至少有10260个无序点对的距离超过3；不需要知道具体签名。

该论证已经关闭整个固定base范围。因此没有运行“两路XOR差=1”的Gaussian阶段，更没有把≥3路径点对强行设成两两parity不同。

## 文件与停止

`screen.py`、`source_check.json`、`source_distances.json`保存唯一源BFS和路径统计；`obstruction.json`保存一个局部见证与短证明范围。`author_data.zip`保留源档案，`source_download.json`记录维护者链接和下载来源。计算CPU约0.159秒，0签名赋值、0Gaussian、0个340点图、0个340图BFS。没有换基图、扩大field或继续符号搜索。当前pending为空。
