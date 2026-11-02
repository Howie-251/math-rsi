# Fresh internal-double source review

Date: 2026-10-13. Verdict: **no blocking source issue found**.
This is a fresh Codex same-family provisional source review under the
project's experiment-bridge adaptation. It does not relabel the earlier
mathematical delta reviews, provide external acceptance, or attest a run.

Reviewed the stable `computations/dd82/n61/internal_double_full61_run/encode.py`,
`SCOPE.md`, and root-owned `runner.py`; read the full graph design and the
additional two-shared-parent port note. Reused generic helper definitions
were inspected only where they serve this implementation. No source edits,
target preparation, solver, certificate check, or external call were made
by this reviewer. Root owns the single source sanity and bounded runs.

## Source findings

- `layout` (encode.py:59) implements all three specified types and the
  attachment normalization. The shared attachment is assigned only in the
  first neutral class for h=1. For r>0 the only matching normalization is
  from the single reference class T[0] to the other seven ordinary classes.
  The 175 fixed pairs contain 35 edges; no second reference or selected
  cross-class matching is introduced. The asserted free-A counts are
  1086/870/800. Core pairs, including nonedges, form an explicit fixed map.
- The fixed zeros match the design: ordinary same-class pairs, exceptional
  avoidance of shared-parent classes, the shared attachment's eight
  attachment nonneighbors, and P/Q independence only in beta=1. Core and
  reference vertices have their complete fixed degree-eight rows checked.
  Every other ordinary vertex has seven exact color degrees; every
  exceptional vertex has an exact total-degree-eight counter.
- Constant folding (encode.py:172) distinguishes Python Boolean constants
  from integer literals. Counters retain repeated literals and subtract
  the number of true constants. `exact_count` asserts adjacent exact
  thresholds, and `defect_count` enforces 0<=B<=2 while returning exactly
  [B>=1] and [B>=2]. Negative/oversized threshold requests return the
  appropriate constants. Empty asserted clauses remain contradictions.
  The reused unary recurrence and actual-AND helper are bidirectional.
- The short counters are formulas for this same A. T/Z counters cover all
  exceptional vertices, and endpoint/Z counters explicitly cover all 50
  vertices, including ordinary ones (encode.py:331). Ordinary T/Z entries
  are zero under their encoded color rules. The row/column budgets use
  these exact bits. The r2 addition sets precisely the 39 entries outside
  each proved eleven-point endpoint domain to zero; it adds no port
  subbranch or selected P/Q matching.
- The original-pair loop visits every one of the 1830 unordered pairs.
  A skipped coverage clause has a real fixed edge or fixed two-edge path.
  All other paths use original edge literals and full AND equivalences;
  every coverage obligation remains present. The common attachment's 49
  other Z pairs get exact mu+A=1 counts using the same path lists, even
  when their coverage clause is already a tautology (encode.py:368).
- Preparation constructs a full deterministic adjacency independently of
  the emitted auxiliary definitions, compares each declared constraint
  against its original degree/common-neighbor semantics, checks the
  threshold bits, and rereads the emitted DIMACS. For this deliberately
  invalid assignment, budget/domain comparisons correctly use the two
  threshold bits' clipped weight. Separate bound constraints ensure that
  every satisfying assignment uses the actual B weight. The receipt
  explicitly says this assignment is not a target witness.
- The generic decoder is reused with the correct case directory and
  encoding/map fields. It checks the complete saved assignment against
  every CNF clause, restores fixed and free pairs across all 61 vertices,
  and writes 244 edges pending independent BFS. It does not decode only a
  quotient or Z subgraph.

## Bounded runner and result scope

The runner imports only the prior generic process limiter and does not
invoke its historical main. One saved case gets at most one solver launch,
with 60 CPU seconds, 90 wall seconds, 4 GiB address-space limit, 512 MiB per
output file, and solver soft limit 58 seconds. On SAT, decode and independent
BFS may add 20 CPU/30 wall seconds. The separate certificate check has its
own 90 CPU/120 wall budget.

