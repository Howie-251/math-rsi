GitHub 上传与重建说明

这是153个命名图的紧凑源码包，覆盖43组参数。47条具体图Lean完成状态来自原记录；其余106个也有计算检查或完整覆盖论证。153是命名图实例数，不是153个全球纪录。

上传什么：
将本文件所在目录的内容放进你要发布的GitHub仓库即可。建议保留目录结构，让README.md、catalog.csv和reproduce_index.csv位于同一层。源码目录约11 MB；原先目录直接索引的完整边表约3.58 GB。

包内有：
- early_d5：103个早期D5图。三份压缩基图、完整新增邻域参数、重建程序。
- late_graphs：后期50个图。原构造源码、小参数、输入表、统一重建入口。
- verification：106个未Lean图的相应历史验图材料，以及本轮打包重放记录。
- reproduce_index.csv：全部153个图各自的重建命令。
- catalog.csv：原目录快照，包括规模、形式化及公开比较状态。

重建示例（先进入本目录）：

python3 early_d5/reproduce.py --degree 12 --order 42402 --output graph_d12_D5_n42402.edges.gz

python3 late_graphs/rebuild.py --case d20_D3_n3750 --output graph_d20_D3_n3750.edges

python3 late_graphs/rebuild.py --case d98_D3_n414132 --output graph_d98_D3_n414132.edges

早期程序只需Python标准库；后期部分构造还需本地已有的C++17编译器。源码包不包含编译二进制、Lean缓存或大量完整图边表。

图文件是边列表，不是邻接矩阵。一条u v代表一条无向边。早期图含n m首行；后期按原格式保存，具体看late_graphs/cases.csv的edge_format列。body-only表示文件没有n m首行，规模由目录给出。

本轮实际检查：
1. 从打包基图重算103步完整current-R4覆盖和度数，全部通过。
2. 37631、42402、51457三个D5终图的重建边集与原文件完整一致。
3. 后期9个代表图的重建整份整数行与原文件完整一致：3750、3900、20580、7532、2016、4125、16416、57672、414132。
4. 没有重新跑全部153个图的全源距离计算或47个Lean构建。

原图完整文件如有需要，可运行对应生成命令取得。直接上传本源码包即可完整说明图的确定性定义，不需要上传邻接矩阵。各个原始图、控制器和已有框架的出处保留在原程序及参数文件中。

方便给别人看的中文验图和存储说明另存于ar4math/GRAPH_VERIFICATION_AND_UPLOAD.txt；压缩包位于ar4math/graph_sources_for_github.zip。

实际存储大小（本轮打包测量）：
源码文件数量：115
源码文件合计：10962731 字节，约 10.96 MB
ZIP：5587539 字节，约 5.59 MB
