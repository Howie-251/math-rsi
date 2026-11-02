# v2文档与DD发现入口集成

2026-11-03。本轮读取`EVOLUTION.md`，沿已读的新`mathrsi-meta-evolve`执行合同做有界集成。先向DD作者确认实际技能名与五workflow接口，再读已写入口与README；未修改`plugins/degree-diameter/`、ARIS副本、Root的EVOLUTION或其它owner文件，未外部发布。

## 实际改动

- `README.md`、`README.zh-CN.md`：保留原图、主要章节、Property B案例和已有使用入口。增加DD四技能/资料层与当前五workflow关系；同步仅形式目标直接Lean；把“v2只是未来图节点/新meta未接DD”的旧阶段描述更新为本轮增量实现与实际维护记录。历史DD/Property B仍为研究来源，未改写成新版实验。
- `docs/QUICKSTART.md`：新增DD自然语言调用、双端发现说明、仅形式目标的真实入口与返回示例；同时要求自然语言audit时两项各按合同执行。原clone、agent启动、reviewer配置和proof-repair步骤保留。
- `docs/WORKFLOWS.md`：保持五个子workflow和唯一父调度，流程图增仅形式目标入口；新增DD的五阶段输入→领域调用→实际消费表。
- `docs/PLUGIN_CONTRACT.md`：新增与Property B并列的DD调用表；明确DD不重开总控、有限证据返回原图/当前caller，handoff交base。ECC仍草案，未升级验收状态。
- `docs/EVOLUTION_WORKFLOW.md`：保留新meta作为唯一维护执行链，连接本轮EVOLUTION与具体v2改变，删除“只有入口，DD尚未进入实施”的阶段滞后说明；不扩大授权或独立试用门槛。
- 新增`docs/V2_CHANGES.md`：具体说明B1直接形式目标、B2基线改变队列、B3对象改变后的正负证据、B4共同覆盖/局部门，以及DD与meta怎样用。采用与review的最终状态留Root记录，不预写整个版本已终审。

八个新增发现别名均为相对链接，双端共用同一DD正文：

```text
.agents/skills/mathrsi-degree-diameter -> ../../plugins/degree-diameter/skills/mathrsi-degree-diameter
.agents/skills/dd-construction -> ../../plugins/degree-diameter/skills/dd-construction
.agents/skills/dd-obstruction-certificate -> ../../plugins/degree-diameter/skills/dd-obstruction-certificate
.agents/skills/dd-transfer-diagnosis -> ../../plugins/degree-diameter/skills/dd-transfer-diagnosis
.claude/skills/<同上四名> -> ../../plugins/degree-diameter/skills/<对应同名>
```

没有调用全局安装器或改用户配置。现有别名原样保留。

## 与DD作者确认的实际接口

`mathrsi-degree-diameter`核原对象和路由；`dd-construction`处理当前覆盖/full-neighborhood/仿射/GQ构造；`dd-obstruction-certificate`处理必要域、完整枚举、exact dual与原图到Lean；`dd-transfer-diagnosis`处理换源/域/连接/基线后的继承。

prepare/survey共享一次来源调查，收到精确对象、进口与比较；route-loop收到改变障碍的新规则及首探针；prove收到真实定义、degree/all-pair caller或准确条件；verify收到精确有限命题、原图连接/形式出口；handoff取已核正文与复现入口。每项返回直接父caller，不启动第二个同级workflow。历史wiki随archive提供，新题wiki写工作区。

## 实际检查

1. 本owner七份维护文档210个相对目标实际检查，0缺失。
2. 八个别名均为相对路径、解析仍在本仓、各有实际SKILL.md。
3. 比对Git HEAD中两README的图片引用，原图片全部保留，未重绘或替换。
4. `git diff --check`对本owner文档exit0。
5. 首轮全仓check发现DD作者在写的两个example暂未存在，已通知作者；作者交回完成后复查：`python3 tools/check_links.py` exit0，78份文档/1248本地目标，0缺失。原始输出见`V2_INTEGRATION_LINKS.txt`，范围与机器结果见`V2_INTEGRATION_CHECKS.json`。

链接检查只证路径存在，别名检查只证发现结构，不认证数学或实际模型可用。没有重跑旧Lean、旧模型、求解器、BFS或研究Goal；没有用文档改动声称新题收益实测。全仓Git diff同时包含Root此前对meta相关文档的未提交变化，本记录只声明上述本次增量，不覆盖或认领原有改动。

交回Root：集成内容和发现入口已可消费；最终meta审阅修订、版本采用、完整发布核验与提交由Root处理。
