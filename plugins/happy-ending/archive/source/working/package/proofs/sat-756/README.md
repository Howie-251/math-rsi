# 756 容量 25 的既有资料

- [55 个反例单元的证据索引（CSV）](55-case-register.csv)
- [同一索引及原始收据字段（JSON）](55-case-register.json)
- [原始 CNF、证明、检查器与收据定位（TSV）](EXTERNAL-MATERIALS.tsv)
- [旧证据目录的来源和文件散列](evidence-manifest.json)
- [25 点染色见证](color.tsv) · [便携核验源码](verify_color.py) · [历史核验收据](verification.json) · [历史便携核验收据](portable-verification.json)

旧 E 编号是档案标识。证据目录沿用旧 manifest 的精确 95 项。55 单元索引记录原始 CNF、证明、检查器、收据的位置、散列及现有字节数等字段。大型 CNF 和 DRAT 等证明主体仍以索引中的 Linux 原路径定位。本包提供本机留存的原始收据和索引，文件完整性检查的对象是本包所含文件。

25 点见证核验记录属于旧交付。若需要重验，可在 Linux 上把 `verify_color.py` 与 `color.tsv` 复制到独立临时目录，在其中运行 `python3 verify_color.py color.tsv`，以保留包内历史回执。该脚本仅核验下界见证。此次打包核对原字节及散列，历史证书检查状态沿用旧原件。
