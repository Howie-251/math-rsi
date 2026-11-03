# 程序、工作副本与可移植重放

以下从**当前任务工作区**执行。先按正在使用的 MathRSI 克隆确定插件绝对根；将示例中的 `/path/to/MathRSI` 替换为该克隆的真实路径，不使用作者机器路径：

```sh
DD_PLUGIN="/path/to/MathRSI/plugins/degree-diameter"
TASK_DIR=$(pwd -P)
```

后续代码块沿用这两个变量，无需切换到插件目录。程序由 `DD_PLUGIN` 定位，`--workspace`／`--output` 都在 `TASK_DIR` 下的新行动目录；只读证书结果输出到终端。归档是历史输入。原作者脚本若会写本目录、使用旧 ROOT 或依赖省略数据，应先按下文准备任务副本，不在归档中直接执行任意 `run_once.py`／`compile.py`。

## 1. 已有可移植构造器

[constructors/README](../archive/source/constructors/README.md)描述153named、103earlyD5及50latecase。`reproduce_index.csv`和`late_graphs/cases.csv`给完整caseID与格式；原catalog中的路径是历史工作区路径，不是所有大edgefile已随包。

```sh
python3 -B "$DD_PLUGIN/archive/source/constructors/late_graphs/rebuild.py" --list
```

它只列50case与adapter，不生成图。大图原text直接索引108份约3.58GB，完整包本身以输入／配方／小表代替；没有为维护重建它们。最大case414132点/19680570边，文本约265MB，不能因`rebuild`一条命令就忽略输出成本。

### 真实小构造：F4原参数，无新SAT

```sh
run_dir=$(mktemp -d "$TASK_DIR/dd-replay.XXXXXX")
python3 -B "$DD_PLUGIN/archive/source/constructors/late_graphs/rebuild.py" \
  --case d20_D3_n3840 --workspace "$run_dir/source" --output "$run_dir/g3840.edges"
python3 -B "$DD_PLUGIN/archive/source/constructors/late_graphs/rebuild.py" \
  --case d22_D3_n4192 --workspace "$run_dir/source" --output "$run_dir/g4192.edges"
```

rebuild将materials复制到工作树，改原wrapper的ROOT常量，按依赖构建3750／3840等source。使用savedparameters／Nrecipe，不调用原SAT／MIP、Lean或网络。`--output`要求新文件，`--workspace`中的已有source会复用，因此新配方／参数核查用干净目录，不以旧output冒认此次生成。

两个输出有`n m`header，生成不能单独证明D3；使用完整原route／clone证明及相应字面绑定。此命令适合检查输入闭包；不是本插件默认自动验整个portfolio。重放相同规则不计新图或新数学。

### GQ小例及真正diagonal编辑

```sh
run_dir=$(mktemp -d "$TASK_DIR/dd-replay.XXXXXX")
python3 -B "$DD_PLUGIN/archive/source/constructors/late_graphs/rebuild.py" \
  --case d26_D3_n7531 --workspace "$run_dir/source" --output "$run_dir/g7531.edges"
python3 -B "$DD_PLUGIN/archive/source/constructors/late_graphs/rebuild.py" \
  --case d26_D3_n7532 --workspace "$run_dir/source" --output "$run_dir/g7532.edges"
```

依赖7242 incidence／spread／P17中心输入，第二项在7531 parent上donate17edge并加hub，不能用purefullN的旧图身份代替。它会生成必要旧source，但无新几何搜索。currentR2等原producer有限校验可能执行，若用途只需解析证书不必调用图重建。

### D5的当前覆盖重放

```sh
python3 -B "$DD_PLUGIN/archive/source/constructors/early_d5/verify_covers.py"
```

无`--output`时仅读三份压缩bases及families.json，输出103步每次degree／当前B4并检查。继承原baseD5，未跑每个prefix全部roots。需要文件结果时将`--output`指向任务目录。reproduce.py的接口：

