# v6 Evolution & Implementation Record (`2026-11-17`)

- **Release target:** `v6` on `main` (fixed `v1`–`v5` tags preserved unchanged).
- **Source archives ingested (read-only originals):**
  1. `C4-Free进展.zip :: 成果汇编_20261031/` ($Q_7 = 304$ source report + $Q_\infty$ `0.59124` `T3`/`T4` flag-algebra & generalized degree-potential proofs and C++20 128-bit verifiers);
  2. `C4-Free进展.zip :: Q8_C4_upper683_20261116/` ($Q_8$: `682 ≤ ex(Q₈, C₄) ≤ 683` Theorem B, 4 explicit 682-edge seeds, 2 explicit 304-edge $Q_7$ constructions, and the zero-dependency `cube_coevolve` primal–dual coevolution engine);
  3. `R-S-n=7(2).rar :: R-S-n=7/` (Ruskey–Savage $Q_7$ complete **E16**: every matching with $\ge 56$ edges / $\le 16$ holes across all $\mu \in \{0,1,2,3,4\}$ extends to a Hamilton cycle, bundled with all 290 verified `baseline_imports` from the 2026-11-14 $Q_7$ archive).

## 1. Cross-model adversarial design & audit (`grok-4.7-build`, `xhigh`)

Three consecutive rounds of read-only cross-model review (`grok-4.7-build`, `--reasoning-effort xhigh`, session `eb4cbde8-ffbb-4704-b8ad-a6b63d447aec`, all `stopReason=end_turn`) plus a fresh zero-context pre-PR audit (`grok-4.7-build`, `xhigh`, session `01a1e7c7-62f1-7ad3-a3b6-05901db5d6f1`, `stopReason=end_turn`, `VERDICT: PASS`) were conducted before release:
- **Mathematical verification:** Confirmed the 5-line `(v, S, T)` hypergeometric tower making `T4` ($\le 0.5912405942$, $m=1024$) unconditional for all $n \ge 1024$; confirmed exact upward rounding (`0.5912405943` for `T3`, `0.5912405942` for `T4`, rejecting 8-digit downward truncation `0.59124059`); audited the `MU0_STRUCTURED_JOINT.py` transformation (`100,055 - 5 + 1 = 100,051` constraints, removing the 5 inner-axis signed-imbalance constraints `1140..1144` while keeping small-face holes `h_0..h_63` symbolic); and audited non-theorem/open boundaries (`0.5907` CP residual, retracted $Q_5$ `0.5899`, open $Q_8 \le 682$, open $Q_7 \le 55$ edges / $R_7$ / $P_7$ / 7-direction lifting).
- **$Q_7 = 304$ separate scoping:** Adopted the explicit distinction between the two directly verified 304-edge constructions (`A.edges`, `B.edges`, proving $\ge 304$) and the source-reported upper bound: *"304-edge construction verified; 304 upper bound as reported in the source package, not re-verified in this pass."* / *“304 边构造已验证；304 上界按原包报告，本次未复验。”*
- **Curated `<50 MiB` normal-Git packaging (~116 MB total, zero Git LFS):** Retained all proofs, source builders, basis JSONs, C++17/20 exact verifiers, `cube_coevolve` and all 290 E16 baseline imports; omitted multi-hundred-MB raw `.cnf`/`.drup`/`.drat` traces and `.npz` discovery arrays uniformly per family with explicit `INVENTORY.json` provenance and clean CLI missing-input guards in `q8-683/replay.py`. Hash manifests identify external files and never substitute for trace replay.

## 2. Shared Base (`base/skills/`) changes in `v6`

