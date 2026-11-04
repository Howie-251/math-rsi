# Qeq position-marked ordinary-state campaign (2026-09-02--03)

## Scope and frozen inputs

This campaign asks whether positional information around the first-to-next
transition

\[
P(v,w)=\{v=\text{first }E411/(6<5),\quad
w=\text{next }E421/(6<5)\}
\]

can name a branch-dependent fixed singleton second globally missing ordinary
state besides `G410` on the two accepted exact `Qeq` partitions
`(q_v,q_w,w-v)=(1,1,1)` and `(1,1,2)`.  The accepted Qeq/Qgt matrix, Qgt
singleton and Hall evidence, and Qlt-through-`qv20` envelopes are read-only
inputs and are not rerun.  `qv21`, monolithic `Agt1`, and triple-only are
prohibited or out of scope rather than sealed inputs, and are not invoked.

The source is the accepted set of nine distinct complete assignments: five in
`(k,d)=(1,1)` and four in `(1,2)`.  Every record is re-decoded from the frozen
matrix output and checked against the exact gate and an independently rebuilt
strict-N25 profile before its positional data are used.

## Position vocabulary and the counting theorem

For an ordinary base state `G`, define

\[
L_G=[\exists u<v:S(u)=G],\qquad
I_G=[\exists v<u<w:S(u)=G],\qquad
R_G=[\exists u>w:S(u)=G].
\]

Strict-N25 state injection and the exceptional states at `v,w` make these
three predicates mutually exclusive and give

\[
O[G]\iff L_G\lor I_G\lor R_G.
\]

Hence a present `G` makes exactly two of its three region marks false, while a
globally absent `G` makes all three false.  Summing over the 25 ordinary-state
fibres gives the exact identity

\[
\#\{\text{false atomic region marks}\}
=50+\#\{G:\neg O[G]\}.
\]

The constant 50 is a structural baseline and has no charging capacity.  The
only count-eligible excess in a `G` fibre is the simultaneous failure of
`L_G,I_G,R_G`, which is exactly the original global resource `not O[G]`.
Prefix/suffix, first/last, and endpoint-neighbour marks are therefore
diagnostics or antecedent refinements, not additional resources: under state
injection first and last coincide when `G` occurs (and are both undefined when
it does not), while the prefix/suffix predicates are just unions of
`L_G,I_G,R_G`.

This yields the legal form of every candidate tested below:

\[
H_{k,d}\land C_{F=x}\Longrightarrow \neg O[G],\qquad G\ne G410,
\]

where the marked predicate `C` occurs only in the antecedent and the conclusion
is global and unmarked.  A local zero such as `not I_G` is never scheduled as a
solver cell.

## Context families

The v1 registry fixes three categorical families before inspecting occupancy:

1. `left_anchor`: the ordinary state at `v-1`;
2. `open_gap_trace`: `EMPTY` for `d=1`, or the single ordinary state at
   `v+1=w-1` for `d=2`;
3. `right_anchor`: the state at `w+1`, with a separate `BOUNDARY` value.

The families are tested separately.  They are not mutually exclusive with one
another, so successful edges from different families cannot be spliced into
one exhaustive partition theorem.  To close an exact partition with a
branchwise singleton rule, every declared branch of one selected family must
either be verified infeasible or be audited realizable and receive a global
second singleton charge.  A Cartesian signature is a possible later
refinement, not part of the sealed v1 screen.

For consecutive exceptional endpoints, the first endpoint owns the first
slot and every later endpoint owns its unique incoming transition edge.  This
controls reuse on the exceptional side only.  On the ordinary side, every
marked rule projects to its base `G`; any future Hall test must be performed
after that projection, so multiple marks of the same `G` cannot inflate the
neighbourhood.

## Accepted nine-model empirical census

The server-side v3 replay was accepted with nine distinct assignments and no
solver, proof producer, checker, or Hall invocation.  The registry contains
425 positive diagnostic marks and 25 count-resource fibres.

| exact partition | retained models | raw observed | raw structural zero | raw empirical zero | distinct empirical-zero predicates |
| --- | ---: | ---: | ---: | ---: | ---: |
| `(1,1)` | 5 | 154 | 125 | 146 | 62 |
| `(1,2)` | 4 | 163 | 0 | 262 | 108 |

The raw zeros above are diagnostic.  After requiring an observed context
branch and a globally absent secondary state in every retained support model,
135 legal SAT candidates remain.  This number is a discovery-obligation count,
not a count of proved charges.

The observed branch distribution is:

