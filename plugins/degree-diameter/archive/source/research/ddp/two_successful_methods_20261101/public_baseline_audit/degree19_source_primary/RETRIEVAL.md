# Rajiv 19度2783源：原始小文件与精确入口

来源为2026-09-30 Zenodo记录23052995，完整archive59224157 bytes。本次只取末尾central directory和两成员的local header／compressed payload，总76900 bytes；HTTP206范围、文件尺寸和来源地址见RANGE_RETRIEVAL.json。用Python标准库raw-deflate解压后原样保存witness与作者源码，没有运行其生成／验证函数、下载adj或完整ZIP。

- fq_d19_k3_n2783.json：完整q11、field、X、Xp、t和有限gadget数据，原gadget标签u=11a+l。
- verify_witness.py:58..85提供field；88..158为实际q11构图函数fibre_build；175..205的check_fibre用它生成并比对原adj，再全源BFS。本次没有调用这些函数。
- 几何点用first-nonzero=1归一化、lex排序。aff点v[1]非零，point ID由该排序给定，未必等于仿射坐标a*q²+b*q+c。
- 线为normalized point frozenset，按sorted(pointset)排序；剔除过inf的线，line ID=1331+index。
- class M是过inf的q+1条线，按同样line-set排序。各M的pencils以交点m排序；每pencil取最小line-set作base，β(a,l)=z_l(base)。这具体固定了gadget在哪条线起作用，不能忽略base相位。
- 源码208..242另有fibre_coordinate_edges简式（point(a,1,b,c)用a*q²+b*q+c，line用q³+w*q²+u*q+s），但作者仅在matching verifier中调用。q11若改用此式，须核β同构／标签桥，不能仅靠同点数和度数替换原source。

作者witness包含其既有校验字段；本次未计算、调用或采用它们作新验收。后续可只提取field和fibre_build函数体，避免执行main和所有图的全源验证。图正确性、实际R2 pin-cover接口及新图验收由数学任务另行负责。
