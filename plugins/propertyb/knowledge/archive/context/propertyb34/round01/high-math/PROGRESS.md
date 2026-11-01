# T34 round01 high-vertex mathematics

## Latest status — 2026-10-13 15:06 UTC

**This worker's assigned mathematics is now closed at paper-candidate level:**
24 vertices, 25 vertices, and the newly assigned 23-vertex r=3 branch.

- 24: `CANDIDATE_TWENTYFOUR_COMPLETE.md` and
  `FULL24_MATCHING_COVERAGE_AUDIT.json`.
- 25: `CANDIDATE_TWENTYFIVE.md` and `FULL25_COVERAGE_AUDIT.json`.
- 23, exactly three six-degree points: `CANDIDATE_THREE_LOW_23.md` and
  `V23_THREE_LOW_COVERAGE_AUDIT.json`. Four common-unit highs including two
  actual sevens leave ten final local profiles, all strict; all four stage
  inventories and 139 exact joint certificates were replayed.
- The 24-point temporary-negative-empty coverage question is explicitly
  resolved in `SEVEN_TEMPORARY_NEGATIVE_AUDIT.json`: 56 temporary negative
  promotions produce 207 rescued actual orbits after degree lowering; every
  one is present in both the complete catalogue and bound table. The generator
  correctly postpones its sign check, so no numerical certificate changed.

Root has received all entry paths and owns Grok/Gemini review, wiki and Lean.
No end-to-end T34 or new formal theorem is claimed by this worker.

## Latest status — 2026-10-13 14:50 UTC

**24 and 25 vertices now both have complete paper candidates.** The new
`CANDIDATE_TWENTYFOUR_COMPLETE.md` closes r=1..4 through the eight-lock matching
selection and complete 16,006 seven-lock domain. Of 375 mixed seven-lock
residues, all actual eighth-low extensions are handled: 22,615 strict deletion
projections, 220 direct eight-lock witnesses, and two exact joint duals. The
q=0 eighth-lock domain is also complete, with 881 direct witnesses and one
four-layout dual. `FULL24_MATCHING_COVERAGE_AUDIT.json` has all_covered=true;
all actual profile/projection bindings and all six new duals were checked.

Root owns cross-family review and Lean. No end-to-end T34 theorem is claimed.
At root's request this worker now turns to **23 vertices, exactly three
degree-six points**, continuing in this directory. Earlier status below is
historical; the r=1..4 mathematical gap at 24 vertices is no longer open.

## Latest status — 2026-10-13 14:20 UTC

- **25 vertices, full paper candidate:** `CANDIDATE_TWENTYFIVE.md`. Complete
  nine-lock catalogues cover q=5,8,9 low locks; q=5 has 11,692 strict colored
  types. Every q=8/9 residue admits an actual tenth lock and all extensions are
  strict. `FULL25_COVERAGE_AUDIT.json` independently reconstructs the complete
  classifications, color assignments, projections and witness binding.
- **24 vertices, r=5 complete paper candidate:** `CANDIDATE_FIVE_LOW_FULL.md`.
  Nonunit low matchings close with one/two usable high locks. With unit lows,
  every nonunit high pair closes; four unit highs then invoke the conditional
  `NINE_LOCK_UNIVERSAL_LEMMA.md`, which holds on at most 25 vertices.
- With the completed r>=6 candidates and earlier r=0 candidate, this worker's
  remaining mathematical branches are **24 vertices, r=1..4**.
- Root owns model reviews and Lean. These are paper candidates and exact local
  witnesses, not a claim that T34 or its main Lean theorem is complete.
- Current next route: a weighted three-coloring of all degree-six/seven points
  gives a codegree-two matching in each color class. For r<=3 at least 19 such
  points exist, hence seven locks can be selected. Their local domain is being
  investigated. Six all-seven matching locks remain insufficient: 34 and 41
  orbits with two/three matching edges are non-strict after current joint LP.

The sections below are chronological earlier records; this latest status
supersedes their old open-branch counts.

Active continuation of the authorized long-term Goal. Old one-hour cutoff no
longer applies. New files stay in this directory; no Lean, wiki, or old evidence
has been modified by this worker.

