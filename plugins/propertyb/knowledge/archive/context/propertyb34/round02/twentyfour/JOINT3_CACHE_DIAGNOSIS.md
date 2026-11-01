# 23点五低 Joint3：原数值证书的缓存求值

目标是让既有20布局证书接受Lean kernel核验，不改变布局、系数、配额或严格不等式。旧源为 `TwentyThreeFiveLowStrictJoint3Data/Numeric.lean`；既有源证书是 `context/propertyb34/round01/middle-math/EXTEND_LOW_23_5.json` 的group3，本目录 `JOINT3_SOURCE.json`仅复制这一条输入便于短探针绑定。已通过的SixLowStrictJoint1不修改、不重算。

新正规候选模块为 `formal/Aris4Math/ThirtyFour/TwentyThreeFiveLowStrictJoint3CachedNumeric.lean`。它先独立证明原 `data_valid`，然后使用已验通用 `CachedRows.rows_eq`，在同一真实profile上将 Numeric.boundA/B/C 改成六个剩余边大小的质量桶。`free_eq`、`a_eq`、`c_eq`对所有实际布局成立；`strict`最终恢复原MixedLayoutApplication严格不等式，惩罚项仍为原 `MixedLayoutCounts.penalty`。没有新证明假设、外部计算公理、搜索或候选域缩减。

短探针统一由 `run_short_probe.py`以20秒/4GB进程组上限运行。以下都是kernel证明，预期有理值来自既有JSON，数值绑定由Lean实际求值检查：

| 探针 | 实际范围 | 秒 | 峰值组RSS | 状态 |
|---|---|---:|---:|---|
| joint3-valid | 原data_valid全部20布局 | 2.99 | 2.24GB | PASS |
| joint3-cached-api | data_valid及所有free/a/c语义桥 | 2.71 | 2.27GB | PASS |
| joint3-free0-cached | 第0布局所有自由位置之和 | 4.61 | 2.64GB | PASS |
| joint3-free0-old | 同一自由位置原ABC式 | 5.96 | 3.05GB | PASS |
| joint3-penalty0 | 中心0完整20布局原penalty=0 | 4.07 | 2.37GB | PASS |
| joint3-penalty0-computed | 同一penalty先把p函数整体改写为computed | 4.33 | 2.37GB | PASS |
| joint3-five-layouts-cached | 布局0、4、7、13、19全部自由和及5中心A/C | 15.89 | 2.79GB | PASS |

源全部保留，命令、退出码、RSS与日志同名 `.json` / `.log`。单中心惩罚不支持“每个中心都已验”；五布局通过不支持完整20布局strict已经通过。完整正规构建交主代理统一队列，未在本子代理启动。

旧写法 `simp only [p_eq_computed]`会改写可见的 `p l`，不会改写仍作为函数参数的 `a positions p`、`c positions p`中的p。缓存版显式展开cachedCenterA/C后，其p l都会被改写。旧中心探针首次因simp无进展退出，保留为诊断，不计数值核验通过。没有证据需要预计算共享坏对权重，因此本次保留原penalty定义。

生成器 `make_joint3_cached.py`生成新模块与基础探针；5布局整合探针独立保存为 `Joint3FiveLayoutsCachedProbe.lean`。后续若新Numeric正规通过，由23点所有者修改实际caller的import/open并同步其规范生成器，避免重复生成旧慢模块。

## 单体缓存仍未通过，改为逐布局证书组合

主代理正规运行单体CachedNumeric时，160秒已约13.2GB，按180秒限额停止；这说明五布局pilot不足以外推整式。原单体源码保存为`Joint3CachedNumericMonolithicBeforeBlocks.lean`。本子代理只读确认原PID64521/64522/64619均不存在后，才替换组合源码，未修改在运行文件。

规范新生成器为`generate_joint3_cached_blocks.py`（加`--assemble`安装最终组合）。模块依次为`TwentyThreeFiveLowStrictJoint3CachedCore`、`CachedRows0`至`CachedRows3`、`CachedPenalty`、`CachedNumeric`。Core保留原data_valid与通用rows_eq桥；每Rows块仅五布局，每布局分别核验其完整free及5个center的A/C值；Penalty保留原定义，五个中心各自证明为0。最终Numeric引用上述等式后只算小有理数表达式。所有布局、权重、μ、quota和实际调用假设保持原状。

较后布局15–19的完整inline Core+Rows3短探针`joint3-cached-block3.log/json`已经PASS：12.40秒，峰值3.41GB，rows_19标准三公理。这仍只是该块证据；全部分块及最终strict由主代理正规队列验收。

## 正规验收结果

主代理完整分块队列已全部PASS：Core3.30秒；Rows0/1/2/3分别12.52、12.53、12.41、11.96秒；Penalty6.67秒；最终Numeric2.88秒。合计62.27秒（分项墙钟之和）；原strict传递公理仅propext、Classical.choice、Quot.sound。相比旧Numeric600秒超时及单体缓存180秒超时，逐布局证明再组合是实际有效的最终修法。全部源码冻结；23点所有者继续实际H调用接线，不能把数值证书的完成写成该实际链已经验收。
