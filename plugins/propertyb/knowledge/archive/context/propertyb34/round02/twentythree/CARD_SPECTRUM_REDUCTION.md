# 五低与六低提升：以一、二阶矩代替完整残型重标号

## 数学缩减

对重数函数 μ，令 C_k(μ)=Σ_{|T|=k} μ(T)。真实输入满足
C_k(count(H,f))= #{e∈H.edges : |lockSignature(f,e)|=k}。
改变锁标号不会改变任何一条原始边的迹大小，因此保持全部 C_k。
该恒等式按原始边计数，允许不同边产生同一迹。

`TwentyThreeTraceShape.cardMass_actual`、`cardMass_relabel`、
`cardMass_of_relabelled_counts` 已以一般 Fin n / Fin v 参数证明；
`trace-shape-spectrum-r1.log` exit0、1.97秒、标准三公理。

五低严格排除后的两个残型的大小谱是
(12,16,4,2,0,0) 和 (13,13,7,1,0,0)。任一真实五锁子集
由实际分类获得一个残型及置换，再用上面的不变性获得此必要条件。
六锁提升不再在每次删除中寻找120个置换，只检验这两种大小谱。

## 完整输入与剩余

原容量剪枝域不变：两个旧残型分别有1835、3028个容量向量；
实际所有中心超额条件过滤后分别264、516个，共780个。
对每个向量，若某个五点删除不符合上述两谱，就指定该删除作为拒绝义务；
若所有删除都符合，仍只有6+7=13个输入，均属于原来的三个六锁轨道。
这不是把全域缩成抽样；整个原容量域由同一个 `actual_mem` 覆盖。

`generate_low_promotions.py` 已在全部780个输入上复算此结论，
`LOW_PROMOTION_EXPORT.json` 标记 projection_gate 为 size spectrum only。
正式完整内核覆盖仍由两个 SixLowPromotionCoverage 模块承担，尚待构建。

只有13个新标号置换实际被目录使用，现仅保存这13个置换及各自单射证明，
不再保存720个全排列。无需证明所保存的置换穷尽所有置换：每个存活输入
只需一个能把其重数送到明确代表的具体见证，coverage 对它逐项核对。

`SixLowActualProbe.lean` 对新Data和完整实际调用连接做了条件接口测试：
只将旧五低分类与完整coverage作为显式参数，其他实际H、投影、谱不变性、
容量成员、全部重数恢复及重标号均使用生产证明。
`six-actual-probe-r1.log` exit0、3.49秒、标准三公理。
这不替代尚待正式构建的分类和数值模块。

## 四低到五低：二阶矩恰好补足一阶信息

仅把上述大小谱方法移用于4→5时，901个满足实际中心预算的输入会剩249个，
比原54个多出195个。因此不能直接使用一阶谱。

进一步令 M_{k,p}(μ)=Σ_{|T|=k} μ(T)^p。M_{k,1}即大小谱；
M_{k,2}记录同一迹类型上重数的聚集程度，也可解释为具有相同k元迹的
有序原始边对数（含自配对）。重标号只是双射地置换类型集合，故任意p的矩均不变。
`cardMoment_map`、`cardMoment_relabel`、`cardMoment_of_relabelled_counts`
已在任意Fin n / Fin v / 自然数p上证明，轻测2.61秒、标准三公理。

对全部901个可行五锁输入，仅要求每次四点删除的一阶及二阶矩
属于某个旧四低残型的对应矩，恰好保留原54个输入、12轨道，额外输入为0。
完整独立复算在 `analyze_four_projection_invariants.py/.json`。
三阶以上不再减少此域，无须引入。生产生成器已改为这一必要条件，
每次拒绝只指定一个四点删除，并由Lean核验该删除的矩条件足以排除。

旧四锁classifier返回真实H上的残型和置换；矩不变引理因此从实际输入
构造新的必要条件，不把矩条件留作最终外部前提。新目录只保存实际使用的32个
新置换，删去原120个全排列和24个旧置换的穷尽检查。
`FiveLowMomentActualProbe.lean`包含新Data、一般矩引理、真实旧classifier与actual全链，
仅目录coverage作为显式参数；`five-moment-actual-probe-r1.log` exit0、4.80秒、标准三公理。

## 性能记录

旧全残型版本的 `FiveLowPromotionCoverage0` 处理731个容量向量。
运行到4分54秒仍未完成，由主代理精确终止该Lean子进程；
Lake最终记录exit143、307.47秒墙钟，不计PASS。
保留 `TwentyThreeFiveLowPromotionCoverage0-build.log`，不得将取消视为数学错误。
这次转向使用一般计数不变量消掉昂贵的重标号比较；新coverage尚待正式pilot，
不据生成器速度或轻量caller通过宣称已有实测加速。

## 当前最短构建链

逐个正式构建 FiveLowPromotionCoverage0…7 → Numeric/actual →
FiveLowClassified → SixLowPromotionData → Coverage0/1 → Numeric/actual →
SixLowClassified → ManyLowComplete。
已有 strict 数值模块可并入对应阶段，但重核验由主代理单一调度。
最终原始分支仍为 H23、点对覆盖、34边、至少七个六度点⇒PropertyB，
不在最终签名保留残型、大小谱、概率或coverage作为前提。

## 稳定的核验输入版本

旧残型的期望矩/谱以小常数表 `expected` 保存，`expected_correct` 内核检查其
与原始残型重数一致。这样完整coverage不必为每个输入再次展开原50型目录。
5低Data+actual的最终接口复测为 `five-moment-actual-probe-r2.log`，7.91秒；
6低为 `six-actual-probe-r2.log`，4.96秒；均exit0、标准三公理。
接口probe统一由 `generate_actual_probes.py` 从生产源构造，coverage及未构建的旧分类
仍显式参数化，不作为正式分支验收。此版本冻结，先测正式Coverage0后再决定性能修改。