| partition/family | observed branches | legal candidates |
| --- | ---: | ---: |
| `d=1`, left anchor | 5 | 41 |
| `d=1`, open gap (`EMPTY`) | 1 | 0 |
| `d=1`, right anchor | 4 | 30 |
| `d=2`, left anchor | 4 | 32 |
| `d=2`, open-gap state | 3 | 22 |
| `d=2`, right anchor | 2 | 10 |

In particular, the five accepted `d=1` models collectively occupy every
secondary state on the `EMPTY` branch.  Thus the coarse open-gap family cannot
supply a second fixed global charge for `d=1`.

## SAT-first policy

The first wave contains exactly the 11 candidates supported by at least two
retained models:

- `d=2`, `right_anchor=G331`: targets `G330,G310` (support 3);
- `d=1`, `right_anchor=G332`: targets `G322,G430,G311,G420` (support 2);
- `d=2`, `open_gap_trace=G321`: targets
  `G320,G430,G330,G310,G420` (support 2).

Before any cell solve, one retained complete assignment for each of the three
branches must pass a full branch-formula and independent semantic replay.  The
cell formula is the exact gate, followed by selector-conditioned context
clauses, followed by the single positive global occupancy unit `O[G]`; it adds
no variable.  A short external Kissat run is used only to seek counterexamples.
An accepted SAT result eliminates the candidate.  A timeout is `UNKNOWN`, and
a raw solver return of UNSAT is only a persistent-zero signal; it is not a
theorem until a separate AE proof, independent checker, and finalizer all pass.

Hall remains frozen throughout this screen.

## Current logical stopping rule

- If every realizable branch of one exhaustive family has a verified second
  global charge distinct from `G410`, proceed to reuse control and a separate
  projected two-slot Hall campaign.
- If an accepted realizable branch admits every secondary `G`, that family is
  insufficient for a branchwise forced-singleton rule and is abandoned without
  testing its remaining branches.
- If all three v1 families fail this singleton test, the next options include a
  predeclared joint signature, a separately justified set-valued neighborhood,
  or a stronger ordinary resource system; local zeros remain non-charges.
- No three-event/three-slot Hall work begins before the two-event conditions
  above are met.

## SAT-first results (2026-09-03)

The support-at-least-two P0 campaign first audited all seven retained
branch-support rows across three branch gates.  All eleven empirical-zero candidates
then produced complete SAT assignments and passed an independent exact-gate,
position-context, global-occupancy, and strict-N25 profile replay.  There were
no persistent zeros and no unknowns:

| P0 branch | empirical zeroes tested | audited SAT | persistent/unknown |
| --- | ---: | ---: | ---: |
| `d=2, right_anchor=G331` | 2 | 2 | 0 / 0 |
| `d=1, right_anchor=G332` | 4 | 4 | 0 / 0 |
| `d=2, open_gap_trace=G321` | 5 | 5 | 0 / 0 |

Before the P0 terminal result was read, the next obstruction probe was fixed
as the smallest empirical-zero `left_anchor` branch in each exact partition.
Both retained branch witnesses passed the nonvacuity replay.  All twelve P1
candidates were again audited SAT:

| P1 branch | empirical zeroes tested | audited SAT | persistent/unknown |
| --- | ---: | ---: | ---: |
| `d=1, left_anchor=G331` | 6 | 6 | 0 / 0 |
| `d=2, left_anchor=G311` | 6 | 6 | 0 / 0 |

Across P0 and P1 there were 23 external SAT calls, 23 audited counterexamples,
zero proof-producer calls, zero checker calls, and zero Hall calls.  The sum of
solver wall times recorded in the case receipts was 159.626 seconds; the
largest single solve was 24.185 seconds.  The longer campaign wall time came
from rebuilding and independently checking complete strict-N25 assignments.

## Forced-singleton obstruction certificate

For each probe branch, combine the states already occupied by its retained
models with the targets realized by its audited SAT counterexamples.  The
result is the complete 24-state secondary universe
`{G : G != G410}`:

| exact branch | retained support | occupied in retained models | zero targets refuted by SAT | combined secondary states |
| --- | ---: | ---: | ---: | ---: |
| `d=1, open_gap_trace=EMPTY` | 5 | 24 | 0 | 24 |
| `d=1, right_anchor=G332` | 2 | 20 | 4 | 24 |
| `d=1, left_anchor=G331` | 1 | 18 | 6 | 24 |
| `d=2, open_gap_trace=G321` | 2 | 19 | 5 | 24 |
| `d=2, right_anchor=G331` | 3 | 22 | 2 | 24 |
| `d=2, left_anchor=G311` | 1 | 18 | 6 | 24 |

