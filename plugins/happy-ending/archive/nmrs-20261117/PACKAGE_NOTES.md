# 打包范围、来源与边界

本包是2026-11-17现有研究快照的离线阅读交接；原研究目标与接受状态不变。源文件按原字节保存在source/，SOURCE_MANIFEST.json逐件列出SHA-256和字节数。HANDOFF.md只重写链接目的地，reading/页面只作阅读派生，不另立数学正文。

## 选择范围

从现用交接的所有直接本地Markdown链接出发，递归收集相关材料；另补E21完整checker、milestone9展开目录、五锁块q5、旧pivot-rows完整有限证据、两份历史PDF及公开八参数15文件子包。包括必要的历史证明、CNF/DRAT和失败边界；未把整个仓库、私有缓存、连接配置或全部运行目录打包。全文件清单见FILE_INDEX.html。

## 历史相对路径漂移

下面三处旧文中的链接原本失效。原件保留不改；阅读派生页链接转向实际canonical原件：

- `.trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md` → `.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md`
- `.trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/09-03-35-state-cardinality-charging/research/cardinality-semantic-simplification-20260927.md` → `.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-semantic-simplification-20260927.md`
- `.trellis/tasks/10-19-nr7-structure-capacity/reports/state_charging_qgt_two_slot_hall_20260901.md` → `reports/state_charging_qgt_two_slot_hall_20260901.md`

其余解析到的 Out_c、In_c、表达式、v、w 为公式或语法示例，不是缺失文件。历史原件中其本来失效的相对链接仍可借上述映射查找。本文不把源文失效链接伪装成原历史路径存在。

## 排除的控制面噪声

因与数学结论无关而未收入下列传输文件；离线阅读页不为它们制造失效点击：

- `.trellis/tasks/10-19-nr7-structure-capacity/research/evidence/shallow-support25-20261114/transport.ps1`
- `.trellis/tasks/09-03-35-state-cardinality-charging/research/evidence/c9-c10-accepted-20261022/download_manifest.json`
- `tmp/d7_tau_critical_20261027/upload_published_D26_sources.json`
- `tmp/d7_tau_critical_20261027/fetch_published_D26_results.json`
- `tmp/d7_tau_critical_20261027/upload_endpoint_clone_check.json`
- `tmp/d7_tau_critical_20261027/fetch_endpoint_clones.json`
- `tmp/d7_tau_critical_20261027/upload_critical18_sources.json`
- `tmp/d7_tau_critical_20261027/fetch_critical18_final.json`
- `tmp/d7_global_critical_20261027/fetch_decision_final.json`
- `tmp/balanced49_fan_joint_deficit_20261026/upload_explicit_checker.json`
- `tmp/balanced49_transfer_20261026/retrieval_receipt_network.json`

公开finite目录只收入原15文件子ZIP、成功receipt/result/stdout/stderr/exit；没有批量收入该目录的fetch-private.tmp、scp-debug-private.tmp、askpass、network、上传或远端启动材料。

## 已做的包检查

读取所选文档和脚本并作只读密钥模式筛查；所收三份嵌套证据压缩包及公开15文件子ZIP的成员也在临时目录解开筛查。未发现所用token/private-key/password赋值模式；这不是第三方安全审计。PDF作为既有历史阅读资料原样收入，没有重新编译或改写。

所有本地工作均为控制面文件复制、网页派生、压缩解压、散列和链接检查。没有新数学推导、solver、checker、SSH、Lean、外部审阅、Goal、wiki或提交。没有宣称他人独立复现。

## 已知未随包内容

完整官方约240MB公开包、部分Linux大矩阵/全搜索目录、机器专用工具链和完整Lean工程未收入。固定有限子包、紧凑证书、主要CNF/proof和已有回执的存在，不等于所有历史作业可从本包单独复现。既有工作上界与独立接受的差别，详见HANDOFF.md §8。
