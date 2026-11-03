# 固定三base × Z26 的六端口 controller 精确门

执行前预测，2026-11-01。此为同一Goal中的新连线规则；不恢复C60+H18的两次UNKNOWN CNF，不重跑任何旧图。

## 对象与归属

继承 `../../f7_c60_d35/PARAMETERS.json` 中 Bhakar（作者仓库 f4t4nt/degree-diameter-graphs）的三base `(a,b,s)` Schreier框架及零电压b三角形。这里改为唯一固定deck Z26，增加明确的第六匹配t；新参数、实际78点controller及覆盖证据归本次。一般Schreier lift不是本次发明。

顶点 `(c,g)`，`c=0,1,2`、`g∈Z26`，label=`26c+g`。ports依次 `a+,a−,b+,b−,s,t`，inverse=`[1,0,3,2,4,5]`。

- a+: base0→0 shift α0；1→2 shift α1；2→1 shift α2。
- a−：0→0 shift −α0；1→2 shift −α2；2→1 shift −α1。
- b±：base±1，shift0，所以b³在每个deck坐标给实际三角形。
- s：0→1 shift σ，1→0 shift −σ，base2自身shift13。
- t：0→2 shift τ，2→0 shift −τ，base1自身shift13。

简单6正则的充要参数约束是 `α0∉{0,13}`，其他四参数非零，且 `α1+α2≠0 (mod26)`。deck单位乘法保留13与b零电压，合法α0的gcd仅1、2，故整个固定family可归一到α0=1或2。其他四参数不再作WLOG。

## 单次有限门、预算与停止

单worker总10 CPU秒，含准备、编译、搜索与成功后的本地证据导出。按α0=1,2 outer，其余 `(α1,α2,σ,τ)` 在1..25字典序，只跳 `α1+α2=0`。每branch375000个简单参数，合750000（raw781250）。不扫描其他modulus、matching/permutation，不作坏对hillclimb。

预计算3个base根的全部648个三port词，其终点为四搜索参数加α0与13的线性式。对每候选以9个26位mask精确检查3×78=234个deck平移类，首个完整 `A³>0` 即停。平移保ports，故这等价于全部6084有序点对；相同／非相邻端点的三步walk自动无即时回退，能直接接已PASS的F9六端口局部满秩／相邻pencil接口。成功controller阶78对应条件性目标56862=78×729、degree54，已读public54保证55350。

成功保存完整controller边表、porttable、参数与234个实际三port见证，并核全部实际度数、inverse ports、零电压b三角形与见证deck平移。若两branch穷尽则仅排此固定m26 family；若预算尽则UNKNOWN并给出已试字典序domain。0 fiber图、BFS、solver、Lean、hash、install。

纸面独立核对已确认两代表、simple约束、每branch375000与234类等价；不运行第二数值worker。
