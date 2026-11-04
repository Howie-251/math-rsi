# 复现与进一步迭代

## 第一级：交付完整性

双击OPEN.cmd阅读，运行VERIFY.ps1重算全部清单SHA。它不证明数学结论，只验证文件未损坏、未遗漏。

## 第二级：最终证明总装

运行REPLAY_FINAL.ps1。使用原始P6_FULL_REVIEW_check.py --final，重新散列绑定证书、核验九个孔层、依赖无环及端点/余域有限逻辑。通过Path.write_text的输出重定向，结果存入verification_runs，冻结源文件不变。报告明确 large_local_certificate_computations_rerun=false。

## 第三级：重算局部有限证据

以research/six_directions/P6_FULL_REVIEW.json为根，沿imported_dependency_hashes和checker_artifact_hashes查找每层的独立检查程序。先读对应REVIEW.md/.json，确认其参数、输入字节格式及实际接受范围，再在新工作副本执行对应checker。不同checker可能复用大量工作文件，不应以文件名相似就混用命令。具体历史命令在trajectories/TOOL_EXECUTION.jsonl中按程序名检索。

## 第四级：重跑原始搜索

从运行轨迹提取真实参数、编译命令与预算；使用包内.cpp/.py与原始输入。编译产物.exe保留供同平台使用，但依赖工具链需另外匹配。先按RELOCATION_NOTES.json替换工作副本中的E/F原路径，再安装DEPENDENCIES.json所列实际需要的库。可将search output与原证书比较，但生成器本身不作为真实性依据。

## 新RSI迭代

保留本包SHA基线，在新目录记录问题变体、输入与算法版本、随机种子、资源、每轮成功/失败和审计结论。重新证明目标不能仅修改原审计状态。Q6成果与七方向探索必须分别记账。

## 目录和解释器

所有顶层验证入口基于自身目录定位，不使用原E/F盘。runtime/python为Windows x64便携解释器；其他平台可用Python3.10+执行verify_package.py和replay_final.py。生产搜索对Python/C++版本的需求以原代码为准。
