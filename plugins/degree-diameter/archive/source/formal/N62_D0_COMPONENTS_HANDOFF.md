# Actual D0 closed components, 2026-10-11

Scope: `proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`, sections 1–2 only. The paper route passed parent-managed PASS32/B16. No global double-edge parity, classification, triple-repeat checker, D1 outlet, or universal order62 exclusion is claimed here.

`DegreeDiameter/N62D0Components.lean` imports the completed N62D0Bin chain. `D0ParentTemplate` contains only actual distinctness, adjacency, parent-set and ordinary-parent-uniqueness conditions. Its root neighborhood is independent, w has three parents i,j,k, and a has two distinct disjoint parents p,q. No defect row or counting certificate is a template field.

- `n62_d0_match_closed_component`: original degree/diameter/card62 hypotheses, the actual parent template and w nonadjacent a construct b. The conclusion contains six distinctness statements, all four actual defect rows, and all six original nonedges among r,w,b,a.
- `n62_d0_bout_closed_component`: the BOUT template adds w adjacent a, root-neighbor b outside the five parents, and two actual distinct common neighbors of w,b. The conclusion contains the same four actual rows and exactly the original matching edges rb and wa.
- `d0_bout_template_of_unit_repeat` is the complete semantic bridge from the actual branch condition B[w,b]=1 to that graph-only BOUT template. `bout_common_neighbors_of_unit_repeat` exposes its common-neighbor witness directly.
- `closedDoubleFour_no_external_repeat` explicitly gives B[v,x]=0 for every v among the four and every x outside them.

`ClosedDoubleFour G r w b a` expands to pairwise distinctness and the actual rows

    B[r] = 2 e_w + e_a
    B[w] = 2 e_r + e_b
    B[a] = 2 e_b + e_r
    B[b] = 2 e_a + e_w.

Proof refinements relative to the reviewed paper: in MATCH, commutation at (r,w) directly forces B[w,x]=0 for each root neighbor x, avoiding the five-class counting argument. In both branches, commutation at (i,a) directly forces a adjacent c_i; the three distinct c_i then give three actual common neighbors of a,b. The already proved edge-defect bound rules out a adjacent b. MATCH nonadjacency of w,b follows directly from commutation between the completed root and b rows, so no separate triangle-free lemma is needed.

Build/audit commands (Lean/mathlib 4.24, at most three threads):

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62D0Components
lake env lean ReviewN62D0Components.lean
```

Successful initial full build: `logs/n62-d0-components-full-first.log`.
Final build and dedicated audit: `logs/n62-d0-components-final-build.log` and `logs/n62-d0-components-type-axiom-audit.log`. The dedicated audit prints both input templates, the actual four-row definition, all seven exported types and their transitive axioms, and compiles raw MATCH and BOUT callers. All seven results depend only on propext, Classical.choice and Quot.sound. No sorry, new axiom or native_decide was introduced. Parent owns shared entry point, STATUS and final source review.
