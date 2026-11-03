# Mizuno十三度88452源：cap14全邻域克隆接口

## 实际结果

- 原拟81点超平面块统一失败；更强地，任意单fiber的完整N克隆中心最多27点。原因是四个输入方向正好是同一二维W的全部四条射影线；self-loop删除和删重不会解除共同邻点。
- 非异常fiber0的规范27块H0={x0=y0=0}也失败：普通邻域324点不交，但M制造27个load2冲突。
- 从该冲突导出的不变泛函修法成功：f=x0+y0+z，H={(-z,0,a,b,z)}。其27个中心的完整旧邻域并集351点，最大负载1，ordinary/M交集0，P0。明确局部标签保存在INVARIANT_FUNCTIONAL_RESULT.json。
- 尚无≥213块全局packing结果，因此没有新图或新纪录，也没有启动controller级求解器。

## 完整对象与来源

只取作者GitHub Contents API的degree13-diameter5/certificate目录中的CONSTRUCTION.md、generate_graph.py和controller_affine_chart.txt/main_matching.txt/spare_matching.txt。SOURCE_FETCH_RECEIPT.json保存取得路径与时间。作者generator仅阅读，未运行；未取压缩边表、未重复作者88452根BFS，也未读取或计算产物摘要。该source不是旧十四度图改标。

1456个A全部可逆；四目标fiber在全部364状态互异。28个self-port各有27个自环坐标，合756个P端点。M为182对fiber双射，336个仿射fiber/28个非仿射fiber；其目标总是普通目标之一。P为168条同fiber边＋210条跨fiber边，详细分布见STRUCTURE.json与P_EXCEPTION_STRUCTURE.json。

## 预测与修正

PREDICTION_AND_SCOPE.md先冻结“共同横截81超平面＋M/P容量模型”预测；实际证据反驳该接口，所以未运行71块模型。随后按根代理明确指示，只分析一个27点规范补空间；LOCAL_27_BOUND_AND_PROBE.json记录M冲突。INVARIANT_FUNCTIONAL_PREDICTION.md再先冻结一项不变泛函充分修法；一次121个f检验得到18解，确定性构造H并逐邻点核对成功。完整数学推导见PROOF.md。

## 成本、产物与范围

结构预处理0.54635031CPU秒；W及唯一规范27块分析0.060309449秒；P异常摘要0.000426523秒；不变泛函检验0.019830286秒，实测小代数部分合约0.62692CPU秒（网络取原材料单列）。全部单worker，明显低于120＋20CPU授权预算。

可复算源码为probe_interface.py、analyze_local_block.py、invariant_functional_probe.py；原作者数据在source/。机器结果在RESULT.json、STRUCTURE.json、COMMON_W_CERTIFICATE.json、LOCAL_27_BOUND_AND_PROBE.json、INVARIANT_FUNCTIONAL_RESULT.json。此目录不改主Wiki、Goal状态或Lean；所有本批任务均终态。

局部27块合法不等于完整扩张验收。一般完整N克隆、非线性W横截面、其它fiber与其它source未被失败的规范块排除；cap15的计数阴性也只属于这一固定source/完整N规则。


## 本批最终收束：原点域排除，九个局部仿射相位通过

后续尚未启动336线性块批处理前，零点门已严格给出sum x≤91：每个过原点块都占四个普通目标的零点。该域不可能达到213块，所以未做无意义的HiGHS调用。证据GLOBAL_LINEAR_ZERO_BOUND.json；这是固定原点块域上界，不是一般克隆数上界。

随后只对u0已成功的H检查9个W平移相位，全部局部合法，351旧邻点/maxload1。相位code2有一个M零点，但仍合法；若可选剔除它并要求非零相位，共7个单零点相位codes[1,3,4,5,6,7,8]。详细phase规则与每port的81点目标超平面方程见AFFINE_PHASE9_RESULT.json。

目前没有≥213块全局packing结果。真正剩余条件是：不同source块进入同一target的81点仿射超平面必须平行且错开；非平行必交27点。M/P还要另核容量。体积、zero或单块可行性不能代替这个联合条件。

新补充零点门与九相位检查分别0.010210343与0.032416924 CPU秒，全部有限代数检验计时合约0.66954秒（网络原材料取得另列）。没有启动336新扫、controller模型、图生成器或源BFS。所有任务已终态。


## 统一H跨source法向门的最终结果

新批固定同一个H及全部9相位，没有新H筛。336无self/P source中，21个M非仿射排出本局部域；315个仿射M均F=A_matching_port，其中105个source九相位全部有M冲突，210个九相位全过。

对210个可用source的840个普通目标incidence按实际81点超平面法向分组：350个目标最大同normal组h_b=1，14个为0。故4T≤350、T≤87（只上界、不声称达到），最多2349克隆、总90801，不能超过94186。没有运行controller求解器。

更保守地，未局部检查的21个非仿射＋28个self/P共49个source，即使各乐观贡献一个满27块，统一H九相位全域也最多87+49=136块、3672克隆、92124点，仍不足。这个推论没有声称异常source已通过；自选H、非线性横截面与不满块仍开放。

本批0.444907884 CPU秒，0solver/BFS/图。证明见UNIFORM_H_NORMAL_GATE_PROOF.md，逐source和target证据分别见UNIFORM_H_SOURCE_PHASES.json与UNIFORM_H_TARGET_NORMAL_GROUPS.json。统一H域现在停止，不自动派发source-dependent H或全局点级搜索。