## New complete paper results

- **24 vertices, at least seven degree-six vertices:** the two formerly missing
  seven-low trace types now have finite rational layout mixtures strictly below
  one. Full actual coverage and the fixed-slot averaging argument are in
  `CANDIDATE_SEVEN_LOW.md`. The two certificates and independent injection replay
  are `SEVEN_MIXTURE.json` and `SEVEN_MIXTURE_INDEPENDENT.json`. Root owns Grok /
  Gemini review status; no Lean completion is claimed.
- **25 vertices, the affine nine-lock family:** all q=5..9 versions selected by
  the old universal nine-lock lemma can be handled. The formerly failing q=8/9
  cases admit an actual tenth lock and all its local extensions are strict.
  `V25_AFFINE_OBSTRUCTION.md` gives selection and complete extension coverage;
  the 24 / 28 / 16 witnesses are independently checked. General nine-lock
  classification remains open.

## Useful implementation

`subset_position_dp.py` implements one exact DP over `(position, placed-label
subset)`, optimizing all lock orders and all positions simultaneously. A
subset-zeta table aggregates the type rows. Coefficients are integer multiples
of `1/(v-s)!`; ordinary Fraction and independent stub/injection rows replay every
retained result. Nine locks take about 0.25 seconds per input here.

The initial verification wrapper misread `multilock.rows()['C']` as corrected.
The mathematical DP was unaffected. All 204 previous witnesses happened to have
zero deductions; after correction every one was replayed, then five separate
nonzero-deduction single-lock inputs were also checked. Full correction and
replay evidence: `SUBSET_DP_REPLAY_CORRECTION.json`.

## 24 vertices, exactly six low vertices: complete new paper candidate

At least ten seven-degree vertices exist. Remove the at most six exceptional
partners of the lows: at least four seven-degree vertices remain, all unit with
every low. Each has total codegree excess five.

For the four unresolved six-low unit profiles, a first such high gives a
complete 131-input local extension domain. The exact position DP plus shared
actual bad-vector dual certificates leave five orbits. Seventeen new strict
dual certificates independently replay in `SIX_EXTENSION_JOINT_INDEPENDENT.json`.

Adding a second high with mutual codegree one or two, and requiring its separate
seven-lock projection to remain bad, gives a complete smaller domain. Every
codegree-two case is strict. The Pasch six-low type is also completely handled
in this domain. Twelve labelled codegree-one cases remain under the current
bound. Raw coverage and certificates are `SIX_LOW_TWO_HIGH.json` and
`SIX_TWO_HIGH_JOINT.json` (the latter remain >=1 and are diagnostic, not proofs).

All codegree-three/four cases also passed. Codegree at least five is already
strict on the two high locks alone. In a counterexample all usable highs must
therefore be pairwise unit. The twelve residual labels have four orbits, and
their pair restrictions cannot hold for three highs: the proof ends with short
analytic A/B and singleton-edge pigeonhole arguments. A separate complete
172-extension check confirms zero residues. The new proof is
`CANDIDATE_SIX_LOW.md`; generator/projection binding replay is
`SIX_LOW_COVERAGE_AUDIT.json` (all bindings pass). Root owns cross-family review
and Lean implementation. Combined with the seven-low result, all r>=6 cases now
have paper candidates; r=1..5 remain open.

## Smaller low counts

`MIXED_SIX_JOINT.json` applies the new shared-vector dual method to the old local
domains for one through five lows. Successful local certificates are verified
in `MIXED_SIX_JOINT_INDEPENDENT.json`. Several cases improve, but no entire new
low-count branch has yet closed. The table is a diagnostic / reusable evidence
pool; it is not a claim that all original 24-vertex hypergraphs are covered.

## Next obligations

1. Root is reviewing the complete six-low candidate and its exact evidence.
2. A bounded 180-second pilot constructs complete unit-lock clique
   decompositions through nine vertices by vertex extension and exact invariant
   canonicalization. This addresses the actual missing 25-point coverage; it
   must not be mistaken for a proof until actual degree profiles and probability
   bounds are attached.
3. Continue one-through-five-low 24-point structures according to the first
   universal-classification pilot's measured size and residuals.
