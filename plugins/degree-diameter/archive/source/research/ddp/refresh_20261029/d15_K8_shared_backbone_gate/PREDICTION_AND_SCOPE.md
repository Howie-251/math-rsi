# K8共同骨架的稀R2支持诊断

事前预测：5184个仅有3个R2 provider的旧目标可能重复少量几何槽，而非5184个互不相关约束；同一三元组的目标可能共享R3的fiber占用结构。本批将报告精确重数，允许该预测被否定，不预设三元组同fiber、共线或为旧selfline。

唯一构造规则仍为固定15552源上新增K8；八组互斥旧free pins各至多8，必要充分条件是每组 R3(A_i)∪R2(T)=V。可补满每组8而不损失解；共同T大小64。未启动该整数构造模型。

本诊断仅从已有FREE_ORDER及target_R2/R3_support二进制转置缓存读取：筛出完整5184条R2支持大小3的行，按三个实际literal提供者精确去重；核同一81点fiber及F3^4仿射直线，统计648个port的不同三元组/带目标重数覆盖；对这5184个目标统计实际24个freefibers的R3 provider数向量和非空fiber集合，检查相同R2三元组内及全局共享情况。

输入标签为81*controller+x，x按little-endian base3解码。没有独立fiber平移假设；已知纯平移核为零，不能据几何共线直接合并不同literal覆盖列。仅保留完整literal支持接口，后续是否建模由root决定。

预算单worker≤5CPU，一次运行；不读源边、重算距离球、BFS、solver、LP、枚举helper数或构造新图。不计算任何哈希。
