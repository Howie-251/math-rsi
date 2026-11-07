# 35-state cardinality charging: C1 production report

Date: 2026-09-03

Updated: 2026-09-13. Independent acceptance was published at 09:57:33 UTC+8:
the effective C1 result is ten checker-qualified `VERIFIED_UNSAT` cells,
zero UNKNOWN and zero counterexamples. The accepted receipt establishes C1
and `N<=34` in the domain below. The immutable pre-audit final deliberately
retains `c1_proved=false`; publication authority comes from the separate
accepted receipt, not an edit to that final. Earlier OPEN checkpoints and
failed generations below are historical provenance, not the current outcome.
The full charging inequality `m>=e` and `N<=25` are not proved by C1.

The consolidated [methods and results checkpoint](../.trellis/tasks/09-03-35-state-cardinality-charging/research/methods-and-results-20260913.md)
records the N25 structural work, vocabulary obstructions, and order-generic
cardinality proof dependencies. Current acceptance hashes are at the end here.

## Scope and frozen evidence

This campaign starts from the complete canonical family of 35 down-set state
types: 25 ordinary and 10 exceptional.  It does not extend a fixed N25
transition formula.  Previously accepted Qlt and Qeq/Qgt evidence, together
with the prior Agt1, triple-only, ordinary-matrix, singleton, and Hall
artifacts, is frozen.  `qv21` was deliberately never run and remains outside
this campaign.  The seal's explicit frozen-invocation registry records zero
calls **by this C1 campaign** to `Qlt`, the never-run `qv21` slot, `Agt1`,
`triple_only`, `transition_ordinary_matrix`, and
`Qgt_singletons_or_hall`; it does not
claim that the historical campaigns had zero executions, nor reinterpret any
earlier evidence as a C1 cell.  The fact that `qv21` was historically never
run is separate provenance, not an inference from the new seal's zero counter.

Let \(\mathcal T_N\) be the class of complete ordered two-color rank-3
signotope colorings on `N` points that satisfy the blue-path-5 and red-path-6
bounds and contain no weak 7-gon, and put
\(\mathcal T=\bigcup_N\mathcal T_N\).  Here and throughout the theorem
statements, `X` ranges over \(\mathcal T\).  A strict-cell result makes no
claim about merely path-bounded colorings outside this target-free domain.
Let `e(X)` be the number of occupied exceptional types and `m(X)` the number
of globally missing ordinary types.
Endpoint-state injection gives

\[
|X|=(25-m(X))+e(X)=25+e(X)-m(X).
\]

The first layer is

\[
C_1:\qquad\forall X\in\mathcal T,\quad
e(X)\ge1\Longrightarrow m(X)\ge1.
\]

Its exact bad cells are

\[
\mathcal A_{1,e}
=\{X\in\mathcal T_{25+e}:e(X)=e,\ m(X)=0\},
\qquad e=1,\ldots,10.
\]

For each mathematical class \(\mathcal A_{1,e}\), the campaign materializes a
distinct strict CNF \(\Phi^{\rm strict}_{1,e}\); `A[1,e]` is only the campaign
label for this semantic/CNF pair.

Thus C1 is a ten-cell finite coverage problem at orders 26 through 35.  If all
ten strict CNFs are independently proof-verified UNSAT, the encoding bridge
below makes all ten mathematical classes empty and proves C1.  The numerical
consequence has two branches.  If `e(X)=0`, then
`|X|=25-m(X)<=25`.  If `e(X)>=1`, C1 gives `m(X)>=1`, while the catalog gives
`e(X)<=10`, and therefore

\[
|X|=25+e(X)-m(X)\le25+10-1=34.
\]

So complete C1 closure proves the intermediate bound `|X|<=34` without a
heredity argument.  It does not by itself prove the final bound 25.

## Mathematical dependency audit

The paper-level theorem graph is recorded in
`.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md`.
The main dependencies are deliberately separated:

1. independent enumeration gives exactly 35 canonical states, split 25/10;
2. completeness of the coloring and the exact terminal-path recurrence prove
   endpoint-state injection, while the two path bounds separately place those
   distinct states inside the finite 35-state catalog (neither step needs N25,
   signotope, or weak-7-freeness);
3. injection gives the counting identity above;
4. the strict base and exact state/occupancy/count encoding are sound and
   complete, so CNF satisfiability is equivalent to nonemptiness of the
   corresponding mathematical cell;
5. exact `(e,m)` cells cover every target-free counterexample to C1;
6. only proof/checker-qualified closure of all ten strict cells establishes
   C1.

The full triangular registry contains 55 cells
`A[r,e]`, `1 <= r <= e <= 10`, in `(r,e)` order.  The C1 row and the ten-cell
N26 spine are immutable projections of that same registry.  The N26 spine can
eventually prove the numerical bound 25 by heredity, but the hereditary object
is the restricted coloring, not its occupancy mask: endpoint states,
occupancy, `e`, and `m` must be recomputed after restricting to 26 points.
The spine cannot replace the off-diagonal cells needed for the stronger layer
theorems.

If all ten layers are ultimately proved, full charging also has two explicit
branches.  For `e(X)=0`, `m(X)>=e(X)` is immediate.  For
`e(X)=k in {1,...,10}`, theorem `C_k` gives `m(X)>=k=e(X)`.  Only after this
case split may the identity be used to conclude `|X|<=25`.

## Formula and checker audit

The theorem interpretation depends on the following bidirectional encoding
statement for every registered strict cell:

\[
\Phi^{\rm strict}_{r,e}\text{ is SAT}
\quad\Longleftrightarrow\quad
\mathcal A_{r,e}\ne\varnothing.
\]

In the forward direction, soundness of the order-generic base makes the triple
assignment a target-free rank-3 signotope coloring, exact state clauses recover
its endpoint states, occupancy is an iff, and the four at-most encodings
enforce the two exact counts.  In the reverse direction, completeness of the
base encoding extends every coloring in \(\mathcal A_{r,e}\) by its canonical
path/target auxiliaries.  The packet at-most-one-sign-change axiom gives the
same-endpoint path-deletion lemma, which supplies the downward implications
`P(i,j,d) -> P(i,j,d-1)` required by the path encoding.  Target lifting is
separate: in the `(7,5,6)` scope a weak 7-gon is exactly a blue cap4 and red
cup5 with common outer endpoints, so weak-7-freeness directly satisfies the
strict target clauses.  The exact state/occupancy definitions and all four
complete deterministic at-most encodings then supply some auxiliary extension
to a satisfying CNF assignment; uniqueness of totalizer auxiliaries is not
claimed.  Independent SAT replay audits the forward direction; the
construction/completeness argument for the reverse direction is what allows
proof-verified CNF UNSAT to exclude a mathematical class.  Publication may
invoke this bridge only for CNFs freshly reconstructed by the exact hash-bound
sealed builder/runtime closure.

