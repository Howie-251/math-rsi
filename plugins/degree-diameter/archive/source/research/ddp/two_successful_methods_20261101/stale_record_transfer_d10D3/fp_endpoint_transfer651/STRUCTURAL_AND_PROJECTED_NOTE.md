# actual650：容量并不短缺，精确压缩仍UNKNOWN

本轮从旧1170变量20秒无incumbent继续一个具体结构问题，而非续timer。只复用旧覆盖模型系数：1040cut列按真实F身份合为520个C_f，各包72；130个D_p各86，所有65 twin-P的D列均不同，不能直接合成65star变量。

## 事前预测与实际检验

预测至少一two-starP选择通过按65类0/1/2 donor配额、总8包的覆盖容量上界。完整8385对全部通过，最小upper surplus46，预测支持。首star0/73剩366点，各类局部最优加和449，实际八包并仅337（全F覆盖491/520），漏29；这展示该见证的重复覆盖，不证明其它选择也漏。上界过松，不能把此门写成Fcover可行或整族No。

DP在m1≤m2≤2m1下等价为mandatory h后取6个最高递减边际；真实F身份的best single无需嵌入best pair，按最终cost重取局部argmax。独立paper已核这个上界与索引契约。0源/A2/A3/新BFS。

## 理解改变了下一次求解

利用每class恰K8,2，消去donor指派变量得到650binary/652rows/50440nonzeros的精确整数投影（原1170/1302/90480）。两类P实际D仍分别保留。原20秒窗口未重跑；新encoding只开一次18秒，实际18.007674689CPU到时无incumbent，process18.287680910，仍UNKNOWN。没有实际8F+2Pstar，没有donor冻结/15repair/newroot/oldold检查，不能把失败归因于PP repair或旧路线损伤。

原PP已有边可保留为degree9分支，代码已实现但未进入；这不改变前置F-cover。即使将来有y/z，单一canonical donor还原失败也不排同y/z其它合法指派。

## 停止范围

wholecase最终42.416193092/45CPU，包含旧22.084731374、读门/准备、完整容量门/编译、projection构造/solver及root整理，不清零。旧FP_RESULT/旧ROOT原样保留为历史，新ROOT为当前终态。0新图/参数/Lean/ARIS，0源图验证或图BFS。停止本源的FP-cover窗口，不第三solve、换seed或加FPcuts。一般(10,3)及该FP机制仍OPEN/UNKNOWN；下一换参数，保留精确投影与缓存。
