# 下一项小度数D4／D5：仅建议一个新的route兼容门

本note遵从最新steering：停止新的D3 degree／复制倍数扩展，重点转向4≤Δ≤12的D4／D5。这里只读现有registry、casebook、相关源与严格失败账，不启动新图、旧源BFS／DP、field／rank、solver、查询或Lean。下述是一个待root授权的≤20CPU可推翻预测，不是新合法图或已排队计算。

## 选择：优先(8,5)的非均匀phase电压必要门；对照(9,4)停止固定源append

| 对象 | root本次fresh主表值 | 实际现状 | 此次选择 |
|---|---:|---|---|
| (8,5)，以已缓存Loz1100／D4作5-sheet source | 5334 | 旧125个特定metacyclic5500对象均失败；一般edge-local cover未被排除。已有精确五-route数据，可区分路线缺少与共同电压不相容。 | 一个新的phase-dependent deck门；若未来全成功图存在则n5500、m22000，比本次已读5334多166。当前没有这张合法图。 |
| (9,4)，当前1768源 | 1768 | 源7956边、max9强迫9regular；固定cap9保全部旧边连通增点已关闭；旧literal请求404。 | 继承STOP，不重profile／下载／append，也不把文件名1818当合法图。 |

这只是两个具体对象的对照，不是方法清单。公开表值由root在2026-11-01实际核读继承；本note没有重新联网或把描述页的过期小值作为门槛，也不认证全球priority。

## 为什么8D5有一个真实但未验证的接口

已缓存Loz1100源的RIGHT law是

    (j,n)(k,m) = (j+k mod20, n*2^k+m mod55),

四个正向dart为(1,0)、(12,33)、(11,1)、(16,19)，另四个是真逆。该源的1100点／8regular／D4和既有配方作为已知输入继承，不重新BFS或恢复。它很小，且next gate只需20个phase与旧保存word，不需读完整源边表。

严格已关闭的是：normal改为Z275、保固定source π55、五种合法action lifts2/57/112/167/222，每种所有625source-label-preserving generator lifts经严格gauge压成25项，共125normalized对象／3125raw选择。每个实际5500图的identity R5失败，UNKNOWN／未试均0。这个完整负结论必须原样保留，不再追加action、s/t、prime或按剩余62坏点微调。

旧诊断已说明更具体的覆盖现象：源中长度≤5的reduced路线最低数量恰5，在identity与g3=(11,1)及其逆三个紧fiber达到；所以“五条不够”猜测已被反驳。g3的五条保存word在10个旧settings中确实给五个不同deck值，但同一setting仍可能漏另一fiber，例如r2/s1/t1漏source projection(0,6)。因此单个紧fiber成功也不是D5；真正未知是多组路线电压能否同时满足。这里不把这个旧诊断再登记为新认识。

原始证据：

- `research/ddp/more_graphs_20261027/d4_source_transfer/{REPORT.md,SOURCE.json}`：实际RIGHT源与已关闭的D4迁移范围。
- `research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/{REPORT.md,RESULT.json,ANALYSIS_NORMALIZATION.md}`：原25类、完整规范化与严格scope。
- 同目录`all_action_lifts/{REPORT.md,RESULT.json}`：新增四action的100类，合计125完整关闭。
- 同目录`base_route_multiplicity_gate/{REPORT.md,RESULT.json,FIVE_ROUTE_RESULT.json,COMPARISON.json}`：已计算的精确五-route、各旧setting的deck像及不同fiber反例。
- `research-wiki/experiments/ddp-loz1100-z275-all25-preserving-lifts-8d5-20261028.md`：明确保留arbitrary edge-local covers未排除。

## 新规则的区别：每个phase有自己的deck电压

固定原1100 source，不改其四个正向dart或任一源邻接。在每个phase j∈Z20、每个正向type p∈{0,1,2,3}上取独立θ_(j,p)∈F5，共80个标量。候选连接规则为

    (j,n,z) → (j+k_p, n*2^(k_p)+m_p, z+θ_(j,p)),

其中n仍模55、z模5。反向dart在phase j+k_p的电压强制为−θ_(j,p)，不是另一个独立变量。这定义了同一简单8regular源的ordinary5-cover；若生成则恰5500点／22000边，邻接端点与端口simple性由固定源继承。连通性和D5不能仅凭这个定义宣称。

