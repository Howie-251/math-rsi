# 完整小案例：F4共享chart失败如何成为实际3840图

本例供route-loop诊断、prove复现参数或verify核原图连接。它不是一次新研究或当前纪录认证。

## 输入与第一道判断

C60为简单五度控制器，每个fiber是64点的F4³，使用五条conic方向。原规则按五个port共享全局chart，反向port配对，自匹配port要求真正的线性involution。1260个距离恰为3且只有一条三步路线的控制器点对强迫中央turn满秩，但每条边的必要matching门都通过。这既未否定模型，也没有给出共同chart。

完整全局PGL域有60×60×16=57600项，无一同时覆盖3300个同层或非相邻控制器点对。NO只限固定conic、齐次、全局共享chart和真逆的范围；不排一般20度图或逐边chart。

## 新规则与证明

改为150条无向边各选projectivity，反向使用实际逆矩阵，解除自匹配port共用单个全局矩阵的限制。每条边48种允许映射，7200个选择变量及Sinz计数辅助变量，共14250变量、24450子句。每个必要点对的子句包含能实现任一实际满秩NB3路线的选择，不提前固定某条word。

实际SAT后重查完整CNF、300条dart的逆／方向／pencil及3300份rank路线，定义3840点、38400边的简单20正则图。相邻层由前后回退的平面并覆盖，共享同一个直接边中心；同层或非邻层选满秩word，将目标减去源路线中心后解三个noise参数。任意源坐标的量词由仿射线性证明，不是只测零坐标。Moore界401<3840或kernel中的0→6见证排除D2。

完整原证明在[逐边chart目录](../archive/source/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/)。后来的exact-domain证明还说明完整pencil在此固定齐次域中必要；不扩到offset或其它控制器。

## 从当前任务工作区重建

将 `DD_PLUGIN` 设为当前MathRSI克隆的真实插件绝对路径。新输出和所需源副本都留在本次任务目录：

```sh
DD_PLUGIN="/path/to/MathRSI/plugins/degree-diameter"
TASK_DIR=$(pwd -P)
run_dir=$(mktemp -d "$TASK_DIR/dd-replay.XXXXXX")
python3 -B "$DD_PLUGIN/archive/source/constructors/late_graphs/rebuild.py" \
 --case d20_D3_n3840 --workspace "$run_dir/source" --output "$run_dir/g3840.edges"
```

读取保存的PARAMETERS，不运行SAT。预期header为3840 38400，边表严格字典序、全部度20。本次插件实现已运行小重建并核这些字面属性，记录在[F4_REBUILD_INTERFACE](../evidence/F4_REBUILD_INTERFACE.json)。没有新BFS或Lean；历史全部3840根独验和kernel证据由原receipt复用，不能描述成这条命令自动验D3。

## 消费与后继

固定构图任务交完整公式、字面输入和路线证明给verify。研究全局chart失败的任务返回明确共享范围及释放条件，不重新开相同field／seed梯子。需要Lean固定目标时，走[实际caller链](../references/lean-and-representation.md)；SAT或三个basis的普通数值检查不能冒作kernel。
