# q8三图：可迁移复现说明

归档模式；完成情况以旁附FREEZE_RECEIPT为准。当前SOURCES是原repo相对路径映射；仅拿到这些小文档还不是离线材料包。本次归档要求包含三终图及两classical unfilled输入，raw共909069434bytes。旧P33包不属于本材料。

阅读主HTML及同字节.html.txt；Word为原生Office XML。目录迁移应保留research/、formal/和expert_review_current/相对结构。以下是供专家主动选择的未来重建命令，本次prepare没有运行任何命令里的构图/核验/Lean，也不会安装依赖。

## 只重建80／81源

需已有Python3/g++。将AR4MATH_ROOT设为解包repo根目录，先设Q8_SRC=$AR4MATH_ROOT/research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81。下列各行分别执行，输出全新目录：

```sh
mkdir -p "$AR4MATH_ROOT/replayed_q8_sources"
g++ -O3 -std=c++17 "$Q8_SRC/produce_sources.cpp" -o "$AR4MATH_ROOT/replayed_q8_sources/produce_sources"
"$AR4MATH_ROOT/replayed_q8_sources/produce_sources" derived "$Q8_SRC/derived/TABLES_INPUT.txt" "$AR4MATH_ROOT/replayed_q8_sources/derived" 30
"$AR4MATH_ROOT/replayed_q8_sources/produce_sources" balanced "$Q8_SRC/balanced/TABLES_INPUT.txt" "$AR4MATH_ROOT/replayed_q8_sources/balanced" 30
```

原生产run_once.py有防覆盖guard，不应指示在已含RESULT的原目录直接重跑。上述原C++入口显式输出新位置，保留input physical labels。

## 只重建82图

设置Q8_COPY=$Q8_SRC/balanced_full_ovoid_copy82，使用独立新cwd中的两份小input；source是已验balanced81，不能用Payne80或currentN：

```sh
mkdir -p "$AR4MATH_ROOT/replayed_q8_copy82"
cp "$Q8_COPY/INPUT_TABLES.txt" "$AR4MATH_ROOT/replayed_q8_copy82/"
cp "$Q8_COPY/OVOID_INPUT.txt" "$AR4MATH_ROOT/replayed_q8_copy82/"
g++ -O3 -std=c++17 "$Q8_COPY/produce.cpp" -o "$AR4MATH_ROOT/replayed_q8_copy82/produce"
cd "$AR4MATH_ROOT/replayed_q8_copy82"
./produce "$Q8_SRC/balanced/graph_d81_D3_n342290.edges" 30
```

这只重建图，不执行BFS；fresh verifier源码及实际完整日志/表在各independent_acceptance目录。source verifier须同时有两个classical unfilled文件作为输入，不能为缩包省略它们。不要把实际历史BFS范围改称全部旧根BFS。

## Lean与原环境

SOURCES列出四个original Exact/Audit seeds的递归repo-local imports；Mathlib第三方环境不随本计划复制，需已有Lean4.24.0和与formal/lake-manifest.json相符的已安装依赖。原FORMAL_ENV_COMMAND.json是历史元数据，绝对路径需在新机器替换，不能照搬。构建时以新输出目录承接.olean/日志，提供实际LEAN_BIN和依赖LEAN_PATH；不调用lakefetch、不安装、不覆写旧缓存。

当前source2 fullproof与82原目标状态从主稿链接的实际CHECKPOINT/FINAL读取。FINAL缺失时不称目标已闭合；单module PASS或pilot不等于整图kernel PASS。最终完整包只有fresh C实际返回且root另授权后才可冻结。

## 优先权

三图数学验收不解除exactsourcefill优先权UNKNOWN/JGT全文缺口。若同fill及接口公开，则当前64/65/65优势可归0。计划不含世界纪录证明。
