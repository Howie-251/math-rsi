# 同基线图表同步

2026-10-21。已冻结本次图源和输出，供主执行者重生成总阅读页。

`figures/propertyb_bounds/plot_bounds.py` 保留历史 `small_k_sources.json`，显式加载本目录 `MATCHED_BASELINES.json` 作为当前覆盖。共同参考集为已核五项明确参考式加 GL Theorem 1 的 k=5…9 具体下界，逐 k 取最大值；不声称世界最佳。k=5…11 灰点/共同基线为32、64、128、263、538、1085、2245，新展示值35、65、130、266、542、1112、2275，红色差值3、1、2、3、4、27、30。

k=12 的新值由 `k12-lock-pilot-20261021/pilot/SUMMARY.json` 中完整 M4660 结果读取，并断言 complete、691429型及结论4661。该点与原桥接数据共同基线4633核对，红色+28；蓝色同 k 的≥2保留。蓝线原12…64数据及定义均未改动。k=4精确值23零点保留，k=13不加红点。

主图英语坐标与脚注明确同一参考包络及两个独立纵轴；红色为 Delta_ind=L_ind−L_ref，蓝色为 Delta_cert=g_*≤Delta。图注明示不能根据视觉交点或高度判断方法反超。小参数归一化绝对值图也同步灰点并延至12，overview同样加入12的新点。历史GL10/11的1070/2213及+42/+62留在正文折叠附表。

`proofs/propertyb-general/RESULTS_FIGURE.md` 已同步定义、八个红点、历史附表、k12证据范围及 K12_LOCK_COMPARISON.html／原证书报告／独立报告链接。k5…11原候选状态保留；k12标完整纸面与整数证书候选、无Lean，并精确说明独立全域覆盖、31个Fraction边界与3348个独立算术型的范围。

实际执行 `.tools/math-python/bin/python figures/propertyb_bounds/plot_bounds.py` 成功，无报错。生成 delta/small/overview/gain 各 SVG、PNG、PDF，整组 `propertyb_bounds.pdf` 顺序 delta、small、overview。主执行代理实际查看三张PNG，坐标、图例、红蓝k12标签与附注均未遮挡；全部图中文字为英文。此处验证绘图和数据连接，不重新证明数学结论。

写入范围仅本报告、绘图脚本、RESULTS_FIGURE.md和图输出；未改主HTML生成器／主数学规范、Lean、Goal或wiki。
