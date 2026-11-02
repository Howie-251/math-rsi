# 当前42345基图的全域 Q-line 度数池：609组

固定已独立验收的42345点、245253边、最大度12、直径5图，复用41356-core fold映射，对全部66430个flat-plane中心、5380830条非H9奇异Q-lines重新检查**当前完整base度数**。得到611条原lines，对foldedpins去重后 **609组**：596组10pins（余2个anchor名额）、13组8pins（余4个名额）。其中605组不属于原来的7-item池。完整候选与见证已交root决定下一明确构造批；本轮没有任何R4、BFS、anchors补全或新图。

这是新base下的整体degree筛，不是重复旧52569线候选的覆盖搜索。原42342source之后3个新增点的度消耗已纳入current42345边表；core fold本身保持不变。

## 实际规则与计数

迁移上一批已校准的native枚举器，只改fold映射、当前degree输入和cap12，N11历史文件不动。每中心由六个Plücker式加polarB取3维核，选择basis(y,x,z)，生成dual(1,a,b)的81条外线。原lines按唯一中心不重计；每条遇到任一满degree12的实际pin才早拒绝，幸存者必须处理完整10个原points，再canonical pinset去重并保存完整line witness。

| 项目 | 数量 |
|---|---:|
| 中心，全部新base重筛 | 66430 |
| 原始非H9 Q-lines | 5380830 |
| 因满度pin排除的原lines | 5380219 |
| degree可行原lines | 611 |
| 原line像大小10 / 8 | 598 / 13 |
| 不同foldedpinsets | 609 |
| 重复可行foldedpinsets | 2 |
| 不同10pins / 8pins | 596 / 13 |
| 剩余anchor名额2 / 4 | 596 / 13 |
| 实际生成并degree检查的points | 7637627 |

原pool1、2、3、6仍在该degree池中；它们的旧coverage失败已按source_n与status标注，**本轮没有重试**。原1/2/3的失败base为42343，后来shortcut可能改变可行性但未据此猜测或自动重跑；原6的失败base也是42345，明确标记same_currentbase，不能当成未测试项偷偷恢复。其余605组才是原小池之外的完整新几何邻集。

## 真实成本与校准

1000中心profile为0.011042CPU秒，投影native全域0.769167秒；因低于预算，继续同一进程完整处理，没有重跑profile。实际native0.737731CPU秒，编译1.662746CPU秒，含current边表读取/degree准备总2.588419CPU秒，单worker，10CPU秒预算内完成。

对全部609个保留见证追加一次轻量Python geometry API对照，完整10个原point labels、foldedpins及现度全部MATCH，CPU0.072778秒，无距离检查。两阶段合计约2.662CPU秒。当前degree文件只是从已验边表得到的vertex-degree数据，不是新图；已验42343/42345产物均未改写。

## 输出与边界

`pool.json`每个record给pins、pin_current_degrees、anchor_cap/remaining_anchor_capacity，以及至少一条完整center/plane/dual/linebasis/10-point witness。`RESULT.json`、`profile1000.json`、`pool_calibration.json`保存完整计数和真实成本。`enumerate.cpp`是literal迁移源码，`run.py`保留从固定N11源码到本参数的可复现迁移过程。

degree可行只表示能保留旧边再接全部mandatory line像，既有统一几何保证只负责共同旧core覆盖；完整42345base还有extras，必须由后续完整R4及有限anchor判定覆盖。13个8pins项不能自动按两anchors处理，也不能未经授权扩到任意更大补全。此处不推测最终新图数、直径或参数界提升。

状态 `COMPLETE_GLOBAL_DEGREE_SCREEN`，pending为空；冻结预测“原7项之外仍有新degree候选”由605组证实。本轮到此交接，不按缺项分数调参、不恢复旧coverage范围、不加外审/依赖或哈希。原source及H9/partial-fold credit继承Dharunish Yugeswardeenoo与Rishabh Rajiv，当前42345扩张和验收见 `../h9_d12_followups/`。