这是edge-local、phase-dependent的电压连接，不再要求整图是一个固定半直积群的四generator Cayley图。旧125-class规范化只涵盖其明写的global action/generator lifts，不涵盖这80个独立phase电压；phase-dependent重连可打破旧各source fiber共享同一少量action／s／t参数的耦合。反过来也不能说它包含所有旧非中心metacyclic covers，或全部edge-local5-covers；这里只选一个清楚的新子模型。phase/generator标签和mod55均固定，不做phase pattern或prime ladder。

可作合法gauge z↦z+f(j)，仅把type0的phase0..18十九条spanning-tree电压置0；type0在phase19的闭cycle电压必须保留，不能全20条强制0。这样最多61个自由F5标量。这个gauge是坐标等价，不是已经求得的参数，也不需先运行一次全参数搜索。

## 下一次唯一≤20CPU预测与返回对象

具体正预测P：存在上述phase电压，使**每个j=0..19**的三个紧source fibers（identity、g3、g3逆）的五条≤5路线分别具有五个互异deck像。也就是60个五元组都恰覆盖F5，而非只让某一根／某一fiber计数改善。

每条word的deck值是沿其实际phase序列累加θ的线性形式。反向出现时使用上述负向电压规则。g3五条word直接从已保存FIVE_ROUTE_RESULT.json读取；g3逆使用反向并逐dart取逆的五word；identity使用已知empty及两种五cycle和其逆，完整性继承旧最小route-count证据。删除立即backtrack不改变deck像，所以不漏额外≤5walk可提供的新deck值。不得为了这个门重做source route DP、source BFS、旧125图或场检查。

这是D5的必要条件：某紧source fiber只有这五个reduced路径像，而目标cover有五个deck点。若其中任意两像相等，就有一个lifted目标在≤5不可达。源Cayley的左移把这些word输送到每个source root；新规则依phase变化，故不能只检j0。对normal坐标的左平移(j,n,z)↦(j,n+c*2^j,z)仍保边，deck整体平移也保边，所以同phase的全部normal／deck起点等价；这解释20phase门的范围，而不是未经证明的全source传递性。

建议未来一batch总≤20CPU（含读取、建模与返回），1worker；solver至多12CPU，预算到即UNKNOWN，不重启timer。只解80变量或上述合法gauge后的有限F5 all-different可行性，不最小化坏对、不全参数随机筛。当前已有solver可表达模5线性形式；无须安装新工具。返回：

- SAT／可行：保存具体θ、每个phase／tightfiber的五条实际电压值、gauge与反向绑定，验证60个tuple互异。明确这只支持P，不是完整5500图或D5。
- 严格INFEAS：仅关闭这个phase-only additiveF5电压规则的必要门；给solver证据级别，不外推所有ordinary5-covers或整个(8,5)。
- UNKNOWN：保存实际incumbent／bound／未完成条件，停止，不自动延时或换phase／seed。

若P支持，下一步才由root决定是否生成那一组具体候选并检查其他source fibers；旧例(0,6)说明这个全局义务不能省略。若P被推翻，它就说明放开phase仍不能协调最紧路线，足以停止这一新子模型，不应继续追逐各fiber少量坏点。这个必要门故意不是“先试许多图看看”。

## 9D4对照及1818命名误读纠正

`research/ddp/more_graphs_20261027/d9_D4_current1768_source/SOURCE_NOTES.md`和`PROVENANCE.json`已清楚记录：1700个9regular点、删191边、增68点／497边，最后7956=1768·9/2且max9，故全9regular。其D4依公开完整成图继承，不能从删边前1700图自动推得；source literal未本地绑定，指定一次请求404后停止。既无degree slack，也没有新的删边路线依据，本note不将它重开为clone／helper搜索。

`research/ddp/more_graphs_20261027/current_d4_1818_rows.json`并非1818点图：实际是六条Wiki更新，含一个13D5、三个11D4、两个12D4记录，没有9D4或n1818合法实例。不得以“1818”文件名修正主表1768或计新成果。这里的9D4不是被排为一般无望，只是当前固定source append没有接口。

## 本轮决策

只推荐root考虑上面的8D5 phase-voltage必要门，当前不派发。fresh5334留有条件目标5500的166点窗口；这不是找到新图或声明成功概率。9D4固定保边范围保持STOP。没有使用过时D4描述页的小值挑题，也不退回旧2485源去追当前2556；本轮未定位新2556的实际source，因此不能给它编造迁移接口。没有机械重开H9前缀，也没有新的D3degree／k扩展。现有16389形式化收尾与本选题门分账，任何核内pilot进展都不把这个新8D5预测标成结果。

本note写入进程CPU：1.6452000000000133e-05秒；只有只读选题及纸面规则，没有新数值实验。
