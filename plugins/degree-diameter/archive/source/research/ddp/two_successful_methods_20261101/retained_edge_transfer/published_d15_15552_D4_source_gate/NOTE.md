# 实际15552源：有真实27点横截平面接口，仅建议一次controller门

**结论：值得root另行授权一个固定192点controller packing小门；本批未启动。** 唯一候选为每个所选controller取同一27点平面W={x1=0}，复制其完整原始simple邻域一次。要超过已定位16384，至少需要31个controller的五目标集合两两不交；条件点数16389，仅多5。没有现成31集合或新图，不把该条件写成成功。

## 真实来源和度数

公开源是[Zenodo23691325](https://zenodo.org/records/23691325)，实际作者literal URL为https://zenodo.org/api/records/23691325/files/deg15_diam4_n15552.txt/content。本地source15552.author.adjlist.txt和source15552.header.edges位于more_graphs_20261027/d15_D4_current15552/；DOWNLOAD_RECEIPT.json记录原实际下载1311860bytes，SOURCE_PROFILE/SOURCE_FACTS已绑定15552点、116316边、简单无向。实际degree14有648点，degree15有14904点，故不是15regular。D4沿用公开结果；该source profile明确没有重测source BFS。本门也没有重新解析边表或下载。

旧“连续81标签分块并非ordinary equitable”结论保留，但后来的loop-completed relation不同：只给648个degree14点各补一个virtual self-entry，所有行恰有五个目标controller×每目标三点。24个controller有此虚拟自关系。affine_relation_recovery/RESULT和独立数学接口ANALYSIS_AFFINE_CERTIFICATE记录全部960 directed arcs、77760实际rowsets精确匹配，而不是仅拟合basis。由此已恢复真实192×F3^4接口，不由15552因式分解猜测。

完整实际table是d15_loop_completed_quotient_probe/affine_relation_recovery/source15552_AFFINE_RELATIONS.json，generator.py可读取。局部标签x=sum_i x_i3^i，全局81*a+x。每条实际关系为y=B*x+c+t*v，t∈F3；只有整个global标签相同才删除virtual loop，同local offset但不同controller仍是真边。本次仅比较表内metadata，确见五种literal(B,v,c)且每个controller使用同五种类型；没有运行生成器、field、rank或BFS。

## 一个实际横截平面，而非模板清单

已保存signed5_frame_gate/REPORT和matroid36_induced_subset/PROFILE给五个rank3 input-kernel line代表（各controller只是重排）：

    (1,2,1,0),(1,1,1,1),(1,2,1,2),(1,2,2,0),(0,1,0,1).

其第二坐标都是1或2。因此共同normal=(0,1,0,0)对全部五条kernel非零，W={x1=0}是27点横截hyperplane。此次只读取已认证的kernel坐标，没有重算kernel/rank。对固定arc，W上两个不同中心若共有目标邻点，则它们之差落ker(B)；横截性强迫两中心相同。故同一个W的27个完整邻域两两不交。删除原virtual self-entry只减邻域，不破坏互斥。

唯一controller规则：T(a)为table中from=a的五个to标签。选择I使T(a)两两不交，再取所有( a,x∈W )为原源中心，各复制一次完整simple N14或N15。标签是81*a+x0+9*x2+27*x3。a=0的实际T(0)=[0,11,59,79,180]；必须保留0这个self-controller目标，不能拿删selfloop后的普通openN误替此五目标集合。不同所选controller的pins落不同fiber，故全体load≤1，原degree14/15升至最多15/16。fullN真Walk桥可在D=4使用：新旧、new-new路径都由源内点实现，无需中心独立；源最小度14保证无isolates。该逻辑只给条件构造，不是本次实际D4验收。

这个接口与成功C30/F4³方法相同之处是“横截plane＋控制器目标邻域packing→完整N互斥”；区别是这里F3^4、27中心/块、五个实际线性关系且带24个self-controller relation，不能套C30的96中心证书或4port/no-loop结论。

## 按真实度数重算预算

cap16的原点总spare为648*2+14904=16200。若M=x+y新增点分别复制degree14/15中心，必要14x+15y≤16200，直接M≤1157。SOURCE_FACTS的minSatN=12意味着每个中心至少有一个degree15邻点，而那些旧点只有一个spare，故任何中心不能重复复制；因此x≤648并得到M≤floor((16200+648)/15)=1123，最终n≤16675。这都是例行预算，不是新定理，也不证明可达。原15regular的floor15552/15=1036不适用。

超过16384至少新增833点。完整27-plane块需31块，得到837新增点、条件n16389。每个T(a)恰五点，纯计数至多38个互斥块，条件n≤16578。下一小门应严格只问固定actual192-controller上是否存在31个两两不交T(a)，不扫其它source/field/planes；本门不运行packing。若该门失败，仅关闭这个完整27-plane/互斥目标块充分规则，不排任意点级非矩形中心、free顶点load2利用或一般(16,4)。

## 继承旧范围

旧原cap15单helper的all648 free-pin R3覆盖、完整individual-pin覆盖、K2合作、K8共同骨架等保持UNKNOWN，不续timer；它们只允许degree14旧free pins，不是本次raised-cap complete-N复制。原有inversion/five-line/canonical negatives主要是rawUNSAT的限制域，未提升为独立全排。signed5-frame反例只关其binary transfer前提；36-point induced图实际D4失败只关该诱导规则；rank-one reflection quotient的闭范围也只关两intrinsic choices。已读这些实际source/recipe reports未找到此192-controller完整27-plane fullN packing的exact结果或严格排除，故不宣称旧UNKNOWN可外推本门。

本批0新图/参数/Lean，0源生成/边表解析/BFS/field/rank/solver/packing/新query/download/paidreview/hash；未改root、Wiki、专家/冻结包或source17文件。primary的作者名/首发日期不在这轮重新查询范围，未凭Zenodo编号编造。global/priority仍UNKNOWN。
