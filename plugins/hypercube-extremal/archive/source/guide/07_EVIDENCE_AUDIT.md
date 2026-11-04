# Q4 证据审计与可复现性

审计日期：2026-11-04。源目录只读；以下结果由本轮原始文件审读和独立整数核验获得。

## 当前最强已找到的可认证上界

`pi_Q(C4) <= 23662061277957791/40000000000000000 = 0.591551531948944775`，向外小数 `0.59155154`。
这是渐近密度上界，未达到 0.59；不代表 Q4 层级理论最优、SDP 全局最优、有限 Q8 上界或 Erdős 1/2 猜想证明。
最终文件虽位于 `q5_empty_moment_20261028`，其 `q5_cuts=[]`，六块均为整数 Gram PSD，因此保留它不包含任何 Q5/Q6 尝试。

## 精确证书里程碑

|阶段|精确分数|小数|
|---|---|---|
|complete Q4 + real empty face|119941059204403/200000000000000|0.599705296022015|
|full oriented face root refinement|18933741304467/32000000000000|0.59167941576459375|
|joint six-block optimization|236634773493897/400000000000000|0.5915869337347425|
|best found certified pure-Q4 control|23662061277957791/40000000000000000|0.591551531948944775|

所有源路径、SHA-256、大小和证明角色见 `audit/evidence_audit.json`；整数因子是权威数据，小数矩阵/浮点快照不替代证书。

## 六块的几何定义与归一化

Q2 根面四条边按 `(0,1),(0,2),(1,3),(2,3)` 编码。五种合法根型掩码 `0,1,3,6,7` 分别为空、单边、相邻双边、不相交双边、三边路径；全四边因 C4 禁止。
一个外部方向的旗状态为 `connector_mask + 16*translated_square_mask`。保留共同根标号、合法的连接边和翻译面边；五块阶数为 240、212、190、187、170。
矩阵的两个旗由同一个根稳定子元素同步作用；不能把两旗分别旋转后独立取商。根稳定子大小依次为 8、2、2、4、2。
第六块是顶点根：含根顶点的 Q2 四边状态按两个方向交换取商，合法状态 9 个，矩阵 9×9。Q4 上对 16 个顶点和每顶点三种互补方向对划分平均。
局部不等式为 `e(K)/32 + C_F(K) + C_v(K) <= C`。`C_F` 对 24 个根面平均；`C_v` 对 48 项平均。原 C++ 统一分母 `192 D²`，`D=50000000`。

## 全域覆盖及本轮实际复核

Q3 合法图 2,902 个，所有有序层对 8,421,604 个，由 90,179 个互不重叠的自同构轨道覆盖。对每轨道层对枚举全部 256 个连接边掩码，经 C4 条件保留 13,150,453 个合法带标记补全，再按隐藏方向最小轨道序号筛选直接计数 3,312,331 个代表。
最后一个数字是核验器行域大小，不能写成全部非同构 Q4 图数量。覆盖结论来自核验器重建 48 个 Q3 自同构并检查每个合法有序层对。
本轮在 `audit/recheck/` 复制原始四个最小文件，运行 `python -B verify_q5.py certificate_control.json`；重新编译 C++17 后退出 0。
精确最大值 `283944735335493492/480000000000000000`；最坏局部图掩码 `3602350111`。这是局部不等式的最大值，不是渐近极值构造。
此处“独立”指不读取优化端系数表、从几何直接重建；仍是同族代理审计，不能声称跨研究者/跨模型独立验收或 Lean 形式化证明。

## 最终对角界与高维平均证明

本轮从最终整数 Gram 因子逐行平方求和，并与 `result_control.json` 精确分数逐项交叉核对。

|块|阶数|最大对角元（精确）|
|---|---|---|
|0|240|1288810336780277/1250000000000000|
|1|212|247334669209467/250000000000000|
|2|190|298707993982323/312500000000000|
|3|187|37933932961587/39062500000000|
|4|170|2195329262306569/2500000000000000|
|5|9|324664893404033/625000000000000|

