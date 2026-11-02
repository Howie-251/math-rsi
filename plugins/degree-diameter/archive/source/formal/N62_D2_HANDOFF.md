# Actual D2_MATCH exclusion — 2026-10-11

Completed `DegreeDiameter/N62D2.lean` and dedicated `ReviewN62D2.lean`. Shared entrypoint and STATUS were not edited by this worker.

The final original-graph theorem is:

```lean
no_n62_d2_match_template
    (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G)
    (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (h : D2MatchTemplate G r i j k w a) : False
```

`D2MatchTemplate` contains only actual adjacency/vertex conditions: three distinct root neighbors i,j,k; distinct external vertices w,a; root nonadjacency to w,a; w nonadjacent to a; independent root neighborhood; the exact parent sets {i,j,k} for w and {i,j} for a; and uniqueness of a root parent for each other external vertex. It contains no defect row, matrix equation, capacity inequality, class size, parity claim, triangle-free condition, or contradiction field.

The actual caller derives the complete proof chain:

1. Four saturated actual defect rows: r=2e_w+e_a, i=2e_j+e_k, j=2e_i+e_k, w=2e_r+e_a.
2. The five vertices i,j,k,w,a are triangle-free. A small general lemma obtains this from two distinct positive repeats at nonneighbors, using the already derived order-62 triangle row.
3. The third unit repeat c of a lies in the actual singleton-parent class Ck and is not adjacent to a. The k-row has no repeats on either N(i) or N(j).
4. Actual neighbor decompositions give |Ci|=|Cj|=5 and |Ck|=6. Parent uniqueness proves these classes disjoint.
5. Actual AB=BA entries give the class weight equations. Their finite sums saturate every Ci/Cj row: two units go to the opposite five-point class, one goes to Ck, and every other entry is zero. No capacity input is assumed.
6. Genuine common-neighbor counts give each Ci vertex exactly one original neighbor in Cj and Ck; each q in Ck satisfies A[a,q]+|N(q)∩Ci|=1 and the analogous Cj equation.
7. Double counting produces d in Ck adjacent to a, hence d≠c and d has no original neighbors in Ci or Ck. The c-exception formula supplies x in Ci with positive B[x,d], and x has an actual original neighbor y in Cj. Thus (AB)[y,d]>0, while the derived entire row support of y forces (BA)[y,d]=0, contradicting commutation.

The last step needs only absence of d-neighbors in Ci and Ck, so it does not separately use the paper's Cj absence conclusion. This is a simplification of the same argument, not an extra premise. No global simple-defect assumption, triple-repeat elimination, recovered finite template coverage, SAT calculation, or N59 matching-row condition is used.

Actual successful commands, each exit 0, at three threads:

```bash
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62D2
lake env lean ReviewN62D2.lean
```

Evidence:

- `logs/n62-d2-full-second.log` — successful complete module build.
- `logs/n62-d2-type-axiom-audit.log` — actual template and counted-class definitions, all sixteen public theorem types and their transitive axioms, and a compiled raw original-graph caller.

All sixteen audited theorems use only propext, Classical.choice, and Quot.sound. Source inspection found no sorry, native_decide, or new axiom. No hash or checksum was produced. Earlier compiler logs are retained as unsuccessful/intermediate attempts; only the above successful complete build and audit certify the final source. A few harmless unused-argument/deprecated-name warnings remain.

This excludes the actual D2_MATCH branch, not every graph of order 62. The remaining original-graph coverage and remaining double-repeat branches are separate obligations. Parent workflow owns shared integration, source-level cross-family review, and research-state updates. No dedicated n63–65 work was performed.