```sh
run_dir=$(mktemp -d "$TASK_DIR/dd-replay.XXXXXX")
python3 -B "$DD_PLUGIN/archive/source/constructors/early_d5/reproduce.py" \
  --degree 12 --order 42402 --output "$run_dir/graph.edges.gz"
```

原family_generator默认历史PROJECT不portable；packagedreproduce负责提供compressedsource，优先用它。

## 2. 小证书适配：Mizuno exact dual

```sh
python3 -B "$DD_PLUGIN/tools/replay_mizuno_dual.py"
```

标准库；默认本插件archive/source，可用`--source`指定同样结构的任务副本。stdout给364columns/min10001/Q10000/RHS2061908/bound515477/2500/T≤206；失败assert即不接受。无solver、graph、Lean、hash与源写入。本次确已执行，结果在[evidence](../evidence/IMPLEMENTATION.md)。几何必要模型仍是人读证明进口，不把算术checker当一般14D5不存在证明。

原`lp_exact_bound/verify_exact.py`缺`LP_INPUT.json`且会写EXACT_CHECK；本适配只从presentMODEL重建相同365declaredrows，不伪造原缺件或改变archive。原MODEL完整364列必须保留，不拿选定几个dual列当全表。

## 3. 其它原程序与已知依赖边界

| 原程序／family | 真输入与可用范围 | 调用前的具体处理 |
| --- | --- | --- |
| F4generate.py | savedPARAMETERS即可生成3840 | 用rebuild/wrapper；原Lean generate_lean.py另缺ROUTE_CERTIFICATE，不能宣称可重生成全Leandata |
| 3900/4125 literalchecker | 3750全根priorreceipt与两terminalgraph | 原ROOTparentdepth／graph_file绝对绑定已过时，scratch显式适配；不直接跑archive |
| 20580literalchecker | 完整20580edgefile | package只有可重建输入；checker写localreceipt，先scratch放实际graph；本次未重跑全部根s |
| F9U6/U10 | 56862source、typedcenters、immutableN | rebuild准备source；8个F9case是body-only无header，从cases.csv取n/m |
| q7P33 | source160050＋1650center/64pinrows | C++17；请求一个case可能batch生产8或7输出，确认成本和副本位置 |
| q8source/copies | TABLES、OVOID、DELTA及G1 | C++17，先342290→346515→346516，再higherroles；不链错86/98为下一source |
| D4plane837/864 | actual15552adjlist＋I31/I32＋plane | 源degree14/15不统一15；rebuild可用，不跑packingsearch |
| global256gate | actualRIGHTgroup、完整枚举C++ | 缺历史TSV，可scratch重建完整table；预算不够返回UNKNOWN，不能接受NO |
| D2one-repairanchor | archive只有PRED/HANDLE/TERMINAL | 缺详细RESULT、枚举代码和252witness；只能引用历史reportedclosure，不提供replay能力 |
| Leancompile.py | 旧Linux toolchain/LEAN_PATH/cache | 源码完整≠本克隆装好环境，按当前workspace固定toolchain/manifest适配，不写旧Mac/LinuxROOT为默认 |

部分从未命中的SAT positiveexport分支未strictlex排序，归档证据中的NO不受影响；未来若成功应按实际edgeformat规范导出、核验，不能把未执行branch描述为testedproducer。

## 4. 当前任务怎样调用而不改归档

复用现成rebuild时它已创建scratchsource；不需再写统一runner。直接用某原脚本时，先读依赖和写入，复制必要输入闭包到当前taskrun目录，改该副本路径／输出位置，记录改了什么。依赖缺失则准确缩小能力，或由已有presentdata作透明输入适配；不以相近旧源替代缺的实际源。

命令退出0只支持其真实检查：生成、字面绑定、currentcover、exactdual、BFS、kernel分别记。保存实际cwd／argv／exit／结果和输入意义，不因copy或文件数提升历史数学状态。实际授权只核接口时，不恢复旧研究、solversearch或大图验距。
