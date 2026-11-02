# 实现与已完成的小语义核对

2026-10-18。供 [PLAN.md](PLAN.md) 的实现部分引用。生产未执行；本目录没有 `result.json`、`production.stdout` 或生产计时。旧 `cyclic5_h35_run` 的源码与全部结果保持原值。

## 生成、继承与父类回溯

[enumerate.cpp](enumerate.cpp) 保留旧生成器的两型 d、全部5040个排列的字典序、七个两色 mask 的互补 signature join、q 桶内的原插入顺序及实际 H/rho 公式。处理顺序改为 type1、type0；没有连通性条件、随机参数、同构剪枝或固定父类配色。

type0 的前116个相容组合只作顺序继承，不重新评分或回溯。依据为旧 [result.json](../cyclic5_h35_run/result.json)：前116项仅1项通过逐点 rho，且第116项正是旧固定 H；其 [packing_result.json](../cyclic5_h35_run/packing_result.json) 已完整检查70个六点 packing，双色21111合格0。新 runner 读取这些实际字段核对依据；C++ 在第116项核对 p/q 端点与旧记录一致。结果分别记录 `compatible_pairs_seen`、`skipped_inherited`、`checked_this_run`，不会把继承项算成新检查。

每个新通过逐点 rho≤4、总 rho≤130 的 H 立即进行完整六点回溯。候选按顶点递增选择，每次只删除 H 距离≤2的后继点；只按剩余顶点数不足作搜索截断。故每个 H² 独立六集合恰访问一次，不要求 A/P 保持 C5。

对每个六集合 A，从真实六闭邻域取 P=Z\N[A]，并在同一 H 上检查：A 两色重数21111；P 独立；P 每点 rho≤3；全部30对 A/P 已由 H、H²或两种同色关系覆盖；每个 a 的 R(a)\A 和每个 p 的 R(p)\P 大小至多5且 H 独立。源码没有加入一般规范化正文之外的额外剪枝。六闭邻域恰占30点及 P 是双色横截面由已满足的 packing、四正则和局部双色条件保证；独立检查器也直接核它们。

失败继续当前 H 的下一个 A；当前 H 全部失败后继续下一个相容 p/q。首个全通过对象保存 `candidate.edges`、`candidate_parent.json` 及结果中的 H 参数、A/P。它只是必要前端，不是完整61点图。

## 预算与完成性

[run.py](run.py) 只启动一次单线程 C++ 子进程，限制为单 CPU 亲和性、30 CPU秒、45墙钟秒、4 GiB地址空间、单文件256 MiB。C++ 全局软限为27 CPU/40墙钟秒；q/p 扫描、相容组合及 packing DFS 共用该预算，递归内每至多256次轮询检查时钟，进入实际 packing 前另作立即检查。

`packing_started` 与 `packing_exhausted` 分开记录；仅实际穷尽当前 H 全部六集合才计入后者。`compatible_pairs_seen` 包含在预算边界处尚未完成父类检查的最后一个 H，不能把它解释成全部已关闭。`rho_pass_this_run - packing_exhausted` 可显示已见但未关闭的通过 rho 对象；找到前端也不关闭其整个 H 或来源范围。

只有两型均完成全部 join 与所有对应 packing（包括有依据继承的前缀），才输出 `EXHAUSTED_NO_JOINT_PARENT_FRONTEND` 和 `complete=true`。找到对象或任何软/硬资源终止均不标全族完整。硬停止来不及输出计数时，runner 保存 `complete=false`、`partial_counters_unavailable=true` 及真实退出/终止原因，不补造进度。已有生产输出或计时即拒绝重新运行，无自动重启。

## 独立验证与实际小产物

[check.py](check.py) 用普通35×35邻接矩阵直接算 H²、路线重复量、同色覆盖及 R 集合，并用普通集合检查 A/P；不导入 C++ 位集实现或依赖其 rho 快捷公式。找到的实际边表还与参数公式逐边核对，A/P 与保存文件一致后才能得到 `PASS`。

已运行 [sanity.py](sanity.py)，实际输出保存在 [sanity_cpp.json](sanity_cpp.json)、[sanity_check.json](sanity_check.json)、[preparation_timing.json](preparation_timing.json)：

- 两型共4个实际小例的70条边、全部度数、两色局部条件、交矩阵与直接 rho 均一致；含两型合法配色、一个不相容配色和旧固定 H。
- 旧固定 H 的 C++ 完整回溯恰70个六 packing、双色合格0。另一份普通闭邻域集合回溯也恰70个；全部70份 A/P 和每个判定字段逐一一致。
- AP 覆盖有明确真/假点对。Rout 使用旧 H 的根0：余集 `{17,21,22}` 独立且大小3，通过；`{21,22,29}` 含边21–29，失败；原8点余集超过5，失败。这些只验证必要谓词，不声称这些探针父集合构成前端。
- DFS 在第2节点触发仅供 sanity 的确定性中断，得到 `limited=true, complete=false, found=false`，未伪报穷尽。

编译无警告。实际子进程时间：编译1.219791 CPU / 1.224577墙钟秒；C++小语义0.003682 / 0.005126秒；Python直接核对0.064511 / 0.065776秒。没有生产计算。

## 待执行命令

根目录下，小语义入口为：

```sh
python3 computations/dd82/n61/cyclic5_joint_parent_run/sanity.py
```

这次小语义已经完成；无需无变化重跑。新鲜代理受平台线程数限制，改用根及现有Gemini直接源码复核；实际复核和根安排完成后，唯一待执行生产命令为：

```sh
python3 computations/dd82/n61/cyclic5_joint_parent_run/run.py
```

runner 会保存原始 stdout/stderr、`result.json`、`timing.json` 以及独立检查结果和检查计时；当前不执行这条命令。


实际状态更新：唯一生产现已正常完成，两型完整无合格父类；以上未运行语句是准备阶段记录，最新以RESULTS.md及原始result.json为准。
