# Happy Ending / N(m,r,s) 2026-11-17 归档说明

本目录从完整交付包 `NMRS-results-20261117(1).zip`（1,608 文件，269.89 MiB）中精选打包 **955 份原件（48.18 MiB，单文件最大 9.56 MiB，零 Git LFS）**，所有入库文件与原始压缩包逐字节一致。

## 阅读与主入口

- [HANDOFF.md](HANDOFF.md)：2026-11-17 综合交接报告（七、八、九参数与一般 $m$ 受限容量族，125 处本地链接在本目录全部可达）。
- [INVENTORY.json](INVENTORY.json)：全部 955 份随仓文件与 653 份外部保留文件的精确字节数、SHA-256 及省略原因。

## 打包边界与外部文件说明

为遵守普通 Git 仓库 `<50 MiB` 单文件规范且不引入重复体积，[INVENTORY.json](INVENTORY.json) 记录了三类未随仓存放的文件（均保留于外部完整包 `NMRS-results-20261117(1).zip`）：
1. `INDEX.html` 与 `reading/*.md.html`（10.11 MiB）：`source/` 下 Markdown 原稿的预渲染 HTML 副本。
2. `source/reports/n866-joint-label-order-20261117/milestone9.tgz`（1.44 MiB）：同级已解压目录 `milestone9/` 的压缩副本。
3. 中间探索阶段 $\ge 2\text{ MiB}$ 的 `.cnf` / `.drat` / `solver.out` / `evidence.tar.gz` 与 `source/tmp/` 临时文件（210.16 MiB）。

**全部五套关键有限证书均完整随仓保留，可在仓库根目录直接独立复验：**

```bash
# 1. 九参数原生迹稀疏整数对偶证书（N(9,8,8) <= 688 与 D_9 <= 458 含 47,635 行松弛上限见证）
python3 plugins/happy-ending/tools/check_native_trace_cert.py \
  --check plugins/happy-ending/archive/nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/run-988-d2/compact-certificate.json

python3 plugins/happy-ending/tools/check_native_trace_cert.py \
  --check plugins/happy-ending/archive/nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/run-d9-d3/compact-certificate.json \
  --fractional-witness plugins/happy-ending/archive/nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/run-d9-d3/fractional-grid.json

# 2. 八参数 N(8,6,6) <= 61 九洞封包（milestone9，传入 --checker /path/to/drat-trim 同时核验全部 DRAT 证明）
python3 plugins/happy-ending/tools/check_n866_milestone9.py \
  --directory plugins/happy-ending/archive/nmrs-20261117/source/reports/n866-joint-label-order-20261117/milestone9 \
  --allow-no-drat

# 3. 八参数 Schroeder 公开 15 文件遗漏树有限算术重放（C_8 <= 193, D_8 <= 124）
python3 plugins/happy-ending/tools/check_octagon_omission.py

# 4. 七参数 E21 25 点抽象染色下界见证（N(7,5,6) >= 25）
python3 plugins/happy-ending/tools/check_lower25.py \
  plugins/happy-ending/archive/nmrs-20261117/source/reports/n756-professor-review-20261027/evidence/E21/color.tsv
```

（第 5 套为 `source/reports/n7-shared-arm-replay-20261117/lock-blocks/q5/{formula.cnf, solver-proof.drat}` 与 `source/reports/n866-joint-holes-20261117/pivot-rows/budget7/{formula.cnf, proof.drat}`，可直接交 `drat-trim` 核验 UNSAT。）