UNKNOWN, interruption, output limits, and process failures do not produce
an exclusion. SAT becomes a verified target only after full model checking
and independent order/degree/edge-count/diameter checks. RAW_UNSAT remains
unaccepted until the exact saved input/proof check succeeds; even a checked
case is not an order-61 exclusion. All three checked contradictions and the
separate complete mathematical reduction are needed to exclude internal
double-path vertices. Other order-61 structures remain outside that result.

## Handoff

No blocking or nonblocking code defect was found. During handoff, root
reported that the single tiny sanity passed (96 instances, 3060 Boolean
assignments), and all three preparations passed the emitted same-A semantic
sanity. Root reported variable/clause counts 53046/163721, 33296/103603,
27886/86591 in case order, with the expected primary counts and 78 r2
domain-zero pairs. The three bounded profiles have started. These are
root-reported execution facts, not checks repeated by this reviewer;
their authoritative evidence belongs to the run artifacts. No graph or
internal-double exclusion follows from this source review.

## REUSED source delta: appended final port consequences

Date: 2026-10-13. **No blocking or nonblocking source issue found in this
delta.** The baseline review above is reused, not repeated or relabeled.
This remains a same-family provisional source review, separate from the
mathematical acceptance of universal h=0 and the final port consequences.

Reviewed only `refined/encode.py`, `refined/runner.py`, `refined/SCOPE.md`
under the same run directory and read
`proofs/dd82/n61/INTERNAL_DOUBLE_FINAL_PORT_CONSEQUENCES.md`.

- The r1 delta selects the second exact threshold from each existing
  `all_Z_endpoint_actual_B_bounds` record precisely when that vertex's
  parent lies outside U or W. It covers 33 positions per endpoint, hence
  66 pre-simplification conditions. Boolean false folds away, Boolean true
  produces an empty contradiction, and an integer threshold produces its
  negative unit. The stored input's nonconstant case is the intended
  66-unit extension. The dependency on universal h=0 is recorded explicitly.
- The r2 delta selects the first exact threshold in the existing eleven
  point domains and uses the proved ordered allowed pairs
  `(q0,p0)`, `O_c x O_d`, and `O_d x O_c`. These are disjoint and contain
  51 pairs. The other 70 pairs receive precisely `-B1(u,x) or -B1(w,y)`.
  No new port, matching, branch, or variable is selected. Checking the
  121 single-port choices during preparation is sufficient here because
  the inherited exact endpoint budgets already enforce one unit port each.
- The map is taken from all 100 saved endpoint/Z records, whose exact
  endpoint/vertex coverage is asserted. Existing variable IDs are used
  directly, r2 verifies its 22 distinct nonconstant first-threshold bits,
  and all emitted literals must reference the parent variable range.
  No allocator or baseline model builder is called.
- `append_and_compare` changes only the DIMACS clause-count header,
  copies every baseline body byte, and appends the new clauses. Its
  reread compares the entire old body prefix, each appended clause line,
  and final EOF. The original variable count is unchanged; clause IDs
  in delta records are correctly offset by the parent clause count.
- Output is confined to the separate `refined/<case>/` directory.
  Parent inputs, maps, source, and results are read-only. The unchanged
  edge map is copied for complete decoding. Metadata distinguishes
  inherited baseline semantics from the new Boolean checks and retains
  the mathematical dependencies.
- The refined runner changes only HERE and the two permitted case names.
  The parent decoder's HERE override propagates to the generic decoder,
  so model checking and candidate output use the full refined CNF and
  refined edge map. The already reviewed one-shot limits, independent
  BFS requirement, and separate exact-input certificate handling remain.

No sanity, preparation, solver, or certificate check was run by this
reviewer for the delta. The source is ready for the planned root-run
preparation and one profile of each changed input. The two prior UNKNOWN
results are not exclusions; this review proves no new graph or exclusion.