The exact quantified conclusion for each table row is

\[
\forall G\ne G410\;\exists X_G:\quad
X_G\models H_{1,d}\land C_{F=x}\land O[G].
\]

The witnesses `X_G` may be different; the table does not assert that one model
contains all 24 secondary states.  Thus each of the three separately tested
categorical families has a realizable branch, in each relevant exact
partition, on which no named `G != G410` is uniformly absent.  No family can
define a branch-dependent, forced singleton second base state.  This is a
precise obstruction for singleton charges in the sealed v1 **single-coordinate
non-Cartesian** context families; it is not a claim that every positional or
set-valued refinement is impossible.

The same state-injection premise used in the position theorem already implies
that two exceptional endpoints leave at most 23 occupied ordinary states, so
at least two ordinary states are missing.  With `G410` known missing, some
second `G != G410` therefore exists in every model.  What fails here is the
stronger attempt to name one fixed `G` from a single context coordinate in a
way suitable for a controlled singleton charging map.

The stopping classification is
`SINGLETON_CHARGE_OBSTRUCTION_FOR_V1_SINGLE_COORDINATE_FAMILIES`.  No
branchwise forced singleton second charge `G != G410` was obtained.  Since
there was no persistent zero, AE proof production is unnecessary; under the
stated stopping rule the two-event and three-event Hall campaigns remain
frozen and no set-valued Hall mask was tested.  A future campaign may
predeclare a joint signature such as
`(left_anchor, open_gap_trace, right_anchor)`, test a separately justified
set-valued missingness relation, or change the global resource
system/invariant.  Prefix/suffix and first/last aliases alone do not add
independent counting capacity, although they may refine a future joint
antecedent.

## Evidence locations and anchors

- P0 server root:
  `/data/ktqiu_hdd/math_agent/res/state_charging/20260903_qeq_position_context_satfirst_p0_v1`;
  seal-file SHA-256 `4122a8ad3084b655a8149aa999617f62c8ee555c76110697798b812bd7d3c2ba`;
  summary-file SHA-256 `fd29300f87834d447038ae03eac98b8f6e3bef24e6f11fd389ff45ae441f7afe`.
- P1 server root:
  `/data/ktqiu_hdd/math_agent/res/state_charging/20260903_qeq_position_context_satfirst_p1_left_min_v1`;
  seal-file SHA-256 `83d032a680c25e8bef159124143e5c7ad09f78dc276309debf27538c0b4fe77a`;
  summary-file SHA-256 `39bad64c98a65c4f5e1ccdb671ebc12d91fe4f4c844e581a213bef260aef3bec`.
- Accepted solver-free obstruction finalizer root:
  `/data/ktqiu_hdd/math_agent/res/state_charging/20260903_qeq_position_context_singleton_obstruction_final_v3`;
  local mirror
  `tmp/20260903_qeq_position_context_singleton_obstruction_final_v3`.
  Its `campaign_final.json` has serialized file SHA-256
  `07c3fdb552e50c636bcf01269236f2339ad45e4a89bbeab3cef26dcb9b5e997e`
  and semantic `final_sha256`
  `56e9340f20affed0f5317713064318bb3f1de47e50208653b64d446a91297229`.
  Its `campaign_acceptance_audit.json` has serialized file SHA-256
  `f2ecd71f20a5dd9ffc70e6e96555a9c9fd56db5ff7571695e66f82b498a45b57`
  and semantic `audit_sha256`
  `0c675b82771d87334aea112675a7b1c461830d90c07130194dacac1ec149ed04`.
  The accepted receipt binds all six complete probe branches and all 23 static
  SAT audits to the singleton-only obstruction class above.  The finalizer
  itself invoked no solver, proof producer, checker, model re-decoder, or Hall
  routine; `hall_status=FROZEN` and `hall_tested=false`.
- The finalizer runtime SHA-256 is
  `e9ebc662bce9b5b15918a27d04d2c4f0039fffa8b4e907a67bddfaf07fa5f165`;
  the v3 launcher SHA-256 is
  `4385cdca3edfc1c2c8b5b87e7d2d99c90fd8395a5319275631a2db4fe23b0cd9`.
- Local light archives omit only the large CNF byte files; manifests retain
  their server paths, sizes, and hashes.  Archive SHA-256 values are
  `893bc80e16c73a8b054188b9d0eec3e26ab0144b917cd33d1ac0d04deff7fd3b`
  (P0) and
  `61ffac8fe108e7bf1bcf24c1a4838e2a97bcb5ef87a6805d648f5f12c3cfa610`
  (P1).
