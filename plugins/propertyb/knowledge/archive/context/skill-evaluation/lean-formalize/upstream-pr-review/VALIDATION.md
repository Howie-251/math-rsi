# ARIS Lean 双端集成核验

本轮是用户授权的技能 PR 与合并工作，不重新求解 Property B。

- PR：<https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/pull/461>
- 首次提交：`690fa5808d61c588ea98af4bf7b076d8fc35394c`。
- 工作树：`/Users/rfy_naiveai/Desktop/aris_lean_pr`，基于上游 `0974de7`。
- 新技能两端均包含入口和三份参考；Codex 另含 `agents/openai.yaml`。
- 五处父入口：proof-writer、proof-checker、proof-orchestrator、formula-derivation、research-pipeline，主线和 Codex 同步。

## 本地执行

`python3 tools/check_skills_inventory.py` 通过。

`python3 -m pytest tests/test_codex_skill_mirror.py tests/test_skill_groups.py tests/test_install_aris_selective.py tests/test_codex_install_update.py -q`：57 passed in 12.49s。

Codex skill-creator 的 quick_validate 通过。两端 YAML、必要文件、相对 Markdown 链接及参考内容一致性检查通过。该 Codex validator 对 Claude 版的 `argument-hint` 报不支持，此为宿主 schema 差异；Claude 版保留仓库已有的标准 frontmatter 字段，另做 YAML/包结构和仓库检查。验证器 PyYAML 依赖临时放在 `/tmp/aris-lean-skill-validator-pydeps`，未增加 ARIS 运行依赖。

`git diff --check` 通过。helper lint 只报告未修改的 research-wiki 中一个既有 advisory。

## 独立子代理检查

`lean_skill_integration_review` 检查三条实际调用路径：普通短证明不默认 Lean；明确要求 Lean 的裸命题进入证明探索和实现；proof-checker 委派子引理时只关闭相应义务、回到原审计，不递归新建审计。

该代理在隔离目录执行 theory 选择安装：Claude、Codex、Codex+Claude overlay、Codex+Gemini overlay 四种均保留新技能三份参考和共享引用。测试仅在临时脚本副本中重定向全局 repo 指针，避免修改真实 `~/.aris/repo`。临时目录为 `/var/folders/qz/3h_f66zn67zbty04w0mjyysm0000gn/T/aris-lean-integration-rtxdkaks`。未实启 Claude 会话；Claude 桥接按用户此前实测可用处理，不重复验证连接。

同家族内容审阅属于 provisional。跨家族原始记录分别保存在同目录 `grok.json`、`gemini.json`；其结果和最终 CI/合并状态另行记录，不能从本文件推断已通过。
