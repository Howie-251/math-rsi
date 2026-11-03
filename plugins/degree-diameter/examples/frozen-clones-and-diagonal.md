# 完整迁移案例：7242→7531→7532，之后冻结G1

## 源与完整邻域克隆的正证明

真实GQ(4,4)有85点、85线和17条spread线。opposite未填图U阶7225，其中425个flag点度24，其余度25；每条spread线取25个incident flags，添17个filler得到7242点、全25正则、D3的H。已核的17点ovoid与17条spread线的乘积给289个中心。

中心诱导136条匹配边和17个孤点，不独立。但一个源顶点若同时邻接两个中心，line上的ovoid唯一性和point的spread唯一性迫二者相同。因此289个完整开邻域N_H互不交，共有7225个pins，新clone各度25，旧点负载≤1。

冻结这289个**H的原邻域**再增加clone，得7531点、97750边、最大度26、D3。相邻中心对应的新点之间有明确三步路线，不需要加强为中心独立。生成循环若读取`current(center)`，先前增加的clone会污染后继邻域，所得对象就不是此定理定义的图。

## 为什么不能机械续单点

固定7531图的余度点分成289个private classes，每个pin的两步覆盖只能服务相应类；单个新点至少需289个pins，超过26。NO只限同cap、保留旧边、单helper操作，不排合作helpers或改变旧连接。

新规则保留H全部旧边，但clone只取U邻域：省17条diagonal clone→filler边，另加hub连接全部17个fillers。得到7532点，边数仍97750。diagonal clone度24，hub度17，最大度26；全点对证明分别处理旧U、F、diagonal／off-diagonal clones和hub。hub邻域在F而clone邻域在U，不能把hub塌缩到某个H顶点套旧证明。

## 从当前任务工作区调用

按当前克隆设置 `DD_PLUGIN`。`--workspace` 和 `--output` 都明确写入任务下的新目录：

```sh
DD_PLUGIN="/path/to/MathRSI/plugins/degree-diameter"
TASK_DIR=$(pwd -P)
run_dir=$(mktemp -d "$TASK_DIR/dd-replay.XXXXXX")
python3 -B "$DD_PLUGIN/archive/source/constructors/late_graphs/rebuild.py" \
 --case d26_D3_n7531 --workspace "$run_dir/source" --output "$run_dir/g7531.edges"
python3 -B "$DD_PLUGIN/archive/source/constructors/late_graphs/rebuild.py" \
 --case d26_D3_n7532 --workspace "$run_dir/source" --output "$run_dir/g7532.edges"
```

这里是已核参数接口的可用重建入口，本次包装未再执行两图生成或BFS。原producer会在任务源副本写PRED、结果与graph，不写归档。生成不能单独验距，完整[ovoid证明](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/PROOF.md)和[一般diagonal证明](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md)承担路线量词。

## 放大时实际源是什么

重复k个diagonal blocks时，先闭实际G1，再克隆G1的全部首批新增角色——289个clones加首个hub，共290个角色；它们的完整邻域互不交。q8 balanced的G1则有4225个clones加hub，共4226个角色。后续86／90／94／98度实例都直接从G1出发，不链式使用另一个较高k图替代。

消费者读实际源版本、中心／角色标签与完整邻域绑定、旧边包含、负载和度数，以及各类点对由哪项定理承担。只缺新owner或label时不重编旧几何。新规则解除旧单点障碍，不会使旧7531图上的NO变错：它们排除的是不同操作。
