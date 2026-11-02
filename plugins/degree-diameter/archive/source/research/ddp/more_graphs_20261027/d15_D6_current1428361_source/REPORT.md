# (15,6) 当前 1428361：有余量，但无零／单满邻原型

唯一当前实际源已从 [Zenodo23691325 的精确文件](https://zenodo.org/api/records/23691325/files/deg15_diam6_n1428361.txt.xz/content) 下载并解压。压缩 39,667,016 bytes，literal 164,757,004 bytes；未替换成旧1426903、1424896、1424474或1424472。作者说明这是 R. Rajiv 的四份 H(11) incidence compound，加 cut matchings 与11113个顶点。本轮没有重建或验证完整几何 recipe，直接绑定这份当前 literal。

事前预测“至少存在一个只有零或一个满度邻点的原型”被实际数据反驳。完整一次 profile 为：

| 项目 | 实际结果 |
|---|---:|
| 顶点／边 | 1428361／10692016 |
| degree13／14／15 | 9312／22759／1396290 |
| free 顶点／总空位 | 32071／41383 |
| minSatN／达到点数 | 2／2 |
| minSatN 原型 | 323107、1323865 |
| 零满邻／单满邻原型 | 0／0 |

这里 SatN(v) 是 v 的邻集中 degree15 点的个数。一个保留原图全部边、连接到整个 N(v) 的普通 false twin，要求 SatN(v)=0；本源没有这种原型。继承的单满邻替代入口也没有实际对象。32,071 个 free 点本身不保证存在最多15 pins 的完整闭 R5 cover。

按冻结规则，minSatN≥2 即停止：没有启动 proxy、guard、R5 球缓存、solver 或新候选。此结论只关闭当前 literal 的零／单满邻原型入口，不排除不同连接规则、多个替代点或一般更大 (15,6) 图。

原生程序设 RLIMIT_CPU=10，实际 2.06118 CPU 秒；编译 0.702424 秒，解压 3.638449 秒，准备加 profile 合计 6.429542 秒。单一下载耗时 103.914 秒，未并发重下。已知源 D6 继承公开来源，旧源 BFS 为0；新增图、R5球与 solver 均为0，actual_D 和普通无序坏对保持空。

证据：[冻结预测](PREDICTION.json)、[来源绑定](SOURCE_FACTS.json)、[完整统计](SOURCE_PROFILE.json)、[终态](RESULT.json)、[下载记录](SOURCE_RECEIPT.json)。程序为 prepare_source.py、profile.cpp、run_profile.py。