- Strict base: `lib.erdos.etv_signotope(7,5,6,N)`.
- Relaxed discovery base: `lib.erdos.etv_signotope_extension(7,5,6,N)`; it
  omits only the global weak-7 target family at the intended constraint level.
  After projection to triple colorings its semantic model class contains the
  strict class; this containment is called proper only if an audited relaxed
  witness is actually shown to contain a weak 7-gon.  The serialized CNFs are
  not literal clause subsets because omission changes later auxiliary IDs, so
  their bytes and hashes remain independent.
- Literal polarity is fixed by `STATE_756_SPEC` and the recurrence, not by
  legacy group labels: true `x` is red, `cap` uses `~x` and is the blue family
  bounded at length 5, while `cup` uses `x` and is the red family bounded at
  length 6.  Historical `no_red_5_path`/`no_blue_6_path` names are inverted
  relative to these semantics.
- No symmetry breaking is enabled.
- Every endpoint has exactly one canonical state atom.
- There is no cross-endpoint all-different/injection clause family.  The
  mathematical injection lemma is used to bind an arbitrary counterexample's
  order to `N=25+e-m` and thereby prove 55-cell coverage; SAT replay recomputes
  it only as a defensive consistency check.
- Every occupancy atom is the bidirectional equivalence
  `O[G] <-> OR_v S[v,G]`.
- Exact `e` and exact `m` use four chained deterministic at-most encodings,
  with contiguous named auxiliary-variable roles and a hash-stable clause
  order.
- SAT acceptance requires a unique SAT status, a complete assignment through
  the final totalizer variable, replay of every CNF clause, independent
  coloring/signotope/path/target reconstruction, all 35 state atoms,
  endpoint injection, occupancy equivalence, and exact `e,m,N`.
- Raw return code 20 is only a persistent-zero observation.  UNSAT requires a
  nonempty AE proof and the pinned independent checker with return code zero
  and exactly one `s VERIFIED` status line.
- An audited relaxed SAT assignment is only a construction/discovery witness
  in the target-allowed class.  It does not prove the corresponding
  strict cell nonempty and supplies no strict theorem credit.

Pinned production tools:

- AE Kissat:
  `/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`, SHA-256
  `c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa`.
- Checker snapshot:
  `/data/ktqiu_hdd/math_agent/res/state_charging/20260822_unknown_resolution/any/ae_c2e44161_3600/adapter/proof_checker.snapshot`,
  SHA-256
  `2f01df83916c158d7da43deefde1ea3ea60b19f5d636ae03f31042e88ef179e9`.

## Pre-production verification

Before sealed suite generation, the authoritative server checkout passed 33
tests from `test_state_charging_cardinality_campaign`,
`test_state_charging_cardinality_layers`, and
`test_cardinality_c1_remote_tools_20260903`.  They cover the catalog and
registry, exact-cardinality semantics, complete model parsing, independent
state/count checking, strict versus relaxed target semantics, manifest path
and hash boundaries, three-stage classification, checker verdict uniqueness,
canonical-prefix resume, global SAT stop, lock integrity, and receipt
publication ordering.

A later local combined run of those three modules plus
`test_cardinality_c1_final_tools_20260903` passed 40 tests.  The seven
final-tools tests were uploaded to the server only after sealed suite
generation had begun and were never part of that runtime registry.  The
40-test statement is therefore follow-up local regression evidence, not
sealed production evidence.  Separately, local pre-production validation ran
syntax checks and zero-solver self-tests for all four production programs.
The generator self-test discovered a 15-file import closure from the current
source tree and hashed generator, runner, finalizer, and acceptance auditor by
exact bytes; it did not itself build the production overlay.

The following are disposable pre-production server formula smokes.  They
streamed and hashed each canonical DIMACS byte sequence without writing a
retained CNF and invoked neither solver nor checker:

| mode | cell | vars | clauses | DIMACS bytes | peak RSS KiB | DIMACS byte SHA-256 |
|---|---:|---:|---:|---:|---:|---|
| relaxed | A[1,1], N26 | 326,539 | 1,199,872 | 20,204,717 | 583,924 | `1030d317d5662e6de670e53c1f23a93d25ff61c2e566dc4a49e8a9628adb5dec` |
| strict | A[1,1], N26 | 327,276 | 1,202,820 | 20,249,674 | 585,316 | `ac04b6b0d52653564ce92ef5377551754f52ee05da228539b838597573e2cae0` |
| relaxed | A[1,10], N35 | 1,123,746 | 4,065,146 | 71,614,864 | 1,936,508 | `1602f3f87604ee6fc56cc575eeb4f89837337259e1b406aa5725ff43807493f8` |
| strict | A[1,10], N35 | 1,125,203 | 4,070,974 | 71,712,483 | 1,930,072 | `d79379ec3dd5313be5c67a9b4fb57c6f6863b66ee7d8534e036c21263cf88790` |

These four hashes identify only the canonical DIMACS byte streams produced by
the disposable smoke.  They are not hashes of retained CNF files.  They
are not the sealed 20-formula manifest identity or `suite_sha256`, do not bind
the eventual production files, and carry no SAT/UNSAT evidence.  Production
publication must instead cite every sealed manifest row's path, size, and
SHA-256 together with the manifest and suite identities.

## Sealed execution policy

1. Generate all 20 immutable CNFs: relaxed and strict copies of each C1 cell.
2. Require all ten relaxed cells to return independently audited SAT before
   opening the strict phase.  These are target-allowed construction/discovery
   witnesses only.  Any other relaxed outcome leaves v1 OPEN; this sealed
   schedule has no relaxed proof escalation and awards no strict theorem
   credit from relaxed evidence.
3. Run strict SAT-first in the interleaved order
   `e = 10,1,9,2,8,3,7,4,6,5`.
4. On the first independently audited strict SAT, create a global stop receipt
   and prohibit every remaining solve/checker invocation.
5. Only after a stop-free complete strict SAT-first row, proof-escalate the
   persistent-zero cells in the same order.
6. Fresh-finalize only a valid audited-SAT stop or a complete stop-free row.
   The report always contains all ten strict cells; stopped/unresolved cells
   are explicit UNKNOWN entries.
