# Reproduce the 23-point selection modules

Run from project `formal/`:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build Aris4Math.ThirtyThree.TwentyThreeSelection
lake env lean ../context/propertyb33/round02/twentythree-selection/ImportAudit.lean
```

The new selection module builds in the pinned Lean 4.24.0 project; the default old T32 target is unchanged. `lake-build.log` records the successful explicit build. `import-audit.log` records a separate import and an actual Fin 23 caller. This is structural selection, not a complete 23-point Property-B proof.

For the completed colored branch:

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeColoredSelection
lake env lean ../context/propertyb33/round02/twentythree-selection/ColoredImportAudit.lean
```

For the all-unit-low selection:

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeDefectSelection
lake env lean ../context/propertyb33/round02/twentythree-selection/DefectImportAudit.lean
```

For the high-pair and path extensions:

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeHighSelection
lake env lean ../context/propertyb33/round02/twentythree-selection/HighImportAudit.lean
```

For the actual r=0 clique moments and full cluster selection:

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeClusterMoments
lake build Aris4Math.ThirtyThree.TwentyThreeClusterSelection
lake env lean ../context/propertyb33/round02/twentythree-selection/ClusterImportAudit.lean
```

The first new build exited 0 (910 jobs), the second exited 0 (913 jobs), and the independent import with expanded actual Fin 23 caller exited 0. Logs: `moments-lake-build.log`, `cluster-lake-build.log`, `cluster-import-audit.log`. The output theorem still explicitly requires high-codegree and induced-P3 graph exclusions; the numerical probability branches discharge these separately.

For the actual high-codegree probability branches:

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeHighPair
lake env lean ../context/propertyb33/round02/twentythree-selection/HighPairImportAudit.lean
lake build Aris4Math.ThirtyThree.TwentyThreeHighQuadData
lake build Aris4Math.ThirtyThree.TwentyThreeHighQuad
lake env lean ../context/propertyb33/round02/twentythree-selection/HighQuadImportAudit.lean
```

All five commands exited 0. The high-pair build took 2.5 seconds for the new module. The seven-row high-quad data build took 14.853 seconds wall time and 13.30 user CPU seconds. See `high-pair-lake-build.log`, `high-pair-import-audit.log`, `high-quad-data-build.log`, `high-quad-build.log`, and `high-quad-import-audit.log`.

### r=0 概率分支（本轮）

所有 Lean 命令仍在 `formal/`，同一 shell 设置项目 ELAN_HOME/PATH。

- `lake build Aris4Math.ThirtyThree.TwentyThreeHighPathData`：PASS，544秒模块时间。随后 `TwentyThreeHighPathCatalog` 正在检查完整52+63布尔迹分类及真实小型恢复等式。
- `python3 context/propertyb33/round02/twentythree-selection/generate_high_five_data.py`：生成32+41个完整标签五锁输入，全部Python精确界<1。
- `lake build Aris4Math.ThirtyThree.TwentyThreeHighFiveData`：PASS，646秒模块时间、墙钟10:48.69；内核计算73个有效profile与完整非负dual义务。
- `lake build Aris4Math.ThirtyThree.TwentyThreeHighSixProfiles`：PASS，实际六锁表格桥接；只复用Simple5Hypergraph，不另定义数学对象。
- `python3 context/propertyb33/round02/twentythree-selection/generate_high_six_data.py`：生成22个代表，21裸界、1精细扣除。
- `lake build Aris4Math.ThirtyThree.TwentyThreeHighSixData`：PASS，247秒模块时间、墙钟4:09.81。
- `python3 context/propertyb33/round02/twentythree-selection/generate_high_six_catalog.py`：从保存的58行输入映射生成匹配置换、规范大迹、允许余迹、完整有限覆盖和代表等式。

Five/Six Catalog首轮在有限证明处缺少`unfold Admissible`，导致Decidable实例无法展开；已按真实报错修正后重建。此为Lean接口问题，不是数值反例或数学覆盖失败，首轮不计通过。

### r=0 最终验收

- `lake build Aris4Math.ThirtyThree.TwentyThreeHighComplete`：exit0，共1038 jobs，实际构建了Path、Reduction与Complete新入口。
- `lake env lean ../context/propertyb33/round02/twentythree-selection/HighCompleteImportAudit.lean`：exit0；原Bool染色caller与7项传递公理审计全部仅propext/Classical.choice/Quot.sound。
- Five/Six独立分支审计也PASS：`HighClusterImportAudit.lean`及`high-cluster-import-audit.log`。
- 所有TwentyThreeHigh*.lean禁用占位符检索无匹配；未改共享基类、默认目标或另项目文件。


## One-low unit branch and matching normalization (2026-10-13)

From `formal/`, after setting `ELAN_HOME` to the project `.tools/elan` and prepending its `bin` directory to `PATH`:

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveCatalog
lake build Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveComplete
lake build Aris4Math.ThirtyThree.TwentyThreeLowUnitSixSelection
lake env lean ../context/propertyb33/round02/twentythree-selection/LowUnitFiveImportAudit.lean
lake env lean ../context/propertyb33/round02/twentythree-selection/LowUnitSixSelectionImportAudit.lean
```

Explicit build logs: `low-unit-five-catalog-build.log`, `low-unit-five-complete-build.log`, `low-unit-six-selection-build.log`. Independent audits: `low-unit-five-import-audit.log`, `low-unit-six-selection-import-audit.log`. See `LOW_UNIT_HANDOFF.md` for the actual exported scope and source ownership.
