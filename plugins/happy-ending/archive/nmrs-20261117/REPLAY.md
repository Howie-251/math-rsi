# 固定证据的既有复核入口（本次未执行）

请在 Linux 的独立解压副本中运行。下列命令是从已有记录整理的重放入口；本次仅完成打包、解压、散列及链接检查，没有运行这些科研程序。应先阅读相应 REPORT / RESULTS，保留原证书。

## 1. 九参数两份紧凑原生证书

从本包根目录执行：

```bash
cd source/reports/n79-overlap-20261116/direct-cycle-lp
python3 -B compact_certificate_final.py --check run-988-d2/compact-certificate.json
python3 -B compact_certificate_final.py --check run-d9-d3/compact-certificate.json
```

Python 3 标准库即可。预期各 PASS、exit 0；检查的是固定支撑及整数算术，不重做 LP 优化，不替代完整数学装配审阅。原 Linux 日志和 .exit 文件随包。

## 2. 866 九洞 milestone

从包根目录执行（把 checker 路径替换为 Linux 既有 drat-trim）：

```bash
cd source/reports/n866-joint-label-order-20261117/milestone9
python3 verify.py --directory . --checker /path/to/drat-trim
```

预期 PASS：重建115行、11个共享标签核，核验全部核与≤8预算排除、九洞向量，另重放双cell共享pair。原 tgz 和展开文件同时收入。该必要矩阵最小恰9洞不等于61点实际配置，不能宣称已经得到11/12洞。

## 3. E21 25点抽象见证

```bash
cd source/reports/n756-professor-review-20261027
python3 -B verify_color.py evidence/E21/color.tsv
```

checker 明确要求 Linux；它会写本目录的核验输出，故务必在解压副本执行。原回执在 evidence/E21/portable-verification.json。预期2300个三元组、12650个packet、300对外端、最长蓝路4点、红路5点，无weak7；这不是平面坐标核验。

## 4. 公开八参数15文件有限子包

子包位于 source/reports/n79-overlap-20261116/octagon-source-replay/finite-inputs.zip，保持原始ZIP字节。解到新的副本目录，进入 es7_es8_bounds_81_319_v1，然后：

```bash
python3 -B tools/check_octagon_finite.py --output finite-result-new.json
```

预期 PASS。重放范围及输入绑定以 replay-receipt.json、OCTAGON-SOURCE-RECEIPT.md 为准。原 finite-result.json / finite-stdout.log / replay.exit 均随包。此包不是240MB完整官方包，不重建Lean，也不会自动审阅本项目的抽象迁移桥。

## 5. 五锁块与旧pivot八洞

现有 drat-trim 可直接重放封存字节：

```bash
/path/to/drat-trim source/reports/n7-shared-arm-replay-20261117/lock-blocks/q5/formula.cnf source/reports/n7-shared-arm-replay-20261117/lock-blocks/q5/solver-proof.drat
/path/to/drat-trim source/reports/n866-joint-holes-20261117/pivot-rows/budget7/formula.cnf source/reports/n866-joint-holes-20261117/pivot-rows/budget7/proof.drat
```

预期 s VERIFIED、exit 0。原逐条编码审计、bound审计和checker日志随包。audit_core.py、pivot的check.py/check_bound.py会重写输出，只在独立副本执行；具体接口读各自REPORT。旧pivot的八洞已由115行九洞milestone加强，仍保留其历史证据。

## 所需外部环境与范围

本包不提供 drat-trim / Kissat 二进制、Python发行版、完整Lean/mathlib环境、完整公开240MB原包或Linux上的全量大矩阵；不附凭据、SSH传输程序及机器连接配置。上述固定checker不需要重新开搜索或恢复旧作业。本次独立目录检查仅检验包内文件与链接的完整性，不能登记为科研checker重放或另一人独立复现。
