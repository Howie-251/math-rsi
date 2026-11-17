# Q8 C4-free Interval (`682 ≤ ex(Q₈, C₄) ≤ 683`) — Curated Archive

来源为用户归档 `C4-Free进展.zip :: Q8_C4_upper683_20261116/`（2026-11-16 交付；原始运行采用 `MathRSI v3` + 本地 `coevolve` 上下界协同循环，方法在 `v6` 吸收）。主证明目标 `ex(Q₈, C₄) ≤ 682` **仍开放（OPEN）**；当前已完成的非作者整证审查（`PROOF_AUDIT.md`）保障等级为 `PASS · same-family · provisional`。

## 随仓可直接执行的完整核验（Python 标准库 + C++17，约 2 秒）

```sh
# 1. 独立验证四张 682 边无 C4 构造（证明下界 ex(Q8, C4) ≥ 682）
python3 -B plugins/hypercube-extremal/archive/q8-683/check_q8_682_seeds.py

# 2. 快速核验精确有理组合与安全余量 782808475930428709 / 4209067950080000000000 > 0
python3 -B plugins/hypercube-extremal/archive/q8-683/replay.py quick --out /tmp/q8-quick

# 3. 从 C++17 源码重编译并穷举全部 13,150,453 个合法带标记 Q4 补全（核验整数最大值 -37440）
python3 -B plugins/hypercube-extremal/archive/q8-683/replay.py q4 --out /tmp/q8-full-q4
```

## 省略模式与外部归档边界

遵循仓库 `<50 MiB` 无 LFS 规范（Option 2B），本目录保留最终精确组合 `B_enriched8_candidate001/`、全部 83 条活跃不等式参数 `B684_ACTIVE_83_PARAMETERS.{json,md}`、完整证明与非作者终审正文、C++17 全域枚举器 `independent_q4.cpp`、25 份前置 `Q₆` 证书的绑定哈希及 `Q8_683_FRAMEWORK.md`；可调用的 `cube_coevolve` 引擎位于插件 `../../tools/cube_coevolve/`。

以下两类大型文件未随 Git 提交，完整登记在 [INVENTORY.json](INVENTORY.json)（原件保存在研究归档 `C4-Free进展.zip :: Q8_C4_upper683_20261116/`）：
- `replay.py reconstruct` 所需的浮点诊断特征池 `.npz` 与 `pool_B684plus_enriched1..7` 中间搜索池；
- `replay.py q6` 所需的 25 份 `q6_sources/*.drat` 原始轨迹（约 555 MiB；其 4,383,882 次 RUP 添加核验记录见 `finite8_q6_import_audit/VERIFICATION.md`）。

在未挂载上述外部原包时运行 `reconstruct` 或 `q6` 模式，`replay.py` 会明确报错退出并指向 `INVENTORY.json`，不会将缺件伪装成通过；哈希清单亦不替代原始 DRAT 轨迹重放。
