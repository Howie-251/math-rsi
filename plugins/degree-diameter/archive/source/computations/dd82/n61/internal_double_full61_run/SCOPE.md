# Exact internal-double original-graph source

Source implementation only. This file does not attest mathematical or source
review acceptance, prepared inputs, solver results, or certificates. The root
owns those receipts and launches. This is the project experiment-bridge
workflow adapted to the existing mathematical target and bounded CPU tools.

## Target and complete branches

The target is a simple degree-eight, diameter-two graph on 61 vertices with
an internal vertex of the double-defect path forest. The three case names are
`r0_h1_b0`, `r1_h0_b0`, and `r2_h0_b1`. Each is a necessary local type after
the endpoint-adjacency, shared-parent/shared-attachment, and double-shared-
attachment exclusions. The complete coverage and all labeling arguments are
in `proofs/dd82/n61/INTERNAL_DOUBLE_FULL_GRAPH_DESIGN.md`, with its cited
local/followup/exclusion dependencies. A checked contradiction in one case
excludes only that case. Checked contradictions in all three, together with
the reviewed reductions, exclude internal double-path vertices; they do not
exclude every order-61 graph.

Use v=0, u=1, w=2, T=3..10 and Z=11..60. Core and endpoint attachment
incidences are constants. The P/Q attachment labels use parent-category and
within-class permutations with a proved overlap normalization. For r>0 only,
seven reference-to-ordinary five-point matchings are identities. The r=0 case
has no such matching normalization. Primary variables are actual undirected
Z-pair adjacencies, respectively 1086, 870, and 800. Every other original
pair has an explicit Boolean constant, including its nonedges.

## Encoded facts

- Every original vertex has degree eight. Eleven core vertices have their
  complete neighborhoods fixed; preparation checks them. Ordinary points
  have own-color degree zero and each other-color degree one. Exceptional
  points have an explicit exact total-degree counter. The normalized
  reference vertices, when present, also have complete fixed degree eight.
- All 1830 original vertex pairs have a fixed actual witness or an asserted
  direct-edge/actual-two-edge-path coverage clause. Two free-edge paths use
  the full three-clause AND equivalence. Constants are faithfully folded.
- The fixed neighborhoods give the actual defect row B_v=2e_u+2e_w,
  B_uw=beta, the stated B[T] and B[T,u]=B[T,w]=0. Preparation directly checks
  those identities. B always means A²+A−7I−J of this same graph.
- Small T/Z defect counters cover the exceptional points; ordinary T/Z
  defects are already zero by the color degrees. Endpoint/Z counters cover
  **all fifty** Z vertices. Each counter's two threshold bits are equivalent
  to its actual original-A count, with bounds 0<=B<=2. T-row, exceptional
  T-column and endpoint-row port budgets use exactly these bits.
- The shared attachment in r0_h1_b0 has B_s,z=0 for all other 49 points of Z.
  These are exact mu(s,z)+A_s,z=1 counters using the same actual path lists.
- In r2_h0_b1, `INTERNAL_DOUBLE_SHARED_TWO_PORTS.md` restricts the endpoint
  unit ports. The u port is in {q0} union O_c union O_d, and the w port in
  {p0} union O_c union O_d. Each set has eleven vertices. The other 39
  entries per endpoint are set to zero through their already exact B bits.
  No extra port subcases or selected P/Q matching are imposed.

Generic all-Z-pair B upper counters, global B connectedness constraints,
additional path-forest conditions, and triangle-free assumptions are not
encoded. These omissions do not relax the required original degree/diameter
target. A satisfying graph is still an actual full target; the inherited
facts merely supply sound additional constraints and normalizations.

## Source interface and sanity

```
python encode.py sanity
python encode.py prepare --case r0_h1_b0
python encode.py decode --case r0_h1_b0
```

The other two case names use the same interface. `sanity` only exercises the
new short-B constant-folding glue exhaustively on tiny Boolean inputs and
checks the finite label maps. It generates no target input and calls no
solver. It does not rerun older generic or boundary sanity suites.

`prepare` writes the selected case subdirectory and refuses to overwrite a
prepared input. It produces the complete target `input.cnf`, original edge
mapping, fixed-constant reasons, all-pair coverage/path records, constraints,
normalization, an assignment sanity receipt, and `encoding.json` with status
`PREPARED_NOT_RUN`. There is no relaxed target input.

Preparation independently constructs a deterministic full original graph
from one assignment, evaluates all original degrees and common-neighbor
counts, and extends every emitted auxiliary through the actual defining
clauses. No auxiliary definition may fail. Every asserted family must agree
with its independently recomputed graph semantics; the saved DIMACS is then
read afresh and every actual clause evaluated. That graph is deliberately
not asserted to be a satisfying witness. For invalid assignments, the two
defect bits sum to min(2,max(0,B)); this is the explicit semantic comparator
for bit budgets and bit-domain zeros. Separate bounds are also checked, so
in every satisfying model those weights equal the actual B exactly.

`decode` reuses the existing generic full-DIMACS assignment check and restores
every fixed/free original edge. It writes `candidate.json` and the full edge
list with status pending independent BFS. The root-owned runner must perform
that independent check, and must keep raw UNSAT separate from an exact-input
LRAT certificate check. No runner, solver invocation, restart policy, or
resource-limit change is introduced by this encoder.

Only generic definitions are imported from the historical CNF helper through
the existing joint-boundary support module. No historical encoder instance,
old main, adjacent-double case condition, or boundary fixed-mask constructor
is reused. The source includes no external call or hash generation.
