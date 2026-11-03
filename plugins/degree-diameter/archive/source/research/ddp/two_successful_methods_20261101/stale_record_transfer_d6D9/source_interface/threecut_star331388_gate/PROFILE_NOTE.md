# 实际反馈：phase互补预测失败，三类旧边都发现九步瓶颈

唯一新数据进程完成。一次 identity-root depth<=8 support BFS 到达281007点；未见的50380点以 inherited sourceD9 标为9。由同一支持顺序做 shortest-word DP，保存全部331387项 d/c；sphere4实际750点，标签及实际四步路径也已保存。没有重跑旧single-subdivision三queries、旧F6959族或源allrootD9，source-validity BFS计0，new-question support BFS计1。

三份完整 endpoint-pair R8 missing labels 新近持久化；其大小14088/13875/14028与旧已知数量一致，这不是新排除或新认识。新信息是每一份缺集在**全部49个phase上都有点**。所以64827个class/phase tuples的phase-support交都仍为49，0个empty。预测1被推翻：不存在本批所求的phase-disjoint充分证书；这不排除同phase内的normal坐标互相错开，也不关闭三cut六星原族。本次没有据此继续扫normal shifts，因此没有选定六pins或生成候选图。

预测2得到支持。对750×750个u,w，每个positive edgeclass完整查 d(u^-1*s*w)=9 与 shortest-count factorization，实际critical关系大小分别为 **32、21、32**。关系矩阵、每类首actual九步路线均保存，0次u-v BFS。例如type0的首对是u1749、v40385，唯一九步路线为

`1749–127167–139383–14826–0–170329–292433–277770–158690–40385`。

该对 measured<=8 support 不可达、又有实际9walk，故距离确9；total shortest count1等于左右4步count1×1，所有9geodesics经过cut0–170329。对其平移后的任何三cut方案，若其它四pins都不能在3步内接近该对任一端点，新star必留下old-old距离10。此关系指出了必须由别的pins补足的旧路线，而不只是一个坏对分数。

本批结果真正改变下一研究：phase投影完全失去区分力，不能再在phase上寻找空交；actual normal-level M sets和稀疏critical relations现在可共享给另一个明确授权的互补/旧路保护问题。即使将来某六pins通过所有本批4+1+4critical关系，也只是一类old-old必要门，不代表全部D9。root提出的完整seam/count门属于后续纸面/授权范围，本批没有添加。

文件格式在 `PROFILE_DATA_SCHEMA.json`：d.u8/count.u32、sphere4 labels/paths、三M.labels.u32、三critical.u64行bitmatrix。其余sphere0..8可直接由 measured d数组取 `d==i`，无需新BFS。完整64827相位记录和实际数值在 PROFILE_*，readgate的原TERMINAL保留。

编译CPU1.371466、native0.086142；含父进程、继承0.8与准备0.25后累计 **2.511387697/20 CPU秒**。compile/run均exit0，全部终态。0候选图、0solver/Lean/远程、0normal/新seed/额外cut；按原授权停止。
