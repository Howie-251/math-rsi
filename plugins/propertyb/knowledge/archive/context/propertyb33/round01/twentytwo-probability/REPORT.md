# 22点、33边：完整形式分支

2026-10-08。

## 结论与范围

`Aris4Math.ThirtyThree.twenty_two_propertyB` 接受任意 `Simple5Hypergraph (Fin 22)`、点对覆盖和恰33边，返回 `PropertyB H`。最终声明没有所选锁点、度数窗口、类型表、概率界、分类完备性或高阶迹数作为额外前提。

这一分支已完整 Lean 构建。它是 T33 最小反例约化的一部分；23、24点由主线程继续处理，本文不宣称整体T33。

## 实际数学连接

结构端由 `TwentyTwoSelection.lean` 对实际H证明：六度unit pair66/67；七度高共度pair；三七度点的共度2诱导路径；或四七度锁点，其共度2图为31、211，或全unit且前三点实际共边。不存在诱导三点路径的邻域结构与度预算覆盖全部输入。

概率端：

1. `PureLink.lean`：纯单锁边定义为真实 `lockSignature={j}` 的边。其4元link全部位于实际 `v-s` 个自由点上。对实际交集双计数，证明纯坏无序边对至少 `(4*p+2-(v-s))/3`。这是真实坏边对的过滤子族。
2. `TwentyTwoPureDeletion.lean`：非负乘子c,d同时利用总坏对quota q和纯坏对quota r。每个无序槽的亏损为 `max(0,c+d*I_pure-weight)`；实现把一半分配到每个方向，再通过真实类型重数对全部关联异边对求和。结果 `q*c+r*d-全部亏损` 是实际删除重量下界。全部同类型/异类型容量及零权重槽均计入，不把两个重叠下界直接相加。
3. `QuadProfiles.lean`：真实四锁16类分割。总边数、四度、六共度、四种恰含三锁的迹重数及恰含四锁的迹重数恢复全部16个实际重数；零行删除保留真实TableRealization。
4. `TwentyTwoQuadData.lean`：全部20个带标签高迹输入（unit 2、211 7、31 11）。它们对应纸面14个重标号轨道。这里直接处理20个标签输入，减少额外重标号证明。具体正类型表以 `rfl` 绑定恢复公式，内核验证有效性、所有center的双乘子式及严格概率总和。
5. `TwentyTwoQuadAssembly.lean`：实际高迹各≤2、六共度库存上界及unit共边正高迹都由H导出；`data_complete` 在这个明确有限域证明每个合法输入都落入20行。`data_of_quadCase` 将实际四锁送入真实 `TwentyTwoQuad.propertyB_of_data`。
6. `TwentyTwoTriple.lean`：诱导路径的两种实际三点共度0/1均连接全部八类型和真实纯槽扣除。`propertyB_of_path` 自动推出三点共度范围。
7. `TwentyTwoHighPair.lean`：两个七度点共度≥3，自动由度7推出共度≤7，全部五种无修正概率界接入实际四类型。
8. 原 `TwentyTwo.lean` 的66/67实际caller保留。`TwentyTwoComplete.lean` 将全部结构分支装配成实际Bool染色。

## 验证证据

项目固定 Lean 4.24.0、原Mathlib manifest，无依赖升级。

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.ThirtyThree.TwentyTwoComplete
lake env lean ../context/propertyb33/round01/twentytwo-probability/import-audit.lean
```

- `build-dual-r4.log`：PureLink与完整双乘子实际删除接口成功。
- `build-quad-r2.log`：四锁实际反演与真实profile实现成功。
- `build-quad-data-r1.log`：20个带标签有限局部输入全部核验成功（本机226秒）。
- `build-quad-caller-r1.log`：实际四锁→PropertyB成功。
- `build-triple-r1.log`、`build-high-pair-r1.log`：新三锁与高共度双锁实际caller成功。
- `../twentytwo-selection/complete-build.log`：完整22点分支清洁构建成功。
- `import-audit.lean/log`：独立导入并展开原有限边集、五元性、33边、点对覆盖→Bool染色。主分支、关键连接与旧32边Main的传递公理仅为 `propext`、`Classical.choice`、`Quot.sound`。

源码无 `sorry`、`native_decide` 或新增公理。有限计算只核验局部输入及有理公式；没有枚举超图或染色。

## 来源和生成

纸面完整论证：`proofs/propertyb33/TWENTY_TWO.md`。根线程保存了各使用局部型的独立A/B/C复算与原双乘子JSON。

`QUAD_LABELLED_DATA.json` 保存原14轨道见证重标号展开为20标签输入后的值。生成器在 `computations/propertyb33/round01/generate_twentytwo_quad_lean.py`、`generate_twentytwo_triple_lean.py`，从formal目录运行；Lean编译不依赖Python执行。

Gemini B4 recovery已只读审阅纸面22分支并手核两个紧型，没有发现缺口；未运行代码。Grok B4中断无最终回包，不计通过。新Lean完整链的跨模型审阅由主线程安排。模型意见与内核证明分别记录。