7. Run an independent fresh-finalization subprocess and require byte-for-byte
   equality before publishing the acceptance receipt.

Default sealed budgets are 900 seconds for each relaxed and strict SAT-first
cell, 7200 seconds for each proof-producing cell, 7200 seconds for the checker,
and a 120-second outer solver grace period.  The campaign uses one worker to
retain a single canonical prefix and immediate stop semantics.

## Production result

The sealed source campaign completed and was independently accepted on
2026-09-03.  Its result is an audited **OPEN** outcome, not a proof of C1:

- all ten target-allowed relaxed gates are AUDITED_SAT;
- all ten strict SAT-first cells are TIMEOUT after their sealed 900-second
  budgets;
- there are zero strict counterexamples, zero checker-qualified UNSAT cells,
  and ten UNKNOWN cells;
- the empty proof-escalation schedule made zero solver, proof-producer, and
  checker invocations; and
- the acceptance auditor rebuilt the final in a fresh process and required
  byte equality.

### Immutable identities and protected roots

| artifact | bytes | serialized-file SHA-256 |
|---|---:|---|
| campaign config | 3,407 | b79ce783bfdf338ae91af044c16d1382fd273b99a58297dadd0dc6bb9c8ab335 |
| suite manifest | 1,017,370 | afd6d141fa9b5fa1832b34a4283a9f0ef66887879f133dd5ee31b74d0384e997 |
| campaign seal | 7,978 | 5376c753ae41a978dad410e06d17a8ddee53c3320dc40ebe1a0b6604ed5c3642 |
| retained final | 29,109 | 34acce18c8af91c77235736d39010b22b1ae76421162b9f45f2ba9c4ad93e4c8 |
| acceptance receipt | 3,132 | 06cbf1c3cb61dc67cf4773af759b03008018ffb65df05223b1a581899e64ab76 |

The semantic suite identity is
cb72cc710df8a6ac8327a7f7df98924aeceb770ee2f2c8f0787e9902a01de3ae;
the semantic seal identity is
1edc03953a0d215dcf9bfc675041899d5bb1a857126a2a71729d991406052703;
and the runtime-registry identity is
80b578532941f5ee8c9932a5abdc91f7392af6df6b0b5e75f12080d5bf0cfc20.
The protected roots are:

- suite: /data/ktqiu_hdd/math_agent/res/state_charging/20260903_35_state_cardinality_c1_v1/suite;
- campaign: /data/ktqiu_hdd/math_agent/res/state_charging/20260903_35_state_cardinality_c1_v1/attempt00; and
- overlay: /data/ktqiu_hdd/math_agent/tmp/cardinality_c1_overlay_20260903_v1.

The seal binds a 19-file runtime closure by exact path, size, and SHA-256.  In
particular it binds the generator, runner, finalizer, acceptance auditor, the
two cardinality modules, and all imported encoding modules.  The pinned solver
and checker identities are listed above.  Generation records zero solver,
proof-producer, and checker invocations.  The accepted frozen-campaign counter
also records zero invocations for Qlt, qv21, Agt1, the transition matrix,
Qgt singletons/Hall, and triple-only.

### Sealed 20-formula manifest

The 20 retained CNFs contain 846,216,628 bytes in total.  Each path is under
the protected suite root; the basename below, together with that root and
mode directory, identifies the exact retained file.

| mode | e | N | variables | clauses | bytes | CNF SHA-256 | basename |
|---|---:|---:|---:|---:|---:|---|---|
| relaxed | 1 | 26 | 326,539 | 1,199,872 | 20,204,717 | f0bd4a72a74910db42241e124413b7513b633837594c64923f772fdd031dc484 | cardinality_A_r01_e01_N26_target_allowed_relaxed.cnf |
| relaxed | 2 | 27 | 382,244 | 1,400,804 | 23,867,884 | bbc0aa398e72d8562dda12a7b0aa418532011997b7b6c3e6190ab59fb80549d3 | cardinality_A_r01_e02_N27_target_allowed_relaxed.cnf |
| relaxed | 3 | 28 | 444,793 | 1,626,244 | 27,828,366 | fff4a2bc3a1dbb7fa2cdff0b033a93063f23444e3cfb56055d4981b4ec32a38e | cardinality_A_r01_e03_N28_target_allowed_relaxed.cnf |
| relaxed | 4 | 29 | 514,767 | 1,878,214 | 32,263,122 | 0161815f2f9cc1f468c2a9e9f06f2f8d3136d106f61b1ac3158023db81e8a3b4 | cardinality_A_r01_e04_N29_target_allowed_relaxed.cnf |
| relaxed | 5 | 30 | 592,734 | 2,158,731 | 37,207,470 | 2e0e3d550268223b893b0bc738e0f8bb3b9b4ed8c61e30b8d8906f436fe9caaa | cardinality_A_r01_e05_N30_target_allowed_relaxed.cnf |
| relaxed | 6 | 31 | 679,283 | 2,469,886 | 42,698,671 | e9f18271bbdc1514708b021855b54c5a1fd23d4aff228ca9d8c5c9f04c60a563 | cardinality_A_r01_e06_N31_target_allowed_relaxed.cnf |
| relaxed | 7 | 32 | 775,024 | 2,813,844 | 48,775,702 | f6bcc4b97d21d3ba07fe00df26350e28d727e722cc5d0b8deaab6261038dce51 | cardinality_A_r01_e07_N32_target_allowed_relaxed.cnf |
| relaxed | 8 | 33 | 880,588 | 3,192,844 | 55,476,268 | 6d9c084f808cc857da6c568d13279d34d1a07e0987d37589c2486bbd6ef6aafb | cardinality_A_r01_e08_N33_target_allowed_relaxed.cnf |
| relaxed | 9 | 34 | 996,593 | 3,609,120 | 62,829,188 | 047e897d1e4517d4219e89125581e748f044c06ad22519f59243687c08c38f42 | cardinality_A_r01_e09_N34_target_allowed_relaxed.cnf |
| relaxed | 10 | 35 | 1,123,746 | 4,065,146 | 71,614,864 | 923855dd3a7fac6b15450a3b0725cec1c51c3001655bfa34ca72e6464ef3cdb4 | cardinality_A_r01_e10_N35_target_allowed_relaxed.cnf |
| strict | 1 | 26 | 327,276 | 1,202,820 | 20,249,674 | 932224251a5c0a66c0253b28a15d393141d7282e33c5f02c71956b97095f796a | cardinality_A_r01_e01_N26_strict_no_target.cnf |
| strict | 2 | 27 | 383,049 | 1,404,024 | 23,918,599 | 11d5e358317553d2c4a4492527afbb66563f79a9ebbc018bc11651e1d7bdfbc3 | cardinality_A_r01_e02_N27_strict_no_target.cnf |
| strict | 3 | 28 | 445,669 | 1,629,748 | 27,883,554 | e79001fa3556555eee00613965bee7d4baf569aaaf038d0aae822174d313c364 | cardinality_A_r01_e03_N28_strict_no_target.cnf |
| strict | 4 | 29 | 515,717 | 1,882,014 | 32,322,972 | c617fb6e9a580527e4983c6399644dd38806eca6c6625912be9d8f21184f0651 | cardinality_A_r01_e04_N29_strict_no_target.cnf |
| strict | 5 | 30 | 593,761 | 2,162,839 | 37,272,171 | aee32e3f05197e8df30c10baf12c3bbd2649d72f01be2ee8aaf5f7d7cada1ac4 | cardinality_A_r01_e05_N30_strict_no_target.cnf |
| strict | 6 | 31 | 680,390 | 2,474,314 | 42,768,412 | e441198b5b50e333ef7261af2663e9295acd0d3444af1f71519f9823ac59fc41 | cardinality_A_r01_e06_N31_strict_no_target.cnf |
| strict | 7 | 32 | 776,214 | 2,818,604 | 48,850,672 | bc0d9bcdc1d1333f2d186a06581ef72a22f0b19c78fa9f4b7e3b3f952ef7848a | cardinality_A_r01_e07_N32_strict_no_target.cnf |
| strict | 8 | 33 | 881,864 | 3,197,948 | 55,556,656 | db258e45a318cc4fa0caaba2e702247e4562af4084fcddffb820ca9f3e179e73 | cardinality_A_r01_e08_N33_strict_no_target.cnf |
| strict | 9 | 34 | 997,958 | 3,614,580 | 62,915,183 | ff1638272d0bb388fc7914f6c961e2f6b1c946250fce74523f0efecdfdab4cfc | cardinality_A_r01_e09_N34_strict_no_target.cnf |
| strict | 10 | 35 | 1,125,203 | 4,070,974 | 71,712,483 | 6a9dee71e58db7ec815f3dae6f3892183cd59310e34f51712220c90d6c9778b9 | cardinality_A_r01_e10_N35_strict_no_target.cnf |