`M_F=1288810336780277/1250000000000000`；`M_v=324664893404033/625000000000000`。
固定根面且 q=n−2 时，方向频率 u 和不同方向联合分布 R 满足 `uu^T=((q-1)/q)R+diag(u)/q`。PSD 与最大对角界推出面根平均至少 `−M_F/(n−3)`。
顶点根下两个随机方向对不相交的概率 `p_n=(n−2)(n−3)/(n(n−1))`。无条件 PSD 平方型非负且矩阵条目绝对值不超过 `M_v`，条件平均至少 `−M_v(1−p_n)/p_n`。
故 n≥4 时 `rho(G) <= C + M_F/(n−3) + M_v(4n−6)/((n−2)(n−3))`；令 n→∞ 得渐近结论。该解析平均步骤依据历史研究报告/README，不由有限整数扫描单独证明。
本轮按完整整数矩阵重算绝对算术安全界为 `3045579237691790784 < 2^63`。

## 最小运行与搜索重现

最小核验仅需 `certificate_control.json, keys.bin, verify_q5.py, verify_local.cpp` 四文件及 Python 标准库、GNU/Clang C++17 编译器，无需 NumPy/SciPy/求解器/互联网。在可写副本运行：

```text
python -B verify_q5.py certificate_control.json
```

如改成纯 Q4 包装器，保持证书字节不变，先断言 q5_cuts 为空；保留原核验器作为归档。不要关闭 Python/C++ assert。
可选搜索重现须保留模型目录与控制目录的相邻布局，依赖清单已列在 JSON；需额外 NumPy 2.4.2、SciPy 1.17.0、OpenMP。无需复制 Q5 的 cuts/partition/moments 文件。

```text
cd optimization_20261028_q4
g++ -O3 -shared -fopenmp -fPIC evaluate.cpp -o evaluate.so
cd ../q4_control
python column_lift.py --no-q5 --rounds 20 --prefix final_control
python certify_lift.py --input final_control_best.npz
python verify_q5.py certificate.json
```

上面的 `q4_control` 是推荐可移植目录名；原始脚本依赖其兄弟目录 `optimization_20261028_q4`，前提是已复制相应数据文件。浮点路径受 BLAS/平台影响，不承诺逐位重获同一界。证书验证才是决定性结果。
Windows 编译共享对象需使用相应 DLL 选项并保持 ctypes/C++ ABI 一致。原 `certify_lift.py` 无论输入名称都覆盖当前副本的 `certificate.json`，应在 scratch 中运行，再明确重命名输出。

历史数据重建入口为 `prepare_data.py`, `build_face_orbits.py`, `generate_models.cpp`；旧 `full_C/full_meta` 来自 `build_full_flags.py/full_flags.cpp`，还需完整历史输入链，详见 JSON。直接证书核验不需要这条大数据重建链。

## 可移植修复清单

- Use explicit executable .exe suffix on Windows, and use UTF-8/ASCII text I/O.
- Original wrapper writes matrices/executable in its source directory: run a writable copy.
- Compiler needs C++17 plus GNU/Clang __int128 and __builtin_popcount extensions; plain MSVC is not supported.
- Keep assertions enabled: do not use Python -O or C++ -DNDEBUG.
- Binary geometry uses native int32/uint16 layout; supplied files were produced on little-endian x86-64.
- model.py ctypes c_long / C++ long is 32-bit on Windows and 64-bit on Linux; maintain ABI agreement.
- evaluate.so must be rebuilt on target OS (Windows DLL or Linux shared object), with OpenMP.
- Search imports SciPy private scipy.optimize._highspy._core; pin NumPy 2.4.2 / SciPy 1.17.0 or adapt API.
- column_lift.py uses RNG seed 20261029, while historical run_manifest.json says 20261028; use script value and record this metadata discrepancy.
- column_lift.py and certify_lift.py expect sibling optimization_20261028_q4 directory; rewrite paths if reorganized.
- Final control certificate is stored under Q5-named directory and proof_type, but q5_cuts is empty; remove misleading Q5 labels in portable Q4-only entry point.
- certify_lift.py writes certificate.json/result.json regardless input; run in scratch copy and rename control outputs afterwards.
- continue_joint.py reads refine_latest.npz active set even when --input is explicit; retain that dependency or replace with deterministic initialization.
- Older README finite-dimension correction constants belong to older matrices; use final bounds recalculated here.