1. **Pillar A — Hardest-remainder split gating & net-new union coverage** (`mathrsi-prove/references/actual-input-coverage.md`, `mathrsi-research/references/global-reassessment.md`, `mathrsi-prove/SKILL.md`): Require a bounded feasibility probe on the hardest open branch before adopting a new case split; measure progress on the same actual input relative to the existing union of proved theorems; do not reset stall counters when easy sibling slices pass while the hardest core remains untouched.
2. **Pillar B — Primal–dual coevolution** (`mathrsi-route-loop/references/primal-dual-coevolution.md`, `mathrsi-route-loop/SKILL.md`): Separate primary proof goal vs. adversarial counterexample target; treat near-extremal working bands as search heuristics only; rotate 4-channel normalized signed residuals $z(X)$; refute candidate inequalities against the full verified archive; export surviving `empirical` obligations to `prove`.
3. **Pillar C — Repair-residual stopping** (`mathrsi-route-loop/SKILL.md`, `mathrsi-verify/SKILL.md`): Stop outer float SDP/LP/CP loops when apparent gains fall at or below exact-repair noise $\varepsilon_{\text{repair}}$, and record nonzero feasibility residuals beside any approximate fit rather than calling it a proved barrier.

## 3. Plugin upgrades & executed checks (`checks/`)

All deterministic verification receipts are stored in [`checks/`](checks/):
- [`asymptotic-05912.json`](checks/asymptotic-05912.json): Recompiled C++20 128-bit `independent_verify_track1.cpp` and `verify_qm_degree_potential.cpp`; verified all `3,212,821` $Q_4$ orbits (`77,107,704` squares) for `T3` and $m=1024$ `T4`.
- [`q7-304.json`](checks/q7-304.json): Verified `A.edges` and `B.edges` (128 vertices, 304 cube edges, 0 $C_4$s) and `six_profiles_independent_audit.py`.
- [`q8-682-seeds.json`](checks/q8-682-seeds.json), [`q8-quick.json`](checks/q8-quick.json), [`q8-q4.json`](checks/q8-q4.json), [`q8-reconstruct-guard.txt`](checks/q8-reconstruct-guard.txt): Verified all four 682-edge seeds, exact rational margin `782808475930428709 / 4209067950080000000000 > 0`, C++17 complete `13,150,453`-completion enumeration (max `-37440`), and clean nonzero exit on omitted external modes.
- [`cube-coevolve-tests.txt`](checks/cube-coevolve-tests.txt), [`cube-coevolve-smoke.txt`](checks/cube-coevolve-smoke.txt), [`cube-coevolve-q8-smoke.txt`](checks/cube-coevolve-q8-smoke.txt): All `18/18` unit tests and offline smoke loops passed (including Darwin `RLIMIT_AS` compatibility in `tools/cube_coevolve/cube_coevolve/worker.py`).
- [`q7-e16.json`](checks/q7-e16.json): Verified all 261 in-repo E16 payload files and all 290 bundled baseline imports, recomputed the 189-row $\mu=0$ large-face table, and ran `MU0_A0_BASIS_REVIEW_check.py`, `MU0_A0_PLANS_REVIEW_check.py`, `MU0_A12_BASIS_REVIEW_check.py` and `Q6_A8_FULL_REVIEW_check.py`.
- [`aris-smoke.json`](checks/aris-smoke.json), [`regression-v3-q4.txt`](checks/regression-v3-q4.txt), [`regression-v5-q7-plans.json`](checks/regression-v5-q7-plans.json), [`regression-a10-rank.json`](checks/regression-a10-rank.json), [`public-site-build.json`](checks/public-site-build.json): Zero regressions across `base/tests/smoke_bundle.py`, `v3` $Q_4$, `v5` $Q_7$ plans, $Q_6$ A10, and the 80-file public Pages allowlist build.

## 4. Bilingual homepage, readers & native `v0 → v6` media

- Updated `development/homepage-redesign-20261105/site/{index.html, app.js, result-visuals.js, styles.css, zh-CN.js, q7.html}` and created bilingual [`erdos-86-latest.html`](../../../homepage-redesign-20261105/site/erdos-86-latest.html) (added to `site/public-files.json`).
- Regenerated bilingual `figures/mathrsi/results-overview/results-overview.{en,zh}.{svg,png}` and recorded genuine Chromium/ffmpeg `v0 → v6 Current` `figures/mathrsi/media/{evolution.mp4, evolution.gif, poster.png, RECORDING.json}` (`2000 × 728`, 29.0s, zero page/request errors, zero text overflows across EN and `zh-CN` on desktop and mobile).
