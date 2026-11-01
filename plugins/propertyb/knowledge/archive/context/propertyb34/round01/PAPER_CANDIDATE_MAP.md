# Complete T34 paper-candidate map

2026-10-13. All mathematical branches now have paper candidates. This is the
entry map for adversarial proof review and subsequent Lean implementation,
not a declaration that the T34 Goal has been accepted or fully formalized.

The original theorem is `FORMAL_SPEC_PROPERTYB_34.md`: for every finite set
V and every simple family E of five-element subsets, |E|<=34 implies an actual
two-coloring with both colors in every edge. There are no structural premises
in that theorem. Its proposed new lower bound is m(5)>=35, not equality.

## Reduction and completed formal base

`formal/Aris4Math/ThirtyFour/Target.lean`, `SmallVertices.lean` and
`Assembly.lean` provide the actual finite-input reduction. The formal work
has already proved <=20 vertices and the 21-point degree-five, degree-six and minimum-eight branches. The
current `Assembly.RemainingGoal` consists of 21-point inputs with minimum
degree exactly seven and all 22–25-point inputs. Those internal inputs are
simple five-uniform, pair-covering, and have exactly 34 edges. This is still
a conditional reduction, not a proof of RemainingGoal.

Additional compiled interfaces: actual eight matching locks at 24 vertices;
permutation transport of actual lock counts; full 21-point four-lock orbit
coverage. See `middle-lean/REPORT.md`. These do not yet close the remaining
whole-vertex branches.

Evidence: `twenty-lean/REPORT.md` and `twentyone-lean/REPORT.md`, actual
build/import logs and source files. The original T32/T33 proofs are frozen.

## Mathematical branch sources

All paths in this table are relative to this directory unless explicitly
root-relative. Read the referenced proofs in full, not this map alone.

| Internal branch | Full mathematical source |
|---|---|
| 19 and 20 | Already connected in Lean; first-hour nineteen/ and low-math/ proofs, and `twenty-lean/EIGHT_SIMPLIFICATION.md` |
| 21, all degrees | `twentyone-math/COMPLETE_TWENTYONE.md` and its full degree-five/six/seven/eight proof sources |
| 22, all degrees | `middle-math/COMPLETE_TWENTYTWO.md`, `CANDIDATE_TWENTYTWO_SEVEN.md`, `CANDIDATE_LOW_BRANCHES.md` |
| 23, no degree-six points | `twentythree-seven-math/N23_MIN_SEVEN.md`, `SELECTION.md` |
| 23, one/two degree-six points | `middle-math/CANDIDATE_ONE_TWO_LOW_23.md` |
| 23, three degree-six points | `high-math/CANDIDATE_THREE_LOW_23.md` |
| 23, four/five degree-six points | `middle-math/CANDIDATE_FOUR_FIVE_LOW_23.md` |
| 23, at least six degree-six points | `middle-math/CANDIDATE_LOW_BRANCHES.md` |
| 24, all degrees | `high-math/CANDIDATE_TWENTYFOUR_COMPLETE.md` and its referenced r=0,5,6,>=7 sources |
| 25, all degrees | `high-math/CANDIDATE_TWENTYFIVE.md`, `NINE_LOCK_UNIVERSAL_LEMMA.md` and its referenced full nine-/ten-lock classification |

Pair coverage forces minimum degree >=6 at 22–25 points and >=5 at 21.
The degree sum is always 170. Thus the listed degree cases cover every actual
internal input. Finite arithmetic files and coverage generators are indexed
inside the individual proof sources.

## Shared probability and counting interfaces

The fixed random-order coloring construction and its actual failure-event
cover are in root-relative `proofs/PROBABILITY_LEMMAS.md` and the completed
formal probability modules. They are reused with freshly checked 34-edge
trace counts, not old 32/33-edge numeric values.

The shared-bad-vector weak-dual derivation is
`middle-math/CANDIDATE_TWENTYTWO_SEVEN.md` §4 and `joint_layout_lp.py`.
The new `formal/Aris4Math/ThirtyFour/MixedLayout{Dual,Counts,Application}.lean`
connects the ordinary avoided-quota interface to actual H. Its five difficult 21-point 67888 actual
numeric callers have compiled and passed independent standard-axiom import. The weighted overlap enhancement in
`middle-math/WEIGHTED_OVERLAP_QUOTA.md` is a diagnostic side lemma; actual
certificate-field checks show it is not used by the completed candidate, so
it is not an additional required Lean interface.

Each certificate fixes actual H and its bad-pair count vector before selecting
one of finitely many layouts. Different layouts have different conditional
probability spaces. Their exact upper bounds can be averaged: an average
below one implies one layout's bound is below one. No common event probability,
independence, minimax interchange or LP strong-duality theorem is assumed.

## Critical coverage checks

Actual selected traces must reach every local table. A strict projection
supplies a coloring of H directly; only non-strict projections are extended.
Trace promotions enumerate actual multiplicities; equal-degree relabelings
transport the lock positions. The local classifiers do not enumerate whole H.

For the 24-point mixed seven-lock catalogue, artificial degree restoration
may produce a temporarily negative empty count. The generator keeps it until
the low degrees are restored, then tests nonnegativity. The 56 such promotions
produce 207 necessary mixed orbits, all present in the final catalogue and
bound table. See `high-math/SEVEN_TEMPORARY_NEGATIVE_AUDIT.json`. An earlier
all-seven nonnegativity filter would be incorrect; the actual generator does
not apply one.

## Remaining acceptance work

Fresh whole-proof adversarial audit and targeted Grok/Gemini reviews are
underway. Individual reviews have finite scopes and do not replace the
complete proof. All 21-point degree>=6 and 22–25 actual callers, complete
local coverage, required quota interfaces, final Main, bare-original-type
and transitive-axiom audits remain to be finished in Lean. The final readable
proof, offline HTML and reproducible handoff follow the audited mathematics.

## First full paper review

Fresh R1 is complete; no substantive mathematical issue found. One stale
weighted-dependency description was corrected without changing mathematics.
See `paper-audit/PROOF_AUDIT.md`; this remains same-family/provisional and
does not replace final Lean assembly or cross-family C review.

## Formal selection update

23-point minimum-six selection, the same actual seventh vertex for low-weight
extensions, and the W=6 selected-vertex saturation are now Lean-checked.
See `twentythree-seven-math/SELECTION_FORMALIZATION.md`. The equality bridge
uses only selected-vertex saturation to produce an actual degree-eight point
unit to all six locks; the stronger global two-K7 theorem and averaging over
all six-subsets are not needed. The old local tables are unchanged. Full
23-point classification/probability assembly remains an open Lean obligation.
