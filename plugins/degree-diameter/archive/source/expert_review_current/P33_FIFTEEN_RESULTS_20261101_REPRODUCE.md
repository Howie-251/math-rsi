# P33十五图：可迁移离线复现说明

本说明和入口只整理复现方式；本次交付冻结没有运行构图、BFS或Lean。原已验生成器、图和Lean源码不改。十五目标fresh C已实际返回，root已明确授权使用`--freeze`生成完整ZIP；冻结结果以同名前缀FREEZE_RECEIPT.json为准。

本P33归档固定保留140合法named实例／33参数／具体Lean34的审阅快照。后续live142／35及独立q8源图不属于本包。数学、Lean及绑定PASS；global／priority仍为UNKNOWN，冻结不消除文献缺口。

ZIP保留原repo相对路径。解包后进入同时包含`research/`、`formal/`、`expert_review_current/`的目录，设置：

```sh
export AR4MATH_ROOT="$PWD"
```

已有回执里的`/inspire/...`是原机器历史环境，离线复现使用下面的新入口或直接CLI，不要求该路径存在。本包含十五完整图、原source160050、全部本地代码／输入／证明／验证、递归本地Lean与环境元数据；Lean/Mathlib第三方安装另需已有匹配环境，入口不会安装或fetch。

## 阅读现有完整文件

打开`expert_review_current/P33_FIFTEEN_RESULTS_20261101.html`。十五张headered原始边表和source160050按原路径在包内，所有数学核心链接均为相对路径；无需sandbox下载链接。源码／证据计划在同stem的`_SOURCES.html`。

生产入口固定读：

```text
research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/graph_d64_D3_n160050.edges
```

它不是degree72克隆图。两个原producer的`CENTERS_INPUT.txt`也随包保存。

## 可选：用g++重建十五图

需要已安装的Python3和g++。输出是一个全新目录，原artifact不覆盖：

```sh
python3 expert_review_current/p33_offline_entry.py graphs --batch all --output "$AR4MATH_ROOT/reproduced_p33"
```

`--batch lower`只写65..72，`--batch upper`只写73..79。新入口仅把小文本center输入复制到独立工作目录，编译包内原`produce.cpp`并通过参数传入source路径；不改原C++，不BFS，不读取某个新图的current邻域。每个batch的CLI时间参数默认25CPU秒；原始回执及实际成本另见对应`RESULT.json`。

等价的直接CLI示例（低八；各行顺序执行）：

```sh
mkdir -p "$AR4MATH_ROOT/replay_lower/graphs"
cp "$AR4MATH_ROOT/research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/CENTERS_INPUT.txt" "$AR4MATH_ROOT/replay_lower/"
g++ -O3 -std=c++17 "$AR4MATH_ROOT/research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/produce.cpp" -o "$AR4MATH_ROOT/replay_lower/produce"
cd "$AR4MATH_ROOT/replay_lower"
./produce "$AR4MATH_ROOT/research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/graph_d64_D3_n160050.edges" 25 > PRODUCER_REPLAY.json
```

上七把两处`multiplicity65_72_family`换为`multiplicity73_79_family`，并用新的输出目录。不会生成degree80。

## 可选：在已有固定Lean环境重建Audit

需已安装Lean4.24.0，以及与`formal/lake-manifest.json`相符、已有`.olean`的Mathlib／依赖。`FORMAL_ENV_COMMAND.json`记录原环境，不能把其本机绝对路径照搬到新机器。按本机实际目录提供参数：

```sh
cd "$AR4MATH_ROOT"
python3 expert_review_current/p33_offline_entry.py lean --output "$AR4MATH_ROOT/rebuilt_p33_lean" --lean-bin /path/to/lean-4.24.0/bin/lean --dependency-lean-path /path/to/mathlib-and-dependency-olean-paths
```

多个依赖路径按当前系统的PATH分隔符连接。入口依本地import闭包拓扑排序，所有新`.olean`和日志只写新输出目录；不改源`.lean`或已验旧缓存，不调用lakefetch。完整重建的计算量与只查阅已保存的Audit回执不同，由专家自行选择；本轮交付没有执行这条命令。

## 优先权待核问题

JGT9(1985)325–334、DOI10.1002/jgt.3190090304十页正文尚未取得。专家应核查其中或直接后续是否已有同一opposite-GQ spread-fill pins及D3/负载证明。若公开filled160050源与同复制接口成立，十五个+50优势全部归零；图与Lean仍合法。数学C的PASS不认证世界纪录或最早归属。详细状态见包内`research/ddp/two_successful_methods_20261101/public_baseline_audit/SPREAD_FILL_SOURCE_PRIORITY_20261101.md`。