### Relaxed nonvacuity gates

Every row returned code 10 with the unique solver status SATISFIABLE and was
accepted only after complete-assignment CNF replay and independent semantic
reconstruction.  Times are wall-clock seconds.  “Status SHA” and “audit SHA”
are serialized-file hashes, not self-hashes embedded in those records.

| e | N | result | seconds | status SHA-256 | SAT-audit SHA-256 |
|---:|---:|---|---:|---|---|
| 1 | 26 | AUDITED_SAT | 5.079 | 63dc8c15e606e83509c5cabc938b83c1b0fcdb27a908334fef13fc13ee8a22fb | 831af87437fa8ae181ec28780ba681639268ebd6d9260b6730564ccba23dbac3 |
| 2 | 27 | AUDITED_SAT | 4.928 | 9171e11f6fd239b1b6f61d034f03a391bfa07c998a455e0923b2f4d9b9f246d5 | b908ef3b9ae6aec3f8f245048842dffd75dbcb0f811177349098a2447f9c1662 |
| 3 | 28 | AUDITED_SAT | 3.374 | 9f0b18d8ea06ed94e0d5c40f3f92ffab29566bdc93cd3c80f4cb5265a1636f64 | 58e21eddc7633d71e0115e12f98044c3077b6b70a16f9d07bfb6f11341c8e52b |
| 4 | 29 | AUDITED_SAT | 3.725 | 9bfaf56dddd79f4f189b51ba0cda193b642162b3483638e9ea127fc7ebb6192d | c0880eb029428c5df3a5cfbe6122bf0f8d9eaa20feb67b2fa02e7697f1dbe1d1 |
| 5 | 30 | AUDITED_SAT | 4.527 | 893ec4e30375d7c4a29c9e3d7033705ed758229d838d877f992b8cbe3d913114 | f46c82cdf5cdebc56ac79773da65ae68dadf1d1499cb71a32fe735f6949e3940 |
| 6 | 31 | AUDITED_SAT | 4.627 | 94b0bace7bf68b6a21269dd4012ebc5fcbdfa77de422845ddb34cbb2ccefe2fe | 757c34671c942ab9669db77bd51471cfb7138965c4eb6049aa5077e43a68d1dd |
| 7 | 32 | AUDITED_SAT | 7.385 | 9fe992fa6c7f900ad294d5d18f15a06a41d82018124c811bed36c6f5c5ceb2d4 | 98b7d666ae7eaf610cb8f9282612b36a4b9c3240899227afa550fa01f7bb1a3d |
| 8 | 33 | AUDITED_SAT | 7.987 | 2d95cb0b9831cf4a49d4d2b47b5db7ca483a9fcca3f1048e90a2c3548e27e7b3 | b8618ce137303ebe792b9737a6234014846ef74185d24c47523f9f636c90e3fa |
| 9 | 34 | AUDITED_SAT | 21.325 | 688f4ab503672bcb7eeea3d49e64869e925abdc42c90515e80b914e14ceb3ad7 | 3a27e4686120c57604f53132846c29f58c32b1626b1a01f12654d0c320c150db |
| 10 | 35 | AUDITED_SAT | 11.096 | 09a3fb38abdebbf027670c05ce2b6573e864094a73d2880237e497c7bca838a1 | 8305ba9d200856131449ca8a4acc9145fa4d3a78094d23e5781aa101ad8e1823 |

The relaxed phase receipt is 6,414 bytes with SHA-256
286c984ae0f2e2b9cff921d8bf8e5da7869315c5e767113b5d706b435794d0f0.

### Strict SAT-first row

Every strict command was the pinned AE Kissat with --no-binary, --time=900,
and the sealed CNF path.  Every row returned code 0, reported the unique status
UNKNOWN, had outer_timed_out=false, and produced no proof or checker call.
Thus each final row is UNKNOWN with reason strict_sat_first_TIMEOUT.  The
following status and stdout hashes are serialized-file hashes.

