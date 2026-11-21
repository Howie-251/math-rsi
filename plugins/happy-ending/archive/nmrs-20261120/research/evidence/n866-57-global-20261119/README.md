<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Ordinary N866 <= 57: new full H12 query

**The primary full H12 proof has passed two actual complete DRAT checks and an
independent complete semantic reconstruction. Together with the original-input
bridge, this establishes the working ordinary bound N(8,6,6) <= 57.** Both
checkers returned 0 with exactly one `s VERIFIED`; no external review was invoked.

The mathematical bridge is in
[N866_57_GLOBAL_20261119.md](../../N866_57_GLOBAL_20261119.md).
All scientific execution is Linux-only. No external review was invoked.

The primary query is `h12-prefix6-pools01` under the authoritative directory:

`<private-artifact-root>`

It has 70,172 variables and 2,207,400 clauses. CNF SHA256 is
`5d51a77cceb8296381c1ab8cd61c5b52460c5e64a80537d316b067b7803e561d`.
The formula extends the frozen baseline with an actual threshold-13 layer,
641 checked supports, 2,876 Hall clauses, true-P first-two units, two 17-state
pool constraints, canonical source/second-point rank constraints and all 906
rank-bounded true first-six templates. The whole tail and CNF were exactly
reconstructed. Every nonbudget new clause passed the true 36-point calibration.

The primary solver has returned 20 after 1,354.577 seconds. Its original
1,160,694,777-byte proof has SHA256
`fabcd1750c8c093ca8c5d84d4caa0d890536ab7d6901aae590a4fdff0654acee`.
The first actual checker returned 0 with exactly one `s VERIFIED` marker;
verification took 2,034.175 seconds, and the complete solve/check driver took
3,390.825 seconds. The actual solver log ends with `c exit 20`.
The [successful first-checker receipt](../../../SOURCE_MAP.md#excluded-sources),
[original result](../../../SOURCE_MAP.md#excluded-sources), [solver log](../../../SOURCE_MAP.md#excluded-sources), and
[checker log](../../../SOURCE_MAP.md#excluded-sources) were fetched and hash-checked locally.
An independent reconstruction/second replay is coordinated by the parent task
under its own ownership.
The [independent complete semantic reconstruction](../../../SOURCE_MAP.md#excluded-sources)
has passed: it regenerated the full baseline and tail without using the author's
audit or copying the body, and obtained the identical complete CNF hash.
Its [second actual DRAT check](../../../SOURCE_MAP.md#excluded-sources)
has now passed naturally: verification time 2,074.270 seconds, driver time
2,074.392718 seconds, exit 0 and exactly one `s VERIFIED`. The complete CNF and
original proof hashes were independently checked before and after and stayed
identical. This was a separate process using the same authoritative checker
implementation. See the [independent directory README](../n8-total-deficit-313-20261119/ordinary866-h12-second-replay-20261119/README.md)
for its complete provenance and replay paths.

The actual first-checker log ends with:

```text
c 55117 of 2207400 clauses in core
c 11254407 of 17960889 lemmas in core using 368056238 resolution steps
c 6507 RAT lemmas in core; 5340075 redundant literals in core lemmas
s VERIFIED
c verification time: 2034.175 seconds
```

Locally inspectable static evidence:

* [Primary manifest](../../../SOURCE_MAP.md#excluded-sources)
* [Exact tail/CNF reconstruction](../../../SOURCE_MAP.md#excluded-sources)
* [True 36-point nonbudget calibration](../../../SOURCE_MAP.md#excluded-sources)
* [Compact structural input archive](../../../SOURCE_MAP.md#excluded-sources)
* [Local transfer-hash receipt](../../../SOURCE_MAP.md#excluded-sources)

Read-only status (does not restart either process):

```bash
<private-python-runtime> status.py --compact
<private-python-runtime> status.py --splice --compact
```

The complementary `h12-splice6-pools02` uses a single mixed P/E assignment,
exact first and last six templates, and suffix-role guards on true-P source
bounds. Its 72,958-variable, 2,259,135-clause formula was independently built
under a new binding and passed an actual mixed 36-point calibration. The
primary formula and its running proof check were not changed.
At the backup-delivery snapshot, the splice solver had naturally returned 20
after 1,430.100 seconds and its 1,122,865,252-byte original proof was being checked
separately. Its existing controlled driver is retained for its natural receipt.
The primary bound above depends only on the primary formula's two successful
checks and independent reconstruction; no backup success is assumed.

For a full replay on Linux, use the exact retained primary files:

```bash
<private-artifact-root> \
  <private-artifact-root> \
  <private-artifact-root> \
  -t 2147483647 -b
```

This command checks the already produced proof; it is not a request to rerun
the solver or replace any evidence. Large CNFs, baseline bodies and DRATs stay
complete on Linux. Small manifests and structural input snapshots are exported
separately for local inspection. Old H11 files and historical jobs are untouched.
