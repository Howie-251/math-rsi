# q=8 actual branch: complete source, ordinary checks pending

The intended declaration is
`Aris4Math.ThirtyFour.TwentyFiveEightLowComplete.propertyB`.
It consumes a 34-edge actual hypergraph and the actual `MixedLocks H 8 2`
selection, and returns its Property B coloring. No local table or probability
premise appears at that final interface. The full source chain is written;
**the full chain has not passed its ordinary build**.

Use `Q8_COMPLETE_BUILD_ORDER.json` for 175 serial regular targets, after the
shared Unit9 catalogue chain from q=9 is built. Root owns regular builds.

## Mathematical and representation connections

`TwentyFiveColoredActual.actual` explicitly transports the low-degree set when
an actual lock embedding is normalized by the uncolored catalogue. It applies a
degree-preserving colored permutation and returns both the actual large family
and every true multiplicity. The actual total permutation is retained, so the
original tenth lock can be attached using `LockLiftRelabel.lift`.

`TwentyFiveOneHighTable.low_eq` proves that every eight-element subset of Fin 9
is exactly the complement of a single high vertex. Thus the source set is all
374 uncolored families times all 9 high vertices. No color arrangement is lost.
The saved q=8 representatives cover 1,397 feasible source colorings, reducing to
840 representatives. `Q8_COLORED_CERTIFICATES.json` stores all 3,366 direct rows,
with either an explicit label bijection or a short incident-block contradiction.
Certificate recovery took 2.40 seconds and did not search probability layouts.

`TwentyFiveColoredRows` implements direct retained/degree-rejected/budget-rejected
rows. The budget form checks an exact displayed completion with
`TwentyFiveSparseCompletion`, then contradicts the same `Feasible` predicate
proved for the actual hypergraph. This form is also needed for the 252 q=5
source colorings which pass degree budgets but exceed 34 recovered edges.

## Numerical closure

All 840 saved nine-lock placements were replayed with exact bare A/B/C arithmetic;
all values equal the saved values, and 838 are strict. The only residues are
0 and 10. The 358 previously DP-selected q=5 placements were also replayed:
all their *bare* values are strict and equal the saved values. This concerns
saved placements, not a new layout search; evidence is
`Q8_Q5_SAVED_LAYOUT_BARE_RECHECK.json` (0.39 seconds).

The q=8 numeric generator also checks all 20 tenth-lock saved bare values before
export. It emits 70 nine-lock and 2 tenth-lock numeric modules, at most 12 strict
cases per module. These still require Lean kernel execution. The first actual
q=8 caller, exact value 2841/2860, passed a guarded local probe in 5.96 seconds /
2.57 GiB with the standard three axioms (`eight-low-numeric-pilot-r1.log`).

## The actual tenth lock

For residue 0 there are 29 complete promotion choices: 24 feasible, one degree
contradiction, four total-edge-budget contradictions. For residue 10 there are
193 choices: 101 feasible and 92 degree contradictions. All 222 choices appear
in the row list, including all rejected choices. Feasible entries map to the
20 saved targets using explicit permutations preserving the eight low degrees;
the two high vertices may exchange because no further extension is needed.

The four budget failures cannot be disguised as degree failures. They use
`TwentyFiveConditionalBudgetRows`, with the exact full block list and actual
34-edge budget. A short pilot containing one budget rejection, one degree
rejection and one retained permutation passed in 3.62 seconds / 1.51 GiB,
finite kernel check 0.555 seconds; see `eight-low-tenth-budget-pilot-r1.log`.

## Checked API scope

- `colored-actual-r1.log`: actual low-set/permutation/count bridge, PASS.
- `colored-rows-r1.log`: direct colored-row correctness, PASS; the later
  `direct_sound` addition is included in the budget-row probe below.
- `one-high-table-r1.log`: complete high-vertex coverage and row extraction, PASS.
- `conditional-budget-rows-r1.log`: degree and total-budget final-extension
  correctness, PASS.
- `eight-low-final-frame-r1.log`: final actual MixedLocks-to-coloring assembly
  with classification/numeric/tenth facts as explicit theorem parameters,
  PASS 5.23 seconds / 1.25 GiB, standard three axioms. This validates the API
  connections; it does not supply the unbuilt finite facts.

## Regeneration

1. `generate_q8_colored_certificates.py`
2. `generate_q8_numeric.py`
3. `generate_q8_inventory.py`
4. `generate_q8_classification.py`
5. `generate_q8_tenth.py`

The three final aggregate/caller modules are handwritten/generated once:
`TwentyFiveEightLowNumeric`, `TwentyFiveEightLowTenthComplete`, and
`TwentyFiveEightLowComplete`. The q=9 source chain was not modified while
preparing q=8.