| e | N | seconds | status SHA-256 | stdout SHA-256 | stdout bytes |
|---:|---:|---:|---|---|---:|
| 1 | 26 | 900.024 | e36846acd9bec3348948eee17417298342923eacf307f4501bec53b43ba99450 | 506ac3484be63bff6a0861f2bbb5589d84c62da697da2e7f5a698e57dda82144 | 106,552 |
| 2 | 27 | 900.031 | 0b8dec48f3b5462f3701ce44daf15b2f301fbbf45451fb1939d8d0159c6c7b40 | 868493c8a935299325bfa4ef5bfc4a9ab13d9a5a43f95da0ee462e1d671b2939 | 98,883 |
| 3 | 28 | 900.029 | 2efda9a4a7829f3209b9f8f6d81a2618d715f074748571bd1e97c7492728c51d | 5d7404bc46c969545a88c2741e3ff743e825d27bbee891bfcb2b9c3882c74228 | 89,129 |
| 4 | 29 | 900.054 | c467878e0b01a2c48c94eb987b1bc21f3052ed8e808f4c232a1b29c8a1f061a7 | d876a649f22bddf93c87bc6a52f62cab7b7d8565953f41dd2c25a360215cb4dc | 92,089 |
| 5 | 30 | 900.013 | 9a7fcadb2743e272b2638b50703c02f00012017cdc1cf9c5e24cb95739903535 | 3b56ac85955455d20cc8ea4985b76ff4b2b0e69676e1eb85cb261f829ad158bf | 83,788 |
| 6 | 31 | 900.094 | 838978f61ec8d8afdd5fbace5ce44429c860c16a48bf7e297ff234f91cfcc448 | 118fe1dc96ae9333c8dd8435dd4d4f0214f925a3c29303e0d475d8259e238cb4 | 75,186 |
| 7 | 32 | 900.051 | d677db61b36d8f12044d7b1556c62d4cfb917aea1d2d68df831a96e4de6ef4f0 | e05602ff81bbb5ca5189f2e697ba8ef817ba2e81f02150ae225ca076b29f9f30 | 75,206 |
| 8 | 33 | 900.077 | 75176bf866666245eb7d62bb6bd80a5f57a76215a78535d6304e217c695da9a2 | edcbc05a772ba9af02cae5909f70d057966dda8f4d6a15752da40e95e0a18629 | 71,395 |
| 9 | 34 | 900.021 | da6fc726888a2865246ba0e2cb3934db7e9bc558c280c5162270d3053ebd9d45 | 440b15d704d5b66372d12392ff8aaf06e78816abf9f6be2c36235e7f68648450 | 67,556 |
| 10 | 35 | 900.049 | 1fa3aa08e3568c567b2075638c4273a88d1be6fd8a2e3306c1b7f46e57aab5ee | 8244f1db80e40d4271802ec1fa2b72e10aca77ce11816cdadb367f53612c1c0e | 64,368 |

The strict phase receipt is 6,221 bytes with SHA-256
c3be0267a6c1976b486af43bcbc13c030d4252fbb00c2d6cbb63b2d84241dea1.
The explicit empty proof-phase receipt is 811 bytes with SHA-256
03b3151d89e3975d3552e382074b7a1018c7170f02c1271e6b141b6cc292c810;
it binds schedule=[], status_bindings=[], and zero invocations.  The final
progress snapshot is 14,611 bytes with SHA-256
4577f204b1b0373c1dd6a28469a38dff37da664807b480fcc469b835268cc6d3.

### Fresh finalization, acceptance, and mathematical conclusion

The retained final has semantic identity
80e660771f50a13f9bd05cec3a771efd6f799f44f52b2d23b1e81ff23a425915.
The acceptance receipt has semantic audit identity
bc544efd27c63235a1085fc18b56e6988b4b5c7d9c3eb7418603af21d3b8b450
and status ACCEPTED_FRESH_FINALIZATION_BYTE_EQUAL.  It records all of the
following as true: fresh formula replay, validation of all twenty retained CNF
byte streams, and byte equality between the retained final and a fresh
finalizer subprocess.  The subprocess returned code zero.

The accepted classification is therefore:

