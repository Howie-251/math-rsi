# 完全自由二正则内部块与六度跨边

对象是存在29+29划分、两侧诱导各为简单2正则图、跨侧各6度的58点直径至多2图。
`H0,H1`各406个无向边变量全部自由；`C`的841位全部自由。内部度恰2、C行列
和恰6，故完整图为58点232边、全8度。任何内部圈型均可共同选择；没有固定
C29、圈分拆、相对圈顺序、匹配、三角形条件、旧Hamilton排除或C对角值。

跨侧真实路线矩阵`K=H0*C+C*H1+C`的行列和为30。覆盖29个对侧点给出
`K=J+P`，P为某个置换；因为H1完全自由，可无损重标右侧使P=I，详见
[NORMALIZATION.md](NORMALIZATION.md)。这个归一化不是又把某个固定圈型重新
编号为标准圈；本模型没有固定任何内部图。

每个跨侧(i,j)由直接位Cij、28个左内部/跨侧AND、28个跨侧/右内部AND组成
57项路线计数，精确为`1+delta_ij`。每侧全部406个无序点对由直接Hij、27个
同侧中点AND、29个对侧中点AND组成57项覆盖OR。所有AND双向等价；所有
计数器双向编码真实前缀阈值。因此模型可满足当且仅当该完整二正则块族存在
目标图（按允许的右侧重标取代表），不是必要条件筛选。

预期规模由辅助原语逐项算出，正式prepare还会断言：

| 项目 | 变量 | 子句 |
| --- | ---: | ---: |
| H0、H1、C主变量 | 1653 | 0 |
| 58个内部度2、58个跨侧度6计数器 | 15254 | 57362 |
| 812个路线计数1、29个路线计数2计数器 | 96628 | 338546 |
| 跨侧47096个真实AND | 47096 | 141288 |
| 同侧45472个真实AND | 45472 | 136416 |
| 同侧覆盖OR | 0 | 812 |
| 总计 | 206103 | 674424 |

仅复用通用CNFEmitter、enforce_exact及其unary_thresholds、add_iff_and，
和joint_boundary_completion_run中的通用evaluate_clause、check_dimacs。
未调用旧Hamilton或一般补全build，不导入旧图、几何或排除子句。

接口：`python encode.py sanity --output-dir DIR`只建立小模型并保存
`small_sanity.json`；`prepare --output-dir DIR`写input.cnf、encoding.json、
variable_map.json、sanity.json，状态PREPARED_NOT_RUN，不启动solver。
正式prepare另用一张明确失败的完整图作全规模显式赋值、定义扩展及写回CNF
核查；该图不限制主变量。`decode --output-dir DIR --model FILE`默认读取
DIR/solver.log，必须有SAT终态、完整变量赋值并逐条通过保存CNF，随后展开
全部边、独立计算度数、共同邻居计数及全源BFS，输出candidate.json和
candidate.edges、H0/H1/C/P、两侧逐圈的完整图顶点顺序与圈长，以及完整坏对。
`internal_cycles.H0/H1`分别使用0..28、29..57的完整图标签。
非目标失败退出；main(argv=None)
成功正常返回。根代理再从边表调用现有独立图检查器。

小语义使用真实m4、跨度1正例，仍满足`5d=m+1`及余量1，不替换为其他delta。
先检查未归一但合法的图，再检查右侧任意重标并恢复P的代表；逐条完整赋值
与实际BFS对应。另外以m9、跨度2检查所有度数正确且K=J+I，仍有27个同侧
坏对的负例；核对跨侧路线失败、内部及跨侧度数失败，以及AND的8个真值。
初交付只运行这些小检查，不生成29正式CNF或启动solver。

通过单独纸面归约，这覆盖58点目标的全部非平凡二块equitable partition
可能性；该额外结论见旧方向中的握手/容量与4+4奇偶论证，不作为CNF新约束。
没有证明任意58点目标都存在这种划分。UNKNOWN不是排除；未经证书检查的
UNSAT也不作为正式排除。本模型未预先省去已关闭的Hamilton子族。
