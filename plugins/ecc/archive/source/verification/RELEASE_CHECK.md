# 本次发布包验证记录

日期：2026-11-03。实际复制到一个含空格的新路径后运行，检查输入全部来自这个副本；原研究目录只提供只读的固定版本 mathlib 依赖缓存。未用旧工程的本项目 `.olean`。

## 已执行且通过

- 五个下界矩阵：完整枚举 71,675 个非零消息；最小距离与维数符合声明。
- 172 个母码：全部 21,844 个非零重量、秩、偶性、满支撑；pynauty 2.8.8.1 全码字二分图规范化确认两两不等价，hull 分布 33/62/77。
- 全部 429,024 条保存接受记录：核对 Gray 下标、实际码字、规范化坐标及两套集合精确相等。
- 全部 172 例输入绑定及 344 条完整扫描命令的生成。
- 全部 619,053,789 条配对拒绝见证：重新读取 1,679,770,064 字节；重算 54,915,072 条 F—码字距离；所有流严格 EOF，invalid/sentinel/nonrejecting 均为 0。native CPU 64.939645 秒。见 [机器结果](certificates/pair-replay/native_result.json)。
- 母码 `new172_hull14` 的两套完整扫描：每套实际遍历 2³² 代表，均得到 3,785 个接受陪集，与归档精确一致。见 [完整扫描结果](single-case-scan/full_f/SUMMARY.json)。
- 两个 Lean 工程从全新项目源码构建：`ECC.Main`、`ECC.Corollaries`、`ECC42`；随后执行 3 次独立 import/type/transitive-axiom audit。全部退出码 0；导出结果无 `sorryAx`。实际公理列表见 [绑定记录](VERIFICATION_BINDING.json)。固定版本 mathlib 缓存被复用，所有依赖 Git 提交及已跟踪源码干净状态已核对。

## 没有声称本次执行的工作

没有重跑全部 172 个母码的两套全域扫描；仅上面一个母码做了双全域复算。其余输入、完成输出与接受集合全部随包，完整执行命令可用。全部 619,053,789 个 pair 确实在本次重放。

没有重做 E1/E2/E3 的已发表分类。Lean 最终定理依然具有文献和外部计算参数；干净公理列表不会消去这些参数。没有新增外部审稿结论。联合论文保留既有 PDF/TeX，未在本次打包重新编译，数学陈述未改。

## 日志与路径

`certificates/RESULT.json` 和 `lean/RESULT.json` 保存命令、退出码及耗时。为公开交付，日志中本机账户路径替换为 `<RELOCATED_PACKAGE>`、`<RELEASE_TEST_ROOT>`、`<PINNED_DEPENDENCY_CACHE>`、`<PYTHON_3_11>` 和 `<LAKE>`。这只影响日志显示；执行使用真实新目录。

`SOURCE_PROVENANCE.json` 记录来源及路径/文档改写说明；`VERIFICATION_BINDING.json` 记录测试副本和发布科学输入的对应关系。按发布者要求，已移除 SHA 校验清单及校验命令，数学证明、计算证据与 Lean 验证内容不变。重新生成的 ZIP 另行检查成员名单、解压数据与当前目录逐字节一致性。
