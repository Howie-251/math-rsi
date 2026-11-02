# Order61 targets have no actual defect entry three

## Statement and scope

Let G be any finite simple undirected graph on61 vertices, with maximum
degree at most8 and diameter at most2. Let A be its actual adjacency
matrix. Then the actual defect matrix

`B=A²+A−7I−J`

has entries in {0,1,2}. Its positive support is connected by the inherited
connected-defect theorem. This is a structural theorem about every such
original graph, not an exclusion of order61. General58–61 remains open,
with no new graph above57 and no changed bound57≤N(8,2)≤61.

This is a computer-assisted mathematical proof, modulo the explicitly
reviewed finite-enumeration imports of the inherited connectedness theorem,
and the actual checked CNF certificate below. It is not a Lean theorem.
Final same-thread Gemini round4 accepted this integration on2026-10-13.
Its raw response is reviews/dd82/20261013_V3_n61_triples_final_review.json;
the reused local integration delta also passed, with imports explicit.

## Proof from an arbitrary original graph to the checked contradiction

1. Every vertex has degree8: a vertex of degree at most7 could reach at
   most1+7+7*7=57 vertices in distance at most2. The actual B is therefore
   a nonnegative integral symmetric matrix, with diagonal zero and row
   sum4. The complete inherited proof in CONNECTED_DEFECT_REDUCTION.md
   gives connected positive support, without a binary-defect, symmetry,
   equitable-partition or historical n62 assumption.

2. An entry4 would saturate the two corresponding rows and create a
   proper two-vertex B component. Thus no entry4 occurs. Suppose an
   entry B_uv=3 occurs. CONNECTED_TRIPLE_REPEAT_LOCAL.md treats all actual
   remaining unit-port positions: u,v are nonadjacent, share exactly
   four original neighbors, and their residual B ports coincide at w.
   The same proof gives the disjoint full61 partition
   {u,v}, S4, U4, V4, w, Ta5, Tb5, Tc6, Td6, Z24.

3. CONNECTED_TRIPLE_LAYER_INTERFACES.md derives the complete seven core
   neighborhoods and every imposed interlayer degree from the same
   actual A/B. Its handshaking argument leaves both cases: r,s in Z,
   or r=delta in Td and s=gamma in Tc. Both are retained. The independent
   label choices in CONNECTED_TRIPLE_FULL_GRAPH_MODEL.md normalize the
   U/V and Ta/Tb matchings and the Ta/Tc and Ta/Td bijections, while
   leaving both Tb/Tc and Tb/Td permutations variable.

4. CONNECTED_TRIPLE_GRID_NORMALIZATION.md uses real diameter-two
   coverage to prove F↔U and F↔V are bijections and every (Ta,U) cell in
   Z outside F has exactly one point. It then gives a compatible
   labeling of U,V,F and those20 Z points. All actual triple targets
   therefore satisfy the fixed U/Z and Ta/Z blocks; no C matrix, sigma
   permutation, V/Z incidence or graph automorphism is selected.

5. The reviewed encoder in computations/dd82/n61/triple_full61_run/
   and its reviewed grid wrapper in triple_full61_grid_run/ implement
   exactly this necessary model. Every unordered original vertex pair
   has its own A variable. All61 degrees equal8. All1830 pairs have the
   direct-edge or genuine common-neighbor clause, using59 auxiliaries
   each, with both directions of the actual two-edge conjunction.
   Conditional counts retain the two port cases under one Boolean.
   All remaining edge variables are free subject to these conditions.
   The hypothetical original graph, with the proved labeling, assigns
   every edge and all threshold/path auxiliaries their actual values,
   yielding a satisfying assignment of this specific CNF.

6. The actual grid CNF has151179 variables and484629 clauses. Its
   preparation record and direct clause comparison show all baseline
   clauses retained and exactly216 added fixed-adjacency units:196
   from the new coordinates and20 already-implied Ta/F zeros. CaDiCaL
   returned UNSAT (exit20) after18.810613 CPU/19.303201 wall seconds,
   with a39635178-byte LRAT proof. The independent installed lrat-trim
   checker read this exact CNF and proof, checked409043 proof clauses,
   and returned exit20 and `s VERIFIED` after0.472412 CPU/0.566906 wall
   seconds. Thus the CNF has no satisfying assignment, contradicting
   step5. No B_uv=3 can occur.

Together with step2 and the row4 bound, every B entry is0,1 or2. QED.

The proof of necessity does not use a SAT model with an independently
chosen B: B always derives from the same original A. Omitting an explicit
B-connectivity CNF constraint is harmless, because the arbitrary target
already has the inherited property and satisfies every encoded condition.

## Actual evidence and its boundaries

All runtime paths here are under `computations/dd82/n61/`:

- `triple_full61_run/CODE_REVIEW.md`: fresh isolated same-family source
  review of base semantics, branching, model decoding and checker exit.
- `triple_full61_grid_run/CODE_REVIEW.md`: explicitly reused delta review
  of the216 units, retained cases and correct output paths.
- `triple_full61_grid_run/{input.cnf,encoding.json,preparation_sanity.json}`:
  actual input, meaning and direct input comparison; no reconstruction
  or hypothetical input is substituted.
- `triple_full61_grid_run/{solver.log,proof.lrat,result.json}`: actual
  terminal solver evidence and the complete proof.
- `triple_full61_grid_run/{certificate_check.log,certificate_check.json}`:
  independent exact-input certificate verification.
- `reviews/dd82/proof-checker-n61-triple-local-20261013/PROOF_AUDIT.md`
  from the project root: local reduction, layers and grid reviewed in
  their actual scopes; fresh review followed by explicitly reused deltas.

The first unnormalized full61 trial returned UNKNOWN after47.010298
CPU/48.169828 wall seconds. Its partial LRAT is retained but is not used
as proof. The small(C,sigma) catalogue is also not an exclusion premise;
it only corrected earlier reviewer claims and did not restrict this CNF.
No old n62 search, certificate check or Lean task was repeated.

## Immediate mathematical consequences and open obligation

Each actual B row has one of the weighted patterns2+2,2+1+1,1+1+1+1.
An actual A nonedge has at most3 common neighbors. An actual A edge has
at most2 common neighbors. None of this proves B binary or excludes
connected row4 defect with double entries. The next order61 obligation
must address that remaining actual original-graph domain, not restart
the now closed triple-branch solver inputs.
