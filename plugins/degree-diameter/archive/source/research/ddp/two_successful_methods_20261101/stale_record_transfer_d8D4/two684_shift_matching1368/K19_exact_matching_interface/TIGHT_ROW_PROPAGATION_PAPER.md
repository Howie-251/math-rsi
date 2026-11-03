# capacity19行的derived overlap binaries
仅paper，0data/source/数值/BFS/solver；固定σ，沿用原exactly-one shifts与实际point-coverage OR。
该行选中packets总大小恒19，且原OR迫其union=F19；故每个点出现恰一次，选中不同packets必须两两不交。
因此对r≠s且rot(B_r,t)∩rot(B_s,u)非空，¬Y(r,t)∨¬Y(s,u)是原CNF的logical consequence。
必须比较不同r；不能把同一个被选packet与自己相交错误变成禁止它的unit。
追加这些原变量上的binary不删任何原SAT解，也不新增解；无需新变量，fixedσ/gauge/domain均不变，只增强传播。
若capacity>19，重叠可与满覆盖共存，以上推论不成立；不得把此限制施加到非tight行。
实际localtiling witness应满足全部这些binary；此小check只核本行后果，不说明其它coverage行可同时满足。
binary在全packet共同平移下不变；若witness以最大packet shift0表示，可整体减其t0对齐原t0=0再比，不叠两个gauge。
原local不可tile预测已被witness反驳，但不影响这些binary的正确性，也不产生actualmatching graph。
新窗口的rawstatus另存；原fixedσ20s UNKNOWN历史保留，不冒原solver已UNSAT或fullK19族NO。
本次仅授权同σ等价CNF的有限传播加强，case成本不重置；结束STOP，不σ2/新field/新模板或成果计数。
