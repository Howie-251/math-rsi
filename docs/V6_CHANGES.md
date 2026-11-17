# v6: hardest-remainder gates, primal–dual coevolution, and deeper hypercube plugins

**v6 is the current workflow on `main`.** It deepens the shared five-stage research workflow and both hypercube plugins (`hypercube-extremal` and `hypercube-hamilton`), retaining ten base skills, six domains and fourteen domain skills. Clone `main`, [download its ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/heads/main.zip) or use the fixed [v6 tag](https://github.com/lisresearchgroup/math-rsi/tree/v6), and record the exact commit in any research handoff. Fixed `v1`–`v5` tags remain unchanged.

The sources are two research streams run with **MathRSI v3** plus local adaptations and coevolution loops:
- **Erdős Problem 86 ($C_4$-free hypercube subgraphs):** finite $Q_7$ (`304`), finite $Q_8$ (`682 ≤ ex(Q₈, C₄) ≤ 683`) and asymptotic edge density $Q_\infty$ (`T3 ≤ 0.5912405943`, `T4 ≤ 0.5912405942`). [Case study](../case-studies/erdos-86/README.md) · [Bilingual reader](../development/homepage-redesign-20261105/site/erdos-86-latest.html).
- **Ruskey–Savage $Q_7$ Hamilton extension (complete E16):** every matching in $Q_7$ with **at least 56 edges** ($\le 16$ holes, across all $\mu \in \{0,1,2,3,4\}$) extends to a Hamilton cycle retaining every prescribed edge. [Case study](../case-studies/ruskey-savage-q7/README.md) · [Bilingual reader](../development/homepage-redesign-20261105/site/q7.html).

v6 absorbs their reusable workflow actions, domain mathematics and tools; it does not retroactively claim that the published `v6` release produced those source proofs.

## Three concrete base improvements

| Research situation | Action in the existing workflow |
| --- | --- |
| A proposed case split closes easy sub-families while leaving the hardest open core untouched | **Probe the hardest remainder first.** Run a bounded probe on the hardest open branch before adopting a split; measure progress by net-new union coverage on the same actual input and coordinate frame. Easy sibling passes do not reset the stall counter on the shared hardest core. ([actual-input-coverage](../base/skills/mathrsi-prove/references/actual-input-coverage.md), [global-reassessment](../base/skills/mathrsi-research/references/global-reassessment.md)) |
| Constructive lower-bound search and upper-bound inequality discovery stall in isolation | **Primal–dual coevolution.** Separate the open primary proof goal from the adversarial counterexample target; focus parent selection on a near-extremal working band (heuristic only), rotate four channels (`objective`, `challenge`, `novelty`, `condition`) with normalized signed residuals $z = (a\cdot x - b)/\max(\lVert a\rVert_1, \mathrm{IQR})$, and refute candidate cuts against the **entire** verified archive before exporting surviving `empirical` obligations to `prove`. ([primal-dual-coevolution](../base/skills/mathrsi-route-loop/references/primal-dual-coevolution.md)) |
| Outer float SDP/LP/CP iterations keep running after single-round gains fall below exact-repair noise | **Stop at the repair-residual floor.** Halt float iterations when apparent gains fall at or below $\varepsilon_{\text{repair}}$, and record nonzero feasibility residuals beside any uncertified approximate fit rather than presenting it as a proved lower barrier. ([route-loop](../base/skills/mathrsi-route-loop/SKILL.md), [verify](../base/skills/mathrsi-verify/SKILL.md)) |

## Deeper hypercube plugins

### 1. [`hypercube-extremal`](../plugins/hypercube-extremal/README.md)

- **Asymptotic $Q_\infty$ (`archive/asymptotic-05912/`):** Theorem **T3** combines $Q_4$ flag algebra with 35 triangle-free completely positive (COP) cuts and 29 cubic terms to prove $\pi_\square(C_4) \le 681653995482306581 / 1152921504606846976 \approx 0.5912405942282728\ldots \le 0.5912405943$. Theorem **T4** adds the $m = 1024$ generalized hypergeometric vertex-degree potential to prove $\pi_\square(C_4) \le 9701859764505653085708308080340303 / 16409326186106551516455239680000000 \approx 0.5912405941884453\ldots \le 0.5912405942$, backed by a 5-line unconditional `(v, S, T)` hypergeometric tower for all $n \ge 1024$ (never truncating downward to `0.59124059`). Exploratory `0.5907` (approximate CP fit with $\approx 3.9\times 10^{-4}$ residual) and the retracted $Q_5$ `0.5899` claim (refuted by legal $C_4$-free graph `0x69966996699616682994` scoring `0.5922454`) are explicitly documented as non-theorems. The `v3` $Q_4$ certificate (`< 0.59155154`) remains preserved.
- **Finite $Q_7$ (`archive/q7-304/`):** **304-edge construction verified; 304 upper bound as reported in the source package, not re-verified in this pass.** Two explicit 304-edge $C_4$-free constructions (`A.edges`, `B.edges`) prove $\mathrm{ex}(Q_7, C_4) \ge 304$; the upstream 21-instance $Q_6$ RUP reduction report and manifest are preserved, while the 21 raw `.cnf`/`.drup` traces omitted in the upstream compilation are recorded in `INVENTORY.json`.
- **Finite $Q_8$ (`archive/q8-683/`) & [`cube_coevolve`](../plugins/hypercube-extremal/tools/cube_coevolve/README.md):** Four verified 682-edge seeds establish $\mathrm{ex}(Q_8, C_4) \ge 682$, and Theorem B establishes $\mathrm{ex}(Q_8, C_4) \le 683$ by coupling uniform marked $Q_4$ completions, 3-degree edge incidences and global vertex degrees on the same candidate subgraph $H \subseteq Q_8$ across 83 active inequalities and 25 $Q_6$ subcube imports (`PASS · same-family · provisional`; $\mathrm{ex}(Q_8, C_4) \le 682$ remains **OPEN**). The zero-dependency `cube_coevolve` engine is integrated under `tools/cube_coevolve/`.

### 2. [`hypercube-hamilton`](../plugins/hypercube-hamilton/README.md)

- **Complete $Q_7$ E16 (`≥56` edges, `archive/q7-e16/`):** Upgrades the $Q_7$ threshold from $\ge 57$ edges (`v5`) to **all matchings with at least 56 edges** ($\le 16$ holes), closing adjacent-hole augmentation plus all five independent 16-hole classes $\mu \in \{0,1,2,3,4\}$ (with $\mu \ge 5$ ruled out by parity/weight bounds; whole-proof audit `PASS · same-family · provisional · sound-modulo-imports`). Even hole layers 18–38 ($\le 55$ edges), full $Q_7$, free-root paths $P_7$ and seven-direction lifting in $Q_n$ remain **OPEN**.
- **Reusable E16 tools:** Parameterized $Q_6$ $\Delta=2$ double bridge, the 41-orbit $Q_6$ $A_8$ theorem, joint even/odd CNF+DRUP pairs for $\mu=3$, and $S_6$ large-face independent-hole tables (`189` rows for $\mu=0$, `23` rows for $\mu=1$) paired with symbolic small-face holes after removing five inner-axis ordering constraints (`100,055 - 5 + 1 = 100,051` constraints). All 290 baseline imports (`7.98 MB`) from the 2026-11-14 $Q_7$ archive are bundled into `archive/q7-e16/source/`.

## Executed verification scope vs. external archives

All in-repo archives adhere to normal-Git `<50 MiB` per-file packaging (~116 MB added across both plugins, zero Git LFS). Hash manifests in `INVENTORY.json` identify external files and **do not** substitute for certificate or solver-trace replay.

| Check executed in `v6` maintenance | Verified scope |
| --- | --- |
| `asymptotic-05912/run_exact_cpp_checks.py` | Recompiled both 128-bit C++20 verifiers (`independent_verify_track1.cpp`, `verify_qm_degree_potential.cpp`) and checked all `3,212,821` $Q_4$ orbits (`77,107,704` squares) for `T3` and $m=1024$ `T4`. |
| `q7-304/check_q7_304.py` | Checked both 304-edge $C_4$-free constructions (`A.edges`, `B.edges`) and ran `six_profiles_independent_audit.py`. (21 raw `.cnf`/`.drup` upper-bound traces were omitted upstream and not replayed.) |
| `q8-683/{check_q8_682_seeds.py, replay.py quick, replay.py q4}` | Verified all four 682-edge seeds, exact rational safety margin `782808475930428709 / 4209067950080000000000 > 0`, and C++17 enumeration of all `13,150,453` legal marked $Q_4$ completions (max `-37440`). (`reconstruct` `.npz` pools and 25 $Q_6$ `.drat` traces remain in the external archive.) |
| `tools/cube_coevolve` | All `18/18` unit tests and offline smoke loops (`smoke.json`, `q8_offline_smoke.json`) passed without model calls. |
| `q7-e16/check_e16_bundle.py` | Verified all 261 in-repo E16 files and all 290 bundled baseline imports by size and SHA-256, recomputed the 189-row $\mu=0$ large-face table, and ran four zero-dependency geometry/plan checkers (`MU0` $a=0$ census/plans, `MU0` $a=1,2$ orbits, $Q_6$ $A_8$ 41-orbit census). (10 large `.cnf`/`.drup` files totaling `532.49 MB` remain in the external `R-S-n=7(2).rar` archive.) |
| `v3` / `v5` regression & ARIS bundle checks | `verify_final_q4.py` (`v3` $Q_4$), `replay_key_checks.py` (`v5` S3/S2_STRONG), `check_forest_rank.py` ($Q_6$ A10 `1024²` rank `1024`), and `base/tests/smoke_bundle.py` (214 files, 9 offline commands) all exited `0`. |

[Full evolution & Grok review disposition](../development/evolution/v6-c4free-rs7-20261117/EVOLUTION.md) · [v5 history](V5_CHANGES.md) · [v4 history](V4_CHANGES.md) · [Public Pages scope](PAGES.md).
