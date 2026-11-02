# 合并wiki与启动新Goal

## 放到哪里

将整个材料包放到**原degree/diameter专用项目**的：

    context/dd-portfolio-20261026/

这是建议的项目内路径，不是声称用户开发机已存在。继续使用原项目的唯一`research-wiki/`；不要把这里另建成一套独立wiki。需要新Codex对话时仍指向同一授权项目，读取相同文件即可。

## 先做一次入库

将下面内容发给Codex，先只做合并，不启动新研究：

```text
保持旧Goal暂停。读取 context/dd-portfolio-20261026/START_HERE.md
和 IMPORT_AND_START.md，按实际research-wiki技能与helper合并
wiki_import/中的草稿到现有唯一知识库。

先对照已有节点，重复主题合并，不分叉知识库；来源和证据等级不升级。
保存旧N(8,2)成果及开放状态，把其任务安排暂停，而不是宣布完成。
将新范围4≤Δ≤12、D=3/4/5及12个优先入口写入导航。
链接已有反例方法节点，但不自动开启其中的n61专用任务。
将最新人工意见和新旧任务分界写入既有comments记录。

只更新必要导航、wiki关系和恢复入口，报告实际文件路径后停止。
不要启动solver、构造搜索、Lean或重新审计旧证明。
```

每个wiki草稿的id/status只是可移植建议。导入时按照本机真实schema转换，不能凭草稿字段假装已通过proof-checker。`PRIOR_WORK_LEDGER.md`是旧结果导航，不是新的数学claim。`baseline_verification.json`对应已知基线的本轮有限检查，不是新下界。

## 再启动新的Goal

旧Goal保留暂停/归档，避免新旧任务同时向同一wiki和progress.html写入冲突的“当前任务”。用户明确要保留旧Goal并行时，应另设输出入口与资源分配；本包不默认授权。

新Goal建议正文：

```text
在当前degree/diameter项目执行
context/dd-portfolio-20261026/RESEARCH_GOAL.md。

范围4≤Δ≤12、D∈{3,4,5}，允许按数学机制选择参数，
优先产生超过最新公开下界的完整合法图或构造族。
先从登记的12个优先入口选择，其他15格保留为范围内储备。
不要求确定每个N(Δ,D)精确值，也不承诺全部27格解决。

继承已有wiki、程序、失败记录和本包5张已验证已知基线。
旧N(8,2)、n61谱与端口、n62–65及缺陷3推广暂不执行。
不把已知复现或局部排除当新纪录。

按ARIS实际技能组织推导、反例、生成、独立验证和审阅；
最终严格标准保持，Lean后置到真实新成果。
约每小时更新research/progress.html，处理我的comment；
每小时只汇报，不要求换题，更新后继续研究。
```

## 新会话恢复的最短入口

新会话不必重读全部旧对话。读本项目AGENTS、当前wiki query_pack、START_HERE和RESEARCH_GOAL即可；按需下钻旧证明。实际路径不同由Codex定位并写入恢复文件，不让用户填写任务卡。

本次ChatGPT只创建了交接包，没有把文件上传到开发机、写入实际wiki或创建/恢复任何Goal。