\[
(\#\mathrm{VERIFIED\_UNSAT},\#\mathrm{COUNTEREXAMPLE},
  \#\mathrm{UNKNOWN})=(0,0,10).
\]

Consequently this source attempt proves neither C1 nor N<=34.  It preserves
only the catalog/counting baseline N<=35 (and any separately certified prior
bound).  No strict SAT counterexample was found, but absence of a short-budget
counterexample is not theorem evidence.

### Required TIMEOUT resolution

All ten source strict TIMEOUT cells were selected for a separate immutable,
source-bound add-on following user authorization. The accepted source attempt
remains closed-world. The finite v2 result and its independently accepted
composite final are recorded below; unresolved rows are eligible only for the
separately authorized unbounded v3 successor.

## Accepted finite timeout-resolution v2

The result root is
`/data/ktqiu_hdd/math_agent/res/state_charging/20260903_35_state_cardinality_c1_timeout_resolution_v2`,
with campaign `attempt00`. Its runner completed on 2026-09-04 at 17:28 UTC+8;
`/tmp/c1_timeout_addon_v2_run_20260903_01a04149.log` records
`resolution_complete`, ten terminal candidates, and `C1_RUN_EXIT=0`.

| Exact cells | v2 classification | Effective C1 final classification |
|---|---|---|
| e=1,2,3,4,5 | `VERIFIED_UNSAT` | Five checker-qualified `VERIFIED_UNSAT` |
| e=6,7,8,9 | `TIMEOUT` | Four `UNKNOWN` |
| e=10 | `UNVERIFIED_RAW_RETURN_20`; checker exceeded 7200 seconds | One `UNKNOWN` |

The independent auditor completed on 2026-09-06 at 02:03:45 UTC+8. Its
`tmp/c1_v2_audit_20260905.exit` is exactly `0\n`. The canonical acceptance
receipt has status `ACCEPTED_FRESH_COMPOSITE_FINALIZATION_BYTE_EQUAL`, records
five fresh independent checker replays, fresh-finalizer return code zero,
byte equality with the retained final, and zero source-attempt writes.
These receipt and runtime bindings were revalidated read-only on 2026-09-11.

| v2 artifact | bytes | Serialized-file SHA-256 |
|---|---:|---|
| `campaign_seal.json` | 23,037 | `65f9af60744cda6c2765bb4bf2e44d0f9704352238d1b654522bcd5fe5528b86` |
| `cardinality_c1_resolved_final.json` | 46,284 | `aeccd037f231d6d43b9af18523925aebc2d362bc4bc612846126e5768b6708e2` |
| `campaign_acceptance_audit.json` | 3,622 | `e1f1702039e69582149b6261501c4c7018e3a2b96769813fdc72430e3a2a413f` |

Byte-identical local review copies of these three JSON files are retained in
`tmp/c1_v2_accepted_20260911/`; their downloaded file hashes were checked
against the server anchors above. The Linux evidence remains authoritative.

The final semantic hash is
`ba911b35260f8dacfd8ed1466c172a6d3e6cb43dc572a054bad9734ccdd14979`;
the acceptance semantic hash is
`b57bbab3f9be1df52b75d44604e73407dd61aa5ce3b96a14fc85093e943c384a`.
The candidate-set hash is
`9152394b737a2efde3049f3f8972252635f17ba25cb3b89dcbefe7fb278fa39e`;
the runtime-registry hash is
`47aeb93a15bbfe11ed24eda424fb28705029ae5827a0322013f4725efc65ad9c`.

This is an accepted **OPEN** result: `c1_proved=false`,
`certified_upper_bound=null`, `COUNTEREXAMPLE=0`, and `UNKNOWN=5`. It does not
establish C1 or `N<=34`. In particular, e10's raw return code 20 is not an
additional UNSAT theorem, despite its retained nonempty proof.

### Failed generation and launcher provenance

The earlier timeout-resolution_v1 generation failed with
`ERROR: candidate 0 cell fields drifted`, retained in
`/data/ktqiu_hdd/math_agent/tmp/c1_timeout_addon_generate.log`.
Its partial result root
`res/state_charging/20260903_35_state_cardinality_c1_timeout_resolution_v1`
and overlay `tmp/cardinality_c1_timeout_resolution_overlay_20260903_v1`
remain frozen and receive no theorem credit. They are distinct from the
accepted original C1 source campaign `20260903_35_state_cardinality_c1_v1`.

The single production v2 finalizer ran on 2026-09-05. Its initial screen
wrapper expanded `$rc` before bash executed the wrapper, so
`tmp/c1_v2_finalize_20260905.exit` contains only a newline (hex `0a`) and is
not an exit-code certificate. The actual sealed finalizer argv was intact;
its completed JSON output in `tmp/c1_v2_finalize_20260905.log` matched the
retained final's file and semantic hashes. The user authorized preserving
this operational error and proceeding through independently checked output.

A later long inline screen auditor dispatch created no process or log and
did not run the auditor. The actual auditor was started once using the short
path `tmp/launch_cardinality_c1_v2_audit_20260905.sh` (SHA-256
`8c8afffe31277963ba2a98c95d4c607f61756466b89fdac93d42e78332b12317`).
It used fixed success/failure branches and produced the accepted receipt
above. The malformed earlier marker has been preserved, not repaired or used
as theorem evidence. Future persistent launches use standalone scripts.

## Authorized unbounded successor v3

The sealed result root is
`/data/ktqiu_hdd/math_agent/res/state_charging/20260903_35_state_cardinality_c1_timeout_resolution_v3`,
with overlay
`/data/ktqiu_hdd/math_agent/tmp/cardinality_c1_timeout_resolution_overlay_20260903_v3`.
Both roots were absent at the 2026-09-11 preflight. First generation was
started at 17:34 UTC+8 in screen `42642.c1v3gen_20260911`, using
`/opt/anaconda3/envs/forktqiu3/bin/python3.12` and the externally pinned v2
seal, final, and acceptance hashes above. Its standalone launcher is
`tmp/launch_cardinality_c1_v3_generate_20260911.sh` (SHA-256
`022f23ebd6617b0e133b50a9d9a65b6745f487f3146ef317b19c223c41d056a5`).

The authorized candidate set is exactly e6-e9 with
`SOLVE_AND_CHECK_UNBOUNDED`, and e10 with
`CHECK_RETAINED_PROOF_UNBOUNDED`. The latter reuses the exact hash-bound v2
proof. The five accepted e1-e5 rows are inherited without new solver runs.
All three execution limits are null; the e6-e9 solver argv contains no
`--time` option. The e10 command uses the retained v2 proof, whose SHA-256 is
`c109c9438dd7f84f0823710f296dcf97fe4e1054c6e117256c78e0dfd78208a0`
and size is 2,599,101,854 bytes. The sealed order is e10, e9, e8, e7, e6.

Generation completed successfully by 17:48 UTC+8; the exit record
`tmp/c1_v3_generate_20260911.exit` is `0\n`. Generation recorded zero solver,
proof-producer and checker invocations, and zero predecessor writes.

| v3 binding | SHA-256 |
|---|---|
| Seal serialized file (17,047 bytes) | `cd3f39092b5ed6d1f6ff5f41e5d31fbd42d958b62499ee45a8903b150ca2eb0e` |
| Seal semantic value | `bb84231f7c2044dd75910604aa2aa2475888fed7d8f0b9b3c76eacaaf9160065` |
| Configuration serialized file (15,336 bytes) | `ba156b8f6a1bc77c175ca2b989f56811dc120288627b0b153d4696c47629eeb7` |
| Candidate set | `451ac19db2764520b1399e337fb112805c2769a2705774223d33d7819efd26f0` |
| Runtime registry | `5ca810c551dcc37bc9da9007815d75285dcc70c45d7d515abc1905d149abaa2a` |
| Source replay | `ca4ba1362e6b4838180b99c1230368f631bf3d4ce30fa360bb759e8d90870db0` |

The seal/bootstrap runtime closure, protected roots, candidate actions and
exact solver/checker commands passed read-only validation before launch.
The runner started once at 2026-09-11 17:54:03 UTC+8 in screen
`47420.c1v3run_20260911`, PID 47425, parent launcher PID 47422, using
`/opt/anaconda3/envs/forktqiu3/bin/python3.12`. Its standalone launcher is
`tmp/launch_cardinality_c1_v3_run_20260911.sh`, SHA-256
`f56edd3850daa04bddae9875196f62e41219f3123adeab7e4b8f575e467e6214`.
Log/exit paths are `tmp/c1_v3_run_20260911.log` and
`tmp/c1_v3_run_20260911.exit`. The first process check confirmed the expected
argv, unlimited CPU time, and a live internal source-replay child (PID 47427).
This is startup validation, not yet evidence that e10's checker has started.
PID references are launch provenance; later monitoring must check actual argv.

The unchanged v3 implementation previously passed 110 focused tests locally
and 110 on Linux, with a separate Linux generator self-test confirming null
limits. On 2026-09-11 all five v3 tool hashes still matched that tested
version; those tests were not repeated. Both new operational launchers passed
Linux `bash -n` and local/server SHA-256 equality. Cell results and v3 final
publication remain pending; C1 remains `OPEN`. Never regenerate this sealed
v3 or repeat its launcher. No commit or task archive has been performed.

## Parallel task-set amendment (2026-09-12)

The user authorized e8/e7/e6 parallel workers and explicitly required unique
task ownership, arbitrary completion order, unified SAT/error stop, parallel
acceptance and a controlled handoff. This supersedes serial dispatch only;
the original seal/runtime files remain unchanged and are retained as evidence.

### Failed first migration

`20260903_35_state_cardinality_c1_timeout_resolution_v3_parallel_20260912`
contains only a 5,949-byte `protocol_seal.json`, file SHA-256
`5227b6ebccab9c55a7703a194af365c0f25f9b4ff32a059ec1f76247d511fbb6`.
Its controller failed with `AttributeError: module 'os' has no attribute
'pidfd_open'` before sending SIGSTOP. Read-only inspection confirmed the old
runner and e9 checker were still live. The failed root and original controller
were frozen; no parallel worker was launched there. Earlier nine tests had
missed the successful process-control API path.

### Tested replacement protocol

The fresh root is
`/data/ktqiu_hdd/math_agent/res/state_charging/20260903_35_state_cardinality_c1_timeout_resolution_v3_parallel_20260912_v2`.
Preparation completed once with exit `0\n` after a real system-Python pidfd
probe. `protocol_seal.json` has 8,340 bytes and externally pinned SHA-256
`4dae075cb5f56febdddf2554ed83ee03dec556e8dc26d2f15555b6d05ce8467b`.

| Artifact | SHA-256 |
|---|---|
| `tmp/c1_parallel_protocol_20260912_v2.py` | `50f092b0a657642c28b78c1ee5177e57726d38e6513933851604a5d677309ba4` |
| `tmp/c1_parallel_handoff_20260912_v2.py` | `608dc3e5d6f8631b0061e48da3be6e0a9d401f227392a54d1fcb13b6e3c6cbaa` |
| `tmp/test_c1_parallel_protocol_20260912_v2.py` | `b98b7e30d9cf47f3923aacecd5514cd36185b17ee5fcb3de60b485f7f17da6b8` |
| Prepare launcher | `016b98eaa26ebe98d0d6be8d910056756ebd790611f519622ec085393a89342c` |
| Handoff/run launcher | `e7cd8559abb76d49306d07bd14dc01c099447c4da1c216e3b5fd960f90ecff2b` |

The new 21-test Linux unittest suite passed, including real pidfd handoff,
real external-child cancellation, task-set coverage/ownership and full
finalizer/auditor accept/reject paths with synthetic evidence. A test exposed
reentrant `Popen.wait` locking during cancellation; the handler was corrected
to signal without polling/waiting. No production formula was solved by tests.
Both launchers passed Linux `bash -n` and local/remote SHA equality. These are
new amendment checks, distinct from the original unchanged 110-test suites.

e10's original verified status remains pinned at
`0ec91855c7c3d215309f2dd2bcec21ecbe2c6b5c581a294f232db8911c3760af`.
e9's retained proof is 15,750,030,233 bytes, SHA-256
`2ba0862972f1d6de214f82eead021a62de3dcabdf01c70752f1b1b889aa9b26c`.
Because e9 had no committed checker result, the amendment independently
rechecks this proof; it never infers the old solver/checker exit metadata.
e8/e7/e6 run once each, without solver or checker deadlines. All four workers
have one supervisor; audited SAT or ERROR cancels peers and preserves output.

The single handoff/run wrapper started at 11:26:28 UTC+8 in screen
`150401.c1parallel_v2_20260912`. Logs are
`tmp/c1_parallel_handoff_20260912_v2.log` and
`tmp/c1_parallel_run_20260912_v2.log`, each with a corresponding `.exit` file.
Handoff completed with exit `0\n`; its receipt `handoff_complete.json` has
SHA-256 `cf8c09f5369961458dc9366f061afe02e33d1fe953d2b1086c8b2a093ad7c800`.
The recorded actions were OS-level SIGSTOP to the old scheduler, SIGTERM to
its checker, then SIGKILL to retire the scheduler. Both pidfds reported exit.
The old wrapper naturally wrote `1\n`, and the old lock is retained; these
are intentional supersession evidence, not a clean original-run completion.
The receipt explicitly records `old_checker_result_inherited=false` and
`old_solver_exit_code=null`. No original exit metadata was fabricated.

The new supervisor (PID 150430) started at 11:27:12 UTC+8. Its
`run_started.json` SHA-256 is
`391b862df0f6bbaa781f0060977f1e6532277880406ab8d3c7bd0931377da570`.
All four workers and external processes started at 11:27:39 UTC+8:

| Task | Worker PID | External PID | Actual work |
|---|---:|---:|---|
| e8 | 150434 | 150440 | AE Kissat solve and proof production |
| e7 | 150435 | 150438 | AE Kissat solve and proof production |
| e6 | 150436 | 150441 | AE Kissat solve and proof production |
| e9 | 150437 | 150439 | Independent check of retained v3 proof |

Live argv and parent/child ownership were checked. All three solver commands
omit `--time`; `/proc/PID/limits` reports unlimited CPU time for all four
external processes. No new terminal cell exists at this checkpoint. PIDs are
launch provenance only; monitoring must verify current identity, not PID alone.

The existing two-hour heartbeat `monitor-c1-unbounded-reruns` was restored to
ACTIVE with the new task-set root, seal, process identities and publication
commands. It no longer instructs the old serial finalizer/auditor to run.
Unchanged healthy execution remains silent; terminal changes and failures are
reported after validation.

Only the amendment-aware `finalize` and `audit` modes may publish the merged
result; the old serial finalizer/auditor must not be run after handoff. C1
remains OPEN until an independently accepted effective 10/10 result exists.
No commit or archive was performed.

## Parallel finalization and independent acceptance (2026-09-12)

This section preserves the pre-acceptance checkpoint. The following dated
section records the completed independent audit.

The parallel controller completed at 19:47:43 UTC+8. e6/e7/e8/e9 all have
`VERIFIED_UNSAT`, actual zero worker exits, bound nonempty proofs and exactly
one `s VERIFIED` checker verdict with return code zero. There is no global
stop or controller error. The sealed read-only execution validator passed,
including frozen predecessor inventories and unique complete task ownership.
e10 is inherited from original v3 and e1-e5 from accepted finite v2; no
additional solver was run during publication.

| Artifact in the parallel v2 root | Bytes | Serialized SHA-256 |
|---|---:|---|
| `execution_terminal.json` | 9,996 | `f5ce2d07e561c7be7ffc35e120732240c42aeae8e43d989679384fe755441618` |
| `run_exit.json` | 430 | `0650d9be4106a13234d9c6cd3da6acb13c1e0b3143707a04b75c3f0aae822a7e` |
| `finalize_started.json` | 417 | `f7dcb754a59bd4800be46419c88caa8aec4b1b11e8e8e6b881a855ba19100b2d` |
| `cardinality_c1_resolved_final.json` | 53,489 | `213e7415ebd7eee184679ee45826772dec5ad166c83f47c6033707484dbc182d` |
| `audit_started.json` | 598 | `5bee81be3d243573f7ad71802ddd12abce182dbd1531dec924c1bacbf95f4f75` |

The finalizer started once at 20:12:28, wrote the final at 20:22:45, and
exited cleanly; its standalone wrapper recorded `0\n`. Canonical JSON,
exact e1-e10 coverage, all ten checker-qualified rows, no UNKNOWN or
counterexamples and the protocol hash were checked separately. The final is
`PENDING_INDEPENDENT_AUDIT`, with `all_ten_checker_qualified=true`, but
`c1_proved=false` and `certified_upper_bound=null`. Eligibility is not acceptance.

The auditor started once at 20:25:51 in screen
`162958.c1parallelaudit_v2_20260912`, PID 162962. Live boot ID, start ticks,
parentage and exact argv matched `audit_started.json`; CPU time is unlimited.
It consumes the externally pinned final hash above and must freshly check
e6-e10, rebuild final bytes identically and revalidate inventories before
writing `campaign_acceptance_audit.json` last. That receipt is not yet present.

Standalone operational launchers (sealed runtime bytes unchanged):

- `tmp/launch_c1_parallel_finalize_20260912_v2.sh`, SHA-256
  `2e55e3d501839f0f7ec21f6bbc33edbc8418c4c4ec7834881c8c839332617631`.
- `tmp/launch_c1_parallel_audit_20260912_v2.sh`, SHA-256
  `cc59a69e1b7fe50fc9e2e0dd2ff6d5be2c458657e59d6b71347aad3f43c9489c`.

Both passed Linux `bash -n` and local/remote hash equality. Logs and normalized
wrapper exit markers use `tmp/c1_parallel_finalize_20260912_v2.{log,exit}` and
`tmp/c1_parallel_audit_20260912_v2.{log,exit}`. They are not inferred legacy
process exit records. The 21-test Linux unittest suite passed again in 2.359 s;
no production formula was solved. An initial pytest command ran no tests
because pytest is absent; no dependency was installed or environment changed.

A matching local final snapshot is retained in
`tmp/c1_parallel_final_20260912/cardinality_c1_resolved_final.json`. Detailed
continuation instructions are in the task's
`research/final-acceptance-checkpoint-20260912.md`. The existing two-hour
heartbeat was found paused and restored to ACTIVE. It must monitor the
already-started auditor, not start a duplicate or repeat finalization.

All earlier failed finite-v1 and first-parallel-generation provenance remains
as recorded above. Until accepted effective 10/10 evidence exists, C1 stays
OPEN and no new `N<=34` claim is published. No commit or archive was performed.

## Accepted C1 publication (2026-09-13)

The already-running one-shot auditor completed and published
`campaign_acceptance_audit.json` at 09:57:33 UTC+8. Its wrapper recorded exactly
`0\n`, its log agrees with the receipt's actual bytes, and the auditor has
exited. No controller error or global stop was recorded.

| Publication artifact in the parallel v2 root | Bytes | Serialized SHA-256 |
|---|---:|---|
| `protocol_seal.json` | 8,340 | `4dae075cb5f56febdddf2554ed83ee03dec556e8dc26d2f15555b6d05ce8467b` |
| `cardinality_c1_resolved_final.json` | 53,489 | `213e7415ebd7eee184679ee45826772dec5ad166c83f47c6033707484dbc182d` |
| `campaign_acceptance_audit.json` | 4,213 | `cd362ea5385aca6218c099bf6237a934d6b9beb48c98923be0cf09562f670fd3` |

The exact accepted status is
`ACCEPTED_PARALLEL_TASKSET_FRESH_CHECKERS_BYTE_EQUAL`, with
`campaign_status=C1_VERIFIED_UNSAT`, ten `VERIFIED_UNSAT`, zero `UNKNOWN`,
zero `COUNTEREXAMPLE`, `fresh_checker_replay_count=5`,
`fresh_finalization_byte_equal=true`, `c1_proved=true`, and
`certified_upper_bound=34`. The five fresh checks are e6-e10; e1-e5 retain
their accepted finite-v2 provenance. This does not claim ten fresh checker
invocations in the final audit.

Read-only revalidation checked the exact final and receipt bytes, source
anchors, frozen inventories, unique task ownership and bound proof/checker
artifacts. Neither publication stage nor any production solve/check was
repeated for that inspection. The pre-audit final remains immutable, including
its `PENDING_INDEPENDENT_AUDIT` and `c1_proved=false` fields; the separate
accepted receipt discharges its outstanding publication gate.

All ten strict classes A[1,e], e=1,...,10, are therefore empty under the
documented CNF/mathematical-object equivalence. This proves
`e(X)>=1 => m(X)>=1` for `X` in the defined target-free signotope domain.
For `e=0`, `N=25-m<=25`; for `e>=1`, `N=25+e-m<=34`.
Neither `m>=e` nor `N<=25` follows from this C1 result alone.

Six byte-identical lightweight evidence files and their hash inventory are
retained in the task's
[accepted evidence snapshot](../.trellis/tasks/09-03-35-state-cardinality-charging/research/evidence/c1-accepted-20260913/README.md).
Large proofs/CNFs remain on the authoritative server. The unchanged focused
Linux unittest suite passed 21 tests in 2.520 seconds on September 13; its
synthetic SAT/ERROR fixtures are not production results.

The failed timeout-resolution v1, finite v2, retired original serial v3 and
failed first parallel generation remain preserved. No C2, N26-spine, Qlt,
Qeq/Qgt, Hall, marked-position, Agt1, qv21 or triple-only work was run for this
publication summary. No commit or archive was performed.
