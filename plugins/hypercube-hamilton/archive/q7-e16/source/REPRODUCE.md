# 复现与核验

在档案目录根部运行以下命令。目录脚本依据成员清单恢复空目录。文件校验直接核对每个冻结原文件的字节数和 SHA-256。

```powershell
python -B .\archive_inventory\materialize_archive_layout.py --create
python -B .\archive_inventory\verify_package.py
```

本地证书按原名存放，可直接回放。使用 `--baseline` 指定原 RAR，再用 `--compose` 在另一个空目录组装本地文件和逐个验真的基线导入。完整参数和 μ=0 RUP 回放命令见[归档与复现](README.md#归档与组装)。文件及证书校验的数学适用范围见[E16 证明与独审](START_HERE.html#proof-title)。

原 RAR 的 `verification_runs/` 与 `archive_inventory/REPLAY_KEY_CHECKS.md` 保存较早的核验入口。可按[历史核验记录定位](verification_runs/BASELINE_LOCATION.md)查找。
