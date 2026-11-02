# 3750 点具体图的 Lean 绑定结论

修订时间：2026-10-29T16:45:31.290285+00:00。

## 已完成的核心形式化

锁定 Lean 4.24.0，具体图为 `DegreeDiameter.Portfolio.F5Graph3750.graph : SimpleGraph (Fin 3750)`。最终已编译：

- `concrete_order_degree_and_D3`：顶点数 3750、每个顶点的 degree≤20、每对顶点存在长度≤3的真实 graph.Walk。
- `diameter_exact_three_in_project_definition`：`DiameterAtMost graph 3 ∧ ¬ DiameterAtMost graph 2`，即项目现有直径定义下恰为3。

这里 `DiameterAtMost G D := ∀ u v, ∃ p : G.Walk u v, p.length ≤ D` 是实际图上的全称结论。没有源图 D3 假设，没有依赖外部 BFS 正确性。`#print axioms` 对两个最终定理均只返回 propext、Classical.choice、Quot.sound；无 sorryAx、自加公理、native_decide 或依赖未证明证书。

最终结果在 `FINAL_COMPILE_RESULT.json`，完整成功源码冻结于 `FORMAL_FINAL_SOURCES/DegreeDiameter/Portfolio/`。它包括9个新图专用模块及不变的 SingleExtension 依赖；此前 binding-only 和 inverse-only 两个快照仍保留为历史，不是当前最终状态。

## 结构化证明如何避免全图点对穷举

1. F5Graph3750：字面30控制器、四个矩阵、方向与Fin3750标签；检查2500个fiber逆绑定，证明真实邻接恰为20个port/noise生成邻点的像，得到全顶点degree≤20。
2. Routes：编码坐标恢复、加减、抵消与任意输入下的逐步仿射兼容，用代数证明推广有限零起点证书，没有枚125²源目标坐标。
3. RouteWords：把三步纤维关系与三个真实图边组成实际 graph.Walk，给出正确controller/fiber终点标签桥。
4. RouteData、ControllerCertificate、NBDecoderCertificate、AdjacentCertificate：900个controller单元中780个非邻/相同对各选一条NB三port词；36×125=4500个零起点NB位移decoder及4×125=500个相邻pencil位移decoder由Lean kernel检查。相邻路采用前回退或后回退，controller_reverse与fiber逆绑定给共同仿射中心。
5. Diameter：对任意u/v，选择对应controller路线，以`目标−仿射中心`调用小decoder，再利用仿射兼容与实际边桥构造长度3的walk。没有对3750²点对调用decide。
6. Exact：仅检查0→6的20条一步与400条两步生成路线不存在；由已经证明的Adj等价生成边，将任意长度≤2的walk化为这些路线，严格排除D≤2。

最后decoder批实际59.374CPU秒（110CPU guard）三模块全exit0；Exact批2.779CPU秒，exit0。逐模块命令、真实PID、CPU、日志与终态分别见FORMAL_KERNEL_DECODERS_RESULT.json、FORMAL_EXACT_THREE_RESULT.json及同名前缀日志。所有最终作业已终态。

早期单块有限证书触及120CPU软限；保存结果为123.904CPU的失败批，未冒称通过。Array表示、分行证书以及`decide +kernel`使最终批在预算内完成。`decide +kernel`是内核归约检查，未调用native_decide。

## 明确保留的交付边界

具体图公式的阶数、度数上界及全局精确直径已在Lean证明。独立边表BFS也已数学验收3750/37500、20正则、D=3。但“磁盘上graph_d20_D3_n3750.edges的每一条文本记录恰好枚举Lean图全部边”尚未作为Lean输入解析/等同性定理绑定；本次不把文本文件解析和公式定理混成同一个证书。

Lean只证明degree≤20，未额外证明20正则性等号。未引入mathlib.ediam的额外未缓存依赖；项目的DiameterAtMost已是每对顶点真实walk定义，与数学验收直径一致。这不影响本图的核心构造定理。是否为当前公开纪录以及对现有文献的新颖性另行核对，不由本证书声明。

## 可用编译入口与已完成恢复

使用现有 `.tools/lean-4.24.0-linux/bin/lean -j8`，cwd为formal，显式LEAN_PATH见FORMAL_ENV_COMMAND.json；新模块间按FINAL_COMPILE_RESULT.json的compiled_modules顺序编译。`compile_formal_route_stage.py`只调用直接Lean，按RUSAGE扣除每批CPU余额，不运行Lake、下载或安装。

最初误用lake env lean曾实际改写mathlib目录，已立即终止并完全离线使用原v4.24.0源码tar与本机2285个已有Mathlib缓存恢复。原SingleExtension.olean的极小导入/#check实际exit0，44.72秒，之后全部新模块也真实编译成功。完整恢复日志与精确命令保留在FORMAL_ENV_RESTORE_LOG.txt、FORMAL_ENV_COMMAND.json；所有相关lake/git/smoke均终态。
