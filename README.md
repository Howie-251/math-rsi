# MathRSI

**以 ARIS 为基础、由 agent 主导的数学研究工作流。** 固定目标，复用知识，选择与修正证明路线，把局部结果连接成可检查的原命题解答。

MathRSI 以详细 Markdown skills 为主。它告诉 agent 在什么情形下如何思考、调用现有工具、判断证据及调整路线；没有另造自动评分器、数学搜索引擎或强制状态机。当前为本地首版，尚未验证普遍提速或持续自我改进能力。

## 从哪里开始

- **开始或继续一道数学题：** [mathrsi-research 主技能](base/skills/mathrsi-research/SKILL.md)。它是完整执行入口，按需读取两个参考文档。
- **Property B：** 同时读取 [领域技能](plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)，获得选锁、实际迹、共同对象及验证的研究入口。
- **编码理论：** 同时读取 [ECC 领域技能](plugins/ecc/skills/mathrsi-ecc/SKILL.md)，区分构造、局部排除与全域不存在性。
- **准备文件与恢复研究：** [工作区说明](docs/WORKSPACE.md)。已有项目直接沿用原规格与 wiki。
- **已有 ARIS 能做什么：** [ARIS 复用说明](docs/ARIS_REUSE.md)。按义务调用现有技能，不自动运行整套论文流水线。

可以直接向 Codex、Claude Code 或其他能读取本地文件的 agent 发出：

```text
读取 /实际路径/MathRSI/base/skills/mathrsi-research/SKILL.md，
并按需使用 /实际路径/MathRSI/plugins/propertyb/skills/mathrsi-propertyb/SKILL.md。
在 /我的任务目录 中继续研究，先读 FORMAL_SPEC.md 和 NEXT_SESSION.md，
复用原 research-wiki。按原题与预算完成任务，记录实际证据和未闭义务。
```

上述是文件加载方式；本仓库没有自动安装全局 skills，也不要求宿主必须提供某个斜杠命令。没有领域插件的数学任务可以直接使用 base；不要为了启动任务先制造一个插件。

## 三层怎样配合

|层次|维护内容|改变的理由|
|---|---|---|
|`base/`|命题与验收、知识复用、义务与路线、委派、效率诊断、验证、交接|多个任务暴露出通用流程问题|
|`plugins/`|领域对象、定理条件、归约与策略、检查器接入及经验入口|得到本领域可复用的新知识或方法|
|任务工作区|本题规格、证明、wiki、实际输入、计算、审阅与恢复状态|本题产生新结果、反例或路线调整|

核心与插件之间用[人可读的协作约定](docs/PLUGIN_CONTRACT.md)交流，不要求把数学推理塞进固定 JSON。一个检查器只证明它实际检查的属性；完整解答需要 agent 接通原对象、归约、计算或引理与原结论。

## 先使用，再改进

一次解题使用明确的 base 与插件版本。新的领域定理进入插件知识，单题断点留在工作区；通用流程改进以独立变更提出，再通过实际使用核对。不要在解题中静默改变目标、验收或核心来制造成功。

目前两个插件提炼自 Property B 与 ECC 研究，尚未覆盖所有数学领域。示例和首版检查见 [验证记录](development/VALIDATION.md)；它们检验使用连接，不替代新的科研任务评估。

## 本地开发

`main` 保存可用组合版本。具体功能用短期分支，多 agent 有文件冲突时使用独立 worktree；领域方法放目录，不放长期分叉分支。原项目与大型证据不搬入代码仓库。详细约定见 [AGENTS.md](AGENTS.md)。

仓库只提供一个可选的本地文档连接检查器：

```bash
python3 tools/check_links.py
```

它检查维护文档的本地 Markdown 链接目标，帮助插件与 base 移动目录后保持可读；不审阅数学、不更改任务状态、不调用模型。数学运行继续复用任务所需的实际工具。

## 来源

基于 [ARIS / Auto-Research-In-Sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) 的技能组织、研究记忆、评审与形式化经验，沿用 MIT 许可证。具体复用和调整见 [来源说明](docs/PROVENANCE.md)。
