# 独立复核与复现

所有命令从发布目录运行。输入随包提供，输出必须放在发布目录外的新目录；不修改已归档证据。Python ≥3.10（使用 `int.bit_count`）；不要使用 `python -O`，检查依赖断言。建议在单独的 Python 虚拟环境中安装：

```sh
python3 -m venv ../ecc-venv
../ecc-venv/bin/python -m pip install -r requirements-computation.txt
```

下列 `python3` 应替换成所选环境的解释器。C++ 程序仅依赖标准库，支持 C++17，默认为 `c++`，可用 `--cxx clang++` 或 `--cxx g++`。配对驱动使用 Unix `resource`，支持 macOS/Linux；Windows 建议 WSL。

## 有限数据和保存集合

```sh
python3 verify.py quick --output-dir ../ecc-quick
```

依次检查：

1. 五个下界矩阵，共 71,675 个非零消息；172 个母码的 21,844 个非零重量、秩、偶性、距离、满支撑，以及迫使对偶重量 4 的多项式恒等式。
2. 用 pynauty 对“全部 128 码字—40 坐标”的两色二分图规范化，核对 172 个母码两两不等价；重算 hull 分布 33/62/77。穷尽性还使用 E2。
3. 全部 429,024 条保存记录的 Gray 下标、40 位码字、规范化坐标及两套接受集合完全相同；检查历史完整域标记。
4. 为全部 172 例生成两套完整扫描的 344 条命令，并核对输入绑定。该步骤只打印计划，不运行全域扫描。

成功输出 `RESULT.json: PASS`。有限检查不等于重跑 `2³²` 域，也不读取全部配对见证。

## 全部配对证书重放

```sh
python3 verify.py certificates --output-dir ../ecc-certificates
```

包含所有 quick 检查，并从随包 C++ 源码编译独立 checker，重新检查全部 54,915,072 条 F—母码字距离，以及 619,053,789 条配对拒绝见证；严格核对每流 EOF。预期 172 例，149 个二进制流、23 个 TSV，全部 invalid/sentinel/nonrejecting 计数为 0。

默认 native CPU 限额 600 秒、wall 限额 900 秒；慢机器可加 `--cpu-seconds 1800 --wall-seconds 2400`。超时、非零退出或未完整结束均不是 PASS。历史重放在原机器约一分钟，实际耗时取决于硬件和磁盘。本步骤证明保存集合内所有 pair 不兼容，完整集合无遗漏仍由全域扫描承担。

## 两套完整陪集扫描

先检查输入并打印计划：

```sh
python3 computation/reproduce.py full-f --all --implementation both --cpu-seconds 600 --output-dir ../ecc-full
```

加 `--run` 才编译并执行：

```sh
python3 computation/reproduce.py full-f --all --implementation both --cpu-seconds 600 --output-dir ../ecc-full --run
```

每套访问 `172×2³²=738,734,374,912` 个偶陪集代表，总计 344 次运行。每个结果须完整结束、与归档 F 精确一致。历史两套合计约 66.5 CPU 分钟，当前机器可能更慢。`--cpu-seconds` 是单例时限。可用 `--case new172_hull14` 替换 `--all` 只复算一个母码；单例通过不能代替所有 172 例。任何中断/失败需保留原输出并另选新目录再运行。

第一扫描器使用 33 个 free 位中的偶重量代表，分块筛查；第二扫描器独立构造 32 维偶商空间基，使用 Gray 遍历。归档实际整数和坐标置换全部随包提供。native 接口与输入转换可直接审查 `computation/reproduce.py`。

## Lean

安装 elan，执行：

```sh
python3 verify.py lean --get-cache --output-dir ../ecc-lean
```

已有匹配依赖可替换为：

```sh
python3 verify.py lean --dependency-cache /path/to/existing/.lake/packages --output-dir ../ecc-lean
```

脚本从新的工程源副本构建；不复用本项目 `.olean`，可复用固定版本 mathlib 的预编译缓存。输出包含 2 次 build、3 次独立 import/type/axiom audit 的命令、退出码和日志。使用 `--get-cache` 需网络，第一次安装工具链/库可能耗时较长。外部定理/计算参数的含义见 [formal/README](formal/README.md)。

## 输入编码

整数 bit j 是从零起的第 j 个坐标；消息 bit i 选择第 i 行，异或为加法。F 文件为原扫描的 free 坐标压缩整数；Gray 接受文件每行是“Gray 下标、实际 40 位代表、原规范化压缩整数”。pair 流顺序按 F 索引的词典序无序对；二进制值为 0..127 的母码消息，TSV 还含索引和实际拒绝重量。所有解释由 checker 再核验。

`data/COMPUTATIONAL_COVERAGE.json` 与 `data/historical-pair-replay.json` 是历史元数据汇总；其中旧日期的 review/goal/status 字段描述当时状态，不代表本次发布包验证结论。本次状态以 verification/RELEASE_CHECK.md 为准。实际执行读 `evidence/manifest.json`。其中描述性 `source-archive:` 字符串只保留历史出处，不是运行依赖。原研究的冗余逐 pair JSON、发现脚本和私有模型记录不需要参与验收，未包含。
