# 全部648端口与15552目标的K8共同骨架整数模型

本目录只准备了完整整数可行模型，没有调用solver、着色、源图读取或BFS。唯一成功准备PID423591，0.354100389 CPU秒；矩阵15553行×648列、1497528个非零项，约7.49MB，数组269442字节。初次命令仅Python语法解析失败，未开始任何准备或数值操作；修正多余右括号后完成本次唯一实际准备，未重复读取/构建一个已完成矩阵。

## 固定操作和模型含义

继承已验15552点、最大度15、直径≤4的源图G。全部648个可用旧端口均degree14、余度1。拟新增八个彼此相邻的helpers，构成K8；每个helper接八个旧端口，八组互不相交，共选择64个旧端口T。新helper度为7+8=15，旧点至多多一条边，最终目标阶数15560。

固定每组恰八点没有损失：若某个合法K8方案每组至多八点、合计少于64，可用尚未使用的648个余度1端口补满各组；不超度，也不会增大距离。因此这不额外排除使用较少端口的同一K8操作。

T尚未分组时，一个旧目标t若被T的某个R2球覆盖，则无论八色怎样分，该目标都被全部helpers在四步内覆盖：命中端口的本色helper走直接路线，其余helpers先走一条clique边。若t完全没有T中的R2提供者，则每个色组须有R3提供者，至少需要八个不同的T端口。

因此未着色的准确必要门是：

```text
z_p∈{0,1}，p=0,…,647；Σz_p=64；
对每个旧目标t： Σ_{p∈R3-support(t)}z_p
                 +7Σ_{p∈R2-support(t)}z_p ≥8。
```

R2支撑逐项包含于R3。当binary R2-count≥1，R3-count亦≥1，左边≥8；R2-count=0时条件恰为R3-count≥8。因此整数行精确等价于“R2命中，或R3提供者至少八个”，并非把分数松弛误当离散OR。

本模型只判定T的必要门，不能单独产生完整图。若T可行，令U为没有选中R2提供者的全部旧目标；下一步须将64点分成八组、每组八点，使U的每个选中R3支撑均含全部八色。支撑超过八点时允许颜色重复，只要求每色至少出现一次，不是强迫所有点颜色两两不同。给定T着色失败仅排该T，不排其它T或整个K8。

## 数据和逐行布局

全部输入继承../d15_D4_K2_route_gate/已绑定缓存：target_R2_support.u64le.bin及target_R3_support.u64le.bin，每目标11个小端uint64，bit p对应FREE_ORDER第p个旧标签。15552行和全部648列完整保留，无LP支撑筛选、成线/纤维限制、额外对称或target抽样。

prepare.py只导入NumPy和scipy.sparse，不导入或调用优化器。它核缓存长度、648之后padding、R2⊂R3、原标签顺序，以及各列R2/R3球大小191/2310，然后保存：

- constraints.csc.npz：int8 CSC矩阵A；第0行全1，第t+1行对应旧目标t。目标系数为R2支撑中的8、R3\R2中的1，其余0。
- model_arrays.npz：objective=0，integrality=1，变量bounds[0,1]。第0行lower=upper=64；其余lower=8、upper=+inf。另保存old_labels。
- SELECTOR_MAP.json：零起始列、字面旧标签、余度1。
- INPUT_SCOPE.json：输入绑定、布局和实际生成操作。
- MODEL.json / PREPARE_TERMINAL.json：真实prepare终态。

所有R3列大小均2310，所以目标块非零数648×2310=1496880，加首行648，合1497528。系数1/8和所有阈值都是精确小整数；求解时转换float64不会改变这些数。

## 已写但尚未执行的单次求解入口

solve_backbone_once.py必须显式指定--solve才会运行，默认一次HiGHS time_limit45秒，最多允许60秒，process CPU硬限70秒。它通过scipy.optimize.milp/HiGHS作feasibility-only求解，OMP/OpenBLAS/MKL均单线程，向HiGHS传threads=1，保留实际raw状态。

真整数incumbent须在原int64矩阵上检查全部15553行、cardinality64、0/1边界及整数误差，再保存BACKBONE_CANDIDATE.json的columns与旧标签。不把raw solver文字直接视为候选。该脚本不自动着色、生成图、重算球或续另一个T；root可审阅后将它纳入总≤90CPU的一次骨架加着色批。

```text
python solve_backbone_once.py --solve --time-limit 45
```

上述命令尚未运行。UNKNOWN停止本批；若HiGHS声称不可行，只按本必要模型的实际raw结果保存，不冒充LRAT或Lean证书。本目录不引入更多clique尺寸，也没有重启旧K2批。
