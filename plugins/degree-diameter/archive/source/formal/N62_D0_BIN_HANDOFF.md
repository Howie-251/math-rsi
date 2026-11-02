# Actual D0_EDGE_BIN exclusion — 2026-10-11

Completed `DegreeDiameter/N62D0Bin.lean` and `ReviewN62D0Bin.lean`. Shared entrypoint and STATUS were not edited.

Final original-graph theorem:

```lean
no_n62_d0_edge_bin_template
    (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G)
    (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (h : D0EdgeBinTemplate G r i j k b d w a) : False
```

The template contains only actual vertex/adjacency/parent data. The five root neighbors i,j,k,b,d are distinct, the root neighborhood is independent, w has parents {i,j,k}, a has parents {b,d}, w~a, and every other external vertex has at most one root parent. The BIN choice is encoded by a genuine additional common neighbor `∃ t, t≠a ∧ w~t ∧ b~t`. Since a is already a common neighbor of w,b, this supplies the required local multiplicity. Root independence and the exceptional conditions force such a t into the ordinary parent class of b; no complete B row is assumed.

The bridge `bin_common_neighbor_of_unit_repeat` proves that the existing branch condition B[w,b]=1 at a distinct nonedge supplies exactly this adjacency witness. Thus the actual-parent template can be constructed from the recovered BIN choice without strengthening it to a new matrix certificate.

The actual proof derives B_r=2e_w+e_a and B_w=2e_r+e_b. It proves the entire restriction of B_i to the actual root neighborhood by counting genuine common neighbors: only j,k have value one. The actual row sum then supplies c outside the closed root neighborhood, distinct from w, and B_i=e_j+e_k+e_c. Commutation at (i,w) forces c not adjacent to w; the root and w rows force a~c and b~c. The resulting actual triangle a,b,c gives B[b,c]≥1. At (r,c), both i and b then contribute positive units to AB while the exact root row makes BA equal one, giving the contradiction.

Actual commands, each exit 0, with LEAN_NUM_THREADS=3 and RAYON_NUM_THREADS=3:

```bash
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62D0Bin
lake env lean ReviewN62D0Bin.lean
```

Evidence:

- `logs/n62-d0-bin-full-build.log` — successful complete build, 10 seconds.
- `logs/n62-d0-bin-type-axiom-audit.log` — actual template definition, all five public theorem types and transitive axioms, plus a compiled raw original-graph caller.

All five audited theorems use only propext, Classical.choice, and Quot.sound. Source inspection found no sorry, native_decide, or new axiom. Both the initial partial-source check and the first complete build succeeded; there was no failed BIN compiler attempt. No hash or checksum was generated.

This excludes D0_EDGE_BIN, not D0_EDGE_BOUT or every order-62 graph. The proof does not assume global simple defect, a complete repeat row, a capacity certificate, global triple-repeat elimination, or finite template coverage. Parent workflow owns shared integration, final-source cross-family review, and research-state updates. No dedicated n63–65 work was performed.
